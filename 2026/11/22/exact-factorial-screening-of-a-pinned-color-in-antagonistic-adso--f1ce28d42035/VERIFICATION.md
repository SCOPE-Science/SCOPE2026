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

# Verification of the pinned-color response

Run `python verify_seed_response.py` in a standard Python 3 environment. The program uses only the standard library. It enumerates all active-site subsets, permutations of active arrival order, and proposed color marks on one-sided finite paths containing one through seven sites adjoining a preoccupied root. The two root colors are evaluated with identical random inputs. Exact expectation differences at three rational color biases and three rational time cutoffs are compared, without numerical tolerances, against independently built finite-half-line Volterra polynomials.

Observed check: **252 exact equalities over 1,146,655 marked-order cases; all passed.** An additional high-precision series test verifies the balanced spatial response sum \(t/2\) at \(t=1\) with an explicit positive factorial remainder bound after 20 terms.

The independent finite recurrence is
\[
a_m'(t)=\alpha[1-b_{m-1}(t)],\quad b_m'(t)=\beta[1-a_{m-1}(t)],\quad a_0=b_0=0.
\]
For a finite path of \(n\) unseeded vertices and an observation at distance \(d\), its exact influence formula uses the cavity factor \(1-b_{n-d}(t)\). This is different from the infinite-volume hyperbolic cavity law, so the exact finite tests do not assume the conclusion being tested.

The mathematical proof in RESULT.md, not the finite enumeration or the numerical series test, establishes the infinite-volume formula, strict positivity at all distances, and the sharp factorial limit. No formal proof assistant or independent external audit was used. The displayed front matter states the status of the separate independent-audit channel and makes no certification claim.
