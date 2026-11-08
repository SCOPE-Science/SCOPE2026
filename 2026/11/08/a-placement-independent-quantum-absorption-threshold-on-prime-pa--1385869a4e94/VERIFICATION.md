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

# Verification

Run `python verify.py` using Python 3 and its standard library. The program builds the prime Paley adjacency matrices and verifies the strongly regular equations, exact modular Krylov ranks and the nine-site exception. Finite test results obtained:

- \(p=5\): every one- and two-site absorbing set, fifteen sets total, agrees with bright rank \(1+2t\).
- \(p=13\): every nonempty absorbing set with \(1\le t\le6\), 4,095 sets total, has bright rank \(1+2t\).
- \(p=17\): 200 reproducibly selected absorbing sets across sizes \(1\le t\le8\) agree with the theorem.
- The order-nine \(2\times2\) sink block has an explicit adjacency eigenvector at eigenvalue \(1\) that vanishes at the sinks, while a different four-sink placement has an independently reproduced full-rank integer minor with determinant \(6\).

The infinite-prime step is analytical and uses Chebotarev's full Fourier minor nonvanishing theorem as proved in Tao's cited source. Numerical or modular tests alone do not establish the infinite theorem. All asymptotic claims concern eventual absorption only, not finite-time guarantees. Independent audit has not been performed.
