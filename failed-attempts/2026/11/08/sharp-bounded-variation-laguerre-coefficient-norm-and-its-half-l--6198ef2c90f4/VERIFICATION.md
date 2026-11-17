---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

With Laguerre L_n^(0)(0)=1 orthonormal for weight e^-x, the signed primitive F_n(x)=x e^-x L_(n-1)^(1)(x)/n vanishes at 0 and infinity. Stieltjes integration by parts gives sharp BV coefficient bound with a single jump extremizer. The exact ODE F_n''+F_n'+nF_n/x=0 yields Sonin derivative S_n′=(1-2x)(F_n′)^2/n, so the maximum lies at one of the Laguerre roots nearest 1/2. Classical compact-uniform Plancherel–Rotach asymptotics give n^(3/2) S_n(x)→e^-x sqrt(x)/pi and limit n^(3/4) M_n=e^(-1/4)/(2^(1/4)sqrt(pi)). An oscillatory near-1/2 peak supplies lower matching bound; envelope monotonicity gives argmax localization. Numeric independent checks of n=100..800 corroborate only.

## originality

FAIL

The earlier/same-day Resultary complete theorem A hard-edge transition for sharp generalized Laguerre bounded-variation coefficients proves these SAME results for every α>-1: the precise sharp primitive norm, envelope derivative E′=(2α+1-2x)(F′)^2/n, finite maximizing-root classification, bulk asymptotic and localization at α+1/2. Setting α=0 gives every submitted conclusion, constant, and exact two-root rule. Generic weighted primitive and fixed-jump earlier work are additional known ingredients. The new ordinary case is strictly a covered specialization.

## value

FAIL

The best BV norm of Laguerre coefficients is a natural mathematical invariant; nevertheless the complete generalized-parameter theorem already proves this ordinary α=0 case and additionally identifies a hard-edge phase transition. Merely restricting that established theorem to one parameter and restating its proof does not yield distinct value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
