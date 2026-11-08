# Scientific review: conditional random-tree geometry

## Correctness — PASS
The fixed-matching contraction gives a bijection with Cayley trees carrying independent fair edge-lift choices, and uniqueness of perfect matchings removes double-counting. Direct inspection of the matching-edge geometry gives the claimed binomial-change exact path law, with its special \(L=1\) variance case. The Cayley two-point tail follows by path counting; bounded differences transfer it to lifted distances. The uniform all-pairs estimate, tight Cayley diameter and the measure-preserving quotient projection yield the claimed metric limit. The relative scaling is \(3/2\), not a claim of a differently normalized absolute Brownian CRT. A standalone exact enumerator independently passes 943 assertions for the finite identities.

## Originality — PASS, with historical-priority risk
The driving 2024 paper arXiv:2407.02958 treats optimization and recognition, not a conditioned uniform law or metric limit. Dong–Ge arXiv:2103.05294 explicitly covers fixed-matching spanning-tree enumeration, so the exact event probability is not claimed as independently new. The relevant 2023 conditioned-tree scaling source arXiv:2310.11530 conditions on leaves rather than matchability; it does not give the \(3/2\) path dilation. Searches for perfect-matchable Cayley trees, conditioned bipartite spanning-tree distances, contraction lifts, and the exact constant found no statement covering the combined conditional geometry. A prior related complete-split-graph tree construction involves a different graph and different conditioning, and does not imply the displayed distribution. Full historical coverage cannot be proved by these searches.

## Value — PASS
Perfect matchability is a natural but exponentially rare constraint on spanning trees. The exact conditional construction explains the resulting ensemble rather than only counting it; the nontrivial \(3/2\) metric factor transfers the complete random-tree scaling geometry and gives explicit two-point distance laws, while the conditioning event has exponentially small probability. This is a structural random-geometry result, not a parameter substitution or a known forest count presented as novel.

## Scope and risks
The law is restricted to uniform spanning trees on balanced complete bipartite graphs and relies on classical Cayley-tree convergence for the full measured metric limit. The leading exact counting probability follows from earlier work. No claim is made that bibliographic searches certify historical priority, nor that numerical enumeration certifies infinite asymptotics.

Self-review: passed. Independent audit: not yet performed.
