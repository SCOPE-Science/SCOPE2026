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

Run `python verify.py` and `python verify_dynamics.py` with Python 3 (standard library only). The checker enumerates all permutations and initial colorings in nine small complete-multipartite cases and separately calculates the joint-tail expression from multinomial color occupancy probabilities and falling factorials. It compares 189 joint-tail thresholds exactly using `fractions.Fraction`, checks rational convergence inequalities, and verifies a nontrivial sharp-rate lower bound already in the multicolor domain.

Expected success markers:

```
DIRECT_LABEL_COLOR_ENUMERATION_PASS cases= 9 joint_tails= 189
EXACT_TAIL_IDENTITY_AND_RATE_WITNESSES_PASS
VERIFY_OK
```

The verification is finite corroboration, not a substitute for the general uniform-injection argument, stopping-time coupling, or geometric second-moment bound. No code verifies historical originality. Neither a peer review nor an independent audit is asserted.
