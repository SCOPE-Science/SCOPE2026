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

Run `python verify.py` from the directory containing `requirements.txt` and `verify.py`, with Python 3.10 or later and SymPy installed. The program terminates with `All exact symbolic, full-state and sign certificates PASS` when all checks succeed.

The checks enumerate every possible three-particle bit configuration for each ring length between four and eight, verify directed strong connectivity by forward and reverse graph reachability, and build symbolic quotient generators directly from the two cyclic local transitions. Marked jumps that preserve a quotient orbit are included. An exact symbolic stationary and Poisson solve computes both cumulant rates and compares them against every stated rational formula. Independently, the program uses each full labeled generator, verifies the stationary Gibbs weights, solves its full rational Poisson problem at \(q=1/2\) and \(q=2\), and checks both cumulants. Finally, it checks the strict-noise numerator identities, the Sturm sign variations, the one-sign-change derivative patterns and the rational root brackets. All these checks were executed successfully on the package code.

The analytic proof relies on the exhaustive, specified finite generator construction plus the polynomial sign arguments. The discrete full-state computations cover only \(n\in\{4,5,6,7,8\}\). The tests at two recovery ratios corroborate but do not replace the symbolic all-positive-ratio identities. This package does not independently certify the originality claim or replace separate external scientific audit.
