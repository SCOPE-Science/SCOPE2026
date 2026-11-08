# Sharp rare-energy tails and finite-size edge smoothing in a switching harmonic gas

## Finding

Consider the stationary switching-trap gas defined below, and its empirical quadratic position energy \(E_N=N^{-1}\sum_{i=1}^N X_i^2\). Its density \(f_N(s)\) has a three-region large-deviation rate, two distinct endpoint-dependent algebraic prefactors outside the typical energy interval, and exact \(N^{-1/2}\)-wide smoothing profiles at both ends of that interval.

Set
\[
 a=\frac{D}{\mu_1},\quad b=\frac{D}{\mu_2},\quad \Delta=b-a,\quad
 p=\frac{r_1}{2\mu_1},\quad q=\frac{r_2}{2\mu_2},\quad
 \bar v=a+\frac{\Delta p}{p+q},\quad B=B(p,q).
\]
Define the nonnegative mixing density, supported on \((a,b)\),
\[
 g(v)=\frac{v}{\bar v B\Delta}
 \left(\frac{v-a}{\Delta}\right)^{p-1}
 \left(\frac{b-v}{\Delta}\right)^{q-1},
\]
and the conditional energy rate
\[
 I(s\mid v)=\frac12\left(\frac{s}{v}-1-\log\frac{s}{v}\right)
 \qquad(s,v>0).
\]
The mixing law and conditional independence are known from [1]; their application to sharp empirical quadratic-energy tails below is the subject of this finding.

**Exact finite-size formula.** For every integer \(N\ge1\) and \(s>0\),
\[
 f_N(s)=\frac{(N/2)^{N/2}s^{N/2-1}}{\Gamma(N/2)}
 \int_a^b g(v)v^{-N/2}\exp\!\left(-\frac{Ns}{2v}\right)dv.
\]

**Three-region rate.** The variables \(E_N\) obey a good large-deviation principle at speed \(N\), with rate
\[
 J(s)=\begin{cases}
 +\infty,&s\le0,\\
 I(s\mid a),&0<s<a,\\
 0,&a\le s\le b,\\
 I(s\mid b),&s>b.
 \end{cases}
\]
For fixed \(s\in(a,b)\), the density converges to \(g(s)\), a consequence of the conditional-i.i.d. sum principle already present in [2].

**Sharp out-of-support density laws.** Introduce
\[
 c_- =\frac{a}{\bar v B\Delta^p},\qquad
 c_+ =\frac{b}{\bar v B\Delta^q},\qquad
 k_-(s)=\frac{a-s}{2a^2},\quad
 k_+(s)=\frac{s-b}{2b^2}.
\]
For each fixed \(0<s<a\),
\[
 f_N(s)\sim \frac{c_-\Gamma(p)}{2\sqrt\pi\,s\,[k_-(s)]^p}
 N^{1/2-p}\exp[-N I(s\mid a)].
\]
For each fixed \(s>b\),
\[
 f_N(s)\sim \frac{c_+\Gamma(q)}{2\sqrt\pi\,s\,[k_+(s)]^q}
 N^{1/2-q}\exp[-N I(s\mid b)].
\]
The corresponding one-sided threshold probabilities have the same exponential rates, but powers \(N^{-p-1/2}\) and \(N^{-q-1/2}\), respectively; their leading constants are obtained by dividing the above density prefactors by \((a-s)/(2sa)\) and \((s-b)/(2sb)\), respectively.

**Finite-size endpoint profiles.** For any fixed real \(z\), locally uniformly as \(z\) varies over compact subsets of \(\mathbb R\),
\[
 \lim_{N\to\infty}N^{(p-1)/2}f_N\!\left(a+\frac{z}{\sqrt N}\right)
 =\frac{c_-}{2\sqrt\pi\,a}
 \int_0^\infty y^{p-1}\exp\!\left[-\frac{(z-y)^2}{4a^2}\right]dy,
\]
\[
 \lim_{N\to\infty}N^{(q-1)/2}f_N\!\left(b+\frac{z}{\sqrt N}\right)
 =\frac{c_+}{2\sqrt\pi\,b}
 \int_0^\infty y^{q-1}\exp\!\left[-\frac{(z+y)^2}{4b^2}\right]dy.
\]
In particular,
\[
 f_N(a)\sim\frac{c_-\Gamma(p/2)(2a)^p}{4\sqrt\pi\,a}N^{(1-p)/2},
\quad
 f_N(b)\sim\frac{c_+\Gamma(q/2)(2b)^q}{4\sqrt\pi\,b}N^{(1-q)/2}.
\]
Consequently, the finite-size density at the lower edge diverges, remains of positive constant order, or vanishes according as \(p<1\), \(p=1\), or \(p>1\); the corresponding upper-edge criterion is \(q<1\), \(q=1\), or \(q>1\). The algebraic powers of the far tails independently expose the two dimensionless switching rates, despite their common exponential rate being independent of them.

## Assumptions and scope

For every integer \(N\ge1\), take positive parameters \(D,r_1,r_2,\mu_2\) and \(\mu_1>\mu_2\). Let \(S_t\in\{1,2\}\) be an autonomous irreducible continuous-time Markov chain switching \(1\to2\) at rate \(r_1\) and \(2\to1\) at rate \(r_2\). Let \(B_1,\ldots,B_N\) be independent standard Brownian motions, independent of \(S\). The particle dynamics are
\[
 dX_i(t)=-\mu_{S_t}X_i(t)dt+\sqrt{2D}\,dB_i(t),\qquad i=1,\ldots,N.
\]
Take the unique stationary law obtained from the infinite-past stochastic convolution. All density asymptotics are for fixed \(s>0\) unless the displayed critical scaling fixes \(z=O(1)\). In particular, no asserted uniformity extends to \(s\downarrow0\), \(s\to\infty\), or simultaneous parameter limits. The observable is the mean squared **position**, not energy defined with the instantaneous trap stiffness.

## Proof

**1. Stationary random variance.** The infinite-past solution is conditionally centered Gaussian, independent across the particles given the entire environment trajectory. Its common conditional variance is
\[
 V_t=2D\int_{-\infty}^{t}\exp\!\left(-2\int_u^t\mu_{S_w}dw\right)du.
\]
It satisfies the piecewise-deterministic equation \(\dot V=2(D-\mu_{S_t}V)\) and lies in \((a,b)\) in stationarity. Writing \(h_j(v)\) for the stationary joint phase-variance densities, their fluxes are \(j_1=-2\mu_1(v-a)h_1\) and \(j_2=2\mu_2(b-v)h_2\). Zero total flux implies \(j_1=-H\), \(j_2=H\). The phase-one stationary equation gives
\[
 \frac{H'(v)}{H(v)}=\frac{p}{v-a}-\frac{q}{b-v}.
\]
Therefore \(H(v)\) is proportional to \((v-a)^p(b-v)^q\), and
\[
 h_1(v)+h_2(v)=\frac{H(v)}2
 \left[\frac1{\mu_1(v-a)}+\frac1{\mu_2(b-v)}\right]
 \propto v(v-a)^{p-1}(b-v)^{q-1}.
\]
Beta integration normalizes the density to the displayed \(g(v)\). This matches [1, Eqs. (12)--(13)]. No endpoint atoms occur because both switching rates are positive.

**2. Exact conditional law.** Given \(V=v\), the variables \(X_i/\sqrt v\) are independent standard normals. Thus \(NE_N/v\) has the \(\chi_N^2\) law. Mixing the gamma density over \(g\) yields the exact displayed integral.

**3. Uniform conditional saddle factor.** Stirling's formula at fixed \(s>0\) gives, independently of \(v\in[a,b]\),
\[
 f_N(s\mid v)=\frac{\sqrt N}{2\sqrt\pi\,s}
 e^{-NI(s\mid v)}\bigl(1+O(N^{-1})\bigr).
\]
Differentiating \(I\) with respect to \(v\) gives \(\partial_v I(s\mid v)=(v-s)/(2v^2)\). Its minimizer over \([a,b]\) is \(a\) for \(s<a\), \(s\) for \(a<s<b\), and \(b\) for \(s>b\). Uniform conditional Cramér bounds together with compactness of the variance interval give the good large-deviation principle and its stated rate; the mixing density puts positive mass in every open subinterval of \((a,b)\). The point \(s=0\) has infinite rate, since the conditional \(\chi_N^2\) lower tails vanish superexponentially as a neighborhood of zero shrinks.

**4. Fixed-energy endpoint Laplace method.** As \(v\downarrow a\), \(g(v)\sim c_-(v-a)^{p-1}\); as \(v\uparrow b\), \(g(v)\sim c_+(b-v)^{q-1}\). If \(s<a\), then \(I(s\mid a+t)=I(s\mid a)+k_-(s)t+O(t^2)\). Watson's lemma therefore supplies \(\Gamma(p)[Nk_-(s)]^{-p}\). If \(s>b\), the substitution \(t=b-v\) analogously supplies \(\Gamma(q)[Nk_+(s)]^{-q}\). Combining with step 3 establishes both fixed-tail density formulas. For the one-sided tail probabilities, the outer integration in \(s\) is another one-sided Laplace integral with positive slope \((s-b)/(2sb)\) above \(b\) or slope magnitude \((a-s)/(2sa)\) below \(a\); this introduces one extra factor \(N^{-1}\).

**5. Critical edges.** Set \(s=a+z/\sqrt N\), \(v=a+y/\sqrt N\) at the lower edge. For fixed \(y\ge0\) and bounded \(z\),
\[
 NI(s\mid v)\longrightarrow\frac{(z-y)^2}{4a^2},\qquad
 N^{p/2}g(a+y/\sqrt N)\,dv\longrightarrow c_-y^{p-1}dy.
\]
Here \(dv=dy/\sqrt N\), and the displayed measure limit follows from the endpoint power law. To justify dominated convergence, separate \(v\in[a,a+\epsilon]\) from the exponentially suppressed complementary interval. On the first portion, convex quadratic lower bounds for \(I\) near its unique minimizer give an integrable bound of the form \(C y^{p-1}e^{-c(y-M)^2}\) on compact \(|z|\le M\); the same argument works at \(b\). The Gaussian integral profiles follow. Evaluating them at \(z=0\) uses \(\int_0^\infty y^{\theta-1}e^{-y^2/(4t^2)}dy=(2t)^\theta\Gamma(\theta/2)/2\), proving the edge exponents and constants.

**6. Interior.** For \(s\in(a,b)\), the unique nondegenerate interior minimizer \(v=s\) has \(\partial_v^2 I(s\mid s)=1/(2s^2)\). The standard interior Laplace factor cancels the prefactor in step 3 and gives \(f_N(s)\to g(s)\), consistent with the published conditional-sum limit [2].

## Verification

The accompanying standalone `CHECK.py` numerically evaluates the exact finite-size gamma-mixture density by adaptive quadrature, independently computes the analytic asymptotic constants, and compares both tails and both critical edges for two regimes with \(p<1<q\) and \(q<1<p\). It also checks mixing normalization and the first three exact moments against beta-function expressions. Run `python CHECK.py` after installing the package listed in `requirements.txt`. Its 40 assertions are finite diagnostics, not a replacement for the endpoint Laplace proof.

## Relationship to prior work

Biroli, Kulkarni, Majumdar and Schehr [1] derive exactly the shared-variance, conditionally independent Gaussian stationary law for the same switching harmonic gas, as well as particle order statistics, extreme values and their finite-support shapes. Their supplement also treats full counting statistics and explicitly identifies the \(p=1\) and \(q=1\) endpoint-singularity transitions for *order-statistic* scaling functions; those exponent thresholds are not themselves new. The Gaussian mixing density and stationary particle correlations are therefore **not new claims** here. Biroli, Larralde, Majumdar and Schehr [2] give a general large-sample conditional-i.i.d. sum limit (Sec. III.A and its appendix), which already implies the interior weak limit for this quadratic observable. Their work does not present the two explicit out-of-support quadratic-energy rare-event powers, the associated rate-independent switching-rate diagnostics, or the finite-\(N\) quadratic-energy edge profiles analyzed above. Those statements require the separate chi-square saddle and endpoint calculations. The novelty claim is qualified: the new formulas are derived from the previously known joint stationary law, and a broader unindexed asymptotic treatment could imply them.

## Limitations

These results concern a fixed-time stationary snapshot, not the time-integrated work or heat, first-passage energies, or dynamical trajectory large deviations. The independent Brownian noises share only the environmental switching process; direct interactions and spatially varying trap curvature are outside scope. For \(s\) tending to \(0\) or infinity with \(N\), and for simultaneous limits in \(D,\mu_j,r_j\), no uniform error estimate is supplied. Numerical checks at finitely many parameters do not prove the theorems. Scientific priority remains subject to comparison with any unindexed general results on sharp Gaussian-scale-mixture tails. Independent scientific validation has not been performed.

## References

[1] M. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570, first publicly posted 2023-12-05; https://arxiv.org/abs/2312.02570. Main equations (12)--(14) and supplementary mixture/counting-statistics analysis.

[2] M. Biroli, H. Larralde, S. N. Majumdar and G. Schehr, *Exact extreme, order and sum statistics in a class of strongly correlated system*, arXiv:2307.15351, first publicly posted 2023-07-28; https://arxiv.org/abs/2307.15351. Section III.A, Eq. (18), and sum-statistics appendix.
