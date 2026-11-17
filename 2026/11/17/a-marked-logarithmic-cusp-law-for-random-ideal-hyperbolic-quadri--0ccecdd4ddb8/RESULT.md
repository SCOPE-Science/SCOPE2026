# A marked logarithmic cusp law for random ideal hyperbolic quadrilaterals

## Finding

Let four independent uniform boundary points of the unit Poincaré disk be written counterclockwise, beginning at one designated sampled point of angular coordinate \(\Phi\). Let \(X,Y,Z,W\) be the successive positive angular gaps, summing to \(2\pi\). Set
\[
Q=\frac{\sin(X/2)\sin(Z/2)}{\sin((X+Y)/2)\sin((Y+Z)/2)}\in(0,1).
\]
This is the Ptolemy-normalized cross ratio of the four boundary vertices: the product of the first and third side chords divided by the product of the two diagonals. For \(0<\varepsilon<1\), on \(Q<\varepsilon\), define
\[
U_\varepsilon=\frac{\log X}{\log\varepsilon},\qquad V_\varepsilon=\frac Q\varepsilon.
\]
Then, as \(\varepsilon\downarrow0\), the **complete joint conditional law**
\[
\mathcal L(\Phi,Y,U_\varepsilon,V_\varepsilon\mid Q<\varepsilon)
\]
converges **in total variation** to the product of four probability measures: uniform arclength on \([0,2\pi)\), the angular law \(\sin^2(y/2)\,dy/\pi\) on \((0,2\pi)\), and two independent uniform laws on \((0,1)\). In particular, the two opposite gaps \(X,Z\) both vanish, and, for every fixed interior logarithmic exponent \(u\), their respective scales are \(\varepsilon^u\) and \(\varepsilon^{1-u}\); the exponent is asymptotically uniform and independent of the macroscopic separation and normalized cross ratio. The scalar cusp probability used for normalization is previously known, **not claimed as new**:
\[
\Pr(Q<\varepsilon)\sim\frac3{\pi^2}\varepsilon\log(1/\varepsilon).
\]

## Assumptions and scope

The sampling law consists of exactly four independent Euclidean-arclength-uniform boundary points on the same unit circle. The origin and the boundary angular coordinate are part of this sampling convention; the marked angular variables are not individually Möbius invariants. The root is a designated original point (not the smallest angle relative to a fixed coordinate), and the other points are taken in increasing counterclockwise angular order. The four gaps divided by \(2\pi\) have the \(\operatorname{Dirichlet}(1,1,1,1)\) distribution independently of the root phase \(\Phi\). Thus \((X,Y,Z)\) has constant density \(3/(4\pi^3)\) on \(x,y,z>0\) with \(x+y+z<2\pi\). All statements concern a fixed four-vertex ideal quadrilateral in curvature \(-1\), with no independent audit implied.

## Proof

**1. Exact angular coordinate and monotonicity.** For four points on a circle, a chord subtending angle \(s\) has length \(2\sin(s/2)\). Consequently the specified ratio \(Q\) is exactly the displayed expression. Given \(x,y>0\), \(x+y<2\pi\), put
\[
B(x,y)=\frac{\sin(x/2)}{\sin((x+y)/2)}.
\]
For \(0<z<2\pi-x-y\), the function \(q=B(x,y)\sin(z/2)/\sin((y+z)/2)\) is strictly increasing from \(0\) to \(1\). Differentiation gives
\[
\frac{\partial q}{\partial z}=\frac{B(x,y)\sin(y/2)}{2\sin^2((y+z)/2)}>0,
\qquad
\frac{\partial z}{\partial q}=\frac{2\sin^2((y+z)/2)}{B(x,y)\sin(y/2)}.
\]
This proves the global invertibility required for the density change of variables; no spurious solution branches occur.

**2. Pointwise marked density.** Fix any \(u\in(0,1)\), \(y\in(0,2\pi)\) and \(v\in(0,1)\), and substitute \(x=\varepsilon^u\), \(q=\varepsilon v\). Because \(x\to0\), \(q/x\to0\), the uniquely determined \(z=z_\varepsilon(u,y,v)\) satisfies
\[
z=\frac{4\varepsilon v\sin^2(y/2)}{x}\,(1+o(1))
\quad\text{and}\quad
\left|\frac{\partial(x,z)}{\partial(u,v)}\right|
=4\varepsilon\log(1/\varepsilon)\sin^2(y/2)(1+o(1)).
\]
Indeed \(B(x,y)=x/(2\sin(y/2))(1+o(1))\), \(z\to0\), \(|dx/du|=x\log(1/\varepsilon)\), and \(dq/dv=\varepsilon\). These asymptotics are pointwise on every interior triple and uniform on any compact subset of that interior. The three-gap Dirichlet density therefore gives the *unconditioned* density, with respect to \(du\,dy\,dv\), as
\[
\frac3{\pi^3}\varepsilon\log(1/\varepsilon)\sin^2(y/2)(1+o(1)).
\]
For fixed \(u<0\) the coordinate \(x=\varepsilon^u\) eventually exceeds the total circle length, so the density vanishes. For fixed \(u>1\) and interior \(y,v\), the inverse solution instead approaches \(z=2\pi-y\), with the remaining gap \(w=2\pi-x-y-z\sim x/(\varepsilon v)\). The Jacobian is then \(O(x^2\log(1/\varepsilon)/\varepsilon)\), and after division by the scalar event probability the conditional density is \(O((x/\varepsilon)^2)\to0\). Hence pointwise conditional convergence holds also outside the limiting support, except on measure-zero boundaries; no unproved tightness assumption is used.

**3. Exact normalization from known literature.** The classical circularly ordered version of Martin's full cross-ratio distribution (Theorem 4.1 of the cited 2018 public preprint) gives
\[
f_Q(q)=\frac3{\pi^2}\left[
\frac{-\log(1-q)}q+\frac{-\log q}{1-q}
\right],\qquad 0<q<1.
\]
The factor three conditions the author's labelled cross-ratio law on the cyclic interval \((0,1)\); the two alternative cyclic choices \(q\) and \(1-q\) have the same density. The expression integrates to one because each bracketed term integrates to \(\pi^2/6\). Integration at zero yields
\[
\Pr(Q<\varepsilon)=\frac3{\pi^2}\varepsilon\log(1/\varepsilon)+O(\varepsilon).
\]
This scalar distribution, including its cusp, predates the present marked statement and is only an input, not a new finding.

**4. Total variation, not only convergence of moments.** Divide the unconditioned marked density by the preceding exact event probability. On the interior \((u,y,v)\in(0,1)\times(0,2\pi)\times(0,1)\) the resulting conditional density converges pointwise to
\[
g(u,y,v)=\frac{\sin^2(y/2)}\pi.
\]
Extend \(g\) by zero elsewhere in \(\mathbb R\times(0,2\pi)\times(0,1)\). Because
\[
\int_0^1du\int_0^{2\pi}\frac{\sin^2(y/2)}\pi\,dy\int_0^1dv=1,
\]
and the exact conditional densities each integrate to one, Scheffé's lemma gives \(L^1\), equivalently total-variation, convergence of the three marks. The rotation phase \(\Phi\) is exactly independent and uniform for every \(\varepsilon\), so adjoining it preserves total-variation convergence. The log-scaling of \(Z\) follows from the \(z\)-asymptotic in step 2 and concentration in the stated limiting interior.

## Verification

The standalone `verify.py` checks Martin's density normalization by quadrature, checks the *exact* derivative of the cross-ratio mapping against the boundary-layer Jacobian at multiple decreasing scales, and samples two million independent Dirichlet gap quadruples with a fixed seed. Its three scalar event-rate comparisons lie within five binomial standard errors of the integral of the known density; it also reports finite-threshold conditional mark means. The checker returns `MARKED_IDEAL_QUADRILATERAL_CHECKS_OK`. The theorem is established by the analytic proof above; the finite experiments are only corroboration. All proof steps are independent of a numerical extrapolation.

## Relationship to prior work

Vuorinen and Wang (2012) provide the pre-2016 geometry of ideal and Lambert hyperbolic quadrilaterals, including opposite-side distance inequalities and the MSC 51M09 setting. Izmestiev (2014) develops cyclic-quadrilateral cross-ratio and hyperbolic-geometric identities without this sampling limit. Martin (first public 2018) computes the *complete unmarked* law of the cross ratio for four uniform circle points and related random punctured-torus moduli. The present finding begins **after** that scalar law: it concerns the joint conditional distribution of the actual angular placement and two coupled collision scales, which the one-variable marginal does not determine. Other random-geometry near-collision results may display logarithmic scales but concern different objects and are not an implication of Martin's scalar density. No uniqueness or definitive historical-priority claim is made from failed searches.

## Limitations

The boundary angular marks depend on Euclidean-arclength-uniform sampling and the chosen disk center; they are not themselves conjugacy invariants of ideal hyperbolic quadrilaterals. The result fixes four vertices; it gives a limiting, not an exact finite-threshold, four-mark distribution. It does not cover nonuniform endpoint laws, polygons with more vertices, or rates of total-variation convergence. Historical priority remains subject to sources not indexed or read, and independent mathematical validation has not been performed.

## References

1. M. Vuorinen and G. Wang, *Hyperbolic Lambert Quadrilaterals and Quasiconformal Mappings*, arXiv:1203.6494, first public March 29, 2012, https://arxiv.org/abs/1203.6494 (2010 MSC 51M09, 51M15).
2. I. Izmestiev, *A porism for cyclic quadrilaterals, butterfly theorems, and hyperbolic geometry*, arXiv:1408.2247, first public August 10, 2014, https://arxiv.org/abs/1408.2247.
3. G. J. Martin, *Random Ideal Hyperbolic Quadrilaterals, the Cross Ratio Distribution and Punctured Tori*, arXiv:1807.06202, first public July 17, 2018, Theorem 4.1, https://arxiv.org/abs/1807.06202. The known scalar law is explicitly credited to this source.
4. G. Wang, M. Vuorinen and X. Zhang, *On cyclic quadrilaterals in euclidean and hyperbolic geometries*, arXiv:1908.10389, first public August 27, 2019, https://arxiv.org/abs/1908.10389.
