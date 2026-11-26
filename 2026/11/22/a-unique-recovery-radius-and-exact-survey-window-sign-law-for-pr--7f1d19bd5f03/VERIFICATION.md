---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The loss curve at fixed radius increases strictly from zero to infinity, with derivative J=mu+aN/(1+ahS)^2, giving a unique positive smooth S. With Q=aN/(1+ahS), implicit differentiation gives S'/S=(-d mu+(n-d)Q)/J and P'/P=Q[n-(d-n)ahS]/[(1+ahS)J]. If n>=d the latter is strictly positive; otherwise S falls strictly to zero, giving precisely one interior minimum when the source bracket is negative. At equality only the source derivative vanishes. For a trial density xS(0), x=exp(-dR), the arrival-minus-loss residual divided by xS(0)aN(0)>0 is 1/(1+y0)-z/(1+xy0), z=exp(-nR). Its sign is (1-z)+(x-z)y0, hence also the sign of P(R)-P(0). For n<d the cutoff Y has log derivative n/(1-exp(-nR))-(d-n)/(exp((d-n)R)-1)>0 since the two terms straddle 1/R. Its open endpoints are n/(d-n) and infinity. This establishes the sign law, boundary cases, unique return beyond the trough, and strict F0 cutoff by source balance. Independently solving the example equilibrium by bisection gives r_min=1.2220613022, P(r_min)=0.4242721190, P(2)=0.4464195167, P(2 log 4)=0.5, and P(4.7438645184)=0.6920159049. For replay, bisect the increasing loss-minus-arrival function on [0,F(r)/mu]. The finite diagnostic script was inspected, not executed; universal validity is analytic. The fraction is the fraction of equilibrium loss not due to predation, not a prediction of successful establishment.

## originality

PASS

Best of current knowledge: pass the joint classification and exact, strictly ordered source-to-endpoint cutoff, not the parent-centered exponential/Holling-II model, qualitative finite-window effects or an establishment-density criterion. The published model is credited as prior. No verified source supplies or supersedes the exact escape-fraction law; the foundational original's decisive passages could not be reread, so the comparison is explicitly bounded.

## value

PASS

For a standard mechanistic equilibrium and a motivated finite survey comparison, the law gives a directly usable separation: the survey extent alone can reverse the near-versus-far ordering with fixed biology and a fixed interior trough. It identifies the unique radius, the parameter regime in which such sensitivity is possible, and an equivalent source-arrival threshold, without confusing escape with recruitment or asserting field power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
