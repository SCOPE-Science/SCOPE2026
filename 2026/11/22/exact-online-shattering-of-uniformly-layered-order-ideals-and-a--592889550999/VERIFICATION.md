---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

An ideal is empty or is specified by its last nonempty level and a nonempty subset of that level; all strictly lower levels are full. This gives 1+h(2^w−1), and exactly the antichains can be shattered. The one-point extension above any such ideal realizes the strict-order trace over the named finite poset. The critical online recurrence is exact: a query in a full cube at position j leaves the earlier or later full cubes with one additional (w−1)-cube at the cut and possibly the outer boundary cube. At zero full cubes, one boundary cube has rank w−1 and two have the same rank by width induction. With t≥1 full cubes, querying an end boundary has an outer branch of rank w−2; a full-cube query gives minimum residual rank w−1+floor(log2 min(j,t−j+1)), maximized at a middle cube. This proves the formula for all w,h, with w=1 given by threshold search. For s=floor(log2(h+1)), the counting bound lies between w−1+s and w+s; at h=1–4 substitution gives no deficit, and at h=5 the interval 2^(w+2)≤5·2^w−4<2^(w+3) gives the first deficit for every w≥2. RESULT.md lines 15–51 is the all-parameter proof. The supplied verify.py and verification_output.txt were inspected; their finite checks were not rerun and are not needed for the induction.

## originality

PASS

Best-of-knowledge pass for the uniform layered closed rank and sharp five-level entropy boundary, not for the general ideal-rank recurrence, VC-width equality, or the threshold rank of a chain. The closest broader exact algorithm requires a separate analysis to solve its recurrence on this family. Distinct same-day results inspected do not supply that solution.

## value

PASS

The result supplies an exact online benchmark in a natural class of fixed-width posets, including the first place a realizable decision tree must lose a bit relative to the number of ideals. The rank stability under small boundary cubes explains that loss and is more informative than tabulating ranks or just observing a static/online separation on chains. Scope is uniform positive widths and finite traces only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
