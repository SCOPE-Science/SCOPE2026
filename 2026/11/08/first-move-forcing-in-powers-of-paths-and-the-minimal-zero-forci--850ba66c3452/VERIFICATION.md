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

# Verification evidence and limits

Run `python3 verify_pathpower.py` with Python 3.8+; no external packages or input data are required. The checker constructs graph adjacency by its definition, computes ordinary forcing closure without calling the theorem, and enumerates all masks for \(1\le k\le5\), \(k+1\le n\le14\). It separately constructs all oriented-edge triggers and their minimal antichain for \(3\le n\le18\), checks each square's entire mask lattice, and compares the predicted minimal-set polynomial coefficient by coefficient.

Actual source-code replay yielded:

```
VERIFY_OK first_move_cases=55 first_move_subsets=163716 square_orders=3..18 square_full_subsets=524280 square_minimal_sets=288 exact_polynomial=PASS all_minimal_triggers=PASS standard_zero_forcing=PASS
```

The proof supplied in `RESULT.md` establishes the general assertions. Finite experiments are corroborating evidence only, not a substitute for the unrestricted proof. Scientific review is same-model and non-independent. Independent audit: not performed.
