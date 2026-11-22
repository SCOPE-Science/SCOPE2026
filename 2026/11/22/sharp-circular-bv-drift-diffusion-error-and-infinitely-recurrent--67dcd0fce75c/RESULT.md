# Sharp circular BV drift–diffusion error and infinitely recurrent peaks

## Finding

On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), let \(b\in\mathbb R\), \(t>0\), and \(P_t^{(b)}=\exp[t(\partial_\theta^2+b\partial_\theta)]\). For real distributional \(BV(\mathbb T)\), set \(V(f)=|Df|(\mathbb T)\) and use **unnormalized** Lebesgue \(L^1\). Then the exact sharp operator defect is

\[
C_b(t):=\sup_{V(f)>0}\frac{\|f-P_t^{(b)}f\|_{L^1(\mathbb T)}}{V(f)}
=\mathbb E\,d_{\mathbb T}(bt+\sqrt{2t}\,Z,0)
=\frac\pi2-\frac4\pi\sum_{\substack{k\ge1\\k\ \mathrm{odd}}}\frac{e^{-k^2t}\cos(kbt)}{k^2},
\]
where \(Z\) is standard normal and \(d_{\mathbb T}(\theta,0)=\min_{m\in\mathbb Z}|\theta-2\pi m|\). **Precisely** the nonconstant two-level half-circle step functions, up to rotation, nonzero scaling and addition of a constant, attain equality.

At each fixed \(t>0\), the coefficient depends only on the circular drift displacement \(bt\pmod{2\pi}\); it is strictly increasing with its geodesic distance from zero, so is uniquely smallest at zero drift phase and largest at antipodal phase.

For \(b=0\), \(C_0(t)\) increases strictly to \(\pi/2\). For **every** \(b\ne0\), \(C_b(t)\) has infinitely many alternating strict local maxima and minima. With \(\beta=|b|>0\) and
\[
t_n^{(0)}=\frac{\pi/2+\arctan\beta+n\pi}{\beta},
\]
there is, for all sufficiently large integers \(n\), exactly one critical time \(t_n\) near \(t_n^{(0)}\), with no further sufficiently large critical times, and
\[
t_n=t_n^{(0)}+O_\beta(e^{-8t_n^{(0)}}),\qquad
C_b(t_n)-\frac\pi2=(-1)^n\frac{4\beta}{\pi\sqrt{1+\beta^2}}e^{-t_n}+O_\beta(e^{-9t_n}).
\]
Even \(n\) give strict local maxima and odd \(n\) strict local minima.

## Assumptions and scope

Functions are real-valued \(L^1\)-equivalence classes of finite distributional variation, with \(V(f)>0\). The heat coefficient is one, not one-half. Every \(t>0\) has a smooth **strictly positive** circular heat kernel, including when \(b\ne0\). Constants disappear from the seminorm and defect. The first, more general, ingredient applies to any circle probability convolution whose law has a strictly positive density; it does not assume kernel symmetry.

## Proof

**1. Universal circle convolution lemma.** Write \(\tau_zf(x)=f(x+z)\), and let \(\mu\) be any probability law on the circle. For the shorter representative \(|z|\le\pi\), the fundamental theorem for distributional derivatives and Tonelli's theorem give the sharp translation estimate
\[
\|f-\tau_z f\|_1\le |z|\,V(f)=d_{\mathbb T}(z,0)V(f).
\]
Consequently \(\|f-\int\tau_zf\,\mu(dz)\|_1\le V(f)\int d_{\mathbb T}(z,0)\,\mu(dz)\). If \(E\) is any arc of length \(\pi\), then \(V(\mathbf1_E)=2\) and \(\|\mathbf1_E-\tau_z\mathbf1_E\|_1=2d_{\mathbb T}(z,0)\). For each fixed \(x\), all the differences \(\mathbf1_E(x)-\tau_z\mathbf1_E(x)\), over arbitrary \(z\), share a sign: nonnegative on \(E\) and nonpositive on its complement. Thus the triangle inequality is an equality after averaging, proving the exact coefficient.

**2. Equality rigidity.** Suppose the convolution density is strictly positive everywhere, and a nonconstant \(f\) attains equality. Equality in the chain of inequalities in step 1 forces \(\|f-\tau_zf\|_1=d_{\mathbb T}(z,0)V(f)\) for almost every \(z\). Write the nonzero zero-total-mass signed derivative as \(Df=\nu^+-\nu^-\). If two points in the supports of \(\nu^+\) and \(\nu^-\) had geodesic distance strictly smaller than \(\pi\), then an oriented arc of length strictly below \(\pi\) could contain positive masses from each, on an open set of arc origins and lengths. On those arcs, \(|Df(I)|<|Df|(I)\), making the translation estimate strict for a positive-measure set of \(z\), a contradiction. Every positive-support/negative-support pair must therefore be antipodal. Since both masses are nonzero, this forces \(\nu^+=c\delta_a\) and \(\nu^-=c\delta_{a+\pi}\) for some \(c>0\); integration gives exactly a constant plus a nonzero half-circle step, with either sign and arbitrary rotation.

**3. Gaussian drift and Fourier normalization.** Brownian motion with variance \(2t\) and deterministic drift \(bt\) gives the convolution law of \(P_t^{(b)}\). The triangular geodesic-distance function has the absolutely and uniformly convergent Fourier expansion
\[
d_{\mathbb T}(z,0)=\frac\pi2-\frac4\pi\sum_{\substack{k\ge1\\k\ \mathrm{odd}}}\frac{\cos(kz)}{k^2}.
\]
The Gaussian character expectation equals \(e^{-k^2t}\cos(kbt)\), yielding the exact series. Strict positivity of the heat density proves rigidity in step 2.

**4. Phase-optimality.** At fixed \(t>0\), set \(F_t(s)=\mathbb E d_{\mathbb T}(s+\sqrt{2t}Z,0)\). This is a smooth even periodic heat evolution of \(d_{\mathbb T}\). Its derivative \(\partial_sF_t\), restricted to \((0,\pi)\), is the Dirichlet heat evolution of the initial constant function one: the initial sign function is odd about both endpoints. The positivity-improving Dirichlet heat kernel gives \(\partial_sF_t(s)>0\) for \(0<s<\pi\). The two endpoints are therefore the only phase minimum and maximum, modulo full turns.

**5. Recurrence and localization.** Termwise differentiation is justified for \(t>0\):
\[
C_b'(t)=\frac4\pi\sum_{\substack{k\ge1\\k\ \mathrm{odd}}}e^{-k^2t}\left[\cos(kbt)+\frac b k\sin(kbt)\right].
\]
For \(\beta=|b|\), the contribution from \(k=1\), after multiplication by \(\pi e^t/4\), is
\[
F(t)=\cos(\beta t)+\beta\sin(\beta t)
=\sqrt{1+\beta^2}\cos(\beta t-\arctan\beta).
\]
The sum of the remaining odd modes, together with its time derivative, is \(O_\beta(e^{-8t})\), uniformly as \(t\to\infty\). Every sufficiently late simple zero of \(F\) therefore has exactly one nearby zero of \(C_b'\): on fixed-width disjoint neighborhoods \(F'\) has magnitude bounded below and the perturbation is small in \(C^1\), while outside these neighborhoods \(|F|\) is bounded below. The mean-value theorem gives the stated \(O_\beta(e^{-8t_n^{(0)}})\) displacement. Since \(F\) changes from positive to negative at even \(n\) and conversely at odd \(n\), the extrema alternate. Substitution into the first Fourier mode and the \(O(e^{-9t})\) tail yields the displayed signed deviations. If \(b=0\), instead \(C_0'(t)=(4/\pi)\sum_{k\ \mathrm{odd}}e^{-k^2t}>0\).

## Verification

The standalone `check.py` evaluates the exact Fourier series independently of periodic-grid semigroup action, including positive and negative drift and nonsmooth half-circle steps. It compares 16 half-circle numerical sharpness cases, 80 random-input upper bounds, 48 shorter-arc bounds and 16 asymptotic critical-time cases: 160 finite numerical comparisons in all. It also prints the first four numerical critical times for unit drift. Running `python check.py` with NumPy and SciPy reports `PASS 160 independent numerical comparisons`. These finite calculations are consistency checks only; they do not prove the infinite-series estimate or equality classification, which follow analytically above.

## Relationship to prior work

Delon, Rabin and Gousseau developed circular geodesic transportation formulae in arXiv:0906.5499; those concern transport between probability histograms rather than the BV-to-\(L^1\) identity defect of advection–diffusion. Carneiro, Finder and Sousa's arXiv:1512.02715 treats variation diminution for convolution-type **maximal operators** on the line, torus and sphere; the operator, norm, drift and temporal question differ. Classical symmetric heat and Fejér-kernel special-case variation statements do not imply either the formula for arbitrary nonsymmetric kernels or the repeated drift-induced temporal extrema. The result does not claim novelty for Gaussian Fourier diagonalization, the basic translation inequality or elementary heat-kernel positivity separately.

## Limitations

The full equality characterization uses a strictly positive convolution density; for atomic or non-full-support laws there may be additional extremizers. The eventual critical-point classification is asymptotic for each fixed nonzero drift and does not count every finite-time turning point. No assertion concerns nonlinear maximal operators, higher-dimensional tori, spatially variable drift or numerical time stepping. Historical priority outside the inspected accessible sources cannot be ruled out; independent mathematical validation has not been performed.

## References

1. J. Delon, J. Rabin and Y. Gousseau, *Transportation Distances on the Circle and Applications*, arXiv:0906.5499, first submitted 2009-06-30, https://arxiv.org/html/0906.5499v3.
2. E. Carneiro, R. Finder and M. Sousa, *On the variation of maximal operators of convolution type II*, arXiv:1512.02715, first submitted 2015-12-09, https://arxiv.org/abs/1512.02715.
3. J. Hou, F. Simons and R. Hinkelmann, *Improved total variation diminishing schemes for advection simulation on arbitrary grids*, DOI:10.1002/fld.2700, online 2011-11-14; related finite-volume methodology rather than the continuous-time operator claim, https://doi.org/10.1002/fld.2700.
