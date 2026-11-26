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

At universality index 2 the shortest length is 2σ: two complete greedy arches require σ letters each. At that length the arches are permutations, and conversely any two permutation arches cover every ordered pair and miss xxx. For first arch increasing, length-three subsequences break into disjoint two- and three-symbol supports. An ascending pair contributes 4 and a descending pair 3. In lexicographic order the six local triple counts with all symbols distinct are 5,5,5,4,4,4. Thus the excess over 3 binom(σ,2)+4 binom(σ,3) is the sum of two nonnegative counts; the pair-count excess is already strictly positive unless Q reverses P, where both vanish. There is one word per first permutation. Uniqueness for simultaneous extremality follows at length three and existence follows from Adamson et al.'s all-length result. Independent incremental distinct-subsequence replay (python3 /workspace/branches/independent_checks.py 3) verified both local tables and all normalized second permutations at σ=2,…,8; the local support argument proves the universal claim.

## originality

FAIL

The exact strongest equality statement is covered by a distinct indexed theorem: the one-switch permutation-arch result gives it as the immediate a=b=1 case, and even counts all the absent triples for arbitrary Q. The covering record is in a later-dated catalogue path; this verdict is about demonstrable coverage now, not a claim that the assigned result was copied or that catalogue dates establish discovery priority. The earlier Adamson et al. general theorem by itself does not classify equality.

## value

FAIL

Classifying all shortest extremizers would address a meaningful equality question left open by the non-strict inequality, but the exact result is already available by the one-switch specialization. The frozen claim adds no extremal case outside that coverage, so there is no distinct valuable finding to repair here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
