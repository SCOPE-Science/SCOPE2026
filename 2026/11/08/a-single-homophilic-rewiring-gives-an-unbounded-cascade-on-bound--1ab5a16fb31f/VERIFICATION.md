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

# Reproducibility and limits

Use Python 3.9+ with no third-party packages:

```sh
python verify.py
```

`verify.py` reconstructs the original \(m+6\)-vertex tree from its edge definition, computes the deterministic strict fractional adoption closure by repeated synchronous simultaneous rounds, enumerates all three initially mixed-status edges, uniformly enumerates all permissible target nonadopters for the chosen susceptible endpoint, and computes the outcome distribution and its expectation with `fractions.Fraction`. It also verifies that the same threshold-blocked static closure has exactly three adopters. It checks \(m=1,\ldots,20\) at the rational thresholds \(1/4\), \(3/10\), and \(333/1000\), covering boundary, interior, and near-upper-bound parameters. It additionally tests 20 below-threshold static completions and 19 upper-bound counter-controls. The run returned `PASS: 60 exact case families and 39 endpoint controls, n=7 to 26; every permissible one-shot rewiring`; representative checks have exact probabilities \(2/3\) and expectations \(17/3\), \(19/3\), \(7\), \(35/3\), and \(55/3\) for path lengths \(m=1,2,3,10,20\), respectively.

The infinite-family result follows from the four-case proof, not from testing finitely many sizes. The computation does not reproduce ongoing rewiring dynamics, estimate physical time, or establish that the theorem is unpublished elsewhere. Independent audit has not been performed.
