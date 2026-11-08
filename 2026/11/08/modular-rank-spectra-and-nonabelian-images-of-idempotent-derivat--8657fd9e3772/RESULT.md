# Modular rank spectra and nonabelian images of idempotent derivations of free class-two Lie algebras

## Finding

Fix an integer \(d\geq3\) and a field \(k\). Let \(V\) be a \(d\)-dimensional \(k\)-vector space, and let
\[
L_d=V\oplus\bigwedge^2V,\qquad [u+z,v+w]=u\wedge v.
\]
This is the free class-two nilpotent Lie algebra on \(d\) generators. Let \(\mathcal E_d(k)\) denote all ordinary derivations \(D:L_d\to L_d\) satisfying \(D^2=D\). The following classification holds over *every* field, including characteristic two.

**Theorem (classification and arithmetic rank spectrum).** Every \(D\in\mathcal E_d(k)\) is uniquely
\[
D=\begin{pmatrix}A&0\\ B&\rho(A)\end{pmatrix},\qquad
\rho(A)(u\wedge v)=Au\wedge v+u\wedge Av,
\]
where \(A\in\operatorname{End}(V)\) is idempotent. Write \(V=U\oplus W\), with \(U=\operatorname{im}(A)\), \(W=\ker(A)\), \(r=\dim U\), and \(s=d-r\).

* If \(\operatorname{char}(k)\ne2\), necessarily \(r\in\{0,1\}\). When \(r=0\) the derivation is zero. When \(r=1\), the free parameter \(B\) satisfies \(B(W)\subseteq U\wedge W\) and \(B(U)\subseteq\bigwedge^2W\), with \(s^2+\binom{s}{2}\) free coordinates, and \(\operatorname{rank}D=d\).
* If \(\operatorname{char}(k)=2\), every \(0\leq r\leq d\) is possible. The free parameter \(B\) satisfies
\[
B(W)\subseteq U\wedge W,\qquad B(U)\subseteq\bigwedge^2U\oplus\bigwedge^2W,
\]
with \(r s^2+r\bigl(\binom r2+\binom s2\bigr)\) free coordinates, and \(\operatorname{rank}D=r(d+1-r)\).

For a finite field \(k=\mathbb F_q\), let \({d\brack r}_q\) be the Gaussian binomial coefficient. The rank-generating polynomial \(R_{d,q}(z)=\sum_{D\in\mathcal E_d(\mathbb F_q)}z^{\operatorname{rank}D}\) is exactly
\[
R_{d,q}(z)=1+{d\brack1}_q q^{(d-1)(3d-2)/2}z^d\quad(q\text{ odd}),
\]
and, when \(q\) is even,
\[
R_{d,q}(z)=\sum_{r=0}^{d}{d\brack r}_q
q^{r(d-r)+r(d-r)^2+r\left(\binom r2+\binom{d-r}2\right)}
z^{r(d+1-r)}.
\]
All displayed exponents are nonnegative integers. In particular, the maximum possible derivation rank equals \(d\) in odd characteristic and \(\lfloor(d+1)^2/4\rfloor\) in characteristic two. In characteristic two, \(\operatorname{im}D\) is an abelian ideal exactly when \(r\leq1\); for \(r\geq2\), it is nonabelian and not an ideal. Thus the finite-field count of operators with nonabelian image is the subsum of the even-characteristic formula over \(2\leq r\leq d\).

**Geometric conclusion.** Over an algebraic closure, the reduced variety of idempotent derivations has exactly two smooth geometrically irreducible connected components in characteristic different from two, and exactly \(d+1\) in characteristic two. The component indexed by \(r\) is a vector bundle over the rank-\(r\) idempotent-matrix variety; it has dimension
\[
2r(d-r)+\begin{cases}
(d-1)^2+\binom{d-1}{2},&\operatorname{char}(k)\ne2,\ r=1,\\
0,&\operatorname{char}(k)\ne2,\ r=0,\\
r(d-r)^2+r\bigl(\binom r2+\binom{d-r}2\bigr),&\operatorname{char}(k)=2.
\end{cases}
\]
The statement concerns reduced geometric varieties, not possible nilpotent structure of the unreduced equation scheme.

## Assumptions and scope

The Lie bracket is alternating in every characteristic: \([x,x]=0\), with \([v,u]=- [u,v]\) in odd characteristic and \([v,u]=[u,v]\) in characteristic two. The vector-space direct sum \(V\oplus\bigwedge^2V\) is part of the specified model. Derivations are ordinary \(k\)-linear derivations, not restricted or higher derivations. For the geometric statement, the algebraic set is equipped with its reduced structure after extension to an algebraic closure. Rank means the rank of \(D\) as an endomorphism of the entire space \(L_d\), whose dimension is \(d+\binom d2\).

## Proof

**1. All derivations.** The derived ideal \([L_d,L_d]=\bigwedge^2V\) is characteristic, so every derivation preserves it. Its action on the quotient \(L_d/[L_d,L_d]\cong V\) is an arbitrary \(A\). The Leibniz identity on the brackets \([u,v]=u\wedge v\) forces the restriction to \(\bigwedge^2V\) to be exactly \(\rho(A)\) as displayed. The central part \(B:V\to\bigwedge^2V\) of \(D|_V\) is unrestricted by Leibniz. Conversely these block matrices obey Leibniz on all pairs, since \(\bigwedge^2V\) is central. This proves the claimed uniqueness without any assumption on the characteristic.

**2. Idempotence.** Squaring the block matrix gives precisely
\[
A^2=A,\qquad \rho(A)^2=\rho(A),\qquad B A+\rho(A)B=B.
\]
Because \(A^2=A\), the decomposition \(V=U\oplus W\) is canonical, and \(A\) acts as one on \(U\), zero on \(W\). The natural decomposition
\[
\bigwedge^2V=\bigwedge^2U\oplus(U\wedge W)\oplus\bigwedge^2W
\]
consists of eigenspaces of \(\rho(A)\), of eigenvalues \(2,1,0\), respectively. Since \(2^2-2=2\), idempotence of \(\rho(A)\) permits \(\bigwedge^2U\ne0\) exactly in characteristic two. Therefore, outside characteristic two we require \(\binom r2=0\), i.e. \(r\leq1\); in characteristic two every \(r\) is allowed.

**3. Classification of the free block.** Restricting \(B A+\rho(A)B=B\) to \(W\) yields \(\rho(A)B(W)=B(W)\), so \(B(W)\) lies in the eigenvalue-one space \(U\wedge W\), of dimension \(rs\). Restricting to \(U\) yields \(\rho(A)B(U)=0\). In characteristic two the latter kernel is \(\bigwedge^2U\oplus\bigwedge^2W\), of dimension \(\binom r2+\binom s2\). Otherwise the only nonzero case has \(r=1\) and the kernel is \(\bigwedge^2W\). Counting the independent column parameters gives the displayed affine-fiber dimensions. No solutions have been omitted.

**4. Full operator rank.** The projection of \(\operatorname{im}D\) to \(V\) equals \(U\), of dimension \(r\). The central intersection \(\operatorname{im}D\cap\bigwedge^2V\) is exactly \(\operatorname{im}\rho(A)=U\wedge W\): every vector mapping to zero in the \(V\)-quotient comes from \(W\oplus\bigwedge^2V\), and \(B(W)\subseteq U\wedge W\). Hence \(\operatorname{rank}D=r+rs=r(d+1-r)\). For odd characteristic the only nonzero case has \(r=1\), giving rank \(d\). For characteristic two, maximizing this concave quadratic over integer \(0\leq r\leq d\) yields \(\lfloor(d+1)^2/4\rfloor\).

**5. Finite-field count.** There are exactly \({d\brack r}_q\) choices for the image \(U\) of an idempotent \(A\), and for each \(U\) there are \(q^{rs}\) complementary kernels \(W\); each complement gives a distinct \(A\). Given \(A\), the allowed \(B\) form an affine linear space of the dimensions determined in step 3. Multiply these factors and sort by the full rank from step 4. In odd characteristic \(r=0\) contributes the zero map, while \(r=1\) contributes exponent \(s+s^2+\binom s2=s(3s+1)/2=(d-1)(3d-2)/2\). In characteristic two, sum the contributions of all \(r\), including different \(r\) that may yield the same full rank. These are the two exact generating polynomials.

**6. Image criterion and components.** In characteristic two, for \(u_1,u_2\in U\), the brackets of their lifted image elements are \(u_1\wedge u_2\). Thus if \(r\geq2\), the image is nonabelian. Moreover these brackets lie in \(\bigwedge^2U\), disjoint from \(\operatorname{im}D\cap\bigwedge^2V=U\wedge W\), so the image is not an ideal. If \(r\leq1\), its brackets are zero and its brackets with \(L_d\) lie in \(U\wedge W\subseteq\operatorname{im}D\), so it is an abelian ideal. The odd-characteristic cases automatically have \(r\leq1\) and the same conclusion.

For geometry, the rank-\(r\) projector variety is the smooth geometrically irreducible homogeneous space \(\mathrm{GL}_d/(\mathrm{GL}_r\times\mathrm{GL}_{d-r})\), of dimension \(2rs\). The linear conditions of step 3 form a constant-rank vector subbundle of \(\mathrm{Hom}(V,\bigwedge^2V)\) over that base, so each allowed \(r\)-stratum is smooth and geometrically irreducible, with the asserted dimension. The characteristic polynomial of \(A\) is \(t^{d-r}(t-1)^r\), which distinguishes the finitely many ranks even in characteristic two; consequently the allowed strata are pairwise disjoint, closed and open in the reduced solution variety, and are exactly its irreducible connected components.

## Verification

The included standalone \(\texttt{check\_idempotent.py}\) constructs the original Lie bracket on the basis \(V\cup\{e_i\wedge e_j\}\) and checks the unaltered Leibniz and idempotence identities. For \(d=2\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\) and \(d=3\) over \(\mathbb F_2\), it exhausts all idempotent quotient blocks \(A\) and all central blocks \(B\), detects solutions from the original square-one identity, determines their *full* linear ranks by elimination, and matches the generating polynomial. Exhaustion of all idempotent \(A\) is complete because every idempotent \(D\) has idempotent quotient block. It also checks the original derivation identity for every matrix constructed. Its binary three-generator result is \(1+1408z^3+448z^4\). The odd-field three-generator prediction is \(1+28431z^3\) for \(q=3\), but that larger case is reported as a formula evaluation and was not exhaustively enumerated. The code includes a true quadratic extension field \(\mathbb F_4\), not integer arithmetic modulo four. It additionally verifies directly that for the three-generator binary case with quotient projection rank two and zero central block, the bracket of two image generators lies outside the image. Output appears verbatim in \(\texttt{verification\_output.txt}\).

## Relationship to prior work

Bai, Gao and Li (2015) prove that the image of an idempotent derivation is an abelian ideal, explicitly assuming complex coefficients; their key step divides a relation by two. That result correctly covers the characteristic-different-from-two image conclusion, but it neither covers nor rules out the characteristic-two nonabelian-image families, nor provides their finite-field rank spectrum. Benito and Roldán-López (first arXiv version 2019) describe derivations of free nilpotent Lie algebras by their action on generators, over characteristic zero. This familiar unrestricted-derivation parametrization is used here as background; the classification and arithmetic of idempotents require the separate characteristic-sensitive matrix analysis. Enomoto and Satoh (2010) treat graded derivation algebras and trace maps of free Lie objects, not the present idempotent-point variety. Milentyeva (2014) provides context on varieties of two-step nilpotent Lie algebras, not this rank census. A prior finite-field census for idempotent derivations of Heisenberg algebras includes the \(d=2\) instance of the present free family; the claim is restricted to the genuinely higher-generator range \(d\geq3\). An earlier analysis of *square-zero* derivations of free class-two Lie algebras studies \(D^2=0\), so does not imply the present idempotent spectrum. Broad undiscovered covering results remain possible.

## Limitations

The result concerns idempotent derivations of the free class-two Lie algebra only, not higher nilpotence class, arbitrary nilpotent Lie algebras, or derivations satisfying other polynomials. It counts labeled operators and does not classify their orbits under automorphisms. It asserts component geometry only for the reduced variety. Finite check cases corroborate but do not replace the exact proof. Publication priority remains subject to further independent evaluation.

## References

1. R. Bai, Y. Gao and Z. Li, *Lie algebras with idempotent derivations*, Mathematica Aeterna **5** (2015), 159–162, https://www.longdom.org/articles-pdfs/lie-algebras-with-idempotent-derivations.pdf . (The article explicitly assumes complex coefficients.)
2. P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897v1 (2019-11-05), https://arxiv.org/abs/1911.01897 .
3. N. Enomoto and T. Satoh, *On the derivation algebra of the free Lie algebra and trace maps*, arXiv:1012.2169v1 (2010-12-10), https://arxiv.org/abs/1012.2169 .
4. M. V. Milentyeva, *Generic properties of 2-step nilpotent Lie algebras and torsion-free groups*, arXiv:1408.0871v1 (2014-08-05), https://arxiv.org/abs/1408.0871 .
