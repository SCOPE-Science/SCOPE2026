# Sharp three-restricted cuts and a triangle threshold in higher Kneser graphs

## Finding

For integers \(k\ge3\) and \(n\ge3k-1\), let \(G=\mathrm{KG}(n,k)\) be the graph whose vertices are the \(k\)-element subsets of \([n]\), with an edge exactly between disjoint subsets. Put \(N=\binom nk\) and \(d=\binom{n-k}{k}\). The three-restricted edge-connectivity, the minimum number of edges whose deletion disconnects \(G\) into components of order at least three, is

\[
\lambda_3(G)=\begin{cases}
3d-4,&n=3k-1,\\
3d-6,&n\ge3k.
\end{cases}
\]

Moreover **every** minimum three-restricted cut separates one connected three-vertex subgraph from its connected complement. When \(n=3k-1\), that subgraph is necessarily a path \(P_3\), and the exact number of minimum cuts is \(N\binom d2\). When \(n\ge3k\), it is necessarily a triangle \(K_3\), and the exact number is \(Nd\binom{n-2k}{k}/6\). Counts refer to distinct deleted edge sets, not isomorphism types.

## Assumptions and scope

All graphs are finite, undirected, simple. A three-restricted edge cut \(F\) is a set of edges such that \(G-F\) has at least two components and each component has at least three vertices. The set \(F\) need not initially be assumed inclusion-minimal. A graph is *super-three-restricted* if every minimum cut isolates an order-three connected component. The theorem covers all \(k\ge3\), \(n\ge3k-1\); it makes no claim about the interval \(2k+1\le n<3k-1\), the rank-two Kneser graphs, or cyclic edge cuts as a separate invariant.

## Proof

**1. Spectrum from incidence functions.** For each \(i\in\{0,\ldots,k\}\) and \(i\)-subset \(T\subseteq[n]\), define \(f_T(X)=\mathbf1_{T\subseteq X}\) on the vertices of \(G\). Let \(U_i\) be the span of functions \(f_T\) with \(|T|\le i\), and put \(U_{-1}=\{0\}\). For adjacency operator \(A\), the number of neighbors \(Y\) disjoint from \(X\) and containing \(T\) is \(\binom{n-k-i}{k-i}\) when \(X\cap T=\varnothing\), otherwise zero. Inclusion-exclusion gives the exact identity

\[
Af_T=\binom{n-k-i}{k-i}\sum_{J\subseteq T}(-1)^{|J|}f_J.
\]

Thus \(U_i\) is invariant, and the action on \(U_i/U_{i-1}\) is multiplication by \((-1)^i\binom{n-k-i}{k-i}\). Since \(A\) is symmetric, this scalar is its action on \(U_i\cap U_{i-1}^{\perp}\). The spaces exhaust all vertex functions because \(U_k\) contains every singleton vertex indicator. For \(n>2k\), the nonzero binomial magnitudes decrease with \(i\), so the largest adjacency eigenvalue on the orthogonal complement of constants is

\[
t=\binom{n-k-2}{k-2}.
\]

This derivation also verifies the spectral premise rather than assuming a numerical eigenvalue list.

**2. A uniform small-boundary gap.** For any vertex set \(S\) with \(s=|S|\le N/2\), the Laplacian Rayleigh bound applied to \(\mathbf1_S-(s/N)\mathbf1\) yields

\[
|\partial S|\ge(d-t)s(1-s/N). \tag{1}
\]

Because \(n\ge3k-1\),

\[
\frac td=\frac{k(k-1)}{(n-k)(n-k-1)}\le\frac{k}{2(2k-1)}\le\frac3{10};
\qquad N\ge56,\quad d\ge10.
\]

For \(5\le s\le N/2\), the function \(s(1-s/N)\) increases, so (1) implies

\[
|\partial S|\ge5(d-t)(1-5/N)\ge\frac72d\left(1-\frac5{56}\right)
=\frac{357}{112}d>3d.
\tag{2}
\]

For \(s=4\), at most six edges lie inside \(S\), hence \(|\partial S|=4d-2e(G[S])\ge4d-12>3d-4\), using \(d\ge10\). For \(s=3\), the exact identity \(|\partial S|=3d-2e(G[S])\) shows that the smallest possible boundary is \(3d-6\) if a triangle is present, and \(3d-4\) for a connected triple if the graph is triangle-free. A triangle in \(G\) is precisely three pairwise disjoint \(k\)-sets; it exists exactly when \(n\ge3k\). If \(n=3k-1\), connected triples are paths because the graph has degree \(d\ge10\) and no triangle.

**3. A three-vertex deletion never disconnects.** Suppose deleting a vertex set \(W\) of size at most three disconnects \(G\). Choose a component \(S\) of \(G-W\) of size \(s\le N/2\). All its boundary edges lead to \(W\), and so \(|\partial S|\le3s\). But (1) and the estimates in step 2 give

\[
|\partial S|\ge(d-t)s/2\ge\tfrac7{20}ds\ge\tfrac72s>3s,
\]

contradiction. In particular, removing the three vertices of any path or triangle in step 2 leaves a connected complement.

**4. Sharpness, rigidity and enumeration.** Deleting the boundary of one such path (for \(n=3k-1\)) or triangle (for \(n\ge3k\)) is therefore a valid three-restricted cut with the stated size. Conversely, let \(F\) be any three-restricted cut. Select a smallest component \(S\) of \(G-F\). Then \(3\le s\le N/2\) and \(F\) contains \(\partial S\). Inequalities (2) and the \(s=4\) bound rule out \(s\ge4\) for a minimum cut. Its order-three component must realize the largest possible number of internal edges: two at the triangle-free boundary and three thereafter. Equality of \(|F|\) with \(|\partial S|\) forces \(F=\partial S\), so no other edges are deleted, and step 3 ensures exactly two connected components. This proves super-three-restricted optimality.

At \(n=3k-1\), each path triple has a unique middle vertex and is specified by choosing two of that vertex's \(d\) neighbors; hence \(N\binom d2\) distinct cuts. At \(n\ge3k\), an ordered triple of pairwise disjoint \(k\)-sets can be chosen in \(Nd\binom{n-2k}{k}\) ways, and each triangle corresponds to six orderings; hence \(Nd\binom{n-2k}{k}/6\) cuts. Distinct small components give distinct cuts because the complement is connected and has more than three vertices. \(\square\)

## Verification

The standalone Python verifier `verify_kneser_lambda3.py` constructs the exact disjointness graph and exhaustively checks every three- and four-vertex subset for \((n,k)=(8,3)\) and \((9,3)\). It confirms respectively \((\lambda_3,\#\mathrm{cuts})=(26,2520)\) and \((54,280)\), and checks that an extremal triple has connected complement. It independently verifies the incidence-operator identity on \(\mathrm{KG}(8,3)\). Integer inequalities supporting the general estimates are checked over 264 further parameter pairs as corroboration; these finite tests do not prove the unrestricted statement, whose proof is above.

Run with Python 3 standard library: `python3 verify_kneser_lambda3.py`.

## Relationship to prior work

Balbuena and Marcote study \(p\)-restricted edge connectivity of Kneser graphs and determine the full \(p\)-range for \(\mathrm{KG}(n,2)\), not the higher-rank \(p=3\) formula and optimal-cut census here [2]. Yu, Xu, Wu and Zheng establish restricted and cyclic edge-connectivity for generalized Johnson graphs, including Kneser graphs [3]. Cyclic cuts require cyclic components and therefore do not cover the acyclic isolating paths at the sharp \(n=3k-1\) boundary. The relationship to their cyclic-edge conclusion in the triangle-containing range is a close priority comparison and not an assertion that that work has no relevant implications. Yang, Zhang, Qin and Guo give a sufficient criterion for super-three-restricted cuts in four-cycle-free vertex-transitive graphs [4]; the graphs treated here do contain four-cycles, so the stated criterion does not directly apply. Ballinas, Caine, Hopkins and Rivera Laboy study the related uniform-edge scramble and gonality of Kneser graphs, motivating renewed attention to restricted edge cuts [1]; their Section 5 addresses two-restricted cuts, rather than a three-restricted classification.

## Limitations

The theorem excludes \(2k+1\le n<3k-1\). It does not determine other restricted-connectivity levels, divisorial gonality, cyclic edge connectivity, or the full spectrum of near-minimum cut sizes. Standard incidence linear algebra and binomial inequalities suffice to establish the unrestricted claim; no probabilistic assumption or computer-assisted infinite argument is used. A published 2023 generalized-Johnson-graph paper was accessible only through its abstract and opening-page preview, so its full proof and possible implicit consequences for the triangle case remain a priority risk. Independent validation has not been performed.

## References

1. L. A. Ballinas, W. Caine, D. B. Hopkins and D. Rivera Laboy, *On the gonality of Kneser graphs*, arXiv:2609.00258, first posted 2026-08-31, https://arxiv.org/abs/2609.00258.
2. C. Balbuena and X. Marcote, *The p-restricted edge-connectivity of Kneser graphs*, Applied Mathematics and Computation 343 (2019), 258–267, doi:10.1016/j.amc.2018.09.072, public accepted proofs at https://upcommons.upc.edu/bitstream/handle/2117/184872/AMC-RestrictedEdgeKneser.pdf.
3. Z. Yu, L. Xu, X. Wu and C. Zheng, *On the Super (Edge)-Connectivity of Generalized Johnson Graphs*, International Journal of Foundations of Computer Science 35 (2024), 579–593, doi:10.1142/S012905412350017X.
4. W. Yang, Z. Zhang, C. Qin and X. Guo, *On super 2-restricted and 3-restricted edge-connected vertex transitive graphs*, Discrete Mathematics 311 (2011), 2683–2689, doi:10.1016/j.disc.2011.08.021.
