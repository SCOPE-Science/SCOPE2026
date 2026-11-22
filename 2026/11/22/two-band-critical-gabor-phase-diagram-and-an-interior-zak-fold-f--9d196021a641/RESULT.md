# Two-band critical Gabor phase diagram and an interior Zak fold for three Cauchy poles

## Finding

For real parameters \(0<r,q<1\), define three logarithmically equally spaced pole heights
\[
 a=\frac{\log(1/r)}{2\pi},\qquad h=\frac{\log(1/q)}{2\pi},
\]
and a signed Cauchy-window family
\[
 g_\lambda(t)=\frac1{t+ia}-\frac{\lambda}{t+i(a+h)}+
             \frac1{t+i(a+2h)},\qquad \lambda\in\mathbb R.
\]
Consider the critical integer Gabor system
\[
 \mathcal G_\lambda=\{e^{2\pi i mt}g_\lambda(t-n):m,n\in\mathbb Z\}
 \quad\text{in }L^2(\mathbb R).
\]
Introduce the four positive constants
\[
 c_+=\frac{1-rq}{1-r},\quad d_+=\frac{1-rq}{1-rq^2},\quad
 c_-=\frac{1+rq}{1+r},\quad d_-=\frac{1+rq}{1+rq^2}.
\]
Assume the open geometric condition
\[
 \boxed{\left(\frac{1+rq^2}{1+r}\right)^2>q.}\tag{H}
\]
Then **the complete real-residue frame phase diagram** is
\[
 \boxed{\mathcal G_\lambda\text{ is a frame (equivalently a Riesz basis)}
 \iff \lambda\notin I_-\cup I_+,}
\]
where the two closed forbidden bands are
\[
 \boxed{I_-=[2\sqrt{c_-d_-},\ c_-/q+qd_-],\qquad
 I_+=[c_++d_+,\ c_+/q+qd_+].}
\]
The intervals are disjoint, yielding **three open Riesz-basis phases**, whenever
\[
 c_-/q+qd_-<c_++d_+.\tag{S}
\]
Their endpoints are genuine nonframe parameters. The lower band begins at a *quadratically degenerate interior Zak zero* at
\[
 x_*=\frac12,\quad s_*=\sqrt{\frac{1+rq^2}{1+r}},\quad
 \omega_*=\frac{\log s_*}{\log q}\in(0,1),\quad
 \lambda_*=2\sqrt{c_-d_-}.
\]
Just above \(\lambda_*\), that zero splits into two distinct zeros on the same spatial fiber, with the sharp square-root law
\[
 \boxed{\omega_\pm(\lambda)=\omega_*
 \pm\frac{\sqrt{\lambda-\lambda_*}}{|\log q|(c_-d_-)^{1/4}}
 +O_{r,q}(\lambda-\lambda_*),\qquad \lambda\downarrow\lambda_*\ \text{from above}.}
\]
In particular the exact choice \(r=4/5\), \(q=1/4\) satisfies (H) and (S) and produces the simple complete classification
\[
 \boxed{\mathcal G_\lambda\text{ is a Riesz basis}
 \iff\lambda\notin
 \left[\frac8{\sqrt{21}},\frac{62}{21}\right]
 \cup\left[\frac{92}{19},\frac{308}{19}\right].}
\]
The first fold is at \(\omega_*=\log(\sqrt{7/12})/\log(1/4)\); its splitting coefficient is \(21^{1/4}/(2\log4)\).

## Assumptions and scope

All windows are elements of \(L^2(\mathbb R)\); the pole heights are positive and distinct, and the real residue parameter ranges over all of \(\mathbb R\). The Gabor system uses integer translation and modulation and the standard \(L^2\) frame inequality. The claim addresses the two-parameter **open region (H)**, with (S) added only for separation of the two forbidden intervals; no description is asserted outside (H). The lowest-frequency one-sided Zak limits count as genuine frame obstructions. The theorem does not assert a uniform lower frame bound across all admitted \(\lambda\), nor a result for noncritical lattices.

Use the Fourier convention \(\widehat f(\xi)=\int_{\mathbb R} f(t)e^{-2\pi it\xi}\,dt\). The Zak transform is normalized by
\[
 Zg(x,\omega)=\sum_{n\in\mathbb Z}g(x+n)e^{-2\pi in\omega},
 \qquad 0\le x<1,\quad 0<\omega<1.
\]
For rational windows the series can be interpreted by its \(L^2\) Fourier-series realization; the closed-form analytic expression below gives its representative in the open frequency strip, with finite one-sided endpoint limits.

## Proof

**1. Exact Zak formula.** For any real \(b>0\), contour integration gives
\[
 \widehat{(t+ib)^{-1}}(\xi)=-2\pi i\,e^{-2\pi b\xi}
 \mathbf 1_{(0,\infty)}(\xi).
\]
Poisson summation in the Zak frequency variable yields, for \(0<\omega<1\),
\[
 Z[(t+ib)^{-1}](x,\omega)=
 -2\pi i\,e^{2\pi ix\omega}
 \frac{e^{-2\pi b\omega}}{1-e^{-2\pi b}e^{2\pi ix}}.
\]
Set \(u=e^{2\pi ix}\), \(s=q^\omega\in(q,1)\). Since the three pole factors are \(r,rq,rq^2\), linearity gives
\[
 Zg_\lambda(x,\omega)=-2\pi i\,e^{2\pi ix\omega}r^\omega
 \left[\frac1{1-ru}-\frac{\lambda s}{1-rqu}
             +\frac{s^2}{1-rq^2u}\right].\tag{1}
\]
Every denominator is nonzero for \(|u|=1\). The right side is bounded and continuous on the **one-sided compact rectangle** \(|u|=1\), \(q\le s\le1\). The Zak unitary equivalence at critical density says that \(\mathcal G_\lambda\) is a frame/Riesz basis exactly when the essential infimum of \(|Zg_\lambda|\) is positive. By continuity on the one-sided rectangle, this is equivalent to the absence of zeros of the bracket in (1) for any \(|u|=1\), \(s\in[q,1]\). Endpoint zeros yield arbitrarily small interior moduli, so they also destroy the lower frame bound.

**2. All possible zeros lie on two spatial fibers.** Solving the bracket equation (1) for the real parameter gives
\[
 \lambda=F(u,s):=\frac{1-rqu}{s(1-ru)}
                  +s\frac{1-rqu}{1-rq^2u}.\tag{2}
\]
Write \(u=e^{i\theta}\). A direct imaginary-part calculation yields
\[
 \operatorname{Im}F(e^{i\theta},s)=\sin\theta\left[
  \frac{r(1-q)}{s|1-re^{i\theta}|^2}
  -\frac{rq(1-q)s}{|1-rq^2e^{i\theta}|^2}\right].\tag{3}
\]
If \(\sin\theta\ne0\) and the right side vanishes, then
\[
 \frac{|1-rq^2e^{i\theta}|^2}{|1-re^{i\theta}|^2}
 =qs^2\le q.\tag{4}
\]
For \(0<r,q<1\), the left side is strictly increasing as a function of \(\cos\theta\), because its derivative is the positive quantity
\[
 \frac{2r(1-q^2)(1-r^2q^2)}{(1+r^2-2r\cos\theta)^2}.
\]
Consequently it is at least \(((1+rq^2)/(1+r))^2\), which exceeds \(q\) by (H), a contradiction. Thus any zero must lie on \(u=1\) (\(x=0\)) or \(u=-1\) (\(x=1/2\)).

**3. Exact forbidden intervals.** At \(u=1\) and \(u=-1\), respectively, (2) becomes
\[
 \lambda_+(s)=\frac{c_+}{s}+d_+s,
 \qquad \lambda_-(s)=\frac{c_-}{s}+d_-s,
 \qquad q\le s\le1.\tag{5}
\]
The first is strictly decreasing, since \(c_+/d_+=(1-rq^2)/(1-r)>1\), so its range is exactly \(I_+\).

The second is strictly convex; its unique stationary point is
\[
 s_*=\sqrt{c_-/d_-}=\sqrt{(1+rq^2)/(1+r)}.
\]
The strict inequalities \(q<s_*<1\) hold for every \(0<r,q<1\): namely \((1+rq^2)>q^2(1+r)\) and \((1+rq^2)<(1+r)\). Hence its minimum is \(2\sqrt{c_-d_-}\). Its maximum is at \(s=q\), because
\[
 \lambda_-(q)-\lambda_-(1)=(1-q)(c_-/q-d_-)>0,
\]
using \(c_-/d_-=(1+rq^2)/(1+r)>q\), equivalently \((1-q)(1-rq)>0\). Thus its exact range is \(I_-\). This proves the claimed if-and-only-if for all real \(\lambda\) under (H), including all one-sided endpoints. Under (S) the intervals are disjoint and the stable set has three connected components.

**4. Interior fold and splitting.** At \(s=s_*\), the first derivative of \(\lambda_-(s)\) vanishes, but its second derivative is \(2c_-/s_*^3>0\); therefore the Zak-zero equation has a quadratic tangency along the frequency fiber \(x=1/2\). The nonzero transverse imaginary derivative follows from the strict inequality used in (4). Taylor expansion gives
\[
 \lambda_-(s)-\lambda_*=\frac{d_-}{s_*}(s-s_*)^2
 +O_{r,q}(|s-s_*|^3).
\]
Since \(ds/d\omega=s\log q\ne0\), the two roots for \(\lambda>\lambda_*\) sufficiently close to it satisfy precisely the stated square-root expansion. They are both in the open frequency strip; below \(\lambda_*\) there are no zeros on that fiber. This is an interior birth of two Zak zeros, not a zero arriving from a frequency endpoint.

**5. Exact rational specialization.** For \(r=4/5\), \(q=1/4\),
\[
 c_+=4,\quad d_+=16/19,\quad c_-=2/3,\quad d_-=8/7,
 \quad ((1+rq^2)/(1+r))^2=49/144>1/4.
\]
The two forbidden intervals are therefore exactly those in the finding, with
\(62/21<92/19\). The coefficient in the square-root law simplifies to \(21^{1/4}/(2\log4)\). Every threshold follows by exact algebra, not numerical fitting.

## Verification

The proof above is self-contained apart from the standard Zak-transform frame criterion and the Fourier transform of one Cauchy kernel. Run `python3 CHECK.py` using only Python's standard library. The checker verifies exact rational factors and inequalities and evaluates the analytic Zak factor on an extensive deterministic grid, including points constructed from the exact zero curves. These finite diagnostics supplement but do not replace the analytic continuous-parameter proof. The code is part of this package, and no external data files are needed.

## Relationship to prior work

Belov, Kulikov and Lyubarskii established the general Gabor-frame framework for rational Cauchy windows, including positivity of Herglotz mixtures at critical density, and discussed qualitative two-kernel frame sets [1]. Their results do not provide the signed **three-pole** real-residue phase diagram (2)–(5) or its interior quadratic bifurcation; their irrational-density general theorem does not decide the critical integer lattice here.

The published signed **two-Cauchy** study [2] already exhibits two disjoint nonframe intervals with a stable gap and gives an optimal lower-frame-bound law there. Thus neither reentry by itself nor the general Zak criterion is claimed as new. The specific additional structure here is a geometrically spaced **three-pole** family, a nontrivial open two-parameter classification region, and a lower-band threshold born from a double zero in the *interior frequency fiber*. In the analogous signed two-pole calculation the zero ratio is proportional to \(1/s\) and cannot have this interior fold. Later work on rational windows with symmetric upper/lower poles [3] has different pole and lattice hypotheses.

## Limitations

The zero-exclusion condition (H) is sufficient for the complete classification given; cases outside that region may have non-axial Zak zeros and are not classified here. The full phase diagram concerns only real signed middle residues, geometrically spaced three **simple** poles on the same side of the real axis, and critical integer Gabor density. Exact numerical lower and upper frame bounds, parameter-dependent condition numbers, perturbations breaking pole spacing, and subcritical-density frames are not computed. The result gives no independent historical-priority certification or independent mathematical audit.

## References

[1] Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frames for rational functions*, arXiv:2103.08959 (first public 16 March 2021); *Inventiones mathematicae* 231 (2023), 431–466. https://doi.org/10.1007/s00222-022-01151-8 . Relevant: Sections 1.3–1.7.3.

[2] *Exact protected-gap lower frame bound for signed two-Cauchy Gabor windows* (2026), publicly available mathematical research record; see the repository https://github.com/published-finding corpus/2026 . Relevant: exact two-pole protected gap, excluding three-pole interior fold.

[3] R. Ghosh, *Gabor Frames for Rational Windows with Symmetric Poles*, arXiv:2608.10568 (11 August 2026). Relevant: different symmetric-pole families and rational lattice criteria.

[4] K. Gröchenig, *Foundations of Time-Frequency Analysis*, Birkhäuser (2001), for the classical Zak-transform frame criterion.
