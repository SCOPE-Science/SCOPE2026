# Kirillov index of the three-step graph Lie algebras of complete bipartite graphs

## Finding
Let \(k\) be any field and let \(a,b\geq2\). For the three-step Lie algebra \(\mathfrak n_{K_{a,b}}\) associated by Gallo and Videla to the complete bipartite graph \(K_{a,b}\), put
\[
 w(a,b)=b\binom a2+a\binom b2.
\]
The Kirillov index, defined by
\[
 \operatorname{ind}_k(L)=\min_{\varphi\in L^*}\dim_k\{u\in L:\varphi([u,L])=0\},
\]
is exactly
\[
 \boxed{\operatorname{ind}_k(\mathfrak n_{K_{a,b}})=
 \begin{cases}
 w(a,b)+2,&(a,b)=(2,2),\\
 w(a,b)+ab-a-b,&\text{otherwise}.
 \end{cases}}
\]
Equivalently the largest possible rank of a Kirillov form is \(6\) at \(K_{2,2}\), and \(2(a+b)\) for all other complete bipartite graphs with both parts of size at least two. All assertions hold in characteristic two and over finite fields without extension of scalars. Since the center is the length-two-path space of dimension \(w(a,b)\), the theorem also determines the exact index excess over the center.

## Assumptions and scope
Write the graph's parts as \(X=\{x_1,\ldots,x_a\}\) and \(Y=\{y_1,\ldots,y_b\}\). The Lie algebra is the vector-space direct sum \(L=V\oplus E\oplus W\), where \(V\) is spanned by the vertices, \(E\) by edges \(e_{ij}=[x_i,y_j]\), and \(W\) by distinct unoriented length-two paths. It has
\[
 \dim V=a+b,\qquad\dim E=ab,\qquad \dim W=w(a,b).
\]
The edge space \(E\) and path space \(W\) span an abelian ideal, and \(W\) is central. All brackets not prescribed by the graph construction, skew-symmetry and bilinearity vanish. For each \(1\le i<h\le a\), \(1\le j\le b\), denote by \(s_{j;ih}\in W\) the basis vector associated with \(x_i-y_j-x_h\); for each \(1\le j<\ell\le b\), \(1\le i\le a\), denote by \(t_{i;j\ell}\in W\) that associated with \(y_j-x_i-y_\ell\). With the edge orientation above, the nonzero vertex-edge brackets are
\[
 [x_i,e_{hj}]=[x_h,e_{ij}]=s_{j;ih},\qquad
 [y_j,e_{i\ell}]=[y_\ell,e_{ij}]=t_{i;j\ell}.
\]
This formulation uses alternating brackets also in characteristic two. The theorem is restricted to \(a,b\ge2\); stars with a part of size one are not asserted to obey its formula.

## Proof
Fix a functional \(\varphi\in L^*\). Relative to the ordered decomposition \(V\oplus E\oplus W\), its alternating Kirillov matrix is
\[
 K_\varphi=\begin{pmatrix}C&D&0\\-D^{\mathsf T}&0&0\\0&0&0\end{pmatrix},\qquad
 C=\begin{pmatrix}0&F\\-F^{\mathsf T}&0\end{pmatrix},
\]
where \(F_{ij}=\varphi(e_{ij})\), and \(D\) is the \((a+b)\)-by-\(ab\) vertex-edge block. Every path basis vector can be assigned an independent value by \(\varphi\), so the entries of \(D\) are exactly
\[
 D_{x_i,e_{hj}}=D_{x_h,e_{ij}}=\varphi(s_{j;ih}),\qquad
 D_{y_j,e_{i\ell}}=D_{y_\ell,e_{ij}}=\varphi(t_{i;j\ell});
\]
all remaining entries vanish. Since \(E\oplus W\) is abelian and \(\dim V=a+b\), the rank of every Kirillov form is at most \(2(a+b)\).

First consider \(K_{2,3}\). Give the three paths \(x_1-y_3-x_2\), \(y_2-x_1-y_3\), \(y_1-x_2-y_2\) value one and all other path basis vectors value zero. In the row order \((x_1,x_2,y_1,y_2,y_3)\) and column order \((e_{11},e_{12},e_{13},e_{21},e_{22},e_{23})\), the resulting mixed block is
\[
 D=\begin{pmatrix}
 0&0&0&0&0&1\\
 0&0&1&0&0&0\\
 0&0&0&0&1&0\\
 0&0&1&1&0&0\\
 0&1&0&0&0&0
 \end{pmatrix}.
\]
Deleting its first column leaves a square matrix of determinant \(1\). Thus \(D\) has full row rank over every field.

We extend the witness one graph vertex at a time. Suppose the current graph has at least two vertices on each side, its mixed block has an \((a+b)\)-by-\((a+b)\) minor of determinant \(\pm1\), and at least one edge column was not used in that minor. Add a vertex to one part, retain all prior path evaluations, and give value one to exactly one new two-path whose endpoints are the new vertex and the old endpoint of an unused edge column, with the same middle vertex as that old edge. Give all other new path vectors value zero. The newly added row then has a single nonzero entry, equal to one, in that previously unused edge column; the reciprocal entry lies in a *new*, unselected edge column. Therefore adjoining the old unused edge column to the selected columns produces a new square minor with the same determinant up to sign. There are at least two new edges but only one extra selected column, so an unused edge column remains. Induction proves that \(D\) has full row rank for every \(a\ge2,b\ge3\); exchanging the parts also covers \(a\ge3,b=2\).

If \(D\) has full row rank \(r=a+b\), the noncentral block \(\begin{psmallmatrix}C&D\\-D^{\mathsf T}&0\end{psmallmatrix}\) has rank exactly \(2r\). Indeed, its image has rank at most \(2r\), while the invertible \(r\)-by-\(r\) minor of \(D\) gives a nonsingular alternating \(2r\)-by-\(2r\) principal submatrix. Hence
\[
 \operatorname{ind}_k L=(a+b+ab+w(a,b))-2(a+b)=w(a,b)+ab-a-b.
\]

It remains to treat \(K_{2,2}\). With four freely chosen path evaluations \(s_1,s_2,t_1,t_2\), its mixed block is
\[
 D=\begin{pmatrix}
 0&0&s_1&s_2\\ s_1&s_2&0&0\\
 0&t_1&0&t_2\\ t_1&0&t_2&0
 \end{pmatrix}.
\]
Direct determinant expansion gives \(\det D=0\) as a polynomial over the integers. The corresponding \(8\)-by-\(8\) noncentral alternating Kirillov block consequently has determinant \((\det D)^2=0\); since alternating matrices have even rank over any field, its rank is at most six. Setting \(s_1=t_1=1\), \(s_2=t_2=0\) makes \(D\) have rank three, which forces the Kirillov block to have rank at least six. Thus its maximum rank is exactly six, and \(\dim L=12\) gives index \(6=w(2,2)+2\). This completes the proof.

## Verification
The standalone file `checker.py` constructs all Kirillov matrices independently from graph brackets using exact modular arithmetic. It checks explicit full-rank functionals and integer-unimodular mixed-block minors for 36 part-size/prime-field cases, with part sizes up to five and characteristics \(2,3,5,7\). It also enumerates every functional on the noncentral bracket coefficients for \((a,b,q)=(2,2,2),(2,2,3),(2,3,2)\): respectively \(256\), \(6{,}561\) and \(32{,}768\) functionals. The maximal ranks found are \(6,6,10\), in agreement with the theorem. Run `python checker.py` from the folder containing the source. The recorded output is `checker_output.txt`. Exhaustive finite checks are *not* a proof over all fields; the determinant-one construction and the exceptional symbolic determinant identity supply that proof.

## Relationship to prior work
Gallo and Videla [1] introduce the three-step graph Lie algebra and compute dimensions, lower-central-series terms and centers, including the complete-bipartite ingredients used here. Their full construction does not give the Kirillov index for the present family. Burde and Dekimpe [2] determine indices for several nilpotent families, including the *two-step* graph Lie algebra associated to a graph; this is a different Lie algebra, since its edge space is central. Their general index-rank methods and abelian-ideal bound motivate the calculation, but do not provide the claimed full-rank mixed-block certificate or exceptional square case. Existing work on stars and subdivided stars likewise concerns different graphs. The contribution is the complete two-parameter, arbitrary-field index formula for the Gallo–Videla three-step construction, with the singular four-cycle boundary.

## Limitations
This result does not classify all graph Lie algebras or the entire distribution of Kirillov ranks. It excludes graph stars and disconnected graphs. It proves the index but not a full description of generic coadjoint stabilizers. Although the relevant papers and research records were compared by claim implication, historical priority remains subject to an unindexed equivalent computation. Independent mathematical review has not been performed.

## References
1. Andrea L. Gallo and Denis E. Videla, *Nilpotent Lie algebras of nilpotence class at most three via graphs*, arXiv:2610.33963v1, October 25, 2026, especially Sections 2–4. https://arxiv.org/html/2610.33963v1
2. Dietrich Burde and Karel Dekimpe, *The index of nilpotent Lie algebras*, arXiv:2505.08331, first public May 13, 2025, especially Sections 2, 4 and 5. https://arxiv.org/abs/2505.08331
