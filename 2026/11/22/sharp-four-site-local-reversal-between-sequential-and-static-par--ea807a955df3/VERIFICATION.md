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

# Verification

Run `python3 check.py` with Python 3 and the standard library. The recorded stdout is in `checker_output.txt`. The checker makes 289 exact-rational assertions, including every site at each length \(14\le n\le22\), the sharpness counterexample \((n,j)=(13,7)\), independent greedy first-arrival recursion checks up to size nine, independent complete static maximal-set enumeration up to size ten, and exact rational sign certificates for all numeric inequalities used by the analytic infinite proof. The checker needs no scientific datasets, external services or packages.

The infinite assertion is not based on finite computation alone: the proof in `RESULT.md` establishes, for all \(n\ge23\), the Padovan-ratio enclosure by a positive convex recurrence, a uniform bound on interior baseline probabilities, a rigorous integrated Taylor bound, and the sign of each of five boundary comparisons. All remaining sizes are finite and checked exhaustively with rational arithmetic.

The checks do not assess historical priority beyond the sources explicitly examined; one earlier relevant paper was not available in full text. No independent assessment has been performed.
