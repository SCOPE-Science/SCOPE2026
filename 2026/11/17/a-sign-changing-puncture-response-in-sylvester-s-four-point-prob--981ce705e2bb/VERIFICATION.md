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

# Verification and reproducibility

The analytic derivation uses the exact line-coordinate Jacobian for two uniform points in the disk, a polynomial integral for anchored triangle area, the disjoint four-point containment alternative, and a total-variation expansion for deleting a disk. The circular cap estimate makes the near-boundary inequality strict without relying on numerical evaluation of the off-center triangle-containment integral.

To reproduce the numerical checks, install the dependencies in `requirements.txt` and execute `python check.py` using Python 3. The checker evaluates an independently parameterized one-dimensional angular integral for the fixed-point containment probability, compares it with direct random-triple simulation at three fixed radii (1,200,000 independent configurations at each), checks exact anchored-area constants, verifies three explicit near-boundary lower bounds, and confirms the asymptotic slope. The successful run printed `DISK_PUNCTURE_SYLVESTER_SIGN_REVERSAL_OK`.

Random sampling has finite precision and only corroborates the deterministic analysis. The proof is an ordinary self-contained written mathematical argument, not a machine-formalized certificate. Independent audit and independent historical verification have not been performed.
