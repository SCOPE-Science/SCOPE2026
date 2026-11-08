# A sharp horizon transition for pinned observations of two exponential modes

## Finding
Consider noisy observations of a two-mode stable diagonal system, with one reading fixed at the initial time, one at the terminal time, and one independently measured reading free to be placed between them. The optimal determinant of information has an exact, rate-uniform horizon threshold. For distinct known decay rates \(0<a<b\), define
\[
T_c=\frac{\log(b/a)}{b-a}.
\]
For every \(T\in(0,T_c]\), the only determinant-maximizing placements of the free observation are \(t=0\) and \(t=T\). For every \(T>T_c\), there is one and only one optimal interior placement, given by an explicit root of a quadratic equation in \(e^{-(b-a)t}\). For every such longer horizon, that optimum satisfies \(0<t_*(T)<T_c<T\), and \(t_*(T)\to T_c\) at both ends of the range \(T\in(T_c,\infty)\). In particular, the optimal free observation time is not a monotone function of the terminal horizon.

Write \(r=b/a>1\), \(q=e^{-aT}\), and \(v=e^{-(b-a)T}\). For \(T>T_c\), let \(u_-\) be the smaller of the two roots in \((v,1)\) of
\[
Q_T(u)=r(1+q^2)u^2-(r+1)(1+q^2v)u+1+q^2v^2.
\]
Then
\[
t_*(T)=-\frac{\log u_-}{b-a}.
\]
The smaller root may be evaluated stably as \(u_-=2(1+q^2v^2)/[(r+1)(1+q^2v)+\sqrt{\Delta}]\), where
\[
\Delta=(r+1)^2(1+q^2v)^2-4r(1+q^2)(1+q^2v^2)>0.
\]
The best interior design's information-determinant advantage relative to repeating either endpoint diverges exponentially, with exact ratio asymptotic
\[
\frac{F_T(t_*(T))}{F_T(0)}\sim
\frac{(r-1)^2}{2r^{\,2+2/(r-1)}}e^{2aT}
\qquad(T\to\infty).
\]

## Assumptions and scope
Let \(0<a<b\), \(T>0\), and \(\sigma>0\) be fixed and known real numbers. The state evolves according to \(\dot x(s)=\operatorname{diag}(-a,-b)x(s)\), with observation row \(C=(1,1)\). Its unknown initial amplitudes \(A,B\in\mathbb R\) are measured through the scalar signal
\[
y(s)=A e^{-as}+B e^{-bs}+\eta_s.
\]
Three observation **events** occur at \(s=0,t,T\), with \(0\le t\le T\). Their errors are independent Gaussian \(\mathcal N(0,\sigma^2)\) random variables, which makes the Fisher-information interpretation exact. The associated normal-equation Gram calculation also applies under independent centered equal-variance errors. If \(t=0\) or \(t=T\), two different observation events occur at the same physical time, with independent errors. With rows \((e^{-as},e^{-bs})\) at the three times, let \(X_t\in\mathbb R^{3\times2}\) be the design matrix, \(G_t=\sigma^{-2}X_t^{\mathsf T}X_t\), and \(F_T(t)=\sigma^4\det G_t=\det(X_t^{\mathsf T}X_t)\). The optimization is over continuous observation time \(t\), not over the rates, the number of readings, sensor positions, or any alternative loss objective.

For notation set \(x=e^{-at}\), \(u=e^{-(b-a)t}\), \(q=e^{-aT}\), \(v=e^{-(b-a)T}\), and \(r=b/a\), so \(q\le x\le1\), \(v\le u\le1\), and \(u=x^{r-1}\). The endpoint design value is
\[
E_T=F_T(0)=F_T(T)=2q^2(1-v)^2>0.
\]

## Proof
**1. Exact determinant.** Cauchy–Binet applied to the three rows of \(X_t\) yields the sum of the three squared pair minors. It is exactly
\[
F_T(t)=x^2(1-u)^2+q^2(1-v)^2+q^2x^2(u-v)^2.\tag{1}
\]
The endpoint values stated above follow by setting \(x=q,u=v\) or \(x=1,u=1\); their equality is an exact identity, not a symmetry assumption about the decays.

**2. A quadratic controls every stationary point.** Treat \(F_T\) as a function of \(x\in[q,1]\). Since \(d(x^{r-1})/dx=(r-1)u/x\), differentiating (1) gives
\[
\frac{dF_T}{dx}=2x\big[(1-u)(1-ru)+q^2(u-v)(ru-v)\big]
=2xQ_T(u),\tag{2}
\]
where \(Q_T\) is the quadratic in the finding. Its endpoint values are
\[
Q_T(v)=(1-v)(1-rv),\qquad
Q_T(1)=q^2(1-v)(r-v)>0.\tag{3}
\]
Because \(v=e^{-(b-a)T}\), the sign of \(1-rv\) changes precisely at \(T=T_c\). The quadratic's leading coefficient \(r(1+q^2)\) is positive.

**3. Complete classification.** If \(T<T_c\), equation (3) gives \(Q_T(v)<0<Q_T(1)\). A strictly convex quadratic negative at the left endpoint has exactly one zero within \((v,1)\), after which it is positive. Thus (2), with \(x\) increasing from \(q\) to \(1\), shows that \(F_T\) strictly decreases and then strictly increases. Both endpoints have the same value \(E_T\), and these are the only maxima. At \(T=T_c\), \(Q_T(v)=0\) and direct differentiation gives \(Q'_T(v)=(r-1)(q^2/r-1)<0\); \(Q_T\) is negative immediately to the right of \(v\) before its one other zero in \((v,1)\). The same endpoint conclusion holds.

If \(T>T_c\), equation (3) gives \(Q_T(v)>0\). Hence (2) makes \(F_T(x)>F_T(q)\) for all \(x>q\) sufficiently close to \(q\). But \(F_T(1)=F_T(q)\), so its derivative must be negative somewhere between. A quadratic positive at \(v\) and at \(1\), but negative in between, has exactly two distinct roots \(v<u_-<u_+<1\). Equation (2) gives the three successive derivative signs \(+,-,+\). Its unique local maximum, at \(u_-\), is strictly above both equal endpoint values, and its local minimum, at \(u_+\), cannot be a global maximum. This proves existence, uniqueness, and the explicit interior formula for all real rates \(0<a<b\).

**4. Sharp placement bound and nonmonotonicity.** Still for \(T>T_c\), we show \(u_->1/r\). Equation (2) evaluated at \(u=1/r\) yields
\[
Q_T(1/r)=q^2(1/r-v)(1-v)>0,
\]
while
\[
Q'_T(1/r)=-(r-1)+v^{2/(r-1)}[2-(r+1)v]<0.
\]
For the strict last inequality, on \(0<v<1/r\) the function \(v^{2/(r-1)}[2-(r+1)v]\) has maximum at \(v=4/(r+1)^2\), with value at most \(2(r-1)/(r+1)<r-1\). Thus \(1/r\) lies to the left of the first root \(u_-\), and therefore \(t_*<T_c\). At \(T\downarrow T_c\), the first root approaches \(v=1/r\), so \(t_*\to T_c\). At \(T\to\infty\), \(q,v\to0\), and the quadratic tends to \((1-u)(1-ru)\). Its smaller root tends to \(1/r\), so again \(t_*\to T_c\). The strict intermediate inequality together with these two endpoint limits proves nonmonotonicity of \(t_*(T)\) on \((T_c,\infty)\).

**5. Transition and long-horizon gains.** Let \(\delta=T-T_c\downarrow0\), \(g=b-a\), and \(q_c=e^{-aT_c}\). Expanding equation (2) at the lower endpoint \(x=q\) gives
\[
F'_T(q)=\frac{2q_c(r-1)g}{r}\delta+O(\delta^2),
\qquad
F''_{T_c}(q_c)=-\frac{2(r-1)^2}{r}\left(1-\frac{q_c^2}{r}\right).
\]
Solving for the unique nearby maximizer and substituting into the Taylor series yields
\[
t_*(T)=T_c-\frac{q_c^2}{r-q_c^2}\delta+O(\delta^2),\qquad
F_T(t_*)-E_T=\frac{q_c^2g^2}{r-q_c^2}\delta^2+O(\delta^3).\tag{4}
\]
For long horizons, \(u_-\to1/r\), \(x_*\to r^{-1/(r-1)}\), and (1) gives
\[
F_T(t_*)\to r^{-2/(r-1)}(1-1/r)^2.
\]
Because \(E_T\sim2e^{-2aT}\), their ratio is exactly the stated exponentially growing asymptotic. All limits assume fixed distinct rates and positive noise variance.

## Verification
The standalone standard-library script `verify.py` checks 56,063 assertions. These include exact-rational Cauchy–Binet identities for nine integer rate ratios, exact rational derivative identities, independent determinants from \(X_t^{\mathsf T}X_t\), dense grids spanning both sides of the threshold for nonintegral rate ratios, and numerical checks of the short-horizon, transition, and large-horizon expansions. Running `python verify.py` reports `VERIFICATION_OK 56063 exact-rational and sampled-grid assertions`. Finite sampling is not a proof of optimization for all continuous rates or times: the global result rests on the sign analysis in Steps 2–4. For illustration at \(a=1,b=2,T=1\), the threshold is \(\log 2\), the interior optimal time is approximately \(0.666852546\), and the information determinant increases by approximately \(8.4\%\) relative to repeating an endpoint.

## Relationship to prior work
Reci and collaborators (2018) analyze noisy bi-exponential sampling for nuclear magnetic resonance through a four-unknown-parameter Cramér–Rao criterion and numeric sampling patterns, including 32-point families. Their model motivates the two-decay problem but their objective, known/unknown parameters, sampling budget, and theorem differ. Krauss, Lopez and Müller (2022) establish rank-based sample observability for discrete-time linear systems, without maximizing a three-event Fisher determinant. Kazma and colleagues (2023) analyze sensor-subset selection by log-determinant and trace metrics on a fixed time window, rather than one free measurement time with two pinned observations. An earlier exact-design study by Dette, Martínez-López, Ortiz-Rodríguez, and Pepelyshev (2004) obtains the same logarithmic-mean expression in a different setting: a standardized maximin design robust to an unknown single exponential rate, with a different Fisher regression family and design budget. Its Section 4.2 does not give the pinned, three-event, two-known-decay, two-amplitude observability determinant, phase transition, or finite-rate quadratic optimizer. The critical logarithmic-mean number is therefore not claimed novel in isolation. The confluent equal-rate Jordan limit of the present two-distinct-rate formula reproduces the previously studied single Jordan-mode timing threshold, but that limiting case does not imply the exact distinct-rate optimization or the universal logarithmic-mean boundary. An independently derived exact scheduling theorem in specialized experimental-design literature remains possible; this is a statement of the scope of available comparison, not proof of publication priority.

## Limitations
The model has exactly two known distinct positive decay rates and two unknown real amplitudes, independent equal-variance errors, and exactly three observation events. Repeated endpoint observations are permitted and counted as independent events. Optimality is for the determinant of the Fisher information, not individual amplitude variance, robustness to rate misspecification, estimation of the rates themselves, or optimization with more than three events. Formula (4) is a fixed-rate, local transition expansion, and the large-horizon ratio holds for fixed distinct rates. The mathematical result is analytic; the supplemental verifier is finite. No independent external proof review has been performed.

## References
1. A. Reci, M. I. Ainte, A. J. Sederman, M. D. Mantle, and L. F. Gladden, *Optimising sampling patterns for bi-exponentially decaying signals*, first publicly online 2018-11-06, DOI: https://doi.org/10.1016/j.mri.2018.09.029 ; lawful manuscript: https://api.repository.cam.ac.uk/server/api/core/bitstreams/eec7ee9b-020a-4569-a588-7f6d3daa5b7c/content .
2. I. Krauss, V. G. Lopez, and M. A. Müller, *Sample-based observability of linear discrete-time systems*, arXiv:2204.06451, first posted 2022-04-13, https://arxiv.org/html/2204.06451v3 .
3. M. H. Kazma, S. A. Nugroho, A. Haber, and A. F. Taha, *State-Robust Observability Measures for Sensor Selection in Nonlinear Dynamic Systems*, arXiv:2307.07074, first posted 2023-07-13, https://arxiv.org/html/2307.07074v1 .
4. H. Dette, I. Martínez-López, I. M. Ortiz-Rodríguez, and A. Pepelyshev, *Efficient design of experiment for exponential regression models*, working paper (2004), https://hdl.handle.net/10419/49337 ; DOI: https://doi.org/10.17877/DE290R-15070 .
5. H. Dette and H.-M. Neugebauer, *Bayesian D-optimal designs for exponential regression models*, *Journal of Statistical Planning and Inference* 60 (1997), 331–349, https://doi.org/10.1016/S0378-3758(96)00131-0 .
