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

# Verification of the exact joint distribution and variance

Run `python3 verify_small.py` and `python3 verify_transfer.py` using Python 3 and only the standard library.

- `verify_small.py` constructs the **set of distinct residual strings** by literally deleting each eligible ordered `01` pair from every binary word of lengths 0 through 12; it compares the resulting counts with the contiguous-pattern identity, and checks the exact means and variances, using rational arithmetic.
- `verify_transfer.py` computes the joint distribution of contiguous `01` and `0101` by two independent finite computations: a last-three-symbol automaton and a coefficient recurrence from the proposed rational generating function. It compares all coefficients, their total mass, and the first two moments for every word length from 0 through 26. Arithmetic is integral or rational throughout.

Both commands completed successfully from the packaged files. The formal generating-function calculation and the bounded-dependence central limit theorem, not finite tests, prove the unbounded claims. Verification does not establish novelty or independent scientific certification.
