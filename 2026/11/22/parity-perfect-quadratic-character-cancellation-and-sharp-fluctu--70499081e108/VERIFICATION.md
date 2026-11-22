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

# Reproducibility and proof verification

Run `python3 verify.py` using only the Python standard library. The checker constructs \(24\) distinct nonzero residue pairs modulo five and the exact two-child transition. For each \(0\le j<24\), it verifies

\[
h^{\mathsf T}(T^4-T^2+4I)T^j e=0
\]

as an **exact integer identity**. Cayley–Hamilton, applied to this specific 24-dimensional integer matrix, proves the scalar identity for **all** \(j\ge0\). The checker also compares \(14\) dyadic levels against independently calculated integer Stern terms and tests later reduced recurrence values. This finite certificate is sufficient for the infinite recurrence only because the proof explicitly supplies the dimension and Cayley–Hamilton extension.

The sharp asymptotic extrema use a separate standard irrational-rotation argument: \(\alpha=(1+i\sqrt{15})/2\) has modulus two and normalized cosine \(1/4\), so its normalized angular rotation is irrational. This gives a dense phase orbit and extrema \(\pm\sqrt{8/3}\). The method does not claim full residue-vector distributions or an independent audit.
