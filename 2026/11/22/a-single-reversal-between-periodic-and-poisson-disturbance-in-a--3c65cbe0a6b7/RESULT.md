# A single reversal between periodic and Poisson disturbance in a transient successional habitat

## Finding
Consider a habitat patch reset to a newly disturbed state at successive disturbance times. After each reset it matures at rate \(a>0\), becomes suitable for a transient successional species, and then senesces at rate \(b>0\); it remains unsuitable until the next reset. The two stage durations are independent exponentials, with fresh draws after every reset. Compare independent, identically distributed disturbance intervals of (i) exactly \(m>0\) and (ii) exponential duration of mean \(m\). In each regime let \(U_{\mathrm{per}}(m)\) and \(U_{\mathrm{Poi}}(m)\) denote the almost-sure long-run fraction of time that the patch is suitable.

**Theorem.** For every \(a,b>0\), there is a **unique** \(m_*(a,b)>0\) such that
\[
U_{\mathrm{Poi}}(m)>U_{\mathrm{per}}(m)\quad(0<m<m_*),\qquad
U_{\mathrm{Poi}}(m)<U_{\mathrm{per}}(m)\quad(m>m_*),
\]
with equality exactly at \(m=m_*\). The closed expressions are
\[
U_{\mathrm{Poi}}(m)=\frac{am}{(1+am)(1+bm)},\quad
U_{\mathrm{per}}(m)=\frac{a}{a-b}\left[\frac{1-e^{-bm}}{bm}-\frac{1-e^{-am}}{am}\right]\quad(a\ne b),
\]
and \(U_{\mathrm{per}}(m)=[1-(1+am)e^{-am}]/(am)\) when \(a=b\).

Define \(g(x)=[1-(1+x)e^{-x}]/[x(1+x)]\) for \(x>0\). If \(a\ne b\), the unique crossover satisfies \(g(am_*)=g(bm_*)\). Let \(z=0.868863198403743\ldots\) be the unique positive solution of \((1+z)^3e^{-z}=1+2z\). Then
\[
\frac{z}{\max(a,b)}<m_*<\frac{z}{\min(a,b)}\quad (a\ne b),\qquad m_*(a,a)=\frac{z}{a}.
\]
These are **exactly matched mean disturbance intervals**, rather than equal average patch ages or equal variances.

## Assumptions and scope
Let \(X\sim\operatorname{Exp}(a)\) be the time from the reset to maturation and let \(Y\sim\operatorname{Exp}(b)\) be the subsequent suitable duration; the patch is suitable at time \(t\) since reset precisely when \(X\le t<X+Y\). Each interval uses independent \((X,Y)\) draws, independent of the disturbance interval. An interval ending before maturation simply produces no suitability; a new disturbance erases any unfinished progression. The renewal process has positive finite mean \(m\). The periodic case is interpreted by its long-run time average, or equivalently by a uniform stationary observation phase. The Poisson case uses exponential holding times with rate \(1/m\). There is no immigration, local extinction, demographic feedback, or spatial coupling. Thus \(U\) measures suitable-habitat exposure, not population persistence.

## Proof
Let \(p(t)=\Pr\{X\le t<X+Y\}\). Conditioning on \(X\) yields
\[
p(t)=\int_0^t ae^{-as}e^{-b(t-s)}\,ds
=\begin{cases}\displaystyle\frac{a}{a-b}(e^{-bt}-e^{-at}),&a\ne b,\\at e^{-at},&a=b.\end{cases}
\]
By the renewal-reward theorem, the long-run suitable fraction equals \(\mathbb E[\int_0^T p(t)dt]/\mathbb ET\), with disturbance duration \(T\). For deterministic \(T=m\) this gives \(m^{-1}\int_0^m p(t)dt\). For \(T\sim\operatorname{Exp}(1/m)\), Tonelli's theorem gives \(m^{-1}\int_0^\infty e^{-t/m}p(t)dt\). Evaluating these integrals proves the displayed formulas.

Put \(B(x)=1-(1+x)e^{-x}>0\) and \(g(x)=B(x)/[x(1+x)]\). For \(a\ne b\), subtracting the formulae gives the exact difference
\[
U_{\mathrm{Poi}}(m)-U_{\mathrm{per}}(m)
=\frac{a}{a-b}\bigl(g(am)-g(bm)\bigr).
\]
We establish the nonstandard property that \(g\) is **strictly log-concave on a logarithmic argument scale**: the elasticity
\[
r(x):=\frac{xg'(x)}{g(x)}
=\frac{x^2e^{-x}}{B(x)}-1-\frac{x}{1+x}
\]
is strictly decreasing on \((0,\infty)\). Indeed, the derivative of its first term has the sign of \((2-x)B(x)-x^2e^{-x}\). The negative of this expression is
\[
J(x)=x^2e^{-x}-(2-x)B(x)=(x+2)e^{-x}-(2-x).
\]
Since \(J(0)=0\) and \(J'(x)=1-(1+x)e^{-x}>0\) for every \(x>0\), that first derivative is negative; the derivative of \(-x/(1+x)\) is also negative. Moreover \(r(0+)=1\) and \(r(\infty)=-2\). Consequently \(g\) has a unique positive maximizer \(z\), at \(r(z)=0\), equivalent to \((1+z)^3e^{-z}=1+2z\).

For \(a>b\), the ratio \(g(am)/g(bm)\) strictly decreases with \(m\), because its logarithmic derivative is \(r(am)-r(bm)<0\). It tends to \(a/b>1\) as \(m\downarrow0\), and to \((b/a)^2<1\) as \(m\to\infty\). Thus it crosses 1 exactly once, with the claimed signs. For \(a<b\), the ratio strictly increases between limits \(a/b<1\) and \((b/a)^2>1\); the factor \(a/(a-b)<0\) gives the same advantage signs. The equality lies strictly between the two locations where \(am\) and \(bm\) equal the unique maximizer \(z\), proving the bounds. If \(a=b\), taking the continuous limit in the exact difference yields \(U_{\mathrm{Poi}}(m)-U_{\mathrm{per}}(m)=am\,g'(am)\), which changes sign exactly once at \(am=z\). All positive rates and all positive means are covered.

## Verification
The standalone `check.py` checks 2,016 exact-rational choices of rates and mean interval using three-state Markov balance equations (four assertions per choice), then separately evaluates both renewal integrals by numerical quadrature and checks crossover existence, location and signs at 700 reproducible random parameter pairs. The complete replay output is `PASS: 12924 assertions` using Python's standard library. Symbolic differentiation separately confirms the elasticity and \(J\)-identity used in the proof; the theorem itself relies on the exact analytic argument, not on finite tests.

For \(a=b=1\), the unique crossover is \(m_*=z\). At \(m=1/4\), Poisson disturbances give \(U_{\mathrm{Poi}}=0.16\), versus \(U_{\mathrm{per}}\approx0.105996084643\); at \(m=2\), the ordering reverses to \(U_{\mathrm{Poi}}=2/9\approx0.222222222222\) versus \(U_{\mathrm{per}}\approx0.296997075145\). With \(a=1,b=2\), \(m_*\approx0.607586231916\).

## Relationship to prior work
Ellner and Fussmann (2003) identify the distribution of successional stage durations as relevant to metapopulation persistence. Wilcox, Cairns and Possingham (2006) study stochastic patch turnover and show that the pattern, not just mean patch lifetime, affects persistence. Fraterrigo and Langille (2020) compare deterministic and stochastic disturbance simulations of mature-stage coverage. These contributions motivate the question but use spatial and/or multi-patch models, and do not provide this two-exponential **transient suitability** fixed-mean periodic-versus-Poisson one-crossing classification in the materials inspected. The renewal-reward formula and phase-type exponential convolution are standard; the claim here concerns the rigorous global one-crossing law, not those methods. It is a distinct functional of a single habitat's age, not a metapopulation survival-time result.

## Limitations
This is a mathematical benchmark for a deliberately idealized single patch. It does not establish that random disturbances generally improve species survival, nor that real disturbance clocks are memoryless, nor that observed populations immediately colonize a suitable patch. No results are asserted for longer chains of successional stages, spatially correlated disturbances, deterministic age-dependent hazards, or arbitrary renewal laws. Some older relevant papers were accessible only through abstracts, leaving residual historical-priority uncertainty; independent scientific validation has not been performed.

## References
- S. P. Ellner and G. Fussmann (2003), *Effects of successional dynamics on metapopulation persistence*, Ecology **84**, 882–889. https://doi.org/10.1890/0012-9658(2003)084[0882:EOSDOM]2.0.CO;2 (first published 2003-04-01).
- C. Wilcox, B. J. Cairns and H. P. Possingham (2006), *The role of habitat disturbance and recovery in metapopulation persistence*, Ecology **87**, 855–863. https://doi.org/10.1890/05-0587.
- J. M. Fraterrigo and A. B. Langille (2020), *Stochastic disturbance regimes alter patterns of ecosystem variability and recovery*, PLOS ONE **15**, e0229927. https://doi.org/10.1371/journal.pone.0229927.
- J. E. Keymer, P. A. Marquet, J. X. Velasco-Hernández and S. A. Levin (2000), *Extinction thresholds and metapopulation persistence in dynamic landscapes*, The American Naturalist **156**, 478–494. https://doi.org/10.1086/303407.
