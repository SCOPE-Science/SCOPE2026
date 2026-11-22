# The sharp three-to-four permutation threshold for matching-deleted complete bipartite graphs

## Finding

Let \(R_\pi(G)\) be the least number of permutations of the vertex set whose concatenation is a \(1\)-\(11\) representation of a finite simple graph \(G\): two distinct vertices are adjacent exactly when their two-letter restriction has at most one adjacent-equal-letter factor.

**Structural theorem.** For every finite simple graph \(G\) on a nonempty vertex set, a concatenation of three permutations represents \(G\) if and only if its complement \(\overline G\) is the comparability graph of a partial order of dimension at most three. The phrase "three permutations" permits repetitions of an order when a poset has dimension less than three.

**Sharp family theorem.** Take integers \(a,b\ge1\) and \(0\le s\le\min(a,b)\), and delete \(s\) vertex-disjoint cross edges from the complete bipartite graph \(K_{a,b}\). Denote the result by \(G_{a,b,s}\). Then

\[
R_\pi(G_{a,b,s})=\begin{cases}1,&(a,b,s)=(1,1,0),\\3,&s\le2\text{ and }(a,b,s)\ne(1,1,0),\\4,&s\ge3.\end{cases}
\]

In particular, for every \(n\ge3\), the crown graph \(K_{n,n}\) with a perfect matching removed has \(R_\pi=4\), sharpening the existing universal four-permutation upper bound.

## Assumptions and scope

Graphs are finite, simple, undirected and nonempty. Permutations list each vertex exactly once. For a word made of concatenated permutation blocks, a defect in the restriction to vertices \(u,v\) is an adjacent pair \(uu\) or \(vv\) after all other letters are deleted. A graph edge is encoded by at most one defect and a graph nonedge by at least two. Poset dimension is the minimum number of linear extensions whose order intersection is the poset; a comparability graph joins exactly the comparable distinct elements.

For the bipartite family, let the shores be \(A=\{a_1,\ldots,a_a\}\) and \(B=\{b_1,\ldots,b_b\}\), with deleted edges \(a_ib_i\), \(1\le i\le s\). Changing the labels of a removed matching does not change the isomorphism class. Empty letter sequences in the explicit formulae below are allowed.

## Proof

**1. Three-block characterization.** In a concatenation \(\pi_1\pi_2\pi_3\), restrict to a pair \(u,v\). Within each permutation the two letters alternate; a repeated-letter defect occurs precisely at a block boundary where the relative order of \(u,v\) changes. Thus the pair is a nonedge if and only if its order switches at both boundaries: the two vertices occur in the same relative order in \(\pi_1\) and \(\pi_3\), and the opposite order in \(\pi_2\).

Consider the three linear orders \(L_0=\pi_2\), \(L_1=\operatorname{rev}(\pi_1)\), and \(L_2=\operatorname{rev}(\pi_3)\). A pair is a nonedge exactly when it is ordered identically in all three orders, in one direction or the other. Their intersection is a partial order of dimension at most three with comparability graph \(\overline G\). Conversely, given any partial order \(P\) with \(\dim(P)\le3\), choose three linear extensions \(L_0,L_1,L_2\) whose intersection is \(P\), repeating extensions if needed. Then \(\operatorname{rev}(L_1)L_0\operatorname{rev}(L_2)\) encodes precisely the complement of the comparability graph of \(P\), by the same two-boundary argument. This proves the equivalence.

**2. Sharp lower bound after three deleted matching edges.** The complement of \(G_{a,b,s}\) consists of two cliques (one on each shore) and exactly the \(s\) deleted cross edges. Suppose \(s\ge3\) and it admitted a transitive orientation. Choose any three matched vertices \(a_i,a_j,a_k\) in shore \(A\). The orientation of their clique is a linear order, so relabel these three indices such that \(a_i\to a_j\to a_k\). Vertex \(b_j\) is adjacent in the complement to \(a_j\) but not to \(a_i\) or \(a_k\). If the edge is oriented \(a_j\to b_j\), transitivity along \(a_i\to a_j\to b_j\) would require missing edge \(a_ib_j\). If it is oriented \(b_j\to a_j\), transitivity along \(b_j\to a_j\to a_k\) would require missing edge \(b_ja_k\). Both are impossible. The complement is therefore not a comparability graph. By step 1, a three-permutation representation is impossible.

**3. Three explicit permutations with at most two deletions.** We construct two total orders \(L_1,L_2\) whose common comparabilities are precisely all pairs within the shores and the deleted cross pairs. Then the three blocks \(\operatorname{rev}(L_1),L_1,\operatorname{rev}(L_2)\) represent the desired graph by step 1. Concatenation of letter sequences is indicated by juxtaposition, and a subscript \(\circ\) denotes the sequence remaining after the specified first matched vertices.

For \(s=0\), put \(A=(a_1\cdots a_a)\), \(B=(b_1\cdots b_b)\), and choose \(L_1=AB\), \(L_2=BA\). All cross orders reverse and all within-shore orders agree.

For \(s=1\), write \(A'=(a_2\cdots a_a)\), \(B'=(b_2\cdots b_b)\), and set
\[
L_1=a_1 A' B' b_1,\qquad L_2=B' a_1 b_1 A'.
\]
The only cross pair with agreeing order is \((a_1,b_1)\), and all within-shore pairs agree.

For \(s=2\), write \(A'=(a_3\cdots a_a)\), \(B'=(b_3\cdots b_b)\), and set
\[
L_1=a_1 A'b_2a_2B'b_1,\qquad L_2=b_2B'a_1b_1A'a_2.
\]
Checking separately the four cross categories involving the two special indices and the unspecial vertices shows that only \((a_1,b_1)\) and \((a_2,b_2)\) have the same relative order; all other cross orders reverse. Within each shore the orders agree. Thus this is a realizer of the requisite dimension-two partial order for every allowed part size.

**4. Four permutations always suffice.** Hefty, Horn and Muir, Theorem 3.4, provide the following four-block \(1\)-\(11\) representation of the complete matching-deletion crown with shores indexed from \(1\) to \(N\):
\[
\begin{aligned}
& (a_1\cdots a_N b_1\cdots b_N),\\
& (a_N\cdots a_1 b_N\cdots b_1),\\
& (b_1a_1b_2a_2\cdots b_Na_N),\\
& (a_1b_1a_2b_2\cdots a_Nb_N).
\end{aligned}
\]
Take \(N=a+b-s\), keep left-shore labels indexed \(1,\ldots,a\) and right-shore labels indexed \(1,\ldots,s,a+1,\ldots,N\), and remove every other letter from each block. Relabel the selected letters consecutively in each shore. Restricting the word to an induced subgraph preserves every two-letter defect count, hence gives a four-permutation representation of \(G_{a,b,s}\). In particular the four-permutation upper bound holds for all parameters, including small and disconnected graphs.

**5. Optimality of the remaining cases.** A concatenation of one or two permutations has at most one boundary and therefore at most one defect for any pair, so it encodes only a complete graph. Within this bipartite family with positive shore sizes, the only complete graph is \(G_{1,1,0}=K_2\). That graph has a one-permutation representation. Every other member requires at least three. Combine this with steps 2–4 to obtain all cases of the formula.

## Verification

The self-contained `verify.py` uses only the Python standard library. Running `python3 verify.py` reconstructs edges by directly counting changes in relative pair order across permutation blocks. It validates the induced-crown four-block construction for all \(1\le a,b\le9\) and all feasible \(s\), the three-block constructions for every feasible \(s\le2\) in that same window, and the three-order partial-order intersection identity for each normalized triple of permutations on \(2\) through \(6\) vertices. It prints `VERIFY_OK` after those checks. These are finite tests supporting the constructions and critical three-block lemma; the unrestricted mathematical proof is given above.

## Relationship to prior work

Hefty, Horn and Muir (published online 15 December 2025), Theorem 3.4, explicitly show the **upper bound** \(R_\pi(H_{n,n})\le4\), using the four permutations repeated above. Their paper does not assert the sharp lower bound or the full arbitrary-part-size matching-deletion threshold. The structural statement here additionally identifies exactly the three-permutation class using the complement of comparability graphs with poset dimension at most three. Their even–odd representation theorem concerns a different adjacency rule and does not imply this statement.

Futorny, Kitaev and Pyatkin (2024) provide general permutation \(1\)-\(11\) constructions for split graphs and graphs obtained by partitioning the vertices into a comparability graph and an independent set, but do not calculate the minimum permutation count for matching-deleted bicliques. Das and Hariharasubramanian (2026) study square/cube patterns and regular languages of representations rather than this optimization threshold.

## Limitations

The theorem concerns representations made entirely of full permutations of every vertex. It does not assert minimum **word length** among unrestricted \(1\)-\(11\) words or any analogous result for other defect thresholds. Search did not uncover a prior proof of the complete three-permutation characterization and the matching-deletion threshold; this cannot certify absolute historical novelty. No independent mathematical audit has been carried out.

## References

1. Z. Hefty, P. Horn, C. Muir, *\(k\)-\(11\)-representations of graphs, revisited*, *Proceedings of the Edinburgh Mathematical Society*, DOI: https://doi.org/10.1017/S0013091525101211 (first online 2025-12-15), especially Theorem 3.4.
2. M. Futorny, S. Kitaev, A. Pyatkin, *New Tools to Study \(1\)-\(11\)-Representation of Graphs*, *Graphs and Combinatorics* 40, Article 97 (2024), DOI: https://doi.org/10.1007/s00373-024-02825-1.
3. B. Das, R. Hariharasubramanian, *On Patterns and Languages in \(1\)-\(11\)-Representations of Graphs*, arXiv:2601.20490 (first posted 2026-01-28), https://arxiv.org/abs/2601.20490.
