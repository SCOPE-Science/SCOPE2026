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

# Verification and scope

Run `python3 verify.py` with standard Python 3. No optional dependencies or network access are required. The script checks \(2\le n\le10000\) independently for each \(2\le k\le8\). It computes the divisor sums directly and computes their Dirichlet inverse using the convolution recurrence, not the prime-power formula used in the proof. It separately generates the Möbius and Jordan functions by prime-factor recurrences.

Expected final line:

```
VERIFY_OK k_range=2..8 n_range=2..10000 independent_convolution=yes exact_integer=yes
```

Each \(k\) also yields a `PASS` line giving the exact minimum and its unique minimizer. All comparisons are between integers; there are no floating-point tolerances. The finite check corroborates only the stated finite input range. The unrestricted assertion follows from the explicit case proof, including the Euler-product estimate for cube-free nonsquarefree integers. Independent validation has not been performed.
