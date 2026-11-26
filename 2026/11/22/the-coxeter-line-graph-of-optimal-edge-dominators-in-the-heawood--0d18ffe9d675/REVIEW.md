# Independent mathematical audit

## correctness

PASS

In RESULT.md lines 34–40, the unused points and unused lines of an edge dominator must be incidence-free. Three points meet at least six lines, which rules out size at most four and forces exactly two unused vertices per shore at size five. Thus each optimum is a matching. An unused point pair determines the unused lines, and the remaining induced graph has a forced edge followed by an eight-cycle for the displayed binary pair; transitivity gives 21 times 2 optima. I inspected the census and quotient logic in RESULT.md and the frozen support. An independent exhaustive run over 2^21 subsets confirmed all 17 all-dominator coefficients, the inclusion-minimal polynomial 42z^5+1246z^6+24z^7, and the maximal-matching polynomial 42z^5+168z^6+24z^7. The 28 exchange triangles each contribute a vertex of the quotient, and every original state yields an edge between its two containing triangles; the pairwise check verifies that the edges meet exactly for exchange-adjacent states. An independent isomorphism search checked every pair against the Fano disjointness graph, without assuming the displayed permutation. No one-edge replacement occurs; all roots have shells (1,4,8,16,12,1). The supplied programs were inspected, not executed.

## originality

PASS

Pass the supported distinct contribution: the full labelled dominance censuses and the exact two-edge exchange identification, not the existing Coxeter model, the standard edge-domination reduction, or the numerical minimum as a standalone claim. The strongest related comparisons do not give both the optimizer family and this adjacency rule; access limitations qualify this judgment.

## value

PASS

This resolves a natural optimizer-mobility question on the smallest projective-plane incidence graph: no single-edge exchange is possible, while two suffice and have a classical quotient geometry. The labelled minimal census independently separates optimal matchings from a large class of nonmatching minimal guards; these exact facts are useful benchmarks for incidence-graph domination and reconfiguration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
