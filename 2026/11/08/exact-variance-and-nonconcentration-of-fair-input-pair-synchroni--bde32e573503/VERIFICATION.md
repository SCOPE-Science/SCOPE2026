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

# Verification procedure

Run `python verify_moments.py` with SymPy available.

Observed output:

```
SYMBOLIC_SECOND_MOMENT_AND_VARIANCE_OK
INDEPENDENT_PAIR_MARKOV_OK n=3 E=14 Var=142
INDEPENDENT_PAIR_MARKOV_OK n=5 E=88 Var=5320
INDEPENDENT_PAIR_MARKOV_OK n=7 E=270 Var=49294
INDEPENDENT_PAIR_MARKOV_OK n=9 E=608 Var=248448
INDEPENDENT_PAIR_MARKOV_OK n=11 E=1150 Var=886270
ALL_CHECKS_PASSED
```

The symbolic check reconstructs the second-moment finite-difference forcing and exact sum. The other check enumerates all unordered pairs, applies letters directly, and solves the first- and second-moment rational systems; it does not use the reduced coordinates. Finite tests do not prove all odd sizes. The proof for all odd sizes, including the uniform-tail argument behind nonconcentration, appears in `RESULT.md`. Independent audit is not performed.
