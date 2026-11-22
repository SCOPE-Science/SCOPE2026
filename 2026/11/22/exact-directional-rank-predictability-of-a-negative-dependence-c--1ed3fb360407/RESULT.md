# Exact directional rank predictability of a negative-dependence copula

## Finding

For every \(\theta>0\), the absolutely continuous Ghosh–Bhuyan–Finkelstein copula has the following *population* Chatterjee rank-dependence coefficients, with the direction indicated by the variable to be predicted:

\[
\xi(V\mid U)=\frac{2\theta^2}{(1+\theta)(1+2\theta)},\qquad
\xi(U\mid V)=\frac{2\theta}{3+2\theta}.
\]

In particular, the predictive asymmetry is *strict* for every finite positive \(\theta\):

\[
\Delta(\theta):=\xi(U\mid V)-\xi(V\mid U)
=\frac{2\theta}{(1+\theta)(1+2\theta)(3+2\theta)}>0.
\]

It is maximized uniquely at the positive root \(\theta_*\) of \(8\theta^3+12\theta^2-3=0\), with
\[
\theta_*=0.439692620785908384\ldots,\qquad
\Delta(\theta_*)=0.083778132003164186\ldots.
\]
The gap tends to zero at both parameter endpoints \(\theta\downarrow0\) and \(\theta\uparrow\infty\). The original copula has Kendall coefficient \(\tau=-\theta/(1+\theta)\). Thus, putting \(t=-\tau\in(0,1)\), the exact directional dependence values are \(\xi(U\mid V)=2t/(3-t)\) and \(\xi(V\mid U)=2t^2/(1+t)\), despite the symmetric nature of Kendall's coefficient.

## Assumptions and scope

Let \(\theta>0\), \(b=\theta/(1+\theta)\), and \(r=1-u\). For \(u,v\in[0,1]\), use the following continuous extension at the boundaries of the published copula:

\[
C_\theta(u,v)=\begin{cases}
0,&0\le v\le br,\\
v-r+\dfrac{\theta^\theta}{(1+\theta)^{1+\theta}}r^{1+\theta}v^{-\theta},&br<v\le b,\\
u-(1-v)(1-r^{1+\theta}),&b<v\le1.
\end{cases}
\]

The boundary cases \(v=0\) and \(u=1\) are understood by continuity. Its density, away from the two separating curves, is zero in the first region, \(\theta^{1+\theta}r^\theta/[(1+\theta)^\theta v^{1+\theta}]\) in the second, and \((1+\theta)r^\theta\) in the third. The density is nonnegative; the function has grounded boundaries and uniform marginals. Therefore it is an absolutely continuous copula. The result concerns this one-parameter bivariate model and population quantities, not an estimator or a causal direction.

For a pair \((A,B)\) with uniform continuous marginals, define Chatterjee's population coefficient by
\[
\xi(B\mid A)=6\int_0^1\int_0^1
\bigl(\Pr(B\le z\mid A=a)-z\bigr)^2\,da\,dz
=6\int_0^1\int_0^1\Pr(B\le z\mid A=a)^2\,da\,dz-2.
\]
The two versions are equal because the conditional CDF averages to \(z\). Throughout, expressions are interpreted almost everywhere, so values on switching boundaries have no effect.

## Proof

Write \(r=1-u\). Differentiation of the displayed copula in the first coordinate gives, almost everywhere,
\[
F_{V\mid U=u}(v)=\begin{cases}
0,&0<v<br,\\
1-(br/v)^\theta,&br\le v\le b,\\
1-(1+\theta)(1-v)r^\theta,&b<v<1.
\end{cases}
\]
For \(0<v\le b\), integrate the square first in \(u\), changing variables \(s=br/v\):
\[
\int_0^1 F_{V\mid U=u}(v)^2\,du
=\frac vb\int_0^1(1-s^\theta)^2\,ds
=\frac{2\theta v}{1+2\theta}.
\]
For \(b<v<1\), direct integration gives
\[
\int_0^1 F_{V\mid U=u}(v)^2\,du
=v^2+\frac{\theta^2}{1+2\theta}(1-v)^2.
\]
Subtract \(v^2\) and integrate over the two intervals. With \(b=\theta/(1+\theta)\),
\[
\begin{aligned}
\frac{\xi(V\mid U)}6
&=\int_0^b\left(\frac{2\theta v}{1+2\theta}-v^2\right)\,dv
+\int_b^1\frac{\theta^2(1-v)^2}{1+2\theta}\,dv\\
&=\frac{\theta^2}{3(1+\theta)(1+2\theta)}.
\end{aligned}
\]

Differentiation in the second coordinate instead yields
\[
F_{U\mid V=v}(u)=\begin{cases}
0,&0<v<br,\\
1-(br/v)^{1+\theta},&br\le v\le b,\\
1-r^{1+\theta},&b<v<1.
\end{cases}
\]
Put
\[
J=\int_0^1(1-s^{1+\theta})^2\,ds
=1-\frac2{2+\theta}+\frac1{3+2\theta}
=\frac{2(1+\theta)^2}{(2+\theta)(3+2\theta)}.
\]
For \(v\le b\), integration of the squared conditional CDF over \(u\) gives \((v/b)J\); for \(v>b\) it gives \(J\). Consequently,
\[
\int_0^1\int_0^1F_{U\mid V=v}(u)^2\,du\,dv
=\left(1-\frac b2\right)J
=\frac{1+\theta}{3+2\theta},
\]
and hence \(\xi(U\mid V)=6(1+\theta)/(3+2\theta)-2=2\theta/(3+2\theta)\).

Subtracting the two formulas gives the stated positive gap. Its derivative is
\[
\Delta'(\theta)=-\frac{2(8\theta^3+12\theta^2-3)}{(1+\theta)^2(1+2\theta)^2(3+2\theta)^2}.
\]
The numerator polynomial is strictly increasing on \((0,\infty)\), starts negative, and tends to infinity. It has precisely one positive root, so the gap increases then decreases and has its unique global maximum there. The limits at zero and infinity vanish by direct inspection. The final Kendall reparameterization is algebraic from the published identity \(\tau=-\theta/(1+\theta)\).

## Verification

The standalone file `check_directional.py` uses exact symbolic integration and simplification to check both formulas, their difference, and its derivative. Independent adaptive quadrature integrates the *piecewise conditional CDFs themselves*, rather than their closed-form integrated expressions, at five different positive parameters. The resulting numerical values agree with the formulas within the specified absolute tolerance. An independently root-solved cubic yields the displayed maximizer and maximum. Run `python check_directional.py` with Python, SymPy, and SciPy installed.

## Relationship to prior work

Bhuyan, Ghosh, Majumder and Mitra (2020) introduced the underlying exponential construction \(X=Z_1\), \(Y=\exp(Z_2-Z_1)\) and studied negative dependence and regressions. Ghosh, Bhuyan and Finkelstein (public preprint 2021; journal article 2022) derived this exact copula, its conditional CDFs, Spearman's rho, Kendall's tau, and strong negative stochastic orders. These are prior results, not new claims. The present finding evaluates a *different* nonlinear directed rank dependence functional and proves its sharp directional gap.

Ansari and Rockel (2024) give the general conditional-CDF approach to Chatterjee's coefficient and formulas for numerous standard copulas, including Marshall–Olkin, Cuadras–Augé, and FGM, but their inspected table does not list the Ghosh–Bhuyan–Finkelstein family. The exact region for Chatterjee's coefficient versus Spearman's rho for unrestricted copulas (2026) does not identify these two directional curves for this particular family. No directly covering calculation was located in the specified searches; this is not a proof of priority over every possible earlier publication.

## Limitations

The formulas describe population dependence, not finite-sample bias, variance, testing power, or causality. The asymmetry is specific to the orientation of the named coordinates and vanishes at the limiting independent/countermonotone regimes. The literature comparison is bounded to the inspected sources and mathematical record searches; unindexed or inaccessible model-specific calculations remain a priority risk. Numerical quadrature supports the proof but is not used to justify the all-parameter statements. No independent external audit has been performed.

## References

- Bhuyan, P., Ghosh, S., Majumder, P., and Mitra, M. (2020). *A bivariate life distribution and notions of negative dependence.* Stat 9, e276. First publicly published 5 February 2020. https://doi.org/10.1002/sta4.276
- Ghosh, S., Bhuyan, P., and Finkelstein, M. (2021). *On a Bivariate Copula for Modeling Negative Dependence: Application to New York Air Quality Data.* Public arXiv submission 10 February 2021. https://arxiv.org/abs/2102.05386
- Ghosh, S., Bhuyan, P., and Finkelstein, M. (2022). *On a bivariate copula for modeling negative dependence: application to New York air quality data.* Statistical Methods & Applications 31, 1329–1353. https://doi.org/10.1007/s10260-022-00636-3
- Ansari, J., and Rockel, M. (2024). *Dependence properties of bivariate copula families.* Dependence Modeling 12, 20240002. https://doi.org/10.1515/demo-2024-0002
- *The exact region and an inequality between Chatterjee's and Spearman's rank correlations* (2026). Journal of Multivariate Analysis. https://doi.org/10.1016/j.jmva.2026.105630
