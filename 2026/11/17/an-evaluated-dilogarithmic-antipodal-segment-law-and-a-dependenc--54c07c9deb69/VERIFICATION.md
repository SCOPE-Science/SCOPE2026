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

PASS. Three circle-uniform vertices conditioned on a unique upper vertex yield two independent lower angular tails. The chord x=sin(phi+psi)/(sin(phi)+sin(psi)) strictly decreases in psi; the two disjoint assignments to crossing tails give J(r)=12/pi^3 integral_0^(pi/2) atan(q tan t)atan(q cot t)dt, q=(1-r)/(1+r). Absolute sine-series convergence for each r<1 and orthogonality give J=1/4+6 Li_2(-r)/pi^2-3 Li_2(-r^2)/pi^2. Differentiation yields J_prime=6 log((1+r^2)/(1+r))/(pi^2 r)<0, and integrating at r=1 gives J~3(1-r)^2/(2pi^2). With known one-site p(r)=1/4-3 Li_2(r^2)/(2pi^2), p~3(1-r)log(1/(1-r))/pi^2; covariance is +3/16 at center, negative near one, hence at least one sign change. Independent high-precision quadrature compared with dilogarithmic formula at r=0,0.2,0.7,0.98 to ~1e-15; this is corroboration, the Fourier argument is the proof. No uniqueness of sign-change root follows.

## originality

PASS

PASS best of knowledge. General segment inclusion already had an explicit integral in a 2019 source, and both central 1/4 and exact one-site marginal are earlier. The surviving contribution is a closed three-dilogarithm evaluation for the exact antipodal joint law, its quadratic endpoint coefficient and correlation reversal; no inspected earlier statement implies this evaluated identity and dependence comparison without new calculation. Priority of an unpublished evaluation of the 2019 general integral remains a real risk.

## value

PASS

PASS. Joint capture correlations of two prescribed targets by the SAME random convex hull are geometrically natural; the explicit closed special-function law and sharp positive-to-negative dependence transition are quantitatively informative beyond an uncomputed multi-integral, not a parameter rename. The result is limited to three independent circle-boundary vertices and exactly antipodal targets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
