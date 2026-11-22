# Two sharp cap-spectral transitions on quaternionic projective space

## Finding
Fix an integer \(d\ge3\). Give quaternionic projective space \(\mathbb{HP}^{d-1}\) its normalized invariant probability measure. Its first nonconstant Laplace eigenspace is the complexification of the real functions
\[
 f_A([u])=u^*Au,\qquad u\in\mathbb H^d,\quad u^*u=1,
 \quad A=A^*,\quad \operatorname{tr}_{\mathbb H}A=0.
\]
For the geodesic cap \(C_t=\{[u]:|u_1|^2\ge t\}\), \(0<t<1\), let \(T_t\) be the concentration operator on this eigenspace, characterized by
\[
 \langle T_tf,g\rangle=\int_{C_t}f\overline g\,d\mu.
\]
Its entire spectrum consists of the three branches below, including their multiplicities:
\[
\begin{aligned}
\lambda_{\mathrm{ax}}&=(1-t)^{2d-2}\bigl[1+2(d-1)t-(2d-1)(d+2)t^2+2d^2(2d-1)t^3\bigr], &&(1),\\
\lambda_{\mathrm{cross}}&=(1-t)^{2d-1}\bigl[1+(2d-1)t+d(2d-1)t^2\bigr], &&(4(d-1)),\\
\lambda_{\mathrm{tan}}&=(1-t)^{2d}(1+2dt), &&(2d^2-5d+2).
\end{aligned}
\]
The smallest concentration eigenvalue changes branch at \(t=1/(2d)\): it is axial below this threshold and tangential above it. The largest changes at the distinct threshold \(t=1/d\): it is the cross branch below and the axial branch above. At equality the indicated eigenspaces join, and no other extremal branch changes occur. Thus the exact *squared* condition number of cap restriction is
\[
 \kappa_d(t)=
 \begin{cases}
 \lambda_{\mathrm{cross}}/\lambda_{\mathrm{ax}}, &0<t\le1/(2d),\\
 \lambda_{\mathrm{cross}}/\lambda_{\mathrm{tan}}, &1/(2d)\le t\le1/d,\\
 \lambda_{\mathrm{ax}}/\lambda_{\mathrm{tan}}, &1/d\le t<1.
 \end{cases}
\]
Every nonempty cap gives injective restriction, and the thin-cap law is
\[
 \kappa_d(t)\sim\frac{(d-1)(2d-1)}{(1-t)^2}\qquad(t\uparrow1).
\]

A second, dimension-free description arises at fixed cap volume. Let \(t_d\) be the unique cap height with \(\mu(C_{t_d})=v\in(0,1)\), and let \(y>0\) solve \((1+y)e^{-y}=v\). Then \(2dt_d\to y\), and
\[
\lim_{d\to\infty}\kappa_d(t_d)=
\begin{cases}
\dfrac{1+y+y^2/2}{1+y-y^2/2+y^3/2},&0<y\le1,\\[4pt]
\dfrac{1+y+y^2/2}{1+y},&1\le y\le2,\\[4pt]
\dfrac{1+y-y^2/2+y^3/2}{1+y},&y\ge2.
\end{cases}
\]
The two exact limiting critical cap volumes are \(2/e\) and \(3/e^2\).

## Assumptions and scope
The projective class \([u]\) is invariant under right multiplication of \(u\) by unit quaternions; \(u^*Au\) is real for quaternionic Hermitian \(A\), so it descends to the quotient. The metric is the standard Hopf-quotient normalization (the displayed function space has Laplace eigenvalue \(8d\)); normalization of metric does not affect cap concentration if the cap is specified by \(|u_1|^2\). All functions are measured with normalized invariant Haar measure. The first eigenspace has complex dimension \(2d^2-d-1\). The restriction \(d\ge3\) ensures that all three branches occur with positive multiplicity. The condition number above is the eigenvalue ratio of the positive concentration operator, i.e. the square of the singular-value condition number of the restriction map.

## Proof
**First eigenspace and block decomposition.** Invariant homogeneous quadratic polynomials on \(\mathbb H^d\) are exactly the functions \(u\mapsto u^*Au\) with \(A\) quaternionic Hermitian. Their real Laplacian is proportional to \(\operatorname{tr}_{\mathbb H}A\), so the trace-free ones are degree-two spherical harmonics. There are no nonconstant degree-one harmonics invariant under the right unit-quaternion action. The Hopf quotient therefore identifies these trace-free quadratics with the first nonconstant projective Laplace eigenspace. Quaternionic Hermitian matrices have real dimension \(2d^2-d\); removing the trace gives \(2d^2-d-1\).

Write \(u=(u_1,u')\) and split the matrix into a scalar axial diagonal block, quaternionic off-diagonal blocks joining coordinate one to the remaining coordinates, and a trace-free Hermitian block supported on the remaining coordinates. The corresponding real spaces have dimensions \(1\), \(4(d-1)\), and \(2d^2-5d+2\). They are mutually orthogonal on the full projective space and on every \(C_t\): conditional on \(s=|u_1|^2\), symmetry makes each cross or trace-free tangential term have zero conditional mean, and parity kills cross–tangential products.

**Radial profiles.** For Haar-uniform \(u\), the squared quaternionic coordinate norms have Dirichlet shape parameters equal to two. Thus \(s\) has the \(\operatorname{Beta}(2,2d-2)\) distribution. Conditional on \(s\), the axial function is a multiple of \(s-1/d\). Cross-block squared norms acquire a factor \(s(1-s)\), and tangential-block squared norms acquire \((1-s)^2\). Polarization shows that the cap quadratic form is a scalar multiple of the full quadratic form on each block. Their eigenvalues consequently equal
\[
\begin{aligned}
 \lambda_{\mathrm{ax}}&=\frac{\mathbb E[(s-1/d)^2\mathbf1_{s\ge t}]}{\mathbb E[(s-1/d)^2]},\\
 \lambda_{\mathrm{cross}}&=\frac{\mathbb E[s(1-s)\mathbf1_{s\ge t}]}{\mathbb E[s(1-s)]},\\
 \lambda_{\mathrm{tan}}&=\frac{\mathbb E[(1-s)^2\mathbf1_{s\ge t}]}{\mathbb E[(1-s)^2]}.
\end{aligned}
\]
The last two ratios are survival probabilities of \(\operatorname{Beta}(3,2d-1)\) and \(\operatorname{Beta}(2,2d)\), respectively. For the axial ratio, use \(\mathbb Es=1/d\), \(\mathbb Es^2=3/[d(2d+1)]\), and \(\operatorname{Var}(s)=(d-1)/[d^2(2d+1)]\). Substituting the elementary integer-shape beta survival formula
\[
 \Pr\{\operatorname{Beta}(a,b)\ge t\}
 =\sum_{k=0}^{a-1}\binom{a+b-1}{k}t^k(1-t)^{a+b-1-k}
\]
produces the three displayed polynomials without approximation.

**Exact ordering and both thresholds.** Direct algebra, with no limiting argument, gives
\[
\begin{aligned}
\lambda_{\mathrm{ax}}-\lambda_{\mathrm{cross}}
 &= (4d^2-1)t^2(1-t)^{2d-2}(dt-1),\\
\lambda_{\mathrm{cross}}-\lambda_{\mathrm{tan}}
 &=d(2d+1)t^2(1-t)^{2d-1}>0,\\
\lambda_{\mathrm{ax}}-\lambda_{\mathrm{tan}}
 &=(d-1)(2d+1)t^2(1-t)^{2d-2}(2dt-1).
\end{aligned}
\]
Because all omitted factors are strictly positive on the stated domain, these factorizations prove the complete extremal classification and each equality case. In particular the tangential branch and the axial branch exchange minimum at half the height of the axial–cross maximum exchange. For \(t\uparrow1\), the leading axial polynomial coefficient at \(t=1\) is \((d-1)(2d-1)(2d+1)\), whereas the tangential factor is \(2d+1\), proving the thin-cap law.

**Fixed-volume limit.** The exact cap volume is \(v_d(t)=(1-t)^{2d-2}[1+(2d-2)t]\), strictly decreasing for \(0<t<1\). At \(t=y/(2d)\) it tends to \((1+y)e^{-y}\). Monotonic inversion shows \(2dt_d\to y\). Evaluating the three eigenvalue formulas at these heights gives limits
\[
 e^{-y}(1+y-y^2/2+y^3/2),\quad e^{-y}(1+y+y^2/2),\quad e^{-y}(1+y),
\]
for axial, cross, and tangential sectors. Their differences change signs only at \(y=1\) and \(y=2\), proving the claimed three-piece limiting condition number. Strict positivity of each denominator follows either from these expressions or their defining positive tail integrals.

## Verification
The included standalone Python program `check.py` uses exact rational polynomial integration, independently reconstructing the three normalized radial moments for 60 dimension–height cases with \(3\le d\le12\). It tests all three difference factorizations, branch ordering (including the transition heights), the positive-spectrum bounds and the independent trace identity \(\operatorname{tr}T_t=(2d^2-d-1)\mu(C_t)\). A further test checks convergence to the displayed three fixed-volume scaling profiles. All checks passed. They corroborate rather than replace the proof for arbitrary \(d\) and \(t\).

## Relationship to prior work
Jaming and Speckbacher (first public version 6 April 2020) study concentration of finite spectral expansions on compact two-point homogeneous spaces, explicitly including quaternionic projective spaces. Their Theorem 4.4 gives a general large-sieve upper estimate; it does not calculate the full first-eigenspace cap restriction spectrum or the two distinct optimal-mode transition heights. Ahrens, Cowling, Martini and Müller develop quaternionic spherical-harmonic decomposition for sub-Laplacian multiplier theory, but not this projective-cap restriction spectrum. Related exact cap calculations for complex projective harmonics involve a different coordinate-law shape and do not imply the quaternionic double-switch formula. The sector reduction and beta moments are classical tools; the claimed addition is their complete explicit extremal classification and the two sharp finite- and high-dimensional transition thresholds. Historical novelty is provisional, not a statement of definitive priority.

## Limitations
Only the first nonconstant eigenspace on \(\mathbb{HP}^{d-1}\), \(d\ge3\), is studied. The formulas are not claimed for arbitrary sums of eigenlevels, deformed caps, or discrete observations. At the two crossing heights the extremizing eigenspaces are nonunique as specified; away from crossings the axial extremizer is one-dimensional while the other extrema have the stated branch multiplicities. The supporting numerical calculations are finite and do not prove the universal result. Independent mathematical audit has not been performed. It remains possible that an older result formulated as an isotropy-decomposition integral already implies the same sharp thresholds.

## References
1. P. Jaming and M. Speckbacher, *Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle*, arXiv:2004.02474 (first submitted 6 April 2020), especially Sections 3.1 and 4, Theorem 4.4. https://arxiv.org/abs/2004.02474
2. J. Ahrens, M. G. Cowling, A. Martini and D. Müller, *Quaternionic spherical harmonics and a sharp multiplier theorem on quaternionic spheres*, arXiv:1612.04802 (first submitted 14 December 2016); related harmonic-decomposition context, not a source for the present concentration spectrum. https://arxiv.org/abs/1612.04802
