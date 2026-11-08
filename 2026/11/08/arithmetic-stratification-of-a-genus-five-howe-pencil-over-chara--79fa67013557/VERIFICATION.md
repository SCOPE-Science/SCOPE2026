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

With Python 3, standard library only, execute `python verify_cartier.py` and `python verify_zeta.py` in the directory containing the two scripts. The first expands the cube of the genus-three quotient polynomial directly in a symbolic parameter over the seven-element field and checks the displayed coefficient matrix, the geometric nonzero-cycle rank implications, and all five prime-field cases. The second exhaustively computes quadratic-character fiber counts for both quotient and genus-five curve over fields with seven, 49, and 343 elements, comparing two irreducible polynomial presentations for each extension, and reconstructs all five genus-three numerator factorizations via Newton identities. Both scripts successfully ran and printed success markers.

These are exact finite checks; the algebraic proof of genus and the complete geometric-parameter rank classification uses Riemann--Hurwitz, a known prime-to-seven quotient isogeny, and the symbolic Cartier polynomial matrix. The zeta factors are determined by the exhaustive trace values and the Weil functional equation for each curve over the prime field. No computations establish the nonexistence of distinct geometric isomorphism classes or historical independence. Independent audit has not been performed.
