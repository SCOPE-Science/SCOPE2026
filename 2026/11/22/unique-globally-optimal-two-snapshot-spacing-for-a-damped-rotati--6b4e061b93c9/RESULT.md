# Unique globally optimal two-snapshot spacing for a damped rotation frame

## Finding
For the damped planar rotation semigroup \(T(s)=e^{-as}R(\omega s)\), \(a,\omega>0\), and any unit vector \(g\in\mathbb R^2\), the two vectors \(g,T(h)g\) have a uniquely optimal sampling interval \(h_*>0\) for maximizing their **least frame bound**. With \(\alpha=a/\omega\), \(t=2\omega h\), and \(q=e^{-\alpha t}\), their least frame bound is
\[
m(h)=\frac{1+q-\sqrt{1+q^2+2q\cos t}}2.
\]
The global maximizer is \(h_*=t_*/(2\omega)\), where \(t_*\in(0,\pi)\) is the **unique** root of
\[
q+\cos t=\frac{\alpha^2-1}{2\alpha}\sin t.
\]
Thus the optimum always occurs strictly before the first perpendicularization time \(\pi/(2\omega)\), and it is independent of the orientation of \(g\).

In the strong damping limit \(a/\omega\to\infty\), write \(v_0\) for the unique positive root of \(v_0=2(1+e^{-v_0})\). Then
\[
h_* = \frac{v_0}{2a}+O\left(\frac{\omega^2}{a^3}\right),\qquad
m(h_*)=\frac{v_0(v_0-2)}4\left(\frac\omega a\right)^2+O\left(\frac{\omega^4}{a^4}\right).
\]
Numerically \(v_0\approx 2.21771510575709\) and \(v_0(v_0-2)/4\approx 0.1207075196972503\). These asymptotic constants are supporting consequences, not a claim of novelty for this number in unrelated diffusion-frame models.

## Assumptions and scope
Work over the real Euclidean Hilbert space \(H=\mathbb R^2\), with \(a>0\), \(\omega>0\) and
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad T(s)=e^{s(-aI+\omega J)},\quad \|g\|_2=1.
\]
For **every** positive sample lag \(h\), let
\[
W_h=gg^\top+T(h)gg^\top T(h)^\top,\quad m(h)=\lambda_{\min}(W_h).
\]
The two samples have equal measurement weights; damping is incorporated in the second vector. The sign convention for \(J\) and the choice of the unit vector have no effect on the formula. This is an exact finite two-snapshot **E-optimal frame-bound** problem, not a claim about infinite continuous frames or determinant-optimal designs.

## Proof
**1. Exact spectrum.** By rotational invariance take \(g=(1,0)^\top\), put \(u=e^{-ah}\), and write \(\theta=\omega h\). The two sampling columns are \(g\) and \(u(\cos\theta,\sin\theta)^\top\). Their frame operator has trace \(1+u^2\) and determinant \(u^2\sin^2\theta\). Its two eigenvalues are
\[
\frac{1+u^2\pm\sqrt{(1-u^2)^2+4u^2\cos^2\theta}}2.
\]
Writing \(q=u^2=e^{-\alpha t}\) and \(t=2\theta\) gives the claimed formula.

**2. First half-turn contains every global maximizer.** For all \(t>0\), \(m(h)\le q\): evaluate the quadratic form on any unit vector perpendicular to \(g\). If \(t\ge\pi\), then \(m(h)\le e^{-\alpha\pi}\). At \(t=\pi\), the vectors are perpendicular and \(m=e^{-\alpha\pi}\). Yet the left derivative at \(\pi\) is strictly negative: the formula in Step 3 yields \(m'(\pi^-)=-\alpha q(1-q)/(1-q)=-\alpha q<0\). Consequently some \(t<\pi\) gives strictly more than \(e^{-\alpha\pi}\), excluding **all** later times (including later resonance peaks). There is a positive interior maximum since \(m(0)=0\) and the function is continuous.

**3. Exact stationarity and derivative sign.** For \(0<t<\pi\) set \(B=q+\cos t\), \(s=\sin t>0\), \(D=\sqrt{B^2+s^2}>0\). Direct differentiation yields
\[
\frac{dm}{dt}=\frac{q}{2D}[s-\alpha(D-B)].
\]
Since \(D+B>0\) and \(D-B=s^2/(D+B)\), its sign equals the sign of \(D+B-\alpha s\). The function \(D+B\) is strictly increasing in \(B\) for fixed \(s>0\); the equality \(D+B=\alpha s\) is equivalent, after one squaring step with positive terms, to \(B=(\alpha^2-1)s/(2\alpha)\). It follows that the derivative has the same sign as
\[
F_\alpha(t)=e^{-\alpha t}+\cos t-\frac{\alpha^2-1}{2\alpha}\sin t.
\]

**4. Unique zero and unique global maximizer.** Put \(K=(\alpha^2-1)/(2\alpha)\) and \(f(t)=\cos t-K\sin t\). On \((0,\pi)\), \(F_\alpha=f+e^{-\alpha t}\), with \(F_\alpha(0)=2>0\) and \(F_\alpha(\pi)=e^{-\alpha\pi}-1<0\).
If \(K<0\), the function \(f\) first increases from \(1\) to its sole positive maximum at \(\arctan(-K)\), then strictly decreases to \(-1\). On the rising segment \(f\ge1\), hence \(F_\alpha>0\); on the falling segment both summands strictly decrease and there is exactly one zero.
If \(K=0\), both summands strictly decrease, so there is exactly one zero.
If \(K>0\), \(f\) first strictly decreases from \(1\) to a minimum at \(\pi-\arctan K\), then increases to \(-1\); on its final increasing segment \(f\le-1\), while \(e^{-\alpha t}<1\), so \(F_\alpha<0\). On the initial decreasing segment the sum is strictly decreasing and crosses zero exactly once. Hence in all cases the unique zero \(t_*\) is a strict rise-to-fall change in \(m\). Step 2 makes it the unique global maximum on \((0,\infty)\).

**5. Strong damping.** Write \(v=\alpha t\) and \(\varepsilon=1/\alpha\). The stationarity equation becomes
\[
e^{-v}+\cos(\varepsilon v)-\frac{1-\varepsilon^2}{2\varepsilon}\sin(\varepsilon v)=0.
\]
For bounded \(v\), its left side equals \(e^{-v}+1-v/2+O(\varepsilon^2)\), locally uniformly with derivatives. The limiting function strictly decreases from \(2\) to negative values and has one simple root \(v_0>2\). By strict monotone bracketing plus uniqueness of the finite-parameter zero and the implicit function theorem, \(\alpha t_*=v_0+O(\alpha^{-2})\). Expanding the exact eigenvalue expression for \(t=v/\alpha\) gives
\[
m=\frac{e^{-v}v^2}{4(1+e^{-v})}\alpha^{-2}+O(\alpha^{-4}).
\]
At the root, \(e^{-v_0}=(v_0-2)/2\), so the prefactor is \(v_0(v_0-2)/4\), establishing both stated asymptotics. These arguments use only strictly positive damping; the excluded endpoint \(a=0\) has many maximizers rather than one.

## Verification
The standalone script `check_oscillator.py` independently evaluates the two-by-two frame matrix, the exact eigenvalue formula, roots and derivative signs on sample grids of damping ratios, and the stated limiting coefficients. Its finite tests are diagnostic; Steps 1–5 are the proof for every positive parameter and every sample lag. Example for \(a=\omega=1\): \(t_*=1.746139530408\ldots\), \(h_*=0.873069765204\ldots\), and \(m(h_*)=0.0948896813348\ldots\).

## Relationship to prior work
Bailey, Gallardo-Gutiérrez and Partington establish general continuous-semigroup frame and cogenerator correspondences, including their Theorems 2.11 and 2.18; those are background, not claims of novelty here. Gwizdek, Kużel and Majdak develop general discrete dynamical frames using Stein equations and dilations. Neither inspected work addresses the **globally unique optimal two-time separation** of this damped planar rotation with the smallest-frame-eigenvalue objective. Earlier three-time oscillator determinant-optimization results use a different sample count and objective; earlier two-time diffusion-frame results feature the same limiting numerical coefficient in a different geometry. The new assessed result is the full all-damping global uniqueness law and exact root characterization, not the common coefficient itself.

## Limitations
The theorem is for real isotropically damped rotations, a single fixed unit-norm sensor, exactly two *equally weighted* observations, and the least-frame-eigenvalue (E-optimal) objective. It does not classify three or more observations, arbitrary nonnormal generators, non-isotropic damping, variable relative observation weights, or noise-dependent designs. The exact optimization uses a scalar implicit root rather than an elementary closed form. Literature comparisons do not rule out an older implicit control-theoretic derivation.

## References
1. V. Bailey, E. A. Gallardo-Gutiérrez, J. R. Partington, *Frames Associated with \(C_0\)-Semigroups*, arXiv:2611.13867v1 (10 Nov 2026), https://arxiv.org/html/2611.13867v1.
2. S. Gwizdek, S. Kużel, W. Majdak, *Dynamical frames through Sz.-Nagy–Foiaş dilations*, arXiv:2611.20029v1 (15 Nov 2026), https://arxiv.org/html/2611.20029v1.
3. Relevant distinct comparisons: *Sharp strong-damping observability envelope for three-time oscillator sampling* (three observations, determinant objective); *Exact two-time diffusion frame bounds and optimal blind-spot scaling on the integer line* (diffusion and notch geometry; same strong-damping coefficient).
