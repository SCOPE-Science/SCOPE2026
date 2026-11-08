# Sharp positivity frontier for first-order Korobov lattice quadrature under sine periodization

## Finding

Consider the one-dimensional full-lattice kernel quadrature obtained by sine periodization and first-order Korobov interpolation. For **every** integer \(N\ge2\), there is an explicit, finite, positive threshold \(\Gamma_N\) such that all \(N\) unmodified kernel-quadrature weights are nonnegative **if and only if** \(0<\gamma\le\Gamma_N\). All weights are strictly positive below the threshold. Above it, the weight at the mapped endpoint \(x=0\) is strictly negative; this is also a minimum among the weights.

Write

\[
H_N=\frac12-\frac{N}{4\pi}\sin\!\left(\frac{2\pi}{N}\right),
\qquad
B_N=\begin{cases}
\dfrac{1-\frac\pi N\cot(\frac\pi N)}{4\pi^2},&N\text{ even},\\[5pt]
\dfrac1{4\pi^2}-\dfrac{\cot(\frac\pi{2N})}{8\pi N}+\dfrac1{16N^2},&N\text{ odd}.
\end{cases}
\]

Then the sharp threshold is

\[
\boxed{\displaystyle\Gamma_N=
\frac{H_N}{\frac{4\pi^2 B_N}{N}-\frac{\pi^2H_N}{3N^2}}},
\qquad
\boxed{\displaystyle\Gamma_N=N+\frac{\pi^2}{3}+O(N^{-1})}.
\]

In particular, for each fixed \(\gamma>0\), all quadrature weights are eventually **strictly positive**, not merely asymptotically nonnegative in total variation. The exact frontier is not monotone in small \(N\): for example, \(\Gamma_2\approx5.63275666085\), \(\Gamma_3\approx19.26348712387\), and \(\Gamma_4\approx11.15215619868\).

## Assumptions and scope

Let \(\mathbb T=\mathbb R/\mathbb Z\) and \(N\ge2\), and take nodes \(t_j=j/N\), \(j=0,\ldots,N-1\). The periodic first-order Korobov kernel, including its constant Fourier mode, is

\[
K_\gamma(s,t)=1+\gamma\sum_{m\in\mathbb Z\setminus\{0\}}
\frac{e^{2\pi i m(s-t)}}{m^2}
=1+2\pi^2\gamma B_2(\{s-t\}),
\quad B_2(u)=u^2-u+\frac16,
\]

with \(\gamma>0\) and fractional part \(\{\cdot\}\). This kernel is strictly positive definite on distinct grid nodes. The periodization \(x=\psi(t)=\sin^2(\pi t)\) converts uniform integration on \([0,1]\) to integration with probability density

\[
\mu(t)=\frac\pi2|\sin(2\pi t)|.
\]

Let \(G_{ij}=K_\gamma(t_i,t_j)\), \(\kappa_i=\int_0^1 K_\gamma(t_i,t)\mu(t)\,dt\), and \(w=G^{-1}\kappa\). The rule under study is \(Q_{N,\gamma}(f)=\sum_{j=0}^{N-1}w_j f(\psi(t_j))\), without weight normalization, constant exactness correction, or positivity projection. The conclusion concerns every such \(N\) and \(\gamma\), and exact arithmetic.

## Proof

**1. Variational representation.** The reproducing-kernel norm is

\[
\|u\|_{K_\gamma}^2=\left|\int_0^1u(t)\,dt\right|^2+
\frac1{4\pi^2\gamma}\int_0^1|u'(t)|^2\,dt.
\]

For nodal data \(v_j\), their kernel interpolant is the unique minimum-norm periodic \(H^1\) interpolant. Set \(h=1/N\). Let \(L_v\) be the periodic piecewise-linear interpolant and, on cell \([jh,(j+1)h]\), let

\[
b_N(t)=\frac12(t-jh)((j+1)h-t)\ge0.
\]

The Euler equation under nodal constraints is \(u''=4\pi^2\gamma\bar u\) within each open cell, where \(\bar u=\int_0^1u\). Thus

\[
u=L_v-4\pi^2\gamma\bar u\,b_N,
\qquad
\bar u=\frac{N^{-1}\sum_j v_j}{1+\pi^2\gamma/(3N^2)},
\]

since \(\int_0^1 b_N=1/(12N^2)\). The nodal continuity is automatic; derivatives need not match across constrained nodes. Strict convexity of the norm proves this is the unique kernel interpolant.

**2. Every weight has the same subtractive correction.** Let \(\varphi_j\) be the periodic piecewise-linear hat basis, \(L_v=\sum_jv_j\varphi_j\). Define

\[
H_j=\int_0^1\varphi_j(t)\mu(t)\,dt,
\qquad B=\int_0^1b_N(t)\mu(t)\,dt.
\]

Integrating the kernel interpolant against \(\mu\) and comparing its coefficients of \(v_j\) gives the **exact identities**

\[
w_j=H_j-D_{N,\gamma},\qquad
D_{N,\gamma}=\frac{4\pi^2\gamma B}{N(1+\pi^2\gamma/(3N^2))}.
\]

These coincide with the matrix definition \(w=G^{-1}\kappa\) because both compute the integral of the unique kernel interpolant for every data vector.

**3. The smallest hat integral is at zero.** The density has the absolutely convergent Fourier series

\[
\mu(t)=1-2\sum_{m=1}^\infty\frac{\cos(4\pi m t)}{4m^2-1}.
\]

The Fourier coefficient of the hat function at frequency \(2m\) is \(N^{-1}\operatorname{sinc}^2(2\pi m/N)\), with \(\operatorname{sinc}(z)=\sin(z)/z\). Consequently,

\[
H_j=\frac1N-\frac2N\sum_{m=1}^\infty
\frac{\operatorname{sinc}^2(2\pi m/N)}{4m^2-1}
\cos\!\left(\frac{4\pi m j}{N}\right)\ge H_0.
\]

Direct integration over the support of \(\varphi_0\) gives \(H_0=H_N\) from the theorem. The same constant \(D_{N,\gamma}\) is subtracted from each hat integral, so \(w_0\) is a minimum for all \(\gamma\). For \(N\) even, \(w_{N/2}=w_0\) as well. The mapped point \(\psi(t_0)=0\) is unique in the transformed grid, so \(w_0<0\) is a genuine negative weight even after duplicate transformed nodes are combined.

**4. Exact bubble integral.** The periodic bubble \(b_N\) has mean \(1/(12N^2)\) and Fourier coefficient \(-1/(4\pi^2N^2m^2)\) at each nonzero frequency \(mN\), with all other nonzero coefficients vanishing. Combining this with the Fourier coefficients of \(\mu\) yields

\[
B=\frac{1}{12N^2}+\frac1{2\pi^2N^2}
\sum_{\substack{m\ge1\\mN\text{ even}}}
\frac1{m^2((mN)^2-1)}.
\]

All correction summands are strictly positive. Using the classical partial-fraction identity

\[
\sum_{m=1}^\infty\frac1{m^2-a^2}
=\frac1{2a^2}-\frac\pi{2a}\cot(\pi a),\quad 0<a<1,
\]

and separating even \(m\) when \(N\) is odd gives precisely the displayed even/odd closed forms for \(B_N=B\).

**5. Sharp transition and endpoint.** Since \(H_N\le\frac1N\) (the mean of the \(H_j\) is \(1/N\)), whereas the preceding positive series gives \(B_N>1/(12N^2)\),

\[
d_N:=\frac{4\pi^2B_N}{N}-\frac{\pi^2H_N}{3N^2}>0.
\]

Therefore

\[
w_0=\frac{H_N-\gamma d_N}{1+\pi^2\gamma/(3N^2)}.
\]

Every denominator is strictly positive. Thus \(w_j\ge0\) for all \(j\) exactly when \(\gamma\le H_N/d_N=\Gamma_N\), strict for \(\gamma<\Gamma_N\). At equality \(w_0=0\); above it \(w_0<0\). This proves necessity and sufficiency for all integers \(N\ge2\), without finite enumeration.

**6. Asymptotic frontier.** Taylor expansion of the displayed trigonometric expressions gives

\[
H_N=\frac{\pi^2}{3N^2}+O(N^{-4}),\qquad
B_N=\frac{1}{12N^2}+O(N^{-4}).
\]

Substituting into \(d_N\), retaining the \(N^{-4}\) term, yields \(\Gamma_N=N+\pi^2/3+O(N^{-1})\). For fixed positive \(\gamma\), this implies \(\gamma<\Gamma_N\) for all sufficiently large \(N\), establishing eventual strict positivity.

## Verification

The standalone Python 3 script `verify.py` uses analytic primitives for integrals of polynomials against the piecewise sinusoidal density, rather than sampling or evaluating a truncated infinite Fourier series. For \(N=2,\ldots,12\), it independently checks the exact \(H_N\) and \(B_N\) formulas against segmented integration, then solves \(G w=\kappa\) directly at four relative positions on either side of each threshold. It reports `VERIFY_OK` for 44 direct linear-system comparisons, as well as numerical asymptotic checks. The all-\(N\) and asymptotic assertions above follow from the proof, not from those finite tests.

## Relationship to prior work

Bartel, Gilbert, Griebel, Kuo and Sloan (arXiv:2610.01113v1, Sections 2.1, 3.1–3.3 and 7.2) define the Korobov kernel, sine periodization, and kernel-quadrature weight system used here. They establish numerical integration error rates and note that asymptotic positivity is not known for their multivariate method, but give no exact one-dimensional threshold for a negative endpoint weight. Their original method and equations are not claimed as new.

Karvonen, Kanagawa and Särkkä (arXiv:1812.08509v2, Sections 3 and 4) establish other positive-weight conditions, in particular for locally optimized nodes under total positivity, and upper bounds for Sobolev-equivalent kernels. Their hypotheses do not imply the present sharp result for the unoptimized uniform grid and, when \(\gamma\) is large, the sign-changing periodic Korobov kernel. Their general observations on non-unit total mass are credited. Bartel, Gilbert, Kuo and Sloan (arXiv:2506.07729, Sections 2–5) study lattice approximation and sampling error, not positivity under this sine density. The positivity proof relies on the particular Fourier signs of \(\mu\) and the first-order spline structure, rather than on a generic Bayesian-quadrature assertion.

## Limitations

The claim is for one-dimensional **full** lattices, first-order Korobov smoothness \(\alpha=1\), strictly positive kernel weight \(\gamma\), exactly the sine-squared periodization density, and unmodified exact-arithmetic weights. It does not classify higher smoothness, subsampled grids, other densities, multivariate lattices, or weights after ad hoc normalization or positivity projection. A separate independent mathematical audit has not been performed. Priority remains subject to previously unindexed spline/product-integration literature.

## References

1. F. Bartel, A. D. Gilbert, M. Griebel, F. Y. Kuo and I. H. Sloan, *A higher order lattice-based method for high-dimensional numerical integration using periodization*, arXiv:2610.01113v1 (first posted 2026-10-01), https://arxiv.org/html/2610.01113v1 .
2. T. Karvonen, M. Kanagawa and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509, https://arxiv.org/pdf/1812.08509 .
3. F. Bartel, A. D. Gilbert, F. Y. Kuo and I. H. Sloan, *Minimal Subsampled Rank-1 Lattices for Multivariate Approximation with Optimal Convergence Rate*, arXiv:2506.07729, https://arxiv.org/html/2506.07729 .
