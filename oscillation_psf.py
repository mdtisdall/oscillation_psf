import numpy as np
from PIL import Image as im

## Make an image just using a simple distance mask
distance = (lambda x: np.add.outer(x,x))(np.arange(-256,256)**2)

distanceMask = np.ma.masked_less_equal(distance, 40)

data = np.zeros((512,512))

data[distanceMask.mask] = 1


## save the image
dataIm = im.fromarray(data)

dataIm.save('data.tif')


## create the k-space of the data
dataFourier = np.fft.ifftshift(np.fft.ifft2(np.fft.fftshift(data)))


## create the array of sample times
trTimes = np.arange(0, 512)
measTimes = np.arange(0, 512) / 1000 + 1/500

sampleTimes = np.add.outer(trTimes, measTimes)


## compute displacement of each sample, assuming periods from 1 TR to 4 TRs
displacements = 3 * np.sin(np.multiply.outer(1/np.arange(1,5), sampleTimes * 2 * np.pi))


## save the displacement maps for each sample as images 
for rate in range(0,4):
    displacementsIm = im.fromarray((displacements[rate] + 3) / 6)
    
    displacementsIm.save('displacements' + str(rate + 1) + '.tif')


## compute the x-direction k-space coordinates 
kCoords = np.linspace(-0.5,0.5,512)


## compute the point spread function that results from the displacements (first in k-space, then in image space) 
kernelsFourier = np.exp(-2j * np.pi * displacements * kCoords[None, None,:])

kernels = np.fft.fftshift(np.fft.fft2(kernelsFourier), (-2,-1))

## save the point spread functions as images 
for rate in range(0,4):
    kernel = np.abs(kernels[rate])
    kernelIm = im.fromarray(kernel / kernel.max()) 
    kernelIm.save('kernel' + str(rate + 1) + '.tif')


## compute the convolution of PSF and image as a multiplication in k-space
output = np.fft.fftshift(np.fft.fft2(kernelsFourier * dataFourier[None,:,:]), (-2, -1))


## save the resulting output images
for rate in range(0,4):
    outputMag = np.abs(output[rate])
    outputIm = im.fromarray(outputMag / outputMag.max())
    
    outputIm.save('output' + str(rate + 1) + '.tif')


