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

The executable `verify.py` checks nine exact coefficients of the degree-eight transformed derivative polynomial, the coefficient comparison controlling the Descartes sign count, and rational evaluations at \(z=1/3,1/2,3/5,3/4,9/10,1\) for the sharpness witness. SymPy is required (`python verify.py`). The results certify identities and finite rational signs, not the universally quantified Descartes argument, which is supplied in the proof.

The scope is the geometric-vector trial lower bound for positive four-periodic geometric shifts, not the exact operator numerical radius. No independent audit has been performed.
