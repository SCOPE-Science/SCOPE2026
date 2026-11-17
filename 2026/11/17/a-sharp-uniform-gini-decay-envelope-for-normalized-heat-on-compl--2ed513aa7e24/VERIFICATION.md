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

The analytic argument establishes the statement for all integers \(p,q\ge1\) and all real \(t\ge0\). The standalone `verify.py` uses only Python's standard-library `fractions.Fraction`, computes rational semigroup values from the block spectral formula, and checks exact cut norms, ordinary signed-signal inequalities, uniform finite-size bounds, and explicit approaching witnesses.

Run `python3 verify.py` beside the included result. The verification suite reports:

```text
EXACT_FULL_CUT_OPERATOR_NORMS_PASSED 16100
EXACT_SIGNED_INPUT_TESTS_PASSED 5804
STRICT_FINITE_CONTRACTION_AND_UNIFORM_ENVELOPE_PASSED 576
SHARP_ENVELOPE_APPROXIMATION 10 100 80/109
SHARP_ENVELOPE_APPROXIMATION 20 400 360/419
SHARP_ENVELOPE_APPROXIMATION 40 1600 1520/1639
SHARP_ENVELOPE_APPROXIMATION 80 6400 6240/6479
SHARP_ENVELOPE_APPROXIMATION 160 25600 25280/25759
ALL_BIPARTITE_GINI_HEAT_DIAGNOSTICS_PASSED
```

The finite tests corroborate identities but are not used to infer unrestricted quantifiers. The proof's coarea argument covers arbitrary real signals; the algebraic bound handles every finite graph and every real time; the lower sequence establishes only a supremum, not finite attainment. Scientific priority has not been independently validated.
