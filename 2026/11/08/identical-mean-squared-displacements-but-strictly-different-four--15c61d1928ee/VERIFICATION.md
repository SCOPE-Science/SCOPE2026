---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In RESULT.md the stationary independence hypotheses identify the product-drift covariance as AB exp(-(a+b)|t-s|), and the Brownian increment adds only D_x T to the variance. On ordered times set p=exp(-2ay), q=exp(-2by), with y the middle time gap. Wick's formula contributes factors (1+2p) and (1+2q); independent Poisson sign increments replace the second factor by 1. In both mechanisms the disconnected terms give the factor 1+2pq after removing A²B² exp(-(a+b)(x+z)). The connected factors are therefore 2(p+q+pq) and 2p(1-q), which give both strict inequalities, the exact F combinations after multiplying by 4!, and the stated T⁴ and T⁵ coefficients from the first nonzero terms. Dividing F by T and using an exponential majorant gives 1/(c²d), yielding the stated positive rates and their ratio. Independently, conditioning on the stiffness path gives a centered Gaussian with variance D_x T+<U,C_Y U>. For Gaussian U the variance term is a sum of weighted independent Gaussian squares with weights from C_U^(1/2) C_Y C_U^(1/2); this is a nonzero positive trace-class operator, and its largest weight gives divergence at both endpoints as well as outside the interval. For the sign process the quadratic form is uniformly bounded by BT||C_Y||, and ||C_Y||≤2A/a. The conclusion includes D_x=0 in the abstract process and T=0 for the MSD only. The primary source confirms the physical calibration with D_x>0. The supplied check.py and VERIFICATION.md were inspected: the 193 listed diagnostics are bounded/reported evidence, not a fresh run and not an operator-domain proof. The replayable verification here is the analytic reconstruction of RESULT.md, proof parts 1–4.

## originality

PASS

Credit the source model and MSD, the separately documented Gaussian dimer fourth cumulant, and the previously documented underlying bath distinction. The surviving contribution is the quantitative comparison of the integrated product drifts: the positive telegraph fourth cumulant, explicit paired growth ratio, and exact finite-time exponential-moment distinction in the same calibrated models. None of the compared sources establishes that combined result.

## value

PASS

Two physically motivated mechanisms with identical transport curves have a quantitative discriminator at every positive observation duration. The positive finite-time separation, strength of the long-time contrast independently of amplitudes and bare diffusion, and different moment domains go beyond the existence of some non-Gaussian difference. This is an exact-law comparison, not a finite-sample inference guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
