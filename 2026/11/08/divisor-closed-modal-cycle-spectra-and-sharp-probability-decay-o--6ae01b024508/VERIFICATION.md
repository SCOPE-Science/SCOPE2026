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

# Verification details

Run `python checker.py` from the extracted package directory. The program checks disjunctive formulas using independent propositional letters against all valuations in small cyclic frames, verifies the divisibility signature of the formula \(p\leftrightarrow\Box^a p\) for several lengths, and checks exact counts of permutations by recurrence against complete enumeration of \(S_n\) for \(n\le8\).

The analytic proof of the classification and decay exponent is in `RESULT.md`. Finite tests do not prove arbitrary formula-depth validity, the divisor-closed classification in general, or the asymptotic limit. The exact recurrence is proved by differentiating the labelled exponential formula; both inequalities controlling coefficients are explicit in the proof. This constitutes self-review only. No external or independent audit has been performed.
