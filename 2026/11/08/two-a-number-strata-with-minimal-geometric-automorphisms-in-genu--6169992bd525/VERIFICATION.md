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

# Exact verification and limits

The accompanying `verify.py` requires Python 3 and SymPy, and was executed with SymPy 1.14.0. From the source files execute `python3 verify.py`. Expected output:

```text
a5=0 CARTIER_RANK=2 A_NUMBER=4 AUTOMORPHISM_BASE_MAP_IDENTITY_OK
a5=1 CARTIER_RANK=3 A_NUMBER=3 AUTOMORPHISM_BASE_MAP_IDENTITY_OK
CERTIFICATE_OK
```

For each fixed curve the code computes the polynomial coefficients of \(f(Ax+B)-A^7 f(x)\) modulo \(3\). It imposes that \(A^7\) be a nonzero constant in \(\mathbb F_3\), and that the difference be of the form \(h(x)^3-h(x)\) for \(\deg h\le2\). The reduced Gröbner basis in each case is \(\{B,A-1\}\). Exact Gaussian elimination modulo \(3\) checks the ranks \(2\) and \(3\) of the two displayed Cartier matrices.

The program does **not** establish the descent of all geometric automorphisms to affine base transformations; that necessary theorem is stated and cited as [1, Lemma 3.2(i)] and applied in `RESULT.md`. Nor is the all-coefficient Cartier rank formula inferred from finite examples: its proof appears explicitly in `RESULT.md`. Scientific priority has only self-review; independent audit is not performed.
