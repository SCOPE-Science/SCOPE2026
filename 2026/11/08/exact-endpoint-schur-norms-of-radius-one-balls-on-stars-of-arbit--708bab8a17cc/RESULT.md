# Exact endpoint Schur norms of radius-one balls on stars of arbitrary degree

## Finding

Let \(V_n=\{0,1,\ldots,n\}\) be the vertices of the graph star \(K_{1,n}\), with center \(0\) and \(n\) leaves. Set \(m_{ij}^{(n)}=1\) when the graph distance \(d(i,j)\le1\), and \(m_{ij}^{(n)}=0\) otherwise. Let \(P_n(X)=(m_{ij}^{(n)}x_{ij})\) be the Schur projection on the complex operator algebra \(B(\ell^2(V_n))\).

**Theorem.** For every integer \(n\ge1\),
\[
\|P_n\|_{B\to B}=\|P_n\|_{\mathrm{cb}}=\frac{5n-1}{3n+1}=\frac53-\frac{8}{3(3n+1)}.
\]
For the countably infinite star \(V_\infty=\{0\}\cup\mathbb N\) with the same radial mask, the analogous Schur projection has operator and completely bounded norm exactly \(5/3\). On trace class, the same masks have the same norms by duality; on Hilbert–Schmidt class they have norm one.

Thus the endpoint norm increases strictly with the degree of the star and has a finite, sharp unbounded-degree limit. The \(n=2\) value \(9/7\) was known (Levene, 2014) and is not asserted to be new.

## Assumptions and scope

All matrices and operators are complex. The completely bounded norm is \(\sup_{k\ge1}\|\mathrm{Id}_{M_k}\otimes P\|\), with the spatial matrix amplification. The graph distance is the usual edge distance; the mask retains the diagonal and center–leaf entries but deletes distinct-leaf entries. The infinite-star operator acts on \(B(\ell^2(V_\infty))\), not just finite matrices. No regularity, bounded degree, or finite-rank restriction is assumed for the infinite star.

## Proof

**1. Finite upper bound by positive Schur symbols.** Fix \(n\ge1\), and define
\[
t=\frac{5n-1}{3n+1},\qquad x=t-1=\frac{2(n-1)}{3n+1},\qquad d=1-x.
\]
Define the real symmetric matrix \(H\) by \(H_{ii}=t\), \(H_{0j}=H_{j0}=d\) for each leaf, and \(H_{ij}=x\) when \(i\ne j\) are leaves. We claim that \(H+M\) and \(H-M\) are positive semidefinite, where \(M=(m_{ij}^{(n)})\).

The leaf-coordinate space orthogonal to the all-ones vector has eigenvalues \(t-x+1=2\) for \(H+M\) and \(t-x-1=0\) for \(H-M\). On the orthogonal two-dimensional space spanned by the center and the normalized all-ones leaf vector, the two matrices have representatives
\[
\begin{pmatrix}t\pm1&\sqrt n(d\pm1)\\ \sqrt n(d\pm1)&t+(n-1)x\pm1\end{pmatrix}.
\]
Their diagonal entries are nonnegative and each determinant vanishes: direct substitution gives
\[
(t\pm1)(t+(n-1)x\pm1)=n(d\pm1)^2.
\]
These facts prove both matrices are positive semidefinite, including the \(n=1\) boundary case.

Put \(Q_+=(H+M)/2\) and \(Q_-=(H-M)/2\). Their Schur actions are completely positive, and since every diagonal entry of \(Q_\pm\) equals \((t\pm1)/2\), the completely positive Schur-multiplier norm formula gives
\[
\|P_n\|_{\mathrm{cb}}\le\|S_{Q_+}\|_{\mathrm{cb}}+\|S_{Q_-}\|_{\mathrm{cb}}=\frac{t+1}{2}+\frac{t-1}{2}=t.
\]
For clarity, the positive Schur-multiplier norm formula follows from a Gram factorization of its positive kernel and equality on the identity operator.

**2. Matching lower bound from a trace-norm witness.** Set
\[
q=\frac{n+1}{3n+1},\qquad r=\frac{2}{3n+1},\qquad u=(\sqrt q,\underbrace{\sqrt r,\ldots,\sqrt r}_{n\text{ leaves}}).
\]
The identity \(q+nr=1\) makes \(u\) a unit vector. The Hermitian matrix \(B=\mathrm{diag}(u)M\mathrm{diag}(u)\) has diagonal entries \(q,r,\ldots,r\), has center–leaf entries \(\sqrt{qr}\), and has zero off-diagonal entries between distinct leaves. On leaf-difference vectors its eigenvalue is \(r\) (multiplicity \(n-1\)). On the center and normalized leaf-average plane it has the matrix
\[
\begin{pmatrix}q&\sqrt{nqr}\\\sqrt{nqr}&r\end{pmatrix}.
\]
Since \((q-r)^2+4nqr=1\), the two eigenvalues are \(2(n+1)/(3n+1)\) and \(-(n-1)/(3n+1)\). Consequently
\[
\|B\|_{S_1}=\frac{2(n+1)+(n-1)+2(n-1)}{3n+1}=t.
\]
Choose the self-adjoint contraction \(X=\operatorname{sgn}(B)\), defining its sign as zero on the null space. As \(M\) is real symmetric,
\[
\langle P_n(X)u,u\rangle=\operatorname{Tr}(BX)=\|B\|_{S_1}=t.
\]
The left side is bounded by \(\|P_n\|\|X\|\le\|P_n\|\). Thus \(\|P_n\|\ge t\), and together with the previous step all claimed finite-dimensional equalities follow.

**3. Countably infinite star.** Let \(M_\infty\) be the radial mask on \(V_\infty\). For bounded diagonal sequences
\[
v_0=\frac{2}{\sqrt3},\quad v_j=\frac1{\sqrt3}\ (j\ge1),\qquad
w_0=\frac1{\sqrt3},\quad w_j=-\frac1{\sqrt3}\ (j\ge1),
\]
write \(D_v,D_w\) for the corresponding bounded diagonal operators on \(\ell^2(V_\infty)\). Entrywise, the mask decomposes as
\[
M_\infty=Q_+-Q_-,\qquad Q_+=vv^*+\operatorname{diag}(0,1,1,\ldots),\quad Q_-=ww^*,
\]
where \(vv^*\) and \(ww^*\) designate positive kernels, not rank-one bounded operators (the sequences need not lie in \(\ell^2\)). The associated Schur maps are well defined and completely positive: \(S_{Q_+}(X)=D_vXD_v^*+\sum_{j\ge1}E_{jj}XE_{jj}\) and \(S_{Q_-}(X)=D_wXD_w^*\). The diagonal sum converges ultraweakly and defines diagonal conditional expectation onto the leaves. Because \(Q_+\) has diagonal \(4/3\) at every vertex and \(Q_-\) diagonal \(1/3\), their completely bounded norms are respectively \(4/3\) and \(1/3\). Hence \(\|P_\infty\|_{\mathrm{cb}}\le5/3\).

Every finite star is a principal corner of the infinite star, so \(\|P_\infty\|\ge\sup_{n\ge1}(5n-1)/(3n+1)=5/3\), proving both infinite norms exactly.

**4. Trace and Hilbert–Schmidt endpoints.** Schur multiplication by this symmetric real mask is self-adjoint under the trace pairing, so its operator norm on trace class equals its dual operator norm on \(B(\ell^2)\). On Hilbert–Schmidt class the mask is an orthogonal coordinate projection, of norm one. The same conclusions hold for both finite and infinite stars.

## Verification

The standalone script `checks/star_ball_checker.py` runs using Python's standard library and checks 15 exact rational identities for each degree from 1 through 1024; its output is `STAR_BALL_EXACT_CERTIFICATES_OK 15360`. In particular it verifies the two determinant equalities, leaf-subspace eigenvalues, lower-bound eigenvalue discriminant and trace identity, and normalization. The proof for every degree and the infinite star is analytical; finite checks alone do not establish those universal statements.

## Relationship to prior work

González-Pérez and collaborators (2026, arXiv:2610.15881v1) study radial Schur multipliers on trees and Fourier–Schur transference, motivating an exact endpoint test for a particularly simple bounded-diameter family. Arhancet (2026, arXiv:2610.30832v1) studies quantitative transference and complete boundedness in intermediate Schatten regimes. Neither inspected result gives the all-degree radius-one star operator-norm formula above.

The two-leaf star has three vertices and gives \(9/7\), an exact norm already calculated as a three-by-three idempotent mask by Levene (2014). The result here is the full expression for arbitrary numbers of leaves, in particular degrees at least three, together with the countably infinite star limit. Davidson and Donsig (2005) establish general factorization techniques and compute other symmetric Schur patterns; their general methods are related but do not give the displayed all-star formula as a stated theorem. These comparisons concern mathematical implication and parameter range, not just matching terminology.

## Limitations

This result treats the radius-one zero-one mask on a star and the two endpoint Schatten classes together with Hilbert–Schmidt, not arbitrary radial profiles, other trees, or the full range of Schatten exponents. It does not claim the known \(n=2\) value as new. Earlier unindexed graph-pattern or Schur-factorization formulae may be equivalent to the all-degree identity; publication priority is not independently certified. No independent mathematical audit has been performed.

## References

1. A. González-Pérez et al., *Radial Schur multipliers on trees and the failure of Fourier–Schur transference* (2026), arXiv:2610.15881v1, https://arxiv.org/abs/2610.15881. First public version dated 2026-10-11.
2. C. Arhancet, *Radial Schur multipliers on trees and quantitative Fourier–Schur separation* (2026), arXiv:2610.30832v1, https://arxiv.org/abs/2610.30832.
3. R. H. Levene, *Norms of idempotent Schur multipliers*, New York Journal of Mathematics **20** (2014), 325–352, Proposition 5.1(8), https://nyjm.albany.edu/j/2014/20-19.html.
4. K. R. Davidson and A. P. Donsig, *Norms of Schur multipliers* (2005), arXiv:math/0506073, https://arxiv.org/abs/math/0506073.
