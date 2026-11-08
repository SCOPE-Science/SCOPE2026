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

# Reproducible verification

The exact rational verifier `verify.py` derives the coefficient polynomial from the explicit lattice-point count, computes its Newton finite-difference representation, and converts to the magic basis by a triangular identity. The full small-parameter vectors, six finite negative certificates, Bernoulli anchors, and formula spot-checks are covered.

Execute `python3 verify.py` with Python 3's standard library; the actual tested output is:

```text
VERIFY_OK 176 exact rational checks
positive low range q=1..8; negative finite range q=9..14; analytic four-residue threshold q>=15
```

The all-integer conclusion depends on the proved ratio bound for Bernoulli numbers and its induction across each residue class. Computation checks only finite identities and starting certificates. No independent audit or machine-checked infinite formalization was performed.
