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

# Reproducibility and verification

Run `python3 checker.py` in the directory containing `checker.py`; no external dependencies are required.

The checker reconstructs the literal integers \(Q_k(n)\) from products and LCMs over full candidate periods for every \(1\le k\le14\). It independently computes the generating-polynomial probabilities, compares exact rational frequency tables, and tests all proper divisor periods. It also confirms the parity-bias zero among \(2\le k\le39\). The observed output was:

```
PASS: 543 exact quotient instances across k=1..14; distributions and least periods match.
PASS: exact sign bias vanishes for k=2 and for no k from 3 through 39.
```

The full theorem is supported by the mathematical proof in `RESULT.md`: CRT for the finite distribution, the prime-number theorem for the first two growing-window moments, Berry--Esseen for normal convergence, and prime-number-theorem remainder control at the logarithmic singularity for parity decay. Finite code does not verify an infinite asymptotic or a universal least-period claim. External independent audit has not been performed.
