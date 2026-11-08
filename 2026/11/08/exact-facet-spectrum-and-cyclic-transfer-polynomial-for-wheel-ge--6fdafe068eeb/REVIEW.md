# Scientific review: maximal general-position sets in wheels

## Correctness — PASS

The construction and proof have four independently inspectable steps. The wheel's diameter-two metric gives exactly the cyclic prohibition of 111 for hub-free subsets and forces the hub-bearing rim subset to be a clique. Vertex insertion is blocked exactly by isolated zero-runs, or double-zero runs flanked by two 11-runs. Counting closed block walks with the two-state matrix gives the coefficient-extraction formula by the formal trace/log-determinant identity; the run bounds yield both spectrum endpoints and each intermediate size by explicit cyclic words. The exceptional 4-rim opposite pairs and the complete 3-rim wheel are handled separately. The standalone verifier reconstructs distances and checks all configurations at indicated small orders. Risk: exhaustive finite tests do not prove the general case; the direct structural and trace proofs do.

## Originality — PASS, with literature risk

In the primary 2020 wheel paper, Theorem 4.1 gives maximum cardinality and uses 111-avoidance for maximizing sets. Its argument neither counts all inclusion-maximal configurations nor treats lower-cardinality facet gaps. The 2023 lower general-position paper formalizes the minimum facet size but discusses other named classes. The 2024 general-position-polynomial paper provides a graph-join formula that covers the polynomial counting **all** feasible subsets, so that assertion is excluded from the contribution. The new result instead enumerates only inclusion-maximal sets at each cardinality, giving a cyclic transfer function and all facet-size gaps. Database searches using wheel, maximal/general-position, facet, enumeration, and equivalent cyclic-word terms found no covering claim. A relevant October 2026 paper devoted to numbers of maximal general-position sets has not been inspected in full; whether it contains a wheel specialization is an unresolved priority risk.

## Mathematical value — PASS

The counting problem is the natural facet/enumerator refinement of the established wheel general-position parameter: it measures the number and sizes of *irreducible locally maximal configurations*, rather than only the optimum. The theorem resolves it for every wheel, identifies the unique pure cases, gives exact lower general-position values and constructs arbitrarily long gaps in the maximal-set size spectrum, using an explicit two-state transfer polynomial. Those conclusions are not determined by the earlier maximum-cardinality theorem or the all-set polynomial alone.

## Source limits and comparison

Sources examined include the full sections about wheel graphs in arXiv:2002.03108, the lower general-position preprint arXiv:2306.09965, the join polynomial proposition in arXiv:2401.05696, and the GP achievement-games preprint arXiv:2205.03526. The inaccessible full text for DOI 10.26493/2590-9770.1957.bc9 is material priority uncertainty. Unindexed equivalences are always possible. The evidence supports a provisional, not independent, assessment.

Self-review: passed. Independent audit: not yet performed.
