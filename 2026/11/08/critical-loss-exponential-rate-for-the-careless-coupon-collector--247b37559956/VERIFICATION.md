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

# Reproduction and limits

Run `python3 checker.py` using only the Python standard library. The code independently solves stationary **count-chain** linear systems for \(1\le n\le7\) with four rational loss parameters and independently solves the **set-valued** chains for \(1\le n\le4\) with two further rational parameters. It compares every inclusion factorial moment with the exact product, and checks stationary entry/exit flow. It computes an independent Simpson-rule approximation to the proposed integral for \(c=1/4,1/2,1,2,4\) and compares it with stationary-product Riemann sums at five finite system sizes. All 491 finite exact/numerical checks passed.

The full claim is proved by the stationary inclusion recurrence, the monotone-coupling lower bound, a uniform \(nq^t\) total-variation coupling bound, Markovian block estimates for the upper bound, and Riemann convergence. Finite tests do not establish infinite limits, prove uniqueness in the literature, or supply independent validation. The mean hitting-time rate is proved for every fixed positive \(c\); no multiplicative prefactor or distributional limit is claimed.
