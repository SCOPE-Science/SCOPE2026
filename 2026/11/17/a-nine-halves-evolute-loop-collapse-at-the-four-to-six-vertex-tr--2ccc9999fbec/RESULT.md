# A nine-halves evolute-loop collapse at the four-to-six vertex transition of two-harmonic ovals

## Finding
Let \(p_{a,b}(\theta)=1+a\cos(2\theta)+b\cos(3\theta)\) be the support function of a strictly convex Euclidean plane oval, where \(b>0\), \(a\ge0\), and \(3a+8b<1\). Its curvature has six distinct stationary points for \(a<6b\), four for \(a>6b\), and four distinct stationary points, one degenerate of order three, for \(a=6b\).

Fix \(0<b<1/26\), put \(a=6b-\delta\), and let \(\delta>0\) decrease to zero. For all sufficiently small \(\delta\), a bounded *simple* evolute loop with a transverse closing double point and three ordinary cusps is traced by \(\theta\in[\pi-u_0,\pi+u_0]\), where \(u_0=\arccos(a/(6b))\). Its (unsigned, multiplicity-one) enclosed Euclidean area is
\[
\boxed{\mathcal A(6b-\delta,b)=\frac{128\sqrt3}{8505}\frac{\delta^{9/2}}{b^{5/2}}(1+o(1)).}
\]
The exponent \(9/2\) quantifies the collapse of a three-cusp evolute loop at the four-to-six curvature-vertex transition.

## Assumptions and scope
The boundary is parametrized by outward normal \(n(\theta)=(\cos\theta,\sin\theta)\), positively oriented tangent \(t(\theta)=(-\sin\theta,\cos\theta)\), and \(q=p n+p't\). Its radius of curvature is \(\rho=p+p''=1-3a\cos(2\theta)-8b\cos(3\theta)>0\). The evolute is the locus of centers of curvature \(E=q-\rho n=p't-p''n\), parametrized by the normal angle. An *ordinary cusp* means the local smooth parametrization has nonzero second derivative and linearly independent second and third derivatives. The result concerns the small loop near \(\theta=\pi\), not the full global self-intersection classification of the evolute. All asymptotics fix \(b\) and let \(\delta\) tend to zero through positive values.

## Proof
**Curvature-vertex count.** Direct differentiation gives
\[
\rho'(\theta)=6a\sin(2\theta)+24b\sin(3\theta)=12\sin\theta\,[a\cos\theta+2b(4\cos^2\theta-1)].
\]
The two roots of the quadratic in \(z=\cos\theta\) are
\[
z_\pm=\frac{-a\pm\sqrt{a^2+64b^2}}{16b}.
\]
The positive root always lies strictly between \(0\) and \(1\). The negative root lies strictly between \(-1\) and \(0\) exactly when \(a<6b\), and equals \(-1\) exactly when \(a=6b\). Including \(\theta=0,\pi\), the root counts are consequently six and four; at the transition, Taylor expansion at \(\pi\) yields \(\rho'(\pi+u)=60b u^3+O_b(u^5)\), establishing the triple zero. Since \(\rho>0\), stationary curvature and stationary radius are the same positions.

**The loop's exact closure and cusps.** Write \(u=\theta-\pi\). The evolute coordinates are exactly
\[
\begin{aligned}
E_x(\pi+u)&=-3a\cos u-a\cos(3u)+6b\cos(2u)+3b\cos(4u),\\
E_y(\pi+u)&=3a\sin u-a\sin(3u)-6b\sin(2u)+3b\sin(4u)\\
&=4(a-6b\cos u)\sin^3u.
\end{aligned}
\]
The first coordinate is even, the second odd. At \(u=\pm u_0\), where \(u_0=\arccos(a/(6b))\), both endpoints therefore coincide. For \(0<u<u_0\), the second coordinate is strictly negative, and for \(-u_0<u<0\) it is positive. The identity \(E'=-\rho'n\) implies on the positive half-loop
\[
\frac{d E_y}{d E_x}=\tan u
\]
whenever \(E_x'\ne0\). For small enough \(\delta\), there is exactly one critical value \(u_c\in(0,u_0)\) of \(E_x\), namely \(u_c=\arccos((a+\sqrt{a^2+64b^2})/(16b))\), and \(E_x\) decreases then increases. If two parameters on opposite sides of \(u_c\) have the same first coordinate, comparison of their derivatives \(\tan u\) along the two branches from the shared turning point gives strictly different second coordinates. Thus neither half-loop self-intersects; their interiors lie in opposite open half-planes. The point \(u=0\) is an ordinary cusp since \(\rho''(\pi)=-12\delta\ne0\) and \(E^{(3)}(\pi)\) has a transverse component; the same derivative criterion gives ordinary cusps at \(\pm u_c\). At \(\pm u_0\), the derivatives have opposite nonzero horizontal and equal nonzero vertical components, hence the identified endpoints form a transverse double point. The resulting boundary is a simple closed loop in the piecewise-regular Jordan sense.

**Blow-up and sharp area.** Set \(u=s\sqrt{\delta/b}\), subtract \(E(\pi)\), and define
\[
X_\delta(s)=\frac b{\delta^2}(E_x(\pi+u)-E_x(\pi)),\qquad
Y_\delta(s)=\frac{b^{3/2}}{\delta^{5/2}}E_y(\pi+u).
\]
Uniform Taylor expansion in \(s\), with first derivatives, on every compact interval gives
\[
(X_\delta,Y_\delta)\longrightarrow (X,Y)=(-6s^2+15s^4,\,-4s^3+12s^5).
\]
The rescaled endpoints satisfy \(u_0\sqrt{b/\delta}\to 1/\sqrt3\). The oriented area of the limiting loop is
\[
\int_{-1/\sqrt3}^{1/\sqrt3}X(s)Y'(s)\,ds=-\frac{128\sqrt3}{8505}.
\]
Indeed \(Y'=-12s^2+60s^4\), so the integral is elementary. Uniform first-derivative convergence on the moving compact parameter interval implies convergence of these oriented area integrals. The coordinate Jacobian of the inverse blow-up is \(\delta^{9/2}/b^{5/2}\); taking the absolute value yields the claimed coefficient. The additional cusps obey \(u_c\sim\sqrt{\delta/(5b)}\), giving a sharp square-root angular birth scale.

## Verification
The complete proof above is analytic for every allowed parameter, not extrapolated from numerical experiments. The accompanying `check.py` independently integrates the exact finite-parameter loop area at five positive deficits, compares the rescaled values with \(128\sqrt3/8505\), and exits only after an explicit numerical tolerance check. The symbolic polynomial integral can be reproduced from \(X\), \(Y\), and their derivatives as stated above. All checks use the package's own source files.

## Relationship to prior work
The classical four-vertex theorem guarantees at least four vertices for smooth simple closed ovals; it does not determine this two-harmonic six-to-four transition or the area collapse. DeTurck, Gluck, Pomerleano and Vick review that theorem and its converse. Musin studies curvature vertex counts through Chebyshev zero principles, which do not calculate this loop. Allemann, Hungerbühler and Wasem give a general evolute–equilibrium relationship and discuss support functions, but their studied invariant is the equilibrium count rather than the area of the small bounded evolute loop. Work on Wigner caustics and centre-symmetry sets is not interchangeable with the ordinary evolute defined here. No claim of a universal exponent for all degenerate evolutes is made.

## Limitations
The sharp constant is for the specific lowest even/odd mixed support-harmonic family, with \(b>0\) fixed and \(\delta\downarrow0\). It is not a classification of all evolutes, not a statement about Wigner caustics, and not an assertion that no earlier formulation exists. Historical priority is subject to further specialist assessment; independent verification has not been performed.

## References
- D. DeTurck, H. Gluck, D. Pomerleano, and D. S. Vick, *The Four Vertex Theorem and its Converse*, first public September 10, 2006, https://arxiv.org/abs/math/0609268.
- O. R. Musin, *Chebyshev systems and zeros of a function on a convex curve*, March 11, 2009, https://arxiv.org/abs/0903.1908.
- J. Allemann, N. Hungerbühler, and M. Wasem, *Equilibria of Plane Convex Bodies*, Journal of Nonlinear Science **31**, 86 (2021), https://doi.org/10.1007/s00332-021-09740-2.
