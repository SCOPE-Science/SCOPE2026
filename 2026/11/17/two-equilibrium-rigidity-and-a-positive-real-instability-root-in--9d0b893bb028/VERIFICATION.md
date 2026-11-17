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

# Verification and scope

The companion \(\texttt{verify.py}\) uses Python 3 standard library only. Run it from the directory containing this document and \(\texttt{RESULT.md}\):

```sh
python3 verify.py
```

The completed checks reported:

```text
POSITIVE_CHARACTERISTIC_ROOT 2 0.0530779492369
POSITIVE_CHARACTERISTIC_ROOT 3 0.0638598947468
POSITIVE_CHARACTERISTIC_ROOT 4 0.0638598947468
POSITIVE_CHARACTERISTIC_ROOT 6 0.0638598947468
VERIFY_OK exact_determinants 23 positive_real_root_cases 4
```

The exact-arithmetic calculations construct Jacobian characteristic matrices at positive equilibria with \(n\in\{2,3,4,6\}\) for five rational susceptible-population levels and check the exact determinant–derivative identity. Three more degenerate checks use \(A_i=0\) and verify a zero characteristic determinant. Four numerical checks locate strictly positive real characteristic roots at the lower equilibrium of the sharpness witnesses; these are evidence only, not proofs of an infinite-domain statement. All universal assertions follow from the algebraic and real-analysis argument in \(\texttt{RESULT.md}\). The original full model, including the auxiliary infected-population coordinate and its history constraint, was used in the characteristic calculations. Independent audit: not performed.
