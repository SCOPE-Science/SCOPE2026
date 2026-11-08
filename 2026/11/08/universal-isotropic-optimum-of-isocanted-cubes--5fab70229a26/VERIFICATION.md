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

# Reproducibility and verification

The theorem is proved by an all-dimensional disintegration of normalized Lebesgue measure with respect to the coordinate spread, conditional interval moments, and exact symbolic differentiation. The proof explicitly covers every integer \(d\ge2\) and every finite real \(t\ge0\); numerical or computer enumeration is not used to infer an infinite-dimensional conclusion.

A separate verification file, `check_isocanted.py`, reconstructs the zonotope vertex set, computes boundary simplicial incidences with `scipy.spatial.ConvexHull`, and then integrates volumes and all quadratic moments with rational determinants (`fractions.Fraction`). Its numeric geometry step is used only to identify faces, and each resulting volume/moment comparison is exact-rational. The code independently checks 12 cases across dimensions two through four, integrating 592 facet simplices, including \(t=0\), the proposed minimizer \(t=1\), and both smaller and larger cant ratios. It also verifies three symbolic moment/differentiation identities using SymPy.

Run `python check_isocanted.py` using Python 3 with NumPy, SciPy, and SymPy. Observed output:

```
ISOCANTED_COVARIANCE_EXACT_CHECKS_PASSED 12 592 3
```

The triangulation is not assumed to prove a claim about all dimensions. The global derivative-sign proof is exact; the checker is a finite independent diagnostic. No external mathematical validation is claimed, and an earlier equivalent formula might exist beyond the inspected literature.
