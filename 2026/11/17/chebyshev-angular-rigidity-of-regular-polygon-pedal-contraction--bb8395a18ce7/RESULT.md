# Chebyshev angular rigidity of regular-polygon pedal contraction

## Finding

Fix an integer \(n\ge3\), and let \(Q_n\) be the regular \(n\)-gon with vertices \(v_j=e^{2\pi i j/n}\) for \(j=0,\ldots,n-1\). Set \(c=\cos(\pi/n)\). For an interior point \(p=\rho e^{i\phi}\), let \(F_n(p)\) be the product of its distances from the \(n\) supporting side lines divided by the product of its distances from the \(n\) vertices. This is the modulus of the direct similarity relating a regular polygon to its \(n\)-fold pedal iterate whenever that iteration is nondegenerate, by the established pedal-iteration formula [1].

The complete interior profile is
\[
 F_n(\rho,\phi)=
 \frac{2^{1-n}\rho^n\bigl(T_n(c/\rho)+\cos(n\phi)\bigr)}
 {\sqrt{1+\rho^{2n}-2\rho^n\cos(n\phi)}}
 \quad (0<\rho<1,\ \rho e^{i\phi}\in\operatorname{int}Q_n),
\]
where \(T_n\) is the degree-\(n\) Chebyshev polynomial of the first kind. At the center, \(F_n(0)=c^n\).

**Sharp angular rigidity.** On each nonempty intersection of the open disk of radius \(\rho\) with \(\operatorname{int}Q_n\), \(F_n\) is strictly increasing in \(s=\cos(n\phi)\). Its maximizers on any fixed-radius polygonal cross-section, for \(0<\rho<1\), are exactly the \(n\) vertex directions \(\phi=2\pi k/n\). For \(0<\rho<c\), its minimizers are exactly the \(n\) side-normal directions \(\phi=(2k+1)\pi/n\), and the extrema are
\[
 F_n^{\max}(\rho)=\frac{2^{1-n}\rho^n\bigl(T_n(c/\rho)+1\bigr)}{1-\rho^n},\qquad
 F_n^{\min}(\rho)=\frac{2^{1-n}\rho^n\bigl(T_n(c/\rho)-1\bigr)}{1+\rho^n}.
\]
In particular the angular contrast is positive and exactly
\[
 F_n^{\max}(\rho)-F_n^{\min}(\rho)
 =\frac{2^{2-n}\rho^n\bigl(1+\rho^nT_n(c/\rho)\bigr)}{1-\rho^{2n}}
 \quad(0<\rho<c).
\]
For \(c\le\rho<1\), the continuous extension to the closed radial cross-section takes its minimum value zero precisely at boundary intersections with sides; the interior infimum is zero, but is not attained there.

**First anisotropic jet.** The function \(A_n(\rho)=2^{1-n}\rho^nT_n(c/\rho)\) is a polynomial in \(\rho^2\) with constant term \(c^n\). Uniformly in angle,
\[
 F_n(\rho,\phi)=A_n(\rho)
 +(c^n+2^{1-n})\rho^n\cos(n\phi)+O_n(\rho^{n+2})
 \qquad(\rho\downarrow0).
\]
Thus the full Taylor expansion is radial through degree \(n-1\), and the first nonradial homogeneous term has exactly degree \(n\) with strictly positive coefficient.

## Assumptions and scope

All Euclidean distances are ordinary unsigned distances. Side lines are the infinite lines supporting the edges, not line segments. The point \(p\) lies strictly in the regular polygon; consequently all numerator and denominator factors are positive. The formula defines a scalar on *all* interior points, including any for which a particular intermediate pedal polygon is degenerate. Identifying this scalar with an actually realized \(n\)-step similarity uses the nondegeneracy hypotheses of [1]; no claim is made that every interior parameter produces a nondegenerate intermediate polygon. At radial boundary intersections the scalar is defined by continuity. At \(\rho=1\) vertex denominators vanish, so the last boundary assertion deliberately restricts to \(\rho<1\).

## Proof

Write \(\alpha_j=(2j+1)\pi/n\) for the outward unit normal angle to the side \(v_jv_{j+1}\). Since \(p\in\operatorname{int}Q_n\), the side-line distance is
\[
 d_j=c-\rho\cos(\phi-\alpha_j)>0.
\]
The Chebyshev root-product identity, including its multiplicities, is
\[
 \prod_{j=0}^{n-1}\bigl(x-\cos(\phi-(2j+1)\pi/n)\bigr)
 =2^{1-n}\bigl(T_n(x)+\cos(n\phi)\bigr).
\]
Indeed \(T_n(\cos\theta)=\cos(n\theta)\); each listed root has \(\cos(n\theta)=-\cos(n\phi)\), and both sides have leading coefficient one. For generic \(\phi\) the roots are simple; by continuity the identity extends to all angles where roots merge. Substituting \(x=c/\rho\) gives the numerator
\[
 \prod_jd_j=2^{1-n}\rho^n\bigl(T_n(c/\rho)+\cos(n\phi)\bigr).
\]
Independently, the roots-of-unity factorization yields
\[
 \prod_j|p-v_j|=|p^n-1|=\sqrt{1+\rho^{2n}-2\rho^n\cos(n\phi)}.
\]
This proves the exact profile. At \(p=0\), the original distance products give \(c^n\).

Fix \(0<\rho<1\) and write \(q=\rho^n\), \(B=1+q^2\), \(a=T_n(c/\rho)\), and \(s=\cos(n\phi)\). The formula becomes
\[
 F_n=2^{1-n}q\,\frac{a+s}{\sqrt{B-2qs}}.
\]
At every interior parameter, \(a+s>0\) because the side-distance product is positive. Consequently
\[
 \frac{\partial F_n}{\partial s}
 =2^{1-n}q\left(\frac{1}{\sqrt{B-2qs}}
 +\frac{q(a+s)}{(B-2qs)^{3/2}}\right)>0.
\]
The allowed angular cross-section is a union of equal arcs symmetric about the vertex rays \(\phi=2\pi k/n\), on each of which \(s\) decreases from one to its allowed endpoint value. Thus precisely those vertex rays maximize the function. If \(\rho<c\), the complete circle is admissible and the unique minimal values of \(s=-1\) correspond to side-normal rays. Inserting \(s=\pm1\) gives the stated two sharp formulas and their difference. The difference is positive since \(q>0\), \(a+1>0\) on all interior side-normal rays, and the numerator \(1+qa\) is positive: \(q a=2^{n-1}\prod_jd_j\) at \(s=0\) whenever that angle is interior, or directly \(1+qa>0\) from \(a>-1\) at \(\rho<c\), \(0<q<1\).

If \(c\le\rho<1\), the circle meets the sides of \(Q_n\). Along a side, at least one side-distance factor is zero, while no vertex denominator vanishes for \(\rho<1\). This gives zero on the boundary, and strict positivity in the interior. For \(\rho=c\), the circle touches each side at its midpoint; the same conclusion holds. This proves the radial boundary assertions.

Finally \(T_n\) has powers of the same parity as \(n\), so \(A_n\) is a polynomial in \(\rho^2\) and \(A_n(0)=c^n\). Expanding the denominator uniformly for \(q=\rho^n\to0\) gives
\[
 F_n=(A_n+2^{1-n}q s)(1+q s+O_n(q^2))
 =A_n+(c^n+2^{1-n})q s+O_n(\rho^{n+2}),
\]
because \(A_n-c^n=O_n(\rho^2)\) and \(q^2=O(\rho^{n+2})\) for \(n\ge3\). The coefficient is positive and all lower-order terms are radial, proving the claimed first anisotropic degree.

## Verification

The accompanying `verify_pedal.py` checks the direct distance product against the Chebyshev formula for randomly chosen interior points at eighteen polygon orders, independently constructs and iterates the actual pedal projection map for a subset, and checks the fixed-radius endpoint formulas and angular monotonicity. It reports **2,865 finite checks passed**. Where the angular difference is smaller than binary64 resolution, the code uses the analytically stable positive-gap expression instead of requiring two rounded floats to differ. Finite testing is not used as proof of the exact or all-order statements.

## Relationship to prior work

Zwierzyński [1, Theorem 2.2 and Corollary 2.3] supplies the general pedal-iteration similarity product and the sharp global incenter contraction bound. Those results are inputs, not claimed as new here. The present statement evaluates the *entire off-center regular-polygon product* using the Chebyshev identity, classifies the exact strict angular ordering and all fixed-radius extremizers, and identifies the sharp first anisotropic term. The latter conclusions are not asserted in the inspected source. Standard roots-of-unity and Chebyshev factorization are likewise prior mathematics. Searches for corresponding cyclic-pedal, Chebyshev-profile and angle-ordering statements did not locate an equivalent full result; see `REVIEW.md` for originality comparisons and risks.

## Limitations

The finding is confined to regular Euclidean polygons and points in their interiors. It does not prove any nondegeneracy theorem for all pedal iterates, any global extremal property for arbitrary polygons, or a new general pedal-similarity theorem. The scalar at polygonal boundary points is only the continuous extension of the distance product. Historical priority of the combined Chebyshev angular classification is provisional against older geometry sources that might use different terminology. No independent mathematical audit has been performed.

## References

[1] Michał Zwierzyński, *When Pedal Shapes Come Back: a Complex Story*, arXiv:2611.01247v1 (first publicly posted 2026-10-31), https://arxiv.org/abs/2611.01247. Theorem 2.2 and Corollary 2.3; complete eight-page version inspected.
