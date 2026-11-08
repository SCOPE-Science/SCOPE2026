# Logarithmic onset of the beta-prime failure-rate peak

## Finding

Let \(X_{a,b}\) have the beta-prime distribution with shape parameters \(a,b>0\), normalized to unit scale, and let \(h_{a,b}\) be its failure rate. The known qualitative distinction between decreasing and arc-shaped hazards has a sharp quantitative boundary layer at \(a=1\). Put

\[
K_b=\psi(b+1)-\psi(1),
\]

where \(\psi\) is the digamma function. For fixed \(b>0\), the unique maximum of \(h_{1+\varepsilon,b}\), at location \(x_{\varepsilon,b}\), obeys

\[
\boxed{x_{\varepsilon,b}=\varepsilon+b\varepsilon^2(\log\varepsilon+K_b)+O_b(\varepsilon^3\log^2\varepsilon)}
\]

and its height obeys

\[
\boxed{h_{1+\varepsilon,b}(x_{\varepsilon,b})=
 b\big[1+\varepsilon(\log\varepsilon+K_b-1)\big]
 +O_b(\varepsilon^2\log^2\varepsilon).}
\]

These estimates are uniform when \(b\) ranges over any fixed compact subset of \((0,\infty)\). Thus the hazard peak emerges at a distance asymptotic to \(a-1\) from the origin, but its next displacement is logarithmic and depends explicitly on the second shape parameter. This is a location and height result, not a claim to have first discovered the arc-shaped hazard class.

## Assumptions and scope

The density, survival function, and hazard for \(x>0\) are

\[
f_{a,b}(x)=\frac{x^{a-1}}{B(a,b)(1+x)^{a+b}},\qquad
S_{a,b}(x)=\int_x^\infty f_{a,b}(y)\,dy,\qquad
h_{a,b}(x)=\frac{f_{a,b}(x)}{S_{a,b}(x)}.
\]

Every statement is for real parameters \(a,b>0\); no moments are assumed. The asymptotic formulas are for \(a=1+\varepsilon\) with \(\varepsilon\downarrow0\) and \(b\) fixed or constrained to a compact positive interval. Location and height refer to the hazard, not the density mode. Any positive external scale multiplies the location and divides the hazard height.

For completeness, when \(0<a\le1\), \(h_{a,b}\) is strictly decreasing. When \(a>1\), it is strictly increasing up to a unique peak and strictly decreasing thereafter. The latter shape classification is used as a lemma; the new quantitative target is the critical onset expansion above.

## Proof

**1. A unique peak and an explicit bracket.** Define the negative logarithmic density slope

\[
g(x)=-\frac{f'_{a,b}(x)}{f_{a,b}(x)}
=\frac{(b+1)x-(a-1)}{x(1+x)}.
\]

Differentiating \(h=f/S\) using \(S'=-f\) gives

\[
h'(x)=h(x)\big(h(x)-g(x)\big).
\]

For \(0<a\le1\), \((\log f)''=(1-a)/x^2+(a+b)/(1+x)^2>0\). Therefore, for each \(t>0\), \(f(x+t)/f(x)\) is strictly increasing in \(x\). The identity \(S(x)/f(x)=\int_0^\infty f(x+t)/f(x)\,dt\) shows that \(S/f\) increases strictly, so \(h\) decreases strictly.

For \(a>1\), set \(m=(a-1)/(b+1)\). Then \(g\le0\) on \((0,m]\), and hence \(h'>0\) there. Moreover,

\[
g'(x)=\frac{(a-1)(1+2x)-(b+1)x^2}{x^2(1+x)^2}.
\]

Its numerator has precisely one positive root,

\[
c=\frac{a-1+\sqrt{(a-1)(a+b)}}{b+1}>m.
\]

Thus \(g\) rises on \((m,c)\) and decreases on \((c,\infty)\). Since \(g\) is positive and strictly decreasing beyond \(c\), for each \(x\ge c\) and \(t>0\),

\[
\frac{f(x+t)}{f(x)}=\exp\left[-\int_0^t g(x+u)\,du\right]
>e^{-tg(x)}.
\]

Consequently \(S(x)/f(x)>1/g(x)\), or \(h(x)<g(x)\), and \(h'<0\) for \(x\ge c\). On \((m,c)\), write \(H=h-g\). At every zero of \(H\), the identity above gives \(H'=-g'<0\). Since \(H(m)>0\) and \(H(c)<0\), exactly one zero exists (all zeros cross strictly from positive to negative). It is the unique global hazard maximizer \(x_{a,b}\), with the strict bracket

\[
\frac{a-1}{b+1}<x_{a,b}<\frac{a-1+\sqrt{(a-1)(a+b)}}{b+1}.
\]

**2. Critical asymptotics.** Fix a compact \(K\subset(0,\infty)\) for \(b\), and write \(a=1+\varepsilon\). Uniformly over \(b\in K\), the beta normalization has the expansion

\[
B(1+\varepsilon,b)^{-1}
=b\big[1+\varepsilon K_b+O_K(\varepsilon^2)\big],
\qquad K_b=\psi(b+1)-\psi(1).
\]

Consider \(x=\varepsilon+\varepsilon^2z\), with \(|z|\le C|\log\varepsilon|\), where \(C\) is fixed. Expanding the density, and integrating it from zero to \(x\) to obtain \(S=1-\int_0^x f\), yields, uniformly in this window,

\[
\begin{aligned}
f_{1+\varepsilon,b}(x)
 &=b\big[1+\varepsilon(K_b+\log\varepsilon-b-1)\big]
 +O_{K,C}(\varepsilon^2\log^2\varepsilon),\\
S_{1+\varepsilon,b}(x)
 &=1-b\varepsilon+O_{K,C}(\varepsilon^2|\log\varepsilon|),\\
h_{1+\varepsilon,b}(x)
 &=b\big[1+\varepsilon(K_b+\log\varepsilon-1)\big]
 +O_{K,C}(\varepsilon^2\log^2\varepsilon),\\
g(x)
 &=b+\varepsilon(z-b)+O_{K,C}(\varepsilon^2\log^2\varepsilon).
\end{aligned}
\]

In particular,

\[
H(x)=h(x)-g(x)=
\varepsilon\big[b(K_b+\log\varepsilon)-z\big]
+O_{K,C}(\varepsilon^2\log^2\varepsilon).
\]

Set \(z_0=b(K_b+\log\varepsilon)\). Choosing \(z=z_0-1\) and \(z=z_0+1\) gives opposite signs for \(H\) for all sufficiently small \(\varepsilon\), uniformly in \(b\in K\). By uniqueness, the maximum lies in that window. There \(g'(x)=\varepsilon^{-1}+O_{K,C}(|\log\varepsilon|)\), while \(h'=hH\) is bounded by \(O_{K,C}(\varepsilon|\log\varepsilon|)\); hence \(H'=-\varepsilon^{-1}+O_{K,C}(|\log\varepsilon|)\). The mean-value theorem, with \(H(\varepsilon+\varepsilon^2z_0)=O_{K,C}(\varepsilon^2\log^2\varepsilon)\), gives

\[
x_{\varepsilon,b}-(\varepsilon+\varepsilon^2z_0)
=O_K(\varepsilon^3\log^2\varepsilon).
\]

Inserting that location into the uniform hazard expansion yields the claimed peak-height formula. All remainders arise from smooth beta-function Taylor expansion and elementary bounds on \(\varepsilon\log x\) and \(x\); none requires an unproved asymptotic interchange.

## Verification

The standalone Python 3 script `verify.py` uses only the standard library. It verifies 5,910 exact-rational and numerical assertions. Exact identities include the case \(a=2\), where direct integration gives

\[
S_{2,b}(x)=\frac{1+(b+1)x}{(1+x)^{b+1}},\quad
h_{2,b}(x)=\frac{b(b+1)x}{(1+x)(1+(b+1)x)},\quad
x_{2,b}=\frac1{\sqrt{b+1}}.
\]

It also checks the two critical asymptotic approximations at decreasing \(\varepsilon\) for several integer values of \(b\), using an independent finite-binomial formula for the survival integral. Run with `python3 verify.py`. These finite checks are consistency tests; the preceding analysis is the proof for all real \(b>0\).

## Relationship to prior work

Baricz, Prabhu K., Sahoo and Singh (2026), Theorem 4, classify the beta-prime law as NWU exactly for \(a\le1\), and as neither NWU nor NBU for \(a>1\). Earlier survival-analysis papers, including Cox (2008) on generalized \(F\) hazards and Glaser (1980) on hazard-shape criteria, already develop arc-shaped failure rates. Leão et al. (2018) explicitly mention arc-shaped beta-prime hazards. Those prior qualitative classifications are not claimed as new. The present quantitative statement isolates the critical shape crossing and computes the universal linear onset, the shape-dependent logarithmic correction, and the peak-height boundary layer. Targeted source and literature searches did not reveal those two asymptotic coefficients, but historical priority has not been independently established.

## Limitations

The expansion is local to the threshold \(a\downarrow1\); it does not characterize all-parameter maximizer asymptotics in other limits, nor any gamma-gamma product's hazard mode. The exact shape classification is classical or closely implied by general hazard-shape theory. Broader full texts of Cox (2008) and Glaser (1980) were not accessible at review; they are priority risks for a possible pre-existing quantitative result. The checker does not certify infinite asymptotics or independent mathematical validation.

## References

1. Á. Baricz, D. Prabhu K., S. Sahoo and S. Singh, *The NWU ageing property of the gamma-gamma distribution*, arXiv:2610.37725v1 (first public October 27, 2026), especially Theorem 4, https://arxiv.org/abs/2610.37725.
2. J. Leão, M. Bourguignon, M. Santos-Neto and H. Saulo, *The negative binomial beta prime regression model with cure rate*, arXiv:1812.07935v1 (2018), especially introduction and Section 2, https://arxiv.org/abs/1812.07935.
3. C. Cox, *The generalized F distribution: An umbrella for parametric survival analysis*, Statistics in Medicine 27 (2008), 4301–4312, https://doi.org/10.1002/sim.3292.
4. R. E. Glaser, *Bathtub and related failure rate characterizations*, Journal of the American Statistical Association 75 (1980), 667–672, https://doi.org/10.1080/01621459.1980.10477530.
5. K. Siegrist, *The Beta Prime Distribution*, Probability, Mathematical Statistics, and Stochastic Processes, online exposition (2022), https://www.randomservices.org/random/special/BetaPrime.html.
