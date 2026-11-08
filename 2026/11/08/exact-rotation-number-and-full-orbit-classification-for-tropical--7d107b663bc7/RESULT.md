# Exact rotation number and full orbit classification for tropical rank-two mutations

## Finding

For positive real parameters \(p,q\) with \(0<pq<4\), define the real tropical mutation
\[
M_{p,q}(s,t)=\bigl(-s+q[t+p[s]_+]_+,\ -t-p[s]_+\bigr),\qquad [x]_+=\max\{x,0\}.
\]
Put \(\kappa=\sqrt{pq}\) and \(\theta=\arccos(\kappa/2)\), so \(0<\theta<\pi/2\). Define the piecewise quadratic first integral
\[
\Phi_{p,q}(s,t)=\begin{cases}
p s^2-pqst+q t^2,&s<0<t,\\
p s^2+pqst+q t^2,&\text{otherwise}.
\end{cases}
\]
Then \(\Phi_{p,q}\) is strictly positive away from the origin, and every positive level \(C_c=\{\Phi_{p,q}=c\}\) is a star-shaped piecewise-elliptic Jordan curve. The restriction of \(M_{p,q}\) to every \(C_c\), \(c>0\), is topologically conjugate, through a normalized sector-area coordinate, to the *same* rigid clockwise rotation of the circle by
\[
\boxed{\rho(p,q)=\frac{2\theta}{\pi+2\theta}}\pmod1.
\]
The area of the enclosed level disk \(D_c=\{\Phi_{p,q}\le c\}\) is
\[
\boxed{\operatorname{Area}(D_c)=\frac{c(\pi+2\theta)}{2\kappa\sin\theta}}.
\]

This gives a complete classification of nonzero orbits. If \(\theta/\pi=a/b\) in lowest terms with \(0<a/b<1/2\), **every nonzero point has least period**
\[
\boxed{P(a,b)=\frac{b+2a}{\gcd(2,b)}}.
\]
If \(\theta/\pi\) is irrational, **every nonzero orbit is aperiodic and dense in its own level curve**, and its empirical measures converge to the unique invariant probability measure on that curve, namely normalized angular sector area. The origin is fixed for all parameters. In particular, \(M_{p,q}\) is globally periodic as a pointwise dynamical system exactly when \(\theta/\pi\) is rational.

The previously established integer-reciprocal-angle family \(\theta=\pi/m\), \(m\ge3\) [1, Theorem 3.12], is recovered, but the formula also treats all reduced rational multiples, including \(\theta=2\pi/7\) with least period \(11\), and all irrational angles.

## Assumptions and scope

The parameter domain is all ordered pairs of positive real numbers \((p,q)\) satisfying \(pq<4\). The map uses the max-plus convention \([x]_+=\max\{x,0\}\) and acts on the **entire real plane**, not the strictly positive quadrant of the original nontropical mutation. Its invariant curves are not claimed to be smooth at switching axes; each is a continuous Jordan curve assembled from elliptic arcs. The conjugacy refers to the angular dynamics of the tropical map only, not the nontropical rational mutation.

For \(c>0\), let \(r_c(\varphi)=\sqrt{c/\Phi_{p,q}(\cos\varphi,\sin\varphi)}\). The invariant probability measure \(\nu_c\) has angular density
\[
\frac{d\nu_c}{d\varphi}=\frac{1}{2A_{p,q}\Phi_{p,q}(\cos\varphi,\sin\varphi)},\qquad
A_{p,q}=\operatorname{Area}(D_1).
\]
Here \(\varphi\) is ordinary polar angle and angular integration is over any full turn. The formula is properly normalized because \(A_{p,q}=\frac12\int_0^{2\pi}\Phi_{p,q}(\cos\varphi,\sin\varphi)^{-1}\,d\varphi\).

## Proof

**1. The map is a positive homogeneous, area-preserving homeomorphism.** Write
\[
M_{p,q}=M_2\circ M_1,\quad
M_1(s,t)=(-s,t+p[s]_+),\qquad M_2(s,t)=(s+q[t]_+,-t).
\]
Each is a continuous piecewise-linear homeomorphism: given \((u,v)=M_1(s,t)\), recover \(s=-u\) and \(t=v-p[-u]_+\); given \((u,v)=M_2(s,t)\), recover \(t=-v\) and \(s=u-q[-v]_+\). On each linear branch its Jacobian determinant is \(-1\), hence the composition has determinant \(+1\) almost everywhere. It preserves planar Lebesgue area exactly, and \(M_{p,q}(\lambda z)=\lambda M_{p,q}(z)\) for every \(\lambda\ge0\).

**2. Exact invariant and geometry.** Let \(f(s,t)=ps^2+pqst+qt^2\) and \(g(s,t)=ps^2-pqst+qt^2\). The defining formulas yield these exhaustive cases, with boundary equalities following by continuity:

* If \(s\le0,t\le0\), then \(M(s,t)=(-s,-t)\), and \(f(-s,-t)=f(s,t)\).
* If \(s\le0,t>0\), then \(M(s,t)=(-s+qt,-t)\), and \(f(-s+qt,-t)=g(s,t)\).
* If \(s\ge0\), put \(v=t+ps\). For \(v\ge0\), \(M(s,t)=(-s+qv,-v)\) and \(f(-s+qv,-v)=f(s,t)\).
* If \(s\ge0,v<0\), then \(M(s,t)=(-s,-v)\), and \(g(-s,-v)=f(s,t)\).

Therefore \(\Phi\circ M=\Phi\), independently verifying the conserved quantity known from [1, Theorem 3.5]. The discriminant of either quadratic is \(pq(pq-4)<0\), and each leading coefficient is positive; hence both are positive definite. Along any ray, \(\Phi(ru)=r^2\Phi(u)\), where \(\Phi(u)>0\). Thus \(D_c\) is a bounded star-shaped topological disk and \(C_c\) is a Jordan oval. As \(M\) is a homeomorphism preserving \(\Phi\), it restricts to an orientation-preserving homeomorphism of each oval.

**3. Exact enclosed area.** Use coordinates \(S=\sqrt p\,s\), \(T=\sqrt q\,t\), with area Jacobian \(dS\,dT=\kappa\,ds\,dt\), where \(\kappa=2\cos\theta\). In normalized coordinates the relevant quadratic forms are \(S^2\pm\kappa ST+T^2\). There are three quadrants whose radial sector integral is
\[
I_+=\frac12\int_0^\infty\frac{dz}{1+\kappa z+z^2}
=\frac{\theta}{2\sin\theta},
\]
and one quadrant (\(S>0,T<0\)) whose integral is
\[
I_-=\frac12\int_0^\infty\frac{dz}{1-\kappa z+z^2}
=\frac{\pi-\theta}{2\sin\theta}.
\]
The arctangent antiderivative and \(0<\theta<\pi/2\) establish both evaluations without branch ambiguity. Dividing the normalized area by the Jacobian gives
\[
A_{p,q}=\frac{3I_++I_-}{\kappa}=\frac{\pi+2\theta}{2\kappa\sin\theta}.
\]
Homogeneity implies \(\operatorname{Area}(D_c)=c A_{p,q}\).

**4. The area coordinate conjugates the map to a rigid rotation.** Fix \(c>0\) and the point \(z_c=(\sqrt{c/p},0)\) of \(C_c\). Define \(h_c(z)\in\mathbb R/\mathbb Z\) as the planar area of the radial sector of \(D_c\) swept **clockwise** from the ray of \(z_c\) to the ray of \(z\), divided by \(cA_{p,q}\). Since the radial density \(r_c(\varphi)^2/2\) is strictly positive and continuous, \(h_c\) is an orientation-reversing (relative to counterclockwise orientation) homeomorphism of \(C_c\) onto the circle.

The positive-homogeneous area-preserving homeomorphism \(M\) maps each radial sector bijectively onto the radial sector between its endpoint images, preserving its planar area. Consequently the clockwise sector-area increment \(h_c(Mz)-h_c(z)\in\mathbb R/\mathbb Z\) is independent of \(z\). It suffices to compute it at \(z_c\).

By homogeneity, start at \(z_1=(1,0)\), with \(\Phi(z_1)=p\). One step gives \(M(1,0)=(pq-1,-p)\). In the entire swept lower-half-plane sector, \(\Phi=f\). Make the linear change of variables
\[
(U,V)=\bigl(\sqrt p\,s+\cos\theta\sqrt q\,t,\ \sin\theta\sqrt q\,t\bigr),
\]
whose Jacobian determinant is \(\kappa\sin\theta>0\), and for which \(f=U^2+V^2\). The two rays map to \((\sqrt p,0)\) and \((\sqrt p\cos(2\theta),-\sqrt p\sin(2\theta))\), so the clockwise sector is a Euclidean circular wedge of angle exactly \(2\theta\). This is the **minor** clockwise wedge because \(0<2\theta<\pi\). Its original planar area is \(p\theta/(\kappa\sin\theta)\), whereas the entire level disk has area \(p(\pi+2\theta)/(2\kappa\sin\theta)\). Their ratio is \(\rho=2\theta/(\pi+2\theta)\). Therefore
\[
\boxed{h_c(Mz)=h_c(z)+\rho\pmod1}
\]
for every \(z\in C_c\), with the same \(\rho\) for all \(c>0\).

**5. Periods and equidistribution.** If \(\theta/\pi=a/b\) is reduced, then \(\rho=2a/(b+2a)\). Its reduced denominator is
\[
\frac{b+2a}{\gcd(2a,b+2a)}=\frac{b+2a}{\gcd(2,b)},
\]
so rigid rotation forces every point of every oval to have exactly this least period. If \(\theta/\pi\) is irrational, then so is \(\rho\), because \(\theta/\pi=\rho/(2(1-\rho))\). Irrational rigid rotation is minimal and uniquely ergodic; transporting Haar probability through \(h_c^{-1}\) yields density \(\frac{1}{2A_{p,q}\Phi(\cos\varphi,\sin\varphi)}\), and the claimed convergence of orbit averages for every starting point. Finally \(M(0,0)=(0,0)\). These cases exhaust the entire plane.

## Verification

A standalone standard-library Python script, `verify_rotation.py`, reproduces exact rational branch identities and complete least-period checks for seven parameter pairs with \(pq\in\{1,2,3\}\), over a grid of rational starting points in all quadrants, including switching axes. It checks 22,756 individual exact or floating-point assertions and reports `TROPICAL_ROTATION_EXACT_AND_AREA_CHECK_OK 22756`. Separate midpoint radial quadrature agrees with the analytic enclosed area for five asymmetric parameter pairs; seven rational-angle tests verify the transformed endpoint rays and predicted return time. All universal mathematical statements are proved above; these finite checks are **not** substituted for an infinite proof.

## Relationship to prior work

Machacek and Ovenhouse introduced this tropical map and its piecewise quadratic conserved quantity, proved its symplecticity, and established the special integer reciprocal-angle periodicity law for \(pq=4\cos^2(\pi/m)\), integer \(m\ge3\) [1, Section 3.3, Theorems 3.5 and 3.12]. These are prior results, not part of the originality claim. The present result evaluates the invariant disks' exact sector areas, identifies the rotation angle *for all real elliptic parameters*, and derives complete periodic/aperiodic orbit classification, including higher-numerator rational angles and unique ergodicity. For example, \(\theta=2\pi/7\) yields period \(11\), outside the original \(\theta=\pi/m\) family. Generic rotation-number and area-coordinate methods are classical; the claimed contribution is the explicit law for this particular mutation system, not the general method.

The related work [2] on half-plane piecewise rotations concerns discontinuous isometries of a different form, not this positively homogeneous tropical mutation. The related [3] studies critical curves for piecewise-linear planar rotations with different branch matrices. Existing same-subject literature was inspected to distinguish a theorem for this explicit map from those broader analogies.

## Limitations

The result assumes strictly positive \(p,q\) and \(pq<4\). The parabolic and hyperbolic ranges \(pq\ge4\) have different noncompact level geometry and are outside scope; the nontropical mutation is not addressed. The curves need not be differentiable across the coordinate axes. Dense-orbit equidistribution is with respect to normalized sector area on **each** invariant oval, not planar Lebesgue ergodicity on the whole plane. A complete externally independent literature and mathematical review has not been carried out; potential unindexed equivalent calculations remain a priority risk.

## References

[1] John Machacek and Nicholas Ovenhouse, *Discrete Dynamical Systems From Real Valued Mutation*, arXiv:2109.06927, version first publicly posted 2021-09-14; later in *Experimental Mathematics* 33 (2024), 261–275. Primary full text: https://arxiv.org/pdf/2109.06927 .

[2] A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *On some rational piecewise linear rotations*, arXiv:2306.17543 (2023), https://arxiv.org/abs/2306.17543 .

[3] J. A. G. Roberts, A. Saito and F. Vivaldi, *Critical curves of rotations*, arXiv:2303.17955 (first posted 2023; published 2024 in *Indagationes Mathematicae*), https://arxiv.org/pdf/2303.17955 .
