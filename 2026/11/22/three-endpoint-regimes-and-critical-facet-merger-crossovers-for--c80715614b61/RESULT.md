# Three endpoint regimes and critical facet-merger crossovers for spherical orthogonal sectors

## Finding

Let \(K_{\alpha,\beta}\subset S^3\) be the orthogonal spherical join of two closed plane sectors of angular apertures \(0<\alpha,\beta\le\pi\), with normalized uniform three-dimensional spherical measure. For the intrinsic nearest-boundary distance \(D\), put \(A=\sin(\alpha/2)\), \(B=\sin(\beta/2)\), \(q=A^2B^2/(A^2+B^2)\), and \(\rho=\arcsin\sqrt q\). Then \(\rho\) is the inradius and, for \(0<t<\rho\),

\[
\Pr(D>t)=\frac4{\alpha\beta}\int_0^{\alpha/2}\!\int_0^{\beta/2}
\left[1-\sin^2t\left(\csc^2u+\csc^2v\right)\right]_+\,dv\,du.
\]

Write \(a=\alpha/2\), \(b=\beta/2\), \(H=2\cot\rho\), \(c_a=2q\cos a/\sin^3a\), \(c_b=2q\cos b/\sin^3b\). As \(h\downarrow0\) with apertures fixed, the three distinct sharp endpoint regimes are

\[
\Pr(D>\rho-h)\sim
\begin{cases}
\dfrac{2H^3}{3\alpha\beta c_ac_b}h^3,&\alpha,\beta<\pi,\\[5pt]
\dfrac{16H^{5/2}}{15\pi\beta c_b\sqrt q}h^{5/2},&\alpha=\pi,\;\beta<\pi,\\[5pt]
\dfrac4\pi h^2,&\alpha=\beta=\pi.
\end{cases}
\]

When \(\beta=\pi\), \(\alpha<\pi\), interchange the apertures in the middle formula. At \(\alpha=\beta=\pi\), an additional all-threshold identity holds:

\[
\Pr(D>t)=1-\frac{4t}{\pi}-\frac{2\sin(2t)}\pi+\frac{4\sin^2t}\pi,
\quad 0\le t\le\pi/4.
\]

These are genuine transitions as a pair of distinct boundary great hemispheres merges into one at a hemispheric aperture, rather than continuations of the cubic coefficient.

**Critical windows.** For fixed \(0<\beta<\pi\), let \(\alpha_h=\pi-\lambda\sqrt h\) with fixed \(\lambda\ge0\); let \(B=\sin(\beta/2)\), \(q_0=B^2/(1+B^2)\), \(\rho_0=\arcsin\sqrt{q_0}\), \(H_0=2\cot\rho_0\), and \(c_{b,0}=2q_0\cos(\beta/2)/B^3\). Then

\[
\lim_{h\downarrow0}h^{-5/2}\Pr\big(D_{\alpha_h,\beta}>\rho_{\alpha_h,\beta}-h\big)
=\frac{2}{\pi\beta c_{b,0}}
\int_0^{L_\lambda}[H_0-q_0(\lambda x+x^2)]^2\,dx,
\quad L_\lambda=\frac{\sqrt{\lambda^2+4H_0/q_0}-\lambda}{2}.
\]

If both \(\alpha_h=\pi-\lambda\sqrt h\) and \(\beta_h=\pi-\mu\sqrt h\), with fixed \(\lambda,\mu\ge0\), then

\[
\lim_{h\downarrow0}h^{-2}\Pr\big(D_{\alpha_h,\beta_h}>\rho_{\alpha_h,\beta_h}-h\big)
=\frac4{\pi^2}\int_{\xi,\eta\ge0}
\left[2-\frac{\xi^2+\lambda\xi+\eta^2+\mu\eta}{2}\right]_+\,d\xi\,d\eta.
\]

In the first window at \(\lambda=0\), and in the double window at \(\lambda=\mu=0\), the right sides agree with the respective fixed hemispheric coefficients.

**Marked boundary law.** If \(\alpha,\beta<\pi\) are fixed, write \(T\) for the squared norm in the first coordinate plane, \(U\) and \(V\) for the nearer angular side coordinates; put \(T_*=q/A^2\), \(L_a=\sin(2\rho)/A^2\), \(L_b=\sin(2\rho)/B^2\). Given \(D>\rho-h\), the rescaled triple \((x,y,w)=((a-U)/h,(b-V)/h,(T-T_*)/h)\) converges in total variation to the uniform distribution on

\[
\Omega=\big\{x,y\ge0:\ -L_a+c_ax\le w\le L_b-c_by\big\}.
\]

The four normalized slacks \(\big(c_ax,c_by,w+L_a-c_ax,L_b-c_by-w\big)/H\) have limiting \(\operatorname{Dirichlet}(1,1,1,1)\) law.

## Assumptions and scope

The unit sphere is \(S^3\subset\mathbb R^4\). Define \(K_{\alpha,\beta}\) using

\[
X=(\sqrt T\cos u,\sqrt T\sin u,\sqrt{1-T}\cos v,\sqrt{1-T}\sin v),
\quad 0\le T\le1,\ 0\le u\le\alpha,\ 0\le v\le\beta.
\]

Take \(X\) uniformly in this set according to spherical three-volume, and use intrinsic unit-radius great-circle distance to the **topological boundary of this same set**. The set is an intersection of four hemispheres when both angles are strictly below \(\pi\), of three at one hemispheric aperture, and of two at both. Lower-dimensional coordinate-plane edges have zero measure. All limits are taken with the stated parameters fixed, except the apertures explicitly depending on \(h\) in the two window statements. The probability at \(t=0\) is one and at \(t\ge\rho\) is zero.

## Proof

**Spherical volume and facet distances.** The angular join coordinates have spherical volume element \(\frac12\,dT\,du\,dv\). Consequently \(T\) is uniform on \([0,1]\), independently of uniform \(u\in[0,\alpha]\) and \(v\in[0,\beta]\). Let \(U=\min(u,\alpha-u)\) and \(V=\min(v,\beta-v)\), independent uniforms on \([0,a]\) and \([0,b]\). The bounding great hyperplanes of the first sector have oriented unit normals whose inner products with \(X\) are \(\sqrt T\sin u\) and \(\sqrt T\sin(\alpha-u)\), and similarly for the second sector. An intrinsic ball about \(X\) is contained in the intersection if and only if its radius is no greater than each geodesic margin, hence

\[
\sin D=\min\{\sqrt T\sin U,\sqrt{1-T}\sin V\}.
\]

For \(s=\sin t\), the event \(D>t\) is the interval condition \(s^2\csc^2U<T<1-s^2\csc^2V\). Integrating the uniform \(T\) first proves the exact two-angle formula. The largest feasible \(s^2\) is the maximum, over \(U,V\), of \((\csc^2U+\csc^2V)^{-1}\), namely \(q\) at \(U=a,V=b\); this yields \(\rho\). At this maximizer the two limiting \(T\) bounds meet at \(T_*=q/A^2\).

**Interior-aperture endpoint.** Let \(U=a-hx\), \(V=b-hy\), \(s^2=\sin^2(\rho-h)\). On compact \(x,y\)-sets,

\[
1-s^2(\csc^2U+\csc^2V)
=h(H-c_ax-c_by)+O(h^2(1+x^2+y^2)).
\]

Since \(c_a,c_b>0\) the positive integration support lies within \(x,y\) bounded uniformly in sufficiently small \(h\). Dominated convergence gives \(4h^3/(\alpha\beta)\int_{x,y\ge0}(H-c_ax-c_by)_+\,dx\,dy\). The integral is \(H^3/(6c_ac_b)\), proving the cubic coefficient. To retain \(T\), the lower and upper interval bounds expand respectively as \(T_*+h(-L_a+c_ax)+O(h^2)\) and \(T_*+h(L_b-c_by)+O(h^2)\). Since \(L_a+L_b=H\), rescaling yields uniform density on \(\Omega\) by convergence in measure of bounded moving domains. Affine mapping to the four slacks gives a constant density on the standard three-simplex, hence the stated Dirichlet law and total-variation convergence.

**One merged facet.** At \(\alpha=\pi\), expand the reciprocal sine around \(U=\pi/2\) at the scale \(U=\pi/2-\sqrt h\,x\), while \(V=b-hy\). Uniformly on the bounded positive support,

\[
1-\sin^2(\rho-h)(\csc^2U+\csc^2V)
=h(H-qx^2-c_by)+o(h).
\]

The Jacobian is \(h^{3/2}\), and its positive-part integrand contributes a further factor \(h\). Thus the coefficient is \(\frac4{\pi\beta}\int_{x,y\ge0}(H-qx^2-c_by)_+\,dx\,dy\). Evaluating first in \(y\) and then in \(x\) gives \(16H^{5/2}/(15\pi\beta c_b\sqrt q)\). Positivity confines the integration to a compact set, so dominated convergence is justified. Interchanging sectors handles the symmetric case.

**Two merged facets.** At \(\alpha=\beta=\pi\), take \(U=\pi/2-\sqrt h\,x\), \(V=\pi/2-\sqrt h\,y\), \(q=1/2\), \(H=2\). Then the interval length is \(h[2-(x^2+y^2)/2]_++o(h)\). Its quarter-disk integral is \(\pi\), giving \(\frac4{\pi}h^2\). For the exact expression at all thresholds, note that here the region is the intersection of the two hemispheres \(X_2\ge0\) and \(X_4\ge0\). Differentiate the survival volume with respect to \(t\): the two shifted-facet contributions reduce by the spherical cosine rule to

\[
-\frac{d}{dt}\Pr(D>t)=\frac4\pi\big(1+\cos 2t-\sin 2t\big),
\quad 0<t<\pi/4.
\]

For completeness, this derivative also follows by conditioning on the first positive coordinate: the conditional remaining three-dimensional direction's required orthant fraction is \(1-\tan t\); multiplying by the coordinate density \(4\cos t/\pi\), the Jacobian \(\cos t\), and both facets gives \((4/\pi)(1+\cos2t-\sin2t)\). Integration from \(\Pr(D>0)=1\) yields the stated closed formula.

**Critical merger windows.** When \(\alpha_h=\pi-\lambda\sqrt h\), the angle maximum is at \(a_h=\pi/2-\lambda\sqrt h/2\). Put \(U=a_h-\sqrt h\,x\); subtracting the reciprocal-sine value at \(a_h\) yields precisely \(h(\lambda x+x^2)+o(h)\). In the fixed-\(\beta\) case, set \(V=b-hy\), so the limiting positive interval length divided by \(h\) is \([H_0-q_0(\lambda x+x^2)-c_{b,0}y]_+\). Integrate \(y\) to obtain the one-window formula and \(L_\lambda\). If both apertures vary at rate \(\sqrt h\), use \(U=a_h-\sqrt h\xi\), \(V=b_h-\sqrt h\eta\). The two reciprocal-sine differences contribute respectively \(\frac12(\lambda\xi+\xi^2)h\) and \(\frac12(\mu\eta+\eta^2)h\), while the derivative of \(\sin^2(\rho_h-h)\) contributes \(2h\). This gives the double-window integral. All rescaled supports are uniformly bounded for fixed nonnegative window parameters, establishing the limits through dominated convergence. At zero window parameters the Gaussian-quadrant integrals coincide with the hemispheric coefficients.

## Verification

The companion `checker.py` uses high-order Gauss–Legendre quadrature on the exact two-angle integral and compares its tails against the three analytic endpoint coefficients and the two crossover integrals, including symmetry and a direct all-threshold check of the both-hemisphere formula. It is numerical corroboration, not a replacement for the preceding dominated-convergence proof. Run `python checker.py` with NumPy and SciPy installed.

## Relationship to prior work

Lassak (first available 6 December 2013, primary MSC 52A55) develops the supporting-hemisphere, spherical-lune, width and thickness framework. Lassak and Musielak (2018) study spherical bodies of constant width and discuss lunes and supporting hemispheres. Neither inspected text states a random three-dimensional **orthogonal join** nearest-boundary distance law, the endpoint merger exponents, or the two-parameter critical scaling integrals. Classical inner-parallel-body and tube formulas address related volume erosion, but without the evaluated, parameter-dependent singular regimes here. The present work does not claim the prior spherical width constructions as new.

## Limitations

The probability law concerns the specified orthogonal join in the unit three-sphere, with uniform spherical volume and intrinsic nearest-boundary distance. It does not establish comparable exponents for general spherical polytopes, nonorthogonal joins or arbitrary sampling densities. Historical priority is provisional; an unlocated specialized spherical inner-tube formula could imply a part of the statement. The crossover limits are pointwise in fixed window parameters and are not asserted uniform over unbounded windows. No external independent audit has been performed.

## References

1. M. Lassak, *Width of spherical convex bodies*, Aequationes Mathematicae 89 (2015), 555–567; online publication 6 December 2013. https://doi.org/10.1007/s00010-013-0237-3. Primary MSC 52A55.
2. M. Lassak and M. Musielak, *Spherical bodies of constant width*, Aequationes Mathematicae 92 (2018), 627–640. https://doi.org/10.1007/s00010-018-0558-3.
3. M. Koçak and A. V. Ratiu, *Inner tube formulas for polytopes*, arXiv:1008.2040 (2010). https://arxiv.org/abs/1008.2040. Euclidean rather than spherical polytopes.
