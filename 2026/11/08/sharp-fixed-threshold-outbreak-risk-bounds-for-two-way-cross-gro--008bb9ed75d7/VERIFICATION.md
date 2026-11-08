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

The accompanying `verification.py` is a standalone Python 3 standard-library checker. Execute `python3 verification.py` in the extracted package directory. Its successful output is:

```
PASS 1664 deterministic assertions; no random trials
```

It tests exact rational identities for expected total progeny under fixed offspring-rate product, exact coefficient inequalities to finite degree 120, 999 positive-curvature samples, high-precision numerical fixed-point residuals, supercritical sharp bounds and asymmetry monotonicity across several parameter values, and convergence toward the unattained infimum. For all-parameter claims, verify the complete proof in `RESULT.md`; these finite tests are diagnostics and cannot replace its infinite-domain coefficient and strict-concavity arguments.

Historical-priority screening compared full text of Ball et al. (2004), Rao and Bauch (2006), Alexander and Day (2010), and Aravinda et al. (2024), with limitations recorded in `AUDIT.json`. Independent mathematical audit has not been performed.
