---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

Independence of size d in C_{2d} forces d cyclic gaps each >=2 with sum 2d, hence only parity shores A,B. The strict alpha<d definition therefore excludes precisely faces containing A or B; the simplicial complex equals ∂Δ_A^{d-1}*∂Δ_B^{d-1} exactly. Radial barycentric maps of these boundaries into augmentation spheres U_A and U_B are equivariant for vertex permutations; the join gives S(U_A⊕U_B). The half-turn on 2d coordinates is d transpositions. For even d it preserves each shore and its two fixed shore-constant vectors, giving (+,-)=(d-2,d); for odd d it interchanges shores and removes one + and one - constant eigenline, giving (d-1,d-1). A unit-sphere join is equivariantly S^{p-1}*S^{q-1}; quotienting the sign component yields the claimed actual homeomorphism S^{p-1}*RP^{q-1} for p>0 and RP^{q-1} for p=0 (only d=2). Since q is even, RP^{q-1} has integral reduced H_{2j+1}=Z/2 for 1<=2j+1<=q-3 and H_{q-1}=Z; p-fold unreduced suspension shifts these degrees to p+2j+1 and p+q-1=2d-3. Thus d=2 gives RP1=S1, d=3 gives S3, d=4 first 2-torsion and arbitrarily high d yield unbounded torsion degrees. Independent finite enumeration of all size-d independent vertex sets and separately anchored exact integer involution ranks agrees for d=2..8. Finite checks are corroboration; the gap and representation arguments prove the infinite family.

## originality

PASS

Best-of-knowledge PASS for the complete geometric central-half-turn orbit-space classification of BI_d(C_{2d}) at every d>=2 and its integral Z/2-torsion degrees. Bayer et al. (2022/2025) already state the exact two alternating maximal independent sets at threshold; Carnero Bravo (2026) and a prior 2026 dihedral study establish only nonequivariant sphere homotopy and orientation/rational quotient characters. These do not state or determine the actual equivariant sphere model and integral geometric quotient. The new result combines an equivariant radial join homeomorphism with an explicit parity-dependent half-turn eigenspace calculation to classify the canonical quotient. The construction is mathematically elementary once the two-shore complex is identified, so this is a focused exact structural classification, not a new general quotient theorem. No earlier checked published statement gives the all-d projective suspensions and their integral homology. The same finding returned by Resultary is a self-match, not independent priority evidence; a Nov 17 path-reversal projective-suspension theorem is later and concerns a different family. Historical priority remains qualified, especially by potentially unindexed or inaccessible equivariant sources.

## value

PASS

The central half-turn is a canonical involution of every even cycle, and its geometric orbit-space homeomorphism and integral homology are natural, fully determined equivariant-topology invariants. The quotient develops Z/2 torsion while its covering bounded-independence complex is a sphere and prior rational characters cannot detect the torsion; the sharp d=4 transition and unbounded sequence of torsion degrees provide a motivated structural distinction. The family-wise parity-sensitive geometric classification is independently useful, despite elementary ingredients, and is neither an arbitrary finite slice, mere parameter substitution nor a recomputation of a previously listed integral quotient table. It does not claim an all-group quotient theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
