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

# Verification instructions and limitations

The included `verify_recursive.py` performs exhaustive Catalan recursion and exact \(\mathbb F_2\) column elimination on all diagonal monomials up to the proposed degree. The independent `verify_flips.py` builds all triangulations by legal flips and performs row-wise \(\mathbb F_2\) elimination, checking the Catalan counts and the explicit even/odd flip-cube obstruction. Use `python3 verify_recursive.py` and `python3 verify_flips.py` from the directory containing these files. No downloads or third-party packages are necessary.

Both programs ran successfully and asserted the full row rank at degrees \(1,1,2,2,3,3,4\) for polygons with \(4,5,6,7,8,9,10\) vertices. The derivation of the unbounded lower bound is algebraic and independent of computational enumeration. Finite-field full rank supplies a nonzero integer minor, which is sufficient for full real rank; the exact modulo-two intermediate ranks must not be mistaken for a complete complex- or real-rank census.

Only the self-contained finite computations and direct proofs listed here have been checked. Independent audit and independent validation have not been performed. The general upper-bound equality for larger polygons remains unproved.
