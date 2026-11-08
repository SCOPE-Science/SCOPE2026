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

# Reproducible checks

Run `python3 verify.py` with a standard Python 3 installation. The script builds each rook graph from row/column equality, directly enumerates every nonempty vertex subset in twelve instances, and tests connectivity and closed-neighborhood domination without consulting the classification. Inclusion-minimality is checked through every one-vertex deletion; this is sufficient for connected domination because any nonminimal connected dominating set contains a smaller connected dominating set, and a leaf outside that smaller connected subgraph can be removed while preserving both connectivity and domination. The script separately computes the claimed polynomial from Stirling-number recurrence and compares every coefficient to the exhaustive count.

Checked dimensions: `(2,2), (2,3), (2,4), (2,5), (2,6), (2,7), (3,3), (3,4), (3,5), (3,6), (4,4), (4,5)`.

Observed completion: `VERIFY_OK 12 1435460 7406`. The three integers are the number of instances, the number of tested nonempty subsets, and the number of inclusion-minimal connected dominating sets across all instances. Representative histograms: `(3,5): {3: 5, 4: 60, 5: 3, 6: 210}` and `(4,5): {4: 5, 5: 244, 6: 1380, 7: 3600}`.

Finite exhaustive checks do not prove the arbitrary-parameter statement. The mathematical proof uses the weighted matrix-tree identity, proved in `RESULT.md`, and a two-sided maximality argument. No independent mathematical audit has been performed.
