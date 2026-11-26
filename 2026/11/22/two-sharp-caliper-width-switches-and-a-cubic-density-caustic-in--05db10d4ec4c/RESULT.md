# Minimum-width transition and cubic caustic for parabolic segments

## Finding

Let \(a>0\) and \(K_a=\{(x,y): |x|\le a,\ x^2\le y\le a^2\}\), so the ratio of rise to half-chord is \(a\). The Euclidean minimum caliper width switches from the vertical normal to a pair of oblique normals at
\[
a_m=\sqrt{s_m}=1.92532470080679\ldots,\qquad 16s_m^3-56s_m^2-12s_m-1=0,
\]
where \(s_m\) is the unique positive root. For \(a<a_m\) the minimum is \(a^2\) and only the vertical normal minimizes (modulo antipodes). For \(a>a_m\) the minimum is \(w_a(t_+)\) with \(t_+=a+\sqrt{a^2-2}\); its normals have \(|u_x/u_y|=t_+\). At \(a=a_m\) these three unoriented normals coexist.

For a Haar-uniform unoriented unit normal, the width \(W_a\) has the law of \(w_a(\tan\theta)\) for \(\theta\) uniform on \([0,\pi/2]\), where
\[
w_a(t)=\begin{cases}
(a+t/2)^2/\sqrt{1+t^2},&0\le t\le2a,\\
2at/\sqrt{1+t^2},&2a\le t\le\infty.
\end{cases}
\]
At \(t=\infty\) use the limiting value \(2a\). In particular the CDF is \((2/\pi)\int_0^\infty\mathbf1_{\{w_a(t)\le v\}}\,dt/(1+t^2)\). For \(v\ge0\) the first branch is evaluated by the sign intervals of \((a+t/2)^4-v^2(1+t^2)\) on \([0,2a]\); the second branch is increasing with inverse \(v/\sqrt{4a^2-v^2}\) on its range below \(2a\). Each interval contributes \(2/\pi\) times its arctangent length. For \(v<0\) the CDF is zero.

At \(a=\sqrt2\) there is a cubic stationary point at \(\theta_* =\arctan\sqrt2\). Put \(w_*=3\sqrt3/2\) and \(c=3\sqrt6/4\). Then
\[
\Pr(|W_{\sqrt2}-w_*|\le\varepsilon)\sim (4/\pi)c^{-1/3}\varepsilon^{1/3},\qquad
f_{\sqrt2}(v)\sim (2/(3\pi))c^{-1/3}|v-w_*|^{-2/3}\quad(v\to w_*\text{ from either side}).
\]
The two critical widths born for \(a=\sqrt2+\delta>\sqrt2\), at \(t_\pm=a\pm\sqrt{a^2-2}\), satisfy
\[
w_a(t_-)-w_a(t_+)\sim \frac{4\,2^{3/4}}{3\sqrt3}\delta^{3/2}\quad(\delta\downarrow0).
\]

## Assumptions and scope

All widths are Euclidean distances between parallel supporting lines of the closed body including its chord. The angle is uniform modulo antipodes, with no additional reweighting. The asymptotics are for the limits stated. The global maximum switch is not part of the contribution: it is implied by the diameter result for the corresponding arc [1], as explained below.

## Proof

By reflection and antipodal symmetry use a normal \((u_x,u_y)\) with nonnegative coordinates and \(t=u_x/u_y\). The positive support is at \((a,a^2)\); the negative support is the maximum of \(-u_x x-u_y x^2\) for \(|x|\le a\). Its unconstrained vertex is admissible when \(t\le2a\); otherwise the maximizer is \(x=-a\). Substitution gives the stated width, including the horizontal normal by a limit. Folding Haar angular measure gives the density \(2/\pi\) of \(\theta\) measured from vertical. The CDF calculation follows by integrating on each monotone or polynomial sign interval.

In the first branch,
\[
w'_a(t)=\frac{(t+2a)(t^2-2at+2)}{4(1+t^2)^{3/2}}.
\]
The second branch increases strictly; at \(2a\) the first branch has positive derivative. Thus the only interior stationary direction for \(a\le\sqrt2\) occurs at equality and is not an extremum. For \(a>\sqrt2\) one has \(0<t_-<t_+<2a\), with a local maximum at \(t_-\) and local minimum at \(t_+\). The horizontal width exceeds \(w_a(t_+)\), as the width increases strictly after \(t_+\). Hence the minimizing candidates are just \(t=0\) and \(t=t_+\).

At a stationary root put \(x=t^2\), so \(a=(x+2)/(2\sqrt x)\) and \(w_a(t)=(1+x)^{3/2}/x\). The sign of \(w_a(t_+)^2/a^4-1\) is the sign of \(x(-x^3+8x^2+24x+16)\) at \(x=t_+^2\). That cubic has exactly one positive zero by Descartes's rule and the signs at zero and infinity, and is positive at \(x=2\). As \(t_+^2\) increases strictly from 2 to infinity, the unique minimum switch and all equality cases follow. To identify \(s=a^2\) at equality use \(x^2-Lx+4=0\), with \(L=4s-4\). The cubic reduces modulo this quadratic to \(Ax+B\), with \(A=-L^2+8L+28\) and \(B=4L-16\). The product of its values at the two quadratic roots is \(4A^2+LAB+B^2=-64(16s^3-56s^2-12s-1)\). The latter cubic also has exactly one positive zero by Descartes's rule and the signs at zero and infinity, identifying the switch.

At the birth \(a=\sqrt2\), the numerator of \(w'_a\) is \((t-\sqrt2)^2(t+2\sqrt2)\). Thus \(w'_a(t)=(\sqrt6/12)(t-\sqrt2)^2+O((t-\sqrt2)^3)\). Integrating and using \(dt/d\theta=3\) at \(\theta_*\) gives \(w_a(\tan\theta)-w_*=c(\theta-\theta_*)^3+O((\theta-\theta_*)^4)\). Width is strictly increasing in the folded angle at this parameter, so the angular band has length \(2(\varepsilon/c)^{1/3}(1+o(1))\). Inverting on either side and using the Taylor expansion of the angular derivative gives the asserted density.

For the unfolding let \(t=\sqrt2+\sqrt\delta\,u\), with \(a=\sqrt2+\delta\). The two roots converge in the \(u\)-coordinate to \(\pm B_0\) where \(B_0=2^{3/4}\). Uniformly for bounded \(u\), \(-w'_a(t)/\delta\to(12-3\sqrt2 u^2)/(12\sqrt3)\). Integration between the two roots yields the coefficient \(\int_{-B_0}^{B_0}(12-3\sqrt2 u^2)/(12\sqrt3)\,du=4B_0/(3\sqrt3)\).

## Comparison with earlier or related results

The arc \(\Gamma_a=\{(x,x^2):|x|\le a\}\) in [1] has convex hull \(K_a\). Taking the convex hull does not change diameter, and maximizing the caliper width over normals gives that diameter. The diametral pairs in [1] therefore specify the global maximum-width switch at \(\sqrt{(11+5\sqrt5)/8}\) and the maximizing directions (parallel to the diametral displacements), including coexistence. This is credited overlap, not a priority claim. The random variable in [1] is a distance between two sampled arc points, not the width in a single sampled direction. Its statements do not furnish the minimum-width transition or the cubic width-density singularity and splitting law.

Finch [2] studies angular widths for regular polygonal and polyhedral examples, and Abas [5] studies three-dimensional polytopes; these do not state the present curved planar width law. Classical segment geometry [3] and the Cauchy mean-width identity do not determine its distribution or minimum-width transition. Historical coverage is not exhaustive; the full text of [4] was not available for comparison.

## Reproducibility

`parabolic_segment_width_check.py` supplies supplementary algebraic checks and finite numerical diagnostics for the width profile, the extremal comparisons (including the credited diameter threshold), mean width, and the local asymptotics. Its historical execution is recorded in `CHECKS.txt`. The proof above, not the finite diagnostics, addresses the quantifiers over all shapes and directions.

## References

1. *Golden-ratio diameter bifurcation and sharp long-chord tails on a truncated parabola*, Resultary record `2e6c3c85982f`, 2026-11-22, [Finding](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-golden-ratio-diameter-bifurcation-and-sharp-long-chord-tails-on--2e6c3c85982f/RESULT.md).
2. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, [arXiv:1110.0671](https://arxiv.org/abs/1110.0671).
3. E. W. Weisstein, [Parabolic Segment](https://mathworld.wolfram.com/ParabolicSegment.html), Wolfram MathWorld.
4. M. H. Thibodeaux, *Arc Lengths and Curvature of Parabolic Segments*, Journal of the Pipeline Division 90 (1964), 1–6, [DOI](https://doi.org/10.1061/JPLEAZ.0000062).
5. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, [arXiv:2609.26202](https://arxiv.org/abs/2609.26202).
