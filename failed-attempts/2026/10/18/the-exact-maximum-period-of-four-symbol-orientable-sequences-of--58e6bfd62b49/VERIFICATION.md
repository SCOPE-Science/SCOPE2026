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

Reconstructed the upper bound in the directed triple graph. There are 120 nonpalindromic reversal pairs. A cyclic word and its reverse give balanced disjoint circuits, so their union is balanced, and its indegree at each constant vertex is twice the indegree of the original circuit. The ambient indegree at each constant vertex is three, forcing at least u=4 omissions of the constant-triple type (more precisely, u>=4). For the twelve triples aab with a!=b, the ambient outdegree minus indegree is one at each triple, so missing arcs satisfy O_T-I_T=12. Each of the u omissions enters T once and never leaves T. Every other missing pair gives at most one outgoing arc except for the six pairs aabb/bbaa: both directions can start with a nonconstant repeated-leading triple only when both ends of the word are doubled. With r omitted pairs, this gives 12+u<=O_T<=r-u+6, hence r>=14 and m<=106. Independently read the supplied line and checked all 106 length-four slices of the word with its first three symbols appended: each occurs once and its reversal occurs zero times, also excluding palindromes. There are 14 unused classes, agreeing with the recorded list. The window check establishes the lower bound, not the upper bound.

## originality

FAIL

A distinct indexed result states the identical maximum under the identical definitions. It uses an integer-optimization proof route rather than the frozen counting argument and is dated later than the frozen record. This shows equivalent coverage at review time, not that the other record has historical priority. There is also an older distinct indexed lower-bound construction attaining 106 that explicitly leaves optimality open.

## value

FAIL

The natural invariant and the self-contained counting argument are mathematically useful, especially in explaining why the earlier witness is optimal. As a claimed new exact invariant, however, this finding has the same scope and value as the distinct exact indexed result. It does not establish a separate structural theorem or broader bound beyond what is needed for that covered fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
