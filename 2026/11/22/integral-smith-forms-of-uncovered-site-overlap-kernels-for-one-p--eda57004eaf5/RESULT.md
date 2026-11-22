# Integral Smith forms of uncovered-site overlap kernels for one-point partial-Steiner diagrams

## Finding
Let \(A=(V,\mathcal B)\) be any finite partial Steiner triple system, with \(|V|=n\ge1\). A partial triple system has unordered three-point blocks, with no unordered pair in two blocks. Its *leave* \(H\) is the graph of old pairs absent from all blocks. Let \(\mathcal M(H)\) denote the matchings of \(H\), including the empty matching, and \(m=|\mathcal M(H)|\). An induced labelled one-point extension by a new point \(x\) is indexed by its matching \(M\), consisting of those pairs \(uv\) for which \(\{x,u,v\}\) is a new block. Let \(u_M\in\{0,1\}^V\) indicate the *uncovered old sites*: \(u_M(v)=1\) when no block containing \(x,v\) was specified. Define the integral overlap kernel
\[
K_A(M,N)=\sum_{v\in V}u_M(v)u_N(v),\qquad M,N\in\mathcal M(H).
\]
Thus \(K_A\) measures the number of old sites individually unused in **both** one-point extension diagrams, not the number of simultaneous two-point realizations.

**Connected-leave classification.** If \(H\) is connected, the nonzero invariant factors in the Smith normal form of \(K_A\) are exactly the following, with \(m-r\) additional zero factors:

* If \(H\) is nonbipartite and \(n\) is odd: \(r=n\), and the nonzero part is \(I_n\).
* If \(H\) is nonbipartite and \(n\) is even: \(r=n\), and the nonzero part is \(\operatorname{diag}(I_{n-2},2,2)\).
* If \(H\) is bipartite with parts of sizes \(p,q\) and \(p=q\): \(r=n-1\), and the nonzero part is \(\operatorname{diag}(I_{n-2},n)\).
* If \(H\) is bipartite with unequal part sizes, put \(s=|p-q|>0\) and \(g=\gcd(n,s)\). Then \(r=n\), and the nonzero part for \(n\ge2\) is \(\operatorname{diag}(I_{n-2},g,s^2/g)\). For \(n=1\) it is \(I_1\).

Unit factors displayed in these formulas are retained even when \(g=1\) or \(s^2/g=1\). The two nonunit factors in the unequal-part case satisfy \(g\mid s^2/g\), since \(g\mid s\). Thus these are valid Smith normal forms over the integers, not only rational ranks.

For **arbitrary**, possibly disconnected \(H\), let \(b\) be the number of bipartite connected components, including isolated vertices. Give each bipartite component any two-colouring and let \(s_j\) be its signed part-size difference. Then
\[
\operatorname{rank}_{\mathbb Q}K_A=n-b+\mathbf1_{\{\exists j:s_j\ne0\}}.
\]
Moreover an explicit integer Gram-lattice algorithm gives the complete Smith form for arbitrary \(H\): take an integer basis of
\[
L(H)=\mathbb Z\mathbf1+\sum_{uv\in E(H)}\mathbb Z(e_u+e_v)\subseteq\mathbb Z^V;
\]
its Euclidean Gram matrix is integrally congruent to the nonzero core of \(K_A\). Hence the kernel has the same positive rational rank as the lattice and no negative eigenvalues.

Two concrete partial-Steiner bases show different arithmetic mechanisms. Two disjoint named triples have leave \(K_{3,3}\), \(m=34\), and
\[
\operatorname{SNF}_{\mathbb Z}(K_A)=\operatorname{diag}(I_4,6,0_{29}).
\]
The Fano seven-point Steiner triple system together with an eighth isolated named point has star leave \(K_{1,7}\), \(m=8\), and
\[
\operatorname{SNF}_{\mathbb Z}(K_A)=\operatorname{diag}(I_6,2,18).
\]
In the second example the single-factor order-nine component appears within the factor \(18\), so the overlap kernel has odd-primary torsion even though each site indicator is binary.

## Assumptions and scope
All vertices and extension points are individually labelled. The base is any finite *relational* partial Steiner triple system; no claim is made that the class of all such systems with induced embeddings has a Fraïssé limit. One-point extensions are finite diagrams, not asserted to be complete first-order types of a homogeneous infinite structure. Their matching parametrisation follows directly from the condition that each pair appears in at most one triple. The kernel compares *individually free old sites* for separate diagrams; it does not assert that the two extensions can be jointly amalgamated. Two matching diagrams sharing an edge cannot be jointly realized on distinct new points, even if their uncovered-site overlap is positive.

The theorem uses the ordinary integral Smith normal form of the \(m\times m\) matrix \(K_A\); the zero factors number \(m-r\). For connected \(H\), the single-vertex case is included separately. Arbitrary disconnected leaves are covered by the rank formula and constructive lattice reduction, not an additional closed-form invariant-factor classification.

## Proof
**1. Type diagrams and the Gram factorization.** The set of blocks involving the new vertex \(x\) is \(\{\{x,u,v\}:uv\in M\}\). Such a pair \(uv\) must lie in the leave, or the pair \(uv\) would be repeated. Distinct new blocks cannot share any old vertex, or the pair \(xv\) would be repeated. Conversely, every matching in the leave specifies a valid induced one-point diagram. Thus the set of diagrams is exactly \(\mathcal M(H)\). Write \(e_v\) for the standard basis of \(\mathbb Z^V\). The indicator of uncovered sites is
\[
u_M=\mathbf1-\sum_{uv\in M}(e_u+e_v).
\]
Let \(F\) be the \(m\times n\) matrix whose rows are the \(u_M\). By definition \(K_A=FF^{\mathsf T}\). The empty matching contributes \(\mathbf1\), and the difference of its row and the row for a one-edge matching \(\{uv\}\) is \(e_u+e_v\). Every other matching row is the corresponding sum of these basic rows, so the row lattice of \(F\) is exactly \(L(H)\).

Choose a \(\mathbb Z\)-basis \(b_1,\ldots,b_r\) of this lattice. Integer elementary row operations transform \(F\) to a matrix with the \(b_i\) as its only nonzero rows. Consequently an integer-unimodular congruence sends \(K_A\) to \(G\oplus0_{m-r}\), where \(G=(b_i\cdot b_j)_{i,j}\). This proves that its Smith data are exactly those of the Euclidean Gram lattice \(L(H)\) and that its rank is \(r\). For full-rank lattices the Gram cokernel identifies with the discriminant group \(L(H)^*/L(H)\), where the dual uses the standard dot product.

**2. Edge-sum lattice.** Let \(Q(H)=\sum_{uv\in E(H)}\mathbb Z(e_u+e_v)\). For a connected graph, in the quotient \(\mathbb Z^V/Q(H)\), each edge identifies \(e_u\equiv-e_v\). If the graph is bipartite with sign vector \(\sigma\in\{\pm1\}^V\), all vertices have a consistent sign, so the quotient is infinite cyclic and
\[
Q(H)=\{z\in\mathbb Z^V:\sigma\cdot z=0\}.
\]
If the graph is nonbipartite, an odd cycle additionally forces twice the vertex generator to vanish. The parity-of-coordinate-sum map is the remaining nontrivial quotient, hence
\[
Q(H)=D_n:=\{z\in\mathbb Z^n:\sum_v z_v\equiv0\pmod2\}.
\]
These quotient arguments establish equality of integral lattices, not merely equality of real spans.

**3. Nonbipartite case.** Since \(L(H)=D_n+\mathbb Z\mathbf1\), it equals \(\mathbb Z^n\) for odd \(n\) and \(D_n\) for even \(n\). For even \(n\), the discriminant group of \(D_n\) has four elements generated by the classes of \(e_1\) and \(\tfrac12\mathbf1\), each of order two. Thus its Gram invariant factors are \(1\) repeated \(n-2\) times, followed by \(2,2\). For odd \(n\), the lattice is unimodular and its Gram invariant factors are all one.

**4. Balanced bipartite case.** If \(|P|=|Q|\), then \(\sigma\cdot\mathbf1=0\), so \(L(H)=Q(H)\). After independent coordinate sign changes this is the type-\(A_{n-1}\) root lattice \(\{z:\sum z_i=0\}\). The basis \(e_i-e_n\) for \(i<n\) has Gram matrix \(I_{n-1}+J_{n-1}\), whose Smith form is \(\operatorname{diag}(I_{n-2},n)\) (subtract the first row from the remaining rows and perform the analogous column operations, or compute its cyclic discriminant group). Hence \(r=n-1\).

**5. Unbalanced bipartite case.** Choose \(\sigma\) so that \(\sigma\cdot\mathbf1=s\) or \(-s\), where \(s>0\). Then
\[
L(H)=\{z\in\mathbb Z^n:\sigma\cdot z\equiv0\pmod s\},
\qquad L(H)^*=\mathbb Z^n+\mathbb Z\sigma/s.
\]
The first lattice has index \(s\) in \(\mathbb Z^n\), hence its Gram determinant is \(s^2\). The quotient \(\mathbb Z^n/L(H)\) is cyclic of order \(s\), generated by the class \(a\) of a signed coordinate vector \(\sigma_i e_i\). Adjoin the class \(b\) of \(\sigma/s\) in \(L(H)^*/L(H)\). The complete relations are
\[
sa=0,\qquad sb=na.
\]
Indeed the second relation follows from \(\sigma\cdot\sigma=n\), and the successive quotient description proves that these generate the full group of order \(s^2\). The presentation matrix \(\begin{pmatrix}s&-n\\0&s\end{pmatrix}\) has Smith factors \(g=\gcd(n,s)\) and \(s^2/g\). Since its remaining \(n-2\) Gram invariant factors are units, the formula follows. For \(n=1\), \(s=1\) and the sole factor is one.

**6. General disconnected rank.** On each nonbipartite component, edge-sums span the entire coordinate space over \(\mathbb Q\); on each bipartite component, they span the codimension-one signed-sum-zero hyperplane. Thus \(Q(H)\otimes\mathbb Q\) has codimension \(b\). Adding \(\mathbf1\) fills one of these missing dimensions exactly when some bipartite component has unequal colour-class sizes. This gives the displayed general rank formula.

## Verification
Run the included Python 3 standard-library checker with `python3 verify.py`. It computes exact integral generators, performs unimodular column elimination to obtain lattice bases, and uses exact Bareiss determinants and gcds of minors to calculate Smith factors. It checked all \(772\) labelled connected graphs on at most five vertices (the number includes distinct labelings), and all \(306\) labelled partial triple systems through six vertices. For bases on at most four vertices, it also reconstructs the complete overlap matrix independently from all matchings, verifies every entry, and compares its Smith form to that of the lattice Gram. It confirms the \(34\)-type \(K_{3,3}\) and eight-type \(K_{1,7}\) examples. These finite checks support but do not replace the unrestricted lattice proof.

## Relationship to prior work
Raines and Rodger (1997) study when partial Steiner triple systems have a one-factor or near-one-factor in the leave. Their four-page article was inspected in full; it does not define overlap kernels or derive their integral Smith invariants. The previously published finding *Real-rooted one-point extension spectra of partial Steiner triple systems* establishes exactly the matchings-in-the-leave bijection and one-point extension polynomial; this established bijection is credited and is not claimed as new. Its full proof and limitations were inspected, including its explicit warning that such finite diagrams must not be confused with complete one-types of the functional Steiner model completion. The contribution here is the new vacancy-overlap matrix and a uniform integral Gram-lattice classification by connected-leave parity and bipartition imbalance, together with a rank result for disconnected leaves.

Barbina and Zambella (2010) give general homogeneous/amalgamation-model background; their accessible arXiv HTML was inspected for its definitions and existence framework, but the present statement does not rely on an (in general unavailable) homogeneous relational partial-Steiner limit. The root lattices and their classical discriminants are standard. The proof supplies their needed integer descriptions and discriminant calculations rather than claiming those tools as new. Searches for prior monomer-support overlap Gram forms and equivalent signless-incidence-lattice statements did not locate an exact published classification of this kernel. Search incompleteness remains a historical-priority risk.

## Limitations
The kernel is an overlap of individually unused old sites in two **separate** finite one-point diagrams. It is neither a Boolean compatibility matrix nor the count of actual two-point completions: shared matching edges can obstruct amalgamation. The complete closed Smith formula assumes connected leave; the general disconnected case is treated by the stated rank formula and explicit integer-lattice reduction. It is not a theorem about a complete Steiner quasigroup, about the existence of a relational Fraïssé limit for all partial systems, or about eigenvalues other than rank and nonnegativity. Independent mathematical checking and exhaustive historical-priority verification have not been performed.

## References
1. M. E. Raines and C. A. Rodger, *Matchings in the Leave of Equitable Partial Steiner Triple Systems*, J. Combinatorial Mathematics and Combinatorial Computing **24** (1997), 115–118, publicly dated 1997-06-30. https://combinatorialpress.com/article/jcmcc/Volume%20024/vol-24-paper%207.pdf
2. L. D. Andersen, A. J. W. Hilton, E. Mendelsohn, *Embedding Partial Steiner Triple Systems*, Proceedings of the London Mathematical Society, s3-41 (1980), 557–576. https://doi.org/10.1112/plms/s3-41.3.557
3. Silvia Barbina and Domenico Zambella, *A viewpoint on amalgamation classes*, arXiv:1009.1789, initially public 2010-09-09. https://arxiv.org/abs/1009.1789
4. *Real-rooted one-point extension spectra of partial Steiner triple systems*, previously published finding (2026-10-04). https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-real-rooted-one-point-extension-spectra-of-partial-steiner-tripl--9599713a6632/RESULT.md
