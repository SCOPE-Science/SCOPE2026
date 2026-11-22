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

The proof supplies the complete continuum argument. Run the standalone standard-library checker as `python3 check_inverse.py`. On the supplied package it reported `PASS: 2458 independent exact equalities, inequalities, inverse and monotonicity assertions`.

The checker uses independent stationary-generator linear systems to calculate the first two common-variance moments; compares them against rational beta-moment identities; checks the strict feasible wedge; tests unique rate reconstruction by nested bisection; and tests strict variance decrease along fixed-mean fibers. A rational example is \(a=2,b=1,D=1,r_1=4,r_2=6\), yielding \(S=16/25\) and \(K=13/1250\).

Limits: the finite test grid is not a proof for all positive parameters. In particular, the strict global two-crossing lemma and the weak endpoint limits are proved analytically in RESULT.md. No finite-sample identification or numerical conditioning guarantee is asserted. No independent external audit was performed.
