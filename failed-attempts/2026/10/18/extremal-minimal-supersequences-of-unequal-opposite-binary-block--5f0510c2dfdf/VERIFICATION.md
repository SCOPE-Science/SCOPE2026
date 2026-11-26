---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Minimality is equivalent to coverage by positions essential to at least one input. At length |A|+|B| both embeddings would be unique and would partition the positions. For a closest equal-letter pair of opposite owners, uniqueness forces an intervening position of each owner; both intervening letters must be the opposite binary letter, contradicting closest distance. At length one less, if one essential set has a deficit of one, the two sets partition the word. Every embedding of the deficient input inserts one letter into the same fixed essential subsequence. Two possible insertions in different gaps would force identical letters between the gaps and allow both insertions while omitting one supposed essential position. Two insertions in the same gap can replace that letter and an equal immediate neighbor, since every input run has size at least two; that also omits an essential position. Thus the embeddings are unique and share exactly one position. Greedy extremal choices locate the shared letter; a same-symbol letter next to it on the wrong side would allow substitution, forcing the claimed opposite-symbol end conditions. Conversely those conditions make the first a zeros and last b ones the only embedding of A and the first c ones and last d zeros the only embedding of B, covering all positions. The two cases have different Parikh counts and each has the stated binomial product. The singleton restriction is material. The independent checker independent_replay.py tested complete extremizer sets for 80 tuples, 6,888 extremal words in total, and excluded length |A|+|B| for the 16 tuples with exponents 2 or 3. The frozen checker and its output were inspected but not executed; finite checks do not prove the general bound.

## originality

FAIL

The full finding is demonstrably covered by a distinct indexed stronger theorem for arbitrary positive a,b,c,d, including both exact word families after specialization, not merely identical counts. The stronger record has a later displayed date, so this comparison does not establish historical priority. The evidence supports a failure of distinct coverage relative to examined results, not a finding that the proof is false or that the older inaccessible articles already established it.

## value

FAIL

The longest-length layer of opposite-block inputs is a natural extremal invariant. However, the frozen exact invariant, all its maximizers and its stated symmetries are already supplied by specialization of the stronger indexed theorem. A different proof of this restricted finding does not establish a separate valuable mathematical remainder; the submitted claim does not give a new length layer or settle a further regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
