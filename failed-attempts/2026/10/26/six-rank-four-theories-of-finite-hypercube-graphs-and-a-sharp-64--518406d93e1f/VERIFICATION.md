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

The ordered tuple orbit is determined by counts of column patterns after translation by its first vertex; extending gives precisely all ordered nonnegative splits of those counts, including repeat vertices. The atomic diagram records clipped distances and the set of next types gives exactly the next EF rank. For remaining rank r, clipping each parent count at 2^(r+1) preserves the feasible splits clipped at 2^r: a saturated count can realize every one-small/one-saturated pair or two saturated children. The base cap 2 suffices for equality and adjacency. Thus all dimensions ≥16 have the same one-vertex rank-three profile and hence root rank-four type by transitivity. A new exact implementation compared nested profiles for dimensions 1–17 and found representatives 1,2,3,4,5,6 with identical profiles at 6–17, bridging the finite range to the lemma. Replay: branches/1d8a83cb-c95f-47f3-a4f3-3ad4945f8a6a/independent_profile_check.py and independent_profile_check_output.txt. Exact objects, not just hashes, were compared. Degree ≥2 and ≥3, two closed neighborhoods, diameter ≤4, and coverage by two radius-two balls are correctly ranked separators; the last fails from d=6 since 2(1+d+binom(d,2))<2^d. Hence the six classes and sharp in-family bound 64 are correct. Frozen source/output inspected only; attestation, prior independent audit, and Lean channels were not performed.

## originality

FAIL

A distinct same-day Resultary record explicitly classifies all finite Hamming graphs in the identical signature and rank, with the exact six binary classes as one branch. It covers both the precise cutoff and the optimal binary representative. This is a finding of actual coverage, not a claim of relative priority, derivation, or misconduct. The later exact duplicate is corroborating overlap, not evidence of earlier priority.

## value

PASS

As mathematics the cutoff is substantively motivated: it determines exactly what four quantifier rounds can distinguish in a natural unbounded graph family and identifies the sharp representative size. The proof gives explicit boundary witnesses and an exhaustive stabilization certificate. This does not overcome the separate originality failure from the stronger indexed classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
