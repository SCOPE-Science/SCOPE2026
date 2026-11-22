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

The proof of the infinite family is analytical, based on an exact invariant decomposition and the sign of the quadratic roots in squared energy. The standalone `verify_star.py` is runnable with Python 3, NumPy and SymPy. It independently forms each matrix from the graph edges, checks symbolic four-site and trimer characteristic polynomials, checks the size-three nilpotent Jordan structure at the uncoupled threshold, and verifies 108 full weighted-star spectra numerically against the exact formula. Run `python verify_star.py` from a directory containing that file. Expected terminal line: `PT_STAR_CHECKS_PASSED 108 symbolic_charpoly_and_Jordan_passed`.

No finite test exhausts all real hopping strengths or star sizes. Historical priority and independent external validation have not been certified.
