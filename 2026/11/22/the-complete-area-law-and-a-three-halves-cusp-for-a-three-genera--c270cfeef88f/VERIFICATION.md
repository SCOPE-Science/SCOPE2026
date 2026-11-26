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

For three unit segments almost surely in distinct projective directions, the boundary has two edges of length one in each of the three directions; the determinant area formula has no extra factor for segments [0,u]. Relative to labelled direction 1 the remaining two angles are iid uniform mod pi, independent of direction 1. Sorting yields constant density 2/pi² in the (X,Y) gap coordinates, with W=pi-X-Y. The determinant sum is sin X+sin Y+sin W. At fixed X=x this is sin x+2 cos(x/2) sin(y+x/2), so solving the sine inequality between its endpoint and midpoint values gives the entire piecewise slice length. Each slice level set has zero length for 0<x<pi, so the law has no atoms. Concavity gives the unique maximum at equal gaps and the closed simplex gives infimum zero at the three corners; continuity and the positive interior density give the whole asserted support. At each corner the two small gaps r,s have A=2(r+s)+O((r+s)^3), sandwiching the sublevel triangle between sizes t/2+O(t^3). Its area is t²/8+O(t^4); the three corners and constant density give the coefficient and symmetric label. The rescaled corner domains converge in area to the same triangle, so the uniform conditional densities converge in total variation, and 2(r+s) on that limiting triangle is Beta(2,1). Near the maximum the quadratic deficit is sqrt(3)(u²+uv+v²)/2. The ellipse at deficit 1 has area 4pi/3; the positive Hessian confines the region to O(sqrt(h)), where the cubic remainder gives O(h^(3/2)) area error and symmetric-difference convergence of the rescaled regions. The normalized quadratic radial deficit is uniform. Finally, at a boundary contact use inward gap r and the other gaps (pi-r)/2±s; the coordinate Jacobian has absolute value one. Here A=sin r+2 cos(r/2) cos s. The local survival integral extended to r<0 is smooth in t near 2 because its normal derivative is positive. Restricting back to r>=0 subtracts the strip only for t=2-h, |2 sin(s/2)|<sqrt(h). With u=2 sin(s/2) its Jacobian tends to one; the inverse normal-coordinate lower limit is of size -(h-u²) times a smooth factor with value 1 at the contact. The strip area is 4h^(3/2)/3 plus O(h²); rescaling u by sqrt(h) gives a smooth bounded coefficient in sqrt(h) and hence a derivative term of order sqrt(h). There are three contacts; the interior level is regular and there are no other boundary crossings at level 2. This gives the negative symmetric-difference coefficient -8/pi² and a continuous first derivative but unbounded one-sided second derivative at 2. Parallelism means a zero gap and boundary area 2 sin x, whose maximum is 2. These are analytic checks of the full claim; the frozen numerical verifier was inspected, not run.

## originality

PASS

The model, determinant formula, circular-spacing framework, and deterministic extrema are not new. The supported distinction is the finite-three-direction threshold analysis, including the explicit cusp coefficient and marked limits, together with the explicit scalar quadrature. In particular the known equivalence to a triangle model must use its perimeter, not its area. Neither the inspected exact moment results nor large-generator laws give these threshold and marked statements. Historical priority for the quadrature alone is not established.

## value

PASS

The first non-parallelogram fixed-length zonogon gives a natural, small finite case not answered by large-sample limit theory. The largest parallel-pair area provides an intrinsic interior threshold, and the computed cusp shows a specific failure of twice differentiable survival there while excluding an atom. The two different marked endpoint geometries identify the configurations responsible for the tails. Those are useful exact distributional facts beyond a rescaling of a known expectation or an isolated numerical evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
