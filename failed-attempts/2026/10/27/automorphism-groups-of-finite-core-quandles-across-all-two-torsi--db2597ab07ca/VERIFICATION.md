---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Products of core reflections give exactly the translations by H=2A. Normalizing that subgroup forces the same L on each coset, and substitution in 2y−x gives precisely 2b_c=L(2r_c) for a map fixing zero, with bijectivity exactly the permutation condition on C. The map δ:C→H/2H is onto with t fibers of size u. For fixed L, the zero fiber has (u−1)! permissible bijections and the other fibers have u! each; each of the ut−1 nonzero cosets has t lifts, and b_0 is fixed. The factor |A| is for undoing the normalization. This includes the trivial group, odd order, and exponent two. The factorial factor for rank-two mixed heights is 16 versus the group-automorphism ratio 8; for two heights at least two it is 64 versus 16. The other patterns give ratio one. Hand checks reproduce 128, 768 and 6144; the uploaded verifier was read, not run.

## originality

FAIL

The unrestricted normal form and entire order formula are already represented in distinct indexed results. The rank-two index follows from their formula and the standard two-primary group orders; it is not an uncovered theorem. The overlapping unrestricted records are later-dated, so this is a finding of equivalent catalog coverage, not a claim about who proved the result first or how the records are related.

## value

PASS

A complete stabilizer normal form and exact affine index address a natural structural question about even dihedral products, with a mechanism distinguishing elementary from higher two-primary factors. This evaluates the mathematical utility of that classification, not novelty relative to the duplicate coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
