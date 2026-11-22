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
# Verification of the finite-horizon star-gossip formula

## Analytical checks

For each \(m\ge3\), leaf-permutation invariance reduces the centered quadratic observable to the hub and leaf-contrast eigenspaces. The exact update operator has trace \(5(m-1)/(4m)\), determinant \((m-2)(m-1)/(4m^2)\), and positive off-diagonal entries. Its eigenvalues yield the radical formula. The difference recurrence \(r_{k+1}-q_{k+1}=q_k/2+3(m-1)(r_k-q_k)/(4m)\) establishes the strict finite-horizon optimizer. The initial data \(r_0=1\), \(r_1=1-1/(2m)\) give the exact closed form; positivity and ordering of the eigenvalues imply strict log-concavity and the asymptotic rate.

## Executable checks

Execute `python3 verify_star_gossip.py` alongside this file. The script uses standard-library exact fractions, constructs independently the original pair-averaging matrices, checks the two invariant projector images coordinate by coordinate, iterates full covariance matrices for six nonzero horizons, and tests strict rate comparisons and characteristic identities. Its observed output was:

```
PASS exact rational finite assertions: 2060
```

All exact arithmetic checks passed. These tests cover only the finite range programmed; the general conclusions rest on the proof in RESULT.md. The check does not verify publication priority, floating-point implementation stability, or any independent mathematical review.
