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

Integrating the dose-adjusted first-infection hazard gives survival exp(−ε[A/400+16−J_A(t)]), with J_A=AU+V the stated positive sum. For ε>0 stationarity and comparisons are identical to those of J_A. Its derivative F= A exp(−20t)(1/441−20t/21)+exp(−t/4)(16/25−t/5) has signs +,−,+,− at 0,1/20,1,4. The middle inequalities follow from −2000/(441·3)+63/100<0 and −500/2^20+11/50>0. For the independent root-count bound, (exp(20t)F)'' is exp(79t/4) times an affine polynomial of nonzero slope −(79/4)^2/5. Two Rolle steps counting multiplicity bound total multiplicity by three; the three distinct bracketed roots must all be simple. The hazard's own derivative has the same affine plus exponential-affine structure after scaling, and signs +,−,+,− at 0,1/10,1,5 (at 1/10 bound by −100/9+1; at 1 bound below by −9500/2^20+3/8); this independently confirms two waves. Time zero is not a global maximum because F(0)>0, and the positive J_A vanishes at infinity. U peaks at 1/420 and its minimum on [0,1/20] is 1/441 because U(1/20)=22/(441e)>1/441, whereas U(1)=22 exp(−20)/441<1/441. This gives D'(A)>0 along the continuous simple-root branches. At A=100 the early value is <5/21+17/25<0.92 and the late maximum is ≥J_100(16/5)>(16/5)/3>1. At 500 the early value is >500/441+16/25>1.77; every t≥1 is bounded above by 11000/(441·2^20)+80/53<1.61, using exp(4/5)>1+4/5+(4/5)^2/2. This proves the sole tie, strict uniqueness on either side and jump >19/20. A bounded independent replay by 50-digit Decimal bisection of exp(20t)F on the three analytic brackets and of D on [100,500] gave A_c≈350.48017998995181 and dates approximately 0.004472463253515 and 3.2. These are orientation only. I inspected, did not execute, the frozen diagnostic script. This is a prescribed-hazard individual prevention model, not a clinical or population result.

## originality

PASS

Best-of-knowledge pass for the explicit continuous one-dose example with an exhaustive stationary-point classification, opposite global height ordering at two amplitude bounds, and a uniquely located jump for all positive hazard scales. Waning protection, competing incidence peaks and the integration and root-count tools are not claimed as new. The inspected timing/adaptive-policy literature does not entail the model-specific classification; historical full-text coverage for Werker remains incomplete.

## value

PASS

A natural benchmark for scheduling one waning preventive intervention under separated exposure peaks: the calculation shows that unimodality and smooth motion of the global optimizer can both fail within a simple explicit hazard family. An exhaustive certificate, an isolated crossing and a uniform strict jump are more useful than a sampled bimodal plot. The coefficients and interval are designed as a theoretical witness, not a disease calibration or a recommendation about when anyone should be vaccinated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
