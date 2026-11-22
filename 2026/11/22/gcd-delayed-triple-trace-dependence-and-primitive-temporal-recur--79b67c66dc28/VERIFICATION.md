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

# Reproduction and verification

Run `python3 verify_three_probe.py` from the directory containing this file. Only Python 3's standard library is required. The program independently builds the finite-field Laurent-polynomial observation matrix for the three stationary sensors and computes its rank by sparse elimination, checking the announced formula. It also checks strong divisibility of the recurrence polynomials using polynomial Euclidean division, evaluates the unquotiented syzygy in the Laurent ring, and directly enumerates all initial input assignments for selected small windows to verify the exact distribution of observable outputs.

The observed run completed with the summary:

```
VERIFY_OK all_prime_field_ranks=13464 Laurent_relations=2244 strong_divisibility=6724 full_distributions=4
```

The tests cover prime fields of sizes 2, 3, 5 and 7 and finite parameter ranges. They **do not** establish the theorem for arbitrary prime powers or unbounded observation horizons. Those quantifiers follow from the algebraic proof in `RESULT.md`; no external formal proof certification is asserted. The independent-audit status in the front matter records that no independent scientific validation has been performed.
