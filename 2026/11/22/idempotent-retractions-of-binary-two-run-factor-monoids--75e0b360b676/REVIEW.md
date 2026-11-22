# Scientific review: idempotent retractions of binary two-run factor monoids

## Correctness — PASS

The proof constructs and proves minimality of the proper-prefix recognizing DFA, classifies nonidentity idempotents by initial runs and first change of symbol, gives explicit inducing words for every counted idempotent, and counts disjoint killed-domain/fixed-state families. The exceptional cases with a unit-length run are treated separately via two explicit retraction classifications and an anti-isomorphism cross-check under reversal. The rank statement is independently checked for all cases. Both self-contained verification programs independently enumerated entire finite monoids for all one hundred parameter pairs with parameters from one through ten and reproduced all counts and (where applicable) explicit idempotent transformation sets. The infinite claim rests on the structural proof rather than finite extrapolation.

## Originality — PASS, with priority risk

The closest substantive earlier theorem is Gusev–Maslennikova–Pribavkina's 2013 principal-ideal syntactic-complexity theorem, which already determines the total number of transformations (and is credited). Its prefix/suffix normal forms are a potential source of derived information, but the reviewed theorem and proof do not calculate idempotence under composition, list the fixed-state retractions, or derive the idempotent density. The 2017 regular-ideal bound is for extremal transition semigroups and likewise does not cover this invariant. The 2023 syntactic-monoid learning paper develops inference methodology, not this special-family classification. The relevant indexed mathematical claims and exact-phrase literature searches showed no directly equivalent structural enumeration; search absence alone is not regarded as proof of novelty. An unindexed older equivalent or an unstated consequence developed elsewhere remains a real priority risk.

## Value — PASS

Composition-idempotents are canonical stabilization transformations, not an artificial selected subset of a monoid. This exact family is a standard two-run pattern-detection construction for which only the total syntactic complexity was previously cited. The result supplies a complete structural and enumerative refinement, classifies all nontrivial idempotents as two-point-image retractions, and isolates a nontrivial change of the limiting stable-transform fraction from one-half to three-fifths. Its scope is limited to binary principal ideals and its implications for learning algorithms are not claimed as proved.

## Closest sources and limitations

- https://arxiv.org/abs/1304.3307 — Theorem 1 and exceptional cases; total monoid size already covered, rank-two idempotent classification not found in reviewed primary text.
- https://doi.org/10.1007/s00224-017-9803-8 — broad upper-bound and extremal-witness results, not the present idempotent spectrum.
- https://proceedings.mlr.press/v217/dieck23a.html — current motivating syntactic-monoid inference context (proceedings published 2023-07-05), with no idempotent enumeration in the inspected manuscript.

Self-review: passed. Independent audit: not yet performed.
