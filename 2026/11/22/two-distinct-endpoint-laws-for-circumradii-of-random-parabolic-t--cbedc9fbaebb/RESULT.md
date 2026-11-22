# Two distinct endpoint laws for circumradii of random parabolic triangles

## Finding
Fix \(a>0\). Independently sample \(U_1,U_2,U_3\) uniformly from \([-a,a]\), and let \(T\) be the triangle with vertices \(P(U_i)=(U_i,U_i^2)\). These vertices are noncollinear almost surely. Let \(\mathcal R_a\) denote its Euclidean circumradius and define
\[
R_a^{\max}=\tfrac12(1+4a^2)^{3/2}.
\]
The essential support of \(\mathcal R_a\) is precisely \([1/2,R_a^{\max}]\). For \(\varepsilon\downarrow0\), at fixed \(a>0\),
\[
\boxed{\Pr(\mathcal R_a<\tfrac12+\varepsilon)
=\frac{2\pi}{3a^3}\varepsilon^{3/2}
+\frac{\pi}{5a^3}\varepsilon^{5/2}
+O_a(\varepsilon^{7/2})}
\]
and
\[
\boxed{\Pr(\mathcal R_a>R_a^{\max}-\varepsilon)
=\frac{\varepsilon^3}{192a^6(1+4a^2)^{3/2}}+O_a(\varepsilon^4).}
\]
The distinct exponents arise from two different geometric configurations: the lower endpoint is a nondegenerate three-parameter interior minimum at the parabola's vertex, whereas the upper endpoint consists of the two opposite corners of the parameter cube.

These statements include two conditional limit laws. Write \(\mathbf1=(1,1,1)^{\mathsf T}\) and \(H=I_3+\mathbf1\mathbf1^{\mathsf T}\). Conditional on the lower-tail event, \((U_1,U_2,U_3)/\sqrt\varepsilon\) converges in total variation to the normalized uniform law on
\[
E=\{z\in\mathbb R^3:z^{\mathsf T}Hz<4\},\qquad \operatorname{vol}(E)=16\pi/3.
\]
For the upper event, let \(\sigma\in\{-1,1\}\) indicate which of the two maximizing corners is nearer, put \(D_i=a-\sigma U_i\ge0\) and \(c_a=2a\sqrt{1+4a^2}\). Then \(\sigma\) converges to a fair sign, independently of the conditional limit of \((c_aD_1/\varepsilon,c_aD_2/\varepsilon,c_aD_3/\varepsilon)\), which is uniform on
\[
\Delta=\{v\in\mathbb R^3:v_i\ge0,\ v_1+v_2+v_3<1\}.
\]
Here the sign assignment can be made arbitrarily outside fixed disjoint neighborhoods of the two corners, because such points have zero upper-tail probability for sufficiently small \(\varepsilon\).

## Assumptions and scope
All probabilities are for three **independent uniform parameters**, rather than uniform Euclidean arclength, on the fixed graph \(P(u)=(u,u^2)\). The parameter \(a\) is fixed and strictly positive. Circumradius means the radius of the circle through the three distinct vertices, **not** the radius of their minimum enclosing disk. Degenerate samples have probability zero. Both probability inequalities can be replaced by non-strict inequalities because the random variable has no atoms at these levels. The \(O_a\) constants may depend on \(a\); no assertion of uniformity as \(a\to0\) is made.

## Proof
**Exact identity and extrema.** For distinct real \(u,v\),
\[
\|P(u)-P(v)\|=|u-v|\sqrt{1+(u+v)^2}.
\]
The unsigned area of the triangle is
\[
\frac12|(u-v)(v-w)(w-u)|.
\]
Substitute these into the classical identity \(R=\ell_1\ell_2\ell_3/(4\operatorname{area})\). Cancellation yields the exact, continuously extendible formula
\[
\mathcal R(u,v,w)=\frac12\prod_{\{i,j\}\subset\{1,2,3\}}
\sqrt{1+(u_i+u_j)^2}. \tag{1}
\]
Each factor is at least one, and equality in all factors forces \(u_1=u_2=u_3=0\). Each is at most \(\sqrt{1+4a^2}\). Equality in all upper bounds forces either \((u_1,u_2,u_3)=(a,a,a)\) or \((-a,-a,-a)\). Continuity on the parameter cube then establishes the claimed essential support, including its endpoints as limiting configurations of nondegenerate triangles.

**Lower-tail localization and leading coefficient.** Put \(s_{ij}=u_i+u_j\). If \(\mathcal R<1/2+\varepsilon\), (1) implies \(|s_{ij}|\le2\sqrt{\varepsilon(1+\varepsilon)}\). As \(u_i=(s_{ij}+s_{ik}-s_{jk})/2\), the whole event lies within \(O(\sqrt\varepsilon)\) of the origin; hence, for small \(\varepsilon\), the parameter-cube boundary is irrelevant. Set \(u=\sqrt\varepsilon z\). With
\[
Q(z)=\frac14\sum_{i<j}(z_i+z_j)^2=\frac14z^{\mathsf T}Hz,
\]
a uniform Taylor expansion on bounded \(z\)-sets gives
\[
\frac{\mathcal R(\sqrt\varepsilon z)-1/2}{\varepsilon}
=Q(z)+\varepsilon T(z)+O(\varepsilon^2),
\quad T(z)=\frac1{16}\Big(\sum_{i<j}(z_i+z_j)^2\Big)^2
-\frac18\sum_{i<j}(z_i+z_j)^4. \tag{2}
\]
The matrix \(H\) has eigenvalues \(4,1,1\). Therefore \(\{Q<1\}\) has volume \(16\pi/3\). Dividing by the parameter cube volume \(8a^3\) gives the leading coefficient \(2\pi/(3a^3)\).

**Exact second coefficient.** Apply \(z=2H^{-1/2}y\), with Jacobian \(4\). Then \(Q(z)=\|y\|^2\). For \(\omega\in S^2\), each of the three linear forms \(z_i+z_j\) becomes a linear functional of \(\omega\) with coefficient-vector length two, since
\[
(e_i+e_j)^{\mathsf T}H^{-1}(e_i+e_j)=1.
\]
Consequently its fourth-power spherical mean is \(16/5\), by \(\mathbb E[(v\cdot\omega)^4]=\|v\|^4/5\). On the unit sphere \(\sum_{i<j}(z_i+z_j)^2=4\), so the spherical mean of \(T\) in (2) equals \(1-3(16/5)/8=-1/5\). The perturbed radial boundary is
\[
r(\omega,\varepsilon)=1-\tfrac12\varepsilon T(2H^{-1/2}\omega)+O(\varepsilon^2).
\]
Integrating \(r^3/3\) over the sphere and multiplying by the Jacobian gives the exact parameter-space sublevel volume
\[
\varepsilon^{3/2}\bigl(16\pi/3+8\pi\varepsilon/5+O(\varepsilon^2)\bigr).
\]
Division by \(8a^3\) proves the stated two-term lower expansion. Smoothness and transversality of the limiting ellipsoidal boundary justify the uniform radial expansion and the remainder. Bounded support and convergence in measure of the scaled sublevel sets also imply the stated lower conditional total-variation convergence.

**Upper-tail coefficient and limit.** Let \(M=R_a^{\max}\). On the positive corner write \(u_i=a-d_i\), \(d_i\ge0\). Differentiating (1) shows that each derivative of \(\mathcal R\) with respect to \(u_i\) at this corner is
\[
\left.\frac{\partial\mathcal R}{\partial u_i}\right|_{(a,a,a)}
=M\frac{4a}{1+4a^2}=c_a.
\]
Thus
\[
M-\mathcal R(a-d_1,a-d_2,a-d_3)
=c_a(d_1+d_2+d_3)+O_a(\|d\|^2).
\]
The negative corner gives the reflected expression. The two corners are the only global maximizers, so compactness localizes any upper-tail event to these neighborhoods, and positivity of \(c_a\) further forces \(\|d\|=O_a(\varepsilon)\). After scaling \(v_i=c_ad_i/\varepsilon\), the allowable set converges, with volume error \(O_a(\varepsilon)\), to \(\Delta\), whose volume is \(1/6\). There are two equal corner contributions, so
\[
\Pr(\mathcal R>M-\varepsilon)
=\frac{2}{(2a)^3}\frac{\varepsilon^3}{c_a^3}
\bigl(\tfrac16+O_a(\varepsilon)\bigr)
=\frac{\varepsilon^3}{192a^6(1+4a^2)^{3/2}}+O_a(\varepsilon^4).
\]
The same indicator-set convergence after scaling proves total variation for the corner label and the uniform simplex law.

## Verification
The standalone program `checks/check_parabolic_circumradii.py` checks the determinant cancellation and pair-sum formula against direct Euclidean circumradius computations, verifies the lower ellipsoid matrix and fourth-moment coefficient exactly, evaluates the true lower-tail sublevel volumes by deterministic spherical quadrature, and checks the upper-corner gradient. It prints `PARABOLIC_CIRCUMRADIUS_ENDPOINTS_CHECKS_OK` on successful completion. Finite numerical tests corroborate, but do not replace, the analytic limits and the total-variation arguments.

## Relationship to prior work
Kim and Shim's 2014 paper on triangles associated with strictly convex plane curves explicitly considers the parabola and triangles formed by contact points, but its invariants are **areas of contact triangles and tangent triangles**, and its main results characterize parabolas via area relations. Those statements do not compute the circumradius distribution of independently sampled parabola points or either endpoint probability law [1]. Finch's 2010 analysis concerns sides and perimeter of triangles drawn **inside a disk**, with different sampling support and observable [2]. General circumradius identities are classical and are used as inputs, not claimed as new. A targeted comparison with published mathematical findings about circumradii of area-uniform disk triangles, polygonal boundary triangles, and parabolic random hulls revealed different sampling domains and questions, not a statement implying both formulas above. Absence of a matching indexed statement is not proof of historical priority.

## Limitations
The closed formula (1) itself is an elementary consequence of the circumradius identity; the claimed contribution is the **joint exact support classification, sharp two-term lower tail, distinct upper tail, and conditional limiting configurations** under a specified natural sampling law. No full cumulative distribution is asserted. Sampling uniform in arclength would change the constants and requires a new calculation. Neither the two-dimensional disk-triangle results nor general convex-body asymptotics can be equated with the present one-dimensional parabolic sampling without further argument. Priority remains provisional and independent specialist validation has not occurred.

## References
1. D.-S. Kim and K.-C. Shim, *Area of triangles associated with a curve*, arXiv:1401.4751v1, first public 2014-01-19, https://arxiv.org/abs/1401.4751. Primary MSC 53A04.
2. S. Finch, *Perimeter Variance of Uniform Random Triangles*, arXiv:1007.0261v1, first public 2010-07-01, https://arxiv.org/abs/1007.0261.
3. Classical Euclidean circumradius identity \(R=abc/(4\operatorname{area})\), used in the proof of (1).
