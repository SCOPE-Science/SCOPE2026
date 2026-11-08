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

# Reproducibility and verification

The mathematical proof gives an all-parameter classification and does not require a finite computation for its validity. The two included standard-library scripts provide independently implemented finite cross-checks.

Run `python verify_balanced_multipartite_counts.py`: it constructs and iterates occupancy profiles and weights them by exact binomial multiplicities; all 19 tested parameter pairs are confirmed. The separate output is in `verify_balanced_multipartite_counts.out`.

Run `python verify_balanced_multipartite_direct.py`: it simulates binary majority on explicit labelled neighbor bitmasks for 11 graph sizes and checks every possible initial bitstring. It processes 124400 labelled configurations and reproduces both fixed and least-period-two counts exactly. The separate output is in `verify_balanced_multipartite_direct.out`.

The direct simulator tests graphs with up to 16 vertices. These tests cannot establish the infinite family; the proof relies on preservation of homogeneity, the two-phase tie equation, and exact counting of balanced assignments. Full-text priority comparison for the 1980 Goles–Olivos article remains incomplete. Independent validation has not been performed.
