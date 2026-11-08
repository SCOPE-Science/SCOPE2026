# Scientific review

## Correctness — PASS

The central exchange lemma uses the exact JR witness of \(q\) previously unrepresented voters, degree \(q\) for every selected candidate under welfare optimality, and forced incidence overlap since \(kq\ge n>n-q\). The exchange replaces equal degrees, gains \(q\) represented voters, and loses at most \(q-1\). It proves strict monotonic coverage without overlooking ties or empty ballots. The reduction of EJR to JR follows because no candidate can have the support required for an \(\ell\ge2\) cohesive group. The sharp family has explicitly specified approvals, unique welfare optimum, JR alternative and exact score gap. The provided C++ checker passed all \(1{,}803{,}670\) eligible small election-size instances, and the sharp-family arithmetic for \(q\le100\). The infinite claim rests on the complete proof rather than the checker.

## Originality — PASS (qualified)

Full relevant material inspected: Dong (2026), arXiv:2609.08357, its model, hardness theorem and degree-three/degree-four reduction; Elkind et al. (2024), DOI 10.1145/3676953, its welfare price results, algorithms and motivating example; Schünke (2026), arXiv:2605.30490, its restricted interval-domain characterizations and positive algorithms. The classic JR/EJR reference was consulted at the definition/result level. The closest prior positive result under \(\le2\) approvals per *voter* and fixed \(k=3\) does not subsume the new condition \(\le\lceil n/k\rceil\) approvals per *candidate* for arbitrary \(k\): row sparsity and column sparsity are independent restrictions. Semantically related published records on assignment and apportionment did not assert this statement. Indexed searches found no exact theorem; residual risk of independently rediscovered elementary exchange principles remains. Search absence is not evidence of global novelty.

## Value — PASS

A newly motivated tractability boundary is extracted from a general NP-hard fair-and-efficient voting problem: the maximum per-candidate support controls whether **zero** utilitarian welfare needs to be sacrificed for EJR. The conclusion is constructive, works for every population and committee size and arbitrary individual approval patterns, and has a sharp one-vote degree boundary. This is a structural condition rather than a computational curiosity or a renaming of the earlier bounded-voter-ballot result.

## Scientific limitations and closest results

The statement does not treat EJR+, fractional Pareto optimality, or profiles with larger candidate supports on an instance-by-instance basis. Dong's full-domain hardness, Elkind et al.'s generic price-of-JR bounds, and Schünke's interval-domain algorithms remain distinct. Unindexed equivalent sufficient conditions remain a priority risk. No external independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
