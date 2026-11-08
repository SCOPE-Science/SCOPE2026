# Exact edge count and symplectic fibers in Heisenberg comaximal graphs

## Finding
For every prime power \(q\) and integer \(m\ge 2\), let \(H_m(q)=V\oplus\mathbb F_qz\) be the \((2m+1)\)-dimensional Heisenberg Lie algebra, where \(V\) has a nondegenerate alternating form \(\omega\) and \([u+az,v+bz]=\omega(u,v)z\). The comaximal graph \(\Gamma_m(q)\) has as vertices the nonzero proper Lie subalgebras and joins two distinct vertices if they generate \(H_m(q)\).

Write \(n=2m\), let \({a\brack b}_q\) denote the Gaussian coefficient, and define
\[
 I_k={m\brack k}_q\prod_{i=0}^{k-1}(q^{m-i}+1),\qquad
 D_k=\sum_{j=n-k}^{n-1}{k\brack n-j}_q q^{(n-k)(n-j)}.
\]
Then \(I_k\) is the number of totally isotropic \(k\)-subspaces of \(V\), and \(D_k\) is the number of proper subspaces complementary in sum to a fixed \(k\)-subspace. The exact vertex and unordered-edge counts are
\[
 \boxed{\ |V(\Gamma_m(q))|=\sum_{k=0}^{n-1}{n\brack k}_q+\sum_{k=1}^{m}I_kq^k\ },
\]
\[
 \boxed{\ |E(\Gamma_m(q))|=
 \frac12\sum_{k=1}^{n-1}{n\brack k}_qD_k
 +\sum_{k=1}^{m}I_kq^kD_k
 +\frac12 I_m q^{\,m(m+1)/2+2m}\ }.
\]
Its unique isolated vertex is \(\mathbb F_qz\). Its nonisolated induced graph has diameter exactly \(2\), and
\[
 \boxed{\ \omega(\Gamma_m(q))=\chi(\Gamma_m(q))=\frac{q^{2m}-1}{q-1}\ }.
\]
The decisive additional term in the edge formula counts pairs of graph-type subalgebras over complementary Lagrangian subspaces; such pairs cannot occur over two lower-dimensional isotropic subspaces.

## Assumptions and scope
The field is an arbitrary finite field, including even characteristic. The alternating form is nondegenerate. The rank condition \(m\ge2\) excludes the previously classified three-dimensional Heisenberg case. An edge means Lie *generation*, not that the sum of two subalgebras is closed under brackets. The sums are ordinary finite integer sums, and each edge is counted once. For \(k=0\), the only subalgebra with zero image in \(V\) that is a graph vertex is the central line; there is no graph-type zero subalgebra vertex.

## Proof
**1. Classification of all vertices.** Let \(\pi:H_m(q)\to V\) be the quotient map. If \(z\in U\), then \(U=\pi^{-1}(W)=W\oplus\mathbb F_qz\) for a unique proper subspace \(W<V\). Every such \(W\), including \(W=0\), occurs. If \(z\notin U\), then \(\pi|_U\) is injective, and \(U\) is the graph of a unique linear functional \(f:W\to\mathbb F_q\) on \(W=\pi(U)\). Closure under brackets is equivalent to \(\omega|_{W\times W}=0\), i.e. to total isotropy. Here \(W\ne0\), since the zero graph is not a vertex. Conversely every such graph is a subalgebra, and each isotropic \(k\)-space has exactly \(q^k\) linear functionals. No proper subalgebra projects surjectively to \(V\): if it contained \(z\) it would be the whole algebra, whereas otherwise it would be an isotropic graph over the non-isotropic full space. Thus each proper \(W\) has a fiber of \(1+q^{\dim W}\) vertices if \(W\ne0\) is isotropic, and a fiber of one vertex otherwise. In particular the unique vertex over zero is \(\mathbb F_qz\).

**2. Exact adjacency.** For proper subalgebras \(U,U'\), we have
\[
 \langle U,U'\rangle=H_m(q)\ \Longleftrightarrow\ \pi(U)+\pi(U')=V.
\]
The forward implication is immediate. Conversely, let \(S=\langle U,U'\rangle\) project onto \(V\). If \(z\notin S\), then \(S\) is a graph over \(V\) and would be abelian, since its brackets lie in \(\mathbb F_qz\cap S=0\); this contradicts nondegeneracy of \(\omega\). Hence \(z\in S\), and \(S=H_m(q)\). Different vertices in the same fiber are therefore never adjacent, and all adjacency between distinct fibers follows the subspace-sum graph on proper subspaces of \(V\).

**3. Finite symplectic counts.** For \(0\le k\le m\), an ordered isotropic basis is built inductively: after choosing an isotropic \(i\)-space \(W_i\), the next vector may lie in \(W_i^\perp\setminus W_i\), yielding \(q^{2m-i}-q^i\) possibilities. Divide the product by the number \(\prod_{i=0}^{k-1}(q^k-q^i)\) of ordered bases in a fixed \(k\)-space. This gives
\[
 I_k=\frac{\prod_{i=0}^{k-1}(q^{2m-i}-q^i)}{\prod_{i=0}^{k-1}(q^k-q^i)}
 ={m\brack k}_q\prod_{i=0}^{k-1}(q^{m-i}+1).
\]
For a fixed \(k\)-space \(W<V\), a \(j\)-space \(W'\) satisfies \(W+W'=V\) exactly when \(t=\dim(W\cap W')=k+j-n\ge0\). There are \({k\brack t}_q\) possible intersections, and after fixing one there are \(q^{(n-k)(k-t)}=q^{(n-k)(n-j)}\) possible graphs over a fixed complement of \(W\). Summing over \(n-k\le j\le n-1\) gives \(D_k\), independent of the position of \(W\).

**4. Vertices and edges.** Let a *base vertex* over \(W\) mean \(W\oplus\mathbb F_qz\); there is one for each proper \(W\). There are also \(q^k\) extra graph-type vertices over each nonzero isotropic \(k\)-space. This proves the vertex formula.

Edges between base vertices contribute
\(E_0=\frac12\sum_{k=1}^{n-1}{n\brack k}_qD_k\).
Every extra vertex over an isotropic \(k\)-space has exactly \(D_k\) adjacent base vertices, so extra-to-base edges contribute
\(E_1=\sum_{k=1}^m I_kq^kD_k\).
Finally two isotropic spaces \(W,W'\) can sum to the full \(2m\)-space only if both have dimension \(m\) and meet trivially. Thus extra-to-extra edges occur exactly over *complementary Lagrangians*. The number of Lagrangians is \(I_m\). For each fixed Lagrangian \(W\), choose one complementary Lagrangian \(W_0\); every other complementary Lagrangian is the graph of a linear map \(T:W_0\to W\), and isotropy of that graph is equivalent to symmetry of the associated bilinear form. There are exactly \(q^{m(m+1)/2}\) such symmetric forms, in every characteristic. Each pair of complementary Lagrangians supports \(q^m\cdot q^m\) pairs of extra vertices. The unordered contribution is
\(E_2=\frac12I_mq^{m(m+1)/2+2m}\). Adding \(E_0+E_1+E_2\) proves the edge formula without double-counting.

**5. Clique number, coloring and diameter.** Write \(h={n\brack1}_q=(q^n-1)/(q-1)\). Every proper projection \(W\) lies in some hyperplane. For any clique, choose one containing hyperplane for each projection. Adjacent projections span \(V\), so these chosen hyperplanes must be distinct: the clique has at most \(h\) vertices. Conversely, the \(h\) distinct base vertices over hyperplanes are pairwise adjacent. This proves \(\omega=h\). Assign each graph vertex the color of any containing hyperplane of its projection; adjacent vertices cannot share a color. Thus \(\chi=h\).

The central vertex is isolated since its projection is zero; every vertex with nonzero projection is adjacent to some hyperplane, so no other vertex is isolated. For any two nonzero proper projections \(W_1,W_2\), the union of their annihilators in \(V^*\) is not all of \(V^*\) (two proper linear subspaces cannot cover a vector space). Choose a functional nonzero on each \(W_i\). Its kernel is a hyperplane whose base vertex is adjacent to both. Therefore the nonisolated graph has diameter at most \(2\). Since \(m\ge2\), it contains distinct nonadjacent vertices over a common nonzero isotropic line, so its diameter is exactly \(2\).

## Verification
The standalone program `check_comaximal.py` enumerates every vector subspace of the ambient Lie algebra by reduced row echelon generators, tests Lie closure directly from the alternating bracket, and tests generation for every unordered pair of resulting proper nonzero subalgebras. It independently groups the subalgebras by quotient-image fibers and checks the fiber formulas, then compares graph edges with the symbolic closed forms. The direct cases are \((m,q)=(1,2),(1,3),(2,2),(2,3)\); the first two provide previously known boundary cross-checks rather than new claims. In the first unclassified rank \(m=2\), \(q=2\), the program finds \(156\) vertices and \(3805\) edges (contributions \(925+1920+960\)) over \(\mathbb F_2\), and \(691\) vertices and \(100905\) edges (contributions \(11805+45360+43740\)) over \(\mathbb F_3\). It also executes \(20\) integer formula consistency cases through \(m=5\), over \(q=2,3,4,5\). See `verification_output.txt` for actual recorded output and `VERIFICATION.md` for limitations. An exhaustive finite check is not the proof for all ranks and fields.

## Relationship to prior work
Towers, Zuleta and Gutierrez introduced the comaximal graph and classified all three-dimensional Lie algebras in *The comaximal graph of a finite-dimensional Lie algebra* (first available May 10, 2026; arXiv:2605.09583). In particular they determine the \(m=1\) Heisenberg case, which is explicitly excluded from the present new claim. Their follow-up *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants* (arXiv:2608.16575) studies three-dimensional triangle counts, four-dimensional Lie algebras, and proves a general Frattini-quotient blow-up theorem (Theorem 6.1). The fact that the Heisenberg comaximal graph is a blow-up of a subspace-sum graph is therefore **prior coverage**, not asserted as new here. The new contribution is the **precise nonuniform isotropic-fiber enumeration and the resulting all-rank edge formula**, including the complementary-Lagrangian term, together with the explicit all-rank graph invariants. Existing finite Heisenberg subalgebra-*commutativity* formulas concern whether the vector-space sum of subalgebras is closed, not whether the subalgebras generate the whole Lie algebra. Searches identified no published all-rank edge formula, but absence from searches cannot establish historical priority.

## Limitations
This theorem does not enumerate triangles or graph spectra in arbitrary rank, does not classify every graph automorphism, and does not extend to Lie algebras with degenerate alternating forms or centers larger than one dimension. The field is finite and \(m\ge2\). The general Frattini blow-up principle and the \(m=1\) special case are prior work. The exact finite sum could have an implicit equivalent in subspace-sum-graph or symplectic-incidence literature despite the recorded checks. No independent mathematical audit has been performed.

## References
1. D. A. Towers, Y. Zuleta, I. Gutierrez, *The comaximal graph of a finite-dimensional Lie algebra*, arXiv:2605.09583, submitted May 10, 2026. https://arxiv.org/abs/2605.09583
2. D. A. Towers, Y. Zuleta, I. Gutierrez, *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants*, arXiv:2608.16575, submitted August 17, 2026. https://arxiv.org/abs/2608.16575
3. A. Das, work introducing the subspace sum graph, as cited and distinguished in Reference 1.
