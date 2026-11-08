# Exact bivariate local-time synchronization before absorption

## Finding

Two interior observation sites in an absorbing, Poisson-reset Brownian system have an exact bivariate exponential occupation-density law. Fix \(D>0\), \(r>0\), and \(0<a<b\le R\). Put
\[
k=\sqrt{r/D},\qquad A=\frac{\sinh(ka)}{Dk},\qquad B=\frac{\sinh(kb)}{Dk},\qquad \eta=\frac{\sinh(k(b-a))}{\sinh(kb)}.
\]
For the two local times \(L_a,L_b\), defined below, their joint Laplace transform is exactly
\[
\boxed{\mathbb E_R[e^{-sL_a-tL_b}]=\frac{1}{1+As+Bt+\eta ABst}},\qquad s,t\ge0.
\]
Consequently both marginals are exponential, with means \(A\) and \(B\), and
\[
\boxed{\operatorname{Corr}(L_a,L_b)=1-\frac{\sinh(k(b-a))}{\sinh(kb)}}.
\]
The *entire* joint law is independent of the resetting location \(R\), as long as \(R\ge b\). The correlation is strictly increasing in the resetting rate \(r\), with
\[
\lim_{r\downarrow0}\operatorname{Corr}(L_a,L_b)=\frac ab,
\qquad\lim_{r\to\infty}\operatorname{Corr}(L_a,L_b)=1.
\]
At fixed \(0<a<b\), the large-rate decorrelation gap obeys \(1-\operatorname{Corr}(L_a,L_b)\sim e^{-a\sqrt{r/D}}\). More strongly,
\[
\left(\frac{L_a}{A},\frac{L_b}{B}\right)\Longrightarrow (E,E)
\quad\text{as }r\to\infty,
\]
where \(E\) is one mean-one exponential random variable.

## Assumptions and scope

The process \(X\) starts at \(X_0=R\) on \((0,\infty)\). Between resets it has generator \(D\partial_{xx}\) (equivalently, volatility \(\sqrt{2D}\)). Independently, a rate-\(r\) Poisson clock instantaneously sets its position to \(R\). The process is killed at \(\tau_0=\inf\{t\ge0:X_t=0\}\). Each independent excursion from \(R\) has a strictly positive probability \(e^{-kR}\) of hitting zero before its next reset; hence \(\tau_0<\infty\) almost surely. Local times are normalized as occupation *densities in physical time*: for \(c\in\{a,b\}\),
\[
L_c=\lim_{\varepsilon\downarrow0}\frac1{2\varepsilon}
\int_0^{\tau_0}\mathbf1_{\{|X_t-c|<\varepsilon\}}\,dt,
\]
using the continuous occupation-density version on each Brownian excursion. An instantaneous reset jump contributes no local time. These are not semimartingale-Tanaka local times; the two normalizations differ by the factor \(2D\).

The assertions concern \(r>0\), \(0<a<b\le R\), positive diffusivity, and Poisson resetting to a *fixed* point. The stated limits at \(r=0\) and \(r=\infty\) are limits of this model, not claims of resetting at those endpoints.

## Proof

**1. Killed Brownian Green kernel.** Let a Brownian excursion be stopped at the first of absorption at zero or an independent exponential clock of rate \(r\). Its absorption-before-reset probability from \(x>0\) is \(q(x)=e^{-kx}\). The resolvent occupation-density kernel is
\[
G_r(x,y)=\frac{e^{-k|x-y|}-e^{-k(x+y)}}{2Dk},\qquad x,y>0.
\]
For the complete resetting process, a first-cycle decomposition and renewal at \(R\) give the expected total occupation density
\[
U(x,y)=G_r(x,y)+(1-q(x))\frac{G_r(R,y)}{q(R)}.
\]
Indeed, a first-cycle reset has probability \(1-q(x)\). The future mean occupation from \(R\) is \(G_r(R,y)/q(R)\), since an independent cycle from \(R\) succeeds (absorbs) with probability \(q(R)>0\).

**2. Exact two-site occupation matrix.** Using \(a<b\le R\) in the preceding explicit kernel yields
\[
\begin{array}{c|cc}
 & y=a&y=b\\ \hline
x=R&A&B\\
x=a&A&(1-\eta)B\\
x=b&A&B
\end{array}.
\]
For example, for \(y\le R\), \(G_r(R,y)=e^{-kR}\sinh(ky)/(Dk)\); substitution in \(U(R,y)\) gives \(\sinh(ky)/(Dk)\). For \(x=a,y=b\), the same identities reduce \(U(a,b)\) to \(B[1-\sinh(k(b-a))/\sinh(kb)]\). These identities do not require \(R>b\); equality \(R=b\) is valid.

**3. Feynman–Kac at two point potentials.** Write \(F_x=\mathbb E_x[e^{-sL_a-tL_b}]\) for nonnegative \(s,t\). The occupation-resolvent identity for point killing gives
\[
F_x=1-sU(x,a)F_a-tU(x,b)F_b.
\]
In particular,
\[
(1+sA)F_a+t(1-\eta)BF_b=1,\qquad
sAF_a+(1+tB)F_b=1.
\]
The displayed occupation matrix also implies \(F_R=F_b\). The determinant of the two-by-two system is \(1+As+Bt+\eta ABst>0\); solving the second component gives
\[
F_R=F_b=\frac1{1+As+Bt+\eta ABst}.
\]
The positive Green operator guarantees the gauge identity, alternatively obtainable first for smooth narrow killing functions then by occupation-density convergence. This establishes the full joint law for all \(s,t\ge0\).

**4. Moments and monotonicity.** Differentiating the transform at the origin gives \(\mathbb E L_a=A\), \(\mathbb E L_b=B\), \(\operatorname{Var}L_a=A^2\), \(\operatorname{Var}L_b=B^2\), and \(\operatorname{Cov}(L_a,L_b)=(1-\eta)AB\). Thus the correlation is \(1-\eta\). For fixed \(0<a<b\),
\[
\frac{d}{dk}\log\eta=(b-a)\coth(k(b-a))-b\coth(kb)<0,
\]
because \(z\mapsto z\coth z\) increases strictly for positive \(z\): its derivative equals \((\sinh z\cosh z-z)/\sinh^2z>0\). As \(k\) increases strictly with \(r\), the correlation increases strictly. Small-argument hyperbolic expansions give the limit \(a/b\). For large \(k\),
\[
\eta=e^{-ka}\frac{1-e^{-2k(b-a)}}{1-e^{-2kb}}\sim e^{-ka}.
\]
Finally, substitute \(s/A,t/B\) into the joint transform. The normalized transform is \([1+s+t+\eta st]^{-1}\), which tends to \([1+s+t]^{-1}\), the joint Laplace transform of \((E,E)\). Continuity of multivariate Laplace transforms proves the asserted weak convergence.

## Verification

The companion standalone \(\texttt{verify.py}\) computes the continuum transform from its closed form and separately solves finite-state birth–death/reset Feynman–Kac equations using a tridiagonal solver. The discretization has absorbing state zero, a distant reflecting upper boundary, diffusion jump rates \(D/h^2\), resetting at \(R\), and occupation-density approximations \(\text{time at site}/h\). Comparisons at three diffusion/reset parameter sets and several mesh sizes display convergence toward the stated continuum law. Additional direct Green-kernel identities, correlation monotonicity, endpoint bounds, and normalized transform checks are evaluated by the script. Run with \(\texttt{python3 verify.py}\); it requires only the Python standard library. This numerical evidence is corroborative, not a substitute for the analytic proof above.

## Relationship to prior work

Pal, Chatterjee, Reuveni and Kundu (2019) study single-site local time under stochastic resetting at a fixed observation horizon and discuss spatial correlation as a prospective direction. Singh and Pal (2022) treat first-passage Brownian functionals with resetting, including local time at the reset point, but not the present two-distinct-site joint law below the reset location. Li and Zhou (2017) treat joint local times of spectrally negative Lévy processes stopped at first passage; deterministic-reset jumps yield a state-dependent jump kernel, not a spatially homogeneous Lévy process. Marcus and Rosen (2023) provide broad Markov-process rebirth/permanental local-time theory, which may be useful for alternative derivations, but the explicit parameter-dependent transform and strict monotonicity stated here are not identified in the inspected material. No claim is made that absence of a text match proves publication priority.

## Limitations

The statement does not cover more than two observation sites, resetting sites lying between the sensors, arbitrary reset-time distributions, non-Poisson clocks, non-Brownian spatial motion, or the joint fluctuations of finite-width reactive detectors without passing to their occupation-density limit. The exact law is a specialization of general Green-function/Kac-resolvent machinery; implicit derivability from broader results remains a literature-priority risk. The proof is mathematical, not an experimentally validated sensor protocol. No independent external scientific audit has been performed.

## References

1. A. Pal, S. Chatterjee, S. Reuveni, and A. Kundu, *Local time of diffusion with stochastic resetting*, arXiv:1902.00907v1 (2019), https://arxiv.org/abs/1902.00907 .
2. P. Singh and A. Pal, *First-passage Brownian functionals with stochastic resetting*, arXiv:2202.02715v1 (2022), https://arxiv.org/abs/2202.02715 .
3. B. Li and X. Zhou, *Local times for spectrally negative Lévy processes*, arXiv:1705.01289v1 (2017), https://arxiv.org/abs/1705.01289 .
4. M. B. Marcus and J. Rosen, *Law of the iterated logarithm for k/2-permanental processes and the local times of related Markov processes*, arXiv:2302.10262v1 (2023), https://arxiv.org/abs/2302.10262 .
