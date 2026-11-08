# Scientific review of the six-leaf NOC census

## Correctness — PASS

Every clustering system on six fixed labels is uniquely specified by 56 optional nonsingleton proper clusters. NOC is tested using the exact overlap-witness condition; hereditary failure of this condition proves that the inclusion pruning removes no valid completion. At accepted leaves, Hasse parents are computed by checking all strict intermediate clusters, so the number with two or more parents is precisely the relevant reticulation statistic. Two distinct exhaustive C++ algorithms yield the same 9,654,368 families and all five per-reticulation counts; a third naive Python algorithm independently verifies orders two through four. The entire six-leaf certificate was replayed from supplied standalone files. Finite enumeration proves these finite values only.

## Originality — PASS, subject to historical priority

Lindeberg and Hellmuth's paper (arXiv:2609.13336, first public 2026-09-11, Section 5) defines the parameters and asks for enumeration, but supplies neither the six-leaf table nor a general recurrence determining it. A previously published classification counts only maximum-cardinality NOC systems, not all of them. Earlier binary phylogenetic network counts impose different indegree/outdegree assumptions. Mathematical-record, exact-number, alias, and prior-result searches did not locate a covering distribution. Although this strongly supports novelty, absence of search hits cannot establish universal priority. Relevant work not fully indexed remains a residual risk.

## Mathematical value — PASS

The counts answer a natural, explicitly posed finite enumerative question for canonical normal phylogenetic networks and give its full reticulation stratification, not merely a small example. Six leaves already produce millions of valid systems and all five attainable reticulation classes, so the exhaustive dataset can test prospective recurrences, structural decompositions, and asymptotic predictions. The refinement distinguishes families that an unstratified total obscures. Nothing is claimed about a general formula or a published paper-sized breakthrough.

## Limitations and closest literature

The original NOC realization theorem and the known classification of the extremal-cardinality subfamily are credited, not rediscovered. The six-leaf exhaustive computation does not settle seven-leaf enumeration or any broader asymptotic problem. Binary and nonbinary network classes must not be conflated. Priority and mathematical verification are not independently certified.

Self-review: passed. Independent audit: not yet performed.
