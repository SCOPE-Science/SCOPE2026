# Sharp multiplicity-stratified Hölder stability of ellipsoid intrinsic-volume recovery

## Finding
For every integer \(n\ge2\), let \(E\) be a full-dimensional Euclidean ellipsoid, with positive semiaxes arranged in increasing order \(a_1(E)\le\cdots\le a_n(E)\). Let \(V_k(E)\) be its Steiner intrinsic volumes, defined by
\[
\operatorname{Vol}_n(E+tB^n)=\sum_{k=0}^n\kappa_{n-k}V_k(E)t^{n-k},\qquad \kappa_j=\frac{\pi^{j/2}}{\Gamma(1+j/2)},
\]
and put \(v_k(E)=V_k(E)/\kappa_k\). For ellipsoids \(E,F\), define
\[
d(E,F)=\max_{1\le i\le n}|a_i(E)-a_i(F)|,\qquad \eta(E,F)=\max_{1\le k\le n}|v_k(E)-v_k(F)|.
\]

**Theorem.** Fix a full-dimensional ellipsoid \(E_0\) in \(\mathbb R^n\), and let \(m\) be the largest multiplicity of any one of its semiaxis lengths. There are constants \(r>0\) and \(C>0\), depending on \(E_0\), such that
\[
d(E,F)\le C\,\eta(E,F)^{1/m}
\]
for every pair of full-dimensional ellipsoids satisfying \(d(E,E_0)<r\) and \(d(F,E_0)<r\). The exponent \(1/m\) is *optimal*: for every such \(E_0\) there are pairs \(E_\varepsilon,F_\varepsilon\to E_0\) such that
\[
d(E_\varepsilon,F_\varepsilon)=\Theta(\varepsilon),\qquad \eta(E_\varepsilon,F_\varepsilon)=\Theta(\varepsilon^m).
\]
Thus recovery is locally Lipschitz at ellipsoids with pairwise distinct axes, but loses exactly one Hölder order for each increase of the largest axis multiplicity. The round-ball exponent is exactly \(1/n\).

As an explicit three-dimensional sharpness witness, choose squared semiaxes \((1+2\varepsilon,1-\varepsilon,1-\varepsilon)\) and \((1-2\varepsilon,1+\varepsilon,1+\varepsilon)\) for \(0<\varepsilon<1/2\). Then
\[
d(E_\varepsilon,F_\varepsilon)=\varepsilon+O(\varepsilon^2),\quad
\eta(E_\varepsilon,F_\varepsilon)=2\varepsilon^3+O(\varepsilon^5),\quad
\lim_{\varepsilon\downarrow0}\frac{d(E_\varepsilon,F_\varepsilon)}{\eta(E_\varepsilon,F_\varepsilon)^{1/3}}=2^{-1/3}.
\]

## Assumptions and scope
Only full-dimensional ellipsoids and their unordered semiaxis multisets are considered; centers and orientations cannot be recovered from intrinsic volumes. The bounds are local around a fixed positive semiaxis multiset. The constants are not asserted to remain bounded as two distinct axis clusters coalesce. The proof treats all integers \(n\ge2\), including repeated axes, not a finite enumeration.

## Proof
**1. Smooth invertibility in elementary symmetric coordinates.** Write the squared semiaxes as \(\lambda_i=a_i^2>0\) and form
\[
Q(u)=\prod_{i=1}^n(1+\lambda_i u)=\sum_{j=0}^n s_j u^j,\qquad s_0=1,\qquad T_k(u)=\sum_{p=0}^{k-1}s_pu^p.
\]
An established ellipsoid intrinsic-volume integral identity (Gusakova--Spodarev--Zaporozhets, and formula (3) in Myroshnychenko--Tatarko--Yaskin) is
\[
v_k=\frac12\int_0^\infty u^{-k/2}
\frac{T_kQ'-T_k'Q}{Q^{3/2}}\,du,\qquad 1\le k\le n.
\]
Its numerator is exactly \(\sum_{p<k\le q}(q-p)s_ps_qu^{p+q-1}\). Thus the integral converges locally uniformly on positive-coefficient compact sets: its integrand is \(O(u^{k/2-1})\) near zero and \(O(u^{(k-n)/2-2})\) at infinity. The function of coefficients extends differentiably on an open positive-coefficient neighborhood of every ellipsoid. In addition, \(v_n=\sqrt{s_n}\).

We recall the **specific established strict-Jacobian lemma**, identifying the part borrowed from Myroshnychenko--Tatarko--Yaskin (2026), Lemmas 3.5, 4.1, 4.2 and their proof. At each ellipsoid, the \((n-1)\)-square matrix
\[
M_{kj}=\frac1{v_k}\frac{\partial v_k}{\partial s_j},\qquad 1\le k,j<n,
\]
has positive entries and for each column \(j\) satisfies \(M_{k-1,j}-2M_{k,j}+M_{k+1,j}>0\) for \(k\ne j\), with \(M_{0,j}=M_{n,j}=0\). For precision, their derivative formula is
\[
\frac{\partial v_k}{\partial s_j}=\frac14\int_0^\infty u^{j-k/2-1}Q(u)^{-3/2}
\begin{cases}A_k(u),&j\ge k,\\B_k(u),&j<k,\end{cases}\,du,
\]
where \(A_k=\sum_{p<k}(k-p)s_pu^p\) and \(B_k=\sum_{p>k}(p-k)s_pu^p\). Their strict convexity lemma proves the asserted second differences for \(u^{-k/2}A_k/v_k\) and \(u^{-k/2}B_k/v_k\) using the Alexandrov--Fenchel inequalities and Cauchy--Schwarz; the \(B\) case is transported from the polar ellipsoid. Integration against the strictly positive kernel retains strictness. This nontrivial lemma is cited, not reasserted as an original discovery.

To see explicitly why it yields invertibility, let \(L\) be the tridiagonal Dirichlet matrix with diagonal \(2\) and immediate off-diagonals \(-1\). Then \(G=LM\) has strictly negative off-diagonal entries and positive column sums \(\sum_{k=1}^{n-1}G_{kj}=M_{1j}+M_{n-1,j}>0\). Consequently each diagonal entry of \(G\) is larger than the sum of the absolute off-diagonal entries in its column. Strict column diagonal dominance makes \(G\), hence \(M\), invertible. Since \(v_n=\sqrt{s_n}\), the full Jacobian \(D_s(v_1,\ldots,v_n)\) is block triangular, with a nonsingular first block and bottom-right entry \(1/(2\sqrt{s_n})>0\); it is nonsingular. For \(n=2\) the one-by-one block is immediately positive.

The inverse-function theorem, applied on the positive-coefficient extension, gives a neighborhood of the coefficient vector of \(E_0\) and a constant \(C_0\) such that for any two ellipsoids there,
\[
\max_j|s_j(E)-s_j(F)|\le C_0\eta(E,F).
\tag{1}
\]
This is stronger than bare uniqueness of the ellipsoid from its intrinsic volumes: it controls *polynomial coefficients* linearly.

**2. Root matching with the exact multiplicity exponent.** Let \(\alpha_1,\ldots,\alpha_b>0\) be the distinct squared semiaxes of \(E_0\), with multiplicities \(m_1,\ldots,m_b\) and \(m=\max m_j\). Choose disjoint fixed small neighborhoods of the \(\alpha_j\)'s. For \(E,F\) close enough to \(E_0\), each contains exactly \(m_j\) squared axes in the corresponding neighborhood. Put \(\delta=\max_j|s_j(E)-s_j(F)|\) and consider the monic polynomials
\[
P_E(z)=\prod_i(z-\lambda_i(E)),\qquad P_F(z)=\prod_i(z-\lambda_i(F)).
\]
Their coefficient distance is \(\delta\), so on the fixed bounded union of axis neighborhoods \(|P_E(z)-P_F(z)|\le C_1\delta\). Within cluster \(j\), draw closed disks of radius \(\rho_j=K_j\delta^{1/m_j}\) around all \(m_j\) roots of \(P_E\). If \(\delta>0\) is sufficiently small, these disks remain in the cluster neighborhood, and on the boundary of every connected component of their union, the factors from the current cluster have modulus at least \(\rho_j\), while factors from other clusters have modulus at least a fixed positive gap. Therefore
\[
|P_E(z)|\ge \rho_j^{m_j}g^{n-m_j}>C_1\delta\ge |P_F(z)-P_E(z)|
\]
when \(K_j\) is chosen sufficiently large. Rouché's theorem on each component (on the simple outer boundary of each collinear disk chain) shows the same number of roots of \(P_E\) and \(P_F\) in that component. A component containing \(q\le m_j\) disks has diameter at most \(2q\rho_j\). Thus the real roots in each component can be paired with distance at most \(2m_j\rho_j\). This proves
\[
\max_i|\lambda_i(E)-\lambda_i(F)|\le C_2\max_j\delta^{1/m_j}\le C_3\delta^{1/m}
\]
for sufficiently small \(\delta\). Finally the square-root map is uniformly Lipschitz on an interval bounded away from zero. Combining with (1) proves the asserted bound. If \(\delta=0\), polynomial coefficients and hence semiaxes agree exactly.

**3. Sharpness at every multiplicity.** Select a squared-axis cluster \(\alpha\) of size \(m\). Choose distinct real numbers \(c_1<\cdots<c_m\) and let \(f(z)=\prod_{i=1}^m(z-c_i)\). Choose a sufficiently small fixed nonzero real \(\tau\) so that \(f(z)+\tau\) still has \(m\) distinct real roots \(d_1<\cdots<d_m\) (the implicit-function theorem at the simple roots gives this). For small \(\varepsilon>0\), replace the original cluster in one ellipsoid by squared axes \(\alpha+\varepsilon c_i\), in the other by \(\alpha+\varepsilon d_i\), leaving every other squared axis unchanged. The two monic characteristic polynomials differ exactly by the factor \(\tau\varepsilon^m\) times the monic polynomial of all other roots. Thus their symmetric coefficient distance is \(\Theta(\varepsilon^m)\). The intrinsic-volume data have distance \(\Theta(\varepsilon^m)\): the upper bound follows from smoothness, the lower from (1). Yet their ordered semiaxes differ by \(\Theta(\varepsilon)\), since the two root sets are distinct. Hence no exponent larger than \(1/m\) can hold near \(E_0\).

**4. Exact three-dimensional witness.** At the unit ball in dimension three, differentiating the integral by the beta integral \(\int_0^\infty u^{a-1}(1+u)^{-a-b}\,du=\Gamma(a)\Gamma(b)/\Gamma(a+b)\) gives
\[
D_s(v_1,v_2,v_3)\big|_{(s_1,s_2,s_3)=(3,3,1)}=
\begin{pmatrix}8/35&4/105&1/35\\4/105&8/35&6/35\\0&0&1/2\end{pmatrix},\qquad\det D_s=8/315.
\]
The two squared-axis triples in the finding have identical first and second symmetric sums, while their third sums differ by exactly \(4\varepsilon^3\). Consequently the data difference has leading vector \((4/35,24/35,2)\varepsilon^3\), with error \(O(\varepsilon^5)\). Their ordered semiaxes differ by \(\varepsilon+O(\varepsilon^2)\), establishing the displayed exact limiting ratio.

## Verification
The standalone standard-library file `verify.py` numerically integrates the independently expanded \(p<k\le q\) intrinsic-volume integrand, checks Euclidean unit-ball normalizations in dimensions two to four, checks the exact beta-integral Jacobian entries at the three-ball by central finite differences, and checks the three-dimensional cubic witness at four distinct perturbation sizes. Run from the extracted package with `python3 verify.py`. Its observed output: `PASS: 28 finite checks` and the limiting data-distance ratios tend toward \(2\). The infinite-dimensional and all-multiplicity assertions are analytical; finite computations do not certify them.

## Relationship to prior work
Kabluchko, Marynych and Prochno (first posted 12 May 2026) give intrinsic-volume formulas for coordinate-weighted \(\ell_p\) balls, specializing at \(p=2\) to ellipsoids, and motivate the inverse conditioning question. Gusakova, Spodarev and Zaporozhets give integral formulas for ellipsoid intrinsic volumes. Petrov and Tarasov establish three-dimensional uniqueness. Myroshnychenko, Tatarko and Yaskin (first publicly posted 18 November 2026) establish all-dimensional uniqueness and the strict-Jacobian lemma **used explicitly as a premise here**. Neither their uniqueness theorem nor the cited integral formulas state the sharp local all-multiplicity Hölder exponent, pairwise noise bound, or sharpness constructions. Mere uniqueness, of course, is not claimed as new.

## Limitations
The estimate is local in axis-multiset space, with unspecified constants; no stability is asserted for orientation, center, general convex bodies, vanishing semiaxes, or global measurement noise outside the neighborhood. The sharpness example is not claimed to optimize the prefactor among every possible noisy pair. The central Jacobian nonsingularity is obtained from the cited existing theorem, so the contribution is the exact singular-root conditioning classification and its sharpness rather than a separate derivation of uniqueness. Independent validation has not been performed, and unindexed historical quantitative inverse-geometry work could bear on priority.

## References
1. Z. Kabluchko, A. Marynych and J. Prochno, *Intrinsic volumes of \(\ell_p\)-balls and a continuum of Maxwell--Poincaré--Borel laws for their curvature measures*, arXiv:2605.11995v1, publicly posted 2026-05-12, https://arxiv.org/abs/2605.11995.
2. A. Gusakova, E. Spodarev and D. Zaporozhets, *Intrinsic volumes of ellipsoids*, 2022; see https://arxiv.org/search/?query=Gusakova+Spodarev+Zaporozhets+Intrinsic+volumes+ellipsoids&searchtype=all.
3. F. Petrov and A. Tarasov, *Uniqueness of a three-dimensional ellipsoid with given intrinsic volumes*, Arnold Mathematical Journal 6 (2020), 163--171.
4. S. Myroshnychenko, K. Tatarko and V. Yaskin, *Unique determination of ellipsoids by their intrinsic volumes*, arXiv:2611.24923v1, first posted 2026-11-18; especially Lemmas 3.5, 4.1 and 4.2 and Section 5; https://arxiv.org/abs/2611.24923.
