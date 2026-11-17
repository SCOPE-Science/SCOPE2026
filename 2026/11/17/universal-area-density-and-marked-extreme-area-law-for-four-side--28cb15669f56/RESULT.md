# Universal area density and marked extreme-area law for four-side random quadrilaterals

## Finding
Let \(Q\) be any nondegenerate Euclidean parallelogram of area \(A\). Choose one point independently and uniformly in arclength on each of its four sides, and join these points in cyclic side order. Write \(T\) for the new quadrilateral's area divided by \(A\). For every \(0<t<1\) with \(t\ne1/2\), put \(z=|2t-1|\). Then \(T\) has the **complete, shape-independent** probability density
\[
f_T(t)=-4(1+z)\log z-8(1-z).
\]
It is symmetric about \(1/2\), supported on \([0,1]\), and has a logarithmic singularity
\[
f_T(t)=-4\log|2t-1|-8+o(1)\qquad(t\to1/2).
\]
For \(1/2<t<1\), its survival function is exactly
\[
\mathbb P(T>t)=\frac12+2z-\frac52 z^2+(2z+z^2)\log z,\qquad z=2t-1,
\]
and the survival function below \(1/2\) follows by symmetry. For every integer \(m\ge0\),
\[
\mathbb E\big[(T-1/2)^{2m}\big]=\frac{4}{4^m(2m+1)^2(2m+2)^2};
\]
all odd centered moments vanish. In particular, \(\mathbb ET=1/2\) and \(\operatorname{Var}(T)=1/144\).

The upper and lower rare-area tails have the same **sharp two-term expansion**:
\[
\mathbb P(T>1-\varepsilon)=\mathbb P(T<\varepsilon)
=\frac43\varepsilon^4+\frac{32}{15}\varepsilon^5+O(\varepsilon^6)
\qquad(\varepsilon\downarrow0).
\]
There is also a marked conditional limit for the *four edge-position errors*. Conditional on \(T>1-\varepsilon\), with asymptotic probability \(1/2\) the four sampled points tend respectively to the corners \((1,0),(1,1),(0,1),(0,0)\) of the unit square; with asymptotic probability \(1/2\) they tend respectively to \((0,0),(1,0),(1,1),(0,1)\). These are the two opposite cyclic corner patterns described more precisely below. After recording the appropriate four nonnegative endpoint errors \(d_i\), the five-component vector
\[
\left(\frac{d_1}{2\varepsilon},\ldots,\frac{d_4}{2\varepsilon},
1-\frac{1-T}{\varepsilon}\right)
\]
converges in distribution, independently of the two equally likely corner labels, to \(\operatorname{Dirichlet}(1,1,1,1,1)\). In particular, all four endpoint errors and the unused area budget have asymptotic mean fraction \(1/5\) on the \(2\varepsilon\) scale. The limit does not depend on parallelogram side lengths or angle.

## Assumptions and scope
The vertices are sampled independently and uniformly with respect to arclength on their *specified* sides; this is stratified four-side sampling, not four independent draws from the whole perimeter or interior. An affine map preserves these four uniform side parameters and divides both polygon areas by the same determinant. Thus it suffices to work in the unit square. Put the four sampled points in cyclic order at
\[
P_1=(U,0),\quad P_2=(1,V),\quad P_3=(W,1),\quad P_4=(0,Z),
\]
where \(U,V,W,Z\) are mutually independent \(\operatorname{Uniform}(0,1)\). The resulting quadrilateral is strictly convex almost surely, and its normalized area lies in \((0,1)\) almost surely.

For the upper tail define the corner label \(\sigma=+\) if \(U-W>0\) and \(V-Z>0\), and \(\sigma=-\) if both differences are negative. For \(\sigma=+\) the four endpoint errors are \((d_1,d_2,d_3,d_4)=(1-U,W,1-V,Z)\); for \(\sigma=-\) they are \((U,1-W,V,1-Z)\). When \(0<\varepsilon<1/2\), the event \(T>1-\varepsilon\) implies exactly one of these two labels. The fifth component in the displayed marked limit is nonnegative on this conditioning event.

## Proof
**Affine identity.** The shoelace formula in the square gives the exact identity
\[
T=\frac12\big[1+(U-W)(V-Z)\big].
\]
The two differences \(X=U-W\) and \(Y=V-Z\) are independent, each with the triangular probability density \(g(x)=1-|x|\) on \((-1,1)\). This proves affine universality, symmetry about \(1/2\), and strict positivity of \(T\) and \(1-T\) almost surely.

**Entire density and moments.** Set \(B=XY\). The product density for \(0<b<1\) is
\[
\begin{aligned}
f_B(b)&=2\int_b^1(1-x)(1-b/x)\frac{dx}{x}\\
&=-2(1+b)\log b-4(1-b).
\end{aligned}
\]
Reflection gives \(f_B(-b)=f_B(b)\). Since \(T=(1+B)/2\), the density transformation gives the asserted \(f_T\). Elementary integration of \(f_B\) from \(b\) to \(1\) yields the stated upper survival formula, including the symmetry rule for the lower half. In particular its only unbounded density point is \(t=1/2\), where the logarithmic term has the stated coefficient. Independence also yields, for every \(m\ge0\),
\[
\mathbb E X^{2m}=2\int_0^1 x^{2m}(1-x)\,dx
=\frac{2}{(2m+1)(2m+2)},
\]
so \(\mathbb E[(T-1/2)^{2m}]=4^{-m}(\mathbb EX^{2m})^2\). Symmetry makes odd moments zero.

**Sharp endpoint probabilities.** Substitute \(z=1-2\varepsilon\) into the exact survival formula. Taylor's formula for \(\log(1-2\varepsilon)\), with a bounded remainder on \(0\le\varepsilon\le\varepsilon_0<1/2\), gives
\[
\mathbb P(T>1-\varepsilon)=\frac43\varepsilon^4
+\frac{32}{15}\varepsilon^5+O(\varepsilon^6).
\]
Symmetry gives the lower endpoint. The fourth-power exponent is not inferred from a finite simulation: it follows from the exact distribution, and is geometrically explained by four simultaneous endpoint deficits.

**Conditional five-dimensional simplex law.** On \(T>1-\varepsilon\), necessarily \(|X|,|Y|>1-2\varepsilon\), with \(X,Y\) of the same sign. For either sign, the four errors in the assumptions are nonnegative and at most \(2\varepsilon\). Put \(a=d_1+d_2\), \(b=d_3+d_4\). The exact event and deficit are
\[
2(1-T)=a+b-ab<2\varepsilon.
\]
After writing \(x_i=d_i/(2\varepsilon)\), the admissible region is
\[
\mathcal R_\varepsilon=
\{x_i\ge0: \sum_{i=1}^4x_i-2\varepsilon(x_1+x_2)(x_3+x_4)<1\},
\]
within \(0\le x_i\le1\). The joint density of the original four edge parameters is exactly constant. As \(\varepsilon\downarrow0\), the indicator of \(\mathcal R_\varepsilon\) converges almost everywhere to the indicator of the standard four-simplex \(\mathcal R_0=\{x_i\ge0:\sum_i x_i<1\}\). All regions are contained in \([0,1]^4\), so dominated convergence proves convergence of the corresponding *normalized* uniform measures. Appending the coordinate \(1-\sum_i x_i\) gives the uniform Dirichlet distribution on the five-part simplex; the actual appended coordinate is \(1-\sum_i x_i+2\varepsilon(x_1+x_2)(x_3+x_4)\), which differs uniformly by at most \(2\varepsilon\). By reflection \((U,V,W,Z)\mapsto(1-U,1-V,1-W,1-Z)\), the two signs have *exactly equal conditional probabilities* for every \(0<\varepsilon<1/2\), and the same conditional mark law. This proves joint convergence and asymptotic independence. Equivalently, the two corner regions each contribute \((2\varepsilon)^4/4!+o(\varepsilon^4)\) in the original probability cube; their sum recovers the leading \(4\varepsilon^4/3\) coefficient. QED.

## Verification
The accompanying self-contained `verify.py` checks the shoelace identity against independently generated four-point configurations, compares the exact survival probabilities at nine thresholds to a 420,000-sample direct Monte Carlo experiment, tests the central variance, integrates the independent triangular-product density numerically at three nonsingular points, and checks the endpoint coefficient at four decreasing thresholds. Its separate rare-event check samples 850,000 quadruples of independent endpoint defects uniformly from a shrinking box, conditions directly on the exact nonlinear area deficit, and tests all five limiting Dirichlet means (35,709 accepted cases with the fixed seed). It prints `FOUR_SIDE_QUADRILATERAL_AREA_LAW_OK` if all comparisons pass. These finite numerical checks corroborate but do not prove the distribution, endpoint asymptotics, or weak limit; the analytic arguments above supply those proofs.

## Relationship to prior work
Nguyen and Volkov (first public 2015) define the same four-independent-edge-points operation for general polygons, but their main theorems concern iterated subdivision, shape collapse, and random-matrix Lyapunov behavior. They do not derive the full single-step area density or its conditional endpoint mark law. Volkov's 2011 work addresses a different quadrilateral midpoint-subdivision process and independent side-point sampling in triangles. The later exact second-moment recurrence for random quadrilateral subdivision recovers the already-known one-step variance \(1/144\) in the parallelogram case; this low moment is *not* claimed as a separate discovery. Existing perimeter-uniform random polygon results sample a random number of points on each edge and therefore describe a different law. The elementary mean-half-area formula and midpoint Varignon identity are likewise prior knowledge. The claim here is the **entire affine-universal one-step law and its marked extreme geometry**, not the existence of the sampling model, the area mean, or the variance by itself.

## Limitations
The result applies to one independent uniform point on each of four sides of a *parallelogram*, with affine area normalization. It does not assert the same area distribution for non-parallelogram quadrilaterals, nonuniform side choices, multi-step subdivisions, or separately perimeter-uniform points. The Dirichlet claim is a weak conditional limit, not an exact Dirichlet identity at finite \(\varepsilon\). The numerical checker is not an independent proof or audit. A published complete formula in historical probability-puzzle collections or an unindexed paper may still affect priority; independent external validation has not occurred.

## References
1. T.-M. Nguyen and S. Volkov, *A universal result for consecutive random subdivision of polygons*, arXiv:1506.04942, first public 2015-06-16. https://arxiv.org/abs/1506.04942
2. S. Volkov, *Random geometric subdivisions*, arXiv:1112.0932, first public 2011-12-05. https://arxiv.org/abs/1112.0932
3. *Exact second-moment spectrum and intermittency in random quadrilateral subdivision*, published research record, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-second-moment-spectrum-and-intermittency-in-random-quadril--6188c52bc8e5
4. *Four random points on sides of square are connected to form a quadrilateral: mean and variance of area*, mathematics discussion, first public 2016-12-04, https://math.stackexchange.com/questions/2044074
