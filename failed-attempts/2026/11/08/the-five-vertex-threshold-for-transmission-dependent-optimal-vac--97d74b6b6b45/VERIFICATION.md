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

The objective is the expected uniformly seeded open-component size including the seed: conditional on a realization, multiplying by n−1 gives the sum of squared component sizes, equivalently the ordered connected-pair count. Independent exact enumeration of all labeled graphs, modulo vertex permutations, gave 1,2,6,21 connected classes. For the 28 nonexceptional classes, all 127 deletion-versus-fixed-witness comparisons were certified on the whole open interval by nonnegative coefficients after p=t/(1+t) and multiplication by (1+t)^d. There were 147 exact comparisons of the two objective constructions including repeated A/B checks. The two exceptional adjacency lists give the recorded factorizations: 4(R_A,3−R_A,1)=2p²(4p−1), and 4(R_B,2−R_B,0)=2p²(1−p)(4p−1); all strict competitor and orbit equality identities also match. Thus p=1/4 is the only interior switch and all tie sets are exactly as stated. The other classes have at least one permanent optimum, not necessarily a unique one. The endpoint exclusions are retained.

## originality

FAIL

The entire classification follows from a distinct same-day indexed two-objective result, not just the presence of the same exceptional examples. This is demonstrable coverage, not an inference of historical order between the two records.

## value

FAIL

The first-order change in an optimal preventive deletion is a natural finite classification, but the mean-only projection of the verified broader analysis leaves no new classification or meaningful new bound. The transformed-coefficient certificates are a useful simpler check of known comparisons, not a separately established substantive result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
