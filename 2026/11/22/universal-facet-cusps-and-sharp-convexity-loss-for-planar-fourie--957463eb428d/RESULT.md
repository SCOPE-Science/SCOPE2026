# Universal facet cusps and sharp convexity loss for planar Fourier mean bodies

## Finding

Let \(P\subset\mathbb R^2\) be **any** compact convex polygon with nonempty interior, and use the Fourier convention
\[
\widehat{\mathbf 1_P}(\xi)=\int_P e^{-i\langle \xi,x\rangle}\,dx.
\]
For \(p>0\), define the (possibly unbounded) Fourier mean star \(F_pP\) through
\[
\rho_p(u)^p=\frac{p}{A(P)}\int_0^\infty\big|\widehat{\mathbf 1_P}(ru)\big|^2r^{p-1}\,dr,
\qquad u\in\mathbb S^1,
\]
where \(A(P)>0\) is ordinary area. For \(1<p<2\), fix an outward unit normal \(n\) of any edge, and a perpendicular unit tangent \(t\). Let \(\mathcal E(n)\) consist of the maximal edges whose supporting lines are perpendicular to \(n\) (one edge, or two opposite parallel edges), and write \(\ell_E>0\) for their lengths. Put \(u(\theta)=n\cos\theta+t\sin\theta\).

**Theorem.** For every such \(P,n,p\), \(F_pP\) is a compact star body and
\[
\boxed{\rho_p(u(\theta))^p
=\rho_p(n)^p-\frac{p\pi}{A(P)\Gamma(5-p)\sin(\pi p/2)}
\left(\sum_{E\in\mathcal E(n)}\ell_E^{4-p}\right)|\theta|^{2-p}
+o(|\theta|^{2-p}).}
\]
In particular, the reciprocal radius has a **positive, exact \((2-p)\)-power cusp** at every facet normal:
\[
\boxed{\rho_p(u(\theta))^{-1}-\rho_p(n)^{-1}
=\frac{\pi\sum_{E\in\mathcal E(n)}\ell_E^{4-p}}
{A(P)\Gamma(5-p)\sin(\pi p/2)\rho_p(n)^{p+1}}
|\theta|^{2-p}+o(|\theta|^{2-p}).}
\]
Consequently **\(F_pP\) is nonconvex for every \(1<p<2\)**, irrespective of the number of polygon sides, parallelism, or symmetry. For \(p\ge2\), \(F_pP\) is unbounded (it has infinite radius in every edge-normal direction). Combined with the previously established convexity theorem for \(0<p\le1\), this gives a sharp universal convexity/compactness trichotomy for planar convex polygons.

## Assumptions and scope

All edges are understood as maximal nondegenerate line segments of the polygon boundary, so collinear consecutive subdivisions are merged. The polygon need not be centrally symmetric or regular. The angular limit is two-sided, with \(p\in(1,2)\) fixed. The Fourier normalization is crucial: there are no hidden \(2\pi\) factors in the transform. The exponent \(2-p\in(0,1)\) is the precise one-sided Hölder exponent of the displayed leading cusp, not a claim of global regularity at every direction.

## Proof

**1. Uniform radial finiteness below the first facet threshold.** For every unit \(u\), the divergence theorem and the polygonal edge decomposition give
\[
\widehat{\mathbf1_P}(ru)=\frac{i}{r}
\sum_E (u\cdot\nu_E)\ell_E
\exp(-ir\,u\cdot m_E)
\operatorname{sinc}\left(\frac{r\ell_E(u\cdot t_E)}2\right),
\qquad \operatorname{sinc}(z)=\frac{\sin z}{z},
\]
where \(\nu_E,t_E,m_E\) are an outward unit normal, a unit tangent, and midpoint of edge \(E\). This formula holds for \(r>0\). It yields \(|\widehat{\mathbf1_P}(ru)|\le C_P\min(1,r^{-1})\) uniformly in \(u\). The defining integral therefore converges for every \(0<p<2\), uniformly on the circle, and dominated convergence proves continuity. Since the transform is nonzero near zero, \(\rho_p(u)\) is bounded below by a strictly positive constant. Thus the associated star is compact and contains a disk.

**2. Isolating the edge-normal singularity.** Fix \(n,t\) and write \(u=u(\theta)\). In the edge formula, split the sum into \(S_\theta(r)\), over edges perpendicular to \(n\), and \(T_\theta(r)\), over the remaining edges. For \(r\ge1\) and sufficiently small \(|\theta|\),
\[
|S_\theta|\le C,\quad |\partial_\theta S_\theta|\le Cr,\quad
|T_\theta|\le C/r,\quad |\partial_\theta T_\theta|\le C.
\]
The bounds for \(T_\theta\) follow because \(|u(\theta)\cdot t_E|\) stays bounded away from zero on every nonparallel edge. Hence the contribution to the weighted integral from \(2\operatorname{Re}(S_\theta\overline{T_\theta})+|T_\theta|^2\) changes by \(O(|\theta|)\): its derivative is bounded by a multiple of \(r^{p-3}\), integrable at infinity for \(p<2\). The original Fourier integral on \(0<r<1\) also changes by \(O(|\theta|)\) by smoothness and dominated differentiation. Since \(|\theta|=o(|\theta|^{2-p})\), neither contributes to the leading cusp.

A convex polygon has at most two edges parallel to a prescribed tangent. For two distinct such edges, their midpoint separation has a nonzero component along \(n\). In the cross term of \(|S_\theta|^2\), the relevant oscillation is \(e^{ir q(\theta)}\), with \(q(0)\ne0\). Its nonattenuated integral \(\int_1^\infty r^{p-3}e^{ir q}\,dr\) is locally continuously differentiable for \(q\ne0\), so the change of \(q\) contributes \(O(|\theta|)\). The remaining attenuation term, after setting \(s=r|\sin\theta|\), is \(|\sin\theta|^{2-p}\) times the Fourier transform at frequency \(|q(\theta)/\sin\theta|\to\infty\) of an \(L^1(0,\infty)\) function of the form
\[
s^{p-3}\left[\operatorname{sinc}(a s)\operatorname{sinc}(b s)-1\right].
\]
It is \(o(|\theta|^{2-p})\) by the Riemann–Lebesgue lemma. Thus all cross-edge interactions are strictly lower order, even when the polygon has two opposite parallel sides.

**3. Exact self-edge coefficient.** For a parallel edge of length \(\ell\), its squared self-contribution to the weighted integral for \(r\ge1\) is
\[
\ell^2\cos^2\theta\int_1^\infty r^{p-3}
\operatorname{sinc}^2\left(\frac{r\ell\sin\theta}{2}\right)dr.
\]
Writing \(\beta=2-p\in(0,1)\), subtracting the value at \(\theta=0\), and extending the *difference* to \(r=0\) with \(O(\theta^2)\) error gives
\[
-\ell^2\left(\frac{\ell|\sin\theta|}{2}\right)^\beta
\int_0^\infty\frac{1-\operatorname{sinc}^2s}{s^{1+\beta}}\,ds
+O(\theta^2).
\]
To evaluate the integral, use the exact triangular-kernel identity
\[
\operatorname{sinc}^2 s=\int_{-1}^{1}(1-|v|)\cos(2sv)\,dv
\]
and the standard cosine Mellin integral
\[
\int_0^\infty\frac{1-\cos(as)}{s^{1+\beta}}\,ds
=\frac{\pi|a|^\beta}{2\Gamma(1+\beta)\sin(\pi\beta/2)}.
\]
Tonelli's theorem applies because \(1-\cos(as)\ge0\). It follows that
\[
\int_0^\infty\frac{1-\operatorname{sinc}^2s}{s^{1+\beta}}\,ds
=\frac{\pi2^\beta}{\Gamma(3+\beta)\sin(\pi\beta/2)}.
\]
Consequently the self-edge loss is exactly
\[
-\frac{\pi\ell^{4-p}}{\Gamma(5-p)\sin(\pi p/2)}
|\theta|^{2-p}+o(|\theta|^{2-p}).
\]
Summing the one or two self-edge terms and multiplying by \(p/A(P)\) proves the first boxed expansion. A first-order Taylor expansion of the strictly positive power \(\rho_p^p\) proves the reciprocal-radius formula.

**4. Convexity obstruction and the upper exponent range.** Suppose \(F_pP\) were convex. By Step 1 it is a convex body with the origin in its interior, so its reciprocal radial function equals the support function of its polar body: \(\rho_p(u)^{-1}=h_{(F_pP)^\circ}(u)\). Every support function of a compact convex body is Lipschitz on \(\mathbb S^1\). The positive cusp with exponent \(2-p<1\) violates this: its difference quotient divided by \(|\theta|\) diverges. This proves nonconvexity.

At \(u=n\), the boundary formula instead has the large-frequency expansion
\[
\widehat{\mathbf1_P}(rn)=\frac{i}{r}\sum_{E\in\mathcal E(n)}\sigma_E\ell_E
\exp(-ir\,n\cdot m_E)+O(r^{-2}),
\qquad\sigma_E\in\{-1,1\}.
\]
If there are two parallel edges, their support heights differ. The nonoscillatory diagonal of the squared modulus has strictly positive coefficient \(\sum\ell_E^2\), whereas the cross term has nonzero oscillation frequency. Integration by parts shows that the oscillatory term has lower growth order than the diagonal. Therefore \(\int_1^\infty|\widehat{\mathbf1_P}(rn)|^2r^{p-1}dr\) diverges at \(p=2\) logarithmically and for \(p>2\) polynomially. The first claim for \(0<p\le1\) belongs to Langharst–Manui–Zvavitch's general convexity theorem and is invoked as established literature, not proved here. \(\square\)

## Verification

The accompanying `check.py` runs high-precision independent comparisons. It checks the Fourier transform of the standard triangle against direct two-dimensional integration, evaluates the triangle's radial spectral moment through a separate simplex divided-difference formula, verifies that its edge-normal defect approaches the universal coefficient, tests an asymmetric trapezoid with unequal parallel-side lengths using a separate exact projected-vertex Fourier formula, matches the published square's independent exact coefficient, and confirms the sinc Mellin constant numerically. These checks test normalizations and a non-parallelogram case; the theorem for *all* polygons is established by the proof, not by finite sampling.

The standard-triangle calculation at \(p=3/2\) gives \(\pi/[\Gamma(7/2)\sin(3\pi/4)]\approx1.33686841313653\) for the unnormalized integral's cusp coefficient at a unit-length exposed edge; the independently evaluated divided-difference expression converges to it. For the trapezoid with vertices \((0,0),(2,0),(3/2,1),(1/2,1)\), the unnormalized coefficient at the lower edge normal is independently \(c_p(2^{4-p}+1)\), verifying additive contributions from unequal parallel edges.

## Relationship to prior work

Langharst, Manui, and Zvavitch introduce Fourier mean bodies and prove their convexity for \(0<p\le1\) in all dimensions. Their Theorem 11 and Section 7.2 establish nonconvexity for **cubes** for \(1<p<2\), via a negative-curvature calculation in the planar square. The result here is not another cube example: it identifies the exact cusp coefficient for **every** convex planar polygon, including triangles with no parallel sides, and uses a support-function regularity obstruction. It also shows the compactness endpoint \(p=2\) holds for every polygon. Related indexed results on radial mean bodies, cube resonance, and smooth quartic disks treat different operators or geometric classes; their statements do not supply the universal polygonal law.

## Limitations

The theorem concerns planar polygons, not arbitrary piecewise smooth bodies or higher-dimensional polytopes. The expression has a fixed \(p\in(1,2)\) and makes no uniform claim as \(p\) approaches an endpoint. It does not quantify global nonconvexity by Hausdorff distance. Historical priority for an unindexed equivalent remains possible. Numerical checks are supplements to the analytic proof, not an external or independent audit.

## References

1. D. Langharst, A. Manui, A. Zvavitch, *On the Fourier Mean Bodies of a Convex Body*, arXiv:2601.20117, v1 first submitted 27 January 2026; v3, 17 November 2026. https://arxiv.org/abs/2601.20117 ; https://arxiv.org/html/2601.20117v3 . In particular Definition 2, Theorems 8–11, and Section 7.2.
2. Classical divergence theorem, Riemann–Lebesgue lemma, and cosine Mellin integral; the exact uses and constants are stated and derived in the proof.
