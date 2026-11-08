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

# Reproducibility and verification

Run `python3 verify_witt_moduli.py` with a standard Python 3 interpreter. It uses only the standard library and does not fetch data.

The checker represents multivariate polynomials over \(\mathbb F_2\) as sets of exponent tuples and reproduces the following exact symbolic identities:

1. Writing \(\lambda=w^4\), the characteristic-two Witt-to-Artin–Schreier change of variables gives the quintic coefficients \(A=w^4\), \(B=w^4+w^2+1\), \(C=w+1\).
2. The polynomial \(F_T(L)=(L^2+L+1)^5+TL^6\) has exact degree ten in \(L\), with formal derivative \((L^2+L+1)^4\).
3. In \(\mathbb F_{256}\), the classifier obtained from the quintic formula agrees with the rational formula and the exceptional value has exactly two parameters, both roots of \(L^2+L+1\).

Expected output:

```
EXACT_WITT_TO_QUINTIC_IDENTITY_OK
DEGREE_TEN_SEPARABLE_FIBER_IDENTITY_OK
FINITE_FIELD_F256_CLASSIFIER_AND_SPECIAL_FIBER_OK
CERTIFICATE_OK
```

The checker was executed from the package source and produced precisely these lines. The universal geometric isomorphism criterion, degree-sixteen separability for the translation equation, and the root classification over every algebraically closed characteristic-two field are written mathematical proofs in `RESULT.md`; small finite fields alone do not prove these universal assertions. No independently assessed mathematical verification is claimed.
