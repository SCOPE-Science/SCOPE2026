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

The identities are proved for all finite simple labelled graphs with independent equal-probability site-retention marks. `verify.py` independently exhausts all labelled graphs on one through five vertices and all possible retained sets at two exact rational probabilities. It checks first moments, joint moments, the sign reconstruction, and the exhaustive distinction between graphs with a distance-two pair and disjoint unions of cliques. It also tests the two-root exceptional law for disjoint edges and a distinct second root for a triangle.

Run `python verify.py` with Python 3 standard library. The expected output begins `VERIFY_OK 102616`. The full all-order argument, the continuous parameter classification, and the statistical guarantee follow from the analytic proof; the finite checks do not certify these infinite statements on their own. There is no independent audit or empirical validation of the model on real networks.
