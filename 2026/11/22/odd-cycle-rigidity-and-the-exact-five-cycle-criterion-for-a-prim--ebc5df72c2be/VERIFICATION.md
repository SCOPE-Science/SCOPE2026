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

# Reproducibility and boundaries

The theorem concerns all positive odd shifts and is proved without a global computation. The key two-step facts are: every odd prime maps to an even composite under an odd shift, and every composite maps to a prime. The only possible prime-to-prime edge is \(2\to k+2\), if the target is prime. A primitive odd cycle therefore contains \(2\), proving the at-most-one statement for a deterministic map. A primitive period-five orbit must have exactly the itinerary \(2, k+2,2k+2,q,k+q\) with \(q=P^+(k+1)\), and closes after five distinct states exactly under the arithmetic conditions in RESULT.md.

## Executable checks actually performed

Run `python3 verify.py` in the directory containing this file, `RESULT.md` and `verify.py`. The checker uses only Python 3 standard syntax and an exact sieve to evaluate primality and largest prime factors. Independently, it tests the proposed arithmetic criterion and applies the defining map five times for all \(100001\) positive odd shifts through \(200001\). The full captured output is `verification_output.txt`; all comparisons passed and seven parameters were found in the finite tested interval. The finite check does not establish the infinite proof.

## Limitations

There is no claim concerning even shifts, periods beyond five or infinitude of parameters. The proof has undergone the stated self-review only. Independent audit has not been performed. Relevant earlier material includes arXiv:2312.06629v1 (11 December 2023), Dubickas (2024), and the published same-map exact periods-one-through-four classification.
