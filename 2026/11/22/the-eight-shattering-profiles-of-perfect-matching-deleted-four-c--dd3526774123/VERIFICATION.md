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

# Finite reproducibility checks

The Python `check_matching_profiles.py` script uses only Python 3's standard library and derives all hypotheses from explicit independent-plus-dominating predicates. It enumerates all 272 cube perfect matchings, all 384 cube symmetries and every one of 65,536 possible support masks for a representative of each of eight orbits. It checks every coefficient, facet count, and the two global totals and ends with `PYTHON_Q4_MATCHING_SHATTER_PASS matchings=272 orbits=8 vc5=40 pure=16`.

The independently implemented `verify_q4_matching.cpp` requires only a C++17 compiler, uses a Bron–Kerbosch maximal-clique recursion in graph complements to derive concepts, and uses a bit-position trace encoding unlike the Python set intersections. It performs an independent orbit and complete-support enumeration, checks every enumerated coefficient and facet count and an explicit isomorphism to the generalized Petersen graph, and ends with `Q4_MATCHING_SHATTER_PASS matchings=272 orbits=8 vc5=40 pure=16`.

To reproduce: `python3 check_matching_profiles.py`; `g++ -std=c++17 -O2 verify_q4_matching.cpp -o verify && ./verify`. These are exhaustive finite checks of the precise 16-vertex object, not random sampling, computer-assisted infinite proofs, or independently administered formal verification. Numerical data and lexicographic matching representatives are in `orbit_data.json`. No claims about every dimension of the binary cube are established.
