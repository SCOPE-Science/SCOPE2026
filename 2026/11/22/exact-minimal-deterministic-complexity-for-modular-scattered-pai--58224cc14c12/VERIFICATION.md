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

# Finite computation and proof checking

Run `python verify.py` using standard Python 3 without extra dependencies. The script constructs the complete product automaton, independently minimizes reachable states through iterative partition refinement for each \(1\le r\le9\), \(2\le m\le14\), and compares direct forbidden-factor plus scattered-pair recognition on all binary inputs through length ten for \(1\le r\le5\), \(2\le m\le6\). The observed output was:

```text
PASS 117 independent reachable-DFA minimizations
PASS 51175 direct word-membership comparisons
All m=2..14, r=1..9 attain the claimed formula.
```

The universal proof is in `RESULT.md`: a modulo-counter transition invariant; explicit witnesses for each active state; equal affine zero fibres imply unit-related coefficient vectors over \(\mathbb Z/m\mathbb Z\); a legal boundary suffix separates run states; terminal states collapse into exactly two right languages. No finite computation is treated as an infinite proof. No independent audit has been performed.
