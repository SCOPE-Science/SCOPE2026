---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: Euclidean farthest corners decouple into d copies of f(t)=lambda t-(1-lambda) for t>=0 and lambda t+(1-lambda) otherwise. After a finite first sign switch each coordinate alternates, with period-two values ±(1-lambda)/(1+lambda), so 2^(d-1) antipodal d-dimensional cycles; coordinate sign-reflection symmetry gives basin measure 2^(1-d) away from null ties. For |X_i| uniform, tau_i=ceil(log(1+|X_i|)/delta) almost surely, delta=-log lambda, giving exact CDF [min(1,e^(n delta)-1)]^d for n>=1. As d→∞, maximum uniform deficit d(1-M_d)→Exp(1), yielding 2d(log2-delta H_d)→Exp(1) if d delta→0. For d delta→gamma>0 and fractional phase r, ceiling convergence yields CDF exp[-2gamma(r-k)_+] and the frozen r>0 endpoint when d delta→infinity. Explicit tie convention is necessary for all-point dynamics, but law is almost sure.

## originality

PASS

PASS best of knowledge. Abdulaziz (2024) treats farthest-vertex contractions on planar polygons and establishes even-vertex two-cycle behavior; the submitted hypercube coordinate product and especially the last-coordinate settling-time distribution and scaling crossover are not its results. The exponential limit of maxima of uniform variables is textbook, but exact arithmetic-dependent lattice transition for this natural dynamics is a separate implication. Resultary search found no stronger same-contraction settling-time classification.

## value

PASS

PASS: The last initial sign change is a natural exact settling statistic of a piecewise contraction. Its continuum versus lattice crossover occurs at the sharp dimension-contraction scale d delta≈1, and the limiting law depends on fractional arithmetic phase. It is a nontrivial finite-to-asymptotic classification, not simply restating the known two-cycle existence theorem or presenting finite experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
