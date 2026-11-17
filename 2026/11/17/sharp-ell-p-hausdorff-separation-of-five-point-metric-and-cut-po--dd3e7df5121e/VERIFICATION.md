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

# Verification details

Execute `python3 check_metric5.py` using Python 3 and `sympy` (optional `numpy` and `scipy` for the independent numerical candidate census). The observed exact output was:

`MET5_CUT5_EXACT_PASS inequality_count=40 cuts=16 anticuts=16 rank=10 maximum_cut_size=6 projection_squared_distance=2/45 unique_anticut_residuals=16 numerical_vertex_census=32_matched`

The program evaluates exact `Fraction` coordinates, all forty triangle/perimeter inequalities, active-normal ranks, all sixteen switched mixtures, the ten maximum-cut averaging identities and Euclidean projection normal certificates. For all \(1\le p\le\infty\), exactness is established analytically by Hölder and equality in the finite family of primal vertex inequalities. The assertion that these are all vertices relies on Laurent (1996, §4.3) and is not inferred from numerical Qhull. The optional Qhull run independently enumerated the same 32 candidate vertices but is floating-point only. No exhaustive numerical search of every real \(p\) was attempted or needed. All results concern one coordinate per unordered edge. Independent mathematical audit has not been performed.
