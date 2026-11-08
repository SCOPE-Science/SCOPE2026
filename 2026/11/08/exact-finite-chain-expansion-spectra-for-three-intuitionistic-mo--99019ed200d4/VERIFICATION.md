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
Run `python3 check.py` using Python 3 and the standard library. The checker computes each monotone function pair on the Heyting chains with 2 through 6 elements and evaluates the interaction axioms directly, producing the counts (9,6,4), (100,44,29), (1225,430,288), (15876,5012,3377), and (213444,63924,43088). It also calculates an independent dynamic-programming count of the forbidden-band forms for sizes 2 through 14 and compares these with the closed formulas.

The all-size classification is established by case analysis on the two primitive monotone modal maps and exact binomial enumeration. The asymptotic density limit follows from a ratio estimate and dominated convergence, not from finite experiments. Neither the count nor any proof is independently certified. The source-priority comparison is limited to examined literature and indexed research records.
