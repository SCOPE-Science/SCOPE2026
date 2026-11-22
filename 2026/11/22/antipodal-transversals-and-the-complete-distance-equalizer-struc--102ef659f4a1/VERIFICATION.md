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

# Reproducible finite checks

The graph is defined by the 20 vertices and 30 edges of \(GP(10,2)\), with outer and inner cycles/indexed spokes exactly as in `RESULT.md`. No external graph files or libraries are needed.

**Direct exhaustive test (C++17):**

```bash
c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct
./verify_direct
```

Expected deterministic output:

```
DISTANCE_PAIR_COUNTS 30 60 60 30 10
EQUALIZER_COUNTS 10:1024 11:5120 12:11520 13:15360 14:13440 15:8064 16:3360 17:960 18:180 19:20 20:1
FULL_TOTAL 59049
PASS
```

This checks graph-distance distributions, the antipodal distance identity, that all non-antipodal witness sets comprise two antipodal pairs, **all** potential distance-equalizer vertex subsets, the entire polynomial, and exact equality between the original definition and pair-hitting.

**Independent automorphisms, orbit census, mobility (Python standard library):**

```bash
python3 verify_symmetry.py
```

Expected deterministic output:

```
AUTOMORPHISMS 120
OPTIMUM_SETS 1024
AUTOMORPHISM_ORBITS 20 12:2 20:4 40:2 60:10 120:2
INDUCED_EDGE_HIST 3:20 4:60 5:72 6:120 7:240 8:240 9:120 10:72 11:60 12:20
TOKEN_JUMP_DEGREE 10 TOKEN_SLIDE_EDGES 0
PASS
```

The automorphism argument is exhaustive: the image of one oriented length-two path must be among exactly 120 such paths, and the path's three distance coordinates distinguish all 20 vertices, fixing each candidate map uniquely. All 120 maps are constructed and checked to preserve adjacency. The orbit list is therefore complete. The induced-edge histogram is an independent structural refinement of the minimum-set census, not necessary for the main theorem.

**Scope and limits.** These exact finite checks prove no statement about larger generalized Petersen graphs or absolute historical priority. Successful execution does not constitute external or independent mathematical certification. The scientific claims were reviewed against the supplied source code, outputs, and finite combinatorial proof.
