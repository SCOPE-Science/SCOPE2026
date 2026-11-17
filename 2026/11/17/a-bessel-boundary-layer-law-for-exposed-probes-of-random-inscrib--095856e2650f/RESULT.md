# A Bessel boundary-layer law for exposed probes of random inscribed polygons

## Finding
Let \(K\subset\mathbb R^2\) be a strictly convex compact body with \(C^3\) boundary \(\Gamma\), strictly positive curvature \(\kappa\), and a strictly positive \(C^1\) arclength probability density \(f\). Fix a boundary point \(z\) and its inward unit normal \(\nu(z)\). For each integer \(n\ge3\), let \(P_n\) be the convex hull of \(n\) independent points with boundary law \(f\,ds\). At depth \(t/n^2\), define the deterministic *probe* \(z_{n,t}=z+t\nu(z)/n^2\), for fixed \(t>0\), and the exposure event \(E_{n,t}=\{z_{n,t}\notin P_n\}\).

Put \(x=2t f(z)^2/\kappa(z)\), and let \(K_1\) denote the modified Bessel function of the second kind of order one. Then
\[
\boxed{\lim_{n\to\infty}\Pr(E_{n,t})=H(x):=2\sqrt{x}\,K_1(2\sqrt{x})=\int_0^\infty e^{-u-x/u}\,du.}
\]
The function \(H:(0,\infty)\to(0,1)\) is continuous and strictly decreasing. Thus for known positive \(f(z)\), a single limiting exposure probability at any fixed positive \(t\) determines the curvature \(\kappa(z)\) exactly; for uniform arclength sampling the required density is the reciprocal perimeter.

Choose an arclength origin at \(z\), oriented counterclockwise. Let \(U_n>0\) and \(V_n>0\) be the arclength distances from \(z\) to the nearest sampled vertices respectively forward and backward along \(\Gamma\). Conditionally on exposure, the pair of normalized gaps converges **in total variation**:
\[
\boxed{\mathcal L\bigl(n f(z)U_n,n f(z)V_n\mid E_{n,t}\bigr)\ \xrightarrow{\rm TV}\ \frac{e^{-u-v}{\mathbf{1}}\{u v>x\}}{H(x)}\,du\,dv.}
\]
Before conditioning, the pair converges in total variation to two independent unit exponentials. More strongly, for any fixed finite collection of *distinct* boundary points \(z_1,\ldots,z_m\) and positive depths \(t_1,\ldots,t_m\), the joint laws of their normalized forward/backward gaps and exposure indicators converge in total variation to **independent copies of the displayed local construction**, with respective parameters \(x_j=2t_j f(z_j)^2/\kappa(z_j)\). In particular, the exposure indicators at these distinct fixed sites become independent, although they arise from the same random polygon.

The critical scale is exactly \(n^{-2}\): for any deterministic positive depth sequence \(\delta_n\to0\), the exposure probability tends to one when \(n^2\delta_n\to0\), and to zero when \(n^2\delta_n\to\infty\). These are local inward boundary-layer assertions, with both depth sequences tending to zero. The limiting crossover satisfies
\[
H(x)=1+x(\log x+2\gamma-1)+O(x^2|\log x|)\quad(x\downarrow0),
\qquad H(x)\sim\sqrt\pi\,x^{1/4}e^{-2\sqrt x}\quad(x\to\infty),
\]
where \(\gamma\) is Euler's constant.

## Assumptions and scope
The body and density are fixed as the sample size tends to infinity. Curvature is the ordinary *unsigned* Euclidean curvature of \(\Gamma\), measured per unit arclength. The density integrates to one over the entire boundary. The local sites \(z_j\) are distinct and fixed independently of \(n\). Total variation means the supremum of the difference of probability measures over measurable events; no independent validation is asserted. No claim is made for curvature zero, corners, zero sampling densities, or collections of probe sites whose mutual distances shrink with \(n\).

## Proof
**1. Exact local gap geometry.** Choose signed arclength \(s\) about \(z\) and orient tangent-normal coordinates so the tangent is horizontal and positive inward normal points upward. The \(C^3\) expansion is
\[
\gamma(s)=\bigl(s+O(s^3),\,\kappa(z)s^2/2+O(s^3)\bigr).
\]
For small \(u,v>0\), the chord joining \(\gamma(-v)\) and \(\gamma(u)\) crosses the inward normal line through \(z\) at height
\[
D(u,v)=\frac{\kappa(z)}2uv+O(uv(u+v)).\tag{1}
\]
The displayed *relative* error follows from divided differences of the \(C^3\) coordinate expansions. The curve is strictly convex and all sampled points occur as vertices of the inscribed polygon. The chord joining the two cyclic neighbors of \(z\) is an edge of that polygon. On every sequence of configurations with \(u,v\to0\), the normal probe is inside the polygon precisely when its inward depth is at least \(D(u,v)\), for all sufficiently small depth: the other edges are separated from the probe by a positive local neighborhood, and the polygon lies on the inward side of its local edge. Consequently, up to null equality events, \(E_{n,t}=\{D(U_n,V_n)>t/n^2\}\) with probability tending to one.

**2. Joint local Poisson spacing law in total variation.** Write \(f_0=f(z)>0\) and let \(a,b>0\) denote forward and backward arclengths. For \(a+b\) less than one full perimeter, the nearest-gap pair has joint density
\[
 p_n(a,b)=n(n-1)f(z+a)f(z-b)\left(1-\int_{-b}^{a}f(z+s)\,ds\right)^{n-2},\tag{2}
\]
with the signed arclength notation understood periodically. This follows by choosing the two labeled nearest sample points, requiring all remaining points to avoid the open intervening arc, and integrating their unconstrained positions. After the substitution \(a=u/(nf_0)\), \(b=v/(nf_0)\), its density converges pointwise for every fixed positive \(u,v\) to \(e^{-u-v}\). Both distributions have total mass one, hence Scheffé's lemma gives total-variation convergence. Moreover, \(U_n,V_n=O_{\mathsf P}(n^{-1})\).

For several fixed distinct sites, restrict first to bounded rescaled gap windows small enough that their underlying arclength arcs are pairwise disjoint. The exact joint density has leading factor \((n)_{2m}\) and no-sample factor \((1-\sum_j\int_{-b_j}^{a_j} f(z_j+s)\,ds)^{n-2m}\). After rescaling it converges pointwise to \(\prod_{j=1}^m e^{-u_j-v_j}\). The probability of leaving any sufficiently large bounded gap window is uniformly small for large \(n\), by exponential empty-arc bounds. Thus the joint convergence holds in total variation, and the distinct sites have asymptotically independent exponential pairs.

**3. The exposure transformation.** Multiplying (1) by \(n^2\), while setting \(u=U/(nf_0)\), \(v=V/(nf_0)\), yields
\[
n^2D(U_n,V_n)=\frac{\kappa(z)}{2f_0^2}(n f_0U_n)(n f_0V_n)+o_{\mathsf P}(1).\tag{3}
\]
The product of independent exponentials has a continuous distribution, so the equality boundary \(uv=x\) has zero limiting measure. By the density convergence from step 2, mapping the gap pairs to exposure flags produces convergence in total variation on \(\mathbb R_+^2\times\{0,1\}\), not merely weak convergence. Its exposure probability is
\[
\Pr(E_1E_2>x)=\int_0^\infty\Pr(E_2>x/u)e^{-u}\,du
=\int_0^\infty e^{-u-x/u}\,du=H(x).\tag{4}
\]
Conditioning on an event with positive limiting probability \(H(x)>0\) gives the claimed truncated-exponential joint density in total variation. Applying the argument to the vector of disjoint local neighborhoods yields the finite-site independence statement.

**4. Exact Bessel formula, inversion and critical scaling.** The standard integral representation of \(K_1\) identifies (4) with \(2\sqrt x K_1(2\sqrt x)\). Differentiation under the integral gives \(H'(x)=-\int_0^\infty e^{-u-x/u}\,du/u<0\). The endpoint limits are \(H(0+)=1\) and \(H(\infty)=0\), establishing the exact inversion for curvature. The small- and large-argument Bessel expansions give the displayed asymptotics. If \(n^2\delta_n\to0\), compare the outside event to the event at fixed depth \(t/n^2\), then let \(t\downarrow0\); likewise if \(n^2\delta_n\to\infty\), compare to fixed \(t/n^2\) and let \(t\to\infty\). Monotonicity of inclusion under increasing inward depth is valid in a fixed sufficiently short normal segment through \(z\), because the intersection of any convex set with that segment is an interval and the nearest endpoint of the random hull approaches the boundary. The hypotheses \(\delta_n\to0\) keep the probes in this local segment.

## Verification
Run `python check_boundary_probe.py` with NumPy and SciPy. It compares the Bessel survival function with its independent numerical integral; draws the exact circle-neighbor gaps using a Dirichlet construction for sample sizes \(60\) and \(300\) and three scaled depths; evaluates the exact circle chord intersection independently of the curvature expansion; and, for \(18{,}000\) separately simulated full circle polygons, compares the local-edge exposure test with all oriented hull-edge halfplanes. The checker ends with `BOUNDARY_PROBE_BESSEL_AND_CHORD_OK`. Finite tests do not prove the general limit or its total-variation assertion; those follow from steps 1–4.

## Relationship to prior work
Wendel's 1962 center-containment formula treats a fixed central point and a symmetric law, not the boundary-layer probes considered here. Schneider's 1988 paper establishes convergence rates for boundary-sampled random inscribed polygons, but its accessible publisher abstract does not resolve the present local conditional law. Brunel's arXiv version first posted 2015-03-05 supplies global Hausdorff deviation inequalities and a boundary cap-mass condition; Section 3.3, Proposition 4, does not evaluate a pointwise critical-window distribution or conditional neighboring gaps.

The published *Local curvature from the logarithmic containment law of random inscribed polygons* determines, for each **fixed sample size**, the first near-boundary inclusion asymptotic as inward depth tends to zero. Its remainder is not uniform in sample size and does not imply the present joint large-sample boundary-layer crossover or its conditional marked law. Other published random-polygon gap laws concern polygon corners, where the missed-area functional is a product of exponential gaps, or density zeros controlling global Hausdorff error, rather than the fixed smooth-point normal exposure at critical depth. The evaluated Bessel curve and its independent multisite conditional marks are the claims assessed here; no exhaustive priority certification is claimed.

## Limitations
The theorem addresses finitely many fixed sites on one smooth strictly convex planar curve, with strictly positive curvature and sampling density. It does not imply independence for probe sites that coalesce on the \(n^{-1}\) arclength scale, or for nonsmooth boundaries. The inverse statement requires the local sampling density to be known. Although the exact Bessel integral and conditional limit follow from a local Poisson mechanism, priority remains provisional because some earlier literature on local random-polygon processes is available only in abstract or partial form. Independent validation has not been performed.

## References
1. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica **11** (1962), 109–112, first published 1962-06-01, DOI: 10.7146/math.scand.a-10655, https://journals.msp.org/mscand/article/view/2688.
2. R. Schneider, *Random approximation of convex sets*, Journal of Microscopy **151** (1988), 211–227, DOI: 10.1111/j.1365-2818.1988.tb04682.x, https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1365-2818.1988.tb04682.x (publisher abstract inspected; original month known, not an exact day).
3. V.-E. Brunel, *Uniform Behaviors of Random Polytopes under the Hausdorff Metric*, arXiv:1503.01504v1, first submitted 2015-03-05, https://arxiv.org/abs/1503.01504 (full open-access v2 HTML inspected).
4. *Local curvature from the logarithmic containment law of random inscribed polygons*, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-local-curvature-from-the-logarithmic-containment-law-of-random-i--a0ac1da8caab (published result, full scientific text inspected).
5. *Two geometric phase transitions from a vanishing boundary sampling density*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-geometric-phase-transitions-from-a-vanishing-boundary-sampli--45b7be860cec (published result, full scientific text inspected).
6. NIST Digital Library of Mathematical Functions, Chapter 10, modified Bessel functions, https://dlmf.nist.gov/10.32 (standard integral representation).
