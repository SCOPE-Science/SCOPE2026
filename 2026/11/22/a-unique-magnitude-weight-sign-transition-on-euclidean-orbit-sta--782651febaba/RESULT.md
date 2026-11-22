# A unique magnitude-weight sign transition on Euclidean orbit stars and its sharp polygon-to-circle law

## Finding

For a finite Euclidean configuration consisting of one site and a transitive equidistant rim, its central magnitude weighting has **at most one positive-scale sign change**. Its existence is characterized exactly by comparing the central radius with the mean of the rim's mutual distances. When the rim is a regular polygon, the sign change always occurs and its critical scale has an exact second-order polygon-to-circle limit. Divisible polygon orders have strictly increasing critical scales.

**Theorem (all scales and the circle limit).** Let \(n\ge3\), \(d\ge2\), and let \(X=\{o,x_0,\ldots,x_{n-1}\}\subset\mathbb R^d\) consist of distinct sites such that \(\|o-x_j\|=r>0\) for all \(j\), and the isometry group of the rim \(V=\{x_j\}\) acts transitively on \(V\). Write \(\ell_j=\|x_0-x_j\|\) and \(\bar\ell=n^{-1}\sum_j\ell_j\). For \(t>0\), the unique magnitude weighting \(w_t\) is defined by
\[
\sum_{y\in X} e^{-t\|x-y\|}w_t(y)=1\qquad(x\in X).
\]
Then every rim weight is strictly positive. The central weight is strictly positive at every \(t>0\) if \(r\ge\bar\ell\), whereas if \(r<\bar\ell\), there exists exactly one \(t_*>0\) such that
\[
w_t(o)<0\quad(0<t<t_*),\qquad w_{t_*}(o)=0,\qquad w_t(o)>0\quad(t>t_*).
\]

For the centered regular \(n\)-gon of circumradius one in \(\mathbb R^2\), denote this unique threshold by \(t_n\). It is the unique positive root of
\[
\frac1n\sum_{j=0}^{n-1}\exp\!\left(-2t_n\sin\frac{\pi j}{n}\right)=e^{-t_n}.
\]
Define
\[
I(t)=\int_0^1 e^{-2t\sin(\pi x)}\,dx,
\quad I(t_\infty)=e^{-t_\infty},\quad
D=I'(t_\infty)+e^{-t_\infty}.
\]
The positive root \(t_\infty\) is unique, \(D>0\), and
\[
\boxed{\ t_n=t_\infty-\frac{\pi t_\infty}{3D}\,n^{-2}+O(n^{-4})\ }.
\]
In particular \(t_\infty=1.3635148157\ldots\) and \(\pi t_\infty/(3D)=21.01412167\ldots\). For every pair of integers \(n\ge3\), \(m\ge2\), the exact inequalities
\[
\boxed{\quad 0<t_n<t_{mn}<t_\infty\quad}
\]
hold. The asymptotic coefficient is positive and is the sharp coefficient of \(n^{-2}\).

## Assumptions and scope

All distances are **ordinary Euclidean (chordal) distances**, not squared Euclidean distances or intrinsic arc lengths. The rim is a finite isometry-transitive set on the sphere of radius \(r\) centered at \(o\). No assumption that \(o\) lies in the convex hull of the rim is needed. Only the scalar weighting of \(o\) is classified; the magnitude itself is not claimed monotone. In the polygon case the circumradius is exactly one, so \(t\) is dimensionless under this normalization; scaling the entire configuration by \(R\) divides its threshold by \(R\).

## Proof

**1. Strict positive definiteness.** For distinct Euclidean points, \(Z_t(x,y)=e^{-t\|x-y\|}\) is strictly positive definite for every \(t>0\). Indeed the subordination identity
\[
e^{-t\sqrt u}=\frac{t}{2\sqrt\pi}\int_0^\infty s^{-3/2}
\exp\!\left(-\frac{t^2}{4s}\right)e^{-su}\,ds\qquad(u\ge0)
\]
expresses the Euclidean-distance kernel as a strictly positive mixture of Gaussian kernels \(e^{-s\|x-y\|^2}\). Each Gaussian matrix on distinct points is strictly positive definite by its strictly positive Fourier density. Therefore the weighting exists uniquely for every positive scale.

**2. Two-by-two reduction and sign.** Rim transitivity and uniqueness give a common rim weight \(a(t)\), with central weight \(b(t)\). Put \(E=e^{-rt}\), \(Q=\sum_j e^{-t\ell_j}\). The weighting equations at the central and rim sites are
\[
b+nEa=1,\qquad Eb+Qa=1.
\]
The restriction of \(Z_t\) to the subspace spanned by the center indicator and the constant rim vector is positive definite, so \(Q-nE^2>0\). Solving gives
\[
a=\frac{1-E}{Q-nE^2}>0,\qquad b=\frac{Q-nE}{Q-nE^2}.
\]
The sign of \(b\) is that of
\[
F(t)=e^{rt}Q-n=\sum_{j=0}^{n-1}e^{(r-\ell_j)t}-n.
\]
Here \(F(0)=0\), \(F'(0)=n(r-\bar\ell)\), and
\[
F''(t)=\sum_j(r-\ell_j)^2e^{(r-\ell_j)t}>0,
\]
because \(\ell_0=0\) and \(r>0\). Also \(F(t)\to\infty\) because the \(j=0\) term grows as \(e^{rt}\), whereas the other terms are positive. If \(r\ge\bar\ell\), strict convexity gives \(F(t)>0\) for every \(t>0\). Otherwise \(F\) is negative immediately after zero and, by strict convexity and divergence, has a unique positive zero, negative before and positive after. This proves the classification with no finite-range sampling argument.

For clarity, at the microscopic endpoint the central weight is
\[
\lim_{t\downarrow0}b(t)=\frac{r-\bar\ell}{2r-\bar\ell}.
\]
The denominator is strictly positive: every rim chord is at most \(2r\), one chord is zero, and \(n\ge3\). This endpoint identity alone does not imply the all-scale uniqueness above.

**3. Polygon geometry and the limiting root.** For the centered unit regular polygon, \(\ell_j=2\sin(\pi j/n)\) and
\[
\bar\ell=\frac2n\cot\frac\pi{2n}>1.
\]
For the strict inequality, put \(z=\pi/(2n)\le\pi/6\). The function \(z\cot z\) decreases on \((0,\pi/2)\) because \(\sin z\cos z<z\). Therefore \((4/\pi)z\cot z\ge 2\sqrt3/3>1\). Part 2 supplies the unique threshold \(t_n\).

Let \(H(t)=I(t)-e^{-t}\). The integral version \(F_\infty(t)=e^t I(t)-1\) has strictly positive second derivative (integrate \((1-2\sin(\pi x))^2e^{(1-2\sin(\pi x))t}\)), \(F_\infty(0)=0\), \(F_\infty'(0)=1-4/\pi<0\), and \(F_\infty(t)\to\infty\) because every sufficiently small interval near \(x=0\) has \(2\sin(\pi x)<1\). Hence it has exactly one positive zero \(t_\infty\) and crosses it with positive derivative. Consequently \(H'(t_\infty)=D>0\).

Set \(f_t(x)=e^{-2t\sin(\pi x)}\) for \(0\le x\le1\). For \(t\) in any fixed compact subset of \((0,\infty)\), Euler--Maclaurin for the endpoint-matched trapezoidal average, with \(f_t(0)=f_t(1)\), yields uniformly
\[
\frac1n\sum_{j=0}^{n-1}f_t(j/n)=I(t)+\frac{f_t'(1)-f_t'(0)}{12n^2}+O(n^{-4})
=I(t)+\frac{\pi t}{3n^2}+O(n^{-4}).
\]
Here \(f_t'(0)=-2\pi t\) and \(f_t'(1)=2\pi t\). The Riemann sums converge uniformly on compact \(t\)-intervals. Their unique roots therefore converge to \(t_\infty\) (the opposite fixed signs on either side trap each root). The implicit-root expansion at \(D>0\) first gives \(t_n-t_\infty=O(n^{-2})\), then substitution into the displayed Euler--Maclaurin expansion gives
\[
D(t_n-t_\infty)+\frac{\pi t_\infty}{3n^2}+O(n^{-4})=0,
\]
which is the claimed sharp second-order law.

**4. Strict divisibility order.** Fix \(t>0\) and define the continuous circular function \(g_t(\theta)=e^{-t\sqrt{2-2\cos\theta}}\). The subordination identity in Step 1 gives
\[
g_t(\theta)=\int_0^\infty \rho_t(s)e^{-2s}e^{2s\cos\theta}\,ds,
\qquad \rho_t(s)>0.
\]
Every Fourier coefficient \(c_k(t)\) of \(g_t\) is **strictly positive**: the power expansion of \(e^{2s\cos\theta}\) has nonnegative Fourier coefficients, and the term of order \(|k|\) contributes positively at frequency \(k\). Absolute convergence of the Fourier series follows also from the piecewise smooth first derivative of \(g_t\), which gives \(c_k=O(k^{-2})\). For \(n\ge3\) the roots-of-unity filter yields the exact identity
\[
\frac1n\sum_{j=0}^{n-1}g_t(2\pi j/n)
=c_0(t)+2\sum_{k\ge1}c_{kn}(t),\qquad c_0(t)=I(t).
\]
Thus this discrete average is strictly larger than its integral, and for a proper multiple \(mn\), it is strictly smaller than the \(n\)-point average. Subtracting \(e^{-t}\) preserves these comparisons. At \(t=t_n\), the \(mn\)-point difference is strictly negative, placing its unique positive zero later: \(t_n<t_{mn}\). At \(t=t_\infty\), every finite-point difference is positive, so \(t_{mn}<t_\infty\). This proves the remaining strict inequalities.

## Verification

`center_magnitude_verify.py` uses only the Python standard library. Execute with `python3 center_magnitude_verify.py`. It independently solves all \((n+1)\)-site kernel systems by Gaussian elimination for \(3\le n\le19\), compares 102 explicit polygon weight vectors at both sides of their transitions, also checks twelve positive-only three-rim spherical cases, and tests thirteen orders for positive-root uniqueness bracketing, divisibility inequalities and numerical approach to the sharp asymptotic coefficient. It prints the computed \(t_\infty\), \(D\), and coefficient. These finite numerical checks are supplementary; Steps 1--4 supply the infinite proofs.

## Relationship to prior work

Roff and Willerton introduce scale-dependent weighting and the *microscopic* limit for strictly negative-type metric spaces [1]; the present result uses those definitions but studies the sign **for every positive scale** of a particular geometric extension. Devriendt relates positivity of finite magnitude weightings to circumcenter containment in a similarity embedding [2], a general equivalence that does not evaluate the one-crossing criterion or circular \(n^{-2}\) scale law. The cyclic two-chunk metric construction [3] likewise permits block-constant weights but has two equal-size orbits, not a singleton-plus-transitive-rim geometry. The closest known centered-spherical-cloud microscopic observation concerns only the limit as \(t\downarrow0\), not the unique finite transition or its regular-polygon asymptotic.

## Limitations

The global sign dichotomy needs a unique, transitive rim on a common Euclidean sphere and does not extend as stated to arbitrary unequal radii or non-Euclidean distance kernels. The polygon critical values are defined implicitly; no elementary closed form is asserted. The theorem makes no claim of novelty for the general magnitude definitions, the basic two-by-two symmetry reduction, the microscopic negative-center observation, Gaussian subordination or Euler--Maclaurin in isolation. Unindexed sources on symmetric magnitude weightings or discretized circle kernels could contain an equivalent all-scale or asymptotic result. Independent mathematical validation is not included.

## References

1. Emily Roff and Simon Willerton, *The microscopic weighting on a metric space*, arXiv:2607.05349, first submitted 6 July 2026, https://arxiv.org/abs/2607.05349. Section 1 (weightings) and Theorems 4.11, 5.11 (microscopic geometry).
2. Karel Devriendt, *The geometry of magnitude for finite metric spaces*, arXiv:2510.14684, first submitted 16 October 2025, https://arxiv.org/abs/2510.14684. Theorem 2.12 and Proposition 5.3.
3. *Small-Scale Magnitude Below One for Cyclic Two-Chunk Finite Metric Spaces*, arXiv:2606.00707, https://arxiv.org/abs/2606.00707. Related two-orbit calculation; full text was not accessed for comparison.
4. Mark W. Meckes, *Positive definite metric spaces*, arXiv:1012.5863, https://arxiv.org/abs/1012.5863. Background on positive definiteness for Euclidean metric kernels.
