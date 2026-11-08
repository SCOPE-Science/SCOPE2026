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

# Reproduction and scope

From a directory containing the packaged files run:

```sh
python3 verify_members.py
python3 verify_local.py
```

The first verifier uses only the Python standard library. It constructs cubic-extension fields over prime fields of sizes 2, 3, 5 and 7, constructs normal bases, lists every projective parameter and every rational point of the corresponding plane, tests membership, verifies the unique rational singular points, and compares counts with the claimed q-dependent norm strata. Expected terminal lines:

```text
FROBENIUS_CUBIC_STRATA_PASS 2 (1, 0, 1) 2 {'smooth': 7, 'irreducible_singular': 7, 'reducible': 1} singular_point_counts [4]
FROBENIUS_CUBIC_STRATA_PASS 3 (1, 0, 2) 3 {'smooth': 26, 'irreducible_singular': 13, 'reducible': 1} singular_point_counts [4]
FROBENIUS_CUBIC_STRATA_PASS 5 (1, 0, 1) 5 {'smooth': 124, 'irreducible_singular': 31, 'reducible': 1} singular_point_counts [7]
FROBENIUS_CUBIC_STRATA_PASS 7 (1, 0, 1) 7 {'smooth': 342, 'irreducible_singular': 57, 'reducible': 1} singular_point_counts [7]
```

The second verifier requires SymPy and checks identities for the unique characteristic-not-three singular point, exact nodal quadratic form, characteristic-three cusp normal form, and determinant-nine derivative matrix. Its expected output:

```text
SINGULAR_POINT_IDENTITY_PASS
NODE_LOCAL_FORM_AND_DISCRIMINANT_PASS u**2*v + u**2 - u*v + v**2
CHARACTERISTIC_THREE_CUSP_FORM_PASS
TORUS_GRADIENT_MATRIX_PASS 9
```

## What is and is not established computationally

The enumerations cover four prime fields; they are not exhaustive over all fields or all extensions. The theorem for arbitrary prime powers relies on the explicit general algebraic proof in RESULT.md. The published cyclic-cubic irreducibility lemma is cited. No independent external audit has been carried out.
