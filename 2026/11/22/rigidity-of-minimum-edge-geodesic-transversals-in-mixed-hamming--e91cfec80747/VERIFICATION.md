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

# Verification of the coordinate rigidity theorem

The all-dimensional proof is in `RESULT.md` and rests on two mathematically independent arguments: a probability-average lower bound and two exact-one path-exchange equalities on every coordinate square. The latter imply constant edge indicators on coordinate classes. Tests do not substitute for those proofs.

Run from this directory:

```
python3 verify_hamming_geodesic.py
```

The checker independently builds labelled coordinate graphs and enumerates all maximal geodesics as paths between tuples differing in every coordinate, then enumerates every edge subset of the proposed minimum size for seven small factor tuples. It verifies both the count and the exact edge members against the coordinate-class classification. It also checks that every coordinate class hits each maximal path exactly once on five larger tuples. The final expected marker is `VERIFY_OK`.

Exhaustive cases include mixed alphabets \((2,3)\), \((3,3)\), and \((2,2,3)\), not just binary cubes. There is no claim of exhaustive computation at arbitrary order; the general theorem rests on the written proof. Independent validation remains unperformed.
