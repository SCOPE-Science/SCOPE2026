# Three-regime boundary leakage for optimal inversion at a repeated disk-boundary zero

## Finding

Fix an integer \(m\ge2\) and a real \(\alpha<1\). In the analytic coefficient Hilbert space \(\mathcal D_\alpha\), let \(q_n\) be the degree-at-most-\(n\) optimal polynomial approximant to \(1/(1-z)^m\), and let \(R_n=1-(1-z)^m q_n\). Write \(L=n+m\), \(\beta=1-\alpha\), and
\[
C_{\beta,m}=(-1)^{m-1}\frac{(\beta)_m}{(m-1)!},\qquad
D_{\beta,m}=\beta\left(\frac{(\beta+1)_{m-1}}{(m-1)!}\right)^2.
\]
Here \((a)_j=a(a+1)\cdots(a+j-1)\), with \((a)_0=1\).

**Sharp off-zero boundary asymptotics.** The following statements hold *uniformly on every compact subset* \(K\subset\overline{\mathbb D}\setminus\{1\}\), with the limits taken through integers \(n\to\infty\):

- For \(\alpha<0\),
\[
\sup_{z\in K}\left|L R_n(z)-C_{\beta,m}\frac{z^{L+1}}{z-1}\right|\longrightarrow0.
\]
- For \(\alpha=0\),
\[
\sup_{z\in K}\left|L R_n(z)-\frac{C_{1,m}z^{L+1}-D_{1,m}}{z-1}\right|\longrightarrow0.
\]
- For \(0<\alpha<1\), with \(G_\alpha(z)=\sum_{k=0}^\infty z^k/(k+1)^\alpha\) (uniformly convergent on compact subsets of \(\overline{\mathbb D}\setminus\{1\}\)),
\[
\sup_{z\in K}\left|L^{1-\alpha} R_n(z)-D_{\beta,m}G_\alpha(z)\right|\longrightarrow0.
\]

**Interior profile for every \(\alpha<1\).** On every compact subset \(K\subset\mathbb D\),
\[
\sup_{z\in K}\left|L^{1-\alpha}R_n(z)-D_{\beta,m}\sum_{k=0}^\infty\frac{z^k}{(k+1)^\alpha}\right|\longrightarrow0.
\]
In particular, the residual tends uniformly to zero on compact subsets of the *closed* disk away from the repeated root. For every fixed boundary point \(|z|=1\), \(z\ne1\), the order \(L^{-1}\) for \(\alpha<0\) is sharp. For \(0<\alpha<1\), the order \(L^{-(1-\alpha)}\) is sharp at \(z=-1\), since \(G_\alpha(-1)=\eta(\alpha)>0\); at \(\alpha=0\), order \(L^{-1}\) is sharp at \(z=-1\) because \(D_{1,m}=m^2>|C_{1,m}|=m\). These three boundary laws exhibit a transition at the Hardy weight \(\alpha=0\): a terminal oscillatory coefficient dominates for negative weights, a terminal and initial coefficient coexist at zero, and a convergent polylogarithmic initial-coefficient profile dominates for positive weights.

## Assumptions and scope

The domain is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and
\[
\left\|\sum_{k=0}^\infty b_kz^k\right\|_\alpha^2=\sum_{k=0}^\infty(k+1)^\alpha|b_k|^2.
\]
For each \(n\ge0\), \(q_n\) is the unique complex polynomial of degree at most \(n\) minimizing \(\|1-(1-z)^m q\|_\alpha\). Existence and uniqueness follow from finite-dimensional Hilbert projection and injectivity of multiplication by \((1-z)^m\). The exponent \(\alpha\), multiplicity \(m\), and compact set are fixed as \(n\to\infty\). No uniformity as \(\alpha\to0\), \(\alpha\to1\), or \(m\to\infty\) is claimed. For real \(\alpha<0\) this includes the usual weighted-Bergman coefficient regime.

## Proof

**1. An exact finite-degree residual.** Set \(L=n+m\). The polynomial \(R_n\) is the unique minimum-norm polynomial of degree at most \(L\) satisfying \(R_n(1)=1\) and \(R_n^{(j)}(1)=0\) for \(1\le j<m\). Euler derivatives \((z\,d/dz)^j\) generate the same jet constraints at \(1\). By orthogonality (or by the inverse moment Gramian), its coefficients are
\[
R_n(z)=\sum_{k=0}^{L}c_{k,L}z^k,\qquad
c_{k,L}=(k+1)^{-\alpha}\sum_{j=0}^{m-1}A_{j,L}k^j,
\]
where the invertible positive-definite \(m\times m\) matrix and vector are
\[
(E_L)_{ij}=\sum_{k=0}^{L}k^{i+j}(k+1)^{-\alpha},\qquad
A_L=E_L^{-1}e_0,\quad 0\le i,j<m.
\]
The \(k=0\) convention is \(0^0=1\). This exact coefficient representation is the known higher-multiplicity formula of Bénéteau–Manolaki–Seco (Theorem 7.1); it is used as a premise, **not claimed as a new discovery**.

**2. Fixed-dimensional moment scaling.** Let \(\beta=1-\alpha>0\) and \(T_L=\operatorname{diag}(1,L,\ldots,L^{m-1})\). Uniform elementary Riemann-sum estimates, for the fixed indices \(i,j\), give
\[
E_L=L^\beta T_L\,(H+o(1))\,T_L,\qquad H_{ij}=\frac{1}{\beta+i+j}.
\]
The matrix \(H\) is the strictly positive Gramian of \(1,x,\ldots,x^{m-1}\) in \(L^2([0,1],x^{\beta-1}dx)\). Thus its inverse is continuous and, if \(a=H^{-1}e_0\),
\[
A_{j,L}=L^{-\beta-j}(a_j+o(1))\quad(0\le j<m).
\]
In particular \(L^\beta c_{0,L}\to a_0\) and \(L c_{L,L}\to\sum_{j=0}^{m-1}a_j\).

**3. Evaluate both endpoint constants exactly.** Introduce \(P(x)=\sum_{j=0}^{m-1}a_jx^j\) and the rational function
\[
F(t)=\sum_{j=0}^{m-1}\frac{a_j}{t+\beta+j}.
\]
The moment equations \(Ha=e_0\) say \(F(i)=\delta_{i0}\) at \(i=0,\ldots,m-1\). Since its denominator is fixed and its numerator has degree at most \(m-1\), interpolation determines it uniquely:
\[
F(t)=(-1)^{m-1}\frac{(\beta)_m}{(m-1)!}\,
\frac{\prod_{i=1}^{m-1}(t-i)}{\prod_{j=0}^{m-1}(t+\beta+j)}.
\]
Comparing its \(t^{-1}\) coefficient at infinity yields \(P(1)=C_{\beta,m}\); taking its residue at \(t=-\beta\) yields \(P(0)=a_0=D_{\beta,m}\). Both constants are nonzero and \(D_{\beta,m}>0\).

**4. Local interior convergence.** On \(|z|\le r<1\), for each fixed \(j\), the sum \(\sum_{k\ge0} k^j(k+1)^{-\alpha}|z|^k\) is bounded independently of \(L\). Step 2 makes the contributions from \(j\ge1\), after multiplication by \(L^\beta\), tend uniformly to zero, while the \(j=0\) contribution converges uniformly to \(D_{\beta,m}\sum_{k\ge0}(k+1)^{-\alpha}z^k\). This proves the full interior profile.

**5. Positive weights and boundary Dirichlet convergence.** Suppose \(0<\alpha<1\), so \(0<\beta<1\). The \(j=0\) series \(\sum_{k=0}^L(k+1)^{-\alpha}z^k\) converges uniformly on each compact subset of the closed disk away from \(1\): geometric partial sums are bounded by \(2/|1-z|\), and \((k+1)^{-\alpha}\) decreases to zero. For each fixed \(j\ge1\), summation by parts and monotonicity of \(k^j(k+1)^{-\alpha}\) give, uniformly where \(|1-z|\ge\delta>0\),
\[
\left|\sum_{k=0}^L k^j(k+1)^{-\alpha}z^k\right|=O_{j,\alpha,\delta}(L^{j-\alpha}).
\]
Multiplying by \(L^\beta A_{j,L}=O(L^{-j})\) gives \(O(L^{-\alpha})=o(1)\). The \(j=0\) coefficient tends to \(D_{\beta,m}\); hence the positive-weight boundary formula.

**6. Nonpositive weights and both boundary endpoints.** If \(\alpha\le0\), write \(\beta\ge1\). The exact algebraic identity
\[
(z-1)R_n(z)=c_{L,L}z^{L+1}-c_{0,L}
-\sum_{k=1}^{L}(c_{k,L}-c_{k-1,L})z^k
\]
holds for all \(z\). We show, uniformly for \(|z|\le1\), \(|1-z|\ge\delta\), that
\[
\sum_{k=1}^{L}(c_{k,L}-c_{k-1,L})z^k=o(L^{-1}).
\]
Indeed, Abel summation applied to the sequence of first differences bounds this sum by a constant depending on \(\delta\) times the first and last first differences plus the total absolute second variation. For each monomial \(j\), the smooth interpolation \(x^j(x+1)^{\beta-1}\) has second derivative \(O_{\beta,j}((x+1)^{\beta+j-3})\), aside from finitely many harmless first indices. Its coefficient is \(A_{j,L}=O(L^{-\beta-j})\). Consequently the second-variation total is bounded by a fixed sum of quantities of the form
\[
O\!\left(L^{-\beta-j}\sum_{k=1}^{L}(k+1)^{\beta+j-3}\right)=o(L^{-1})
\]
whenever \(\beta>1\), and also for \(\beta=1\), \(j\ge1\); at \(\beta=1\), \(j=0\) is constant and has identically zero variation. Both endpoint first differences obey the same \(o(L^{-1})\) bound. Hence the displayed oscillatory-sum estimate follows. Step 2 gives \(Lc_{L,L}\to C_{\beta,m}\), while \(Lc_{0,L}\to0\) for \(\beta>1\) and \(Lc_{0,L}\to D_{1,m}\) for \(\beta=1\). Division by \(z-1\), uniformly bounded away from zero on \(K\), proves the two remaining boundary formulas.

**7. Sharpness.** When \(\alpha<0\), the leading term at a fixed \(|z|=1\), \(z\ne1\), has modulus \(|C_{\beta,m}|/(|z-1|L)\), independent of the oscillatory phase, and the error is \(o(L^{-1})\). When \(0<\alpha<1\), evaluate at \(z=-1\): \(G_\alpha(-1)=\eta(\alpha)>0\) and \(D_{\beta,m}>0\). At \(\alpha=0\), \(D_{1,m}=m^2\) and \(|C_{1,m}|=m\), so the leading numerator at \(z=-1\) has modulus at least \(m^2-m>0\). This proves the stated sharp orders and completes the proof.

## Verification

A standalone checker `verify.py` reconstructs each finite moment Gramian, checks its moment constraints and endpoint constants, and evaluates the three boundary approximations for multiple degrees and weights. The numerical comparisons test finite examples and their asymptotic behavior; no finite computation substitutes for the inverse-Gramian, rational interpolation, Abel-summation, and Dirichlet-convergence arguments above. Run using `python verify.py` with `mpmath` installed.

## Relationship to prior work

Bénéteau, Manolaki, and Seco, *Boundary behavior of optimal polynomial approximants*, arXiv:1901.00694, Section 7, already give the **exact repeated-root coefficient formula** and sharp **squared-norm** asymptotic. The squared norm is the initial coefficient, so their constant \(1/[\beta B(m,\beta)^2]\), where \(B\) is the beta function, is precisely \(D_{\beta,m}\). Their discussion directly following Corollary 7.4 leaves the repeated-root *uniform closed-disk convergence* problem for future work. Their Theorems 1.8 and 6.1 concern **simple** zeros and do not supply this repeated-zero boundary asymptotic.

The 2026 research record *Additive squared-multiplicity law and Legendre boundary profiles for optimal Hardy approximants* gives a Hardy-space coefficient profile for two or more distinct boundary nodes with multiplicities. Its single-node Legendre polynomial term has the same endpoint constants as the \(\alpha=0\) law here, though the single-node configuration is outside that theorem's stated hypotheses. The distinct contribution here is the sharp weighted boundary profiles, including both non-Hardy regimes and the transition at zero weight. Acuaviva–Seco (2022) investigates zeros of approximants principally with simple boundary zeros. The Bénéteau–Centner survey provides context but no comparable non-Hardy repeated-zero boundary law.

## Limitations

All statements fix one repeated root at \(1\), multiplicity \(m\ge2\), and one real \(\alpha<1\). Rotation transports the result to other isolated unit-circle points. No claim is made for several different repeated roots, moving roots, \(\alpha\ge1\), degree-dependent multiplicity, or compact sets containing the zero. The transition laws are pointwise in the weight, not uniform as \(\alpha\to0\). At \(z=1\) the residual is identically \(1\), so convergence is impossible there. The mathematical proof is independent of numerical experiments, but historical priority for equivalent older coefficient-asymptotic formulations remains subject to further bibliographic review.

## References

1. C. Bénéteau, M. Manolaki, D. Seco, *Boundary behavior of optimal polynomial approximants*, arXiv:1901.00694, first posted 2019-01-03, Sections 6–7, especially Theorems 7.1 and 7.3, discussion after Corollary 7.4. https://arxiv.org/abs/1901.00694
2. A. Acuaviva, D. Seco, *Equidistribution of zeros of some polynomials related to cyclic functions*, published online 2022-03-18, DOI:10.1007/s13324-022-00655-z. https://doi.org/10.1007/s13324-022-00655-z
3. C. Bénéteau, R. Centner, *A survey of optimal polynomial approximants, applications to digital filter design, and related open problems*, arXiv:2102.01725, 2021. https://arxiv.org/abs/2102.01725
4. *Additive squared-multiplicity law and Legendre boundary profiles for optimal Hardy approximants*, research record 2026-10-18, ID `SCOPE-additive-squared-multiplicity-law-and-legendre-boundary-profiles--5397a5ef85ee`.
