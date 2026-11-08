# Integral automorphism modules of pendant-supported higher independence complexes

## Finding
Let \(G\) be a finite, connected, simple graph with at least three vertices, and let \(W\ne\varnothing\) be the set of its non-leaf vertices (degree at least two). Assume that **every** vertex in \(W\) has at least one adjacent leaf. Let \(L=V(G)\setminus W\), \(n=|W|\), \(m=|L|\), and \(A=\operatorname{Aut}(G)\). All actions below are the natural actions by graph automorphisms. Write
\[
V_L=\ker\bigl(\varepsilon:\mathbb Z[L]\longrightarrow\mathbb Z\bigr),\qquad\varepsilon(\ell)=1,
\]
and let \(\det\mathbb Z[W]=\bigwedge^{n}\mathbb Z[W]\) be the rank-one orientation/sign module of the permutation of non-leaves.

For each integer \(r\ge1\), define \(X_r=\operatorname{Ind}_r(G)\): its faces are the subsets \(F\subseteq V(G)\) for which every component of \(G[F]\) has at most \(r\) vertices. Then, canonically as integral \(\mathbb Z[A]\)-modules,
\[
\widetilde H_i(X_r;\mathbb Z)\cong
\begin{cases}
\displaystyle \det\mathbb Z[W]\otimes\bigwedge^{r-n}V_L,&n\le r\le n+m-1\text{ and } i=r-1,\\
0,&\text{in all other cases}.
\end{cases}
\]
In particular, the entire nontrivial homology is torsion-free, has rank \(\binom{m-1}{r-n}\), and is an explicit **integral representation of the full graph automorphism group**, not just an abstract free abelian group. The rank and non-equivariant sphere-wedge homotopy types were already determined in Deshpande–Singh, Theorem 3.10; they are not new claims here.

For any \(g\in A\), denote the cycle lengths of its leaf permutation by \(c_1,\ldots,c_s\). Its rational homology character in the nonzero range is
\[
\operatorname{tr}\bigl(g\mid\widetilde H_{r-1}(X_r;\mathbb Q)\bigr)
=\operatorname{sgn}(g|_W)[t^{r-n}]\frac{\prod_{j=1}^{s}(1-(-t)^{c_j})}{1+t}.
\]
The quotient is a polynomial with integral coefficients, since \(\mathbb Z[L]\) contains a trivial permutation summand over \(\mathbb Q\). Outside that range all reduced homology characters vanish.

## Assumptions and scope
All graphs are finite, connected, undirected, loopless, and simple. The nonempty non-leaf set \(W\) is invariant under \(A\); the leaves \(L\) are its invariant complement. The condition of at least one leaf attached to every non-leaf is essential to the contractible-deletion argument. The graph induced on \(W\) is automatically connected: an internal vertex of a path between distinct non-leaves cannot be a leaf. The theorem includes trees with arbitrarily many leaves on each non-leaf and graphs with cyclic cores, including fully whiskered cycles and cliques. Nothing assumes a chosen order or labeled leaf at each core vertex.

Use ordinary reduced **integral simplicial homology** with its natural signed chain action. For the boundary case \(r=n\), \(\bigwedge^0V_L=\mathbb Z\). For \(r<n\), or \(r\ge n+m\), the complex is contractible. The equality is of \(A\)-modules; it is not an assertion of equivariant homotopy equivalence.

## Proof
**Step 1: a canonical contractible subcomplex.** Define
\[
K_0=\{F\in X_r:W\not\subseteq F\},\qquad
K_w=\{F\in X_r:w\notin F\}\quad(w\in W).
\]
Then \(K_0=\bigcup_{w\in W}K_w\), an \(A\)-invariant subcomplex. For every nonempty subset \(S\subseteq W\), the intersection \(K_S=\bigcap_{w\in S}K_w=\operatorname{Ind}_r(G-S)\) is a cone: take any \(w\in S\) and one of its adjacent pendant leaves \(\ell\). Once \(w\) is deleted, \(\ell\) is isolated in \(G-S\). Consequently adjoining \(\ell\) to any simplex of \(K_S\) preserves its membership in \(K_S\), so \(K_S\) has apex \(\ell\). Every intersection is nonempty, and the nerve of the cover \(\{K_w\}_{w\in W}\) is the full simplex on \(W\). By the simplicial nerve lemma, \(K_0\) is contractible. This argument requires no equivariant contraction: it only uses an invariant subcomplex with vanishing reduced integral homology.

**Step 2: relative faces.** Suppose \(r\ge n\). Since \(G[W]\) is connected and each leaf is adjacent to \(W\), the induced graph on \(W\cup F\), for \(F\subseteq L\), is connected and has \(n+|F|\) vertices. Thus the faces in \(X_r\setminus K_0\) are *exactly*
\[
W\cup F\qquad (F\subseteq L,\ |F|\le k=r-n).
\]
Set \(Z_k=\{F\subseteq L:|F|\le k\}\), with the empty face included. The augmented relative chain groups, in degrees \(n+j-1\), are
\[
C_{n+j-1}(X_r,K_0;\mathbb Z)
\cong \det\mathbb Z[W]\otimes\bigwedge^j\mathbb Z[L]
\quad(0\le j\le k),
\]
and vanish in other degrees. To see this, orient a face by listing all non-leaves first and the leaves second. A graph automorphism preserves the two sets, giving the determinant sign on \(W\) and the usual exterior action on the leaves. Deleting a core vertex lands in \(K_0\) and hence is zero in relative chains; deleting a leaf gives, up to the uniform degree sign \((-1)^n\), contraction by the augmentation functional \(\varepsilon\). This proves the displayed chain isomorphism, not merely an equality of character dimensions.

**Step 3: exact integral kernel.** The augmented full-simplex complex on \(L\) has chain differential \(\iota_\varepsilon:\bigwedge^j\mathbb Z[L]\to\bigwedge^{j-1}\mathbb Z[L]\). Choose any leaf \(\ell_0\), so \(\mathbb Z[L]=\mathbb Z\ell_0\oplus V_L\) as abelian groups, and contraction \(\iota_\varepsilon\) gives an exact complex. Its top-degree kernel when truncated at \(j=k\) is precisely \(\bigwedge^k V_L\), an intrinsic \(A\)-invariant sublattice independent of \(\ell_0\). The same holds for \(k=0\), where the only relative group is \(\det\mathbb Z[W]\) in degree \(n-1\). Therefore the relative homology vanishes except at degree \(n+k-1=r-1\), where it is \(\det\mathbb Z[W]\otimes\bigwedge^kV_L\). Since \(K_0\) is nonempty and contractible, the long exact sequence of the pair \((X_r,K_0)\), including its reduced degree-zero segment, makes this isomorphism natural and \(A\)-equivariant.

If \(r<n\), no face of \(X_r\) contains all of \(W\), so \(X_r=K_0\) and is contractible. If \(r\ge n+m\), the full vertex set is allowed and \(X_r\) is a simplex.

**Step 4: character.** Over \(\mathbb Q\), the permutation module on leaves splits as the augmentation module plus a trivial line. Thus \(\det(I+t\,g\mid V_L)=\det(I+t\,g\mid\mathbb Q[L])/(1+t)\). A cycle of length \(c\) contributes \(1-(-t)^c\) to the numerator. Taking the \((r-n)\)-th coefficient and multiplying by the core-orientation sign proves the trace formula.

## Verification
The companion standard-library-only `verify.py` reconstructs every face directly from connected components of induced graphs. It computes reduced mod-two homology by explicit boundary ranks, signed Lefschetz traces for actual graph automorphisms, the proposed exterior-augmentation character using cycle polynomials, and the cone property for every nonempty set of deleted core vertices. Eleven distinct core/leaf profiles include stars, asymmetric and symmetric double-stars, paths, triangles, cycles, cliques, and a branched core. It reports **712 homology/character checks and 819 deletion-cone checks**, with `ALL_VERIFY_OK`. These finite checks are independent corroboration of the definitions and signs; the all-parameter integral theorem is proved by the relative-chain argument, not by enumeration. Run `python3 verify.py` in a directory containing this document and the verifier; compare with `verify_output.txt`.

## Relationship to prior work
Deshpande and Singh, *Higher independence complexes of graphs and their homotopy types* (arXiv:2001.05448), **Theorem 3.10**, already determines the same sphere count \(\binom{m-1}{r-n}\) and ordinary homotopy type for graphs satisfying the pendant-leaf condition. That previously published statement is fully acknowledged as covering the nonequivariant rank and sphere-wedge assertions. The present claim instead determines the **natural integral automorphism module** and every full-group character value, and is not implied by a non-equivariant wedge decomposition or by a Morse matching that singles out labeled leaves.

Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees* (arXiv:2605.25150v1, publicly posted 24 May 2026), establishes vertex decomposability for all trees, a different property; it neither gives the full signed homology action nor covers the non-tree cores included here. Abdelmalek et al., *Chordal graphs, higher independence and vertex decomposable complexes* (arXiv:2106.10863), study shellability and vertex decomposition rather than these integral representations. The distinction is between **homotopy rank**, known, and **canonical group action on integral homology**, the asserted refinement. Targeted literature and mathematical-record comparisons did not identify an existing statement of this full integral module, but unindexed equivalents remain possible.

## Limitations
The result requires a connected graph whose every non-leaf has an adjacent pendant leaf. It gives integral homology representations, not an equivariant wedge decomposition, fixed-point homotopy classification, or chain-level equivariant contraction. The nonequivariant sphere ranks and homotopy types are known and are not new. No claim of formal computer verification or independent certification is made. An equivalent unindexed representation computation could reduce originality; independent validation has not been performed.

## References
- R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1 (first public 2026-05-24), https://arxiv.org/html/2605.25150v1.
- P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (first public 2020-01-15), Theorems 3.8 and 3.10, https://arxiv.org/pdf/2001.05448.
- F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (first public 2021-06-21), https://arxiv.org/abs/2106.10863.
