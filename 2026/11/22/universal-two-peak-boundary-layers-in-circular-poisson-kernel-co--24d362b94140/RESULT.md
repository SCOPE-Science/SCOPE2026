# Universal two-peak boundary layers in circular Poisson-kernel compression

## Finding
Let
\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2},\qquad
F_{r,a}(\theta)=\frac{P_r(\theta-a)+P_r(\theta+a)}2,
\]
with the fixed separation parameter \(0<a<\pi/2\) and concentration \(0<r<1\). Fit \(F_{r,a}\) by **one normalized Poisson kernel** \(P_t(\cdot-\phi)\), freely choosing \(0\le t<1\) and \(\phi\in\mathbb R/(2\pi\mathbb Z)\), under squared \(L^2(d\theta/(2\pi))\) error. Write \(\mathcal E_a(r)\) for the minimum.

**Theorem.** For each fixed \(a\in(0,\pi/2)\):

1. For all sufficiently small \(r>0\), there is exactly one optimal kernel (the angle of the uniform kernel is immaterial). Its angle is \(\phi=0\), and its strictly positive radius obeys
\[
t_*(r)=r\cos a+O_a(r^3).
\]
2. For all \(r<1\) sufficiently close to one, there are exactly two optimal kernels, interchanged by reflection. Put \(\delta=1-r\), \(k_*=1+\sqrt2\), and
\[
C_a=\frac{(2+\sqrt2)^4\sin(2a)}{4[1-\cos(2a)]^2}>0.
\]
Their parameters have the sharp expansions
\[
t_\pm(r)=1-k_*\delta+O_a(\delta^2),\qquad
\phi_\pm(r)=\pm\left[a-C_a\delta^4+o_a(\delta^4)\right].
\]
The best attainable error diverges with the **universal, strictly positive coefficient**
\[
\mathcal E_a(r)=\frac{2\sqrt2-5/2}{1-r}+O_a(1),
\qquad \lim_{r\uparrow1}(1-r)\mathcal E_a(r)=2\sqrt2-\frac52.
\]
The sharp improvement over fitting the uniform kernel is
\[
\sup_{t,\phi}\left(2\langle F_{r,a},P_t(\cdot-\phi)\rangle-\|P_t\|_2^2-1\right)
=\frac{3-2\sqrt2}{1-r}+O_a(1).
\]
Thus the optimizing direction necessarily changes from a unique bisector to two off-axis branches as concentration grows; the theorem does **not** claim uniqueness or a specified count of intermediate transitions.

## Assumptions and scope
All circle integrals use the probability measure \(d\theta/(2\pi)\), so \(P_r\) has integral one. Radius \(t=0\) denotes the constant-one kernel and is a single function regardless of angle. The two source locations are distinct and nonantipodal, with fixed \(a\in(0,\pi/2)\) independent of \(r\). Big-O constants and the neighborhoods establishing uniqueness may depend on \(a\). Kernel amplitudes and mixture weights are **not** optimized: each source has fixed weight \(1/2\), and the fitted kernel retains its mean-one normalization. Excluded are coincident or antipodal source endpoints, changing separation as \(r\uparrow1\), signed mixture weights, and other discrepancy metrics.

## Proof
**1. Exact reduction and existence.** The Fourier series \(P_q(\theta)=1+2\sum_{n\ge1}q^n\cos(n\theta)\) yields the Poisson convolution identity
\[
\langle P_r(\cdot-\xi),P_t(\cdot-\phi)\rangle=P_{rt}(\phi-\xi).
\]
Consequently, minimizing squared error is equivalent to maximizing
\[
J_{r,a}(t,\phi)=P_{rt}(\phi-a)+P_{rt}(\phi+a)-\frac{1+t^2}{1-t^2}.
\tag{1}
\]
At \(t=0\), \(J=1\). For any fixed \(r<1\), the two positive terms are bounded uniformly as \(t\uparrow1\), while the negative term tends to minus infinity, so a maximizer exists.

**2. The low-concentration unique branch.** Use the disk coordinate \(z=t e^{i\phi}\). From \(P_q(\theta)\le1+2q/(1-q)\), every competitor satisfying \(J\ge1\) must obey
\[
0\le J-1\le\frac{4rt}{1-rt}-\frac{2t^2}{1-t^2},
\qquad t\le\frac{2r}{1-r}.
\tag{2}
\]
For \(r\) small, all maximizers thus lie in a disk \(|z|=O(r)\). In the real coordinates \(z=x+iy\), exact Fourier expansion of (1) gives, uniformly with two derivatives on that disk,
\[
J-1=4r\cos(a)x-2(x^2+y^2)+4r^2\cos(2a)(x^2-y^2)-2(x^2+y^2)^2+O_a(r^3|z|^3+|z|^6).
\tag{3}
\]
Its real Hessian is \(-4I+O_a(r^2)\), hence negative definite throughout the disk for sufficiently small \(r\). The maximum is unique. Reflection \(y\mapsto-y\) forces \(y=0\); the critical equation gives \(x=r\cos a+O_a(r^3)>0\). Thus \(\phi=0\), and the first assertion follows. The unique maximizer is interior because the first-order gain at \(z=0\) in the positive real direction is positive.

**3. A sharp universal one-peak blow-up problem.** Put \(\delta=1-r\) and \(t=1-k\delta\). If \(\phi=a+\delta s\) and \(k>0\) and \(s\in\mathbb R\) range over compact subsets, a direct Taylor expansion of the rational Poisson kernel, including two derivatives in \((k,s)\), yields
\[
\delta(J_{r,a}(1-k\delta,a+\delta s)-1)
=G(k,s)+O_a(\delta),\qquad
G(k,s)=\frac{2(1+k)}{(1+k)^2+s^2}-\frac1k.
\tag{4}
\]
The second source contributes only \(O_a(\delta^2)\) after multiplying the objective by \(\delta\). For fixed \(k\), \(G\) is strictly maximized at \(s=0\). The remaining function \(g(k)=2/(1+k)-1/k\) has exactly one global maximizer on \(k>0\): the derivative equation \((1+k)^2=2k^2\) gives \(k=k_*=1+\sqrt2\), with
\[
G(k_*,0)=3-2\sqrt2>0.
\tag{5}
\]
The \((k,s)\) Hessian of \(G\) at this point is strictly negative definite: its diagonal entries are \(4/(1+k_*)^3-2/k_*^3<0\) and \(-4/(1+k_*)^3<0\), and the mixed entry is zero.

**4. No hidden competing global maxima.** Equation (4) at \((k_*,0)\) gives a competitor with \(J-1\ge c/\delta\) for some fixed \(c>0\). A global maximizer therefore satisfies \(P_{rt}(\phi-a)+P_{rt}(\phi+a)\ge c/\delta\); at least one Poisson term is at least \(c/(2\delta)\). The elementary bound \(P_q(\theta)\le2/(1-q)\) forces \(1-rt=O(\delta)\), hence \(1-t=O(\delta)\). Its exact denominator \((1-rt)^2+2rt(1-\cos\theta)\) then forces the relevant circular angular distance to one source to be \(O(\delta)\). The other source remains separated by \(2a>0\) and contributes \(O_a(\delta)\) to \(J\). If \((1-t)/\delta\to0\), the negative term \(-\delta(1+t^2)/(1-t^2)\to-\infty\) while the positive terms remain bounded after scaling, contradicting (5). Thus \(k=(1-t)/\delta\) stays within a compact subset of \((0,\infty)\), and the scaled displacement \(s\) remains bounded. Every accumulation point must maximize \(G\), so it must be \((k_*,0)\).

By the negative Hessian in step 3 and the analytic implicit-function theorem applied to the scaled stationary equations, each sufficiently small fixed neighborhood of either limiting source contains exactly one critical point near \((k_*,0)\). Compactness from the preceding paragraph places every global maximizer in one of these neighborhoods. Reflection \(\phi\mapsto-\phi\) gives equal values, so there are **exactly two** global maximizers for sufficiently small \(\delta\), and their fitted depths satisfy \(1-t=k_*\delta+O_a(\delta^2)\). The scaled maximum in (4) equals \(3-2\sqrt2+O_a(\delta)\), proving the stated gain expansion.

**5. Sharp inward angular displacement.** Work near the positive source, writing \(\phi=a+h\). Angular stationarity is
\[
P_q'(h)+P_q'(2a+h)=0,\quad q=rt,
\qquad P_q'(u)=\frac{-2q(1-q^2)\sin u}{(1-2q\cos u+q^2)^2}.
\tag{6}
\]
The scaled stationary equation and strict nondegeneracy of the limiting angular Hessian first imply \(h=O_a(\delta^4)\): the far-source derivative is \(O_a(\delta)\), whereas the near-source curvature is of order \(-\delta^{-3}\). More precisely, since \(q=1-(2+\sqrt2)\delta+O_a(\delta^2)\),
\[
P_q''(0)=-\frac{2q(1+q)}{(1-q)^3}
=-\frac{4+o(1)}{(2+\sqrt2)^3\delta^3},
\quad
P_q'(2a)=-\frac{(2+\sqrt2)\sin(2a)}{[1-\cos(2a)]^2}\delta+o_a(\delta).
\tag{7}
\]
Substitution into (6) gives \(h=-C_a\delta^4+o_a(\delta^4)\), with the stated positive \(C_a\). Reflection gives the negative-source branch.

**6. Sharp error.** Another application of Poisson convolution gives
\[
\|F_{r,a}\|_2^2=\frac12\left(P_{r^2}(0)+P_{r^2}(2a)\right)=\frac{1}{2\delta}+O_a(1).
\]
From (1), \(\mathcal E_a(r)=\|F_{r,a}\|_2^2-\max J_{r,a}\). Steps 3–4 give \(\max J=1+(3-2\sqrt2)/\delta+O_a(1)\). Their difference proves the error expansion and its positive coefficient.

## Verification
A standalone \(\texttt{check.py}\) checks Poisson convolution against independent numerical integration, differentiates the exact rational objective, checks low-radius uniqueness numerically for sample separations, and reproduces the limiting optimal depth, angular \(\delta^4\) coefficient and squared-error constant at small positive \(\delta\). These finite checks are diagnostics, **not** a proof of the global or asymptotic statements. Steps 2–6 above supply those proofs. Run with Python 3 and \(\texttt{mpmath}\) (tested with version 1.3.0): \(\texttt{python check.py}\).

## Relationship to prior work
The wrapped Cauchy density is \(P_r/(2\pi)\). Bailey's thesis (repository released 8 January 2020), chapter 6 and appendix C2, develops Fourier-moment least-squares fitting of **common-center** mixtures and compares wrapped normal versus wrapped Cauchy fits. Its mixture of two wrapped Cauchy densities has a common center and different radial concentration parameters; it does not describe two distinct angular source directions. Bailey and Codling's paper treats mixtures of wrapped normals. Chaubey's 2016 treatment supplies the Poisson/wrapped-Cauchy kernel-estimation motivation, not the present one-kernel projection asymptotics. Earlier results about equal-weight **antipodal** kernel mixtures (the excluded endpoint \(a=\pi/2\)) and **concentric** mixtures (the excluded endpoint \(a=0\)) do not imply the present nonantipodal two-source theorem: in particular, neither has the nonzero inward \(\delta^4\) shift in step 5. Results about selecting observation arcs for two harmonic measures optimize a different functional and do not determine the best single Poisson kernel.

## Limitations
No exact critical concentration or number of intermediate symmetry changes is established. The fixed-separation hypothesis is essential: the expansions are not uniform as \(a\to0\) or \(a\to\pi/2\). The fitted amplitude is fixed, not reweighted. The theorem does not compare nonlinear likelihood, Kullback–Leibler, Wasserstein or other discrepancies, nor higher-dimensional spheres. The literature comparison is best-knowledge; historical priority remains subject to independent verification, including the accepted manuscript of Bailey–Codling which was not fully retrievable during this assessment.

## References
1. J. D. Bailey, *Modelling and Analysis of Individual Animal Movement*, University of Essex PhD thesis (2019), public repository deposit 2020-01-08, chapter 6 and appendix C2. https://repository.essex.ac.uk/26383/
2. J. D. Bailey and E. A. Codling, *Emergence of the wrapped Cauchy distribution in mixed directional data*, AStA Advances in Statistical Analysis 105 (2021), 229–246, first published 2020-10-09. https://doi.org/10.1007/s10182-020-00380-7
3. Y. P. Chaubey, *Smooth Kernel Estimation of a Circular Density Function: A Connection to Orthogonal Polynomials on the Unit Circle*, first posted 2016-01-19, https://arxiv.org/abs/1601.05053 (general background only).
