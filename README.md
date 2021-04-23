# oscillation_psf.py

This is a simple python script, that just relies on the numpy and pillow libraries. It produces the following output files:

1. `data.tif` shows the output data if the object was still 
1. `output<n>.tif` shows the output data for oscillations of period `<n>`/TR
2. `kernel<n>.tif` shows the point spread function kernel for oscillations of period `<n>`/TR
3. `displacements<n>.tif` shows the displacement for each sample in k-space for oscillations of period `<n>`/TR 
