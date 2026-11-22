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

The accompanying `VERIFY.py` is a standard-library-only deterministic Python program. It checks critical values, full-lap endpoints, parity, the trapping inequality and the explicit expansion lower bound on six odd frequencies, plus illustrative finite orbit captures. It returned `PASS: 2807 finite checks; analytic theorems are separate` in the reviewed run. The global Lebesgue-null set assertion uses the standard analytic bounded-distortion theorem for uniformly expanding compact sets without interior, with its hypotheses supplied in RESULT.md. Sampled orbits cannot establish an almost-everywhere statement.

The source publication year and published date are grounded by the publisher's own public “Published” history field (2023-11-01); the issue-date entry differs and is not used as the earliest **verified publication** date. The source's full accessible HTML article was compared against the theorem. No independent audit or external certification has occurred.
