---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Bubble-sort inversion removals preserve 321-avoidance, giving a length inv(pi)+inv(sigma) upper bound. Every 321-avoider splits into two increasing subsequences, so inv≤floor(n²/4), with one even-n maximizer and two odd-n maximizers. A forced first crossing of the middle letter makes each small-large pair reverse twice, giving sharp lower bound 2hℓ+h+ℓ. The unique odd diametral pair follows from the two max-inversion permutations. Independent full BFS on all 321-avoiders for n=1..6 reproduces 0,1,4,7,12,17 and odd uniqueness. Earlier published proof independently establishes diameter and the extremizer classification via weak-order meets.

## originality

FAIL

FAIL: published October 26 result determines exactly this all-n graph diameter, using the identical graph and an even stronger all-pairs weak-order metric formula. The prior proof identifies exactly the two maximum-inversion permutations at odd n; combining rank upper bound with its attained distance gives the submitted odd uniqueness. Alternative forced-crossing proof does not add a new theorem.

## value

FAIL

FAIL: the only substantive claim (diameter and odd antipode uniqueness) is a direct consequence of earlier published all-pairs distance and maximizer classification; the different proof is not a separately motivated new lemma or invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
