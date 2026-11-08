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

# Reproduction and verification

Execute `python3 checker.py` with Python 3 and only standard-library dependencies. The program checks posterior-maximum masses on all distinct noiseless replicated strings for exhaustive small input words and truncated positive-geometric dwell vectors, the exact finite-box formula, and direct sums versus the Markov transition matrix. It also verifies candidate extrema for sample log-convex and log-concave dwell sequences by enumerating positive compositions of several totals. The algebraic transfer argument and the absolutely convergent infinite sums in `RESULT.md` establish the unbounded theorem; finite computation alone would not.

The all-parameter theorem assumes a known source, independent identical strictly positive dwell pmf, and an output that resolves source-state run boundaries. The independent-audit channel is unperformed.
