---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The group generators minus 1 are square-zero and their squarefree monomials are a basis. Linear-leading elements are images of a variable under a filtered automorphism and have rank 16. For Q=z1z2+z3z4, every monomial of degree at least three is divisible by one of the four derivatives of Q; successive substitutions starting at degree two produce the prescribed higher terms without changing earlier degrees. The homogeneous rank is (1+4+1) times 2. For Q=z1z2, normalize its coefficient by a unit, then shift z1 and z2 by the two coefficients in the square of the three-variable ideal. Their product vanishes by degree; this leaves Q+γz3z4z5 with γ measured by Q∧a3. For nonzero γ the tensor differential has homology dimension (4−2)(8−2)=12, giving rank 10 instead of 8. With cubic leading term, the top-degree output is already spanned by products with degree two; coefficients of degree four only add to that spanned output. The degree-four output has alternating rank 2 or 4, and the scalar input contributes one further dimension. Quartic/top leading terms give 2/1. Counting alternating forms by radicals and their nondegenerate quotients gives B2 and B4; the nonzero wedge functional has one fiber of size q^9 per value, and the free quartic and quintic coefficients contribute q^6. All counts sum to q^31. Independently, python3 /workspace/reproductions/rank.py used multiplication by XOR translation in the group basis for all 131203 higher-term choices on canonical nonlinear leading forms over F2, weighted by their leading orbits; the resulting binary counts agree term by term. The all-q argument is algebraic, not extrapolated from binary computation.

## originality

FAIL

The augmented-ideal census and mixed criterion have exact mathematical coverage in a distinct indexed all-algebra census. That catalogue entry is later-dated than the frozen record: the finding fails as a distinct result in the compared corpus, not on a finding that the catalogue entry preceded the frozen result or that the frozen author derived it from that entry.

## value

FAIL

The mixed rank jump is a natural, scientifically useful invariant, and the all-field proof and finite check have replication value. As a separate claimed finding the frozen census adds no rank, stratum, or count beyond the matching all-algebra census, so it does not establish a distinct useful contribution on the present evidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
