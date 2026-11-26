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

Put N=X−I=uφ and M=Y−I=vψ. Their squares vanish and direct expansion gives (1+tr(NM))(N−M). If 1+tr(NM) is a unit this forces equality. Otherwise tr(NM) reduces to −1, so the reduced matrices cannot coincide (the square of their common reduction would vanish). Thus N−M has a unit entry and the scalar must be zero. In the latter branch both cross-pairings are units, so u and v/φ(v) form a split basis of the active plane and ker φ ∩ ker ψ is a free complement on which both vanish. The matrices on the plane are E12 and −E21. In the equality branch a basis of ker φ starting at u and a splitting vector for φ put N in the form E12. These are disjoint, valid even over residue characteristic two and with the zero complement at n=2. Independently count a single N by multiplying the counts T^n−(T/q)^n and T^(n−1)−(T/q)^(n−1) of unimodular u and admissible φ, then dividing by |R×| for unit rescaling. For fixed N=E12, normalize v₂=1 in the nondiagonal branch; then ψ₁=−1, and ψ₂=v₁−Σ_{j≥3}v_jψ_j. The first and remaining n−2 coordinates of v and the last n−2 of ψ are free; row 2 and column 1 recover the normalized factors. This gives exactly T^(2n−3) partners, in agreement with the stabilizer ratio. Reduction of GL is onto by lifting matrix entries and using the unit determinant criterion. Equivariance and transitivity give surjectivity and equal sizes of fibers on both types, with the types never mixed on reduction. The orbit-size ratios give the two lifting exponents and the exact density gives the stated asymptotics. The proof's phrase 'subtracting stabilizer cardinalities' is a wording slip; these counts use division, as the independent count confirms. The ten checker outputs were inspected, not rerun; they corroborate counts in small models, not the orbit and lift claims on their own.

## originality

PASS

The standard two-dimensional noncommuting braid pair and its simple field normal form are prior, as are transvection coordinates over commutative rings. The supported distinct result is the complete two-branch classification on the split primitive locus over arbitrary finite commutative local rings, with exact orbit sizes and type-dependent uniform reduction fibers. The primary results and bounded index comparison do not supply this classification or census.

## value

PASS

An ordered pair satisfying the braid relation is exactly the generator data of a B₃ representation on the specified primitive conjugacy locus. Counting it over finite local thickenings is a natural moduli problem; it resolves which residue pairs lift, distinguishes their fiber exponents, and shows that the answer ignores the multiplication structure even for nonprincipal or mixed-characteristic examples. The contribution is not the familiar 2D block by itself or a census in an arbitrarily chosen small ring.

The dated certificate retains the supplied scientific assessment, sources and limitations.
