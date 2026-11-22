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

# Reproducible checks

The necessary standalone files are `verify_exact.py` and `verify_milp.py`. The first uses only Python 3 standard-library operations and performs an exhaustive exact search over every permitted binary word of lengths one through nine. The graph search uses integer masks and logically valid proper-coloring upper bounds; no floating-point numerical evidence is needed to prove the finite maximum. The second constructs independent one-deletion output incidence constraints using SciPy's integer-programming interface. A numerical MILP optimum alone is not treated as proof.

Executed commands:

```
python3 verify_exact.py
python3 verify_milp.py
```

Observed exact checker output:

```
n=1 source=2 optimum=1 largest_VT_intersection=1 nodes=2
n=2 source=4 optimum=2 largest_VT_intersection=2 nodes=3
n=3 source=6 optimum=2 largest_VT_intersection=2 nodes=3
n=4 source=10 optimum=3 largest_VT_intersection=3 nodes=4
n=5 source=16 optimum=3 largest_VT_intersection=3 nodes=6
n=6 source=26 optimum=6 largest_VT_intersection=6 nodes=7
n=7 source=42 optimum=6 largest_VT_intersection=6 nodes=77
n=8 source=68 optimum=10 largest_VT_intersection=10 nodes=158
n=9 source=110 optimum=13 largest_VT_intersection=12 nodes=14968
length_nine_witness=001001011,001010100,001101101,010011010,010110011,011001001,011010110,100100110,101010101,101101100,110010100,110011011,110110010
PASS: optimum 13 at length nine; first strict gap from VT intersections
```

Observed independent integer-programming output:

```
n=7, sources=42, outputs=56, optimum=6
n=8, sources=68, outputs=102, optimum=10
n=9, sources=110, outputs=184, optimum=13
PASS: independent integer-optimization formulation
```

The most important nonstandard computational inference, the absence of a 14-word code, follows from exhaustive branching in `maximum_clique` using a proper graph-color bound. The complete program verifies the returned thirteen-word witness pairwise. The finite search does not assert anything about longer input words or priority in unindexed publications.
