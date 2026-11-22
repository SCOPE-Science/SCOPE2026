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

The exact algebraic checker is `checker.py` in this package. With Python 3 and SymPy installed, run `python3 checker.py` in the extracted directory. The checker recomputes all Fourier fourth-order collisions, the restricted stationary cubic, the transverse polynomial, the degree-five resultant factor, exact Sturm root isolation, and the subresultant sign certificates for both possible crossings. It independently checks the elementary small-radius estimate and representative numerical signs. The infinite-dimensional parameter range is proved in `RESULT.md`; sampling is not an exhaustive proof. No external or independent validation is claimed.
