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

# Verification of the cubic Fibonacci gcd theorem

The standalone program `check_cubic_gcd.py` uses only the Python standard library, recomputes Fibonacci and Lucas numbers from their initial values, and carries out exact integer arithmetic. Run with `python3 check_cubic_gcd.py`.

The recorded execution produced:

```text
VERIFY_OK even_lengths=120 exact_sum_windows=2400 odd_and_even_periods=checked discrepancy_k6=2_vs_4 k8=9_vs_half_9
```

For every even length \(2\le k\le240\), the program independently computes 20 shifted windows of consecutive Fibonacci cubes, takes their gcd, and compares it with the proposed closed form. It additionally verifies the endpoint-cube gcd, linear-period gcd, periodicity of cubes, and the exact parity of twice the initial sum divided by the endpoint gcd. The computed finite windows are **not** an exhaustive verification of the infinite collection or an infinite proof.

The written proof supplies the infinite reasoning: addition identities determine the linear period, a Cassini-modulo-prime argument determines the cubic endpoint gcd, and the exact initial-sum expansion determines the only possible factor-two loss. Limits: the checks do not establish originality; independent review has not been performed; no formal proof assistant was used.
