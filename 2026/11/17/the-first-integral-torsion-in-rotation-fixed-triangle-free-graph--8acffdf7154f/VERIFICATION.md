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
# Reproducibility and boundaries

Run `python verify_trianglefree_fixed.py` with `sympy==1.14.0`, as specified in `requirements.txt`. The script independently checks two equivalent definitions of faces: enumeration of unordered graph-vertex triples and enumeration of sum-free triples of signed step differences. Both are evaluated for every subset of each distance set up to graph order 21. It then computes integer Smith normal forms for every simplicial boundary matrix. Nonzero Smith factors are all units through order 20; at order 21 the second boundary has seventeen unit factors and a single factor two.

At order 21, the checker separately verifies all 18 facets, all vertex links as six-cycles, all edges in exactly two triangles, connectivity, and inconsistency of global facet orientations. The printed line `TRIANGLE_FREE_CYCLIC_FIXED_INTEGRAL_21_PASS` appears at the end of a successful exact run. The full captured output is stored in `verification_output.txt`.

The exhaustive finite checks establish the precise claimed cutoff and surface identification; none of the calculations claims to cover graph orders 22 or larger. Dependencies are external standard libraries, not hidden mathematical input files.
