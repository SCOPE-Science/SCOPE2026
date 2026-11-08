# Exact John–Löwner contact geometry of the octahedral critical Orlicz body

## Finding

Let \(K=\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le1\}\). Apply the facet boundary-integral definition of the logarithmic-cosh critical functional
\[
\Phi_K(y)=\int_{\partial K}\langle x,n(x)\rangle\log\cosh\!\left(\frac{\langle y,n(x)\rangle}{2\langle x,n(x)\rangle}\right)\,d\mathcal H^2(x),
\qquad T=\{y:\Phi_K(y)\le1\}.
\]
The unique maximum-volume inscribed (John) ellipsoid of \(T\) is \(r_{\rm in}B_2^3\), where
\[
 r_{\rm in}=2\operatorname{arcosh}(e^{1/4})=1.47380918124193748\ldots .
\]
It contacts \(\partial T\) **exactly** at \(\pm r_{\rm in}e_1,\pm r_{\rm in}e_2,\pm r_{\rm in}e_3\).

The unique minimum-volume containing (Löwner) ellipsoid is \(r_{\rm out}B_2^3\), where \(r_{\rm out}\in(0,2)\) is the unique solution of
\[
 \log\cosh\!\left(\frac{\sqrt3 r_{\rm out}}2\right)
 +3\log\cosh\!\left(\frac{r_{\rm out}}{2\sqrt3}\right)=1,
 \qquad r_{\rm out}=1.54462949376420262\ldots .
\]
It contacts \(\partial T\) **exactly** at the eight points \(r_{\rm out}(\pm1,\pm1,\pm1)/\sqrt3\).

A stronger directional assertion holds: for every \(0\le r\le2\), every unit \(u\in\mathbb R^3\),
\[
 \log\cosh\!\left(\frac{\sqrt3r}2\right)
 +3\log\cosh\!\left(\frac r{2\sqrt3}\right)
 \le\Phi_K(ru)\le4\log\cosh(r/2).
\]
For \(0<r\le2\), the lower equality occurs precisely for the eight body diagonals and the upper equality precisely for the six coordinate axes. This last assertion is not extended to \(r>2\).

## Assumptions and scope

The body \(K\) is the three-dimensional unit cross-polytope (a regular Euclidean octahedron) and the Euclidean volume and Euclidean surface measure are unscaled. All ellipsoids and balls are in standard Euclidean coordinates. The scalar level is exactly one, with the normalization in the displayed definition of \(\Phi_K\). The facets have unique normals almost everywhere, so their boundary integral is unambiguous. This is a theorem about the **facet-defined Orlicz functional** for a polytope, not a claim that the source's smooth-boundary covariogram limit theorem already applies to this nonsmooth \(K\).

## Proof

**1. Exact facet sum.** There are eight triangular facets, one for each sign vector \(\varepsilon\in\{\pm1\}^3\). Each facet has unit normal \(\varepsilon/\sqrt3\), support distance \(1/\sqrt3\), and Euclidean area \(\sqrt3/2\). Thus its integrated weight is exactly \(1/2\), giving
\[
 \Phi_K(y)=\frac12\sum_{\varepsilon\in\{\pm1\}^3}
    \log\cosh\!\left(\frac{\varepsilon\cdot y}{2}\right)
 =\sum_{\varepsilon\in\mathcal E}\log\cosh\!\left(\frac{\varepsilon\cdot y}{2}\right),
\quad\mathcal E=\{(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)\}.
\]
The function is even, strictly convex and coercive, because the four linear forms span \(\mathbb R^3\), \((\log\cosh)''>0\), and the log-cosh function grows linearly at infinity. The level set \(T\) is therefore a compact strictly convex body with the signed-permutation symmetries.

**2. A degree-four Euler-factor inequality.** For unit \(u\), set \(t_i=u_i^2\), \(e_2=t_1t_2+t_2t_3+t_3t_1\), and \(e_3=t_1t_2t_3\); then \(t_i\ge0\) and \(\sum t_i=1\). For \(\lambda>0\) define
\[
 P_\lambda(t)=\prod_{\varepsilon\in\mathcal E}
       \bigl(1+\lambda(\varepsilon\cdot u)^2\bigr).
\]
Direct expansion, with no assumptions on the signs of \(u_i\), yields
\[
 P_\lambda(t)=1+4\lambda+(6-8e_2)\lambda^2
     +4(1-4e_2+16e_3)\lambda^3+(1-4e_2)^2\lambda^4.\tag{1}
\]
The elementary inequalities needed below are
\[
 0\le e_2\le\tfrac13,\qquad 9e_3\le e_2,\qquad
 1-4e_2+9e_3\ge0.\tag{2}
\]
The first follows from \(\sum t_i=1\), and the second from \(\sum1/t_i\ge9\) when all coordinates are positive (the boundary is immediate). For the third, observe the identity
\[
 1-4e_2+9e_3=e_3-\prod_{i=1}^3(1-2t_i).
\]
If some \(t_i>1/2\), that product is nonpositive. Otherwise let \(a_i=1/2-t_i\ge0\). Then, for distinct \(i,j,k\), \(t_i=a_j+a_k\), and AM–GM gives
\[
 e_3=\prod_{i<j}(a_i+a_j)\ge8a_1a_2a_3
     =\prod_i(1-2t_i),
\]
proving (2) also on all boundaries.

Let \(t^{\rm ax}=(1,0,0)\), \(t^{\rm dg}=(1/3,1/3,1/3)\). From (1),
\[
 P_\lambda(t^{\rm ax})-P_\lambda(t)
 =8\lambda^2\bigl[e_2(1+2\lambda+(1-2e_2)\lambda^2)-8e_3\lambda\bigr]
 \ge8e_2\lambda^2\left(1+\tfrac{10}9\lambda+\tfrac13\lambda^2\right).
\tag{3}
\]
This is strictly positive except when \(e_2=0\), meaning an axis. For the opposite inequality put \(d=1/3-e_2\ge0\) and \(z=1/27-e_3\). Inequality (2) implies \(z\le4d/9\). Expanding (1) gives
\[
 \begin{aligned}
 P_\lambda(t)-P_\lambda(t^{\rm dg})
 &=8d\lambda^2+16d\lambda^3-64z\lambda^3
     -\tfrac83d\lambda^4+16d^2\lambda^4\\
 &\ge8d\lambda^2\left(1-\tfrac{14}9\lambda
              -\tfrac13\lambda^2+2d\lambda^2\right).
 \end{aligned}\tag{4}
\]
When \(0<\lambda\le1/2\), the bracket is at least
\(1-7/9-1/12=5/36>0\). Therefore (4) is strict unless \(d=0\), which forces \(t=t^{\rm dg}\). Equations (3) and (4) prove the complete direction classification for these factors.

**3. Euler product and spherical extremes.** The standard uniformly convergent Euler product for \(\cosh\) is
\[
 \cosh w=\prod_{m=0}^\infty
        \left(1+\frac{4w^2}{\pi^2(2m+1)^2}\right).
\]
Using the four-form facet sum with \(y=ru\) gives
\[
 \Phi_K(ru)=\sum_{m=0}^\infty\log P_{\lambda_m}(t),
 \qquad \lambda_m=\frac{r^2}{\pi^2(2m+1)^2}.
\]
For \(0<r\le2\), \(0<\lambda_m\le4/\pi^2<1/2\). Taking logs and summing the strict factorwise inequalities proves the spherical bounds, with their equality sets. The axis value is \(4\log\cosh(r/2)\). In the body-diagonal direction, the four absolute linear forms equal \(\sqrt3\) once and \(1/\sqrt3\) three times, giving the displayed lower bound. At \(r=0\), all directions trivially tie.

**4. Exact level radii.** Each fixed unit ray meets \(\partial T\) once, by strict increase of \(r\mapsto\Phi_K(ru)\) for positive \(r\). The least radial intersection is at an axis and solves \(4\log\cosh(r/2)=1\), giving the closed form \(r_{\rm in}\). The body-diagonal intersection solves the strictly increasing lower-bound equation, hence is unique. It lies below two, since
\[
 \cosh(\sqrt3)\cosh^3(1/\sqrt3)
 \ge(1+3/2)(1+1/6)^3>e.
\]
The spherical inequality therefore applies at that intersection and shows that it is the **largest** radial intersection. Strictness proves that there are no other contacts.

**5. Optimal ellipsoids.** Both the John and Löwner ellipsoids of a full-dimensional compact convex body are unique. The full signed-permutation symmetry of \(T\) forces each unique ellipsoid to be centered at zero and its quadratic form to be a scalar multiple of the identity: coordinate sign changes kill mixed coefficients and coordinate permutations equate diagonal entries. Thus the two unique ellipsoids are centered Euclidean balls, and the previously computed extreme radial intersections determine their radii and exactly their contact orbits.

## Verification

The standalone `verify_oct_orlicz.py` uses exact rational arithmetic on 5,000 deterministic squared-direction samples to independently compare the four-factor product with polynomial (1), test both inequalities (2), and compare to the two extremal products. It also numerically brackets both one-dimensional radii by monotone bisection; this checks the normalization but does **not** prove the universal inequalities. A separate symbolic expansion of the four factors confirms (1) algebraically. The proof above establishes the infinite statement directly via (2)–(4) and Euler's product, rather than relying on these finite checks.

## Relationship to prior work

The new critical \(\log\cosh\) boundary integral and its Orlicz interpretation are **already established** by Haddad–Jiménez–Resende [1]; neither the definition nor the general smooth-boundary convergence theorem is claimed here. The source's Theorem 5 assumes \(C^3\) boundary; its proof and concluding Orlicz remark specify the functional but do not determine the exact three-dimensional octahedral ellipsoids or their rigid contact directions. The earlier general Orlicz projection-body framework [2] is substantially broader as a definition and theory of inequalities, but the material available for this comparison did not identify the particular numerical and directional classification here. Previous calculations for separable parallelotope versions of the same functional concern a different nonlinearly coupled facet-normal configuration; they do not imply the four-Rademacher-form inequalities (3)–(4).

## Limitations

This theorem concerns the canonical level one and the particular unit octahedron. The lower-directional inequality is asserted only up to radius two; it can change behavior at larger radii. No covariogram convergence theorem for the nonsmooth octahedron is deduced. The radii are tied to the unscaled normalization from [1], not an arbitrary alternative Orlicz normalization. The available literature comparison does not constitute a guarantee of absolute historical priority, and independent mathematical validation has not been performed.

## References

[1] J. Haddad, C. H. Jiménez, M. Resende, *A Smooth Covariogram and the Transition Between Projection Bodies*, arXiv:2610.11700v1, publicly available 8 October 2026, https://arxiv.org/html/2610.11700v1. In particular Theorem 5, its proof in Section 5, and the concluding Orlicz-projection-body remark.

[2] E. Lutwak, D. Yang, G. Zhang, *Orlicz projection bodies*, Advances in Mathematics 223 (2010), 220–242, DOI:10.1016/j.aim.2009.08.002. Definition and general theory cited in [1].
