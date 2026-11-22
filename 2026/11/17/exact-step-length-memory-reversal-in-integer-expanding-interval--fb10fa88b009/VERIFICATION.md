---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For every integer b>=2 the b full affine branches preserve Lebesgue measure. The observable f_b(x)=|T_b(x)-x| is coordinate-Euclidean and piecewise affine, not the shortest circle displacement. Direct branch integration yields mean (2b-1)/(6b) and lag-zero variance (2b^2-2b-1)/(36b^2). The Perron image of the centered f has a finite break-point piecewise-affine shape; its next image is exactly b^-2 times that centered shape. Integrating f*Pf supplies C_1=(b-4)(b-2)(b^2-b-1)/(180b^4), hence C_n=b^[-2(n-1)] C_1 for each positive lag. Stationary covariance summation gives variance (12b^4-24b^3+11b^2+6b-11)/(180b^2(b^2-1)), positive for b>=2. Summable Perron iterates give bounded Gordin coboundary and reverse-martingale difference, proving a nondegenerate CLT under stationary Lebesgue initial x. The initial endpoint conventions affect a null set only; zero covariance at b=2,4 does NOT assert stochastic independence. Independently integrated the product of exact affine branches at b=2..6 and lags 1,2 using rational three-interior-point quadratic quadrature, reproducing sign reversal b=3 and b>=5 and zeros b=2,4. These finite calculations corroborate, rather than replace, the general transfer identity and CLT argument.

## originality

PASS

PASS, best of knowledge: exact full-lag length-observable covariance, sharp integer-slope sign reversal and its rational nonzero CLT variance were not found in the materially read literature. They are not the earlier beta-map COORDINATE correlations or the preexisting general diffusion algorithm.

## value

PASS

Natural path-length fluctuation statistic for a standard expanding dynamical family; the unexpected complete disappearance of all positive-lag memory at b=2 and b=4, negative memory at 3, and positive memory thereafter is a parameter boundary with an exact Green–Kubo calibration. The CLT supplies a meaningful trajectory-level consequence, not merely a symbolic substitution or low-order variance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
