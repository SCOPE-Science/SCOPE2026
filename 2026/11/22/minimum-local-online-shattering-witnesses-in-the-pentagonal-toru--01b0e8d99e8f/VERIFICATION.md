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

# Reproducible exact checks

From the directory containing the four standalone artifacts, execute:

```sh
python3 verify_census.py
c++ -std=c++17 -O2 verify_census.cpp -o verify_census
./verify_census
```

Expected output fragments are `PYTHON_PENTAGONAL_CENSUS_PASS rooted=84 total=2050 orbits=12 VC=2` and `PENTAGONAL_LOCAL_ONLINE_PASS rooted=84 count=2050 root_pairs=2100 roots_1=2000 roots_2=50 orbits=12 orbit_200=9 orbit_100=2 orbit_50=1`.

The first program uses a direct quadratic-distance predicate, all 1140 rooted subsets and a recursive binary decision-tree trace definition; it recomputes local VC dimension, verifies the twelve complete group orbits and checks eight explicit leaf witnesses in `witness_tree.json`. The second program independently constructs adjacency and uses an explicit four-center 2-versus-2 splitting test. The finite search is exhaustive only **because** every eight-point depth-three support must contain some possible root and its complete four-neighbor set. The proof of that reduction, together with the exact recurrence, is in RESULT.md. No larger-case extrapolation or independent mathematical audit is claimed.
