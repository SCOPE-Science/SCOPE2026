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
# Reproducibility and checks

Two complete executable scripts accompany the proof. Execute `python3 verification/enumerate_matchings.py` and `python3 verification/independent_edges.py` from the package root. Their printed JSON must match the corresponding `.out` file byte-for-byte. The programs do not require external packages.

The first exhausts all maximal matchings by a vertex-state recursion, checks \(192\) size-six optimizers, compares every unordered optimizer pair, and BFS-traverses the entire exchange graph from all \(192\) roots. Its spectrum also includes \(1536\) size-seven maximal matchings and \(272\) perfect matchings.

The second independently scans \(\binom{32}{5}=201,376\) five-edge candidates and \(\binom{32}{6}=906,192\) six-edge candidates, tests pairwise vertex disjointness and unmatched independence, and applies all \(384\) hypercube automorphisms. It independently computes orbit edge-pair types and the all-pairs diameter. These are exhaustive finite checks, not statistical tests or proof of any conjecture for arbitrary dimension.

The two implementations share elementary mathematical definitions of the same graph and parameter; their agreement is not independent scholarly validation. The requirement that intermediate single-edge states also be optimal is deliberately **not** imposed on a simultaneous two-edge exchange. Source coverage and historical priority remain limited by accessible literature.
