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

Run `python3 verify.py` with Python 3.9 or later. It uses only the standard library. The code exhausts all labelled graphs on 2, 3, 4 and 5 vertices and all orientations of their edges. Exact integer identities check means, variances, third centered moments and weighted versions. Triangle indicator marginals, pairwise joints and every distinct-triangle triple joint are also tested, with the exact tetrahedral exception.

Expected output starts `PASS: 1098 labelled graphs (n=2..5), 1004 distinct-triangle triples`. The finite checks do not prove the infinite family; the human-readable Walsh and incidence argument is the proof. No independent audit has been performed.
