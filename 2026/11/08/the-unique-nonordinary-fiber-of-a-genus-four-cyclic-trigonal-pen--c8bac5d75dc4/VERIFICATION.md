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

Run `python3 verify.py` with standard Python 3. The checker uses only `itertools`, `fractions`, and `math` from the standard library, and prints `VERIFY_TRIGONAL13_OK` on success. It checks multinomial coefficient extraction for the four-by-four block-diagonal Cartier matrix, the symbolic determinant identity, the characteristic-thirteen special rank, all smooth prime-field specializations, and the eight fractional-part carry counts. Exact polynomial and modular arithmetic are used; no floating-point approximations or probabilistic tests enter the checker. The proof extends the symbolic identities to every geometric parameter; finite specializations alone would not do so.

The classical Jacobi-sum/Stickelberger slope interpretation is an invoked theorem and is not independently implemented in `verify.py`. The script checks only the finite carry arithmetic needed after applying that theorem. Independent mathematical audit has not been performed.
