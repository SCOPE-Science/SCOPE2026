# Sharp bilateral-front synchronization and a four-particle sign reversal in a reset Brownian gas

## Finding
Fix an integer \(N\ge 2\), diffusivity \(D>0\), and a common Poisson resetting rate \(r>0\). Between reset events, \(N\) particles move as independent Brownian motions with generator \(D\partial_{xx}\); every common reset replaces **all** positions by zero. Observe the unique stationary state. Define the rightward and leftward extremal extents
\[
R_N=\max_{1\le i\le N}X_i,\qquad L_N=-\min_{1\le i\le N}X_i,
\]
and their Pearson correlation \(\rho_N=\operatorname{Corr}(R_N,L_N)\). The extents are signed: for a finite sample, either may occasionally be negative. The correlation is well-defined, independent of \(D\) and \(r\), and has an exact finite-population sign reversal:
\[
\boxed{\rho_2=-\frac13,\qquad
\rho_3=\frac{\sqrt3/\pi-9/16}{7/16+\sqrt3/(2\pi)}<0,\qquad
\rho_4>0.}
\]
In particular, four is the **smallest** population with positive opposite-front correlation. For four particles there is a fully explicit exact value. Put
\[
m_4=\frac{3}{2\sqrt\pi}+\frac{3}{\pi\sqrt\pi}\arcsin\frac13;
\qquad
\rho_4=\frac{3/\pi-\pi m_4^2/4}
{1+\sqrt3/\pi-\pi m_4^2/4}\approx 0.1706428647167904.
\]
More importantly, the two opposite fronts become almost perfectly synchronized at a **sharp logarithm-squared rate**:
\[
\boxed{\lim_{N\to\infty}(\log N)^2(1-\rho_N)
=\frac{\pi^2}{6(4-\pi)}\approx1.9162628019520258.}
\]
Equivalently, the actual leftmost *position* \(\min_iX_i=-L_N\) has Pearson correlation tending to \(-1\) with the rightmost position, with the same absolute deviation. This quantitative correlation deficit is distinct from the previously known one-front extreme-value law and from correlations between adjacent edge gaps.

## Assumptions and scope
All Brownian drivers are independent of each other and of the common resetting clock; there are no particle interactions between reset events, drifts, finite boundaries, or additional reset mechanisms. Brownian diffusivity means \(\mathbb E[(X_i(t)-X_i(0))^2]=2Dt\) between resets. A *stationary observation* samples a generic time, not a reset instant. The backward recurrence time \(A\) is exactly \(\operatorname{Exp}(r)\). Consequently there is the exact distributional representation
\[
(X_1,\ldots,X_N)\stackrel d=\sqrt{2DA}\,(Z_1,\ldots,Z_N),
\quad Z_i\stackrel{\rm iid}{\sim}\mathcal N(0,1),\quad A\perp(Z_i)_{i=1}^N.
\]
Let \(U_N=\max_iZ_i\), \(V_N=-\min_iZ_i\), \(m_N=\mathbb E U_N=\mathbb E V_N\), \(v_N=\operatorname{Var}U_N\), and \(c_N=\operatorname{Cov}(U_N,V_N)\). All these moments are finite. Although \(U_N\) and \(V_N\) are dependent at every finite \(N\), their properly centered and scaled fluctuations become independent in the Gaussian extreme-value limit.

## Proof
**1. Exact common-age covariance identity.** Set \(S=\sqrt{2DA}\), independent of \((U_N,V_N)\). The exponential age yields \(\mathbb E S^2=2D/r\) and \((\mathbb E S)^2=(2D/r)(\pi/4)\). Write \(k=1-\pi/4>0\). Applying the law of total covariance and variance to \(R_N=SU_N\), \(L_N=SV_N\), we obtain the exact identity
\[
\boxed{\rho_N=\frac{c_N+k m_N^2}{v_N+k m_N^2},\qquad
1-\rho_N=\frac{v_N-c_N}{v_N+k m_N^2}.}\tag{1}
\]
This proves independence from the diffusivity and reset rate without approximations. Since \(R_N-L_N= S(U_N-V_N)\) is not almost surely constant, \(\rho_N<1\) for finite \(N\).

**2. Exact two-, three-, and four-particle sign data.** Let \(\phi\), \(\Phi\) be the standard normal density and CDF. Integration by parts in the density \(N\phi(z)\Phi(z)^{N-1}\) of \(U_N\) gives
\[
m_N=N(N-1)\int_{\mathbb R}\phi(z)^2\Phi(z)^{N-2}\,dz,
\]
\[
\mathbb E U_N^2=1+N(N-1)
\int_{\mathbb R}z\phi(z)^2\Phi(z)^{N-2}\,dz.
\]
The joint density of the minimum \(a\) and maximum \(b\) of the Gaussian sample, for \(a<b\), is
\(N(N-1)\phi(a)\phi(b)[\Phi(b)-\Phi(a)]^{N-2}\). Thus
\[
\mathbb E(U_NV_N)=-N(N-1)
\int_{a<b}ab\phi(a)\phi(b)
[\Phi(b)-\Phi(a)]^{N-2}\,da\,db.\tag{2}
\]
For \(N=2\), symmetry yields \(m_2=1/\sqrt\pi\), \(\mathbb E U_2^2=1\), and \(U_2V_2=-Z_1Z_2\), so \(\mathbb E U_2V_2=0\). Substitution in (1) gives \(\rho_2=-1/3\).

For \(N=3\), elementary Gaussian integration gives
\[
m_3=\frac3{2\sqrt\pi},\quad
\mathbb E U_3^2=1+\frac{\sqrt3}{2\pi},\quad
\mathbb E(U_3V_3)=\frac{\sqrt3}{\pi}.
\]
For the last identity, integrate the \(b\) integral in (2) by parts, then its remaining \(a\) integral by parts; the result is \(6\int\phi(z)^3\,dz=\sqrt3/\pi\). Inserting these identities in (1) gives the displayed \(\rho_3\); it is negative because \(16\sqrt3<9\pi\).

For \(N=4\), the same twice-integrated expression (2) reduces to
\(\mathbb E(U_4V_4)=12(\int\phi(z)^2\,dz)^2=3/\pi\), and the second-moment integral gives \(\mathbb E U_4^2=1+\sqrt3/\pi\). The mean integral reduces to
\[
m_4=12\int\phi(z)^2\Phi(z)^2\,dz.
\]
Normalize \(\phi^2\) to a normal density of variance \(1/2\). The resulting \(\mathbb E[\Phi(Y)^2]\), for \(Y\sim\mathcal N(0,1/2)\), is the positive-orthant probability of a centered bivariate normal vector with correlation \(1/3\). The identity \(\Pr(W_1>0,W_2>0)=1/4+(2\pi)^{-1}\arcsin(\operatorname{Corr}(W_1,W_2))\) follows by differentiating the bivariate Gaussian probability with respect to its correlation and using the value \(1/4\) at zero correlation. This yields the stated \(m_4\). Then (1) gives the stated \(\rho_4\). Strict positivity follows, for example, from \(\arcsin(1/3)<7/20\) and \(3.14<\pi<22/7\), which imply \(m_4<21/20\) and \(3/\pi-(\pi/4)m_4^2>0\). The arcsine bound follows from \(\sin(7/20)\ge7/20-(7/20)^3/6>1/3\). Hence populations \(2\) and \(3\) are negatively correlated whereas population \(4\) is positively correlated; among populations \(N\ge2\), four is the first positive case.

**3. Asymptotically independent opposite Gaussian edges with moment control.** For \(N\ge3\), write \(b_N=\Phi^{-1}(1-1/N)>0\) and
\[
W_N=b_N(U_N-b_N),\qquad H_N=b_N(V_N-b_N).
\]
For any fixed real \(x,y\), the exact bivariate CDF is
\[
\Pr(W_N\le x,H_N\le y)=
\left[1-\overline\Phi(b_N+x/b_N)-
\overline\Phi(b_N+y/b_N)\right]_+^{N},\tag{3}
\]
where \(\overline\Phi=1-\Phi\). The Gaussian Mills ratio gives \(N\overline\Phi(b_N+x/b_N)\to e^{-x}\); hence (3) converges to \(\exp(-e^{-x}-e^{-y})\), the product of two standard Gumbel CDFs.

Moment convergence is needed here, not just distributional convergence. For \(u\ge0\), the normal-tail hazard bound yields \(\Pr(W_N>u)\le e^{-u}\). For \(0\le u\le b_N^2/2\), the same hazard bound gives
\(\Pr(W_N<-u)\le\exp[-e^{3u/4}]\). For \(b_N^2/2<u\le b_N^2\), it is at most \(\exp[-N\overline\Phi(b_N/2)]\), which is super-polynomially small in \(N\). For \(u>b_N^2\), use \(\overline\Phi(t)\le\frac12e^{-t^2/2}\) for \(t\ge0\), giving the integrable bound
\(2^{-N}\exp[-N(u-b_N^2)^2/(2b_N^2)]\). Integrating these bounds against \(u^3\) shows that \(W_N\) has uniformly bounded fourth moments for all sufficiently large \(N\); symmetry gives the same bound for \(H_N\). Thus the joint second moments converge. If \(G_1,G_2\) are independent standard Gumbels, then
\[
\operatorname{Var}(W_N)\to\operatorname{Var}(G_1)=\frac{\pi^2}{6},
\qquad\operatorname{Cov}(W_N,H_N)\to0.
\]
It follows that
\[
v_N=\frac{\pi^2/6+o(1)}{b_N^2},\quad
c_N=o(b_N^{-2}),\quad
m_N=b_N+O(b_N^{-1}).\tag{4}
\]
The classic normal-maximum quantile asymptotic is \(b_N^2\sim2\log N\), again by Mills' ratio.

**4. Sharp correlation deficit.** Substitution of (4) into the *exact* identity (1) gives
\[
1-\rho_N=\frac{\pi^2/6+o(1)}{k\,b_N^4}
=\frac{\pi^2+o(1)}{24k(\log N)^2}
=\frac{\pi^2+o(1)}{6(4-\pi)(\log N)^2}.
\]
This proves the limiting constant. In particular \(\rho_N>0\) for every sufficiently large \(N\); no monotonicity in \(N\) or assertion that all \(N\ge4\) are positive is required or claimed.

## Verification
Run `python checker.py` with Python 3, NumPy and SciPy. The deterministic checker passed 28 comparisons. It evaluates the maximum's first two moments from independent one-dimensional Gaussian-tail integrals, and the opposite-edge Gaussian covariance from the two-dimensional Hoeffding CDF identity
\[
c_N=\int_{\mathbb R^2}\Big(
[\Phi(x)+\Phi(y)-1]_+^N-\Phi(x)^N\Phi(y)^N
\Big)\,dx\,dy.
\]
This identity is convergent because Gaussian maxima have finite second moments. The code cross-checks the exact \(N=2,3,4\) moments and signs, computes representative larger-system correlations, checks the parameter-free reset-age scale ratio, and tracks convergence of \(b_N^2v_N\) toward \(\pi^2/6\). All asymptotic statements and the finite-size signs follow from the preceding analytic proof, not from finite quadrature or simulations. The quadrature is truncated to a stated window and is not a certificate of the infinite-\(N\) result.

## Relationship to prior work
Biroli, Larralde, Majumdar and Schehr, arXiv:2211.00563, establish the simultaneous-reset stationary Gaussian-age mixture, the distribution of a *single* ordered position and adjacent spacings, including its supplementary material. Biroli, Larralde, Majumdar and Schehr, arXiv:2307.15351, systematize the conditionally independent Gaussian-mixture construction and the marginal order-statistic/extreme distributions. De Mauro, Biroli, Majumdar and Schehr, arXiv:2509.06658, extend the framework to general renewal clocks, including individual extreme distributions and single-gap statistics. Those works are indispensable premises, not newly claimed. The present contribution isolates a **joint opposite-front observable** and derives its exact smallest positive-population case and second-order Pearson correlation deficit, which do not follow merely from either individual extreme marginal or from adjacent-gap correlations. In addition, the published result *Sharp stationary edge-gap correlation envelope under common renewal resetting* analyzes the correlations of two distinct **adjacent gaps**, while *An opposing-tail covariance transition in a synchronously reset Brownian gas* analyzes **counts above fixed opposite thresholds**. Neither establishes the covariance of the two opposite sample extrema or its \((\log N)^{-2}\) coefficient. A direct derivation from the already-known entire stationary joint law is of course possible, and this dependency is acknowledged.

## Limitations
The theorem applies only to a stationary unconfined Brownian gas under **one common Poisson clock** and a fixed positive diffusion coefficient. It makes no finite-population monotonicity assertion, no claim for independent or partial resetting, no first-passage-time claim, and no claim for heavy-tailed renewal ages. The quadrature checks are finite and cannot replace the Gaussian-extreme moment-limit proof. As with other derived observables of an exactly known joint law, an unindexed equivalent extremal-correlation computation could affect publication priority; an independent scientific audit has not been performed.

## References
1. M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Extreme statistics and spacing distribution in a Brownian gas correlated by resetting*, arXiv:2211.00563, initially public 2022-11-01, https://arxiv.org/abs/2211.00563 .
2. M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated system*, arXiv:2307.15351, initially public 2023-07-28, https://arxiv.org/abs/2307.15351 .
3. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, initially public 2025-09-08, https://arxiv.org/abs/2509.06658 .
4. *Sharp stationary edge-gap correlation envelope under common renewal resetting*, published-finding corpus published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-stationary-edge-gap-correlation-envelope-under-common-rene--34ec84bb2b61 .
5. *An opposing-tail covariance transition in a synchronously reset Brownian gas*, published-finding corpus published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-opposing-tail-covariance-transition-in-a-synchronously-reset--e48faf832997 .
