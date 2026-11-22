# Universal logarithmic mean-distance law for collapsing convex lenses

## Finding

**Theorem (width-profile law and sharp fixed-area envelope).** Let \(a,b:[-1,1]\to\mathbb R\) be Lipschitz functions, with \(a\) convex and \(b\) concave, such that \(a(-1)=b(-1)\), \(a(1)=b(1)\), and \(a(x)<b(x)\) whenever \(-1<x<1\). Set \(h=b-a\) and, for each \(\varepsilon>0\), define the full-dimensional convex lens
\[
K_\varepsilon=\{(x,y):-1\le x\le1,\ \varepsilon a(x)\le y\le\varepsilon b(x)\}.
\]
Let \(X_\varepsilon,Y_\varepsilon\) be independent points uniformly distributed in Euclidean arclength along the *entire boundary* of \(K_\varepsilon\), and write \(P_\varepsilon=\operatorname{per}(K_\varepsilon)\). Then, for fixed admissible \(a,b\),
\[
\boxed{\frac{\mathbb E|X_\varepsilon-Y_\varepsilon|}{P_\varepsilon}
=\frac16+\frac{\varepsilon^2\log(1/\varepsilon)}{32}\int_{-1}^1h(x)^2\,dx
+O_{a,b}(\varepsilon^2),\qquad\varepsilon\downarrow0.}
\]
In particular the leading logarithmic coefficient depends **only** on the vertical thickness \(h\), not on the vertical midline \((a+b)/2\), even when the latter is nonconstant.

Put \(A=\int_{-1}^{1}h(x)\,dx>0\) and \(\kappa(h)=\frac1{32}\int_{-1}^1h(x)^2\,dx\). For all admissible profiles,
\[
\boxed{\frac{A^2}{64}<\kappa(h)\le\frac{A^2}{48}.}
\]
The upper bound is attained precisely when \(h\) is a nonzero triangular tent: for some apex \(t\in(-1,1)\), \(h\) is affine on \([-1,t]\) and \([t,1]\), vanishes at the endpoints, and has height \(A\) at \(t\). The lower bound is not attained by any admissible \(h\), but is the exact infimum over all such profiles with integral \(A\), approached by widening flat plateaus and shortening their linear tip ramps. The sharp \(L^2\)-versus-\(L^1\) width envelope is a known concavity inequality; the new assertion is its appearance with the coefficient \(1/32\) in the boundary **two-point mean-distance** asymptotic.

## Assumptions and scope

Coordinates and lengths are Euclidean, the horizontal interval is exactly \([-1,1]\), and the parameter \(\varepsilon\) vertically scales both graphs. The assumptions imply that \(h\) is nonnegative, Lipschitz, concave, positive in the interior, and zero at both endpoints. They also imply that the boundary comprises exactly two Lipschitz graphs meeting at their tips, without positive-length vertical edge segments. Differentiability of \(a,b\) is required only almost everywhere, where it follows from Lipschitz regularity. Each \(a,b\) is fixed as \(\varepsilon\to0\); neither the remainder nor a rate for its implied constant is uniform over families of profiles with unbounded Lipschitz constants. The physical lens area is \(\varepsilon A\). The theorem does not apply to horizontally normalized ellipses, whose boundary graph slopes diverge at the tips.

## Proof

**1. Replace arclength sampling by a two-branch horizontal mixture.** The derivative of either graph \(u\in\{a,b\}\) exists almost everywhere and is bounded. Thus its horizontal arclength weight is
\[
w_{u,\varepsilon}(x)=\sqrt{1+\varepsilon^2u'(x)^2}=1+O_{a,b}(\varepsilon^2)
\]
uniformly almost everywhere. Consequently \(P_\varepsilon=\int(w_{a,\varepsilon}+w_{b,\varepsilon})\,dx=4+O_{a,b}(\varepsilon^2)\). The boundary sampling law differs in total variation by \(O_{a,b}(\varepsilon^2)\) from the law that independently chooses either graph with probability \(1/2\), then chooses horizontal position uniformly on \([-1,1]\). Since all relevant distances are uniformly bounded, the two-point expected distances differ by \(O_{a,b}(\varepsilon^2)\).

Write \(D_\varepsilon^{(0)}\) for the mean distance under this simplified law. Its exact integral is
\[
D_\varepsilon^{(0)}=\frac1{16}\sum_{u,v\in\{a,b\}}\int_{-1}^1\!\int_{-1}^1
\sqrt{(x-z)^2+\varepsilon^2(u(x)-v(z))^2}\,dz\,dx.
\]
At \(\varepsilon=0\), all four integrals equal \(\int\!\int|x-z|\,dz\,dx=8/3\), so \(D_0^{(0)}=2/3\).

**2. The only logarithmic contribution is between opposite graphs.** If \(u=v\), Lipschitz regularity gives \(|u(x)-u(z)|\le L|x-z|\). Therefore the corresponding integrand differs from \(|x-z|\) by at most \(C\varepsilon^2|x-z|\), and its total contribution to the excess is \(O_{a,b}(\varepsilon^2)\). If \(u\ne v\), replace the vertical difference \(u(x)-v(z)\) by \(\pm h(x)\). Indeed, boundedness and Lipschitz continuity give
\[
\left|(u(x)-v(z))^2-h(x)^2\right|\le C|x-z|.
\]
The identity
\[
|\sqrt{s^2+\varepsilon^2t^2}-\sqrt{s^2+\varepsilon^2q^2}|
=\frac{\varepsilon^2|t^2-q^2|}{\sqrt{s^2+\varepsilon^2t^2}+\sqrt{s^2+\varepsilon^2q^2}}
\]
then bounds the difference by \(C\varepsilon^2\) for \(s=|x-z|>0\). The diagonal has zero area and the same bound extends there by continuity. It follows that
\[
D_\varepsilon^{(0)}=\frac23+\frac18I_\varepsilon(h)+O_{a,b}(\varepsilon^2),
\]
where
\[
I_\varepsilon(h)=\int_{-1}^1\!\int_{-1}^1
\left[\sqrt{(x-z)^2+\varepsilon^2h(x)^2}-|x-z|\right]dz\,dx.
\]

**3. Exact one-dimensional kernel and its logarithmic coefficient.** For \(s\ge0,r>0\), integration gives
\[
F(s,r)=\int_0^s(\sqrt{t^2+r^2}-t)\,dt
=\frac12\left[\frac{sr^2}{\sqrt{s^2+r^2}+s}+r^2\operatorname{arsinh}(s/r)\right].
\]
Therefore
\[
I_\varepsilon(h)=\int_{-1}^1\left[F(1+x,\varepsilon h(x))+F(1-x,\varepsilon h(x))\right]dx.
\]
Since \(h\) is Lipschitz and vanishes at both tips, \(0<h(x)\le L\min(1+x,1-x)\) for interior \(x\). Thus \(r/s\le\varepsilon L\) for both arguments in the last display, making the expansion of \(\operatorname{arsinh}(s/r)\) uniform in \(x\) when \(\varepsilon L<1/2\). Directly from the expression for \(F\),
\[
F(s,r)=\frac{r^2}{2}\log\frac{2s}{r}+O(r^2)
\]
for \(0<r\le s/2\), with a universal implied constant. Hence
\[
I_\varepsilon(h)=\varepsilon^2\log(1/\varepsilon)\int_{-1}^1h^2dx
+\frac{\varepsilon^2}{2}\int_{-1}^1h(x)^2\log\frac{4(1-x^2)}{h(x)^2}\,dx
+O_h(\varepsilon^2).
\]
The second integral is finite: near each tip, \(h(x)\le L\operatorname{dist}(x,\{\pm1\})\), and \(h(x)^2|\log h(x)|\) is integrable; any logarithmic endpoint singularity is integrable after multiplication by \(h^2\). In particular,
\[
I_\varepsilon(h)=\varepsilon^2\log(1/\varepsilon)\int h^2+O_h(\varepsilon^2).
\]
Combine with step 2 to obtain \(D_\varepsilon^{(0)}=2/3+(\varepsilon^2/8)\log(1/\varepsilon)\int h^2+O(\varepsilon^2)\). Step 1 shows the true mean differs by at most \(O(\varepsilon^2)\). Divide by \(P_\varepsilon=4+O(\varepsilon^2)\) to get the stated coefficient \(1/32\) and the main asymptotic.

**4. Sharp shape envelope.** Cauchy–Schwarz on an interval of length two gives \(\int h^2\ge A^2/2\); equality would force \(h\) constant almost everywhere, impossible for a positive continuous profile vanishing at both tips. To see the upper inequality and equality cases self-containedly, define the area-one triangular tent \(T_t\), whose apex lies at \(t\in(-1,1)\), whose value at the apex equals one, and whose endpoint values vanish. Its area is exactly one and \(\int T_t^2=2/3\), independent of \(t\). Any nonnegative concave Lipschitz \(h\) with zero endpoint values is a positive mixture \(h=A\int T_t\,d\pi(t)\), where \(\pi\) is a probability measure on the possible apex positions. This follows from the nonnegative distributional curvature measure \(-h''\) and the Dirichlet Green function of the interval; equivalently, first verify it for polygonal concave graphs by their successive slope drops and then use uniform polygonal approximation. Jensen's inequality yields
\[
\int h^2\le A^2\int\!\int T_t(x)^2\,dx\,d\pi(t)=\frac{2A^2}{3}.
\]
Equality in the strictly convex square-function Jensen inequality requires \(T_t(x)\) to be almost surely independent of \(t\) for almost every \(x\). Distinct apex positions give different tents, so \(\pi\) must be a point mass and \(h\) itself a triangular tent. Conversely every such tent attains the upper bound. For the strict lower infimum fix \(A\) and take symmetric profiles with a horizontal top and two affine tip ramps each of width \(\delta\downarrow0\), rescaling their height to make \(\int h=A\); then \(\int h^2\to A^2/2\). Each is concave, Lipschitz and admissible (for instance take \(a=-h/2,b=h/2\)). Division by 32 completes the envelope. \(\square\)

## Verification

The included `verify.py` performs independent Euclidean-arclength quadrature over all four ordered graph pairs for a triangular-tent lens, a parabolic lens and a shifted parabolic lens with the *same* thickness but different midline. It checks the coefficient extracted from differences of the rescaled deficits at two small values of \(\varepsilon\), using the analytical profile integrals \(\int (1-|x|)^2dx=2/3\) and \(\int(1-x^2)^2dx=16/15\). It uses NumPy as recorded in `requirements.txt`. Finite quadrature is a diagnostic only, not a substitute for the proof or an exhaustive statement over all Lipschitz profiles.

## Relationship to prior work

Eric Shen, *A Sharp Perimeter Inequality for Mean Distances on Convex Curves* (arXiv:2611.21661v1, 7 November 2026), proves the global strict lower bound \(\mathbb E|X-Y|/P>1/6\) and sharpness through degenerating convex bodies. Its proof and references do not give a thickness-dependent logarithmic two-point expansion for general collapsing lenses. The present work determines that previously unquantified deficit for the specified family; it does not claim the global bound itself.

The published *Sharp shape bounds and conditional tomography for acute triangles on collapsing convex lenses* considers a different **three-boundary-point acute-angle probability**, with leading coefficient proportional to \(\int h^2\), and already contains the same classical tent-versus-flat shape envelope. That envelope is not itself claimed as novel here: the new step is the different *two-point expected distance/perimeter* observable, its exact \(1/32\) coefficient, and insensitivity to vertical midline shear. *Universal linear and angular logarithmic saturation for thin parallelograms* concerns the **difference between boundary and interior mean distances** for a fixed-angle parallelogram, whose vertical sides and profile differ from these zero-tip lenses; its formula is not an all-lens two-point boundary expansion. The separately studied thin-stadium mean distance is a special capsule family and does not imply the full arbitrary concave width-profile law.

## Limitations

This is a leading logarithmic expansion with an \(O_{a,b}(\varepsilon^2)\) remainder. It does not identify the complete second-order constant after the logarithmic term, establish uniformity as the profile varies, prove a corresponding theory for unbounded tip slopes, or compare arclength and area sampling of the lens interior. The area-normalized tent-versus-flat envelope is a classical concavity consequence and is included only to characterize the new observable's attainable logarithmic constants. Historical priority outside the inspected public literature is not certified, and no independent mathematical audit has been performed.

## References

1. E. Shen, *A Sharp Perimeter Inequality for Mean Distances on Convex Curves*, arXiv:2611.21661v1, first public 7 November 2026. https://arxiv.org/html/2611.21661v1
2. A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848 (abstract accessible, full text not examined). https://arxiv.org/abs/2608.14848
3. *Sharp shape bounds and conditional tomography for acute triangles on collapsing convex lenses*, publicly indexed mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-shape-bounds-and-conditional-tomography-for-acute-triangle--91e043b96fad
4. *Universal linear and angular logarithmic saturation for thin parallelograms*, publicly indexed mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-universal-linear-and-angular-logarithmic-saturation-for-thin-par--fb1616479c47
5. A. S. Tokmachev, *The Mean Distance Between Random Points on the Boundary of a Convex Figure*, Journal of Mathematical Sciences 286 (2024), 798–806; referenced in Shen (2026). Full text not examined.
