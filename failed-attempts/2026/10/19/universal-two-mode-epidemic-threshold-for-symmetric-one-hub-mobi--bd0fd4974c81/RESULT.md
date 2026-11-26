# Universal two-mode epidemic threshold for symmetric one-hub mobility networks

## Finding
For the SIR-network mobility model with one exceptional transmission patch, all choices of symmetric peripheral mixing have exactly the same basic reproduction number when the flux from the exceptional hub to each peripheral patch is the same. Explicitly, with definitions below,
\[
\mathcal R_0=\frac{T+\sqrt{T^2-4r^2\zeta d^2}}2,\qquad T=r(1+d^2)+\frac{r(\zeta-1)}n[1+(n-1)d^2].
\]
The formula supplies a sharp all-size infection-invasion threshold and establishes the star-class threshold behavior proposed as Conjectures 3 and 4 in the motivating preprint, including even network sizes and peripheral mixing without circulant symmetry.

## Assumptions and scope
Let \(n\ge3\) be an integer. Assume all resident subpopulations have the same positive size, all infected individuals recover at a common rate \(\gamma>0\), and the real \(n\times n\) mobility matrix \(P\) is symmetric, entrywise nonnegative, and row-stochastic. Choose a designated hub indexed by \(n\), assume \(P_{in}=P_{ni}=a\) for every \(1\le i<n\), where \(0<a\le1/(n-1)\), and hence \(P_{nn}=1-(n-1)a\). There are no further assumptions on the peripheral block beyond the stipulated properties. Set the transmission rates to \(\beta_i=\beta_0\) for \(i<n\) and \(\beta_n=\zeta\beta_0\), with \(0<r=\beta_0/\gamma<1\) and \(\zeta>1\). Write \(d=1-na\). The next-generation matrix under these conditions is
\[
K=\frac1\gamma P\operatorname{diag}(\beta_1,\ldots,\beta_n)P
 =rP^2+r(\zeta-1)(Pe)(Pe)^\mathsf T,
\]
where \(e\) is the hub coordinate vector. Strict invasion stability means \(\mathcal R_0=\rho(K)<1\); criticality means \(\mathcal R_0=1\), and invasion instability means \(\mathcal R_0>1\). These definitions are about the infected linearization at a disease-free population configuration; they do not assert asymptotic convergence of all closed-SIR state variables.

Write \(\zeta_c=1+n(1-r)/r\). The sharp classification is:

1. If \(1<\zeta\le1/r\), strict invasion stability holds for every allowed \(a\).
2. If \(1/r<\zeta<\zeta_c\), define
\[
q=\frac{n(1-r)-r(\zeta-1)}{r[1+(n-1)\zeta-nr\zeta]}\in(0,1).
\]
Then strict invasion stability holds exactly when \(|1-na|<\sqrt q\); at equality the system is at its linear infection threshold; and for \(|1-na|>\sqrt q\) it is invasion-unstable. These tests are applied only to the physical domain \(0<a\le1/(n-1)\), so any interval truncation is automatic.
3. If \(\zeta=\zeta_c\), \(a=1/n\) is critical and every other allowed \(a\) is invasion-unstable. If \(\zeta>\zeta_c\), every allowed \(a\) is invasion-unstable.

## Proof
**Invariant decomposition.** Let \(\mathbf1\) be the all-ones vector. Stochasticity gives \(P\mathbf1=\mathbf1\), while the uniform hub coupling gives \(Pe=a\mathbf1+de\). Consequently the two-dimensional subspace \(U=\operatorname{span}\{\mathbf1,e\}\) is \(P\)-invariant. Since \(P\) is symmetric, \(U^\perp\) is invariant too. Both \(Pe\) and the rank-one perturbation in \(K\) belong to \(U\). On \(U^\perp\) the next-generation matrix is \(rP^2\). A symmetric nonnegative stochastic matrix has all eigenvalues in \([-1,1]\), so each eigenvalue of \(K\) on \(U^\perp\) belongs to \([0,r]\), strictly below one.

**Exact two-mode spectrum.** The orthonormal basis
\[
u=\frac{\mathbf1}{\sqrt n},\qquad v=\sqrt{\frac n{n-1}}\left(e-\frac{\mathbf1}n\right)
\]
of \(U\) satisfies \(Pu=u\) and \(Pv=dv\), while \(e=u/\sqrt n+\sqrt{(n-1)/n}\,v\). Therefore the restriction of \(K\) to \(U\) is
\[
K_U=r\begin{pmatrix}1&0\\0&d^2\end{pmatrix}
+\frac{r(\zeta-1)}n
\begin{pmatrix}1&d\sqrt{n-1}\\d\sqrt{n-1}&(n-1)d^2\end{pmatrix}.
\]
It has trace \(T\), and its determinant is \(r^2\zeta d^2\) by the determinant lemma. Its larger eigenvalue is the displayed closed formula. The Rayleigh quotient of \(K\) at \(u\) is \(r[1+(\zeta-1)/n]>r\). Consequently the largest eigenvalue on \(U\) strictly exceeds every eigenvalue on \(U^\perp\). Thus the displayed formula is the **full** \(\mathcal R_0\), not merely a bound or a special-subspace eigenvalue. In particular, peripheral mixing affects other eigenvalues but cannot change \(\mathcal R_0\).

**Sharp threshold.** Let \(h=r(\zeta-1)>0\). Since \(0<r<1\), the positive-definite diagonal matrix \(H=\operatorname{diag}(1-r,1-rd^2)\) obeys
\[
I-K_U=H-hww^\mathsf T,\qquad w=\frac1{\sqrt n}\begin{pmatrix}1\\d\sqrt{n-1}\end{pmatrix}.
\]
The rank-one positive-definiteness criterion yields \(\mathcal R_0<1\) exactly when
\[
\frac h n\left[\frac1{1-r}+\frac{(n-1)d^2}{1-rd^2}\right]<1.
\]
All omitted denominators are strictly positive because \(|d|<1\): indeed \(a>0\), \(a\le1/(n-1)\), and \(n\ge3\). Clearing them gives the equivalent inequality
\[
A-Bd^2>0,\qquad A=n(1-r)-r(\zeta-1),\quad B=r[1+(n-1)\zeta-nr\zeta].
\]
When \(\zeta\le1/r\), \(h\le1-r\) and \(d^2<1\) makes the preceding positive-definiteness inequality strict. If \(1/r<\zeta<\zeta_c\), then \(A>0\) and \(B>0\). To check the latter without hidden sign assumptions, observe that \(B\) is affine in \(\zeta\), and at the two endpoints its values are \((n-1)(1-r)\) and \(n(n-1)(1-r)^2\), both positive. In this same range, \(0<A/B<1\): at \(\zeta=1/r\) the quotient is one, and its numerator tends to zero at \(\zeta_c\), while its denominator remains positive. Furthermore \(A-B=n(1-r)(1-r\zeta)<0\) above \(\zeta=1/r\), so the quotient is strictly below one. The resulting inequality is exactly \(|d|<\sqrt{A/B}\), with equality giving a unit leading eigenvalue. Finally, \(\zeta>\zeta_c\) implies the Rayleigh quotient \(r[1+(\zeta-1)/n]>1\), so instability holds regardless of \(a\). At equality \(\zeta=\zeta_c\), the same quotient equals one; the determinant identity \(n\det(I-K_U)=A-Bd^2\) with \(A=0\) and \(B>0\) makes the leading eigenvalue greater than one for \(d\ne0\), while \(d=0\) gives the threshold eigenvalue one. This completes all cases.

## Verification
A standalone standard-library Python script, `verify.py`, carries out exact-rational matrix calculations. It constructs different nonnegative symmetric stochastic peripheral mixtures for network sizes three through ten; checks the \(U\)-invariance, exact two-mode trace and determinant, independence from peripheral mixing, and the algebraic unit-threshold identity; and additionally verifies seventeen exact critical hub-coupling instances. The program reports 192 rational comparisons and 17 critical cases. Finite tests are illustrations only: the proof for all \(n\) is the invariant decomposition and positive-definiteness argument above.

## Relationship to prior work
Das and Stolerman, *Epidemic Thresholds and Disease Dynamics in Metapopulations* (preprint arXiv:2308.01998, initially public on 2023-08-03; journal article DOI 10.1137/23M1579522), derive the next-generation matrix and formulate their broader star-class claims as Conjectures 3 and 4 (preprint page 16). Their appendix proves representative cases of size nine and seven but not a general arbitrary-size theorem. The earlier fully connected calculation of Stolerman, Coombs, and Boatto (2015, Theorem 2) is covered as a special case. The present result proves the conjectured strict threshold formula for every symmetric stochastic peripheral block with equal hub coupling and gives a network-independent full spectral radius; it does not require peripheral circulant structure or odd size. It does not extend to arbitrary asymmetric, unequal-population, or nonuniform-hub flux matrices.

## Limitations
The result concerns the invasion spectrum for the equal-population SIR network, not the magnitude, timing, or final size of epidemics, nor global nonlinear SIR attraction. Nonuniform hub exchanges, directed mobility, unequal patch populations, multiple heterogeneous hotspots, and heterogeneous recovery are not covered. At \(\mathcal R_0=1\), linearization is critical; nonlinear center dynamics are not classified. Mathematical originality is supported by comparisons with the cited papers and targeted literature and indexed searches, but cannot exclude all unindexed or later literature. The separately hosted journal article's complete text and supplement were not accessible in this examination; its publicly available abstract retains the language of unresolved conjectures.

## References
1. H. K. Das and L. M. Stolerman, *Epidemic thresholds and disease dynamics in metapopulations: the role of network geometry and human mobility*, arXiv:2308.01998, first version dated 2023-08-03. https://arxiv.org/abs/2308.01998 ; preprint relevant sections 2, 4.4.3 and Appendix B, pages 3, 15–16, 36–38.
2. H. K. Das and L. M. Stolerman, *Epidemic Thresholds and Disease Dynamics in Metapopulations: The Role of Network Structure and Human Mobility*, SIAM J. Appl. Dyn. Syst. 23 (2024), 1579–1609, DOI:10.1137/23M1579522; online 2024-06-20. https://doi.org/10.1137/23M1579522.
3. L. M. Stolerman, D. Coombs, and S. Boatto, *SIR-Network Model and Its Application to Dengue Fever*, SIAM J. Appl. Math. 75 (2015), 2581–2609, Theorem 2, DOI:10.1137/140996148. https://doi.org/10.1137/140996148.
4. D. Bichara and A. Iggidr, *Multi-Patch and Multi-Group Epidemic Models: A New Framework*, arXiv:1703.04554 (2017); a different rank-one residence-matrix setting. https://arxiv.org/abs/1703.04554.
