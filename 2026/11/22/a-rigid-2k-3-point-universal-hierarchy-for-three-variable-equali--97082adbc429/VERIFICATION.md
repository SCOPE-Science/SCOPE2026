---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Adjoin equality at level 0 and the total relation at level h=K+1. The three pairwise merger levels determine every pure atom, with level 0 recognizing repetitions. For distinct entries the largest level occurs at least twice by transitivity and nesting. The ordered count is thus 1 all-equal, 3h one-repeated-pair, h equilateral, and 3·binom(h,2) one-closer-pair types. All are realized on the proposed comb: at level j its two new leaves and an older leaf give an equilateral triple, and the older cluster supplies a pair with any earlier merger i. Every universal class tree has at least one node with three children at each of the h levels, each contributing at least two to leaves minus one. Equality forces exactly one ternary branch at every level and no other branching. A type (i,j,j) then places the unique level-i branching node strictly below the unique level-j branching node. This is the extra restriction that forces the spine, not just the equality of branch counts. It fixes the labelled-level hierarchy up to isomorphism, including h=1, where the three leaves form the whole structure. A quantifier-free formula depends only on its complete atomic type, proving the stated single existential-block test.

## originality

PASS

The genuine overlap with parity-game universal trees is substantial: the degree-threshold recurrence inside the proof of Czerwiński et al.'s Theorem 2.3 gives the numerical lower bound at three leaves, and the argument uses only properties valid also without order. Thus the numerical lower bound is not a new independent contribution, and the small universal comb is closely analogous to an ordered universal tree. The contribution surviving comparison is the equality classification of the weaker, unordered profile-universal problem: every minimum host is forced to have its branching vertices on one chain. The known size bounds and ordered universality results do not give this characterization of all unordered hosts. Simple profile counting and the logical rephrasing are not by themselves credited as new structural results.

## value

PASS

For fixed merger levels one can ask which smallest hierarchies serve as a common fixture for every pure three-point test. The exact classification of all minimizers is a useful structural answer: having the necessary equilateral triples at every depth does not fix the fixture, whereas the mixed profiles force the spine. This is a uniform equality case for a motivated small-tree universality problem, not a sample census or just the specialization of the prior size recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
