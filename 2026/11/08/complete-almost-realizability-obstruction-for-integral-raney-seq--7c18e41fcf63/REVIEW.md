# Scientific review

## Correctness — PASS
All quantifiers are explicit: integer \(P\geq1\), \(R\geq1\), positive indices, arbitrary fixed positive multiplier, and arbitrarily large primes. Raney integrality follows from the ordered-forest generating function; the exact formulas for the first two terms and Lucas residues are reproduced in the proof. At prime indices the Dold numerator has residue \(P-R\), and at twice-prime indices along \(R=P\) it has residue \(P(P-1)/2\). In each forbidden case arbitrarily large primes contradict any fixed multiplier. The exceptional family is realized by a fixed point. The embedded exact-integer checker executed successfully with 513 congruence tests; this is corroboration, not an infinite proof.

## Originality — PASS within inspected sources
Closest: Zhang (2023), Theorem 21(1), disproves almost realizability for ordinary Catalan numbers, corresponding to the lone parameter \((P,R)=(2,1)\); his adjacent Motzkin and Schröder results concern different sequences. The full relevant sections, lemma statements and actual proof in the open arXiv manuscript were inspected. The Raney interpretations in Rusu (2021) and Liu–Pego (2014) motivate the parameter family but do not assert this dynamical classification in their available material. Actual published-finding corpus searches of Raney/Fuss–Catalan/Dold/realizability aliases and compatible semigroup families did not identify a dominating claim. The general Lucas and Dold ingredients are standard and unclaimed. Residual risk is an unindexed equivalent statement; absence from a search index alone is not a novelty proof.

## Mathematical value — PASS
This is the natural complete positive-integer parameter classification for a well-studied two-parameter tree-counting family, with the precise boundary between a genuinely realizable and non-almost-realizable family. The diagonal \(R=P\), where the standard prime-index obstruction cancels, requires the new separate twice-prime calculation; it is not merely numerical extension of the known ordinary-Catalan case. This may guide dynamical realizability tests for other parameterized combinatorial counts, without asserting an unproved theorem for those families.

## Limits and independent status
The result concerns only integer Raney parameters and does not address generalized real parameters or nonstandard notions of realizability. Primary source's theorem and proof support the comparison, but independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
