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

Run `python3 verify_ladder.py` from the directory holding these files. The checker constructs \(L_n\) from scratch, computes all distances via breadth-first search and independently lists every geodesic edge triple. It checks these against the four theoretical forbidden-triple patterns, then exhausts each of the \(2^{3n-2}\) edge subsets for \(2\le n\le7\), testing the exact face and inclusion-maximal polynomials, and compares separate symbolic counters for \(8\le n\le40\). The terminal assertion is `VERIFY_OK`.

Observed face totals for \(n=2,\ldots,7\): `16,73,233,634,1590,3807`; observed facet totals `1,7,20,42,75,121`. The all-order result follows from the proof in RESULT.md, not finite extrapolation. The method tests only ordinary undirected open two-rail ladders. Publication-priority and mathematical audit by an independent party have not been performed.
