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

For the fixed cap and iid Exp(1) input, put z=exp(-h). Integration gives Var(F)=2z-z², Var(R)=1−2hz−z² and Cov(F,R)=hz−z(1−z), since FR=hF. The stationary store uses only past inputs. Writing D=Var(Q), N=Cov(Q_t,Q_{t+1}) and X=z[(1−a)h−(1+a)+z], the lag calculation gives N−aD=X and D=(1−a−2X)/(1+a)>0. Thus ρ−a=X/D, and ρ′=(1−a)X′/[(1+a)D²], with X′=z[2(1−z)−(1−a)h]. The first bracket in X is strictly convex, starts negative and has one positive zero h_c. The bracket in X′ is strictly concave, starts at zero with positive slope and eventually becomes negative, so there is a unique positive h_*. At h_c that last bracket equals 1−a−z>0, the derivative of the first bracket at its crossing. Hence h_c<h_*. For lag k≥1, only S_t and R_t carry covariance forward, multiplying the lag-one value by a^(k−1); the limits 0 and a follow by L² convergence of the routed inputs. Independent moment quadrature and bisection at a=1/2 corroborate h_c≈2.888703356193, h_*≈3.920690394873 and ρ(h_*)≈0.529692482. These numerical values are checks, not a proof of the quantifiers.

## originality

PASS

Credit is limited to the exact threshold-dependent classification for this routing model, not annual hydrological memory, linear-store covariance, or nonlinear input partitioning in general. The strongest distinct catalog evidence uses a pollutant wash-off model rather than this rainfall split; the available literature evidence does not demonstrate the exact thresholds. This is a best-of-knowledge decision under the noted access limits.

## value

PASS

The conservation-law model isolates how contemporaneous fast-flow/recharge covariance can lift output correlation above storage retention even with white rainfall. The two exact caps distinguish onset from optimal overshoot, and the same optimum applies at all positive lags. This supplies a precise benchmark for inference from output persistence, not a claim about prevalence in watersheds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
