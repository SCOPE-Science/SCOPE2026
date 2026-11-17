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

# Verification record

Run `python check_tree_angles.py` in a standard Python 3 environment. No external files, remote services, or third-party libraries are necessary.

The script enumerates every Prüfer sequence for orders 3 through 6 (1,440 labeled trees), explicitly deletes all pairs of edges, computes the three surviving components, constructs exact rational facet normals, checks their annihilation of all noncorresponding root generators, and verifies the squared cosine and both sharp equality criteria. Sixty further deterministically sampled labeled trees have orders 7, 8, 12, 20 and 50.

Expected and observed output:

```
TREE_ZONOTOPE_DIHEDRAL_PASS exact_labelled_trees=1440 star_cases=18 balanced_degree2_cases=795 sampled_large_trees=60
```

The checker does not certify all trees of unrestricted order and does not establish historical priority. Those questions are addressed by the analytical proof and separate literature comparison, respectively. An independent mathematical audit has not been performed.
