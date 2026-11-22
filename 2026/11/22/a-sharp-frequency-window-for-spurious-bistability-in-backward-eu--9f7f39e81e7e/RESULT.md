# A sharp frequency window for spurious bistability in backward-Euler Hopf dynamics

## Finding

Consider the isochronous cubic Hopf equation on the complex plane,
\[
\dot z=(\lambda+i\omega)z-|z|^2z,
\qquad h>0,\quad \omega\ne0,\quad \lambda\in\mathbb R,
\]
and its fully implicit backward-Euler step
\[
z_{k+1}=z_k+h\bigl((\lambda+i\omega)z_{k+1}-|z_{k+1}|^2z_{k+1}\bigr).
\]
Put \(a=1-h\lambda\), \(b=h|\omega|\), and, when \(0<b<1\), \(c=\sqrt{1-b^2}\).

**Theorem.** The implicit step defines a globally smooth diffeomorphism \(T:\mathbb C\to\mathbb C\) if and only if \(a>-\sqrt3\,b\). Within this globally diffeomorphic regime, a hyperbolically attracting origin coexists with a normally attracting nonzero invariant circle separated from it by a normally repelling invariant circle if and only if
\[
\boxed{\frac12<b<1,\qquad -\sqrt3\,b<a<-\sqrt{1-b^2}.}
\]
Equivalently, for fixed \(h,\omega\) satisfying \(1/2<h|\omega|<1\), the exact bistability interval is
\[
\frac{1+\sqrt{1-h^2\omega^2}}{h}
 <\lambda<
\frac{1+\sqrt3\,h|\omega|}{h}.
\]
In that interval the two invariant circles have squared radii
\[
r_{\mathrm{in}}^2=\frac{-a-c}{h},\qquad
r_{\mathrm{out}}^2=\frac{-a+c}{h}.
\]
Every orbit with initial radius smaller than \(r_{\mathrm{in}}\) converges to the origin; every orbit of initial radius larger than \(r_{\mathrm{in}}\) approaches the outer circle in distance. The circle at \(r_{\mathrm{in}}\) is invariant and normally repelling, and these three sets contain all recurrent points. The angular motions on the outer and inner circles are, respectively, rigid rotations through \(\operatorname{sgn}(\omega)\arcsin b\) and \(\operatorname{sgn}(\omega)(\pi-\arcsin b)\) modulo \(2\pi\).

The critical frequency value \(h|\omega|=1/2\) is sharp: no such three-stratum coexistence is possible for any globally smooth backward-Euler step at or below that value; at or above \(h|\omega|=1\) there are not two distinct nonzero invariant circles.

## Assumptions and scope

The statement is for the exact implicit numerical update with no finite-precision solver errors, real \(\lambda\), nonzero real \(\omega\), positive \(h\), and the real cubic saturation coefficient normalized to one. The word *globally diffeomorphic* means a single-valued bijective smooth map with smooth inverse on all of \(\mathbb C\simeq\mathbb R^2\), not merely a locally chosen implicit branch. A circle is *normally attracting* or *normally repelling* according to its transverse radial multiplier, while angular motion has unit modulus.

## Proof

**1. Global regularity.** Write the implicit relation as \(z_k=\Psi(w)\), where \(w=z_{k+1}\) and
\[
\Psi(w)=(a+h|w|^2-ih\omega)w.
\]
For a radius \(s\ge0\), with \(u=hs^2\), the image radius is
\[
H(s)=s\sqrt{(a+hs^2)^2+b^2}.
\]
For \(s>0\), differentiation gives
\[
H'(s)=\frac{(a+u)(a+3u)+b^2}{\sqrt{(a+u)^2+b^2}}.
\]
The numerator is also the real planar Jacobian determinant of \(\Psi\), and it equals
\[
D(u)=3u^2+4au+a^2+b^2,\qquad u\ge0.
\]
When \(a\ge0\), this is strictly positive. When \(a<0\), its minimum over \(u\ge0\) occurs at \(u=-2a/3\) and equals \(b^2-a^2/3\). Consequently \(H'(s)>0\) for all radii exactly when \(a>-\sqrt3\,b\). In this case \(H(0)=0\), \(H(s)\to\infty\), and the angular part of \(\Psi\) is a radius-dependent rigid rotation, so \(\Psi\) and \(T=\Psi^{-1}\) are global smooth diffeomorphisms (smoothness at the origin follows from \(a-ih\omega\ne0\)). At equality the derivative is singular on a circle; below it \(H\) decreases on an interval and \(\Psi\) is not injective. This proves the exact smooth-invertibility criterion.

**2. Enumeration of invariant radii.** The radial part of \(T\) is \(H^{-1}\). A positive fixed radius \(s\) therefore satisfies
\[
(a+hs^2)^2+b^2=1.
\]
If \(b>1\) there is no positive solution. If \(b=1\), the only potential positive solution is \(hs^2=-a\), and its radial derivative is one, so it cannot provide an attracting circle separated by a repelling one. For \(0<b<1\), the candidate squared-radius parameters are \(hs^2=-a\pm c\). There are two distinct positive solutions exactly when \(a<-c\); these are the stated \(r_{\mathrm{in}}\) and \(r_{\mathrm{out}}\). This condition, together with smooth invertibility, describes a nonempty interval of \(a\) exactly when \(\sqrt3\,b>c\), or equivalently \(4b^2>1\). Thus \(1/2<b<1\) is necessary and sufficient for a smooth-implicit two-circle interval.

**3. Stability and exact basins.** In the two-circle interval, \(a<-c\) implies \(a^2+b^2>1\), so the origin has a linear multiplier pair of modulus \(1/\sqrt{a^2+b^2}<1\). At any positive fixed radius, \(H'(s)=1+2u(a+u)\), because the square-root factor there equals one. The inner circle has \(a+u=-c\), hence \(0<H'(r_{\mathrm{in}})=1-2c(-a-c)<1\), where strict positivity follows from the global diffeomorphism criterion. Its forward radial multiplier is the reciprocal and exceeds one. The outer circle has \(a+u=c\), hence \(H'(r_{\mathrm{out}})=1+2c(-a+c)>1\), with reciprocal radial multiplier strictly between zero and one.

On the open radial intervals divided by these two radii, \(H(s)/s-1\) has the signs \(+,-,+\), respectively. Since \(H\) is strictly increasing, the signs of \(H^{-1}(s)-s\) are \(-,+,-\). Thus the radial iterates are monotone and trapped by the adjacent fixed radii. They converge to zero below the inner circle and to the outer circle above it; points on the inner circle remain there. No radius other than the three listed fixed radii can be recurrent, since its radial iterates move strictly monotonically. On each positive fixed circle the complex multiplier \((a+hs^2-ih\omega)^{-1}\) has unit modulus and equals \(\pm c+i\operatorname{sgn}(\omega)b\), giving the stated rigid rotation angles.

**4. Example and continuous-time contrast.** For \(h=1\), \(\omega=3/5\), \(\lambda=19/10\), the parameters are \(b=3/5\), \(c=4/5\), \(a=-9/10\), which obey the strict bistability inequalities. The inner and outer squared radii are \(1/10\) and \(17/10\). Their backward-Euler radial multipliers are respectively \(25/21>1\) and \(25/93<1\), while the origin is attracting. In contrast, the continuous-time equation at \(\lambda=19/10>0\) has an unstable origin and only one attracting nonzero radial periodic circle, of radius \(\sqrt{19/10}\).

## Verification

Execute `python3 check.py` using Python 3 without additional libraries. It uses exact fractions to check the two rational-parameter instances, their two fixed radii, Jacobian determinants, radial multipliers and algebraic parameter-window identities. It also performs numerical bisection for the implicit successor radial map and tests convergence from all three basin intervals. The checker reports success for the supplied examples. The quantified proof above, not the finite experiment, establishes the universal theorem.

## Relationship to prior work

Oliveira, *Lyapunov–Schmidt reduction for periodic orbits of implicit discrete dynamical systems* (2026), develops local implicit periodic-orbit criteria at multipliers \(+1\) and \(-1\) and identifies two-dimensional Neimark–Sacker-type questions as further work; its example of backward Euler concerns a cusp of fixed points rather than the global radial dynamics treated here. Buescu and Oliveira, *Singular bifurcations in implicit discrete dynamical systems* (2026), analyze forward evolution folds and interactions with period doubling; their backward-Euler planar example has a different two-variable model and singularity mechanism. The conventional Stuart–Landau Hopf normal form and backward-Euler linear stability function are classical and are not claimed as new. The contribution is the sharp global smooth-inverse restriction, the frequency threshold for three-stratum bistability, exact two circles, and global basin decomposition **together** for this natural numerical step.

## Limitations

The result is confined to the isochronous single-oscillator cubic normal form and to the regime of a *globally* smooth single-valued implicit step. It does not classify multivalued or singular branches, numerical root-solver selection, nonisochronous cubic shear, coupled oscillators, or robustness under general perturbations. It is an explicit model theorem, not a resolution of general two-dimensional implicit-map bifurcation theory. Relevant numerical-discretization literature is extensive; a historical statement equivalent to this precise combined threshold and basin theorem may remain outside accessible indexing.

## References

1. H. M. Oliveira, *Lyapunov–Schmidt reduction for periodic orbits of implicit discrete dynamical systems*, arXiv:2611.03336v1, first public 2026-11-02, https://arxiv.org/abs/2611.03336.
2. J. Buescu and H. M. Oliveira, *Singular bifurcations in implicit discrete dynamical systems*, arXiv:2611.12327v1, first public 2026-11-09, https://arxiv.org/abs/2611.12327.
3. S. H. Strogatz, *Nonlinear Dynamics and Chaos*, 1994, Hopf normal-form discussion.
4. E. Hairer and G. Wanner, *Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems*, second edition, Springer, 1996, implicit numerical integration background.
