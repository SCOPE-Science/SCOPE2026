---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The exact construction is reproduced by `exact_tetra_slepian.py` with SymPy. It derives the cell edge parametrizations, decomposes each quartic into harmonic components, integrates the boundary terms symbolically, and compares all fifteen distinct matrix entries to exact expressions. It checks the trace \(5/4\), the two-by-two characteristic factors and the sharp eigenvalue ordering.

The separate `verify_tetra_numeric.py` integrates over the actual spherical triangle in axis-and-azimuth coordinates using adaptive quadrature. It confirms all twenty-five matrix entries to error below \(8\times10^{-11}\), and the spectrum to tolerance \(5\times10^{-9}\). The calculations are reproducible from the files, using SymPy for the first checker and NumPy/SciPy for the second. A finite quadrature is not used as an infinite proof.

The preceding statements concern checks of the present mathematical result; independent external mathematical audit has not been performed.
