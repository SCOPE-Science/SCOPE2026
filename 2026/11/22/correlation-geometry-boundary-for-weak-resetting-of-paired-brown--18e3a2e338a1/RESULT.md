# Correlation–geometry boundary for weak resetting of paired Brownian searchers

## Finding

Let two particles search for an absorbing target at the origin, with initial distances \(x,y>0\), common diffusion coefficient \(D>0\), and instantaneous noise correlation \(-1<\rho<1\). A single Poisson clock of rate \(r\geq0\) simultaneously returns both particles to their respective initial positions; the search ends on the first target hit. Let \(M(r)\) denote the mean completion time. Put \(U=x/y+y/x\geq2\).

**Sharp local resetting phase diagram.** For \(\rho\geq0\), \(M(0)=\infty\) while \(M(r)<\infty\) for every \(r>0\). For \(\rho<0\), put \(c=-\rho\in(0,1)\) and
\[
 c_*(U)=\frac{U+\sqrt{U^2+216}}{18}.
\]
If \(c<c_*(U)\), there exists \(\varepsilon>0\) such that \(M(r)<M(0)\) for all \(0<r<\varepsilon\). If \(c>c_*(U)\), the reverse strict inequality holds for all sufficiently small positive \(r\). Equality \(c=c_*(U)\) is physically possible precisely when \(2\leq U<3\); then the linear response vanishes, but \(M(r)>M(0)\) for all sufficiently small \(r>0\), with an explicitly positive quadratic coefficient. Therefore, when \(U\geq3\), arbitrarily weak resetting is beneficial for **every** intrinsic noise correlation \(-1<\rho<1\).

For equally distant particles (\(x=y\)), the critical negative correlation is
\[
 \rho_*=-\frac{1+\sqrt{55}}9=-0.935133165232851\ldots.
\]
Consequently, when \(\rho<\rho_*\), weak resetting increases the mean completion time; when \(\rho_*<\rho<0\), weak resetting decreases it. At \(\rho=\rho_*\), weak resetting increases the mean at quadratic order. The complete claim is **local at \(r=0\)** and does not assert global optimality over all reset rates.

## Assumptions and scope

Between resets the positions satisfy \(X_1(t)=x+\sqrt{2D}\,B_1(t)\), \(X_2(t)=y+\sqrt{2D}\,B_2(t)\), where each \(B_i\) is standard Brownian motion and \(\langle B_1,B_2\rangle_t=\rho t\). The first coordinate that reaches zero terminates the search, so the unreset completion time is \(T=\inf\{t\geq0:X_1(t)X_2(t)=0\}\). Each reset restarts **both** coordinates and all future Brownian driving independently of prior excursions. The pair's intrinsic noise correlation \(\rho\) persists within each new excursion; it is not the correlation arising solely from a shared reset clock. Reset events take no time. The domain is \(x,y,D>0\), \(-1<\rho<1\), and \(r\geq0\). No claim is made about non-Poisson clocks, imperfect absorption, motion after an individual target hit, or reset costs.

## Proof

**1. Wedge tail and moment domains.** The unreset generator on the positive quadrant is
\[
 \mathcal L=D(\partial_{xx}+\partial_{yy}+2\rho\partial_{xy}).
\]
For \(-1<\rho<1\), whitening the covariance maps the positive quadrant into a planar wedge of opening \(\alpha=\arccos(-\rho)\) and keeps its two edges absorbing. The classical wedge survival expansion has \(\Pr(T>t)\sim C(x,y,\rho,D)t^{-\pi/(2\alpha)}\) with a strictly positive constant. Thus \(\mathbb E T^k<\infty\) exactly when \(k<\pi/(2\alpha)\). In particular, \(\mathbb ET<\infty\) iff \(\rho<0\). For \(\rho=-c<0\), \(\mathbb ET^2<\infty\) exactly when \(c>1/\sqrt2\), and \(\mathbb ET^3<\infty\) exactly when \(c>\sqrt3/2\). At either equality the corresponding moment diverges logarithmically.

**2. Exact quadrant exit moments.** When finite, the moments \(m_k(x,y)=\mathbb ET^k\) solve \(\mathcal Lm_k=-k m_{k-1}\), \(m_0=1\), with absorbing boundary values zero. Direct polynomial differentiation, followed by the wedge tail bound to remove stopped-process remainders, gives
\[
 m_1=\frac{xy}{2Dc}\qquad (0<c<1),
\]
\[
 m_2=\frac{xy\bigl(x^2+y^2+3cxy\bigr)}{12D^2c(2c^2-1)}\qquad (c>1/\sqrt2),
\]
and
\[
 m_3=\frac{(xy)^3(3U^2+15cU+20c^2-1)}{120D^3c(2c^2-1)(4c^2-3)}\qquad(c>\sqrt3/2).
\]
All three are symmetric in \(x,y\), vanish on either absorbing axis, and satisfy their respective elliptic moment recurrences. In the finite-moment regime the killed wedge process justifies these solutions uniquely as expectations (rather than merely formal polynomial solutions).

**3. Reset renewal and the critical curve.** With \(S(t)=\Pr(T>t)\), define \(A(r)=\int_0^\infty e^{-rt}S(t)\,dt\). Renewal at the first reset yields
\[
 M(r)=\frac{A(r)}{1-rA(r)}\quad(r>0).
\]
The denominator equals \(\mathbb E e^{-rT}>0\). If \(m_2<\infty\), expanding at zero yields
\[
 M(r)=m_1+r(m_1^2-\tfrac12m_2)+o(r).
\]
An exact factorization gives
\[
 m_2-2m_1^2=
 \frac{xy\left[c(x^2+y^2)+(6-9c^2)xy\right]}{12D^2c^2(2c^2-1)}.
\]
Hence the sign of the zero-rate derivative of \(M\) is the **opposite** of the sign of \(cU+6-9c^2\). For \(U\geq2\), the unique positive root of that quadratic is \(c_*(U)\). It increases with \(U\), satisfies \(c_*(2)=(1+\sqrt{55})/9>1/\sqrt2\), and crosses \(1\) exactly when \(U=3\). Thus the finite-second-moment regime has the stated phase diagram.

If \(0<c\leq1/\sqrt2\), \(m_1<\infty\) but \(m_2=\infty\). Monotone convergence yields \((A(r)-m_1)/r\to-\infty\), whereas \(M(r)-A(r)=O(r)\). Consequently \((M(r)-m_1)/r\to-\infty\), so arbitrarily weak resetting is beneficial there as well. When \(\rho\geq0\), the infinite unreset mean follows from Step 1 and \(A(r)<1/r\) gives a finite restarted mean for every \(r>0\).

**4. Strict quadratic response at the critical boundary.** A physical equality \(c=c_*(U)\) requires \(2\leq U<3\), so \(c\in[(1+\sqrt{55})/9,1)\subset(\sqrt3/2,1)\) and \(m_3\) exists. The second-order expansion is
\[
 M(r)=m_1+r(m_1^2-\tfrac12m_2)
 +r^2(\tfrac16m_3-m_1m_2+m_1^3)+o(r^2).
\]
On the critical curve \(U=9c-6/c\) and \(m_2=2m_1^2\). Substitution of Step 2 yields
\[
 M(r)-M(0)=\frac{(xy)^3}{D^3}\frac{162-161c^2}{720c^3(4c^2-3)}\,r^2+o(r^2).
\]
Both numerator and denominator are strictly positive for this physical critical interval. This proves that even the equality curve is locally unfavorable to positive resetting. Finally, \(U\geq3\) corresponds to a starting-distance ratio outside the open interval between \((3-\sqrt5)/2\) and \((3+\sqrt5)/2\); in that geometry, \(c<c_*(U)\) for all \(c<1\). The stated classification follows.

## Verification

The standalone `checker.py` uses exact symbolic differentiation to test all three moment PDEs and their absorbing boundary values, factors the response coefficient, checks the second-order critical identity, and verifies rational parameter signs. As an independent limiting check, at perfect anticorrelation \(\rho=-1\) the motion reduces to a one-dimensional Brownian exit from the interval \((-y,x)\). Its exact Laplace transform is
\[
 \mathbb E e^{-rT}=\frac{\cosh\bigl(\sqrt{r/D}(x-y)/2\bigr)}{\cosh\bigl(\sqrt{r/D}(x+y)/2\bigr)},
\]
whose restarted-mean expansion agrees with the \(c\uparrow1\) limits of the first three moment coefficients. This limit serves only as a check; the theorem's strict stochastic-noise domain is \(-1<\rho<1\). Running `python checker.py` produced 27 passed exact checks. The wedge tail and moment finiteness are analytic inputs, not inferred from finite tests.

## Relationship to prior work

Biroli, Majumdar and Schehr (arXiv:2303.18012, first posted 2023-03-31) analyze independent Brownian searchers and compare independent with synchronous Poisson resetting; their synchronous protocol has zero intrinsic noise correlation before reset. The present claim changes the *pre-reset joint diffusion generator* and classifies its weak-reset improvement in the two parameters \(\rho\) and \(x/y\), including the quadratic equality boundary. Chupeau, Bénichou and Majumdar (arXiv:1501.02274, 2015) supply the known planar-wedge first-passage geometry and survival exponent; their paper does not introduce resetting. Pal and Reuveni (arXiv:1607.06048, 2016) give general renewal theory for restart; the renewal identity here is credited, not claimed as new. The contribution assessed here is the explicit sharp physical phase diagram and critical tangency computed from the correlated quadrant moments. A general restart theorem plus known wedge results may implicitly cover parts of this calculation; independent literature review remains necessary.

## Limitations

The boundary describes only sufficiently weak Poisson resetting. It neither proves uniqueness of an optimal positive reset rate nor rules out improvement at an intermediate rate when weak resetting is detrimental. No finite-time search reliability, finite-sample inference, or energetic cost is assessed. Wedge moment identities are exact; the numerical parameter tests are supplementary rather than proof of all parameter values. Publication priority is subject to comparison with other treatments of correlated quadrant hitting times, particularly implicit moment formulas not located in the inspected sources. Independent validation has not been performed.

## References

1. M. Biroli, S. N. Majumdar and G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012 (v1 submitted 2023-03-31), Phys. Rev. E 107, 064141 (2023). https://arxiv.org/abs/2303.18012
2. M. Chupeau, O. Bénichou and S. N. Majumdar, *Survival probability of a Brownian motion in a planar wedge of arbitrary angle*, arXiv:1501.02274 (2015), Phys. Rev. E 91, 032106. https://arxiv.org/abs/1501.02274
3. A. Pal and S. Reuveni, *First Passage Under Restart*, arXiv:1607.06048 (v1 submitted 2016-07-20), Phys. Rev. Lett. 118, 030603 (2017). https://arxiv.org/abs/1607.06048
