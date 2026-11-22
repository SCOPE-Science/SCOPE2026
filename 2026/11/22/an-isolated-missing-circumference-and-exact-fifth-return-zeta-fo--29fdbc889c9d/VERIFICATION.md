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

# Reproducing the exact finite-state checks

The reproducible result uses standard Python only. From this directory run:

```
python verification/transfer.py
python verification/direct.py
```

`verification/transfer.py` constructs all temporal-column pair graphs directly from the Rule 73 truth table for periods one, three and five. It extracts the sole directed-cycle-bearing component in each, counts \(4\), \(19\) and \(49\) vertices respectively, computes the degree-four and degree-forty-nine characteristic determinant coefficients using integer traces and Newton identities, and compares them coefficient by coefficient to the factorization in `RESULT.md`. It gives exact fifth-cycle counts to length fifty-five and checks their integer divisibility. Its spectral comparison uses **integer** Collatz–Wielandt inequalities: the period-three lower bound is greater than \(3/2\) and the period-five upper bound is smaller than \(7/5\); its displayed floating-point approximations are informational only.

`verification/direct.py` independently applies the local rule five times to **every** binary ring of lengths three through seventeen, subtracts fixed points, divides by five, and checks each resulting primitive-five orbit count. It verifies the two length-eleven and length-twelve primitive-five seed trajectories, the allowed length-three and length-four stationary loop words, and several actual concatenations of these loops, testing every local space-time constraint. This checks the finite exceptional cases and supplies constructive witnesses, but it does not by itself replace the all-length proof.

The `.out` files reproduce the actual output from checks executed with these exact scripts. The proofs for unbounded ring length are the closed-walk bijection, the full exact finite adjacency determinant, and the loop-splicing argument. No external independent audit has been performed.
