# Sharp equilibrium-elimination threshold for a sine–exponential discontinuous interval map

## Finding
For the three-parameter fixed-point-free-map construction in [1], its third (sine–exponential) example has a **sharp, complete equilibrium-elimination frontier**. For every real \(0<a,b,c<1\), define
\[
F_{a,b,c}(x)=\begin{cases}
1-(1-a)\cos^2\!\left(\frac{\pi x}{2b}\right),&0\le x\le b,\\
\displaystyle\frac{c}{e-1}\left(e^{(x-b)/(1-b)}-1\right),&b<x\le1.
\end{cases}
\]
Let \(k=\pi/(2b)\). There is a **unique** \(x_*=x_*(b)\in(0,b/2)\) with
\[
(1-x_*)\tan(kx_*)=\frac{1}{2k}=\frac b\pi.
\]
Set \(a_*(b)=x_*+(x_*-1)\tan^2(kx_*)\). Then \(0<a_*<b\), and the number of fixed points in \([0,1]\) is exactly **two**, **one**, or **zero** according as \(0<a<a_*\), \(a=a_*\), or \(a_*<a<1\). No fixed point occurs on the exponential branch for any allowed parameter. Below threshold the lower fixed point has derivative strictly between zero and one, while the higher fixed point has derivative greater than one. At the threshold the unique fixed point is an ordinary one-sided attracting/repelling saddle-node (multiplier one). The curve \(a_*(b)\) is strictly increasing and has
\[
a_*(b)=\frac{b^2}{\pi^2}+O(b^4)\qquad(b\downarrow0).
\]
For fixed \(b\), set \(t_*=kx_*\) and
\[
K(b)=\frac{\cos t_*}{k\sqrt{(1-a_*)\cos(2t_*)}}>0.
\]
The two fixed points for \(a=a_*-\delta\) are \(x_*\pm K(b)\sqrt\delta+O(\delta)\) as \(\delta\downarrow0\).

## Assumptions and scope
The state space is exactly \([0,1]\), all three parameters are strictly between zero and one, and the discontinuity convention is **left-closed at \(b\)**. All assertions concern literal fixed points, not virtual points or discontinuity-hitting orbit closures. The derivative/multiplier statements concern smooth interior fixed points. No assertion about higher-period dynamics, entropy, cryptographic behavior, or global convergence is made.

## Proof
Write \(t=kx\). On \(b<x\le1\), the right branch is strictly convex, with limiting value zero at \(b+\) and value \(c<1\) at one. By convexity it lies below the chord joining \((b,0)\) and \((1,c)\), and that chord is strictly below the diagonal \(y=x\). Thus no right-branch fixed point exists.

On \(0\le x\le b\), the fixed-point displacement is
\[
D_a(x)=a\cos^2(kx)+\sin^2(kx)-x
=\cos^2(kx)[a-A_b(x)],
\quad A_b(x)=x+(x-1)\tan^2(kx).
\]
Here \(D_a(0)=a>0\), \(D_a(b)=1-b>0\), \(A_b(0)=0\), and \(A_b(x)\to-\infty\) as \(x\uparrow b\). Direct differentiation gives
\[
A'_b(x)=\sec^2(kx)\left[1-2k(1-x)\tan(kx)\right].
\]
The function \(E_b(x)=(1-x)\tan(kx)\) is strictly increasing from zero to infinity, because
\[
E'_b(x)=\frac{k(1-x)-\sin(kx)\cos(kx)}{\cos^2(kx)}>0.
\]
Indeed, \(k(1-x)=k(1-b)+(\pi/2-kx)\), and \(\sin t\cos t<\pi/2-t\) for \(0<t<\pi/2\) (put \(u=\pi/2-t\) and use \(\sin(2u)<2u\)). Therefore \(A_b\) increases strictly to one maximum at \(x_*\) and decreases strictly afterwards. Moreover \(E_b(b/2)=1-b/2>b/\pi\); hence \(x_*<b/2\) and \(\cos(2t_*)>0\). Since \(A_b\) rises above its initial value zero, \(a_*>0\). Since the left branch at \(a=b\) satisfies \(F_{b,b,c}(x)\ge b>x\) for \(x<b\), its displacement is strictly positive throughout, giving \(a_*<b\). Horizontal-line intersections with \(A_b\) yield precisely two, one, or zero equilibria.

At a simple root \(D_a(x)=\cos^2(kx)(a-A_b(x))\), differentiation along the root gives \(F'(x)-1=-\cos^2(kx)A'_b(x)\). The smaller root lies on the increasing portion, so \(0<F'<1\); the larger lies on the decreasing portion, so \(F'>1\). At equality \(F'(x_*)=1\) and \(F''(x_*)=2(1-a_*)k^2\cos(2t_*)>0\): thus the displacement has a strict quadratic minimum zero. This yields the stated one-sided stability. Taylor expansion
\[
0=D_{a_*-\delta}(x_*+z)
=-\delta\cos^2t_*+(1-a_*)k^2\cos(2t_*)z^2+O(|z|^3+\delta|z|)
\]
proves the square-root splitting and its constant.

For fixed \(x\in(0,b)\), the derivative of \(A_b(x)=x+(x-1)\tan^2(\pi x/(2b))\) with respect to \(b\) is strictly positive. Thus the maximum \(a_*(b)\) strictly increases with \(b\): compare a maximizing \(x\) at the smaller \(b\) (which remains in the larger domain). Finally the unique critical equation at small \(b\) gives \(kx_*=b/\pi+O(b^3)\) and \(x_*=2b^2/\pi^2+O(b^4)\); substituting in \(A_b(x_*)\) gives \(a_*(b)=b^2/\pi^2+O(b^4)\).

## Verification
The standalone checker `verify.py` tests the unique critical equation, sign regimes, branch inequalities and root counts using independent numerical root routines over a parameter grid. Its checks are supporting finite illustrations: the preceding monotonicity and Taylor arguments prove the all-parameter statements.

## Relationship to prior work
Lawnik, Moysis and Volos [1] explicitly define this sine–exponential family (their Example 3, equation (21)) and illustrate numerical equilibrium-absence diagrams (Figure 10) while describing analytic parameter determination as difficult. The present result turns that numerical chart into an exact all-parameter threshold with root census, stability and fold asymptotics. An indexed result on a cosine-skewed piecewise interval map treats a different trigonometric branch (unsquared cosine) and a degenerate second branch; that statement does not imply the squared-sine plus exponential family analyzed here. Other generic one-dimensional saddle-node theorems motivate the local bifurcation but do not determine the critical curve and global count for this specific three-parameter map.

## Limitations
Uniqueness is established within this specified sine–exponential family, not among all comparable map models. The square-root asymptotic fixes \(b\); it is not claimed uniform at \(b=0\) or \(b=1\). This is an equilibrium and local-stability classification only; it does not characterize invariant measures, chaos, cryptographic security, or periodic cycles of period greater than one. Originality is based on inspected accessible sources and indexed comparisons; equivalent unindexed literature remains possible.

## References
[1] M. Lawnik, L. Moysis, C. Volos, *A Family of 1D Chaotic Maps without Equilibria*, Symmetry 15 (2023), article 1311, doi:10.3390/sym15071311, first publicly released 2023-06-27, https://www.mdpi.com/2073-8994/15/7/1311.
[2] MDPI, version notes for [1], https://www.mdpi.com/2073-8994/15/7/1311/notes.
