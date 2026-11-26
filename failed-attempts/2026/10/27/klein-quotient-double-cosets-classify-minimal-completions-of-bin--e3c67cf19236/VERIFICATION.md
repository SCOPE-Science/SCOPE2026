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

H-fixed configurations are binary subsets of the quotient. In the Klein quotient every two-point subset is stabilized by translation by the difference of its elements; precisely the singleton and triple subsets have trivial stabilizer, and each family forms one orbit. A rule restricted to H-fixed inputs has no active neighborhood if the pattern is inconsistent on cosets; otherwise it has one projected active pattern. Units restrict to units. The exclusion of the diagonal collapse can also be checked directly in the quotient. Its first nonunit factor after the initial units must have exactly the corresponding cross-orbit pairs as its nontrivial kernel, up to a unit, by transitivity on those pairs. A lazy map with a constant active pattern merges the two constants, so cannot be such a factor. A mixed binary pattern writing 0 either removes the lone 1 from every singleton (an impermissible collapse inside that orbit) or fixes the singletons. On any triple its one zero permits at most one matching mixed-pattern translate, so the map cannot shrink that triple to a singleton and hence cannot merge the two free orbits. The writing-1 case is complementary. For the general kernel rigidity argument, after composing the first nonunit with the preceding unit product its kernel is a nontrivial subrelation of the target kernel; the single orbit of nontrivial unordered pairs forces kernel equality. The two images are then isomorphic as equivariant quotients, and this isomorphism extends to a unit because the complements have the same multiset of orbit types. Distinct H give disjoint double cosets because a unit preserves every point stabilizer. Units recover each representative from any element of its double coset. The elementary-collapse generation and exception lemmas then give sufficiency: each remaining collapse is between the two exact-H orbits, and orientation and choice of bijection are conjugate by units. Finally, the elementary abelian 2-quotient has (2^r−1)(2^r−2) ordered independent functional pairs, with six pairs per kernel. Independent enumeration gave the listed kernel and orbit counts; it tests arithmetic and the quotient orbits, not the generation conclusion.

## originality

FAIL

The exact all-group statement is not printed in the inspected older papers, but it is a direct consequence of the earlier arbitrary-W rigidity lemma and the earlier exception classification, not a new rigidity or separation theorem. The necessity direction literally instantiates Lemma 3.9 at W=L∪S and uses the known quotient obstruction. Sufficiency immediately applies Lemmas 3.7 and 3.14. Distinct kernel labels separate under units, and Gaussian-binomial counting then gives the exact rank. The earlier Klein-only paper also explicitly gives the rank-one case and identifies its compulsory double coset.

## value

FAIL

The relative rank modulo all lazy maps is a natural invariant, and the all-supplement phrasing is a useful summary of its known structure. But the exact missing-generator condition is already forced by the prior arbitrary-supplement lemma and exception list. The remaining orbit count, disjointness of different stabilizer labels, and Gaussian-binomial evaluation leave no independently unresolved precise invariant in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
