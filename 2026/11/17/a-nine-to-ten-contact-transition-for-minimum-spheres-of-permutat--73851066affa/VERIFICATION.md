---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each k=2..10 the image of the Birkhoff polytope is the convex hull of its k! permutation X-rays in ambient unnormalized Euclidean coordinates. The k disjoint-support cyclic X-rays Z_j have squared norms h_j=(k-j)²+j². Active subset J_k is all shifts for k<=9 and excludes j=5 at k=10; positive w_j=(1-t_k/h_j)/2, t_k=(|J|-2)/(sum_J 1/h_j), yield barycentric center C and equal active squared distance R²=t+||C||². Weighted mean-squared-distance identity proves optimality and unique center once containment holds. Independently implemented exact rational weight construction and independent C++ integer-arithmetic enumeration of all permutations for every k=2..10: at k=10 all 3,628,800 permutations verified, exactly nine equality permutations and nine distinct X-rays; all noncontacts strictly inside (minimum positive scaled slack 4,274,850). Checked all 9 exact rational radii, notably R_10²=235064670/3593269. This finite EXHAUSTIVE certificate proves the entire stated finite range and claims nothing for k>=11.

## originality

PASS

The 2026 source on facets of permutation X-ray images studies linear inequality/facet structure rather than the Euclidean minimax enclosing ball. The published all-order X-ray diameter theorem concerns pairwise distances and yields only R²>=diam²/4; already for k=3 this is 7/2 versus the exact 98/23. Related circumradius/contact transitions for partial permutohedra and other polytopes concern different images. No covering result identified in source material; original X-ray article full text could not be obtained and old unindexed metric calculations remain a priority risk.

## value

PASS

The finite classification reaches a natural first combinatorial-geometry contact transition: all k cyclic-shift X-rays are extremal through k=9 but one becomes strictly interior at k=10. Exact rational optimal balls, complete equality classification and a reproducible exhaustive proof distinguish the new polytope’s metric geometry from existing facet and diameter data. It is meaningful finite mathematical information, not claimed to solve arbitrary k.

The dated certificate retains the supplied scientific assessment, sources and limitations.
