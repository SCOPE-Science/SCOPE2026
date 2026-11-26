# Sharp convex-hull escape and singular consensus amplification in utility-weighted opinion dynamics

## Finding

Consider the noise-free specialization of the utility-driven bounded-confidence update introduced by Siebenmorgen and Restrepo [1]. The **universal convex-hull preservation threshold is exactly** \(\mu=1/2\): for any population size, any strictly positive opinion utility and any allowed sequence of interacting pairs, the initial opinion interval is preserved for \(0<\mu\leq1/2\). Conversely, for every \(1/2<\mu<1\), there is a two-agent population with positive exponential utility whose two opinions approach *the same limit strictly above both starting opinions*, even though their separation contracts at every step and remains inside the confidence bound.

The exponential-utility specialization has an exact two-parameter boundary, not just an existence example. Start at \(a<b\), let \(d=b-a\), take \(U(x)=e^{\lambda x}\) with \(\lambda>0\), and assume that the confidence threshold is strictly greater than \(d\). Write \(m_0=(a+b)/2\), \(\eta=\lambda d/2\), and let \(M_\infty\) be the deterministic consensus. Then, for every \(0<\mu<1\),

\[
M_\infty=m_0+d\mu\sum_{k=0}^{\infty}r^k\tanh(\eta r^k),\qquad r=|1-2\mu|.
\]

For \(1/2<\mu<1\), define \(F(\mu,\eta)=\mu\sum_{k\geq0}(2\mu-1)^k\tanh(\eta(2\mu-1)^k)\). The right endpoint is exceeded precisely when \(F(\mu,\eta)>1/2\). For each fixed \(\eta>0\), there is a unique \(\mu_*(\eta)\in(1/2,1)\) satisfying \(F(\mu_*,\eta)=1/2\). For each fixed \(\mu\in(1/2,1)\), there is a unique \(\eta_*(\mu)>0\) satisfying the same equation. Below, at, and above this boundary the consensus lies respectively below, at, and above the initial maximum \(b\). The critical curve \(\eta_*(\mu)\) is strictly decreasing and has the two endpoint laws

\[
\eta_*(\mu)\sim\tfrac12\log\frac1{\mu-1/2}\quad(\mu\downarrow1/2),
\qquad
\eta_*(\mu)\sim2(1-\mu)\quad(\mu\uparrow1).
\]

For each *fixed* \(\lambda d>0\), there is an unbounded deterministic consensus displacement as \(\mu\uparrow1\), with the exact singular coefficient

\[
\lim_{\mu\uparrow1}(1-\mu)(M_\infty-m_0)
=\frac1\lambda\log\cosh\!\left(\frac{\lambda d}{2}\right)>0.
\]

For instance, begin at \(a=0\), \(b=1\), use \(U(x)=3^x\), confidence threshold \(\varepsilon>1\), and learning rate \(\mu=3/4\). The two opinions reach consensus at \(M_\infty=1.009641160060\ldots>1\). This strict escape is certified already by three positive terms of the exact series, using only rational inequalities and radicals, as shown below.

## Assumptions and scope

For a finite set of real-valued opinions, at an interaction between distinct agents \(i,j\) with \(|x_i-x_j|<\varepsilon\), both update simultaneously, without additive noise:

\[
x_i^+=x_i+2\mu\frac{U(x_j)}{U(x_i)+U(x_j)}(x_j-x_i),\qquad
x_j^+=x_j+2\mu\frac{U(x_i)}{U(x_i)+U(x_j)}(x_i-x_j).
\]

Here \(0<\mu<1\), \(\varepsilon>0\), and \(U:\mathbb R\to(0,\infty)\). Pairs not satisfying the strict confidence condition do not interact. Universal convex-hull preservation concerns this zero-noise pairwise rule on any finite population, with arbitrary pair-selection sequence. The exact limit, threshold curve and asymptotic laws concern exactly two agents, the single always-compatible pair, and the positive exponential utility specified above. No population-scale stochastic or diffusion approximation is used.

A two-agent initial gap \(d<\varepsilon\) stays compatible forever, because the gap is multiplied by \(1-2\mu\) at each step. The two-agent result therefore applies to the original *bounded-confidence* rule rather than to a different unconditional-averaging model.

## Proof

**1. Sharp universal preservation half-threshold.** Each interacting opinion is a convex combination of its two pre-interaction values when \(2\mu\leq1\), since the two weights are strictly between zero and one. Consequently no new opinion can leave the interval between the global minimum and maximum of the initial opinions. The argument is independent of network, utility shape, and pair-selection order. Sharpness for every \(\mu>1/2\) follows from Steps 2–4.

**2. Exact two-agent reduction.** Put \(m=(x_1+x_2)/2\) and \(z=x_2-x_1\), allowing \(z\) to change sign after an over-relaxed update. The update identities give

\[
z^+=(1-2\mu)z,
\qquad
m^+-m=\mu z\,\frac{U(m+z/2)-U(m-z/2)}{U(m+z/2)+U(m-z/2)}.
\]

For \(U(x)=e^{\lambda x}\), the fraction equals \(\tanh(\lambda z/2)\). Thus \(z_k=(1-2\mu)^kd\) and

\[
m_{k+1}-m_k=\mu z_k\tanh(\lambda z_k/2)
=\mu d r^k\tanh(\eta r^k)>0.
\]

The final equality also holds for negative \(z_k\), since \(\tanh\) is odd. Because \(\tanh(s)\leq s\) for \(s\geq0\), the series is bounded above by \(\mu d\eta/(1-r^2)\); it converges absolutely for \(r<1\). Hence both opinions converge to the common limit displayed under Finding. In particular, a contracting gap does **not** imply that the consensus lies inside the initial hull.

**3. Unique threshold and its universal sharpness.** For \(\mu>1/2\), \(r=2\mu-1\). Each term of \(F(\mu,\eta)\) is nonnegative and nondecreasing in either argument; the first term \(\mu\tanh\eta\) gives strict increase in both. The series converges locally uniformly for \(\mu<1\), so \(F\) is continuous. At fixed \(\eta>0\), \(F(1/2,\eta)=\frac12\tanh\eta<1/2\). Step 5 proves \(F(\mu,\eta)\to\infty\) as \(\mu\uparrow1\). Thus the unique crossing \(\mu_*(\eta)\) exists. At fixed \(\mu>1/2\), \(F(\mu,0)=0\), whereas monotone convergence gives

\[
\lim_{\eta\to\infty}F(\mu,\eta)
=\frac{\mu}{1-(2\mu-1)}=\frac{\mu}{2(1-\mu)}>\frac12.
\]

This proves the unique crossing \(\eta_*(\mu)\), its strict decrease, and the complete location classification. It also proves sharpness for every \(\mu>1/2\), since some sufficiently steep exponential utility leads to escape.

**4. Endpoint behavior of the threshold curve.** Put \(\delta=\mu-1/2\downarrow0\), so \(r=2\delta\). Let \(\eta_0=\operatorname{artanh}(1/(2\mu))=\frac12\log((1+\delta)/\delta)\). The first term of \(F\) attains \(1/2\) at \(\eta_0\), so \(\eta_*\leq\eta_0\). The remaining terms obey

\[
0\leq F(\mu,\eta)-\mu\tanh\eta
\leq\frac{\mu\eta r^2}{1-r^2}.
\]

For any fixed \(0<c<1\), taking \(\eta=c\eta_0\) makes the deficit \(1/2-\mu\tanh(c\eta_0)\) of order \(\delta^c\), while the displayed remainder is \(O(\delta^2\log(1/\delta))\). Hence \(F(\mu,c\eta_0)<1/2\) for sufficiently small \(\delta\), and \(c\eta_0<\eta_*<\eta_0\). Letting \(c\uparrow1\) proves \(\eta_*\sim\frac12\log(1/\delta)\).

For \(\mu\uparrow1\), write \(h=1-\mu\), and use \(s-s^3/3\leq\tanh s\leq s\) for all \(s\geq0\). Summing the resulting geometric series gives

\[
\frac{\eta}{4h}-\frac{\mu\eta^3}{3(1-r^4)}
\leq F(\mu,\eta)\leq\frac{\eta}{4h},\qquad r=2\mu-1.
\]

At \(F=1/2\), the upper bound implies \(\eta_*\geq2h\). For every fixed \(c>1\), substituting \(\eta=2ch\) into the lower bound yields \(F\geq c/2-O(h^2)>1/2\) as \(h\downarrow0\), so \(\eta_*<2ch\). Letting \(c\downarrow1\) gives \(\eta_*\sim2h\).

**5. Singular amplification near unit learning.** Fix \(\lambda d>0\) and put \(r=2\mu-1\), \(\tau=-\log r\). The elementary Riemann-sum limit for the continuous integrable function \(g(u)=e^{-u}\tanh(\eta e^{-u})\) reads

\[
\tau\sum_{k\geq0}r^k\tanh(\eta r^k)
\longrightarrow\int_0^\infty e^{-u}\tanh(\eta e^{-u})\,du
=\frac{\log\cosh\eta}{\eta}.
\]

Since \((1-\mu)/\tau\to1/2\), multiplication by \(\mu d(1-\mu)\) gives the stated positive limit \(\log\cosh\eta/\lambda\). Thus consensus displacement diverges like \((1-\mu)^{-1}\), although \(z_k\to0\) for every fixed \(\mu<1\).

**6. Exact strict escape example.** With \(d=1\), \(\mu=3/4\), \(\lambda=\log3\), \(r=1/2\), and \(\eta=(\log3)/2\), the first three summands of \(F\) are

\[
\frac34\left[\frac12+\frac12(2-\sqrt3)+
\frac14\frac{3^{1/4}-1}{3^{1/4}+1}\right].
\]

The elementary integer inequalities \(26^2>3\cdot15^2\) and \(3\cdot13^4>17^4\) imply respectively \(2-\sqrt3>4/15\) and \((3^{1/4}-1)/(3^{1/4}+1)>2/15\). Hence these *three* summands total strictly more than

\[
\frac34\left[\frac12+\frac12\frac4{15}+\frac14\frac2{15}\right]=\frac12.
\]

All later summands are positive, so \(M_\infty>1\) is proved without reliance on a floating-point computation.

## Verification

Run the supplied standalone `verify.py` with Python 3. It checks the exact integer inequalities in Step 6, evaluates the convergent series with a mathematically derived upper tail bound \(\mu\eta r^{2K}/(1-r^2)\), solves for the two equivalent threshold parameters, reproduces finite pair updates, and compares the limiting laws at several parameter values. In the exact example, the computed consensus is \(1.009641160060\ldots\), the fixed-utility critical learning rate is \(0.745320731512\ldots\), and the critical utility parameter at \(\mu=3/4\) is \(\eta_*=0.537281449977\ldots\).

Numerical computations are supplementary checks; the universal half-threshold, existence and uniqueness of the boundary, its endpoint laws, and the singular limit are established by Steps 1–6. The truncated series bound is valid for each fixed \(\mu<1\), and no finite truncation is used as proof of the singular limit.

## Relationship to prior work

Siebenmorgen and Restrepo [1] define precisely this utility-asymmetric pair update (their Equation 1), establish its utility-independent gap-contraction identity (their Equation 2), and study stochastic mean-opinion drift, approximate Gibbs stationary densities, well switching, and cluster merging. Their complete accessible main text and supplementary derivations do not state the deterministic exact consensus series, the sharp convex-hull frontier, the two-parameter escape boundary, or its singular asymptotics. The gap contraction identity from [1] is explicitly used here; its independent discovery is not claimed.

Classical Deffuant compromise and related bounded-confidence theory commonly restrict compromise weights so that paired opinions remain convex combinations. Lanchier and Mercer [2], in particular, analyze attraction with \(\mu_-\leq1/2\), and a separate repulsive mechanism acting on *incompatible* pairs. Their results are not the utility-asymmetric over-relaxed attraction mechanism treated here. The review [3] describes the standard convex-hull behavior in conventional averaging-based opinion models; the present theorem locates a model-specific boundary of that property.

The mathematical contribution is the **exact long-run phase classification and blow-up law**, not the elementary observation that a single over-relaxed pair update may overshoot, and not a claim that all bounded-confidence models lose convex-hull preservation.

## Limitations

This is a deterministic, two-agent classification plus a universal finite-population convex-hull statement. It does not describe stochastic trajectories with nonzero additive noise, stationary distributions of the noisy model, populations of three or more agents beyond the universal preservation threshold, or empirical opinion formation. For other utilities, the exact series and threshold curve need not apply; for exponential utility, the consensus value may lie arbitrarily far outside the initial opinion interval as \(\mu\uparrow1\). Historical and bibliographic searches cannot exclude every equivalent result in unindexed literature.

## References

[1] Alex Siebenmorgen and Juan G. Restrepo, *A Utility-Driven Bounded-Confidence Model for Opinion Dynamics*, arXiv:2605.21844v1, publicly submitted May 21, 2026. https://arxiv.org/html/2605.21844v1

[2] Nicolas Lanchier and Max Mercer, *Deffuant opinion dynamics with attraction and repulsion*, arXiv:2310.19073 (2023 preprint; 2024 journal publication). https://arxiv.org/abs/2310.19073

[3] Carmela Bernardo, Claudio Altafini, Anton Proskurnikov, and Francesco Vasca, *Bounded confidence opinion dynamics: A survey*, Automatica **159** (2024), article 111302, DOI:10.1016/j.automatica.2023.111302. The accessible abstract and excerpts on convex-hull preservation and additive-noise disturbance were consulted; the complete publisher-hosted text was not accessible.
