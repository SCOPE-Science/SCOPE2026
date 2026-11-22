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

Analytic verification uses the moment-optimality condition, an elementary finite-Blaschke parametrization of every smallest-support design, the Christoffel diagonal weight identity, and strict monotonicity of the boundary argument of a finite Blaschke product. The root equations each have exactly one root in \((0,\pi)\), and the phase optimizer is unique because the closest-node distance has one strict maximum per phase period.

`check.py` is a reproducible finite diagnostic, not an infinite certificate. The tested positive parameters are \(a=0.2,0.5,0.85\), degrees \(1\le n\le12\), and six quadrature phases plus four competing phases for each extremum. High-degree scalar checks use \(n=1000,10000\). Claims for all positive \(a\), arbitrary degree, and phase uniqueness rely on the mathematical proof in RESULT.md.

The exact illustration with \(a=1/2\), \(n=2\) can also be checked by factoring the cubic node polynomial for \(\eta=\pm1\). Relative mass-optimum limits require fixed \(a\) as degree grows, not a coupled boundary regime.
