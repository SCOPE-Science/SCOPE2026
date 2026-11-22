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

# Reproducibility

Use Python 3 with `verify_howe11.py`, `spectrum_28.csv`, and `parameters_91.csv` saved in the same directory. Execute `python3 verify_howe11.py`. The script enumerates 121 coefficient pairs, establishes exactly 91 smooth models, evaluates the elliptic quotient traces by eleven-term Legendre-character sums and recomputes all 28 polynomial types and coefficient frequencies. It independently counts \(\mathbb F_{11}\)-points on all smooth original octic equations and \(\mathbb F_{121}\)-points in two explicit quadratic residue models. It checks all 91 parameter records and every one of the 28 summary rows. The exact printed success identifier is `HOWE_F11_SPLIT_NONSPLIT_WEIL_VERIFIED`.

## Mathematical boundary

The explicit genus-three involution quotient decomposition is essential for the proof of all extension-field zeta numerators. Finite-field checking alone does not establish that general factorization. The enumeration is exhaustive over the 91 marked smooth coefficient pairs over \(\mathbb F_{11}\), but it does not classify unmarked isomorphism classes or fields beyond those of the displayed zeta polynomials. Independent mathematical validation has not been performed.
