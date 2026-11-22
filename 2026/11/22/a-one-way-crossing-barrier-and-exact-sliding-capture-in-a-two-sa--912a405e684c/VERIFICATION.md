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

# Verification of the stated one-way crossing and sliding theorem

The mathematical proof in `RESULT.md` establishes the conclusions by global normal-sign arguments, explicit diagonalizations and a one-dimensional sign analysis. The companion `CHECK.py` uses Python 3 and SymPy to verify exact first-integral invariance, eigenvalues, flow formulae, contact heights, interface normal signs, golden-ratio flight identities, the Filippov rational vector field and its hyperbolic equilibrium. Finite interior-point tests of both arcs are additional diagnostics, not substitutes for the analytic all-time sign proofs.

Execute:

```bash
python CHECK.py
```

The observed run produced `ONE_WAY_FILIPPOV_VERIFY_OK`. It checks the published benchmark parameter and the symbolic parameter-general normal fields, but it cannot certify publication priority or make claims outside the stated crossing and sliding domains. The no-crossing theorem does not exclude periodic Filippov trajectories that contain a sliding segment.
