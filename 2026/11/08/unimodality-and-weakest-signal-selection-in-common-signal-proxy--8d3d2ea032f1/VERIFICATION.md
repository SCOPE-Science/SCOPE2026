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

# Mathematical verification

Run `python3 verify.py` with Python 3. The script uses exact rational arithmetic for all substantive assertions and computes binomial tails directly, independently of the closed-form increment. It verifies 5,760 increments and 1,280 exact-rational three-signal environments, the rational five-voter counterexample, three large-electorate instances of rare-state selection, and 12 single-state combinations. Its deterministic output is shown below:

```
rare-state optimum 100 = 9
rare-state optimum 150 = 9
rare-state optimum 200 = 9
PASS 5760 exact direct-increment comparisons; 1280 one-peak exact cases; three large-population rare-state checks; one exact counterexample and 12 scalar parameter pairs
```

The proof of an unrestricted electorate size and finite state set is analytic in RESULT.md; no finite enumeration is claimed to certify an infinite assertion. The longer arXiv source of the motivating common-signal model remained inaccessible for full-text comparison. Independent audit has not been performed.
