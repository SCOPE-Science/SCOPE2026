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

# Reproduction and scope

Run `python3 verify_basic_gini.py` using Python 3's standard library. The checker uses integer operations for all 24,308 rank-permutation/cut evaluations, `fractions.Fraction` for their sharp quotients and exact rational perturbation witnesses, and no external dependencies.

Expected output:

```text
N=2 EXACT_GINI_LIPSCHITZ_MODULUS=1 CHAMBER_CUT_PAIRS=2
N=3 EXACT_GINI_LIPSCHITZ_MODULUS=1 CHAMBER_CUT_PAIRS=18
N=4 EXACT_GINI_LIPSCHITZ_MODULUS=1 CHAMBER_CUT_PAIRS=168
N=5 EXACT_GINI_LIPSCHITZ_MODULUS=1 CHAMBER_CUT_PAIRS=1800
N=6 EXACT_GINI_LIPSCHITZ_MODULUS=9/8 CHAMBER_CUT_PAIRS=22320
GENERAL_DIMENSION_LOWER_WITNESSES_PASS_N6_TO30
ALL_EXACT_CHAMBERS_AND_CUTS_PASS 24308
STRICT_SIX_SITE_WITNESS_PASS
```

The proof in `RESULT.md` independently establishes why this finite enumeration covers **every** admissible local linear regime and nonzero perturbation for the sizes claimed. It also provides an analytic proof of the bounds for every larger size. Rational examples through size thirty corroborate that general formula; their finite range is not offered as an infinite proof.

No independent audit or external formal verification has been performed.
