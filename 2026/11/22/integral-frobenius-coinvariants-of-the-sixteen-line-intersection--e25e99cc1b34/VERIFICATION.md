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

# Verification

Run `python3 verify_clebsch.py` from the same directory with Python 3.9 or newer. This standalone executable checks the reconstruction of all sixteen exceptional-curve classes, their intersection matrix, all 1920 even signed permutations, and all 18 classwise arithmetic cokernels. It verifies Smith diagonals using actual integer-unimodular row and column transformations and checks the required divisibility. It also checks that equal line-orbit partitions can yield distinct integral groups.

Run `python3 crosscheck_sympy.py` with SymPy installed to reproduce the same table using SymPy's separate Smith-normal-form implementation. No third-party computer algebra is needed for the main proof and no downloaded data is needed in either program.

The tests are exhaustive for the finite Weyl action and are combined with the stated geometric blow-up identification and the right-exactness of coinvariants. The calculation does not prove fieldwise realizability of each class or any conclusion about Picard, Brauer, or Laplacian critical groups. There has been no independent mathematical audit.
