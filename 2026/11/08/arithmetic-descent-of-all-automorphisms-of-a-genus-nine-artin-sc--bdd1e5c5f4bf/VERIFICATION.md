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

# Exact reproducibility

Run `python3 verify.py` with standard Python 3; no extra packages are needed. The script enumerates the points of \(E:y^2+xy=x^3+1\) over \(\mathbb F_2\) and \(\mathbb F_4\), checks the order-eight elliptic point and the multiplication-by-five Frobenius action, and verifies the group automorphism for both possible central lifting signs.

The script was executed with these lines:

```text
GF4_ELLIPTIC_GROUP_OK
FROBENIUS_ORDER_TWO_OK
DESCENT_C4XC2_AND_MINIMAL_F4_OK
CERTIFICATE_OK
```

The proof identifies the complete geometric group using Tafazolian's published classification (arXiv:2609.14830v1, Theorem 1.7 and Proposition 3.1). The standalone checker does not independently establish that classification, nor is finite testing represented as an infinite proof. The rest of the descent proof is algebraic and covers every \(\mathbb F_{2^r}\), \(r\ge1\). Independent mathematical validation is not performed.
