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

Run `python3 verify_clades.py` with Python 3.10 or later. The checker constructs binary tree cluster sets by recursively splitting the labeled ground set, enumerates every subset of those clusters for two through six taxa, and compares the full Boolean traces against all concept trees. It independently derives the face coefficients using the recurrence for partitions into blocks of size at least two and compares the resulting polynomial with the complete set of supported faces.

The checker also computes the exact Littlestone rank by two-sided branching on concept subsets: every positive hierarchy is tested through four leaves, and histories with at least two positives are tested on five leaves. The finite-check marker is `PHYLO_CLADE_SHATTER_PASS` with totals of 3019 laminar supports and 241 positive-history online cases. The proof's avoidance lemma, hierarchy refinement argument, and all-positive-path upper bound establish the general theorem; no finite computation is presented as an infinite certificate.

The count of abstract laminar faces uses classical hierarchical tree enumeration. The unconditional VC and Littlestone dimensions were established previously and are not claimed as new; novelty is assessed only for the complete shattering characterization, face-count interpretation and positive-history conditional capacity relative to documented prior comparisons; external independent mathematical assessment is not provided.
