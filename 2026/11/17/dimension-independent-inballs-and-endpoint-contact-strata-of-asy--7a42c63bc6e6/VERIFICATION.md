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

The theorem's infinite-dimensional validity is established analytically in `RESULT.md`, Steps 1–4. The independent computational diagnostic is embedded as `verify_twinned_mixed.py` and requires Python, NumPy and SciPy.

Run `python verify_twinned_mixed.py`. It enumerates source vertex configurations; normalizes facet hyperplanes computed by `scipy.spatial.ConvexHull` and compares them to the exact polar vertex list for dimensions 2 through 6. It also solves a separate linear program maximizing the Euclidean inscribed-ball radius with free center coordinates, and checks facet tangency at both segment endpoints and its midpoint. Analytic finite inequalities are checked through dimension seven. The expected final line, observed on the delivered source, is `TWINS_CUBE_SIMPLEX_INBALL_PASS`.

For dimensions 2, 3, 4, 5 and 6 respectively, the independent hull checks found 5, 13, 33, 81 and 193 facet hyperplanes; the maximized radii agree with \(1/\sqrt2\) to floating-point accuracy. Their contact counts (lower endpoint, interior, upper endpoint) were (3,2,4), (9,6,9), (24,12,16), (50,20,25), (90,30,36). These are finite corroborations, not an exhaustive proof over all dimensions.

Scientific limitations: no other polytope realization, non-Euclidean norm, or general pair of posets is covered. Historical priority is provisional. Independent mathematical audit has not been performed.
