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

# Verification and reproducibility

The accompanying scripts use only Python 3 standard-library `fractions`, `functools` and elementary arithmetic. Each is a complete executable independent of external research data. Reproduce from the directory containing the scripts:

```sh
python check_count_chain.py
python check_labelled.py
python check_edge_effect.py
```

The count-state checker explicitly constructs the transition probabilities over hub-bit and number-of-one-leaves states, excludes null selections, and evaluates absorption exactly by rational recurrence for 35 leaf counts (every integer from 1 through 30, and 40, 49, 50, 99, 100). It checks all initial hub bits and all attainable one-leaf counts, including all tie cases.

The labelled-state checker independently constructs the graph from its edge list and enumerates all configurations at each leaf count 1 through 10, computing the exact rational absorbing Markov chain. It checks every one of 8184 labelled states against the claimed kernel.

The edge-effect checker builds both adjacency matrices independently, evaluates the polarized initial-state probability by rational recurrence for leaf counts 1 through 11 and compares their exact difference with the parity formula.

Actual reproduced stdout is included in `count_chain_stdout.txt`, `labelled_stdout.txt` and `edge_effect_stdout.txt`. All three outputs end in `PASS`. These are finite tests, not an exhaustive search over the infinite parameter \(s\). The proof in `RESULT.md` establishes the full domain by a strict descent argument and exact first-effective-update probabilities. No independent scientific audit has been performed.
