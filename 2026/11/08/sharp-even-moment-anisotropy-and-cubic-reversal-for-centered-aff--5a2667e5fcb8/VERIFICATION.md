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

# Reproducibility and limits

Run `python check_triangle_moments.py` in Python 3 with SymPy available. The program carries out exact symbolic comparisons for degrees zero through eighteen and checks the first nine even-moment profiles; it also verifies the real-root discriminant, one-variable absolute-cubic derivative factorization, equality directions and both sharp moment envelopes. The proof of every even order is the coefficient extraction from a rational generating series, rather than extrapolation from the finite checks. The exact divided-difference formula supplies the cubic absolute moment on every uniformly measured triangle; coincident vertex values follow by limits. No numerical experiments are used as an infinite proof and no independent audit was performed.
