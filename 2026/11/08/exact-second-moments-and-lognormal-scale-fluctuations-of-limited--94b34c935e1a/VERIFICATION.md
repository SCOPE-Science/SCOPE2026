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

# Reproduction of finite checks and proof dependencies

The embedded file `check_lpc.py` is executable with Python 3 and requires only the standard library:

```sh
python3 check_lpc.py
```

It independently generates output spheres by recursively choosing disjoint adjacent swaps; it then checks the matching recurrence on each word and compares the exact rational first and second moments with the stated matrix evaluator. The executed test grid is alphabet sizes \(q=2,3,4\) up to lengths \(12,9,7\), respectively: \(59{,}557\) input instances in total. Additional exact rational tests verify nonzero variance for selected longer lengths. The run printed both PASS messages.

The finite program does not establish the almost-sure and Gaussian limits, characterize all possible source laws, or certify the Perron asymptotic for every length. Those infinite claims rely instead on the explicit Bernoulli transition counting, independent regenerative cycles, iid strong/central limit theorems, geometric-tail bound, Perron–Frobenius positivity and exact characteristic-polynomial sign argument stated in `RESULT.md`.

There has been no independent mathematical audit of the proof or verification code. The cited earlier ball-product and mean formulas are acknowledged rather than claimed as new.
