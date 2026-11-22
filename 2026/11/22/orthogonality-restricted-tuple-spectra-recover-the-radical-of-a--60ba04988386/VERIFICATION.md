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
# Reproducible finite verification

With a C++17 compiler and Python 3, run `g++ -O3 -std=c++17 -o verifier verify.cpp && ./verifier` and `python3 verify_general.py` in the directory holding the embedded files. Recorded exact output files are `verify_cpp.out` and `verify_general.out`.

The C++ program independently enumerates admissible pairs in explicit nondegenerate alternating ambient spaces over \(\mathbb F_2\) and \(\mathbb F_3\), grouping complete types by the kernel of their linear relation map and all bilinear pairings with a fixed basis of the named subspace. The eight finite cases include \((q,d,\rho)=(2,2,0)\), \((2,2,2)\), \((2,3,1)\), \((2,3,3)\), \((3,2,0)\). The larger ambient dimension for the three-dimensional radical test prevents false finite-horizon collapse. The final output line must be `FINITE_SYMPLECTIC_SIGNATURES_PASS`.

The Python program independently counts low-rank finite maps and isotropic image strata for all tuple arities through four in eight finite cases, compares their contributions with the full Gaussian expression, and ends `GAUSSIAN_ISOTROPIC_SPECTRUM_PASS`.

These programs support normalization and small-case verification, not completeness for every field or tuple arity. That generality rests on the written orbit classification and finite Gaussian counting proof. Independent mathematical audit is not yet performed.
