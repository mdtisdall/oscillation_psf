# default.nix

with import <nixpkgs> {};
stdenv.mkDerivation {
  name = "dev-environment";
  buildInputs = [
    python37
    python37Packages.virtualenv
    python37Packages.pip
    python37Packages.numpy
    python37Packages.pillow
    ];
}
