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

# Reproducibility checks

The adjacent `verify_injective_quotient.py` constructs orbit cells independently by enumerating injective words and calculating completion parities, including all deleted-letter face incidences. It checks the chain-square identity, the complete low-degree differentials, and the top Smith normal forms for orders 3 through 9. The accompanying `verification_output.txt` is the recorded execution output for these tests.

The infinite proof depends only on the word-orbit and attaching-map arguments in `RESULT.md`; finite checks do not certify arbitrary orders. The special dimension-one attaching relators are checked by a manual generator elimination, not by a Smith normal form alone.

Reproduce with `python verify_injective_quotient.py` in a Python 3 environment with SymPy installed. Independent audit has not been performed.
