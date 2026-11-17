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

# Reproducibility and exact checks

Run `python check_pentasm.py` alongside this document using Python 3; no external packages are required for that exact checker. It constructs all \(2d+2\) Minkowski endpoint candidates for each input, checks the claimed radius, all four positive clearance classes (including the nonvertex endpoint), strict positivity of all positive barycentric weights and their sum, the exact center barycenter, and all unordered vertex pairs against the full diameter equality list.

**Executed and passed:** \(220\) instances, \(3\le d\le24\) and ten positive rational scalar values \(t\in\{1/29,1/7,1/3,1/2,1,5/3,2,13/5,10,57\}\), with \(110220\) exact rational endpoint/distance comparisons. A separate one-off `scipy.spatial.ConvexHull` vertex census confirmed the enumeration for dimensions \(3\) through \(7\), at \(t=1/5,1,17/10\), a total of \(15\) hulls. The independently evaluated radius and contact groups agreed for all tested configurations.

The unrestricted mathematical theorem is instead certified *within the proof* by the equal-distance algebra, the positive contact-barycenter certificate, the exact noncontact squared clearances, and the exhaustive symbolic vertex-type distance bounds. No finite checker proves the all-real-parameter and all-dimension quantifiers by itself. No formal theorem prover or independent scientific audit was used.
