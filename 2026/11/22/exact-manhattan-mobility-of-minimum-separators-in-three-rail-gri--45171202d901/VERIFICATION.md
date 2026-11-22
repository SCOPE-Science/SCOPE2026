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

# Reproduction and scope

From a directory containing the delivered files run:

```sh
python3 grid_sep_exhaustive.py
python3 grid_sep_states.py
```

Only Python 3 standard-library modules are required. The first script constructs the original graph, independently checks all three-vertex candidate cuts and two-vertex non-cuts, constructs token-slide edges using actual graph adjacency, and verifies all pairwise graph distances for \(3\le n\le9\). The second independently builds the feasible coordinate graph and checks vertex and edge counts, connectivity, every graph distance, every eccentricity, radius and diameter for \(3\le n\le24\). The previously observed output from these exact source files is embedded in `verification_output.txt`.

The all-length proof is in `RESULT.md`. Finite checks cannot certify infinitely many lengths, and no external mathematical audit or formal proof checker is claimed.
