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

With the probability normalization, Fourier convolution gives exactly the stated gain J and the squared norm term. J tends to minus infinity as t approaches one at fixed r. For small r, bounding each positive Poisson term confines all fits with J>=1 to t<=2r/(1-r). In disk coordinates the Hessian there is -4I+O_a(r^2), so the sole optimizer is fixed by reflection and its real coordinate is r cos(a)+O_a(r^3)>0. For delta=1-r near zero, a competitor gives J-1 of order 1/delta with positive coefficient. Every global optimizer must therefore have one Poisson term of that order, forcing both 1-t and the distance to one source to be O(delta). The scaled penalty excludes (1-t)/delta near zero while the scaled positive terms stay bounded. On this compact scaled region the objective tends to 2(1+k)/((1+k)^2+s^2)-1/k, which has its unique maximum at (1+sqrt(2),0), of value 3-2sqrt(2) and with negative-definite Hessian. Cancelling delta in the rational expression gives an analytic extension locally; hence there is one critical branch per source, both attaining the global optimum by reflection. With K=2+sqrt(2), the near-source second derivative is asymptotic to -4/(K^3 delta^3) uniformly between zero and the optimal displacement h=o(delta), while the other derivative is asymptotic to -K delta sin(2a)/(1-cos(2a))^2. This gives the inward quartic shift with the claimed coefficient. Subtracting the gain from ||F||^2=1/(2 delta)+O_a(1) gives the stated error. The source check.py supplies integration and finite stationary diagnostics, not a global search; a separate stationary check at a=0.7 and delta=0.0025 gave (depth, h/delta^4, delta times error) about (2.41010,-48.8390,0.32800), approaching (2.41421,-48.58997,0.328427). The proof is the global certificate. Neither uniformity in a at its endpoints nor the number of intermediate transitions is established.

## originality

PASS

The supported distinct result is the joint endpoint classification for the normalized fit at fixed nonzero, nonantipodal separation, including the fitted radial depth, strictly inward angular drift, and the leading optimal error. The strongest compared primary and catalogue statements cover other center geometries. The judgment is bounded by the identified access and priority limitations.

## value

PASS

The result explains a forced change from the bisector to two global optima in a fixed-normalization projection problem where simply placing a fitted kernel on a source peak does not solve the optimization. The universal residual cost and depth describe the scale of the compression loss, and the fourth-order angular drift resolves how the distant source still influences a concentrated fit. The global localization and branch count give these expansions a concrete variational meaning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
