# Exact rotation-overlap rigidity and fractional angular contact for Lamé regions

## Finding

For every fixed real exponent \(0<p<2\), let
\[
K_p=\{(x,y)\in\mathbb R^2:|x|^p+|y|^p\le1\},
\qquad I_p(\theta)=\operatorname{area}(K_p\cap R_\theta K_p),
\]
where \(R_\theta\) denotes rotation about the origin. Define the folded angle
\[
d(\theta)=\min_{k\in\mathbb Z}|\theta-k\pi/2|\in[0,\pi/4],
\]
\(f_p(t)=(|\cos t|^p+|\sin t|^p)^{-2/p}\), and \(F_p(t)=\int_0^t f_p(s)\,ds\) for \(0\le t\le\pi/4\). Then the **exact area** of the rotational intersection is
\[
\boxed{I_p(\theta)=A_p-4\left[F_p(d/2)+F_p(\pi/4-d/2)-F_p(\pi/4)\right]},
\quad A_p=\frac{4\Gamma(1+1/p)^2}{\Gamma(1+2/p)},\quad d=d(\theta).
\]
For \(0<d<\pi/4\), \(I_p\) is strictly decreasing as a function of \(d\). Thus aligned copies uniquely maximize the overlap and quarter-turn-halfway copies uniquely minimize it, modulo the fourfold symmetries. In particular, the overlap area uniquely determines the *unlabelled* relative rotation \(d\).

For fixed \(0<p<2\), as \(d\downarrow0\), the **sharp two-term contact expansion** is
\[
\boxed{I_p(d)=A_p-2(1-2^{1-2/p})d+\frac{2^{2-p}}{p(p+1)}d^{p+1}+o(d^{p+1}).}
\]
The first nonlinear alignment correction has exponent \(p+1\), recording the boundary's Lamé exponent. At the unique minimum \(d=\pi/4\), writing \(\eta=\pi/4-d\),
\[
I_p(d)=I_p(\pi/4)+k_p\eta^2+O_p(\eta^4),
\qquad k_p=-f'_p(\pi/8)>0.
\]

For the classical astroid, \(p=2/3\), the entire overlap profile is **elementary**. Put
\[
G(u)=\frac38\left(\arctan u+\frac{u^3-u}{(1+u^2)^2}\right),\qquad u(t)=(\tan t)^{1/3}.
\]
Then \(F_{2/3}(t)=G(u(t))\) and
\[
\boxed{I_{2/3}(d)=\frac{3\pi}{4}-4[G(u(d/2))+G(u(\pi/4-d/2))].}
\]
Its minimum is \(3\pi/4-8G((\sqrt2-1)^{1/3})=0.84506423640705\ldots\) and its alignment law is
\[
I_{2/3}(d)=\frac{3\pi}{8}-\frac32d+\frac{36}{5\,2^{5/3}}d^{5/3}+o(d^{5/3}).
\]

## Assumptions and scope

All sets are centered, equally scaled, congruent Lamé regions in the Euclidean plane. The exponent \(p\) is held fixed when \(d\to0\) or \(\eta\to0\). No convexity is assumed: \(K_p\) is nonconvex for \(0<p<1\), convex for \(1\le p<2\), and star-shaped for every \(p>0\). Rotation is about the *shared center*, not a free translation. The parameter \(d\) identifies rotations only modulo reflection and quarter-turn symmetries.

## Proof

**1. Polar reduction and angular order.** The radial function \(\rho_p(t)\) of \(K_p\) satisfies \(\rho_p(t)^2=f_p(t)\). Hence
\[
I_p(\theta)=\frac12\int_0^{2\pi}\min\{f_p(t),f_p(t-\theta)\}\,dt.
\]
The function \(f_p\) is even, has period \(L=\pi/2\), is symmetric around \(L/2\), and is strictly decreasing on \((0,L/2)\) when \(p<2\). Indeed, on \((0,\pi/4)\), the derivative of \(\cos^p t+\sin^p t\) has the sign of \(\sin^{p-2}t-\cos^{p-2}t\), which is positive for \(p<2\). The negative exponent \(-2/p\) then makes \(f_p\) decreasing. Symmetries reduce any \(\theta\) to the folded angle \(d\in[0,L/2]\).

**2. Exact overlap.** Since \(\min(a,b)=(a+b-|a-b|)/2\), the area deficit is
\[
A_p-I_p(d)=\frac14\int_0^{2\pi}|f_p(t)-f_p(t-d)|\,dt
=\int_0^L|f_p(t)-f_p(t-d)|\,dt.
\]
For \(0\le d\le L/2\), the two translated functions cross at \(t=d/2\) and \(t=(L+d)/2\) modulo \(L\). Splitting the integral at these crossings, applying evenness and symmetry around \(L/2\), gives
\[
\int_0^L|f_p(t)-f_p(t-d)|\,dt
=4\left[\int_0^{d/2}f_p(t)\,dt-\int_{L/2-d/2}^{L/2}f_p(t)\,dt\right].
\]
This is exactly the displayed formula. The full-area identity \(A_p=4\Gamma(1+1/p)^2/\Gamma(1+2/p)\) follows either by the first-quadrant beta integral or by integrating \(y=(1-x^p)^{1/p}\) for \(x\in[0,1]\).

**3. Strict orientation rigidity.** Differentiating the exact deficit expression for \(0<d<L/2\) yields
\[
\frac{dI_p}{dd}=-2[f_p(d/2)-f_p(\pi/4-d/2)]<0,
\]
because \(d/2<\pi/4-d/2\) and \(f_p\) decreases strictly. Consequently \(d=0\) is the only maximum and \(d=\pi/4\) the only minimum in the fundamental domain, including their periodic copies. Near the minimum, the arguments of \(f_p\) lie away from coordinate axes and are real analytic. A second differentiation gives \(I_p''(\pi/4)=-2f'_p(\pi/8)>0\). Symmetry about \(\pi/4\) eliminates odd powers and yields the stated \(O_p(\eta^4)\) remainder.

**4. Sharp contact exponent.** As \(t\downarrow0\), for every fixed \(0<p<2\),
\[
f_p(t)=1-\frac2p t^p+O_p(t^{2p}+t^2),
\]
whereas, by symmetry and smoothness, \(f_p(\pi/4-t)=2^{1-2/p}+O_p(t^2)\). Insert these into the exact deficit formula and integrate over \([0,d/2]\). The linear term is \(2(1-2^{1-2/p})d\), and the leading correction to the deficit is \(-2^{2-p}d^{p+1}/[p(p+1)]\). The remaining terms are \(O_p(d^{2p+1}+d^3)=o(d^{p+1})\), since \(0<p<2\). This proves the stated expansion, including positivity of both displayed coefficients.

**5. Elementary astroid antiderivative.** For \(p=2/3\), let \(u=(\tan t)^{1/3}\). Then directly
\[
f_{2/3}(t)\,dt=\frac{3u^2}{(1+u^2)^3}\,du
=d\left[\frac38\left(\arctan u+\frac{u^3-u}{(1+u^2)^2}\right)\right].
\]
Since \(F_{2/3}(\pi/4)=3\pi/32\), substitution gives the elementary overlap formula. Setting \(d=\pi/4\) and using \(\tan(\pi/8)=\sqrt2-1\) gives the exact minimum. The general contact coefficient at \(p=2/3\) simplifies to \(36/(5\,2^{5/3})\).

## Verification

The included standalone script `CHECK.py` evaluates the overlap twice: once from the crossing-derived one-dimensional formula and independently from midpoint quadrature of the original two-dimensional radial minimum. It checks angular symmetries, strict monotonicity at a finite grid, several fixed-exponent local asymptotic ratios, the exact astroid antiderivative, and the minimum value. It completed **163 deterministic diagnostics** successfully. The proof is analytic; numerical sampling does not establish statements for all real exponents or angles.

## Relationship to prior work

Classical sources describe the astroid and Lamé superellipse boundaries, areas and parametrizations, including the arclength/cusp geometry of hypocycloids. Craizer, Teixeira and Balestro study a wider class of cycloids via normed-plane evolutes, not intersections of centered rotated Lamé regions. Rai and collaborators give the superellipse geometry and its orientation as a shape-fitting parameter, but do not derive the intersection profile or its sharp contact expansion. Studies of rotated regular-polygon overlap and general ellipse–ellipse overlap address different families; neither yields the continuum \(p\)-dependent fractional contact law by its stated results. The general radial-minimum identity is elementary and is not claimed as independently new. The asserted contribution is the exact all-exponent classification, strict inverse orientation law, and sharp exponent-dependent nonanalytic correction with the elementary astroid specialization. Historical priority remains provisional.

## Limitations

The proof concerns equal-scale concentric copies and \(0<p<2\), not arbitrary translations, unequal scales or the limiting circle \(p=2\), for which the rotational overlap is constant. The \(o(d^{p+1})\) remainder holds for each fixed exponent and is not asserted uniformly as \(p\to0\) or \(p\to2\). No independent mathematical audit has been performed.

## References

- M. Craizer, R. Teixeira and V. Balestro, *Closed Cycloids in a Normed Plane*, arXiv:1608.01651, first posted 2016-08-04. https://arxiv.org/abs/1608.01651
- R. K. Rai, M. Balmer, M. Rieser, V. S. Vaze, S. Schönfelder and K. W. Axhausen, *Capturing human activity spaces: New geometries*, manuscript dated 2006-11-15, https://svn.vsp.tu-berlin.de/repos/public-svn/publications/vspwp/2007/07-06/26feb07activity-spaces.pdf
- E. W. Weisstein, *Astroid* and *Superellipse*, MathWorld, https://mathworld.wolfram.com/Astroid.html and https://mathworld.wolfram.com/Superellipse.html
- G. B. Hughes and M. Chraibi, *Calculating ellipse overlap areas*, 2014, https://digitalcommons.calpoly.edu/stat_fac/17/
