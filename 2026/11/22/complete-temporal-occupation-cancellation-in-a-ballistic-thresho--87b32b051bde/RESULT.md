# Complete temporal occupation cancellation in a ballistic threshold-reset walker

## Finding

For a stationary ballistic particle that repeatedly traverses a fixed segment at an independently sampled positive speed and resets at the absorbing endpoint, **every bounded spatial observable has a centered time integral equal to the difference of two stationary endpoint potentials**. Consequently its unscaled occupation integral converges to the difference of two independent copies of an explicit random variable, rather than displaying ordinary square-root-time central-limit fluctuations. The limiting moment of order \(q>0\) exists exactly when the flight duration has finite moment of order \(q+1\). In particular the stationary time-average variance has a positive exact \(t^{-2}\) leading term when the third flight-duration moment is finite; if that moment is infinite, the unscaled integral variance diverges despite the same uniform stationary one-point position law.

## Assumptions and scope

Let \(L>0\), let \(T_1,T_2,\ldots\) be iid strictly positive flight durations with an absolutely continuous distribution and \(0<\mathbb E T<\infty\), and set the independently renewed velocities \(V_i=L/T_i\). During an excursion of duration \(T_i\), the particle follows \(X(s)=L(1-s/T_i)\), for \(0\le s<T_i\). At the end it jumps instantaneously from zero to \(L\), drawing a fresh duration; reset events take zero time. Start in the *stationary two-sided renewal version*, not at a newly initialized flight boundary.

At a stationary observation time the containing flight duration \(T^*\) is length-biased,
\[
\Pr(T^*\in dt)=\frac{t\Pr(T\in dt)}{\mathbb ET},
\]
and its fractional age \(U\) is independent and uniform on \([0,1]\). Thus \(X=L(1-U)\) is uniform on \([0,L]\). For a bounded real Borel observable \(f\), let
\[
\bar f=\frac1L\int_0^L f(x)\,dx,\qquad
H_f(u)=\int_0^u\bigl[f(L(1-v))-\bar f\bigr]dv,\quad 0\le u\le1.
\]
Define \(\Phi_f=T^*H_f(U)\), and let \(\Phi_f'\) be an independent copy. Let
\[
Y_f(t)=\int_0^t[f(X_s)-\bar f]ds.
\]
For the strict limiting-moment equivalences below, assume \(f\) is not almost-everywhere constant on \([0,L]\).

## Proof

**1. Exact pathwise primitive.** During a flight of duration \(T\), its fractional age advances at speed \(1/T\). Hence the time derivative of \(T H_f(U_s)\) is \(f(X_s)-\bar f\) for almost every time. Crucially \(H_f(0)=H_f(1)=0\) by the definition of \(\bar f\); therefore this primitive stays continuous across every instantaneous reset, although \(X\) jumps. With \(\Phi_f(s)\) the primitive evaluated using the duration and phase of the flight containing time \(s\),
\[
\boxed{Y_f(t)=\Phi_f(t)-\Phi_f(0)\quad\text{pathwise for every }t\ge0.}
\]
This is a genuine full-excursion cancellation: the integral of \(f(X)-\bar f\) over each entire flight is zero for *every realized speed*, not merely in expectation.

**2. Unscaled limiting law.** In the stationary renewal process the residual duration at time zero is finite almost surely. Conditional on this initial flight and its residual, all later durations are fresh iid draws. The nonarithmetic renewal limit theorem (the assumed density makes the duration nonarithmetic) gives convergence of the forward phase-duration pair to its equilibrium length-biased/uniform law independently of the initial flight. First apply this to bounded continuous test functions and then truncate the unbounded primitive. It follows that
\[
(\Phi_f(0),\Phi_f(t))\Longrightarrow(\Phi_f,\Phi_f')
\quad\text{and}\quad
\boxed{Y_f(t)\Longrightarrow\Phi_f'-\Phi_f.}
\]
The limiting characteristic function is explicitly
\[
\boxed{\mathbb E e^{is(\Phi_f'-\Phi_f)}=
\left|\frac{1}{\mathbb ET}\mathbb E\!\left[T\int_0^1 e^{isT H_f(u)}du\right]\right|^2,\qquad s\in\mathbb R.}
\]
The right side is real, nonnegative and defines a symmetric distribution; it is generally non-Gaussian.

**3. Sharp limiting moment boundary.** By the length-biased construction and independence of \(T^*\) and \(U\), for every \(q>0\),
\[
\mathbb E|\Phi_f|^q=
\frac{\mathbb ET^{q+1}}{\mathbb ET}\int_0^1|H_f(u)|^qdu.
\]
For non-a.e.-constant \(f\), the integral over \(u\) is finite and strictly positive. If \(\mathbb ET^{q+1}<\infty\), the elementary two-term \(q\)-moment bound gives a finite moment for \(\Phi_f'-\Phi_f\). Conversely, when \(\mathbb E|\Phi_f|^q=\infty\), choose \(M>0\) with \(\Pr(|\Phi_f'|\le M)>0\). On the independent event \(|\Phi_f|>2M\) and \(|\Phi_f'|\le M\), the difference has size at least \(|\Phi_f|/2\), so its \(q\)-moment diverges. Thus
\[
\boxed{\mathbb E|\Phi_f'-\Phi_f|^q<\infty
\iff\mathbb ET^{q+1}<\infty.}
\]
Because \(T=L/V\), an initial velocity density satisfying \(\phi(v)\sim c v^\beta\) as \(v\downarrow0\) with \(\beta>0\) and \(c>0\) has the limiting occupation-moment cutoff \(q<\beta\). This uses no assumption on upper-speed behavior beyond the probability-density and finite-mean conditions.

**4. Exact large-window variance.** When \(\mathbb ET^3<\infty\), stationary \(\Phi_f(t)\) has finite second moment. Truncation and the above asymptotic independence yield \(\operatorname{Cov}(\Phi_f(0),\Phi_f(t))\to0\). The first two stationary primitive moments are
\[
\mathbb E\Phi_f=\frac{\mathbb ET^2}{\mathbb ET}\int_0^1H_f(u)du,\qquad
\mathbb E\Phi_f^2=\frac{\mathbb ET^3}{\mathbb ET}\int_0^1 H_f(u)^2du.
\]
Stationarity and the coboundary identity imply
\[
\boxed{\operatorname{Var}\!\left[\frac1t\int_0^t f(X_s)ds\right]
\sim \frac{2}{t^2}\left[
\frac{\mathbb ET^3}{\mathbb ET}\int_0^1 H_f(u)^2du-
\left(\frac{\mathbb ET^2}{\mathbb ET}\int_0^1H_f(u)du\right)^2\right].}
\]
The bracket is \(\operatorname{Var}(\Phi_f)>0\) for nonconstant \(f\). If \(\mathbb ET^3=\infty\), the limiting difference has infinite second moment by step 3. The lower-semicontinuity moment inequality applied to the weak limit shows \(\liminf_{t\to\infty}\mathbb EY_f(t)^2=\infty\). At every finite time \(|Y_f(t)|\le 2t\|f\|_\infty\), so each finite-window variance is well-defined. This proves the claimed sharp bounded-versus-divergent unscaled variance dichotomy, without asserting a universal divergence rate.

**5. Position example.** For \(f(x)=x\),
\[
H_f(u)=\frac L2u(1-u),\qquad
\int_0^1H_f(u)du=\frac L{12},\qquad
\int_0^1H_f(u)^2du=\frac{L^2}{120}.
\]
Consequently
\[
\boxed{\lim_{t\to\infty}\operatorname{Var}\!\left(\int_0^t[X_s-L/2]ds\right)
=L^2\left[\frac{\mathbb ET^3}{60\mathbb ET}-\frac{(\mathbb ET^2)^2}{72(\mathbb ET)^2}\right]}
\]
when \(\mathbb ET^3<\infty\). For \(T\sim\operatorname{Exp}(\lambda)\) this limit equals \(2L^2/(45\lambda^2)\), and the limiting characteristic function is
\[
\left|\int_0^1\left(1-\frac{isL}{2\lambda}u(1-u)\right)^{-2}du\right|^2.
\]

## Verification

`checker.py` uses exact rational arithmetic to verify whole-cycle and partial-cycle primitive identities for observables \(f(x)=x^p\), \(p=1,2,3,4\), over multiple flight durations; it verifies the rational exponential-duration variance coefficient; and it independently simulates stationary renewal paths with exponential durations to check convergence to \(2L^2/45\) for \(L=\lambda=1\). The sampled value at lag \(t=50\), using 20,000 paths and a fixed seed, is approximately \(0.04513\) versus the limiting \(0.04444\). This finite simulation is evidence for the calculation, **not** a substitute for the renewal-theorem proof of weak convergence or the all-\(q\) moment criterion.

Run `python3 checker.py` with the Python standard library. The scientific proof does not depend on the program.

## Relationship to prior work

Das, Majumdar and Pal (2026) establish the uniform stationary position distribution, transient propagator, freezing crossover, power-law relaxation and moving shocks of this ballistic threshold-reset model. The present finding addresses *temporal additive observables and their entire unscaled limit laws*, which are not determined by the uniform one-point stationary law. The new cancellation is structural and should be distinguished from conventional regenerative central-limit calculations where cycle-centered occupation rewards typically have positive variance. Standard renewal theory provides the stationary length-bias and phase construction, but does not by itself specify the model's all-observable zero-reward identity or the resulting explicit moment hierarchy. A published study of occupation fluctuations for threshold-reset sluggish diffusion concerns nondeterministic within-cycle paths and nonzero cycle rewards, so it does not imply this theorem.

## Limitations

The stationary starting law is essential for the exact variance formula. The unscaled weak limit requires an absolutely continuous flight-duration law here; the deterministic-duration case is periodic and not covered. At most one-dimensional fixed-length ballistic flights with instantaneous complete resets are treated. Nonzero waiting times at resets, random flight distances, velocity changes within a flight or partial resets generally destroy the exact cancellation. The high-order moments concern the **limiting integrated observable**, not uniform moment convergence for every exponent under infinite-duration moments. The assertion does not establish an entropy-production formula or a finite-window large-deviation principle. The comparison with all unpublished or unindexed equivalences is not exhaustive.

## References

1. R. Das, S. N. Majumdar and A. Pal, *Freezing transition and shock-like transients in ballistic random walks under threshold resetting*, arXiv:2611.16733 (first public version 12 November 2026), https://arxiv.org/abs/2611.16733 . Primary model and one-point results.
2. *Renewal processes*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Renewal_processes . Standard stationary regenerative construction and nonlattice renewal limit theorem.
3. H. Thorisson, *The coupling of regenerative processes*, Advances in Applied Probability (2016), https://www.cambridge.org/core/journals/advances-in-applied-probability/article/coupling-of-regenerative-processes/A92498C27136488BADF78B087CCA027B . General regenerative coupling background.
4. *Universal centered-cycle variance for threshold-reset sluggish diffusion*, previously published related result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-universal-centered-cycle-variance-for-threshold-reset-sluggish-d--5f67338ca3a7 . Different within-cycle stochastic occupation rewards.
