---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The 48 lines exhaust the claimed scope: on a projective line, fourth powers of up to four pairwise nonproportional binary linear forms are linearly independent in characteristic at least five (a Vandermonde minor after dividing by nonzero binomial coefficients). In the diagonal quartic equation each proportionality class must therefore have at least two nonzero coordinate forms, and an actual line must have at least two classes, forcing exactly two pairs. Same-family incidence follows by matching one exponent; for different pairings the four equations form a cycle with determinant a signed difference of powers of a primitive eighth root, so the zero tests specialize uniformly in odd characteristic. Independently expanding those determinants gives 48 vertices, 336 edges and reduced determinant 2^115*3^28*5^6. Frobenius multiplies the odd exponents by the residue of q; its inverse acts identically because odd residues modulo eight square to one. Using the successive differences e_i-e_(i+1) as a degree-zero basis, I imposed both Laplacian columns and Frobenius differences integrally and recovered the invariant factors from exact Hermite indices after adding each p^k times the divisor lattice. Successive differences of log_p(index) count factors of valuation at least k; the identity determinant supplies the complete prime support. All four residues, primary multiplicities and orders match the Finding, including equality for 3 and 7 and full 5-primary torsion for 5. The equivariant perfect graph pairing identifies the fixed group with the dual of the coinvariant group, hence their abstract factors agree.

## originality

PASS

The nonidentity fixed-group rows survive statement-level comparison. The identity row and the geometry are antecedents already excluded from the novelty claim. No inspected prior statement supplies the nonidentity fixed finite groups or a stronger equivariant integral description implying them.

## value

PASS

All three nonidentity actions have the same vertex cycle lengths, but the 5-primary fixed rank is six for residue five and three for residues three and seven. The complete integral table thus answers a well-defined descent question that neither line splitting nor the known abstract full group settles, and supplies local factors for comparing these configurations, not just tree counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
