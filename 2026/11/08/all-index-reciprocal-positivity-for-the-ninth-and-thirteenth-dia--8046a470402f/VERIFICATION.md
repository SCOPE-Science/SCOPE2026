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

# Reproducibility

From the folder containing `positivity_certificate.py`, run:

```sh
python3 positivity_certificate.py
```

The verifier uses the Python standard library only and recomputes normalized Padé coefficients from factorials. Its rational checks locate all 9 and 13 poles by disjoint radius-1/1000 Rouché disks, prove negative real-pole derivative and unique pole-modulus dominance, establish rational upper bounds on nonreal residue sums, and compute exact positive Taylor coefficients before the cutoffs. It reports cutoff index 44 for degree 9 and 105 for degree 13, followed by `CERTIFICATE_OK`.

The printed decimal tail ratios are display approximations to already-verified strict *exact rational* inequalities. Numerical root centers merely specify rational disks; no approximate root-finding result is assumed. The certificate does not prove coefficient positivity at untested degrees, correctness of floating-point matrix exponential implementations, or independent audit status.
