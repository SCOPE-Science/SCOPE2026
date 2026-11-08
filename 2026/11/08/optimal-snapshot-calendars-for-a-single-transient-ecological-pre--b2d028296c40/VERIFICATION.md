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

# Reproducibility and scientific verification

Run `python verify_timed_presence.py` with Python 3 standard library. The script deterministically checks the detection integral against numerical quadrature, the scalar optimization recurrence, independent random schedules, the exact rational rate-ratio-two family, and finite diagnostics of the all-size asymptotic statements. In its supplied form it reports 9,032 passing assertions.

The actual proof of uniqueness and all-count asymptotics is in RESULT.md. Numerical tests do not establish infinite-domain results. External independent review or validation has not been performed; first-discovery priority remains uncertain where relevant primary text was inaccessible.
