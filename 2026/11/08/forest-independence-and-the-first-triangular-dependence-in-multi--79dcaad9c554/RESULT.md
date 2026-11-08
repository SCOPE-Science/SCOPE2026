# Forest independence and the first triangular dependence in multiple-successor logic

## Finding

Let \(n\ge2\) and \(k\ge3\). Independently sample \(k\) uniform linear orders on the labelled set \([n]\), and write \(S_i(x,y)\) when \(y\) is the immediate successor of \(x\) in order \(i\). Let \(G\) be any simple undirected graph on the \(k\) indices. For every edge \(\{i,j\}\) of \(G\), choose an arbitrary two-variable first-order sentence \(\varphi_{ij}\) whose only nonlogical relations are \(S_i,S_j\). Then the associated truth events are **mutually independent for every such choice** if and only if \(G\) is a forest.

The necessity is witnessed, for every nonforest \(G\), by the particular two-variable sentences
\[
\psi_{ij}:=\forall x\,\forall y\,(S_i(x,y)\leftrightarrow S_j(x,y)).
\]
Writing \(c(G)\) for the number of connected components (including isolated vertices), their joint truth probability is exactly
\[
\Pr\left(\bigwedge_{\{i,j\}\in E(G)}\psi_{ij}\right)
=(n!)^{-(k-c(G))},
\]
while the product of their individual probabilities is \((n!)^{-|E(G)|}\). Thus a cycle is an exact, observable obstruction.

The first natural quantitative dependence occurs on a triangle. For distinct indices \(i,j\), let \(X_{ij}\) be the number of **directed** pairs that are successors in both orders. Every two distinct variables \(X_{ij}\) are independent and have mean \(\mu_n=(n-1)/n\). For every three distinct indices,
\[
\boxed{
\mathbb E[(X_{12}-\mu_n)(X_{13}-\mu_n)(X_{23}-\mu_n)]
=\frac{n^4-2n^3+2n^2-4n+1}{n^3(n-1)^2}>0.
}
\]
The same expression is their mixed third cumulant; it equals \(1/n+O(n^{-3})\). More explicitly,
\[
\mathbb E[X_{12}X_{13}X_{23}]
=\frac{n^4-4n^3+8n^2-8n+1}{n^2(n-1)^2}.
\]
For any three distinct index edges that do not form a triangle, the corresponding overlap variables are mutually independent. Hence the triangles are exactly the triples of pairwise-overlap statistics with a nonzero mixed third cumulant.

## Assumptions and scope

A linear order is represented by a permutation \(\pi_i:\{1,\ldots,n\}\to[n]\) sending each position to its vertex. All \(\pi_i\) are independent and uniformly chosen from \(S_n\). The vocabulary contains exactly the indicated successor relations for each pair-local sentence: no vertex constants, colors, extra relation symbols, or externally fixed names are available to those sentences. Equality of vertices and the usual first-order connectives/quantifiers are allowed. Isomorphism invariance of a sentence is essential.

The statement about the universal independence property quantifies over **every** finite simple index graph \(G\) and **every** selection of first-order sentences restricted to the specified pair of successor symbols. The quantitative formula holds for all integers \(n\ge2\), without asymptotic restrictions. The counts \(X_{ij}\) are numeric statistics of relations; the theorem does not assert that arbitrary numeric counting of ordered pairs is itself expressible within plain two-variable first-order logic.

## Proof

### Relative-order coordinates and the forest criterion

Fix an arbitrary orientation of each index edge and write
\[
Q_{ij}=\pi_i^{-1}\circ\pi_j\in S_n.
\]
For every finite forest \(G\), fix one root index per connected component. The mapping from the vertex permutations \((\pi_i)_{i=1}^k\) to all root permutations together with the edge permutations \((Q_{ij})_{\{i,j\}\in E(G)}\) is bijective. Indeed, the unique path from the root to each other index reconstructs its permutation by multiplying the edge coordinates, inverting an edge coordinate when necessary. There are \(k\) independent uniform input permutations and exactly \(c(G)+|E(G)|=k\) output permutations. Every output tuple has exactly one preimage, so all output coordinates, in particular the edge coordinates, are independent and uniform.

An isomorphism of the two-successor reducts \((S_i,S_j)\) can relabel vertices by \(\pi_i^{-1}\), making the first order the standard order and the second order equal to \(Q_{ij}\). Consequently the truth of any sentence using only these two successor symbols is a function of \(Q_{ij}\). The edge-coordinate independence therefore proves the claimed mutual independence for **all** pair-local first-order sentences on a forest. The argument actually works for any isomorphism-invariant measurable pair statistic, not merely for first-order sentences.

For the converse, \(\psi_{ij}\) expresses equality of the two complete successor relations. A finite directed spanning successor path determines its order uniquely, so \(\psi_{ij}\) holds exactly when \(\pi_i=\pi_j\). Within each connected component of \(G\), requiring all these equalities makes every order coincide with a single freely chosen order. Exactly \((n!)^{c(G)}\) of the \((n!)^k\) input tuples satisfy the conjunction. Each individual equality has probability \(1/n!\); independence would give \((n!)^{-|E(G)|}\). For \(n\ge2\) these values agree precisely when \(|E(G)|=k-c(G)\), the forest criterion. This proves both directions.

### Exact triangular cumulant

Put \(\mathcal E=\{(u,v)\in[n]^2:u\ne v\}\), so \(|\mathcal E|=N=n(n-1)\). For directed edges \(e,f\), define \(M(e,f)\) as the probability that a uniform spanning successor path contains both. A single specified edge has probability \(p=1/n\). Two **distinct** specified edges are compatible precisely when they have different sources, different targets and are not mutual reverses; in that case contracting the two designated edges (whether disjoint or consecutive) shows
\[
M(e,f)=w=\frac{1}{n(n-1)}.
\]
For an incompatible pair, \(M(e,f)=0\); and \(M(e,e)=p\).

Expanding the three pair-overlap counts and using independence of the three entire orders gives the exact identity
\[
\mathbb E[X_{12}X_{13}X_{23}]
=\sum_{e,f,g\in\mathcal E}M(e,f)M(e,g)M(f,g).
\]
There are \(N\) choices when all three specified edges coincide. For each first edge there are exactly \(D=(n-1)(n-2)\) distinct compatible second edges. Hence the terms with exactly two equal edges contribute \(3NDpw^2\).

To count the ordered triples of pairwise compatible **distinct** edges, fix \(e=(u,v)\). The second edge \(f\) either attaches to one end of \(e\) (there are \(2(n-2)\) choices) or is disjoint from its endpoints (there are \((n-2)(n-3)\) choices). For attached \(f=(v,w)\), the source of \(g\) must avoid \(u,v\) and its target must avoid \(v,w\). Among the resulting \((n-2)^2\) ordered choices, exactly \(n-3\) have equal endpoints, leaving \(n^2-5n+7\). The other attachment orientation is symmetric. For disjoint \(f=(s,t)\), the two analogous source and target exclusions leave \((n-2)^2\) choices; subtract the \(n-4\) diagonal choices and the two forbidden reversed edges, leaving \(n^2-5n+6\). Therefore the number of ordered distinct pairwise-compatible edge triples is
\[
T=N\left(2(n-2)(n^2-5n+7)+(n-2)(n-3)(n^2-5n+6)\right)
=N(n-2)(n^3-6n^2+11n-4).
\]
These expressions also hold at \(n=2\), when the relevant classes are empty. Thus
\[
\mathbb E[X_{12}X_{13}X_{23}]=Np^3+3NDpw^2+Tw^3
=\frac{n^4-4n^3+8n^2-8n+1}{n^2(n-1)^2}.
\]
Each \(X_{ij}\) has mean \(N(1/n)^2=(n-1)/n\). By the forest result, the three pairwise products have expectations \(\mu_n^2\), so their centered mixed moment is \(\mathbb E[X_{12}X_{13}X_{23}]-\mu_n^3\), which simplifies to the displayed fraction.

The numerator of that fraction equals \(n^2(n-1)^2+(n-2)^2-3\), which is positive for every \(n\ge2\). Also
\[
\kappa_n=\frac1n+\frac{n^2-4n+1}{n^3(n-1)^2}
=\frac1n+O(n^{-3}).
\]
For three distinct index edges not forming a triangle, their three-edge index graph is a forest, hence their overlap statistics are mutually independent. This completes the third-order classification.

## Verification

Running \(\texttt{python3 checker.py}\) checks the stated formulas using exact integer and rational arithmetic. One route exhaustively enumerates **all** triples of permutations for \(n=2,3,4\), independently computes the three overlaps and their complete joint table, tests exact pairwise independence and reconstructs the mixed cumulant. Another enumerates all directed-edge triples through \(n=8\), testing the combinatorial compatible-triple count and rational formula. A third check enumerates the full relative-order coordinate distributions for small rooted trees and triangles, including a four-index forest. All checks emit \(\texttt{ALL_CHECKS_OK}\).

The infinite forest equivalence and all-parameter cumulant are established by the algebraic and combinatorial proofs above, not inferred from the finite checks.

## Relationship to prior work

Jeż, Michaliszyn and Witkowski (2026) study two-variable logic with an arbitrary finite number of independent successor relations, establish finite satisfiability decidability and explicitly discuss common adjacencies of different successors. Their inspected result is algorithmic; it does not state a probability law for independently uniformly chosen orders or a forest/cycle independence classification.

Diaconis, Evans and Graham (2013) determine the exact distribution of shared directed adjacencies between **two** random orders by identifying it with a truncated fixed-point count. This provides the classical one-edge-index-graph marginal law but cannot by itself determine three-way dependence between three pairs of orders.

Bender and Canfield (1999) prove Poisson limits for the number of edges common to several randomly embedded sparse graphs under broad degree assumptions. Their common-to-all statistic is not the three distinct pairwise-overlap statistics considered here, and their theorem does not provide the finite-size mixed third cumulant or the universal logical forest criterion.

A 2026 result on LKJ correlation matrices likewise exhibits pairwise-independent entries with a triangle-supported third cumulant, but its random correlation-matrix law is different from uniform successor paths [4]. The forest-coordinate bijection is a direct instance of the general elementary principle that differences of independent group-valued vertex labels along tree edges are themselves independent. This general mechanism is **not** claimed to be new. The specific logical all-pair-sentence criterion and the exact triangular cumulant for uniformly random successor paths are the objects of the present statement. No assertion of exhaustive historical priority is made.

## Limitations

The universal logical independence criterion assumes uniformly independent complete orders and pair-local isomorphism-invariant sentences. It can fail after restricting the sample space, introducing named vertices, or correlating the orders. The count cumulant quantifies only third-order dependence; it is not a full description of the joint law, nor a proof of a multivariate Poisson approximation. The asymptotic formula applies to fixed triples of distinct order indices and \(n\to\infty\). Independent mathematical review and comprehensive historical-priority verification have not been performed.

## References

[1] Artur Jeż, Jakub Michaliszyn, Piotr Witkowski, “Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors,” arXiv:2610.19943, first posted 14 October 2026, https://arxiv.org/abs/2610.19943.

[2] Persi Diaconis, Steven N. Evans, Ron Graham, “Unseparated pairs and fixed points in random permutations,” arXiv:1308.5459, 2013, https://arxiv.org/abs/1308.5459.

[3] Edward A. Bender, E. Rodney Canfield, “Intersections of Randomly Embedded Sparse Graphs are Poisson,” *The Electronic Journal of Combinatorics* 6 (1999), R36, DOI:10.37236/1468.

[4] Peter Reinhard Hansen, “Correlation Matrices in High Dimensions: The Elliptope as a Sample-Correlation Ensemble,” arXiv:2608.04162, 2026.
