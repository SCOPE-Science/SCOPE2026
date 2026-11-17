# Orthogonal period and Floquet controls for two parallel cycles on a cubic algebraic torus

## Finding

For a natural affine-angular subclass of the cubic vector fields with two invariant parallel planes classified by Jana, the periods and transverse Floquet multipliers of the two parallels have exact, independently controllable algebraic formulas.

For \(a>1\), put \(B(x,y)=px+qy\), \(f(x,y)=\omega+ux+vy\), and consider the autonomous polynomial system
\[
\begin{aligned}
\dot x&=\tfrac z2\bigl[xB(x,y)-a^2p\bigr]+f(x,y)y,\\
\dot y&=\tfrac z2\bigl[yB(x,y)-a^2q\bigr]-f(x,y)x,\\
\dot z&=B(x,y)(z^2-1).
\end{aligned}
\]
It leaves the smooth compact algebraic torus \(\mathcal T_a=\{(x,y,z):(x^2+y^2-a^2)^2+z^2=1\}\) invariant. Assume real \(p,q,u,v,\omega\), with \(p^2+q^2>0\). For \(s\in\{-1,1\}\), let \(\mathcal C_s=\{z=s,\ x^2+y^2=a^2\}\), \(A_s=(u+sq/2,v-sp/2)\), and \(\Delta_s^2=\omega^2-a^2\|A_s\|^2\).

**Theorem.** The circle \(\mathcal C_s\) forms a periodic orbit if and only if \(\Delta_s^2>0\). In that case its least period in the original time coordinate and its unique nontrivial Floquet multiplier **restricted to the invariant torus** are
\[
T_s=\frac{2\pi}{\Delta_s},\qquad
\mu_s=\exp\!\left[-\frac{2\pi s\,\operatorname{sgn}(\omega)\,a^2(pu+qv)}{\Delta_s(|\omega|+\Delta_s)}\right],\qquad\Delta_s=\sqrt{\Delta_s^2}>0.
\]
If both parallels are periodic, their stability factors always have opposite nonzero logarithmic signs whenever \(pu+qv\ne0\); the attracting one is \(s=\operatorname{sgn}(\omega(pu+qv))\), and the other is repelling within the torus. If \(pu+qv=0\), both multipliers are exactly one, without an assertion of nonlinear stability.

The physical-time period difference obeys
\[
\Delta_+^2-\Delta_-^2=-2a^2(uq-vp).
\]
Thus, when both are periodic, **the two least periods are equal precisely when \(uq-vp=0\)**. The dot product \(pu+qv\) controls transverse hyperbolicity, whereas the perpendicular determinant \(uq-vp\) controls period splitting. For any fixed nonzero \((p,q)\) these two controls are independent real linear coordinates on \((u,v)\).

## Assumptions and scope

The torus is the full compact smooth real surface \(\mathcal T_a\), not the solid torus or the ambient three-dimensional phase space. The definition of Floquet multiplier in the theorem is the nontrivial multiplier of the derivative of the return map on a one-dimensional section **inside this two-dimensional invariant surface**; the tangential multiplier is one. The ambient normal multiplier is not part of the claim. Only the two named invariant parallels are classified; additional periodic trajectories elsewhere on the torus are not ruled out. If \(\Delta_s^2\le0\), at least one point of \(\mathcal C_s\) is an equilibrium, so the entire circle cannot be a nonstationary periodic trajectory.

## Proof

**1. Invariant torus and its transverse coordinate.** Put \(U=x^2+y^2-a^2\) and \(H=U^2+z^2-1\). Direct substitution into the displayed polynomial system gives the identities
\[
\dot U=zB(x,y)U,\qquad
\dot H=2zB(x,y)H.
\]
Consequently \(H=0\) is invariant and the circles \(U=0,z=\pm1\) are invariant. Since \(a>1\), the torus has \(x^2+y^2\ge a^2-1>0\), so the polar angle \(\theta\) in the \((x,y)\)-plane is a smooth local angular coordinate everywhere on the torus. At \(\mathcal C_s\), the variable \(U\) is a valid local coordinate transverse to the orbit within the torus: there \(z=s\sqrt{1-U^2}=s+O(U^2)\). In particular, using \(z-s\) as the transverse linear coordinate would be incorrect.

**2. Angular motion and sharp periodicity test.** A direct cross-product calculation, valid for nonzero \(x^2+y^2\), gives
\[
\dot\theta=\frac{x\dot y-y\dot x}{x^2+y^2}
=-f(x,y)+\frac{za^2}{2(x^2+y^2)}(py-qx).
\]
On \(\mathcal C_s\), write \((x,y)=a(\cos\theta,\sin\theta)\) to obtain
\[
\dot\theta=-\omega-a[(u+sq/2)\cos\theta+(v-sp/2)\sin\theta]
=-\omega-aA_s\cdot(\cos\theta,\sin\theta).
\]
A continuous nonzero velocity around a circle has one entire traversal as its minimal periodic return, while any zero creates an equilibrium and prevents a full periodic orbit. The velocity has no zeros exactly when \(|\omega|>a\|A_s\|\), i.e. \(\Delta_s^2>0\). A rotation of the angular origin and the classical elementary integral \(\int_0^{2\pi}(c+d\cos\theta)^{-1}d\theta=2\pi/\sqrt{c^2-d^2}\) for \(c>|d|\) give \(T_s=2\pi/\Delta_s\) with no time reparametrization.

**3. Floquet multiplier.** The first identity in step 1 implies the normal variational equation on the torus,
\[
\frac{d}{dt}\delta U=s a[p\cos\theta(t)+q\sin\theta(t)]\delta U.
\]
Therefore the logarithm of the transverse multiplier is \(s a\int_0^{T_s}[p\cos\theta(t)+q\sin\theta(t)]dt\). Because the orbit makes one full monotone revolution, the integral can be written with the positive time density \(\bigl|\omega+aA_s\cdot(\cos\theta,\sin\theta)\bigr|^{-1}d\theta\). Its exact vector first harmonic is
\[
\int_0^{2\pi}\frac{(\cos\theta,\sin\theta)}{|\omega+aA_s\cdot(\cos\theta,\sin\theta)|}\,d\theta
=-\frac{2\pi a\operatorname{sgn}(\omega)}{\Delta_s(|\omega|+\Delta_s)}A_s.
\]
To verify this, rotate the angular origin to the direction of \(A_s\), integrate the cosine component using \((c+d\cos\theta)^{-1}\cos\theta=d^{-1}[1-c(c+d\cos\theta)^{-1}]\), and note that the sine component integrates to zero. The vector formula extends continuously to \(A_s=0\). As \((p,q)\cdot A_s=pu+qv\), exponentiation gives exactly the stated \(\mu_s\). Its exponent has the sign of \(-s\operatorname{sgn}(\omega)(pu+qv)\). A nonzero exponent proves hyperbolicity and the asserted torus-relative attraction or repulsion; a zero exponent proves only neutrality at linear order.

**4. Independent clocks and stabilities.** Directly expand the squared norm:
\[
\|A_s\|^2=u^2+v^2+(p^2+q^2)/4+s(uq-vp).
\]
Subtracting the two radicands gives the displayed squared-frequency difference. For two positive radicands, equal physical periods are equivalent to equal radicands, hence to \(uq-vp=0\). The linear map \((u,v)\mapsto(pu+qv,uq-vp)\) has nonzero determinant \(-(p^2+q^2)\), proving the controls are independent. Both periodicity inequalities can always be enforced by taking \(|\omega|\) large while keeping \(p,q,u,v,a\) fixed.

Explicit witnesses at \(a=2,p=1,q=0,\omega=5\): choosing \((u,v)=(1,0)\) gives \(\Delta_+=\Delta_-=\sqrt{20}\), equal periods, but opposite hyperbolic stabilities; choosing \((u,v)=(0,1)\) gives \(\Delta_+=\sqrt{24}\), \(\Delta_-=4\), unequal periods, but both multipliers equal one.

## Verification

The standalone reproducibility program `CHECK.py` verifies the polynomial torus cofactor and polar-angle identities with exact symbolic algebra, verifies both algebraic control identities, and checks the period and Floquet formulas against eight independent high-precision original-time quadratures (four parameter choices, both circles). It also tests the two contrasting witnesses. Successful reproducibility output is `EXACT_TANGENCY_ANGULAR_AND_SPLITTING_IDENTITIES_OK`, `EIGHT_ORIGINAL_TIME_AND_FLOQUET_QUADRATURES_OK`, and `ORTHOGONAL_CLOCK_AND_STABILITY_WITNESSES_OK`. The universal result rests on the proof above, not finite numerical tests.

## Relationship to prior work

Jana [1, Theorem 2.6 and its proof] already identifies the full cubic field with two invariant parallel planes and gives the necessary and sufficient zero-free angular-speed test for its parallel circles; the vector field and existence of invariant circles are **not new**. The present theorem specializes that established family to an affine angular coefficient and adds exact original-time periods, exact within-torus Floquet multipliers, and the independent dot/cross control law. Llibre and Rebollo-Perdomo [2] establish broader invariant-parallel and algebraic-limit-cycle configurations on algebraic tori, rather than these coupled quantitative formulas. Llibre and Medrado [3] is earlier work on the same torus, including qualitative limit-cycle conditions; its full text was not available for comparison, so an equivalent special formula there cannot be excluded.

## Limitations

The formulas do not classify other cycles, basin boundaries, the ambient three-dimensional transverse eigenvalue, or nonlinear stability when \(\mu_s=1\). A full text of [3] remains a priority for literature verification. Related results in unindexed publications or alternate notation may exist; no mathematical claim of absolute publication priority is made. The original source [1] is used for system selection and known existence context, not for the newly derived formulas.

## References

[1] S. Jana, *Characterization and dynamics of certain classes of polynomial vector fields on the torus*, arXiv:2401.07843 (first public version January 15, 2024), Theorem 2.6, equation (2.2), and proof in Section 5.

[2] J. Llibre and S. Rebollo-Perdomo, *Invariant parallels, invariant meridians and limit cycles of polynomial vector fields on some 2-dimensional algebraic tori in R3*, Journal of Dynamics and Differential Equations 25 (2013), 777–793, DOI:10.1007/s10884-013-9315-4; accessible author preprint https://ddd.uab.cat/pub/artpub/2013/gsduab_3215/InvParInvMeronTori.pdf.

[3] J. Llibre and J. C. Medrado, *Limit cycles, invariant meridians and parallels for polynomial vector fields on the torus*, Bulletin des Sciences Mathématiques 135 (2011), 1–9, DOI:10.1016/j.bulsci.2010.06.005.
