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

# Verification record

The program `verify_genus.py` is a standalone exact finite-field computation of leading-form evaluation ranks for six distinct points on a smooth conic in characteristic \(101\). Execution yielded `VERIFY_KUMMER_TROPE_UNION_OK ranks=1,3,5,6 local_delta=9 genus=129`. Generality follows separately from the fact that any six distinct points on a smooth conic impose independent conditions on sections of \(\mathcal O_{\mathbb P^1}(d)\) for \(d\ge5\), with ranks \(1,3,5,6\) at homogeneous degrees \(0,1,2,3\). The genus has a second algebraic check: the Cartier divisor \(D\) has \(2D\sim16H\) on the nodal quartic, so \(D^2=256\) and \(p_a=129\). This verification is not independent external audit.
