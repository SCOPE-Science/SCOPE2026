# Optimal fourth-root symmetry stability for the three-point semicircle probability

## Finding
Let \(f\) be a strictly positive, continuously differentiable probability density on the oriented unit circle, regarded as a \(2\pi\)-periodic function. Choose three independent points whose angular density is \(f\), and write \(p(f)\) for the probability that the origin lies outside their convex hull. Define
\[
\Delta(f)=p(f)-\frac34,\qquad
T(f)=\frac12\int_0^{2\pi}|f(\theta)-f(\theta+\pi)|\,d\theta.
\]
Here \(T(f)\) is the total variation distance between the angular law and its antipodal image. Let \(m=\min f>0\), \(M=\max f\), \(L=\|f'\|_\infty\), and let
\[
\widehat f(k)=\frac1{2\pi}\int_0^{2\pi} f(\theta)e^{-ik\theta}\,d\theta.
\]

**Quantitative stability theorem.** With
\[
G(\theta)=\int_\theta^{\theta+\pi} f(t)\,dt,
\]
one has the exact identities and bounds
\[
\boxed{\Delta(f)=3\int_0^{2\pi} f(\theta)\bigl(G(\theta)-\tfrac12\bigr)^2\,d\theta},
\]
\[
\boxed{24\pi m\!\sum_{k\in2\mathbb Z+1}\frac{|\widehat f(k)|^2}{k^2}
\le\Delta(f)\le
24\pi M\!\sum_{k\in2\mathbb Z+1}\frac{|\widehat f(k)|^2}{k^2}}.
\]
If \(L>0\), the following explicit nonlinear rigidity estimate holds:
\[
\boxed{\Delta(f)\ge\frac{3m}{2\pi^3L^2}T(f)^4},\qquad
\boxed{T(f)\le\left(\frac{2\pi^3L^2}{3m}\Delta(f)\right)^{1/4}}.
\]
If \(L=0\), then \(f\) is uniform and \(T=\Delta=0\).

**Optimal exponent.** No power exponent greater than \(1/4\) can replace \(1/4\) uniformly among densities with the same positive lower bound and derivative bound. Specifically, for every odd integer \(k\ge3\), put
\[
f_k(\theta)=\frac{1+k^{-1}\cos(k\theta)}{2\pi}.
\]
These all satisfy \(\min f_k\ge 1/(3\pi)\), \(\|f_k'\|_\infty=1/(2\pi)\), and
\[
T(f_k)=\frac2{\pi k},\qquad \Delta(f_k)=\frac3{2\pi^2k^4}.
\]
Therefore \(T(f_k)\) is a positive constant times \(\Delta(f_k)^{1/4}\), disproving any uniformly stronger Hölder exponent.

## Assumptions and scope
All density bounds are with respect to the angle coordinate in radians and ordinary Lebesgue measure. A density is a positive \(C^1\) periodic function of total integral one. The three points are independently and identically sampled; with probability one no two coincide or are antipodal. The antipodal image has density \(\theta\mapsto f(\theta+\pi)\). The bounds compare the **population probability** with the known extremal value \(3/4\); neither sampling error nor arbitrary non-Lipschitz densities are covered by the stated fourth-root estimate.

## Proof
**1. Exact semicircle probability.** With probability one, three sampled points have a unique counterclockwise starting point for a containing closed semicircle if they all fit in one. Indeed the three consecutive circular gaps sum to \(2\pi\) and the event is equivalent to one gap exceeding \(\pi\), which can happen for at most one gap. Conditional on the starting point having angle \(\theta\), the remaining two points both lie in the following semicircle with probability \(G(\theta)^2\). Summing disjoint starting-point events proves
\[
p(f)=3\int_0^{2\pi}f(\theta)G(\theta)^2\,d\theta.
\]
For two independent angular points the event that the second falls counterclockwise within a half-turn of the first has probability \(1/2\), since interchanging their labels exchanges it with its complement apart from a null set. Thus \(\int fG=1/2\). Consequently \(\Delta=3\int f(G-1/2)^2\). In particular equality in the already-known qualitative bound holds precisely when \(G\equiv1/2\): positivity of \(f\) makes its full-support statement immediate, and differentiating \(G\) gives \(f(\theta+\pi)=f(\theta)\).

**2. Spectral identification.** Set \(u=G-1/2\) and \(h(\theta)=f(\theta)-f(\theta+\pi)\). Then
\[
u(\theta+\pi)=-u(\theta),\qquad u'(\theta)=-h(\theta).
\]
The Fourier coefficients of \(u\) vanish for even integers and obey
\[
\widehat u(k)=-\frac{2\widehat f(k)}{ik} \quad (k\text{ odd}).
\]
Parseval yields the exact identity
\[
\|u\|_{L^2(0,2\pi)}^2=8\pi\sum_{k\in2\mathbb Z+1}\frac{|\widehat f(k)|^2}{k^2}.
\]
Since \(m\le f\le M\), sandwiching the weighted integral \(3\int fu^2\) between \(3m\|u\|_2^2\) and \(3M\|u\|_2^2\) proves both spectral bounds, with no omitted Fourier modes.

**3. Nonlinear inverse stability.** Let \(T=\|h\|_1/2\). Integration by parts and periodicity, followed by Cauchy--Schwarz, imply
\[
\|h\|_2^2=\int_0^{2\pi}u(\theta)h'(\theta)\,d\theta
\le\|u\|_2\|h'\|_2.
\]
By Cauchy--Schwarz in the other direction and the derivative bound,
\[
\|h\|_2^2\ge\frac{\|h\|_1^2}{2\pi}=\frac{2T^2}{\pi},\qquad
\|h'\|_2\le 2L\sqrt{2\pi}.
\]
Therefore
\[
\|u\|_2\ge\frac{T^2}{\pi L\sqrt{2\pi}},
\quad\text{and}\quad
\Delta\ge3m\|u\|_2^2\ge\frac{3mT^4}{2\pi^3L^2}.
\]
The derivative estimate applies when \(L>0\); if \(L=0\), periodicity and normalization force the constant density \(1/(2\pi)\).

**4. Sharpness of the fourth-root *power*.** For the explicit family with odd \(k\), elementary integration gives
\[
G_k(\theta)-\frac12=-\frac{\sin(k\theta)}{\pi k^2}.
\]
Its density satisfies \(\min f_k=(1-k^{-1})/(2\pi)\ge1/(3\pi)\), while \(\max|f_k'|=1/(2\pi)\). Since \(\int_0^{2\pi}\cos(k\theta)\sin^2(k\theta)\,d\theta=0\), the exact deficit is \(3/(2\pi^2k^4)\). Its antipodal difference is \(\cos(k\theta)/(\pi k)\); using \(\int_0^{2\pi}|\cos(k\theta)|\,d\theta=4\) gives \(T=2/(\pi k)\). Thus, for every \(\beta>1/4\), the ratio \(T(f_k)/\Delta(f_k)^\beta\) tends to infinity through odd \(k\). This proves optimality of the Hölder exponent but **not** of the numerical prefactor in the displayed bound.

## Verification
A self-contained Python standard-library verifier (`verify_wendel_stability.py`) independently integrates the probability formula for four trigonometric densities, simulates 280,000 independent three-point configurations using rejection sampling and the maximum-circle-gap test, checks single-harmonic exact formulas, and tests the exact fourth-power scaling and explicit lower bound for four odd frequencies. It emitted `VERIFY_OK formulas=4 simulated_samples=280000 spectral_exponent_cases=4`. Finite computations serve only as independent consistency checks; the theorem follows from the four analytical steps above.

## Relationship to prior work
Wendel (1962) proved the celebrated distribution-free halfspace/semicircle identity for antipodally symmetric laws. **Wagner and Welzl (2001) already proved the more general extremal inequality and characterized equality for balanced angular laws**. Neither statement is claimed as new here. The present incremental claim is the explicitly quantified spectral deficit and the optimal fourth-root modulus for measuring symmetry by total variation under a Lipschitz regularity constraint. Fodor, Montenegro Pinzón and Vígh (2022) review Wendel's equality but focus on *spindle-convex* random hulls; their theorem concerns a different hull operation. The exact weighted deficit and explicit fourth-root power were not located in the inspected prior comparisons; priority remains provisional.

## Limitations
The prefactor in the fourth-root stability estimate is explicit but **not asserted best possible**. The theorem measures antipodal symmetry, not proximity to the uniform distribution: nonuniform antipodally symmetric densities have zero deficit. If the regularity class does not control the derivative of \(f\), fixed total-variation asymmetry can have arbitrarily small deficit through high-frequency harmonics. The result concerns three sampled points and exact distributional probabilities. Other published inequalities may imply quantitative forms not identified in the inspected sources. Independent scholarly priority review has not been conducted.

## References
1. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica 11 (1962), 109–112, doi:10.7146/math.scand.a-10655 (published 1962-06-01; original full text inspected).
2. U. Wagner and E. Welzl, *A Continuous Analogue of the Upper Bound Theorem*, Discrete & Computational Geometry 26 (2001), 205–219, doi:10.1007/s00454-001-0028-9 (author-hosted full text inspected; qualitative extremality and equality are established there).
3. F. Fodor, N. A. Montenegro Pinzón and V. Vígh, *On Wendel's Equality for Intersections of Balls*, Aequationes Mathematicae 97 (2023), 439–451, doi:10.1007/s00010-022-00912-3 (first published 2022-09-10; full open-access HTML inspected).
