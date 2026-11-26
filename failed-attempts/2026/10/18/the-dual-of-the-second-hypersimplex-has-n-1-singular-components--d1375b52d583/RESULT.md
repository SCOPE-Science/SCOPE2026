# The dual of the second hypersimplex has \(n+1\) singular components

## Finding
Let \(k\) be an algebraically closed field of characteristic zero and let \(n\ge5\). Put \(N=\binom n2\). Let \(X_n\subset\mathbb P^{N-1}\) be the projective toric variety parametrized on its dense torus by
\[
[x_1:\cdots:x_n]\longmapsto[x_ix_j]_{1\le i<j\le n}.
\]
Write \(A=(a_{ij})\) for the symmetric \(n\times n\) matrix with \(a_{ii}=0\), and identify the dual projective space with its \(N\) off-diagonal entries. Then its projective dual is the irreducible degree-\(n\) hypersurface
\[
X_n^\vee=\mathcal D_n=V(\det A)\subset\mathbb P^{N-1}.
\]
Its reduced singular locus has **exactly \(n+1\) irreducible components**:
\[
\operatorname{Sing}(\mathcal D_n)_{\mathrm{red}}
=R_{n-2}\ \cup\ \bigcup_{i=1}^n L_i,
\quad R_{n-2}=\{\operatorname{rank}A\le n-2\},
\quad L_i=\{a_{ij}=0\text{ for every }j\ne i\}.
\]
The component \(R_{n-2}\) is irreducible of codimension two **inside** \(\mathcal D_n\); each \(L_i\) is a linear space of codimension \(n-2\) inside \(\mathcal D_n\). At a general point of \(R_{n-2}\), the transverse completed local equation is \(uv-w^2=0\). At a general point of \(L_i\), it is a nondegenerate quadratic equation in \(n-1\) variables. Both generic transverse singularities have multiplicity two. In particular \(\mathcal D_n\) is normal, and its singular locus is non-equidimensional for every \(n\ge5\).

## Assumptions and scope
All varieties are over an algebraically closed field of characteristic zero. The claim concerns the projective dual of the degree-two **squarefree** monomial embedding, not the whole quadratic Veronese variety. Singular loci are reduced support; no primary decomposition of the Jacobian ideal or description of more degenerate intersections is asserted. Generic transverse local forms mean completions at general geometric points of the named irreducible components, after adjoining formally smooth parameters. The source with a verified public date predating 2016 is the toric-duality framework of Bourel--Dickenstein--Rittatore (2008).

## Proof
**1. Identification of the dual.** On the dense smooth torus of \(X_n\), a hyperplane with coefficients \(a_{ij}\) pulls back to the squarefree quadratic form
\[
f_A(x)=\sum_{i<j}a_{ij}x_ix_j=\tfrac12 x^TAx.
\]
Euler's identity and variation of all torus coordinates show that tangency is equivalent to \(Ax=0\), with every \(x_i\ne0\). Thus \(X_n^\vee\subset V(\det A)\). To show equality, let \(r=n-1\), and use the following irreducible Gram parametrization.

For any \(r\ge3\) define the isotropic quadratic cone \(Q_r=\{v\in k^r:v\cdot v=0\}\). It is irreducible (a nondegenerate quadratic form of rank at least three is not a product of linear forms). The map
\[
Q_r^n\longrightarrow\{A=A^T,\ \operatorname{diag}A=0,\ \operatorname{rank}A\le r\},
\qquad (v_1,\ldots,v_n)\longmapsto(v_i\cdot v_j)_{i,j}
\]
is surjective: every symmetric matrix over \(k\) of rank at most \(r\) admits a Gram factorization with \(r\) rows, and its diagonal-zero condition makes every column isotropic. Consequently the rank-bounded hollow symmetric locus is irreducible for \(r\ge3\). For \(r=n-1\), matrices of rank exactly \(n-1\) occur. Indeed nonzero isotropic vectors span \(k^r\), so a general \(r\times n\) matrix with isotropic columns has every \(r\)-column minor nonzero; its Gram matrix has rank \(r\), and its one-dimensional kernel has no zero coordinate. These matrices belong to the tangency locus. Since they are dense in the irreducible hypersurface \(V(\det A)\), its closure is exactly \(X_n^\vee\). Finally, at such rank-\(n-1\) matrices an off-diagonal derivative of the determinant is nonzero, so the determinant is reduced; irreducibility of its support makes \(\det A\) irreducible of degree \(n\).

**2. Complete singular support.** For \(i<j\), differentiation gives
\[
\frac{\partial\det A}{\partial a_{ij}}=2\operatorname{adj}(A)_{ij}.
\]
When \(\operatorname{rank}A\le n-2\), the adjugate vanishes. When \(\operatorname{rank}A=n-1\), symmetry implies \(\operatorname{adj}(A)=\lambda vv^T\) with \(\lambda\ne0\) and \(0\ne v\in\ker A\). All off-diagonal entries of the adjugate vanish precisely when \(v_iv_j=0\) for every \(i<j\), namely when \(v\) is supported on one coordinate. This is equivalent to the corresponding row and column of \(A\) being zero. Thus the displayed union is the entire reduced singular set, without relying on a finite enumeration.

**3. Irreducibility, dimensions, and actual components.** Set \(r=n-2\ge3\). The Gram argument above proves \(R_{n-2}\) irreducible. The open locus of spanning isotropic columns is an open subset of \(Q_r^n\) of dimension \(n(r-1)\). Its fibers under the Gram map are precisely the orthogonal-group orbits, of dimension \(r(r-1)/2\); hence the rank-\(r\) locus has dimension
\[
n(r-1)-\frac{r(r-1)}2=N-3
\]
in the affine space of dimension \(N\). Projectivizing gives \(\dim R_{n-2}=N-4\), while \(\dim\mathcal D_n=N-2\). Each \(L_i\) is projective of dimension \(N-n\), hence has codimension \(n-2\) in \(\mathcal D_n\). To see that \(L_i\) is not contained in \(R_{n-2}\), fill its complementary \((n-1)\times(n-1)\) block with ones off the diagonal and zeros on the diagonal: this block is invertible for \(n\ge5\), so the whole matrix has rank \(n-1\). The distinct \(L_i\) have independent defining row conditions; \(R_{n-2}\) is not contained in any \(L_i\) because its general Gram point has no zero row. The stated \(n+1\) sets are therefore the **irreducible components** of the singular locus.

**4. Generic transverse type on the determinantal component.** At a rank-\(n-2\) point choose an invertible principal \((n-2)\times(n-2)\) submatrix \(B\). By the Schur complement, locally
\[
\det A=\det B\,\det\begin{pmatrix}s_{11}&s_{12}\\s_{12}&s_{22}\end{pmatrix},
\]
where the three \(s\)-entries vanish along \(R_{n-2}\). Their differentials, restricted to the hollow-matrix ambient space, are the three coefficients of the restriction of a varying off-diagonal symmetric form to \(\ker A\). These coefficients are independent on a dense open set of \(R_{n-2}\): explicit integral rank-\(n-2\) witnesses for \(n=5,6\) have rank-three normal-restriction maps, as checked exactly in `verify.py`. Adjoining a nonsingular hollow \(2\times2\) block \(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) retains their two-dimensional kernel and their independent three normal variations, giving a witness for every higher \(n\). Independence is Zariski-open, and \(R_{n-2}\) is irreducible. Consequently the three Schur-complement entries are part of a regular local coordinate system at the general point; the completed transverse equation is \(s_{11}s_{22}-s_{12}^2=0\), a nondegenerate ordinary quadratic surface cone.

**5. Generic transverse type on each zero-row component.** Near a general point of \(L_i\), the complementary hollow block \(B\) is invertible. Writing \(v\in k^{n-1}\) for the entries in the deleted row and column, the exact block determinant identity reads
\[
\det\begin{pmatrix}0&v^T\\v&B\end{pmatrix}=-\det(B)\,v^TB^{-1}v.
\]
The quadratic form on the \(n-1\) independent normal coordinates \(v\) is nondegenerate; over \(k\) in characteristic zero it is formally equivalent to a sum of squares. This gives the asserted ordinary double point transverse to the smooth \(L_i\).

**6. Normality.** The irreducible hypersurface \(\mathcal D_n\) is Cohen--Macaulay, thus satisfies Serre's condition \(S_2\). Its reduced singular set has codimension at least two (the largest component is \(R_{n-2}\), of codimension two inside \(\mathcal D_n\)), so \(\mathcal D_n\) is regular in codimension one, satisfying \(R_1\). Serre's criterion implies normality.

## Verification
The standalone `verify.py` requires only the Python standard library. Its rational row reduction checks explicit rank-\(n-2\) hollow matrices and rank-three maps from ambient off-diagonal perturbations to quadratic forms on their two-dimensional kernels in dimensions \(5\le n\le12\). The family includes integral base witnesses in dimensions five and six and extends them by hyperbolic \(2\times2\) blocks. The script additionally checks a rank-four, five-variable hollow matrix with a full-support kernel, and rank-\(n-1\) matrices with a zero row for \(5\le n\le12\). It prints `VERIFY_OK` on success. These finite checks certify the stated base witnesses and block extension only; the all-dimensional theorem rests on the separate Gram, adjugate, and Schur-complement arguments.

## Relationship to prior work
Bourel, Dickenstein and Rittatore (2008, §2.3) give the general toric-duality framework and torus-tangency parametrization, but do not study the second hypersimplex's hollow determinant singular components. Devriendt, Friedman, Reinke and Sturmfels (2024, Theorem 3.5) identify the **different** rank-at-most-three hollow-symmetric locus with the squared Grassmannian and describe its determinantal equations. Their result identifies \(R_3\) in the special case \(n=5\) but does not imply the all-dimensional \(n+1\) component statement for the **rank-at-most-\(n-1\)** hollow determinant. An independently published analysis of the \(n=4\) hollow determinant quartic gives eleven singular surfaces, reflecting the reducibility of its rank-at-most-two locus; the present statement deliberately begins at \(n=5\), where the isotropic-cone irreducibility argument becomes available. The 2026 second-hypersimplex paper by Oldekop concerns Euler/maximum-likelihood stratifications and factors of the principal \(A\)-determinant; its abstract does not state the Jacobian components or transverse analytic singularities considered here, but the full text was not accessible during this literature comparison.

## Limitations
The theorem is set-theoretic on the singular locus; the Jacobian scheme may have nonreduced or embedded structure not addressed here. It does not classify singularities along intersections of the listed components or describe characteristic-two behavior. The origin of the rank constraints and the \(n=4\) contrast are well understood; the novelty claim is specifically the complete \(n\ge5\) reduced component decomposition, dimensional jump, and two generic transverse models. A remaining bibliographic risk is an unlocated general description of hollow determinantal discriminant singularities, and full-text overlap with Oldekop (2026) was not excluded.

## References
1. M. Bourel, A. Dickenstein, A. Rittatore, *Self-dual projective toric varieties*, arXiv:0805.3259v1 (first public 21 May 2008), §2.3; updated v3 (2011).
2. K. Devriendt, H. Friedman, B. Reinke, B. Sturmfels, *The Two Lives of the Grassmannian*, arXiv:2401.03684v1 (2024), Theorem 3.5 and Example 3.6.
3. A. Al Ahmadieh, C. Vinzant, *Characterizing Principal Minors of Symmetric Matrices via Determinantal Multiaffine Polynomials*, arXiv:2105.13444v1 (2021), Example 6.5.
4. *Eleven singular surfaces on the smallest squared Grassmannian*, public published-finding corpus record `2026/10/4/SCOPE-eleven-singular-surfaces-on-the-smallest-squared-grassmannian--6ce60a96126e`, `RESULT.md` (2026), covering the exceptional \(n=4\) quartic.
5. J. Oldekop, *Euler Stratifications of Second Hypersimplices via Delta-matroids*, arXiv:2606.16482v1 (2026), abstract available; full text not inspected.
