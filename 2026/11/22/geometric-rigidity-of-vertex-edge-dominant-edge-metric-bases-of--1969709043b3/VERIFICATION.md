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

# Reproducible exact verification

The two source files are standalone and are fully included with this result. Their standard-library-only tests reproduce the complete finite census for dimensions \(2\) through \(5\). They test every vertex subset at cardinalities \(d-1\) and \(d\), and separately exclude edge-resolving sets with \(d-2\) vertices for \(d=4,5\). They compare the entire accepted-set collection with the independently generated geometric families.

```sh
python3 verify_independent.py
g++ -std=c++17 -O2 verify_masks.cpp -o verify_masks
./verify_masks
```

The recorded successful runs returned the following values in both implementations:

| Dimension | Edge-resolving sets of size \(d-1\) | Vertex-edge-dominating sets of size \(d-1\) | Joint sets of size \(d-1\) | Joint sets of size \(d\) |
|---|---:|---:|---:|---:|
| 2 | 0 | 4 | 0 | 4 |
| 3 | 0 | 16 | 0 | 32 |
| 4 | 64 | 112 | 0 | 176 |
| 5 | 1280 | 80 | 0 | 160 |

They returned `family_equal=True` / `family_equal=true` at all four dimensions and the respective tokens `CUBE_VE_EDGE_PY_OK` and `CUBE_VE_EDGE_CPP_OK`. All set comparisons are exact; no randomized or approximate calculation is used.

The results do not cover higher dimensions. No independent audit or external certification is claimed.
