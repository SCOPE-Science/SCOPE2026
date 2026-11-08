# Review: two macroscopic avalanche bands on \(K_{3,n}\)

## Correctness — PASS

The assertion is for each integer \(n\ge2\), the standard undirected Abelian sandpile with one sink in the three-vertex part, one grain added to a *different* vertex in that part, and a uniform recurrent initial state. The proof derives the recurrent-state criterion directly from the one-pass burning test, counts exactly \(n^2 3^{n-1}\) recurrent states, and partitions all source additions by the initial hub height and three populations of leaf heights. The inactive, single-hub, two-hub, and second-source-toppling cases exhaust all possibilities. Their disjoint counts sum to the displayed polynomial. Nonnegative integer coefficients and total mass are independently checked. The binomial decompositions prove the two-atom weak limit with the correct conditioning and the exponentially rare maximum event. The separate `verify.py` program exhaustively tests every stable configuration at \(2\le n\le7\), independently simulates the burning and source processes, and checks polynomial normalization at \(2\le n\le80\). Finite tests are corroboration, not proofs of the statements for all \(n\).

## Originality — PASS, within examined evidence

The exact **fixed-hub-source toppling-count polynomial** and its conditional two-band limit have not been identified in the checked sources. Dukes–Le Borgne, arXiv:1208.0024 (sections 1, 3–5), gives the relevant complete-bipartite recurrent classification and decorated-polyomino statistics; it does not give this fixed-source principal-avalanche enumeration. Aval–D'Adderio–Dukes–Le Borgne, arXiv:1307.7740 (introduction, recurrence/cyclic-lemma discussion), concerns operators on configurations, not the claimed source-resolved distribution. Austin and coauthors, arXiv:1605.02713 (introduction and graph-family theorem sections), cover avalanche polynomials for trees, cycles, wheels, and complete graphs, not this \(K_{3,n}\) formula. Selig–Zhu, arXiv:2409.11811 (model and recurrent-characterization sections), treats bipartite stochastic and deterministic recurrence, not this source-resolved two-wave law.

Accessible earlier mathematical-physics findings were compared by implication, not title: a general adjacent-sink-source full-system avalanche identity gives only an extreme coefficient and does not yield the fixed-hub polynomial here; a \(K_{a,b}\) calculation for a source in the part opposite the sink gives full-system counts and an expectation but not the two-band hub-source law; the triangular-book source polynomial concerns \(K_{1,1,n}\), not the nonisomorphic \(K_{3,n}\), and its one-wave result does not imply this two-wave formula. published-finding corpus searches with the graph, source, principal-avalanche, polynomial, and asymptotic aliases did not surface an implying theorem. Absence from searches does not prove global novelty; an independently undiscovered equivalent avalanche calculation remains a historical-priority risk.

## Mathematical value — PASS

The recurrent-state census is known in general, but that alone does not determine the source-specific dynamical avalanche law. The exact polynomial distinguishes separate one- and two-hub waves, a source that topples twice, and explicit binomial coefficient strata; the conditioned law reveals two separated macroscopic activity scales instead of a single size law. This is a concrete, natural dynamical invariant of a canonical dense bipartite sandpile, with a physically meaningful comparison to rare-avalanche and finite-size scaling questions. Its scope is one particular sink/source class and does not imply generic power-law scaling.

## Limits of review

The paper comparison is a finite set of materially examined primary sources, not a universal priority certification. This analysis is not an independent scientific audit. The computation checks finitely many graphs and does not replace the complete burning/counting proof.

Self-review: passed. Independent audit: not yet performed.
