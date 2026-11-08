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

The exact theorem is proven by deriving the finite-characteristic automorphism normal form, identifying the eight diagonal eigenvalue weights and then counting allowed pairs in the cyclic multiplicative group. The source's plus sign in a cubic term must be replaced by a minus sign, as shown explicitly in the proof and independently checked against defining multiplication.

Run `python3 verify.py` (standard library only) to reproduce the finite-field verification output. It constructs the complete multiplication table and the corrected eight-by-eight automorphism matrices, tests 64 ordered basis-pair product identities per selected matrix, checks their invertibility and the rank of the map minus the identity, and enumerates every torus parameter pair over cyclic groups of even orders. It also checks selected nontrivial unipotent parameters. These checks are finite tests, not a proof for all prime powers.

Run `python3 symbolic_check.py` with SymPy installed to verify symbolically over rational functions in seven algebraically independent parameters that all 64 basis products are preserved. Because the identities are rational polynomial identities with denominators dividing six, their formal validity transfers to every field of characteristic greater than three. This proves sufficiency of the displayed family, but completeness is established algebraically in the main proof, not inferred from the symbolic calculation.

The finite checker only constructs matrices over prime fields; extension-field cases are also checked at the multiplicative-group counting stage using cyclic groups with corresponding even orders. It does not enumerate all automorphisms directly, and no external mathematical audit has been performed.
