---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A direct counting proof gives the same polynomial without a magnetic determinant. A core matching of j edges covers j vertices of each color; its 2j attached leaves must be unmatched and supply x^(2j). Each remaining core vertex and its leaf give x²−a or x²−b according to color. With m_j the ordinary cycle's j-matching count and U=(x²−a)(x²−b), this gives Σ_j(−1)^j m_j x^(2j) U^(m−j), equivalently x^(2m) times the even cycle matching polynomial at sqrt(U)/x (interpreted polynomially). The cycle polynomial is p_(2m)−p_(2m−2), where p_n is the path matching polynomial, p_0=1, p_1=z and p_n=z p_(n−1)−p_(n−2); hence it is 2T_(2m)(z/2). Its paired roots give factors U−x²(2+2cos((2k+1)π/(2m))). Thus each quadratic in y=x² has B_k>a+b≥2sqrt(ab), two positive distinct roots, and no shared root with any other factor. Both a and b lie strictly between the two y-roots. Monotonicity of the roots in B_k puts the bracketing pair at the minimum B_k, and their sum and product give the squared gap and both limits. The limiting bands are the continuous images of the cosine midpoint grid; perfect matching also gives the nonzero constant (ab)^m. This checks all m≥2, including equal weights, and does not interpret the x gap as a gap of the same width in dimer activity.

## originality

FAIL

The alternating sunlet result reduces directly to the standard exact cycle matching polynomial: each core matching removes the same number of each pendant type, so the weighting changes only the single cycle monomer variable. The band's two endpoint roots and their separation then follow from the lowest squared cycle matching root and elementary quadratic identities. This is mathematical coverage by a classical exact polynomial and the matching rule, not a finding that the spectral comparators print the formula verbatim or that inaccessible papers cover it.

## value

FAIL

The finite-size separation of two bands in a decorated graph is naturally motivated. Here, however, the exact gap is only the known smallest squared cycle matching root plus the squared pendant contrast, as the elementary color-counting substitution shows. The stated scaling law is the immediate sine limit; it resolves no additional boundary effect beyond that inherited from the cycle. The result is a useful illustration of the substitution, not a distinct unknown invariant in the frozen scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
