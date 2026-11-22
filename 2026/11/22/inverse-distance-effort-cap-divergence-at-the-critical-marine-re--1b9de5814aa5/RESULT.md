# Inverse-distance effort-cap divergence at the critical marine-reserve fraction

## Finding

Consider the deterministic seasonal two-patch fishery defined below. There is an exact critical protected-area fraction \(R_c\in(0,1)\), above which **every finite constant harvesting effort is sustainable** in the sense of a strictly positive globally attracting yearly biomass, whereas each \(0<R<R_c\) has a unique finite maximum sustainable effort \(E_*(R)\). More precisely, as the protected fraction increases toward \(R_c\) from below,

\[
\boxed{\lim_{R\uparrow R_c}(R_c-R)E_*(R)=\frac{mR_c(1-R_c)(2+mR_cT)}{q(1+mR_cT)}.}
\]

The exact threshold fraction is characterized by

\[
\boxed{rR_c\,e^{-[c+m(1-R_c)]T}=1,\qquad R_c=\frac{W_0\!\left(mT e^{(c+m)T}/r\right)}{mT},}
\]

where \(W_0\) denotes the principal real Lambert \(W\) function. This last threshold equation follows from the known infinite-effort limit; the research contribution is the rigorous **sharp inverse-distance divergence**, including its nonzero exact coefficient and the finite-effort trichotomy at the threshold. The divergence holds for every fixed parameter choice in the specified domain, without any numerical fitting.

## Assumptions and scope

Fix \(c,m,q,\beta>0\), \(0<T\le1\), and \(r>e^{cT}\). The protected habitat occupies a fraction \(R\in(0,1)\); the harvested habitat occupies \(1-R\). Effort \(E\ge0\) is constant within and between fishing seasons. Initial total stock is strictly positive. The within-season patch biomasses obey

\[
\frac{d}{dt}\begin{pmatrix}x_1\\x_2\end{pmatrix}=A(E,R)\begin{pmatrix}x_1\\x_2\end{pmatrix},\qquad
A(E,R)=\begin{pmatrix}-c-qE-mR&m(1-R)\\mR&-c-m(1-R)\end{pmatrix}.
\]

Each season starts with the fractions \((1-R,R)\) of the Beverton–Holt recruits. Write

\[
F(E,R)=(1,1)e^{T A(E,R)}(1-R,R)^\mathsf{T}.
\]

Then the yearly total biomass \(N_n\) follows

\[
N_{n+1}=\frac{rF(E,R)N_n}{1+\beta N_n}.
\]

By *sustainable* we mean that every positive yearly initial stock converges to a **strictly positive** fixed point. Thus the boundary \(rF=1\) is not sustainable: every positive trajectory eventually goes to zero there. \(E_*(R)\) is the threshold where \(rF=1\); sustainability for \(R<R_c\) holds exactly when \(0\le E<E_*(R)\).

The constant \(q\) merely converts harvesting effort into an instantaneous mortality rate. There is no finite exogenous equipment limit on \(E\); “all finite efforts” does not claim a mathematically admissible infinite effort.

## Proof

**1. Exact survival representation.** Put \(h=qE\), \(d(R)=c+m(1-R)\), and

\[
D(h,R)=\sqrt{(h-m)^2+4mhR},\qquad
w(h,R)=\frac12\left(1+\frac{m+h(2R-1)}{D(h,R)}\right).
\]

For every \(h\ge0\) and \(0<R<1\), \(D>0\). The matrix eigenvalues are

\[
\ell_+(h,R)=-c-\frac{h+m-D}{2},\qquad
\ell_-(h,R)=-c-\frac{h+m+D}{2}.
\]

The two spectral projectors, paired with the initial distribution and terminal total-mass functional, give the exact real identity

\[
\boxed{F(E,R)=w(h,R)e^{T\ell_+(h,R)}+[1-w(h,R)]e^{T\ell_-(h,R)}.}\tag{1}
\]

This identity follows directly from the projector \((A-\ell_-I)/(\ell_+-\ell_-)\), not from a numerical diagonalization. It also remains regular at \(E=0\), where \(F(0,R)=e^{-cT}\).

**2. Strict loss under harvesting.** Let \(H=\operatorname{diag}(1,0)\) and \(v=(1-R,R)^\mathsf{T}\). Since \(A(h,R)\) has positive off-diagonal entries and \(v\) is strictly positive, the integral identity

\[
\frac{\partial F}{\partial h}=-\int_0^T(1,1)e^{(T-t)A}H e^{tA}v\,dt<0
\]

holds for all finite \(h\ge0\). The sign is strict because every factor of the scalar integrand is positive for \(0<t<T\). Thus \(F\) decreases strictly with effort. The no-effort value \(re^{-cT}>1\) is sustainable by assumption.

**3. Uniform high-effort expansion.** For \(R\) in any compact subinterval of \((0,1)\), binomial expansion of \(D\) in (1) gives, uniformly in \(R\),

\[
\begin{aligned}
D&=h+m(2R-1)+\frac{2m^2R(1-R)}h+O(h^{-2}),\\
\ell_+&=-d(R)+\frac{m^2R(1-R)}h+O(h^{-2}),\\
w&=R+\frac{2mR(1-R)}h+O(h^{-2}).
\end{aligned}
\]

The fast contribution is \(O(e^{-hT/2})\) for all sufficiently large \(h\) in such a compact interval. Consequently,

\[
\boxed{F(E,R)=f(R)+\frac{C(R)}{qE}+O(E^{-2}),}\tag{2}
\]

where

\[
 f(R)=R e^{-[c+m(1-R)]T},\qquad
 C(R)=mR(1-R)(2+mRT)e^{-[c+m(1-R)]T}>0.
\]

The error in (2) is uniform for \(R\) near the interior value \(R_c\). In particular the limit of \(F\) as \(E\to\infty\) is exactly \(f(R)\).

**4. Existence and uniqueness of the cutoff.** The function \(f\) satisfies

\[
f(0)=0,\quad f(1)=e^{-cT}>1/r,\quad f'(R)=e^{-[c+m(1-R)]T}(1+mTR)>0.
\]

It therefore crosses \(1/r\) at a unique \(R_c\in(0,1)\). Rearranging the defining equation gives the stated Lambert \(W_0\) formula. If \(R<R_c\), the strictly decreasing continuous function \(F(E,R)\) starts above \(1/r\) and tends below \(1/r\), hence crosses it at one finite \(E_*(R)>0\). If \(R\ge R_c\), strict monotonicity and its finite high-effort limit give \(F(E,R)> f(R)\ge1/r\) for every finite effort. The Beverton–Holt recurrence proves the asserted sustainability alternatives.

**5. Sharp singular approach.** Suppose \(R\uparrow R_c\) from below. Necessarily \(E_*(R)\to\infty\): otherwise continuity would produce a finite effort with \(F(E,R_c)=1/r\), contradicting step 4. At \(E=E_*(R)\), uniform expansion (2) and Taylor expansion around \(R_c\) yield

\[
\frac1r-f(R)=\frac{C(R)}{qE_*(R)}+O(E_*(R)^{-2})
=f'(R_c)(R_c-R)+O((R_c-R)^2).
\]

Multiplying the first equality by \(qE_*(R)\), and using its divergence together with positivity of \(C(R_c)\) and \(f'(R_c)\), gives

\[
\lim_{R\uparrow R_c}(R_c-R)E_*(R)
=\frac{C(R_c)}{q f'(R_c)}
=\frac{mR_c(1-R_c)(2+mR_cT)}{q(1+mR_cT)}.
\]

This proves the claimed coefficient and exponent. The scale does not depend on \(\beta\), because \(\beta\) changes equilibrium abundance but not the positivity threshold.

## Verification

The included standard-library program `verify.py` implements (1), a separate Taylor-series computation of the matrix exponential, the strict-threshold root, and the constant in the boxed limit. Executing `python3 verify.py` produced `PASS: 435 supplementary exact-formula, matrix-series, and asymptotic checks`.

As a reproducible example, take \(c=m=1\), \(q=0.7\), \(r=2\), \(T=0.5\). Then \(R_c\approx0.876756832620\) and the inverse-distance coefficient is \(0.261680835745\). At distances \(0.02\), \(0.005\), and \(0.001\) below \(R_c\), the corresponding cutoffs are approximately \(13.735591\), \(52.636419\), and \(261.983722\), respectively; their products with the distances approach the proved constant. These numerical checks corroborate but do not establish the infinite-parameter theorem.

## Relationship to prior work

The originating 2026 fishery model already states the exact matrix exponential, the persistence criterion \(rF>1\), and the infinite-harvest reserve condition \(rf(R)>1\). Its Table 1 and bifurcation discussion motivate the horizontal high-effort asymptote. Those facts are not presented as new. The contribution here is the **uniform joint-limit analysis** in which \(R\uparrow R_c\) and the finite effort cutoff diverges, including the explicit first-order survival coefficient and exact inverse-distance constant.

Doyen and Béné (2003) prove a reserve-area viability threshold for a different single-stock uncertain-harvest map; their threshold does not involve the two-patch finite-rate dispersal matrix or the present effort-gap singularity. Earlier marine-reserve models also discuss high-fishing spillover without this exact seasonal limit. The historical priority assessment is literature-bounded and not independently certified.

## Limitations

This is a deterministic constant-effort, fixed-season, two-patch result with homogeneous mortality and fixed-rate mixing. It does not cover adaptive harvesting, finite equipment limits, time-varying catchability, environmental stochasticity, or empirical fishery management outcomes. At the boundary \(rF=1\), the yearly stock still becomes extinct asymptotically (it does not instantly vanish). The result is an asymptotic description near a protected fraction that may exceed practical reserve sizes. No independent scientific audit has been performed.

## References

1. D. Kumar, *Sustainable and Optimal Harvesting in a Seasonally Harvested Fishery with a Marine Protected Area: A Two-Patch Model with Bang-Bang and Singular Control*, arXiv:2601.20563v1, first public 2026-01-28. https://arxiv.org/html/2601.20563v1
2. L. Doyen and C. Béné, *Sustainability of fisheries through marine reserves: a robust modeling analysis*, Journal of Environmental Management 69 (2003), 1–13. https://doi.org/10.1016/S0301-4797(03)00004-5
3. J. Boncoeur et al., *Fish, fishers, seals and tourists: Economic consequences of creating a marine reserve in a multi-species, multi-activity context*, Natural Resource Modeling 15 (2002), 387–411. https://doi.org/10.1111/j.1939-7445.2002.tb00095.x
