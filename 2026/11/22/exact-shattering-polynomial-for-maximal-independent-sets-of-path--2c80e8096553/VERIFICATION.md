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

# Reproducible verification

Run `python3 checker.py` with Python 3 using only its standard library, from the directory containing `checker.py`. The supplied `automaton_certificate.json` records all 28 reachable subset families, their transitions, quotient classes and the six-state accepted-support DFA. `verification_output.txt` records a successful replay.

The verifier independently generates every maximal independent set of each path through length 13, then for each of the 16,382 supports compares direct Boolean trace shattering with the pairwise avoidant-path criterion and the six-state automaton. It reconstructs the 28-family powerset process from the five basic prefix states, refines accepting equivalence to obtain six states and checks the transition table. The independent transfer recurrence and explicit binomial coefficient formula are compared through length 100.

The infinite-length conclusion does **not** follow from those finite comparisons: it follows from the inductive invariant of the family-of-subsets automaton, exhaustive enumeration of its finitely many reachable states, the six-state quotient transition certificate, and exact formal-power-series algebra in `RESULT.md`. Independent external mathematical audit has not been performed. Full text of every close literature record was not available; the originality comparison remains qualified on that point.
