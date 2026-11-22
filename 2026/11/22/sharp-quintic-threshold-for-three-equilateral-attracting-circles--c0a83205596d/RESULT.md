# Sharp quintic threshold for three equilateral attracting circles

## Finding
Let \(C_1=(0,0)\), \(C_2=(1,0)\), \(C_3=(1/2,\sqrt3/2)\), and let \(\Gamma_k(r)=\{z\in\mathbb R^2:|z-C_k|=r\}\). There exists \(r_0>0\) such that, for every \(0<r<r_0\), the **least degree** of a real planar polynomial vector field for which all three prescribed circles are **hyperbolic attracting periodic orbits** is **five**. The circles are pairwise exterior. The assertion concerns these three prescribed orbits; it does not exclude additional periodic orbits elsewhere.

An explicit degree-five realization is
\[
X_r(z)=\sum_{k=1}^3 A_k(z)\,\prod_{i\ne k} f_i(z)\,J(z-C_k),\quad f_i(z)=|z-C_i|^2-r^2,\quad J(s,t)=(-t,s),
\]
where \(A_1(z)=A_2(z)=1+(x-y)/20\) and \(A_3(z)=1-(x-y)/10\), for \(z=(x,y)\). Each \(\Gamma_k(r)\) is a hyperbolic attractor for sufficiently small positive \(r\). Replacing \(X_r\) by \(-X_r\) gives three hyperbolic repelling circles, also at sharp degree five.

## Assumptions and scope
All polynomials have real coefficients; degree means the maximum total degree of the two vector-field components. A hyperbolic attracting circle has positive-time transverse multiplier strictly between zero and one. We require each **given** circle to be a periodic orbit, with no equilibrium on the circle. The centers form the unit equilateral triangle, and the three radii are equal. We assert existence of \(r_0\), not a computed optimal cutoff; one may also require \(r_0<1/2\) to guarantee disjoint disks.

## Proof
**1. Invariance, degree and angular speed.** Each summand in \(X_r\) is tangent to its indexed circle, while every other summand vanishes there because of its factor \(f_k\). Thus all circles are invariant. On \(\Gamma_k(r)\), the angular equation in the standard counterclockwise parameter is
\[
\dot\theta=A_k(C_k+r(\cos\theta,\sin\theta))\prod_{i\ne k} f_i(C_k+r(\cos\theta,\sin\theta)).
\]
The other factors are positive for \(r<1/2\). The center values \(a_k=A_k(C_k)\) are
\[
(a_1,a_2,a_3)=\left(1,\frac{21}{20},\frac{19+\sqrt3}{20}\right),
\]
so the angular velocities are strictly positive for all sufficiently small \(r\). The degree-six homogeneous terms cancel because \(\sum_k\nabla A_k=0\). The \(x^5\) coefficient of the first component after putting \(y=0\) is \(-\sqrt3/20\ne0\), so the degree is **exactly five**.

**2. An exact cofactor formula.** For any affine coefficients \(A_i\), let \(T_i=f_jf_\ell J(z-C_i)\), with \(\{i,j,\ell\}=\{1,2,3\}\). On \(\Gamma_k\), write \(z=C_k+r e(\theta)\), \(e(\theta)=(\cos\theta,\sin\theta)\). The cofactor of \(f_k\), restricted to the circle, equals
\[
K_k=2\sum_{i\ne k}A_i f_j D_{ki},\quad D_{ki}=\det(z-C_i,z-C_k),\quad \{i,j,k\}=\{1,2,3\}.
\]
Since \(2D_{ki}=-\partial_\theta f_i\), the unnormalized logarithm \(\chi_k\) of the positive-time transverse Floquet multiplier, whenever \(A_k>0\), satisfies the **exact** identity
\[
\chi_k=-\sum_{i\ne k}\int_0^{2\pi}\frac{A_i(z)}{A_k(z)}\,\frac{\partial_\theta f_i(z)}{f_i(z)}\,d\theta.
\]
For a clockwise orbit the right-hand side is multiplied by \(\operatorname{sgn}(A_k)\). This is the standard cofactor/Poincaré formula (with physical-time orientation).

**3. Attractive quintic circles.** Set \(g_i=\nabla A_i\), \(d_{ki}=C_k-C_i\), \(a_{ik}=A_i(C_k)\), and \(a_k=A_k(C_k)>0\). Using \(f_i(C_k+re)=|d_{ki}|^2+2r d_{ki}\cdot e\), Taylor expansion of the exact integral gives
\[
\chi_k(r)=-\frac{2\pi r^2}{a_k^2}S_k+O(r^3),\quad
S_k=\sum_{i\ne k}\frac{\det(a_k g_i-a_{ik}g_k,d_{ki})}{|d_{ki}|^2}.
\]
The constant-in-\(\theta\) term integrates to zero exactly, because each \(\partial_\theta\log f_i\) integrates to zero; the leading nonzero contribution uses \(\int_0^{2\pi}(u\cdot e)(d\cdot Je)\,d\theta=\pi\det(u,d)\). Direct exact evaluation yields
\[
S_1=\frac{3(1+\sqrt3)}{40},\qquad
S_2=\frac{3(\sqrt3-1)}{40},\qquad
S_3=\frac{3\sqrt3}{20}.
\]
All three are strictly positive. Uniformity of the analytic expansions over the three compact circles provides an \(r_0>0\) with \(\chi_k(r)<0\) for every \(k\) and every \(0<r<r_0\). The three circles are therefore isolated hyperbolic attracting limit cycles.

**4. The quartic obstruction.** By Cao--Llibre's full normal-form theorem for three non-collinear prescribed invariant circles [1, Theorem D and Proposition 6.1], every degree-at-most-four field preserving the equilateral circles is
\[
Y=\sum_{i=1}^3 B_i f_jf_\ell J(z-C_i),\quad
B_1=-\lambda-\mu+\kappa(-vx-y/2-v),\quad
B_2=\lambda+\kappa(vx-y/2),\quad
B_3=\mu+\kappa y,
\]
where \(v=\sqrt3/2\). Its center angular coefficients are
\[
(b_1,b_2,b_3)=(-\lambda-\mu-\kappa v,\lambda+\kappa v,\mu+\kappa v).
\]
For all three circles to be periodic, \(|b_i|>|\kappa|r\), so their angular speeds have signs \(\operatorname{sgn}(b_i)\). If \(\kappa=0\), [1, Proposition 6.3] shows that no prescribed circle is isolated.

For \(\kappa\ne0\), the three positive-time characteristic exponents, whenever nonzero, obey the exact cyclic sign identities
\[
\begin{aligned}
\operatorname{sgn}\chi_1&=\operatorname{sgn}[\kappa b_1(b_3-b_2)],\\
\operatorname{sgn}\chi_2&=\operatorname{sgn}[\kappa b_2(b_1-b_3)],\\
\operatorname{sgn}\chi_3&=\operatorname{sgn}[\kappa b_3(b_2-b_1)].
\end{aligned}
\]
Here is a direct derivation rather than an appeal to numerical testing. For \(\Gamma_1\), let \(t=\theta-\pi/6\), \(w=\cos t\), and \(Q(w)=1-r^2-4rvw+4r^2w^2=f_2f_3>0\). Holding \(b_1\) and \(\kappa\) fixed, set \(d=b_3-b_2=\mu-\lambda\). The reflected system with \(d=0\) has zero exponent integral, and variation in \(d\) gives exactly
\[
I_1=d r\int_0^{2\pi}\frac{w-2rv}{(b_1-\kappa r w)Q(w)}\,dt,
\qquad \chi_1=\operatorname{sgn}(b_1) I_1.
\]
Moreover \(\int_0^{2\pi}(w-2rv)/Q(w)\,dt=0\), as it is proportional to the full derivative of \(\log(f_2/f_3)\). Subtracting the constant \(1/(b_1-2\kappa r^2 v)\) from the first reciprocal transforms the integrand into one whose sign is everywhere the sign of \(\kappa\), apart from zeros: \(1/(b_1-\kappa r w)\) is strictly monotone with derivative of sign \(\kappa\). Thus \(\operatorname{sgn}I_1=\operatorname{sgn}[\kappa(b_3-b_2)]\). Rotation of the equilateral configuration gives the other two identities.

If the three \(b_i\)'s are not pairwise distinct, at least one \(\chi_i\) vanishes. If they are distinct, their cyclic difference signs are incompatible with the three products above all being strictly negative (or all strictly positive): for example, if \(b_1<b_2<b_3\), negative products for \(\kappa>0\) would require \(b_1<0\), \(b_2>0\), \(b_3<0\), contrary to the ordering; the other five orderings are cyclic or reversed versions of the same contradiction. Hence three hyperbolic attracting prescribed circles are impossible in degree four or below. Combined with steps 1--3, the minimum degree is five. Negation of the quintic field reverses the Floquet exponents without changing polynomial degree.

## Verification
The standalone `checks/check.py` (Python with SymPy) verifies the exact degree-five coefficient, invariance of all circles, positivity of the three symbolic \(S_k\), and the complete cancellation of degree-five/six homogeneous terms in the published quartic normal form. These are algebraic consistency checks. The sign obstruction and uniform small-radius statement follow from the analytic argument above, not from finite numerical enumeration.

## Relationship to prior work
Cao and Llibre [1] classify all degree-at-most-four fields preserving these prescribed disjoint circles, and give a general hyperbolicity criterion; their classification is an essential **premise**, not a newly claimed theorem. The new combination is an equilateral **same-attractor sign obstruction** plus a **degree-five realization**, establishing the sharp degree threshold. Margalef-Bentabol and Peralta-Salas [2] realize arbitrary configurations and prescribed stabilities with polynomial fields but do not obtain this sharp degree-five conclusion for prescribed equilateral circles. Christopher [3] supplies a general degree-six algebraic-curve construction; the degree-five example here lowers that bound for this symmetrical configuration and stability pattern.

## Limitations
The theorem treats equal small radii on a fixed equilateral center triangle, not arbitrary triple geometry. It concerns hyperbolic attraction, not nonhyperbolic attracting cycles. It does not determine every possible additional orbit of the quintic field, an optimal value of \(r_0\), or the minimum degree for other configurations. Priority comparisons may be incomplete for older specialized work not accessible in full text. Independent mathematical audit has not been performed.

## References
[1] Chen Cao and Jaume Llibre, *Quartic polynomial differential systems with three disjoint invariant circles*, arXiv:2611.05696v1, first public 2026-11-03. https://arxiv.org/abs/2611.05696

[2] Juan Margalef-Bentabol and Daniel Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields*, arXiv:1507.00698v1, first public 2015-07-02. https://arxiv.org/html/1507.00698v2

[3] C. J. Christopher, *Polynomial vector fields with prescribed algebraic limit cycles*, Geometriae Dedicata 88 (2001), cited and compared in [1, Introduction].
