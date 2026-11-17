# Review of the exact friendship-graph oscillation-basin theorem

## Correctness — PASS

The graph and synchronous open-neighbour threshold-two rule are explicit. The pivotal lemma is that at hub colour \(h\), only petals of type \(\{h-1,h\}\) can change and each becomes monochromatic; stalling cannot create a new successor-coloured hub neighbour. The four successive hub tests, followed by a monochromatic-petal census, prove \(T^6=T^3\) with sharp entry times. Inclusion--exclusion of four precisely stated failure events gives the exponential generating function for the fixed basin; its coefficient computation supplies the closed count. Time-zero fixed and primitive-three-cycle counts are obtained independently. Graph-based exhaustive enumeration covers \(199287\) labelled states through five petals, and a separate finite quotient with tagged petal types checks the global identity on \(2187\) capped-count classes; symbolic weighted counting matches for every \(1\le k\le27\). The infinite-family conclusion relies on the constructive proof, not finite testing.

## Originality — PASS (qualified)

Fisch--Gravner--Griffeath (1991) introduced general contact-threshold excitable cellular automata and emphasized lattice spiral phenomena. Durrett--Griffeath (1993) refined lattice stable-periodic-object threshold analysis. Their inspected rule descriptions and principal results do not present a labelled basin formula for finite shared-triangle friendship graphs. Gravner--Lyu--Sivakoff (2016), especially its general-graph Theorem 3, applies to the one-neighbour threshold; replacing it by two changes the local transition rule, and its topological criterion does not imply this four-test inequality or exact count. Bello--Sivakoff (2021) studies infinite regular trees, not finite graphs with repeated triangles. The closest accessible historical findings concern threshold-two cyclic dynamics on complete bipartite graphs and other automata, not this hub-petal mechanism. Indexed published-claim searches for the precise graph/rule, equivalent formulations, and numerical counts did not reveal a covering theorem; this is limited evidence, not a proof of global novelty. Less-indexed literature remains a residual priority risk.

## Mathematical value — PASS

The object is a natural minimal network with multiple triangular feedback loops and many degree-two cells, while the threshold equals the entire peripheral degree. The result gives a complete infinite-family eventual-period classification, a sharp global settling-time cutoff, exact labelled attracting basins and periodic-point populations, and a quantitatively sharp rare-fixation law. The nontrivial point is that almost all states are attracted to three-cycles even though the initially periodic three-cycle population is exponentially sparse; the coefficient \(k/3+3\) distinguishes the dominant obstruction caused by a missing threshold in one phase. This invariant is useful in analyzing finite deterministic excitable-media dynamics and graph-motif effects, not merely a small instance or a numerical recomputation.

## Scope and remaining risks

The theorem concerns only the stated synchronous rule and finite friendship graphs. It does not settle general threshold-two graph automata or an exact first-entry-time distribution. The original 1991 and 1993 papers and the 2016, 2021 primary works were inspected at their rule descriptions and relevant result sections; comparison is not a claim that every historical paper was read. External independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.
