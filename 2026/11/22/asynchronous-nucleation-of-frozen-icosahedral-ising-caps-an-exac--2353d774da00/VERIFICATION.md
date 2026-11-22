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

Two standalone exact-arithmetic programs verify the result.

Run `python3 check_rational.py` (Python 3.8+; standard library) and `python3 check_independent.py` (Python 3; NetworkX 2.8+). The first constructs the pole-and-ring graph, checks every one of the 4096 states and computes the exact first-step hitting probabilities by a memoized rational recursion. The second uses a separately constructed icosahedral graph, states represented as immutable sets and an energy-ordered dynamic-programming solution.

Both check all 4096 states, the exact fourteen terminal states, all thirteen initial-positive-population coefficients and the exact \(p=1/2\) probability. The first additionally checks that each synchronous cap has exactly one precursor and that precisely 60 three-positive-spin states have cap absorption probability \(1/30\). All checks are deterministic, exhaustive within this finite domain, and based on integer/rational operations; the generalization to other graphs is unproved. The public proof and programs do not constitute independent scientific validation.
