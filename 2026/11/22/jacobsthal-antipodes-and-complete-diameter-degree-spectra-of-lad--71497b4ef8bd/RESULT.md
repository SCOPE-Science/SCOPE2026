# Jacobsthal antipodes and complete diameter-degree spectra of ladder perfect-matching polytopes

## Finding
For every integer \(n\ge2\), the canonical edge-incidence perfect-matching polytope \(P_n\) of the open two-row ladder \(L_n=P_n^{\mathrm{path}}\square K_2\) has squared Euclidean diameter exactly \(2n\). The unordered vertex pairs at this distance are exactly the pairs of edge-disjoint domino tilings, and their number is
\[
\boxed{E_n=\frac{2^{n-1}+(-1)^n}{3}.}
\]
They form the edges of a **diameter graph** on the \(F_{n+1}\) polytope vertices. For each integer \(1\le k\le\lfloor n/2\rfloor\), precisely \(\binom{n-k}{k}\) vertices contain \(k\) pairs of horizontal dominoes and have degree \(2^{k-1}\) in the diameter graph. The single all-vertical vertex has degree \(1\) for even \(n\) and degree \(0\) for odd \(n\). These statements characterize the entire diameter-degree multiset, including collisions of degrees for \(k=1\) and even \(n\).

As \(n\) grows, the proportion of unordered vertex pairs at maximum Euclidean distance has the sharp equivalent
\[
\frac{E_n}{\binom{F_{n+1}}2}\sim\frac{5}{3\varphi^2}\left(\frac2{\varphi^2}\right)^n,\qquad\varphi=\frac{1+\sqrt5}{2}.
\]
Consequently the proportion decays exponentially, although the squared diameter grows linearly and the number of diametral pairs grows exponentially. The diameter adjacency of any two tilings can also be decided by the two-state transition rule proved below.

## Assumptions and scope
Fix \(n\ge2\). The graph \(L_n\) has vertices \((i,a)\) for \(1\le i\le n\), \(a\in\{0,1\}\), with vertical rung edges \(\{(i,0),(i,1)\}\) and, for \(1\le i<n\), longitudinal edges \(\{(i,a),(i+1,a)\}\). Its \(3n-2\) graph edges index orthonormal coordinate axes. A perfect matching contains \(n\) pairwise vertex-disjoint edges covering all \(2n\) graph vertices. Define
\[
P_n=\operatorname{conv}\{\mathbf1_M\in\{0,1\}^{3n-2}:M\text{ is a perfect matching of }L_n\}.
\]
The metric is the ordinary Euclidean norm in the indicated canonical coordinates, **not** shortest-path distance in the polytope's one-skeleton and **not** square-flip distance between domino tilings. A horizontal pair \(H\) consists of the two longitudinal edges joining adjacent columns, so it occupies two columns; a vertical tile \(V\) is one rung and occupies one column. Denote the standard Fibonacci numbers by \(F_0=0,F_1=1\).

## Proof
**1. Vertex encoding and Euclidean metric.** In any perfect matching, a column that is not covered by its vertical rung must join its two vertices to the same adjacent column. Starting at the left boundary and proceeding rightward, every matching therefore determines a unique word in the tiles \(V\) (one column) and \(H\) (two columns). Conversely every such tiling word yields a perfect matching. If a word contains \(k\) horizontal pairs, it has \(n-2k\) vertical tiles, hence \(n-k\) total tiles; the number with this \(k\) is \(\binom{n-k}{k}\). Summing these numbers gives \(F_{n+1}\) matchings. Each distinct zero-one incidence vector is a genuine vertex: if it were a convex combination of other zero-one incidence vectors, then every coordinate equal to zero (respectively one) would force that same value in every component of the combination, forcing all components to be identical. Since each matching consists of \(n\) edges,
\[
\|\mathbf1_M-\mathbf1_N\|_2^2=|M\triangle N|=2(n-|M\cap N|)\le2n.
\]
In addition, a maximum Euclidean distance between any two points of the convex hull is attained on vertices. Indeed, the squared distance of a nontrivial convex combination to any fixed point is strictly less than the largest of the component distances, unless all component incidence vectors coincide; the same applies to the other endpoint. Thus the possible diameter and its entire attaining set can be investigated using the matching vertices.

**2. Transfer for an arbitrary first matching.** Hold one matching \(M\) fixed and count perfect matchings \(N\) with \(M\cap N=\varnothing\). Process the tile word of \(M\) from left to right. At each tile boundary a two-state variable records whether the first column of the next tile is already covered by a horizontal pair of \(N\) crossing the boundary. State \(0\) means it is not yet covered and state \(1\) means it is already covered. When the tile of \(M\) is \(V\), the vertical rung is forbidden to \(N\). Therefore \(N\) must start a horizontal pair when entering in state \(0\), or must finish its incoming pair when entering in state \(1\). The transfer is
\[
T_V=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
When the tile of \(M\) is \(H\), its two longitudinal edges are forbidden. In state \(0\), the first column must be covered by a vertical rung of \(N\), while in state \(1\) the incoming horizontal pair finishes there. In either case the second column may be covered vertically (outgoing state \(0\)) or by a horizontal pair starting there (outgoing state \(1\)); all these choices use no forbidden edge. Thus
\[
T_H=\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]
This scan is exhaustive and uniquely reconstructs \(N\). The state is \(0\) both at the left and right boundaries, so the exact number of edge-disjoint partners of the tile word \(t_1\cdots t_{n-k}\) is
\[
D(M)=\left(T_{t_1}\cdots T_{t_{n-k}}\right)_{00}.
\]
The elementary identities \(T_V^2=I\), \(T_VT_H=T_HT_V=T_H\), and \(T_H^2=2T_H\) show that, whenever \(k\ge1\), the whole product equals \(2^{k-1}T_H\), and \(D(M)=2^{k-1}\), independently of tile placement. For \(k=0\), the product is \(T_V^n\), so \(D(M)=1\) if \(n\) is even and \(0\) otherwise. Every \(n\ge2\) permits a tiling with at least one \(H\), and it has a disjoint partner. Thus the upper bound \(2n\) is attained, proving the diameter and every asserted vertex degree.

**3. Exact total count.** The ordered count of diametral pairs is the sum of the degrees:
\[
2E_n=\mathbf1_{\{2\mid n\}}+\sum_{k=1}^{\lfloor n/2\rfloor}\binom{n-k}{k}2^{k-1}.
\]
Let \(A_n=\sum_{k=0}^{\lfloor n/2\rfloor}\binom{n-k}{k}2^k\). By splitting on the first tile (with weight \(2\) for \(H\)), \(A_0=A_1=1\) and \(A_n=A_{n-1}+2A_{n-2}\). Solving this recurrence gives \(A_n=(2^{n+1}+(-1)^n)/3\). Substitution and \(\mathbf1_{\{2\mid n\}}=(1+(-1)^n)/2\) yield \(2E_n=(2^n+2(-1)^n)/3\), hence the stated Jacobsthal count. This computation counts each unordered pair twice because its two matchings are distinct.

**4. Rare antipodes.** The exact Fibonacci asymptotic \(F_{n+1}\sim\varphi^{n+1}/\sqrt5\) and \(E_n\sim2^{n-1}/3\) give the displayed sharp fraction. Since \(2/\varphi^2<1\), the fraction tends exponentially to zero.

## Verification
The accompanying dependency-free Python 3 program `verify.py` enumerates every domino tiling independently in tile coordinates, constructs its literal set of graph edges, checks distances for **every unordered pair** through \(2\le n\le12\), and verifies each vertex's diameter degree against the proven formula. It also evaluates every two-state transfer for every tiling through \(n=19\) and checks the closed pair count through that range. Run from the directory containing this document using `python3 verify.py`. All checks passed in the prepared package. These finite checks are corroboration only; the transfer identity and recurrence prove the infinite-family assertions.

## Relationship to prior work
Torres's work on the \(k\)-matching polytope of a bipartite graph supplies the ambient general polytope class and proves its normality and a linear inequality description; those results are credited, not new here. The standard domino-tiling Fibonacci enumeration is also classical. Eğecioğlu, Saygı and Saygı study shortest-path diametral pairs and paths in Fibonacci **graphs**. Although open ladder tilings admit a Fibonacci-string encoding, their graph shortest-path metric differs from the Euclidean distance between matching incidence vectors. A distinct published result on circular/Möbius ladders classifies square-flip paths, not chords of the open-ladder perfect-matching polytope. Another published result on **total** matchings in **complete** bipartite graphs computes its different two-parameter diameter and pair census; it does not imply these open-ladder exact degree classes. The present claim is the sharp Euclidean diameter, complete degree distribution of its diameter graph, and closed Jacobsthal pair count in the natural edge-incidence realization.

## Limitations
Only the open two-row ladder and its canonical unit-edge-coordinate metric are treated. The formula does not assert edge-adjacency in the polytope's one-skeleton, any multirow or cyclic-ladder extension, or a characterization of connected components in the resulting diameter graph. OEIS-style appearances of the same Jacobsthal integers do not establish uniqueness of an enumerative interpretation. An older equivalent enumeration of edge-disjoint domino tiling pairs could remain unindexed. The published-results comparison does not constitute independent scholarly priority certification or independent mathematical audit.

## References
1. Juan Camilo Torres, *Normality of \(k\)-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910 (first publicly posted 2023-06-20), https://arxiv.org/abs/2306.11910.
2. Ömer Eğecioğlu, Elif Saygı, Zülfükar Saygı, *Euler numbers and diametral paths in Fibonacci cubes, Lucas cubes and Alternate Lucas cubes*, arXiv:2210.13849 (first publicly posted 2022-10-25), https://arxiv.org/abs/2210.13849.
3. *Twist-parity duality for square-flip reconfiguration of ladder matchings*, published research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-twist-parity-duality-for-square-flip-reconfiguration-of-ladder-m--8e7090802d17.
4. *A sharp diametral-pair transition in rectangular total-matching polytopes*, published research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-sharp-diametral-pair-transition-in-rectangular-total-matching--1149e0841478.
