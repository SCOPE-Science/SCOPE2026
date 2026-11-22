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

The analytic proof reduces the smooth Green integral to five quadratic/fourth-order Fourier energy sums using integration by parts and the fact that a zero signed sum of at most four powers of an odd base \(\beta\ge7\) must pair frequencies. The passage to the nonrectifiable limit uses geometric convergence of the associated Jordan bodies, not direct differentiation of the limiting boundary. The packaged script numerically compares independent finite-truncation calculations and passes; it does not prove the infinite claims or establish historical priority.

Run: `python verify_inertia.py` (Python 3 and NumPy). The script makes no external connections.
