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

# Reproduction of the analytic proof

The theorem is an analytic theorem, not a conjecture based on computational results. The crucial steps to check are (i) conditional binomial occupancy conditional on no common shock, (ii) the telescoping derivative of the binomial tail, (iii) monotonicity of its elasticity, (iv) the integral representation of the normalized log survival ratio and strict endpoint limits, and (v) the sign of the explicit quadratic derivative of the three-patch mean.

## Deterministic supplementary numerical checks

Run `python3 verify.py` using Python 3.9 or later with no third-party modules. The verifier independently constructs the finite-state continuous-time Markov count chain and checks its survival via Poisson uniformization against the closed form. Its deterministic grid spans patch counts two through eight, all quorum sizes, boundary and interior shared-shock rates and several horizons; it also checks elasticity ordering, numerically brackets crossing locations for intermediate quorum sizes, and tests the mean formula at 101 rational-grid inputs. Expected output: `PASS: 1142 independent finite-state/uniformization, elasticity, crossing and exact-mean tests`.

Exact symbolic polynomial checks using a separate computer-algebra calculation confirmed the binomial-tail derivative for all patch counts two through nine and the mean derivative identity. Such finite checks are corroborative only. The analytic proof is what establishes all positive times, all patch numbers and all real rates.

## Scientific limitations

There is no recovery, migration or recolonization and no heterogeneity between patch marginal hazards. No stochastic empirical data are analyzed. The full text of the directly relevant 2015 and 2016 papers was not accessible, so historical originality is provisional. Independent audit and external validation have not been performed.
