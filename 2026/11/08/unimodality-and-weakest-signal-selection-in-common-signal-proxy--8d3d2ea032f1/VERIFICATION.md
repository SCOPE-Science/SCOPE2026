---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification

To reproduce the companion diagnostic, run `python3 verify.py` in the result package. It uses exact rational arithmetic for comparisons of the pivotal increment with direct binomial tails, for the unimodality tests, for the counterexample, and for the rare-state increment signs. It uses floating logarithms to select the cutoff to test in the rare-state and scalar log-odds examples. In the rare-state example the cutoff also follows from the exact inequalities \((11/9)^{10}<9<(11/9)^{11}\). The scalar grid contains 12 parameter pairs, of which 11 enter the noninteger cutoff comparison; the integer case is skipped.

Recorded output of the unchanged companion script:

```
rare-state optimum 100 = 9
rare-state optimum 150 = 9
rare-state optimum 200 = 9
PASS 5760 exact direct-increment comparisons; 1280 one-peak exact cases; three large-population rare-state checks; one exact counterexample and 12 scalar parameter pairs
```

These checks are finite. The analytic proof in `RESULT.md` establishes the unrestricted electorate-size claims, with a noninteger log-odds ratio required for the stated eventual unique count.
