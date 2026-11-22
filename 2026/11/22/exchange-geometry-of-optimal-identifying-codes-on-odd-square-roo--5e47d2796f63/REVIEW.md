# Self-review

## Correctness — PASS

The minimum identifying-code size and the unique optimizer orbit are **known** from Gravier–Moncel–Semri [1]. For odd board size \(n=2m+1\ge5\), their optimum-support form is one isolated edge plus \(m\) disjoint four-vertex paths in the bipartite row–column graph. Counting row-pair and column-pair matchings establishes the optimizer count. Inspecting all possible one-cell removals establishes exactly two within-path leaf replacements, one internal central-edge replacement, and four central-edge replacements involving the isolated edge, for a total of \(7m\) disjoint legal replacements from each optimum. Thus regularity and the edge formula are all-order proofs. Two different exhaustive verifiers independently enumerate all \(\binom{25}{7}=480700\) candidate codes at board size five, check signatures and moves, and reproduce the 7200 optima, 50400 edges and exact ten-shell breadth-first-search distance spectrum. Known vertex transitivity makes the one-source diameter calculation global. The finite tests do not prove the infinite theorem.

## Originality — PASS with historical priority risk

[1] proves the static minimum size and unique orbit, which are credited and not new. [2] provides an edge-identifying-code equivalence for line graphs and a biclique lower bound, and [3] concerns cardinalities for rectangular products. Those results do not give a legal single-cell exchange classification, an all-odd-order degree formula or a 5-by-5 reconfiguration metric. The closest mathematical database records concern the 4-by-4 rook graph and a crown graph, which do not imply the odd-order result. Search cannot rule out historical results absent from available literature; obscure earlier optimum-code relocation work remains a residual priority risk.

## Value — PASS

The minimum sensor layouts form an important natural family with a previously known static optimizer orbit. The new all-order local exchange law proves uniform mobility with an explicit degree, distinguishing moves within a four-vertex-path sensor block from moves mediated by the unique two-vertex block. The first odd case yields a complete nontrivial 7200-state relocation metric, connectedness and sharp diameter nine; this determines exact optimal-layout mobility rather than merely recomputing a known code cardinality.

## Closest literature and limitations

[1] S. Gravier, J. Moncel, A. Semri, *Identifying codes of Cartesian product of two cliques of the same size*, EJC 15 (2008), N4, DOI and full text at https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1n4/pdf/ .

[2] F. Foucaud et al., *Identifying codes in line graphs*, JGT 73 (2013), 425–448, https://arxiv.org/abs/1107.0207 .

[3] W. Goddard, K. Wash, *ID codes in Cartesian products of cliques*, JCMCC 85 (2013), 97–106, https://combinatorialpress.com/article/jcmcc/Volume%20085/vol-085-paper%206.pdf .

The general-order connectedness/diameter is not claimed; the complete metric is established only at order five. Earlier literature not indexed or available could contain equivalent exchange results.

Self-review: passed. Independent audit: not yet performed.
