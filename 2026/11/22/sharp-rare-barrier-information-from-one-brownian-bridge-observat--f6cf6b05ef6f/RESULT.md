# Sharp rare-barrier information from one Brownian-bridge observation

## Finding

Let \(B\) be the standard zero-to-zero Brownian bridge on \([0,1]\), \(M=\sup_{0\le s\le1}B_s\), and \(E_h=\mathbf1_{\{M>h\}}\) for \(h>0\). A single exact observation is taken at a deterministic time \(t\in(0,1)\). Its explained mean-square information is
\[
I_h(t)=\operatorname{Var}\!\left(\mathbb E[E_h\mid B_t]\right),
\]
so that the minimum mean-square estimation risk is \(e^{-2h^2}(1-e^{-2h^2})-I_h(t)\).

Write \(v=t(1-t)\), \(b=1-t\), and let \(\Phi\) denote the standard Gaussian distribution function. For all \(h>0\), the midpoint has the exact second moment
\[
\mathbb E\!\left[\mathbb E[E_h\mid B_{1/2}]^2\right]
=5\Phi(-2h)-4e^{6h^2}\Phi(-4h)+e^{16h^2}\Phi(-6h),
\]
with \(I_h(1/2)\) obtained by subtracting \(e^{-4h^2}\). As \(h\to\infty\), for each **fixed** \(0<t\le1/2\),
\[
I_h(t)\sim
\begin{cases}
\exp\!\left[-\dfrac{4(1-2t)}{1-t}h^2\right],&0<t<1/4,\\[4pt]
\dfrac12 e^{-8h^2/3},&t=1/4,\\[4pt]
\dfrac{\sqrt v}{h\sqrt{2\pi}}\,C(t)\,e^{-h^2/(2v)},&1/4<t\le1/2,
\end{cases}
\]
where
\[
C(t)=\frac{10}{3}+\frac1{4t-1}+\frac1{4(1-t)-1}
-\frac2{2t+1}-\frac2{2(1-t)+1}.
\]
For \(1/2<t<1\), use \(I_h(t)=I_h(1-t)\). In particular
\[
\frac{I_h(1/2)}{\operatorname{Var}(E_h)}
\sim \frac{5}{3h\sqrt{2\pi}},
\]
whereas this fraction decreases exponentially in \(h^2\) at every other fixed interior time. The unique **fixed-time exponential-rate maximizer** of \(I_h(t)\) is the midpoint; no finite-threshold global optimal-time claim is made.

## Assumptions and scope

The bridge is centered, continuous, Gaussian, has covariance \(\min(s,u)-su\), and is pinned at both endpoints. The observation is a single noiseless real-valued \(B_t\), chosen deterministically before seeing the path; the target is the one-sided strict barrier-crossing indicator. For the rare-barrier limits, \(t\) remains fixed as \(h\to\infty\). A conditional-mean estimator is used under squared loss. The threshold can be any strictly positive real number. The displayed asymptotic equivalents exclude the deterministic endpoints \(t=0,1\), where the explained information is zero for all \(h\).

## Proof

**Conditional event law.** The reflection principle for a Brownian bridge from endpoints \(a_0,a_1<h\) over duration \(\Delta\) gives crossing probability \(\exp[-2(h-a_0)(h-a_1)/\Delta]\). Given \(B_t=y<h\), the bridge pieces on \([0,t]\) and \([t,1]\) are conditionally independent. Therefore, for \(y<h\),
\[
g_{h,t}(y):=\mathbb P(M>h\mid B_t=y)
=e^{-2h(h-y)/t}+e^{-2h(h-y)/(1-t)}-e^{-2h(h-y)/v}.
\]
For \(y\ge h\), \(g_{h,t}(y)=1\). Since \(Y=B_t\sim N(0,v)\), \(\mathbb E[g_{h,t}(Y)]=\mathbb P(M>h)=e^{-2h^2}\), and \(I_h(t)=\mathbb E[g_{h,t}(Y)^2]-e^{-4h^2}\).

**Exact midpoint.** At \(t=1/2\), \(g_{h,t}(y)=2e^{-4h(h-y)}-e^{-8h(h-y)}\) for \(y<h\). For \(Y\sim N(0,v)\), Gaussian completion of the square yields, for every real \(k\),
\[
\mathbb E[e^{-k(h-Y)}\mathbf1_{\{Y<h\}}]
=e^{-kh+k^2v/2}\Phi((h-kv)/\sqrt v).
\]
Apply this with \(v=1/4\), \(k=8h,12h,16h\), and add \(\mathbb P(Y\ge h)=\Phi(-2h)\). This proves the exact midpoint expression. Gaussian Mills asymptotics \(\Phi(-z)\sim e^{-z^2/2}/(z\sqrt{2\pi})\) give
\[
\mathbb E[g_{h,1/2}(Y)^2]\sim
\left(\frac52-1+\frac16\right)\frac{e^{-2h^2}}{h\sqrt{2\pi}}=
\frac{5e^{-2h^2}}{3h\sqrt{2\pi}}.
\]
The subtracted \(e^{-4h^2}\) is negligible.

**Interior times before the quarter point.** By symmetry it suffices to take \(0<t\le1/2\). Put \(q_b(y)=\exp[-2h(h-y)/b]\), \(q_t(y)=\exp[-2h(h-y)/t]\) for \(y<h\), where \(b=1-t\ge t\). Then \(g=q_b+q_t(1-q_b)\) and \(q_b\le g\le2q_b\). The truncated second moment of the longer-piece term is exactly
\[
D_h(t):=\mathbb E[q_b(Y)^2\mathbf1_{\{Y<h\}}]
=e^{-4h^2(1-2t)/b}\Phi\!\left(\frac{h(1-4t)}{\sqrt v}\right).
\]
Under the Gaussian probability law tilted by \(q_b(Y)^2\), the untruncated \(Y\) has mean \(4ht\) and variance \(v\). If \(t<1/4\), its distance below \(h\) diverges linearly; consequently \(q_t/q_b\to0\) in probability and bounded convergence yields \(\mathbb E[g^2\mathbf1_{Y<h}]/D_h(t)\to1\). If \(t=1/4\), this tilted Gaussian is centered exactly at \(h\), and conditioning below \(h\) still forces \(q_t/q_b\to0\) almost surely under the fixed centered truncated Gaussian, yielding the same ratio. The Gaussian tail \(\mathbb P(Y\ge h)\) is exponentially negligible compared with \(D_h(t)\) for \(0<t<1/4\), and smaller by a factor of order \(1/h\) at \(t=1/4\). As \(\Phi(h(1-4t)/\sqrt v)\to1\) below the quarter point and equals \(1/2\) at the quarter point, the first two equivalents follow.

**Times after the quarter point.** For \(1/4<t\le1/2\), make the exact change \(u=h(h-y)\) in the \(y<h\) Gaussian integral. With \(F_t(u)=e^{-2u/t}+e^{-2u/b}-e^{-2u/v}\),
\[
\mathbb E[g^2\mathbf1_{\{Y<h\}}]
=\frac{e^{-h^2/(2v)}}{h\sqrt{2\pi v}}
\int_0^\infty e^{u/v-u^2/(2vh^2)}F_t(u)^2\,du.
\]
The integrand without its factor \(e^{-u^2/(2vh^2)}\) is integrable exactly when \(t>1/4\), since the slowest squared exponential has decay exponent \((4t-1)/v\). Dominated convergence applies. Expanding the square and integrating six exponential terms gives
\[
\int_0^\infty e^{u/v}F_t(u)^2\,du
=v\!\left[\frac73+\frac1{4t-1}+\frac1{4b-1}
-\frac2{2t+1}-\frac2{2b+1}\right].
\]
The Gaussian upper tail contributes \(\mathbb P(Y\ge h)\sim e^{-h^2/(2v)}\sqrt v/(h\sqrt{2\pi})\); adding it supplies the extra \(1\) in \(C(t)\). Again, \(e^{-4h^2}\) is exponentially smaller for fixed interior \(t\).

**Comparison of fixed observation times.** The exponential rates are
\[
\Lambda(t)=\begin{cases}4(1-2t)/(1-t),&0<t\le1/4,\\[3pt] 1/(2t(1-t)),&1/4\le t\le1/2.\end{cases}
\]
Both branches are strictly decreasing up to \(1/2\) and agree at \(t=1/4\). Since \(\Lambda(1/2)=2\) and \(\Lambda(t)>2\) for all other fixed interior times, the midpoint is uniquely optimal at the exponential-rate level. Reflection symmetry handles \(t>1/2\). This does **not** establish exact finite-\(h\) global optimality or uniformity for moving \(t=t_h\).

## Verification

Run `python check.py` with `mpmath`. The executable tests the exact six-term Gaussian expression for the second moment against independent high-precision quadrature at eight finite pairs, verifies five midpoint identities, and compares each of five fixed-time asymptotic equivalents at two large thresholds. The checks passed. These tests support, but do not replace, the analytical limit and optimal-rate proofs above.

## Relationship to prior work

Gerstner, Harrach and Roth (arXiv:1906.11002, first submitted 26 June 2019), particularly their crossing formula (2.4), one-step survival construction and variance comparison in Section 2, give the numerical motivation and the bridge-crossing conditional formula. Their work does not present the fixed-time single-observation information function or the exact three-regime rare-barrier asymptotics proved here. Giles, Debrabant and Rößler (arXiv:1302.4676, first submitted 19 February 2013) study Milstein multilevel Monte Carlo, Brownian-bridge interpolation and barrier-option variance rates as the time mesh is refined; those mesh-width asymptotics are not equivalent to the fixed-time, high-barrier information regime. Riedel (arXiv:1911.05272, initially public 13 November 2019) studies the reverse conditioning direction—Brownian path statistics conditional on extrema and their locations—and does not provide the barrier indicator conditional on one sampled bridge value. The Brownian-bridge reflection formula and normal-tail expansion are classical and are not claimed as new. A literature or indexed-record search cannot exclude an unlocated equivalent source.

## Limitations

This result treats one fixed deterministic noiseless observation, one positive constant barrier, the standard pinned bridge and squared-error information. It does not optimize the exact risk over all \(t\) at finite \(h\), does not cover \(h\)-dependent sampling times, multiple observations, noisy sensors, asymmetric endpoint bridges, two-sided barriers, path-dependent option payoffs or generic diffusions. The asymptotics are pointwise in \(t\), not uniform near the quarter-point transition or endpoints. No independent mathematical or publication-priority audit has been performed.

## References

1. T. Gerstner, B. Harrach and D. Roth, *Convergence of Milstein Brownian bridge Monte Carlo methods and stable Greeks calculation*, arXiv:1906.11002, initially public 26 June 2019. https://arxiv.org/abs/1906.11002
2. M. B. Giles, K. Debrabant and A. Rößler, *Analysis of multilevel Monte Carlo path simulation using the Milstein discretisation*, arXiv:1302.4676, initially public 19 February 2013. https://arxiv.org/abs/1302.4676
3. K. S. Riedel, *Mean and Variance of Brownian Motion with Given Final Value, Maximum and ArgMax: Extended Version*, arXiv:1911.05272, initially public 13 November 2019. https://arxiv.org/abs/1911.05272
