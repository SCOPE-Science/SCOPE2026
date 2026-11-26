---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The KL chain rule with common random labels counts one marginal log 2 per first-round reveal and conditional entropy per second-round reveal, minus the joint entropy. Nearest revealed flanks screen distant observations, with the double correction at distance d counted at each of d−1 interior positions. Exponential decay at fixed ρ justifies the thermodynamic gap series. Expanding I_d in positive geometric modes yields the displayed factored positive second derivative; termwise differentiation is uniform in p for fixed ρ<1 since the denominators are bounded below by 1−ρ². The endpoint derivative at 0 is negative and that at 1/2 positive. In the geometric-flank representation, the linear and linear-log-scale terms of the small-argument binary entropy cancel. For p=t√δ the rescaled geometric flanks have uniform exponential tails on compact t-intervals, justifying the log-moment remainder and expectation convergence. The leading homogeneous bracket at independent unit exponentials is (U+V)h(U/(U+V)); the gamma sum has mean 2 and the independent uniform ratio has mean binary entropy 1/2. Thus the limiting scaled objective is t log 2+1/(2t). Its interior point has smaller value than either fixed bracketing endpoint, which by convexity localizes the true minimizers and proves convergence of values and minimizers. Bounded convergence at fixed p gives p log 2 and the stated relative penalty. These are forward path KL statements in nats; the length-first limit is essential. Replay: RESULT.md steps 1–5; checker.py inspected, not executed (finite identities and diagnostics only).

## originality

FAIL

Two distinct indexed same-day findings directly cover the claimed scientific result. The two-pass finding gives the exact same minimum, optimizer, and locally uniform scaled objective under equivalent parameters; the all-fixed-round theorem also gives both optimizer and minimum at m=2. The date alone does not establish priority or which finding came first. The arithmetic uniform-schedule ratio and shorter conditional-entropy derivation do not establish a distinct scientific claim. This is demonstrated material overlap, not lack of access or a conjectural prior.

## value

FAIL

The sharp optimizer and minimum are useful facts for comparing reveal schedules, but the frozen record adds no independently useful mathematical conclusion over the direct two-pass and fixed-round statements. The equal-round ratio is an immediate consequence of the exact two-round objective and the covered constants. The alternative derivation is expository and is not a substantive surviving finding as presented.

The dated certificate retains the supplied scientific assessment, sources and limitations.
