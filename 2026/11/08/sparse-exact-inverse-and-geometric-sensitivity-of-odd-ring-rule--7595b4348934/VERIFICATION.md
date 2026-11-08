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

# Verification

The accompanying `verify.py` is standalone Python, uses no third-party packages or external data, and derives the elementary cellular automaton rule directly from its Boolean local expression. Running `python verify.py` on the extracted package yielded:

```text
VERIFY_OK odd_sizes=8 single_bit_checks=64 n_max=15
```

The program checks, for every binary output of each odd ring length from 1 through 15, that the explicit inverse maps back to that output under Rule 45. It then enumerates the Boolean derivatives of coordinate zero under every single output-bit flip at each tested ring length, comparing their exact counts with the stated powers of two. For odd lengths through 13 it independently computes the algebraic normal form by the Boolean Möbius transform, verifying its entire support, cardinality and degree. The check can be repeated with the supplied script; these finite checks are evidence of implementation consistency, not substitutes for the proof's universal induction and combinatorial counting.

No independent audit has been performed.
