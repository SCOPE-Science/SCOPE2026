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

# Verification of the two-season survival-kernel theorem

`checker.py` reproduces exact symbolic periodicity and integral identities and numerical comparisons with piecewise ODE integration; it tests the unique crossing and small-season Taylor coefficient. The theorem's monotonicity is proved analytically using the strict increase of \(\coth z-1/z\)), not by finite sampling. The full-source priority comparison is necessarily literature-bounded; source access and historical risks are described in `REVIEW.md`. There has been no independent scientific audit.
