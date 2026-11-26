# The 165 Hermitian cone curves span the Picard group of the characteristic-two Fermat cubic Fano surface

## Finding
Let \(k=\overline{\mathbb F}_2\), let \(X\subset\mathbb P^4_k\) be the Fermat cubic threefold \(\sum_{i=0}^4x_i^3=0\), and let \(S=F_1(X)\) be its smooth Fano surface of lines. For every \(P\in X(\mathbb F_4)\), let \(E_P\subset S\) parametrize the projective lines on \(X\) passing through \(P\). The following all hold.

1. The \(165\) curves \(E_P\) are pairwise distinct smooth plane cubics, hence genus-one curves.
2. Their geometric intersection matrix \(G=(E_P\cdot E_Q)\) is \(A-3I_{165}\), where \(A\) is the adjacency matrix of the point-collinearity graph of the finite Hermitian generalized quadrangle \(H(4,4)\). Its characteristic polynomial is
\[
\det(tI_{165}-G)=(t-33)t^{120}(t+12)^{44}.
\]
3. Consequently, their classes span \(\operatorname{NS}(S)\otimes_{\mathbb Z}\mathbb Q\) and \(\rho(S)=45\). The statement is **rational** spanning, not an assertion of integral index one or of a discriminant group.

The known geometric Picard rank \(45\), the known arithmetic rank \(25\) over \(\mathbb F_2\), and the known Fano zeta function are not newly asserted calculations. The contribution is the explicit rank-saturating geometric generator configuration and its complete intersection spectrum.

## Assumptions and scope
Everything takes place over the algebraic closure \(k\) of the field of two elements. A Hermitian point means a point defined over \(\mathbb F_4\) of \(X\). Two distinct Hermitian points are adjacent when their joining line is contained in \(X\). The Néron–Severi group is modulo algebraic equivalence; generation is only after tensoring with \(\mathbb Q\). There are no genericity qualifications.

## Proof
**The 165 cone curves.** In \(\mathbb F_4\), the cube of every nonzero element is \(1\). Therefore \(X(\mathbb F_4)\) consists of normalized five-tuples with exactly two or four nonzero entries, so it has
\[
\binom52 3+\binom54 3^3=30+135=165
\]
points. Every such point is Hermitian for the standard nondegenerate unitary form \(h(u,v)=\sum_i u_i^2v_i\). By Hermitian Witt coordinates at a point \(P\), the tangent hyperplane section is a cone whose plane section is a smooth Hermitian cubic. For example, with coordinates in which
\[
F=x_0^2x_3+x_0x_3^2+x_1^2x_4+x_1x_4^2+x_2^3,
\]
the point \(P=[1:0:0:0:0]\) has tangent section \(x_3=0\), a cone over the smooth plane cubic
\[
x_1^2x_4+x_1x_4^2+x_2^3=0.\]
The lines in that cone through its vertex form this cubic. Thus \(E_P\) is a smooth plane cubic in a linear Schubert plane of the Grassmannian. Distinct points give distinct curves, since distinct points lie together on at most one line.

**Pairwise intersections and transversality.** If \(P\ne Q\), a line parametrized by both \(E_P\) and \(E_Q\) must be the unique line \(\overline{PQ}\); it lies on \(X\) precisely if \(h(P,Q)=0\). When that occurs the intersection is transverse. Indeed Witt coordinates about the common line permit the local equation \(F\) above with common line \(L=[s:t:0:0:0]\). A first-order nearby line can be written with last three coordinates \((as+bt,cs+dt,es+ft)\). The coefficient of the first-order term of \(F\) is
\[
cs^3+ds^2t+est^2+ft^3.
\]
Consequently \(c=d=e=f=0\), while \(a,b\) freely parametrize the two-dimensional tangent space of \(S\) at \([L]\). The tangent line to \(E_{[s_0:t_0]}\) is \(as_0+bt_0=0\). Distinct \([s_0:t_0]\) impose distinct conditions. Hence
\[
E_P\cdot E_Q=\begin{cases}1,&h(P,Q)=0,\\0,&h(P,Q)\ne0,\end{cases}\qquad(P\ne Q).
\]

**Diagonal intersections.** The Fano scheme is the regular zero locus of the rank-four bundle \(\operatorname{Sym}^3\mathcal U^\vee\) on \(\operatorname{Gr}(2,5)\). Its canonical line bundle is \(\mathcal O_S(1)\), because \(K_{\operatorname{Gr}}=-5H\) and \(c_1(\operatorname{Sym}^3\mathcal U^\vee)=6H\). The Plücker degree of each plane cubic \(E_P\) is \(3\). Adjunction for a smooth genus-one curve gives \(E_P^2=-K_S\cdot E_P=-3\), proving \(G=A-3I\).

**Strong regularity and spectrum.** The isotropic points and totally isotropic lines of the five-dimensional Hermitian space over \(\mathbb F_4\) form the classical generalized quadrangle \(H(4,4)\) of order \((4,8)\). Each point is collinear with \(36\) others. Adjacent points have \(3\) common neighbors and nonadjacent points have \(9\); equivalently the \(165\times165\) adjacency matrix satisfies
\[
A^2=27I-6A+9J.
\]
Thus \(A\) has eigenvalue \(36\) on the all-ones vector, and eigenvalues \(3\) (multiplicity \(120\)) and \(-9\) (multiplicity \(44\)) on its orthogonal complement. Subtracting \(3I\) gives the stated Gram spectrum, whose nonzero rank is \(45\).

**Picard spanning.** For any smooth cubic threefold Fano surface, \(b_2(S)=45\) in \(\ell\)-adic cohomology for \(\ell\ne2\) (Debarre–Laface–Roulleau, Section 4.1). The \(\ell\)-adic divisor-cycle map bounds the Néron–Severi rank by \(b_2\). Since the displayed Gram matrix of algebraic curve classes has rank \(45\), their classes have rational span of dimension \(45\), hence fill \(\operatorname{NS}(S)\otimes\mathbb Q\).

**Arithmetic check (known rank recovered).** The \(\mathbb F_2\)-Frobenius permutes these curves by \(P\mapsto P^{(2)}\). Its permutation on the \(165\) points has \(15\) fixed points, and \(30\) points are adjacent to their own conjugate. For the \((-9)\)-eigenspace of \(A\), the projector is \((15I-5A+J)/60\), so Frobenius has trace \((15\cdot15-5\cdot30+165)/60=4\) on this \(44\)-dimensional space. Together with the all-ones class, its fixed rational span has dimension \(1+(44+4)/2=25\), recovering the published arithmetic Picard rank without claiming it as new.

## Verification
The accompanying standalone `verify.py` enumerates all \(165\) projective Hermitian points using \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\), checks the symmetric adjacency relation, verifies each row has \(36\) neighbors, and exhaustively checks the common-neighbor counts \(3\) and \(9\) for every unordered pair. It also checks the \(15\) rational fixed points, \(30\) points meeting their Frobenius conjugates, and the \(25\)-dimensional invariant span obtained from the eigenspace projector. The geometric transversality and adjunction steps are supplied above as proofs, not merely inferred from finite computation.

## Relationship to prior work
Roulleau's 2010 work calculates intersection numbers and lattice generation for the \(30\) elliptic curves on the **complex** Fermat cubic Fano surface; that result concerns characteristic zero and rank \(25\), not these characteristic-two \(165\) curves. Debarre–Laface–Roulleau's 2015 preprint computes the Fermat cubic Fano surface zeta function and ranks \(25\) over \(\mathbb F_2\) and \(45\) over \(\mathbb F_4\); those ranks are inputs/checks and do not identify the asserted generators. Cheng's later 2023 and 2024 work proves general smoothness and analyzes the Hermitian cone-point geometry of \(q\)-bic Fano surfaces, including families of lines through such points. That geometry is acknowledged; the present finite incidence intersection matrix and rational spanning proof are the proposed additional result.

## Limitations
No integral generating index, torsion, discriminant form, or scheme of *all* elliptic curves is asserted. The calculation does not reprove or improve published point counts and zeta functions. Literature comparisons do not establish absolute priority: an equivalent Picard spanning statement may appear in specialized finite-unitary geometry or under the terminology of cone-point curves. Independent scientific audit has not been performed.

## References
- X. Roulleau, *Fano surfaces with 12 or 30 elliptic curves*, arXiv:1001.4855 (2010), especially Theorem 2 and Lemma 4.
- O. Debarre, A. Laface and X. Roulleau, *Lines on cubic hypersurfaces over finite fields*, arXiv:1510.05803 (first posted 2015-10-20), especially Section 4.1 and Corollary 4.13.
- R. Cheng, *\(q\)-bic hypersurfaces and their Fano schemes*, arXiv:2307.06160 (2023).
- R. Cheng, *\(q\)-bic threefolds and their surface of lines*, arXiv:2402.09884 (2024), especially the Hermitian cone situations in Section 2.
