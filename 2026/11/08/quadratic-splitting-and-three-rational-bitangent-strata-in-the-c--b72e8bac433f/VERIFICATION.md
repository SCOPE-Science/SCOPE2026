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

The principal proof is in `RESULT.md`. It is uniform in every odd prime power, with the three exceptional singular parameters omitted. The exact identities and finite computations listed here are supplementary checks and do not, by themselves, establish a universal theorem.

With Python 3 and SymPy 1.14.0 installed, run:

```text
python verify_symbolic.py
python verify_prime_fields.py
python verify_quadratic_fields.py
```

Actual execution returned:

```text
VERIFY_SYMBOLIC_OK
VERIFY_PRIME_FIELDS_OK 201 {4: 106, 16: 53, 28: 42}
VERIFY_QUADRATIC_FIELDS_OK 29
```

The symbolic script checks all line-section identities, the rank determinant used for smoothness, and root-exclusion relations. The first enumeration uses all projective lines for every smooth parameter in twelve prime fields. The second independently implements arithmetic of \(\mathbb F_9\) and \(\mathbb F_{25}\), then tests all smooth parameters in those fields. Neither script depends on external mathematical databases or files; only the symbolic script uses SymPy. Exact arithmetic is used throughout. The scope does not include positive-characteristic-two curves, singular parameters, fields of definition of individual points of tangency, or independent human validation.
