---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Starting from Gnedin–Olshanski exact two-index displacement mass, weighted double sum is absolutely dominated in q<|z|<1/q by two convergent geometric series. Two standard q-binomial summations, using (1−q)(q²;q)∞=(q;q)∞, give PGF (q;q)∞²/[(qz;q)∞(q/z;q)∞]. Each factor is a geometric-variable PGF; finite total expectations imply almost-sure convergence of two sums and uniqueness of Laurent coefficients. At z=−1, product ∏((1−q^j)/(1+q^j))² is strictly positive and <1; termwise factor comparison, strict at j=1 and absolute log convergence, makes it strictly decrease with q. The previously known identification of fixed-point means with parity at q=1/Q completes c_o(Q)>1/2>c_e(Q), strict monotonicities. This analytic proof justifies all Q>1; rational finite truncation checker only corroborates.

## originality

FAIL

The entire claimed result is reproduced verbatim in a 2026-10-26 full published prior record on the same stationary balanced Mallows law: bilateral PGF, independent-geometric representation, exact parity product and strict Q-monotonicities. A 2026-11-02 full published paper additionally proves the same parity product and conclusions. New algebraic presentation interchanges q-binomial summation order but provides no stronger mathematical statement.

## value

FAIL

The solved fixed-point parity questions are mathematically valuable historically, but were already solved in earlier published results. This restatement supplies no new model, invariant, bound, or theorem; code checks and rederivation cannot create independent incremental value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
