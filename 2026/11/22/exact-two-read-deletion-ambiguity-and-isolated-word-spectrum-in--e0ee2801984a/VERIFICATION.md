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

# Verification and scope

The three standalone scripts in the same package are executable using standard Python 3 without third-party packages:

```sh
python3 verify_deletion.py
python3 verify_transfer.py
python3 verify_isolated.py
```

`verify_deletion.py` constructs distinct single-deletion descendant sets for all admissible words at lengths 1–13, then checks every unordered source pair, every legal adjacent swap and the edge coefficients. `verify_transfer.py` independently counts 010-avoiding inputs via a three-state automaton, checks rational edge generating-series identities through coefficient 100, and counts all swaps through length 17. `verify_isolated.py` checks every coefficient of an eleven-vector polynomial identity representing the exact isolated-word language, and directly enumerates padded-factor and graph-neighbor equivalence for all lengths 0–14.

The successful terminal markers are `VERIFY_DIRECT_OK`, `VERIFY_TRANSFER_OK` and `VERIFY_ISOLATED_OK`. The universal count is proved by the alternating-interval lemma and finite polynomial identities rather than inferred from finite experiments. There is no independent mathematical audit or external certification of this result.
