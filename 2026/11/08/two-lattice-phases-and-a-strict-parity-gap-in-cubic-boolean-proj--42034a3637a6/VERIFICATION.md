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

# Verification
The exact finite identity is checked against independent binomial and character-enumeration implementations in `verify_cubic_projection.py`. Run from a directory containing the file using `python3 verify_cubic_projection.py`, with Python 3.10+ and the freely available `mpmath` library installed for high-precision asymptotic diagnostics. Its exact-rational tests use only the Python standard library.

The run completed with these diagnostics:

```
EXACT_BINOMIAL_BOUNDARY_IDENTITIES_PASSED 148 dimensions
INDEPENDENT_WALSH_CHARACTER_ENUMERATION_PASSED 8 dimensions
HIGH_PRECISION_LATTICE_PHASE_DIAGNOSTICS_PASSED 6 dimensions
ALL_CUBIC_WALSH_PROJECTION_CHECKS_PASSED
```

For all \(3\le n\le150\), exact rational arithmetic compares two distinct finite expressions for the degree-three Walsh projection constant. Directly summing all cubic Walsh characters checks dimensions \(3\le n\le10\). For \(n=1000,1001,3000,3001,5000,5001\), the normalized remainder agrees with the claimed phase function within the stated diagnostic tolerance. Finite checks do not verify all dimensions; the proof in `RESULT.md` establishes the asymptotic by local expansions and cusp-summation estimates. No independent audit or third-party certification is claimed.
