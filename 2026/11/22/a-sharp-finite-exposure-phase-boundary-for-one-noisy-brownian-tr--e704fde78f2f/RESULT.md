# A sharp finite-exposure phase boundary for one noisy Brownian trajectory sensor

## Finding

A single noisy measurement averaging Brownian motion over a fixed-duration exposure exhibits an exact transition between an interior and terminal observation window. Let \(0<h<1\) be the exposure length, \(\eta>0\) the independent readout-noise variance, and \(t\in[0,1-h]\) the exposure start. Under integrated posterior-variance loss, define

\[
F(h)=46h^3-165h^2+180h-60,
\qquad
\eta_c(h)=\frac{60-180h+165h^2-46h^3}{15h(12-7h)}.
\]

The cubic \(F\) has exactly one root \(h_*\) in \((0,1)\), with \(h_*\approx0.653386334746201\). The **unique** optimal window is terminal, \(t_*=1-h\), whenever \(h\ge h_*\), regardless of positive \(\eta\). For \(0<h<h_*\), the unique optimum is strictly interior precisely for \(0<\eta<\eta_c(h)\); for \(\eta\ge\eta_c(h)\), it equals the terminal window. In the interior regime,

\[
\frac{1-h}{2}<t_*<1-h,
\quad
N_h'(t_*)\bigl(t_*+h/3+\eta\bigr)-N_h(t_*)=0,
\]

where \(N_h\) is the explicit cubic below. Within that regime, \(t_*\) is strictly increasing in \(\eta\), and approaches \(1-h\) continuously at the threshold. As \(h\downarrow0\), \(\eta_c(h)\sim1/(3h)\): the finite-exposure terminal phase recedes to infinite noise. For any fixed finite \(\eta>0\), the limit is the strictly interior point-sampling optimum

\[
\lim_{h\downarrow0}t_*(h,\eta)
=\frac{3-6\eta+\sqrt{(3-6\eta)^2+96\eta}}8\in(0,1).
\]

## Assumptions and scope

Let \(W\) be standard real Brownian motion on \([0,1]\), with \(W(0)=0\) and \(\operatorname{Cov}(W(s),W(u))=\min(s,u)\). For a fixed \(h\in(0,1)\), observe exactly one scalar

\[
Y_{t,h}=\frac1h\int_t^{t+h}W(u)\,du+\epsilon,
\qquad 0\le t\le1-h,
\]

with \(\epsilon\sim N(0,\eta)\), \(\eta>0\), independent of the process. Noise variance is held fixed as the exposure duration changes; no time-dependent noise scaling is assumed. The criterion is the unconditional integrated posterior variance

\[
R_{h,\eta}(t)=\int_0^1\operatorname{Var}\bigl(W(s)\mid Y_{t,h}\bigr)\,ds.
\]

The design is nonadaptive and uses one continuous-time window average, not point evaluation or an observation of an integrated Brownian state. Its posterior covariance does not depend on the observed scalar value.

## Proof

**1. Exact scalar objective.** Direct integration of the Brownian covariance gives

\[
\operatorname{Var}(Y_{t,h})=t+\frac h3+\eta,
\qquad C_{t,h}(s):=\operatorname{Cov}(W(s),Y_{t,h})=
\begin{cases}
 s,&0\le s\le t,\\
 s-\dfrac{(s-t)^2}{2h},&t\le s\le t+h,\\
 t+\dfrac h2,&t+h\le s\le1.
\end{cases}
\]

The rank-one Gaussian conditioning identity and \(\int_0^1\operatorname{Var}(W(s))\,ds=1/2\) yield

\[
R_{h,\eta}(t)=\frac12-\frac{N_h(t)}{t+h/3+\eta},
\quad
N_h(t):=\int_0^1 C_{t,h}(s)^2\,ds.
\]

Evaluating the three elementary integrals yields the polynomial identity

\[
N_h(t)=-\frac23t^3+(1-h)t^2+
\left(h-\frac{7h^2}{12}\right)t
+\frac{h^2}4-\frac{7h^3}{60}.
\]

All denominators are strictly positive by the hypotheses. Maximizing \(Q(t):=N_h(t)/(t+h/3+\eta)\) is therefore equivalent to minimizing the specified posterior risk.

**2. One-peak derivative argument.** Set \(D(t)=t+h/3+\eta\) and \(P(t)=N_h'(t)D(t)-N_h(t)\); then \(Q'(t)=P(t)/D(t)^2\). Elementary differentiation gives

\[
N_h'(t)=2t(1-t-h)+h\left(1-\frac{7h}{12}\right)>0,
\quad N_h''(t)=2(1-h-2t),
\]

for every \(t\in[0,1-h]\), and

\[
P'(t)=N_h''(t)D(t).
\]

Consequently, \(P\) strictly increases on \([0,(1-h)/2]\) and strictly decreases on \([(1-h)/2,1-h]\). At the two endpoints,

\[
P(0)=\frac{h\{h(15-14h)+\eta(180-105h)\}}{180}>0,
\]

\[
P(1-h)=\frac{F(h)+15h(12-7h)\eta}{180}.
\]

If \(P(1-h)<0\), exactly one zero of \(P\) lies to the right of \((1-h)/2\), and \(Q\) rises and then falls: its unique global maximizer is that zero. If \(P(1-h)\ge0\), the increasing-then-decreasing shape and \(P(0)>0\) imply \(P(t)>0\) for all \(t<1-h\), so \(Q\) has unique global maximizer \(1-h\). This also handles equality at the boundary without introducing a second optimizer.

**3. Sharp width/noise boundary.** The derivative

\[
F'(h)=6(23h^2-55h+30)
\]

has exactly one zero in \((0,1)\), a local maximum; with \(F(0)=-60\) and \(F(1)=1\), there is exactly one root \(h_*\in(0,1)\). Thus \(F(h)<0\) precisely for \(0<h<h_*\). Since \(15h(12-7h)>0\), the endpoint sign formula above gives exactly the claimed phase diagram and \(\eta_c(h)\). On an interior optimum the implicit function theorem applies, because \(P'(t_*)=N_h''(t_*)D(t_*)<0\), and

\[
\frac{\partial t_*}{\partial\eta}
=-\frac{N_h'(t_*)}{P'(t_*)}>0.
\]

For fixed \(0<h<h_*\), as \(\eta\uparrow\eta_c(h)\), the decreasing-branch root converges to the endpoint. Its first-order arrival law, obtained by Taylor expansion of \(P\) at the endpoint, is

\[
1-h-t_*(h,\eta)=
\frac{h(12-7h)}{24(1-h)\{1-2h/3+\eta_c(h)\}}
\bigl(\eta_c(h)-\eta\bigr)
+O_h\!\left((\eta_c(h)-\eta)^2\right).
\]

**4. Vanishing-window limit.** The exact expression gives \(\eta_c(h)=1/(3h)-29/36+O(h)\) as \(h\downarrow0\). For fixed finite positive \(\eta\), the interior regime therefore applies for all sufficiently small widths. The numerator converges uniformly on feasible compact sets to \(N_0(t)=t^2-2t^3/3\), and the denominator to \(t+\eta\). The limiting derivative condition is

\[
2t^2+(3\eta-3/2)t-3\eta=0
\]

for its positive critical point; the unique positive root is the displayed \(t_{0,\eta}\), strictly below one because this quadratic is negative at zero and positive at one. Uniqueness and compactness imply convergence of the maximizers; equivalently, their explicit derivative equations converge and have a unique interior branch. Hence the finite-width terminal-window phase has no finite-noise point-observation counterpart.

## Verification

The accompanying self-contained source `VERIFY.py` recomputes the covariance integral symbolically, checks the cubic and all derivative and endpoint identities, isolates the sole root of \(F\) in \((0,1)\) by exact rational intervals, tests the point-width asymptotic and phase inequalities on a sample grid, and independently evaluates 75 covariance integrals by high-accuracy numerical quadrature. Run with `python VERIFY.py`; it requires Python 3, SymPy and SciPy. These computational checks support but do not replace the analytic proof above.

As an exact check at \(h=1/2\), the critical noise is \(\eta_c=22/255\). In the zero-noise limiting case, the optimal start is approximately \(0.446640667508570\), strictly between \(1/4\) and \(1/2\). The cubic root satisfies \(h_*\approx0.653386334746201\); its decimal is illustrative, not the definition of the theorem.

## Relationship to prior work

Nguyen and Peraire (2014) provide a general Gaussian-process linear-functional observation framework and posterior-covariance formula for functional data in PDE models; the present rank-one conditioning step is standard. Ji and Müller (2016) develop trajectory-reconstruction design with noisy point observations. Longi and collaborators (2020) develop sensor placement for integral Gaussian-process observations in spatial settings. Those works supply motivating settings or general methods, but their inspected statements do not give the exact Brownian fixed-width exposure optimizer, the algebraic phase boundary \(h_*\), or the singular \(h\downarrow0\) noise threshold. This is a special-model exact optimization result rather than a claim of novelty for Gaussian conditioning or integral observations themselves.

## Limitations

The theorem concerns one scalar measurement of standard Brownian motion on a unit interval, known variance, uniform full-path integrated posterior loss, constant readout-noise variance, and nonadaptive fixed-duration boxcar exposure. It does not characterize multiple sensors, arbitrary Gaussian kernels, variable exposure duration, nonuniform loss, causal filtering, or noise models whose variance changes with the exposure width. A same-source or unindexed equivalent result may exist outside the inspected literature. No independent audit has been performed.

## References

1. N.-C. Nguyen and J. Peraire, *Functional Gaussian processes for regression with linear PDE models*, arXiv:1405.7569v1 (first posted 2014-05-29), https://arxiv.org/abs/1405.7569.
2. H. Ji and H.-G. Müller, *Optimal Designs for Longitudinal and Functional Data*, arXiv:1604.05375v1 (first posted 2016-04-18), https://arxiv.org/abs/1604.05375.
3. K. Longi and coauthors, *Sensor Placement for Spatial Gaussian Processes with Integral Observations*, Proceedings of Machine Learning Research 124 (2020), 1009–1018, https://proceedings.mlr.press/v124/longi20a.html.
