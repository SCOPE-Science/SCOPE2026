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

# Verification instructions

Run `python3 verify.py` using Python 3.9 or later. It uses the standard library (`math`, `fractions`) only. The diagnostic suite verifies two exact-rational branching roots and corresponding uniformly seeded survival probabilities; for 1,700 supercritical combinations of \(p,A,R,c\), it checks both positive scalar root identities, an independent algebraic expression for \(P\), attack-rate composition and every strict monotonic comparison between adjacent allocation levels. It reports 16,816 passed assertions.

The exact sample with \(p=1/2\), \(A=4\), and \(R=1\) gives \(P(1)=1/2\), \(P(4)=3/5\), \(T(1)\approx0.892644753609\), and \(T(4)\approx0.733186926970\). These are complementary checks; the continuum statement depends on the analytic proof in `RESULT.md`. At extreme rates, numerical evaluation can round a within-class infection fraction to exactly one, so that numerical monotonic check uses a weak inequality only for that saturated displayed fraction; the proof establishes true strictness.

**Verification limits:** numerical tests cannot establish a universal parameter theorem, and the model is a deterministic vanishing-seed final-size limit plus an early-stage branching approximation. The exact proof assumes homogeneous rank-one mixing, common exponential recovery, fixed type fractions and strictly supercritical transmission. An independent scientific audit has not been performed.
