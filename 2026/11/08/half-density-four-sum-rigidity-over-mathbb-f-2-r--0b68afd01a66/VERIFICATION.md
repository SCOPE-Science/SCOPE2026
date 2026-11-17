---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The pinned RESULT.md treats 0 by pair-sum pigeonhole for m>=8. For a nonzero missing g, full/single/empty fibers of V/<g> satisfy 2f+s=m and z=f; f=0 forces vanishing second differences of a transversal graph and hence an affine hyperplane. If f>0, a sum-free set around a full fiber forces f>=m/2-1; a four-vertex zero-sum collision rules out f=m/2-1 and, for m>=16, f=m/2. At m=8 remaining occupied quotient four-set must be affinely independent, giving exactly 15*56=840 exceptions with one omitted g. Hyperplane direction four-sums are full for direction dimension>=3. Independently enumerated all 12870 eight-sets: covering 12000, missing-one 840, missing-eight 30, 56 exceptions for each nonzero g. No finite r=5 sampling substitutes for the all-rank proof. Domain r>=4, four distinct summands, exactly half density.

## originality

PASS

PASS best-of-knowledge for unbounded-rank r>=5 inverse classification. Roth-Lempel 1992 and Bajnok 2014 give restricted four-sum size thresholds, not structure of every equality-case obstruction. The published October 11 four-cube Walsh-spectrum census already determines the 840/30 finite exceptional counts under equivalent complementing-translation terminology; this r=4 component is credited and not claimed new. Later Chen-Huang 2026 torsion-size requirement excludes F2^r. An unlocated general restricted-sumset inverse theorem remains a historical priority risk.

## value

PASS

The equality case at the sharp half-density restricted-four-sum critical number is a natural inverse problem; r=4 gives genuine extra exceptions, while an exact sharp structural transition at r=5 classifies every extremizer in infinitely many groups. This is neither routine threshold substitution nor an arbitrary small census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
