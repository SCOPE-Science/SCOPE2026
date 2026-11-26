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

The classified singular map takes the input identity to t², so identity preservation selects exactly involutory t, including t=id. From te=et=e, each idempotent fiber root is t-fixed and each transposition stays within one fiber. Each size-j fiber is specified by the number of transpositions 0 through floor((j−1)/2), yielding the exponent ceil(j/2); removing transpositions gives ordinary partitions. In the right-action convention a final singular factor of a word determines its output retraction up to unit conjugation unless the word has already collapsed to the constant identity map. A nontrivial t can only survive from that final singular factor; t=id cannot be newly produced for a retraction with all fibers of size 1 or 2, because no compatible nontrivial t exists. Conversely a fiber of size at least 3 permits swapping two nonroot vertices, and an even nonidentity involution (12)(34) with e constant onto a fixed point supplies the left collapse for all these types. The constant-identity endomorphism (e=id) is required; two unit generators suffice and products involving a singular map cannot produce a unit. This proves the formula for n≥5 and both generating conventions. A separate labelled census at n=5,6 checked all transformations against the pair conditions, conjugated pairs directly, compared each proposed generator-pair product on every transformation, and closed positive words. Counts were 391 and 2707 singular pairs, 12 and 21 singular orbits, and closures of 511 and 3427 elements from 10 and 16 generators respectively.

## originality

FAIL

The exact unital formula is not printed in the inspected prior full-monoid formula, but it is mechanically implied by the prior structural and enumerative results together. In the earlier plane-partition calculation, a permissible pair is a multiset of rooted fibers consisting of one distinguished fixed-point component and other fixed-point or two-cycle components with leaves. The condition t²=id deletes all leaves from those exact types, so its A and B component series specialize to z and z². The published fiber rule then gives z/((1−z)(1−z²)); the same multiset operator gives the claimed c_n and deleting two-cycles gives p(n). For t=id, the prior iff criterion of at most one nondistinguished fixed component per fiber becomes exactly sizes 1 and 2; excluding e=id leaves floor(n/2) essential rank-two types. The published rank reduction still works on the restricted pairs: the unit group is unchanged, c is unital, and the only collapsing operation needed uses an even rank-three left factor, available for n≥5 as (12)(34) with the constant retraction to 5. The earlier proof of nonessentiality already constructs a rank-three square root of t=id that is thus itself involutory. The exact rank follows by these restrictions, not by substituting a value into the full ambient rank number; it takes no new orbit invariant or essentiality test. The formula is correct, but the asserted distinct quantitative content is covered by this implication.

## value

FAIL

The unital monoid and its minimum generator number are natural, and the explicit formula can be convenient. However, this narrow exact invariant is already mechanically supplied by the previous multiset count and generator classification: omitting leaves, retaining witnesses that square to the identity, and counting ones and twos give the complete stated contribution. The extra labelled computations and explicit values do not supply a further independently useful unknown invariant or structural consequence. No separate surviving claim was established for a substantive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
