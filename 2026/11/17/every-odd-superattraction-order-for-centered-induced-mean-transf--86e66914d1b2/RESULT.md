# Every odd superattraction order for centered induced mean transforms of period-two shifts

## Finding

Let \(M\) be a normalized Kubo–Ando operator mean with representing function \(f\), and assume \(f'(1)=1/2\). Let \(Ue_j=e_{j+1}\) on complex \(\ell^2(\mathbb Z)\). Starting from the strictly positive two-periodic bilateral weighted shift \(We_{2j}=ae_{2j+1}\), \(We_{2j+1}=be_{2j+2}\), iterate the induced mean transform associated with \(M\). On weights this is the precise update
\[
(a,b)\longmapsto \bigl(M(b,a),M(a,b)\bigr),\qquad a,b>0.
\]
Every orbit converges in operator norm to a constant-weight shift \(cU\), with \(c>0\).

Let \(\nu\) be the unique probability measure on \([-1,1]\) obtained by pushing forward the harmonic Kubo–Ando representing measure under \(s\mapsto 2s-1\), and set \(m_j=\int_{-1}^{1}t^j\,d\nu(t)\). The centered condition is exactly \(m_1=0\). There is a complete dichotomy:

* If \(\nu\) is symmetric under \(t\mapsto-t\), then **every orbit reaches constant weights after exactly one update or earlier**.
* Otherwise there is a *smallest odd* integer \(p\ge3\) with \(m_p\ne0\), and the logarithmic contrast \(r=\log(a/b)\) has the sharp local update law
\[
\boxed{\quad r^+=\frac{m_p}{2^{p-1}}r^p+O(r^{p+2}),\qquad r\to0.\quad}
\]
In particular **no even finite superattraction order occurs**. For any orbit not reaching equality at a finite step, its contrast \(e_n=|\log(a_n/b_n)|\) obeys
\[
\lim_{n\to\infty}\frac{e_{n+1}}{e_n^p}=C=\frac{|m_p|}{2^{p-1}}>0,
\qquad
-\log e_n=A p^n+\frac{\log C}{p-1}+o(1)
\]
for a positive \(A\) depending on the initial weights.

**Every odd integer \(p\ge3\) occurs, without finite-step collapse.** More precisely, for any such \(p\) and \(0<\varepsilon<1\), the operator mean with centered representing-measure density
\[
d\nu_{p,\varepsilon}(t)=\frac{1+\varepsilon P_p(t)}{2}\,dt,\quad -1\le t\le1,
\]
where \(P_p\) is the classical Legendre polynomial, has exact order \(p\) and coefficient
\[
\boxed{\quad \lim_{r\to0}\frac{r^+}{r^p}
=\frac{2\varepsilon(p!)^2}{(2p+1)!}.\quad}
\]
For these examples no unequal positive input becomes equal in a finite number of updates.

## Assumptions and scope

The operator mean is a normalized Kubo–Ando mean acting on positive invertible operators, with a unique probability harmonic representing measure \(\mu\) on \([0,1]\). Its scalar restriction is
\[
M(x,y)=\int_0^1\left(\frac{1-s}{x}+\frac{s}{y}\right)^{-1}d\mu(s),\qquad x,y>0.
\]
The measure \(\nu\) is the pushforward of \(\mu\) by \(t=2s-1\). Every mean considered has \(m_1=0\), equivalently \(f'(1)=1/2\). The stated iteration is precisely the induced Aluthge transform of the invertible periodic bilateral weighted shift, not an arbitrary nonlinear map of two numbers. The norm is the bounded-operator norm on \(\ell^2(\mathbb Z)\). The integer \(p\) depends on the mean, not on a nonzero sufficiently small initial contrast. The asymptotic formula for \(e_n\) excludes orbits reaching the diagonal in finitely many steps; all Legendre examples avoid that exception.

## Proof

**1. Exact scalar dynamics from the operator transform.** The absolute value of the two-periodic weighted shift is diagonal with entries \(a,b,a,b,\ldots\), and its polar factor is the bilateral shift \(U\). In the double-operator-integral definition of the induced mean, every nonzero matrix entry of \(U\) is multiplied by the scalar mean of the two neighboring diagonal values. Consequently the induced mean has alternate weights \(M(b,a)\), \(M(a,b)\). This also follows by evaluating its perspective kernel \(P_f(x,y)=xf(y/x)\) on the two diagonal spectral values.

Write \(a=e^{v+r/2}\), \(b=e^{v-r/2}\), and put
\[
u=\tanh(r/2),\qquad H(u)=\int_{-1}^{1}\frac{d\nu(t)}{1-tu}=\sum_{j=0}^{\infty}m_j u^j,\quad |u|<1.
\]
(The first \(u\) is a scalar argument; the symbol \(\nu\) denotes the measure.) The harmonic formula gives the **exact**, nonasymptotic identities
\[
M(b,a)=e^v\operatorname{sech}(r/2)H(u),\qquad
M(a,b)=e^v\operatorname{sech}(r/2)H(-u).
\]
Therefore the updated logarithmic contrast is
\[
\boxed{\quad r^+=\log H(\tanh(r/2))-\log H(-\tanh(r/2)).\quad}
\]
Also \(f'(1)=\int_0^1s\,d\mu(s)=(1+m_1)/2\), so the hypothesis is \(m_1=0\).

**2. Completeness and exact leading coefficient.** The Hausdorff moment problem on the compact interval \([-1,1]\) is determinate. Thus all odd moments of \(\nu\) vanish exactly when \(\nu\) is reflection-symmetric. In that case \(H\) is even and the exact formula gives \(r^+=0\) for every \(r\). Otherwise, since \(m_1=0\), the first nonzero odd moment has index \(p\in\{3,5,7,\ldots\}\). Decompose \(H(u)=E(u)+O(u)\) into its even and odd parts, where \(E(u)=1+O(u^2)\) and \(O(u)=m_pu^p+O(u^{p+2})\). Positivity of \(H\) for real \(|u|<1\) permits logarithms, and
\[
\log\frac{H(u)}{H(-u)}
=\log\frac{E(u)+O(u)}{E(u)-O(u)}
=2m_pu^p+O(u^{p+2}).
\]
Since \(u=r/2+O(r^3)\), this is the claimed coefficient \(m_p/2^{p-1}\), and no even order is possible.

**3. Global convergence and superexponential profile.** Every nontrivial centered Kubo–Ando scalar mean is a strict internal mean: for distinct positive inputs both ordered outputs are strictly between their minimum and maximum. This follows directly from the harmonic integral and \(\int s\,d\mu=1/2\), which excludes a measure supported at just one endpoint. Hence the minimum of each iterated pair is nondecreasing and its maximum is nonincreasing, and both stay in the compact positive initial interval. If the limiting gap were positive, a convergent subsequence and strict internality would contradict convergence of the extrema. Thus both entries approach the same \(c>0\); operator-norm convergence follows because the weights have period two.

For a nonsymmetric mean, along a non-collapsing orbit, local analyticity gives
\[
e_{n+1}=Ce_n^p(1+O(e_n^2)),\quad C=|m_p|/2^{p-1}>0.
\]
Taking logarithms, then telescoping the perturbed affine recursion for \(\log e_n\), shows that \(p^{-n}(\log e_n+\log C/(p-1))\) converges to a negative constant \(-A\). The tail of the telescoping series is \(o(p^{-n})\), since \(e_n\) decays supergeometrically. This yields the asserted asymptotic expansion with \(A>0\).

**4. Exact realization of all possible orders.** For odd \(p\ge3\), the Legendre polynomial satisfies \(|P_p(t)|\le1\) for \(t\in[-1,1]\). Hence \((1+\varepsilon P_p(t))dt/2\) is a strictly positive probability measure. Orthogonality of \(P_p\) to polynomials of degree less than \(p\) gives \(m_1=m_3=\cdots=m_{p-2}=0\). Rodrigues' formula and integration by parts yield
\[
\int_{-1}^1\frac{t^pP_p(t)}2\,dt
=\frac{2^p(p!)^2}{(2p+1)!},
\]
so \(m_p=\varepsilon 2^p(p!)^2/(2p+1)!\ne0\). Thus the local coefficient is exactly the displayed positive constant.

For every odd \(j\ge p\), Rodrigues' formula likewise gives \(\int_{-1}^1t^jP_p(t)\,dt>0\) (the remaining integrand is an even nonnegative power times \((1-t^2)^p\)). Therefore \(H(u)>H(-u)\) for all \(0<u<1\), so no nonzero contrast is ever sent to zero. This proves attainment of every odd order for all unequal starting pairs. The symmetric case is attained, for example, by \(\varepsilon=0\) in the same family.

## Verification

The companion standalone `CHECK.py` independently constructs low-degree Legendre polynomials with rational coefficients, verifies the required vanishing moments and leading coefficients for degrees \(3,5,7,9\), and tests the exact mean-contrast formula numerically via a convergent moment series. The finite tests are diagnostic checks, not a substitute for the measure representation, analyticity, moment determinacy, global contraction, or Rodrigues argument used in the proof. Run with a standard Python 3 interpreter using `python CHECK.py`.

## Relationship to prior work

Kubo–Ando harmonic representation and the symmetry/reflected-measure criterion are classical; the latter is explicit in Pálfia and Petz (2014, Section 2). Yamazaki (2019/2020, Section 5) introduces induced mean iteration and studies its convergence. Osaka and Yamazaki (2024/2025, Definition 1.1 and Theorems 2.3 and 4.4) prove convergence of centered induced iterations; Zhou and Yang (2026, Sections 1 and 3) investigate power-mean transforms and their operator iterates. A separately available sharp nonlinear spectral-rate result for cyclic induced Aluthge means identifies the *zero linear factor* and supergeometric convergence for the centered two-period case but does not imply the **exact first nonzero odd order**, its moment coefficient, or the realization of every odd order. The current statement classifies this degenerate rate entirely, including nonsymmetric operator means and a constructive family of all possibilities. General mean-type iteration results provide convergence frameworks, not the stated moment-stratified hierarchy.

## Limitations

The theorem concerns the centered derivative-one-half regime and two-periodic strictly positive scalar weights. It does not classify noncentered derivatives, higher periods, arbitrary nonperiodic shifts, or noncommuting operator-valued weights. A nonsymmetric mean can possibly send some special unequal input to equality at one step, so the double-exponential asymptotic is explicitly conditioned on the absence of finite collision; the constructed Legendre family is proven collision-free. The moment hierarchy and local coefficient do not determine the limiting constant \(c\). Equivalent claims in the broad literature of nonlinear mean iteration remain a residual publication-priority risk, and no independent proof assessment is asserted.

## References

- J.-B. Zhou and S. Yang, *Power mean transforms of operators*, arXiv:2606.17556v1, first publicly submitted 2026-06-16, especially Sections 1 and 3. https://arxiv.org/abs/2606.17556
- H. Osaka and T. Yamazaki, *Limit of iteration of the induced Aluthge transformations of centered operators*, arXiv:2409.03338v1, first submitted 2024-09-05; Trans. Amer. Math. Soc. 378 (2025), 6857–6884. https://arxiv.org/abs/2409.03338
- T. Yamazaki, *A generalization of the Aluthge transformation in the viewpoint of operator means*, arXiv:1912.08452 (first submitted 2019-12-18), Sections 2 and 5. https://arxiv.org/abs/1912.08452
- M. Pálfia and D. Petz, *Weighted multivariable operator means of positive definite operators*, Linear Algebra Appl. 463 (2014), 134–153, Section 2. https://doi.org/10.1016/j.laa.2014.08.025
- J. Matkowski and P. Pasteczka, *Mean-type mappings and invariance principle*, arXiv:2005.10623 (2020). https://arxiv.org/abs/2005.10623
- *A universal sharp nonlinear spectral rate for cyclic induced Aluthge means*, publicly available research note (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-universal-sharp-nonlinear-spectral-rate-for-cyclic-induced-alu--dc4b3a63342a
