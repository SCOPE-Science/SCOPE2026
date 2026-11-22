# Scientific review

## Correctness — PASS

The graphs are explicitly defined on twelve labelled vertices each, and synchronous open-neighbor strict binary majority with incumbent tie retention is implemented directly. All \(4096\) states of each graph are classified by two genuinely different finite functional-graph algorithms: Python orbit-following and C++ indegree peeling. These agree on every printed first-entry/period category, total basin population, fixed state, primitive two-cycle count, consensus basin and sharp depth. Exhaustive orbit grouping under the complete graph automorphism groups verifies 5/26 and 14/3 fixed/two-cycle geometric class totals; Burnside summation supplies an independent group-accounting check. The state-space proof is exhaustive, not an extrapolation. The source code and reference JSON have been replayed and verified from the accompanying bundle.

## Originality — PASS (qualified)

Goles–Olivos already proves only periods one and two in the finite symmetric setting. More importantly, the published half-factor theorem for majority dynamics on line graphs **covers in principle the cuboctahedron's recurrent counts**, and those are not claimed as independently novel. That theorem neither classifies nonperiodic initial states nor implies that all cuboctahedral two-cycles have zero transient basin. The closest graph-specific published result uses a three-state excitation rule on the truncated tetrahedron; a separate exact result on the same two polyhedra concerns independence-complex homotopy, not majority dynamics. Published majority work on random and other finite graphs does not include this pair's full attraction/entry-time table. Exact-title, object, dual line-graph, numerical and alias searches found no covering result. Risk remains from unindexed tables or older inaccessible graph-specific treatments.

## Value — PASS

The two canonical Archimedean graphs have the same vertex count, yet their exact majority dynamics separate sharply: the cuboctahedral two-cycle basin consists only of its 40 periodic states, whereas 1,888 nonperiodic states flow into oscillation on the truncated tetrahedron. The 4-versus-5 sharp-entry gap and their symmetry-resolved orbit contrasts make this a motivated, completely resolved finite boundary example distinguishing recurrent-state enumeration from attraction basins. This is more informative than simply recounting finite fixed points; in particular, it demonstrates that a general classification of recurrent configurations does not determine how initial states flow toward those configurations. No extrapolation to an infinite graph family is suggested.

## Closest literature and limitations

Goles and Olivos (1980); Benjamini et al. (arXiv:1405.2486, initially public 2014-05-11); Fountoulakis, Kang and Makai (2020); published line-graph half-factor classification; published truncated-tetrahedral excitation census; published two-Archimedean independence-homotopy comparison. The 1980 original was accessible as an institutional abstract, not an inspected complete article. The claims rest on exact finite computational certificates; no independent external mathematical audit has been performed. Additional unindexed material could affect priority.

Self-review: passed. Independent audit: not yet performed.
