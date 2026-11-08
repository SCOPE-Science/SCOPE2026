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

# Mathematical verification

Run `python verify.py` with SymPy installed. This directly checks the Padé Maclaurin terms through degree four, the first four derivative factorizations, all five-state Jordan entries, all four absorbing-column expressions, conservation of row sums, the threshold derivative, and a certified rational root enclosure \(0.49660<h_*<0.49661\). It additionally tests 192 rational examples on acyclic graphs with at most three forward layers. Actual result from the supplied standalone checker:

```
VERIFY_OK exact_formula+derivative+root+small_graph_trials 192
```

The general assertions are proved analytically in RESULT.md by the divided-difference path expansion and a shortest-path Taylor argument. No finite simulation can certify these quantified claims. The positivity threshold refers exclusively to the specific five-state witness in exact arithmetic. Historical priority and generalizations to cyclic generators remain unresolved outside the stated theorem.
