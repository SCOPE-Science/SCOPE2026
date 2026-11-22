# A unique sixth-cumulant crossing and strict eighth-order separation of covariance-matched random diffusivities

## Finding
Two different stationary random-diffusivity mechanisms—squared Ornstein–Uhlenbeck fluctuations and a positive two-state switching environment—can have **identical mean diffusivity, identical entire diffusivity covariance, and identical joint tracer moments of every total degree at most four at arbitrary observation times**. Their sixth tracer cumulants exhibit precisely one diffusivity-contrast crossing. At that crossing their **entire families of joint tracer moments through degree six** coincide, but their eighth tracer cumulants differ strictly at every positive time.

Fix \(m,q>0\). Let \(Y\) be stationary Ornstein–Uhlenbeck with
\[
 dY_t=-\tfrac q2Y_t\,dt+\sqrt{qm}\,dB_t,
 \qquad Y_0\sim\mathcal N(0,m),
 \qquad D_t^{\mathrm G}=Y_t^2.
\]
For \(0<u<1\), let \(S_t\) be a stationary two-state Markov chain. Its low and high diffusivities, its high-state probability, and its jump rates are respectively
\[
 d_-=m(1-u),\qquad d_+=m(1+2/u),\qquad
 p_+=\frac{u^2}{u^2+2},
\]
\[
 k_{-+}=q\frac{u^2}{u^2+2},\qquad
 k_{+-}=q\frac{2}{u^2+2},\qquad D_t^{\mathrm T}=d_{S_t}.
\]
For each environment \(i\in\{\mathrm G,\mathrm T\}\), define an independently Brownian-driven tracer by
\[
 X_t^i=\int_0^t\sqrt{2D_s^i}\,dW_s^i,\qquad X_0^i=0,
\]
where its Brownian driver is independent of the entire diffusivity environment. Both environments are initialized in their invariant laws. Then, for all \(s,t\ge0\),
\[
 \mathbb E D_t^{\mathrm G}=\mathbb E D_t^{\mathrm T}=m,\qquad
 \operatorname{Cov}(D_s^{\mathrm G},D_t^{\mathrm G})
 =\operatorname{Cov}(D_s^{\mathrm T},D_t^{\mathrm T})=2m^2e^{-q|t-s|}.
\]
In particular, all multi-time tracer joint moments through total degree four coincide, and for each \(t>0\),
\[
 \kappa_2(X_t^i)=2mt,\qquad
 \kappa_4(X_t^i)=\frac{48m^2}{q^2}\bigl(qt-1+e^{-qt}\bigr).
\]
Writing
\[
 J_q(t)=\frac{qt-2+(qt+2)e^{-qt}}{q^3}
 =\int_0^t (t-h)h e^{-qh}\,dh>0,
\]
the sixth cumulants are exactly
\[
 \boxed{\ \kappa_6(X_t^{\mathrm G})=5760m^3J_q(t),\qquad
 \kappa_6(X_t^{\mathrm T})=1440m^3(2/u-u)J_q(t).\ }
\]
Consequently, independently of the physical time and relaxation rate, the **unique** crossing is
\[
 \boxed{u_*=\sqrt6-2.}
\]
For \(0<u<u_*\), \(\kappa_6(X_t^{\mathrm T})>\kappa_6(X_t^{\mathrm G})\) at every \(t>0\); for \(u_*<u<1\), this inequality reverses at every \(t>0\). At \(u=u_*\), all multi-time joint moments through total degree six coincide. Nevertheless, with
\[
 H(z)=12z-30+24(z+1)e^{-z}+6e^{-2z},
\]
there is **strict eighth-order separation for all \(t>0\)**:
\[
 \boxed{\ \kappa_8(X_t^{\mathrm G})-\kappa_8(X_t^{\mathrm T(u_*)})
 =\frac{40320m^4}{q^4}H(qt)>0.\ }
\]
The positive function \(H\) obeys \(H(z)=z^4+O(z^5)\) as \(z\downarrow0\) and \(H(z)=12z-30+o(1)\) as \(z\to\infty\). The eighth-order distinction therefore persists on every finite positive observation window and in its long-time growth rate.

## Assumptions and scope
The observation interval is arbitrary \(t>0\); \(m\) and \(q\) are any strictly positive finite real numbers, and \(u\in(0,1)\). The squared-OU diffusivity is nonnegative, while both Markov-switching diffusivities are strictly positive. Diffusivity processes are stationary from time zero, Brownian tracer driving noises are independent of them, and there is no drift, trap, spatial resetting or shared driving noise. The two processes need not be coupled to one another. Cumulants are ensemble cumulants, and multi-time matching is a statement about all finite families of nonnegative observation times and all nonnegative integer exponents summing to at most the specified order. No convergence or Gaussian approximation is invoked to obtain the exact cumulants.

## Proof
**1. Matching the full second-order diffusivity statistics.** The stationary OU covariance is \(\mathbb E[Y_sY_t]=m e^{-q|t-s|/2}\). The Gaussian fourth-moment identity gives \(\operatorname{Cov}(Y_s^2,Y_t^2)=2m^2e^{-q|t-s|}\). For the switching environment, \(p_+\in(0,1)\), and direct substitution gives \(\mathbb ED^{\mathrm T}=m\) and \(p_+(1-p_+)(d_+-d_-)^2=2m^2\). The two-state Markov transition semigroup has the sole nonconstant decay eigenvalue \(-q\), establishing the identical covariance formula. Its two state values are positive since \(u<1\).

**2. Reduction of multi-time tracer moments.** Put \(A_t^i=\int_0^t D_s^i\,ds\). Conditional on the entire environment, every finite vector \((X_{t_1}^i,\ldots,X_{t_n}^i)\) is centered multivariate Gaussian with conditional covariance
\[
 \operatorname{Cov}(X_{t_j}^i,X_{t_k}^i\mid D^i)=2A_{\min(t_j,t_k)}^i.
\]
Wick's formula expresses every even joint tracer moment of total degree \(2r\) as a sum of expectations of products of \(r\) integrated diffusivities. Those expectations depend only on joint moments of \(D\) of order at most \(r\). This proves the degree-four matching from step 1. For a single time, the conditional Gaussian moment generating identity \(\mathbb Ee^{zX_t^i}=\mathbb Ee^{z^2A_t^i}\) gives
\[
 \kappa_{2r}(X_t^i)=\frac{(2r)!}{r!}\,\kappa_r(A_t^i),
\]
for each \(r\ge1\), and every odd cumulant vanishes.

**3. Exact third cumulant and its unique crossing.** For ordered \(s_1\le s_2\le s_3\), the connected Gaussian-square correlation is the single triangular Wick cycle
\[
 \operatorname{cum}(D_{s_1}^{\mathrm G},D_{s_2}^{\mathrm G},D_{s_3}^{\mathrm G})
 =8m^3e^{-q(s_3-s_1)}.
\]
For the centered two-state diffusivity \(Z_t=D_t^{\mathrm T}-m\), the relation \(\mathbb E[Z_t\mid Z_s]=e^{-q(t-s)}Z_s\) and the two-point quadratic identity \(Z_t^2=2m^2+m(2/u-u)Z_t\) imply
\[
 \operatorname{cum}(D_{s_1}^{\mathrm T},D_{s_2}^{\mathrm T},D_{s_3}^{\mathrm T})
 =2m^3(2/u-u)e^{-q(s_3-s_1)}.
\]
Symmetry of cumulants extends both identities to arbitrary triple order. Integrating over \([0,t]^3\), the ordered simplex has measure factor six and its two interior-time variables produce the exact integral
\[
 \kappa_3(A_t^i)=6c_i J_q(t),\qquad
 c_{\mathrm G}=8m^3,\quad c_{\mathrm T}=2m^3(2/u-u).
\]
The displayed sixth-cumulant expressions follow. The function \(2/u-u\) decreases strictly on \((0,1)\), from \(+\infty\) to \(1\), so it equals four exactly once, at its positive quadratic root \(u=\sqrt6-2\). The triple-time diffusivity moments (including all diagonal and coinciding-time limits) match exactly at this root. By Wick's conditional argument, **every multi-time tracer joint moment through total order six** then matches.

**4. Ordered four-time connected correlations at the crossing.** Write \(a=s_2-s_1\ge0\), \(b=s_3-s_2\ge0\), \(c=s_4-s_3\ge0\) for ordered times. The six oriented Wick cycles of the stationary Gaussian squared-OU process, grouped into three inverse-pairs, give
\[
 \operatorname{cum}(D_{s_1}^{\mathrm G},\ldots,D_{s_4}^{\mathrm G})
 =16m^4\left(2e^{-q(a+b+c)}+e^{-q(a+2b+c)}\right).
\]
For the centered two-state process, successive Markov conditional expectations and its quadratic identity give
\[
 \mathbb E[Z_{s_1}Z_{s_2}Z_{s_3}Z_{s_4}]
 =(2m^2)^2e^{-q(a+c)}
 +2m^4(2/u-u)^2e^{-q(a+b+c)}.
\]
Subtracting the three covariance pairings yields
\[
 \operatorname{cum}(D_{s_1}^{\mathrm T},\ldots,D_{s_4}^{\mathrm T})
 =2m^4(2/u-u)^2e^{-q(a+b+c)}
 -8m^4e^{-q(a+2b+c)}.
\]
At \(u=u_*\), the coefficients of the first exponential both equal \(32m^4\), whereas the other coefficients differ by \(24m^4\). Thus, for **every** ordered time quadruple,
\[
 \operatorname{cum}_4(D^{\mathrm G}_{s_1},\ldots,D^{\mathrm G}_{s_4})
 -\operatorname{cum}_4(D^{\mathrm T(u_*)}_{s_1},\ldots,D^{\mathrm T(u_*)}_{s_4})
 =24m^4e^{-q(a+2b+c)}>0.
\]

**5. Strict eighth-cumulant gap at every time.** Joint cumulants integrate against deterministic measures, so \(\kappa_4(A_t)\) is the four-fold integral of the above connected diffusivity correlation. Partitioning into the 24 time orderings and introducing \(a,b,c\) as above shows
\[
 \Delta\kappa_4(A_t)
 =576m^4\int_{\substack{a,b,c\ge0\\a+b+c\le t}}
 (t-a-b-c)e^{-q(a+2b+c)}\,da\,db\,dc>0.
\]
The integral is strictly positive for every \(t>0\). Denote the four-fold ordered-correlation integral divided by its constant \(24m^4\) by \(G_q(t)\). Its Laplace transform, obtained by integrating the two nonnegative endpoint gaps and the three interior gaps, is
\[
 \int_0^\infty e^{-st}G_q(t)\,dt
 =\frac{24}{s^2(s+q)^2(s+2q)},\qquad s>0.
\]
Partial fractions (or direct convolution) give \(G_q(t)=q^{-4}H(qt)\), with the displayed explicit \(H\). Finally \(\Delta\kappa_4(A_t)=24m^4G_q(t)\), and the conditional Gaussian cumulant conversion \(\Delta\kappa_8(X_t)=1680\Delta\kappa_4(A_t)\) establishes the boxed eighth-cumulant formula. Its sign follows from the strictly positive ordered integral, independently of cancellation in the explicit exponential expression. Taylor expansion gives \(H(z)=z^4-\tfrac45z^5+O(z^6)\); the large-\(z\) form is immediate. This completes the proof.

## Verification
`CHECK.py` implements **independent** finite-dimensional moment hierarchies from the infinitesimal generators: the hierarchy of mixed integrated diffusivity and even OU powers, and the occupation-weighted hierarchy of the two-state chain. Matrix exponentiation gives moment orders through four; they are converted to second, fourth, sixth and eighth tracer cumulants without using the closed cumulant formulas internally. Comparison with the theorem's formulas at multiple values of \(m,q,u,t\), including both sides and exactly at the crossing, and with the eighth-cumulant gap, produced **949 successful assertions**. Execute `python3 CHECK.py` with NumPy and SciPy installed. These computations corroborate the identities but cannot prove quantifier-uniform sign or uniqueness; the explicit integral and monotonicity arguments above do so.

## Relationship to prior work
Sposini, Chechkin, Seno, Pagnini and Metzler (2018) compare generalized-grey Brownian motion to continuous diffusing diffusivity and their kurtosis, without the covariance-matched two-state construction here. Sposini, Grebenkov, Metzler, Oshanin and Seno (2019 preprint; 2020 journal) derive the squared-OU integrated-diffusivity framework and spectral observables, and separately analyze resampled jump diffusivities. Hidalgo-Soria, Barkai and Burov (2020 preprint; 2021 journal) derive two-state switching-diffusivity occupation-time laws and the Gaussian conditional-displacement formula for strictly positive diffusivities. Guéneau, Majumdar and Schehr (2025) derive a general exact forward transform and all finite-time moments for reset-to-fresh diffusivity; its two-atom specialization is equivalent to the Markov-switching environment. These are important **prior forward results** and are not presented as new here.

Published related inverse results establish four-observation identification inside the two-state family and eighth-moment identification inside a *harmonically confined* symmetric switching family. Neither addresses the present comparison of **two different unconfined diffusivity mechanisms matched to the same entire covariance**, its unique degree-six cancellation and its strict positive degree-eight residual at all finite times. The new classification is a specific comparative theorem extracted using classical Gaussian and Markov tools; unpublished or unindexed equivalent comparisons remain possible and publication priority has not been independently established.

## Limitations
Both environment laws and the full matching parameterization are assumed known; the theorem does not infer these models from noisy finite-sample trajectories, give sample-size requirements, or claim that the whole tracer laws coincide. At the sixth-order crossing, they agree only through joint moment degree six and **are distinguished already at degree eight**. Positivity of the two-state lower diffusivity motivates the strict range \(u<1\). The squared-OU diffusivity itself can touch zero. The models are assumed stationary, independent of their tracer Wiener drivers, and have finite positive \(m,q\). The main novelty is an exact comparison and identifiability boundary, not the individual forward occupation-time transforms or diffusivity covariance formulas already present in the literature.

## References
1. V. Sposini, A. V. Chechkin, F. Seno, G. Pagnini and R. Metzler, *Random diffusivity from stochastic equations: comparison of two models for Brownian yet non-Gaussian diffusion*, arXiv:1811.09531 (first public 2018-11-23), https://arxiv.org/abs/1811.09531 (especially sections 2, 4, 5.4).
2. V. Sposini, D. S. Grebenkov, R. Metzler, G. Oshanin and F. Seno, *Universal spectral features of different classes of random-diffusivity processes*, arXiv:1911.11661 (first public 2019-11-26), New Journal of Physics 22 (2020), 063056, https://arxiv.org/abs/1911.11661 ; legal full-text https://d-nb.info/1219663301/34 (especially sections 2, 4 and 5).
3. M. Hidalgo-Soria, E. Barkai and S. Burov, *Cusp of non-Gaussian density of particles for a diffusing diffusivity model*, arXiv:2012.11265 (first public 2020-12-21), Entropy 23 (2021), 231, https://www.mdpi.com/1099-4300/23/2/231 (especially section 2 and Appendix A).
4. M. Guéneau, S. N. Majumdar and G. Schehr, *Large Deviations in Switching Diffusion: from Free Cumulants to Dynamical Transitions*, arXiv:2501.13754 (first public 2025-01-23), https://arxiv.org/html/2501.13754v2 (particularly supplemental sections III and IV).
5. *Four cumulant observations identify a two-state fluctuating diffusivity*, published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-cumulant-observations-identify-a-two-state-fluctuating-diff--b41de1dff3bf .
6. *Sharp eighth-moment identification of hidden diffusivity switching and dissipation*, published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-eighth-moment-identification-of-hidden-diffusivity-switchi--56d3d976847e .
