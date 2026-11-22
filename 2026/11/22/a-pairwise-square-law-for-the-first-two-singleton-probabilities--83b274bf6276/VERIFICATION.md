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

# Reproducible checks and limits

Execute `python3 verify.py` under Python 3 with no third-party dependencies. The recorded output is:

```text
PASS; exact_rational_assertions=522; state_sizes=2..6
```

The program computes the full stopped singleton-count law by an exact rational Markov recursion on coupon occupancy states zero, one, or at least two. Independently it evaluates every pair-kernel integral by a signed finite expansion of the factors \(F_k\) followed by exact rational gamma integrals. These two mechanisms agree for deterministic and seeded positive integer weight vectors in dimensions two through six, including uniform and nonuniform cases. The assertions also check normalization, the absence of zero singletons, nonnegative difference, equality only under uniform weights, and the exact two-type boundary identity.

The infinite-dimensional quantifiers over positive real weights and all finite alphabet sizes are proved analytically in `RESULT.md`, not by the finite checker. The historical-priority comparison is limited to the sources listed there and in `REVIEW.md`; there is no independent mathematical validation.
