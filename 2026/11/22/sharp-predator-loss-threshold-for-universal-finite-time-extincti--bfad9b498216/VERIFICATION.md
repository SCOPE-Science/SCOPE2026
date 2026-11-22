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

# Analytical and computational checks

The paper proof is complete analytically: the exact \(q=s^{1-r}\) transformation, mass balance and asymptotic integrating-factor contradiction decide the universal extinction side, while two one-sided comparison bounds establish both outcomes above the threshold. The statements do not assert that a finite numerical trajectory proves nonextinction.

Run `python3 verify.py` with Python 3's standard library. The test first uses `fractions.Fraction` to check strict inequalities for an exact rational model. It then runs four RK4 illustrations with step \(0.002\) through a transformed positive-coordinate ODE. The four outcomes are finite hits at \(\mu=1/2\) and \(\mu=1\) with \(p_0=1/10\), a no-hit numerical illustration at \(\mu=3/2,p_0=1/10\) supported by an independent *analytic* lower bound, and a finite hit at \(\mu=3/2,p_0=2\) below an exact time bound. The exact inequalities, rather than numerical precision, establish critical-case inclusion and the sharpness comparison.

The model uses infection-free initial conditions; the full infected system, stochastic dynamics and finite-sample ecological inference are outside the verified scope. Independent audit has not been performed.
