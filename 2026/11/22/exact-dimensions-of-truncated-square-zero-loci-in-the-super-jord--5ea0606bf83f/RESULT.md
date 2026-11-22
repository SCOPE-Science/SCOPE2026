# Exact dimensions of truncated square-zero loci in the super Jordan plane

## Finding

**Theorem.** Let \(k\) be an algebraically closed field of characteristic zero and
\[
\mathcal B=k\langle x,y\rangle/(x^2,\;yw-wy-xw),\qquad w=xy+yx,
\]
with \(\deg x=\deg y=1\). For every integer \(m\geq0\), put
\[
\overline{\mathcal Z}_m=\{[a]\in\mathbb P(\mathcal B_{\leq 2m+1}):a^2=0\}.
\]
Then
\[
\boxed{\dim\overline{\mathcal Z}_m=\binom{m+2}{2}-1.}
\]
Equivalently, the corresponding affine square-zero cone has dimension \(\binom{m+2}{2}\). This resolves Conjecture 5.14 of de Araujo–Bagio–Baltazar–Santana–Vinciguerra [1] in every nonnegative truncation degree.

## Assumptions and scope

The base field is algebraically closed and has characteristic zero; all geometric dimensions are Krull dimensions of the reduced underlying varieties. The defining ideal, PBW grading, nilpotent classification and faithful matrix embedding are those in [1, Sections 2 and 5]. The symbol \(\mathcal B_{\leq d}\) denotes the vector space spanned by homogeneous elements of degrees at most \(d\); it is **not** an algebra quotient. Set
\[
D_j=\dim_k k[U,W]_{\leq j}=\binom{j+2}{2}\quad(j\geq0),\qquad D_{-1}=0.
\]
The theorem concerns the full square-zero locus, including its mixed even/odd elements, not only its odd-part linear families.

## Proof

**1. Matrix coordinates and the lower bound.** Let \(I=(x)\). By [1, Lemmas 4.1 and 5.5], every square-zero element lies in \(I\), and \(I\) embeds faithfully in \(M_2(\mathcal J)\), where
\[
\mathcal J=k\langle U,W\rangle/(UW-WU-W^2)
\]
is the Jordan Ore domain. Its PBW basis is \(\{W^iU^j:i,j\geq0\}\). More precisely, with \(z=yx\), the images of \(z^{j+1}y^{2k},\ z^{j+1}y^{2k+1},\ xz^jy^{2k},\ xz^jy^{2k+1}\) respectively occupy the entries \((1,1),(1,2),(2,1),(2,2)\), with coefficients
\[
W^{j+1}U^k,\quad W^{j+1}U^kW,\quad W^jU^k,\quad W^jU^kW.
\]
Since \(UW=W(U+W)\), moving powers of \(W\) to the left preserves the filtration in total \((U,W)\)-degree. Therefore \(I\cap\mathcal B_{\leq2m+1}\) identifies linearly with **all** matrices
\[
M=\begin{pmatrix}Wa&W^2b\\c&Wd\end{pmatrix},
\qquad c\in\mathcal J_{\leq m},\quad
 a,b,d\in\mathcal J_{\leq m-1},
\tag{1}
\]
where the last three spaces are zero at \(m=0\). In particular, setting \(a=b=d=0\) gives a linear space of square-zero matrices of affine dimension \(D_m\), corresponding to \(S_m\) in [1]. Thus \(\dim\overline{\mathcal Z}_m\geq D_m-1\).

**2. A projective Ore deformation.** Introduce the polynomial parameter \(T\) and
\[
\mathcal J_T=k[T]\langle U,W\rangle/(UW-WU-TW^2).
\]
This is the Ore extension \(k[T,W][U;\,\delta]\) with \(\delta(W)=TW^2\), so it is a free \(k[T]\)-module on \(W^iU^j\); multiplication structure constants are polynomial in \(T\). Define \(X_m\subset\mathbb P^{D_m+3D_{m-1}-1}\times\mathbb A^1_T\) by equations \(M^2=0\) for the matrices (1), now over \(\mathcal J_T\). There are only finitely many coefficient equations, all homogeneous quadratic in the matrix coordinates and polynomial in \(T\). Consequently \(X_m\) is closed in projective space over \(\mathbb A^1\), so \(X_m\to\mathbb A^1\) is proper.

For any \(t\in k^\times\), the substitution \(U_t\mapsto tU_1\), \(W_t\mapsto W_1\) is a filtered algebra isomorphism \(\mathcal J_t\cong\mathcal J_1\); it preserves all four entry spaces in (1). Hence each nonzero fiber of \(X_m\) is isomorphic to \(\overline{\mathcal Z}_m\). Upper semicontinuity of dimensions of fibers of a proper morphism [3, Lemma 37.30.5] gives
\[
\dim\overline{\mathcal Z}_m=\dim(X_m)_1\leq\dim(X_m)_0.
\tag{2}
\]
No flatness assumption on the square-zero scheme is needed for this inequality.

**3. The commutative special fiber.** At \(T=0\) the algebra becomes the polynomial ring \(R=k[U,W]\). Because \(R\) is a domain, \(M^2=0\) for (1) is equivalent to the following disjoint cases:

* \(c=0\), \(a=d=0\), with arbitrary \(b\in R_{\leq m-1}\);
* \(c\ne0\), \(d=-a\), and \(a^2+bc=0\).

In the second case, if \(a=0\) then \(b=0\) and \(c\) is arbitrary, giving an affine family of dimension exactly \(D_m\). The first case has dimension \(D_{m-1}\).

Suppose \(a\ne0\), so \(b,c\ne0\). Unique factorization in \(R\) and algebraic closedness of \(k\) give nonzero polynomials \(F,G,H\), up to scalar choices, with
\[
a=HFG,\qquad b=-HF^2,\qquad c=HG^2.
\tag{3}
\]
Indeed, dividing \(b,c\) by their monic gcd makes their coprime residual factors squares up to nonzero scalar multiples; the scalar units can be absorbed because \(k\) is algebraically closed. Write their total degrees as \(r=\deg F\), \(s=\deg G\), \(t=\deg H\). The truncation conditions imply
\[
t+2r\leq m-1,\quad t+2s\leq m,\quad t+r+s\leq m-1.
\tag{4}
\]
For fixed \((r,s,t)\), the image of the polynomial parametrization (3) has dimension **at most** \(D_r+D_s+D_t-1\): the nontrivial rescaling \((F,G,H)\mapsto(\lambda F,\lambda G,\lambda^{-2}H)\) leaves its image unchanged, so every fiber contains a one-dimensional multiplicative orbit. The elementary identities
\[
D_r+D_s=D_{r+s}+1-rs,\qquad
D_{r+s}+D_t=D_{r+s+t}+1-(r+s)t
\]
therefore give
\[
D_r+D_s+D_t-1
 =D_{r+s+t}+1-rs-t(r+s)
 \leq D_{m-1}+1\leq D_m.
\]
There are finitely many degree triples (4). Thus the entire affine commutative special fiber has dimension at most \(D_m\), and its \(c\)-only linear subspace has dimension \(D_m\). Projectivizing yields \(\dim(X_m)_0=D_m-1\). Combining this with (2) and the lower bound proves the result when \(m\geq1\).

**4. The initial case.** At \(m=0\), the matrices (1) are exactly \(\begin{psmallmatrix}0&0\\c&0\end{psmallmatrix}\) with scalar \(c\). Hence the projective locus is one point, of dimension zero, which agrees with \(D_0-1\). \(\square\)

## Verification

The attached `CHECKER.py` implements the Ore PBW product, checks associativity and \(UW-WU=TW^2\) for several parameters, verifies the degree inequality for all \(1\leq m\leq60\), and exhaustively enumerates the degree-three square-zero loci over \(\mathbb F_3\) and \(\mathbb F_5\). The counts are respectively \(33\) and \(145\), agreeing with the known degree-three plane-plus-conic formula \(q^3+q^2-q\) from [1, Proposition 5.23]. These finite checks support the formulas but are not the proof of the all-\(m\) dimension theorem. The geometric proof is the PBW identification, properness and upper semicontinuity in Step 2, and UFD parameter-dimension bound in Step 3.

## Relationship to prior work

De Araujo et al. [1, Conjecture 5.14] state precisely the dimension equality as an open conjecture; their Lemma 5.5 and Proposition 5.23 supply, respectively, the matrix-coordinate ingredient and the \(m=1\) case. Their work already establishes that all nilpotents square to zero and constructs \(S_m\), \(H_m\) and Veronese families. Andruskiewitsch and Dumas [2, Proposition 4.2] classify square-zero elements in the **odd part**, which does not determine the dimensions of the mixed-parity full loci. The new step here is a filtered Jordan-Ore degeneration and a uniform dimension bound on its commutative special fiber. The general upper-semicontinuity principle is standard [3], not claimed as new.

## Limitations

This theorem asserts only the dimension of the reduced projective locus, not its irreducible-component census, scheme structure, degree, Hilbert polynomial or rationality. The argument is presented for algebraically closed fields of characteristic zero; a separate analysis is needed for positive characteristic because the faithful embedding and nilpotent reduction have been taken from the characteristic-zero source. The finite checker does not independently certify the published PBW embedding or proper-fiber theorem. Historical-priority searches are not exhaustive; possible equivalent applications of general degeneration methods remain a priority risk. No independent mathematical audit has been performed.

## References

[1] W. de Araujo, D. Bagio, R. Baltazar, A. Santana, R. Vinciguerra, *The automorphism group of the super Jordan plane*, arXiv:2611.19704v1 (first posted 2026-11-15), §§5.1–5.5, especially Lemma 5.5, Proposition 5.23 and Conjecture 5.14. https://arxiv.org/abs/2611.19704

[2] N. Andruskiewitsch, F. Dumas, *On the super Jordan plane*, arXiv:2509.01918v1 (2025), Proposition 4.2. https://arxiv.org/abs/2509.01918

[3] The Stacks Project, Lemma 37.30.5, Tag 0D4I, upper semicontinuity of dimension of fibers of proper morphisms. https://stacks.math.columbia.edu/tag/0D4I
