---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Deletion of one of the two rows maps codewords injectively into F2^3, hence maximum 8. At equality each code is graph of a bijection f:F2^3->F2^3 whose difference-sum x+f(x) is also bijective: exactly an orthomorphism/complete mapping of additive group F2^3. An independent exhaustive enumeration of all 8! maps found exactly 384 such complete mappings and checked all 384 are affine, 48 with zero. These give affine cosets of 48 linear 3-spaces. Read pinned verifier: independent maximum-clique census 384, three-space census 1395/48, GL2*GL3 group sizes6*168 and stabilizer21. The completeness is over ALL eight-word codes, not a sampling of linear spaces; finite exhaustive bijection enumeration is a proof for exactly this finite domain.

## originality

FAIL

FAIL — the complete mapping reformulation is exact, and Bors–Wang, Compositions and parities of complete mappings and of orthomorphisms (arXiv:2207.09642, Theorem 1.1.2 F8 exception), already confines every F8 complete mapping to affine AGL3(2), directly implying every equality code affine. Bedford et al. 1999 explicitly enumerate 384 complete mappings of each noncyclic group of order 8, including additive F2^3. These are stronger/equivalent older assertions after simply writing a maximum code as a graph and applying row puncturing. The exact 384, affinity and 48 zero-containing linear examples are therefore covered, not original in an independent mathematical sense. Group orbit/stabilizer follow routinely from the order-seven linear maps and this same classification.

## value

FAIL

FAIL — the enumeration and rigidity classification are mathematically correct, but translate a known complete-mapping theorem and a known 384-count table into rank-code notation. The change of vocabulary, small finite verification and routine left-right orbit computation do not supply independently unknown or motivated additional structure sufficient to rescue the full final claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
