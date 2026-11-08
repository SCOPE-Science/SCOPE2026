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

# Exact verification procedure

In the directory containing the supplied `.py` files, execute:

```sh
python3 verify_pairlines.py
python3 verify_direct.py
```

`verify_pairlines.py` models \(\mathbb F_{343}\) by adjoining a root of \(u^3+2\), constructs the rational parametrization and the internal-point nodes, enumerates all point pairs, derives the seven line characters, then explicitly generates all points on each eight-secant. It checks all four incidence double-counting identities.

`verify_direct.py` models the same field by adjoining a root of \(v^3+v+1\), directly tests the defining octic polynomial at every affine point, adds its sole point at infinity, scans all 117993 projective lines, and independently counts the eight-secant incidences and the 29 subfield points.

In the final package both programs successfully returned their respective `*_VERIFY_OK` markers, as well as agreeing numerical tables. No external package or data file is needed; there is no stochastic step. The computation checks only the specified \(\mathbb F_{343}\) instance, not arbitrary odd finite fields. The field polynomials are irreducible by explicit no-root tests over \(\mathbb F_7\); with the homogeneous equation and normalized-line loops this is an exhaustive finite certificate, not evidence of a generalization.

Independent mathematical audit is not performed.
