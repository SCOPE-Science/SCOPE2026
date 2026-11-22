# Scientific review

## Correctness — PASS

The assertion is a single uniform theorem about the parity-restricted ideal family of \(k\) disjoint chains of length \(L\ge2\). Every ideal corresponds uniquely to an allowed prefix vector. A support can never contain comparable vertices if shattered. On a transversal, the only parity obstruction occurs when every queried threshold is at an endpoint and the corresponding forced label pattern has the wrong total cardinality parity. This yields the exact complete face polynomial. The integral topology calculation uses the augmented chain complexes of joins, explicit integral join cycles isolating each removed endpoint facet, and the long exact sequence of the pair. For the length-two odd-parity exception it uses the chain ranks of the cross-polytope boundary sphere. No inference from finite experiments is used for infinite parameters. Independent Python and C++17 enumerators reproduce all 24 small cases; a separate boundary-rank computation reproduces 18 finite topology cases. Risks: the usual reduced degree-\(-1\) convention is necessary for the one-chain length-two odd case, and this is stated explicitly.

## Originality — PASS within inspected evidence

Actual literature/database searches included "parity-restricted order ideals of finite posets VC shattering", "finite distributive lattices fixed-size order ideals shattering", "even cardinality down-sets shattering", "parity restricted order ideals of disjoint unions of chains full VC shattering polynomials and integral homology", and the alternate phrasing "even odd ideals in products of chain posets". A Campo–Erné (2018) studies downset counts and poset extensions, Early (2019) studies rank-unimodality in Cartesian *products* of chains, and Ghazi et al. (2021) studies general learning-dimension closure. Those statements do not entail the endpoint-forbidden full-transversal classification or its integral homology. Previously published investigations of unrestricted order-ideal online dimensions and maximal-antichain shattering were also compared by objects and implications, not title similarity; they do not impose the cardinality parity filter. The accessible earlier findings were used only for overlap exclusion, without re-auditing or revising them. A complete priority guarantee is not possible; unindexed exact formulas or alternate topological representations are residual risks.

## Value — PASS

The concept class is a canonical distributive-lattice family under one global congruence condition. Its ordinary width alone cannot distinguish the parity classes when \(L\ge3\), yet the complete face count and integral Betti number record exponential differences; the smallest chain length produces a genuine topological dimension shift. The result supplies a full all-parameter classification and an integral calculation rather than a single isolated finite count, and it provides an exact benchmark for parity-sensitive learning and topology of simplicial trace complexes. No downstream conjecture is claimed necessary for its value.

## Closest work and limitations

The papers by A Campo–Erné (2018), Early (2019) and Ghazi et al. (2021) supply adjacent order-ideal enumeration and learning-theoretic context but not the stated exact parity-constrained topological result. The analysis is restricted to equal-length, disjoint chains and total-cardinality parity, and does not claim a general-poset criterion, a universal online dimension, or a complete homotopy classification. The mathematical proof is self-reviewed and reproduced in bounded finite cases; historical priority and the integral argument have not received independent specialist assessment.

Self-review: passed. Independent audit: not yet performed.
