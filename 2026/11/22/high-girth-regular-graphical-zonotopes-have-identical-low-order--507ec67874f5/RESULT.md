# High-girth regular graphical zonotopes have identical low-order spherical width moments despite unequal volumes

## Finding
For every pair of connected, simple, unweighted, \(d\)-regular graphs \(G\) and \(H\) on the same \(n\ge3\) vertices, with \(d\ge2\), define the canonical centered Euclidean graphical zonotope
\[
Z_G=\sum_{\{u,v\}\in E(G)}[-(e_u-e_v)/2,(e_u-e_v)/2]\subset\mathbf1^\perp\subset\mathbb R^n.
\]
Let \(U\) be Haar-uniform on the unit sphere of \(\mathbf1^\perp\), and let \(W_G(U)\) be the full length of the orthogonal projection of \(Z_G\) on the line spanned by \(U\). If \(g(G)\), \(g(H)\) are the respective girths, then for **every integer** \(1\le k<\min\{g(G),g(H)\}\),
\[
\boxed{\mathbb E[W_G(U)^k]=\mathbb E[W_H(U)^k].}
\tag{1}
\]
Consequently the two width distributions have identical centered moments and cumulants through this order. This is an exact finite-dimensional identity, not an asymptotic approximation.

The 20-vertex cubic dodecahedral graph \(D\), of girth \(5\), and the 20-vertex cubic Desargues graph \(S\), of girth \(6\), give a concrete four-moment collision: their first **four** spherical width moments coincide exactly, whereas their Euclidean zonotope volumes differ:
\[
\boxed{\operatorname{Vol}_{19}(Z_D)=5\,184\,000\sqrt{20},\qquad
\operatorname{Vol}_{19}(Z_S)=6\,144\,000\sqrt{20}.}
\tag{2}
\]
The volume ratio is exactly \(32/27\). Therefore even the full first-four-moment Euclidean projection-width profile does not determine Euclidean volume among graphical zonotopes of equal dimension, degree and edge count.

## Assumptions and scope
A graph is finite, connected, undirected, simple, unweighted and \(d\)-regular. Girth is the length of the shortest simple cycle. A connected graph of degree at least two has finite girth. All coordinate vectors are the standard orthonormal basis, and the Euclidean metric is the ambient metric restricted to the intrinsic zero-sum hyperplane. The full directional width has no extraneous factor of two; explicitly, \(W_G(u)=\sum_{\{v,w\}\in E(G)}|u_v-u_w|\).

The theorem compares graphs with equal \(n\) and \(d\); it does not claim identical widths pointwise in directions, equal volumes, equal full distributions, or moment equality at or beyond the shorter girth. The restriction on \(k\) is strict.

## Proof
**1. Width as a Gaussian edge functional.** A segment \([-v/2,v/2]\) has full directional width \(|\langle u,v\rangle|\). Minkowski addition makes widths additive, establishing the expression in the preceding section. Take independent standard normal coordinates \(X_1,\ldots,X_n\) and define
\[
T_G(X)=\sum_{\{v,w\}\in E(G)}|X_v-X_w|.
\]
The orthogonal projection \(X_\perp=X-\bar X\mathbf1\) admits the polar representation \(X_\perp=RU\), where \(R\sim\chi_{n-1}\) and \(U\) is Haar-uniform and independent of \(R\). Differences are translation invariant, hence \(T_G(X)=RW_G(U)\). All moments exist and
\[
\mathbb ET_G^k=r_{n,k}\,\mathbb EW_G^k,
\qquad r_{n,k}=2^{k/2}\frac{\Gamma((n-1+k)/2)}{\Gamma((n-1)/2)}>0.
\tag{3}
\]
The normalization factor depends only on \(n,k\).

**2. A universal small-forest embedding lemma.** Let \(F\) be any finite simple forest with at most \(k\) edges and no isolated vertices. For an \(n\)-vertex \(d\)-regular graph \(G\) with \(g(G)>k\), the number \(\operatorname{inj}(F,G)\) of injective adjacency-preserving vertex maps \(F\to G\) depends only on \(F,n,d\), not on \(G\).

To prove this assertion, induct on \(|V(F)|\), simultaneously for all such forests. For an arbitrary forest with \(c\) connected components and \(e\le k\) edges, the number of **all**, possibly non-injective graph homomorphisms into \(G\) is exactly
\[
\operatorname{hom}(F,G)=n^c d^e.
\tag{4}
\]
Indeed, root each component, choose its root image in \(n\) ways and choose the image of every newly exposed child among the \(d\) neighbors of its parent. These choices are independent; vertex-image coincidences are allowed in a homomorphism.

Partition all homomorphisms according to the equivalence relation of coincident vertex images. For a partition \(\pi\) of \(V(F)\), form the quotient multigraph and disregard multiple copies of the same edge. If the quotient has a loop, no homomorphism with that kernel is possible. If the loopless quotient contains a cycle, the injective map of quotient vertices into \(G\) would exhibit a cycle of length at most \(e\le k\), contradicting the girth. Every remaining quotient is a forest. For the discrete partition its contribution is exactly \(\operatorname{inj}(F,G)\); for every other partition its loopless forest quotient has strictly fewer vertices, so by the induction hypothesis its injective-homomorphism count is determined by \(F,\pi,n,d\). Subtracting all those known contributions from (4) completes the induction. One-vertex isolated quotient components, if present, have injective counts included by starting the induction with edgeless forests; alternatively no such component arises for an edge-generated forest without loops. Thus the lemma holds for disjoint as well as connected forest patterns. In particular, the number of edge subsets isomorphic to \(F\) is exactly \(\operatorname{inj}(F,G)/|\operatorname{Aut}(F)|\), and is universal.

**3. Every moment below girth is universal.** Expand the \(k\)-th power of the finite sum \(T_G\):
\[
\mathbb ET_G^k=\sum_{(e_1,\ldots,e_k)\in E(G)^k}
\mathbb E\prod_{i=1}^k |X_{a(e_i)}-X_{b(e_i)}|.
\tag{5}
\]
The set of **distinct** edges in any tuple has at most \(k\) members. When \(k<g(G)\), those edges form a forest. For a fixed forest support and fixed positive multiplicity assigned to each of its edges, the Gaussian expectation depends only on its abstract edge-labeled isomorphism class, since the vertex normals are independent and identically distributed. By Step 2, the number of embeddings of that forest support is determined by \(n,d\). Summing over all forest supports and all compositions of \(k\) into positive edge multiplicities proves that the right side of (5) depends only on \(n,d,k\). Formula (3) proves (1) for all asserted \(k\). Cumulants and centered moments are polynomials in raw moments of no larger order, giving the stated consequence.

**4. An exact four-moment collision with a volume gap.** The dodecahedral and Desargues graphs each have 20 vertices, 30 edges and degree three; their shortest cycles have lengths five and six, respectively. Therefore (1) gives equality at \(k=1,2,3,4\). An exact count of their distinct four-edge supports yields the same seven forest-pattern counts, with counts in order: \(10155,12720,420,2520,120,1230,240\). The attached checker lists each pattern explicitly and independently enumerates these supports.

For the intrinsic Euclidean volume, each independent choice of \(n-1\) graphical zonotope generators is a spanning tree. The \((n-1)\)-dimensional parallelotope generated by any spanning tree's root differences has Euclidean volume \(\sqrt n\): the determinant of its Gram matrix is \(n\), by the tree matrix theorem or the unimodularity of a reduced incidence matrix. The zonotope determinant-sum formula thus gives
\[
\operatorname{Vol}_{n-1}(Z_G)=\sqrt n\,\tau(G),
\tag{6}
\]
where \(\tau(G)\) is the number of spanning trees. Exact integer Bareiss determinants of reduced graph Laplacians give \(\tau(D)=5\,184\,000\) and \(\tau(S)=6\,144\,000\). This proves (2) and the contrast.

## Verification
Run `python3 verify.py` in an environment with Python 3 and NetworkX (the latter for the two standard named graph constructions and graph Laplacians). The program checks graph order, size, degree and girth with all-source shortest-cycle BFS, enumerates all edge-support forest shapes for one through four edges (using component degree profiles, which completely classify forests with at most four edges), and compares their exact integer multiplicities. It computes both spanning-tree numbers using a standalone integer Bareiss determinant, and ends with `HIGH_GIRTH_WIDTH_MOMENT_EXACT_PASS k=1..4`. These finite checks verify the exhibited witness; Steps 1–3 prove the unrestricted theorem independently of computation.

## Relationship to prior work
Padrol, Pilaud and Poullot [1] establish the graphical-zonotope construction and its deformation-cone theory. Their publicly accessible full article treats normal fans, facet inequalities and Minkowski decompositions rather than random-direction Euclidean width moments. Earlier exact first/second width calculations and the published third-moment motif formulas [2,3] are credited: those results entail the first three orders for regular graphs without triangles, but they do not establish arbitrary-order girth universality or the fourth-moment equality and volume counterexample. The published bounded-degree spherical-width CLT [4] concerns asymptotic convergence and does not imply exact equalities for these fixed 19-dimensional bodies. Borbényi, Csikvári and Luo [5] study forest-counts and spanning subgraphs of regular high-girth graphs; forest enumeration and matrix-tree methods are not claimed as new. The new statement combines their sort of local acyclicity mechanism with the complete finite-order spherical width-moment hierarchy and an explicit metric-volume separation.

## Limitations
No assertion is made that the two example width distributions agree beyond fourth order, nor that fourth order is the largest possible agreement. The four-edge histogram and the two spanning-tree determinants are exact finite calculations, not a proof of the general girth law; the general proof is the homomorphism/forest argument. Normalization is restricted to the canonical unweighted Euclidean embedding and intrinsic random directions. Historical priority remains provisional: an unindexed equivalent application of local graph-homomorphism counting to Gaussian absolute-edge variation could cover the statement. No independent mathematical audit has been performed.

## References
1. A. Padrol, V. Pilaud, G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first publicly submitted 2021-11-24, https://arxiv.org/abs/2111.12422 ; full open-access article https://doi.org/10.1007/s00454-023-00586-x.
2. *Third angular-width moments of regular graphical zonotopes recover graph triangles*, published research record (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-third-angular-width-moments-of-regular-graphical-zonotopes-recov--49a1005c0e97.
3. *Three-edge motifs determine the cubic projection-width moment of graphical zonotopes*, published research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-edge-motifs-determine-the-cubic-projection-width-moment-of--6bc059dff8f9.
4. *Gaussian universality for random widths of bounded-degree graphical zonotopes*, published research record (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-gaussian-universality-for-random-widths-of-bounded-degree-graphi--7b346228232c.
5. M. Borbényi, P. Csikvári, H. Luo, *On the Number of Forests and Connected Spanning Subgraphs*, Graphs and Combinatorics 37 (2021), 2655–2678, https://doi.org/10.1007/s00373-021-02382-x.
