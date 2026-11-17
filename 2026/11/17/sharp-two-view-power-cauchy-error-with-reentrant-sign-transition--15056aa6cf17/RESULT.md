# Sharp two-view power-Cauchy error with reentrant sign transitions

## Finding
For every real exponent \(p\ge2\), put
\[
c_p=\frac{\Gamma((p+1)/2)}{\sqrt\pi\,\Gamma(1+p/2)},\qquad
\mathfrak D_p(\mu)=\max_{\theta\in\mathbb R/\pi\mathbb Z}
\left|\sum_{j=1}^{m}w_j|\cos(\theta-\phi_j)|^p-c_p\right|.
\]
Among all normalized positive rules \(\mu\) supported on at most two unoriented planar directions, the sharp discrepancy is
\[
\boxed{\inf_\mu\mathfrak D_p(\mu)
=\max\left\{\frac12-c_p,\ c_p-2^{-p/2}\right\}.}
\]
For every \(p\ge2\), the minimizing rule is unique modulo common rotation, reversal of direction representatives and exchange of nodes: two mutually perpendicular axes, each of weight \(1/2\). For this rule, the worst discrepancy is *positive* at the coordinate axes for \(2<p<4\), *negative* at the bisectors for \(4<p<6\), and positive again for \(p>6\). The two signs tie exactly at \(p=4\) and \(p=6\); the rule is exact at \(p=2\). Thus the optimizing directions remain fixed while the worst-error polarity switches twice.

The corresponding sharp **perimeter-normalized planar convex-body brightness error** is exactly one half of the displayed value (definition below). The phase transition holds for the continuum of all real \(p\ge2\), not just even integers.

## Assumptions and scope
Let \(K\subset\mathbb R^2\) be a compact full-dimensional convex body, \(S_K\) its surface-area measure, and \(P(K)>0\) its perimeter. For a unit vector \(u\), define the power-Cauchy brightness observable
\[
B_pK(u)=\frac12\int_{S^1}|u\cdot v|^p\,dS_K(v).
\]
The exact normalized circular average is \(c_pP(K)/2\). A positive rule with one or two unoriented directions is \(\mu=\sum_{j=1}^m w_j\delta_{u_j}\), where \(1\le m\le2\), \(w_j>0\), and \(\sum_jw_j=1\). The error on convex bodies is
\[
\mathcal E_p(\mu)=\sup_{K\text{ full-dimensional}}
\frac{\left|\sum_jw_jB_pK(u_j)-c_pP(K)/2\right|}{P(K)}.
\]
An even continuous potential and increasingly thin rectangles show that \(\mathcal E_p(\mu)=\mathfrak D_p(\mu)/2\). This reduction also follows from the sharp defect theorem of An (2026), and is not a newly claimed identity. The theorem optimizes \(\mathcal E_p\) over fixed calibrated, positive rules supported on at most two projective directions.

## Proof
**1. The two unavoidable directional errors.** Write a two-node rule with weights \(w,1-w\), directions \(\phi_1,\phi_2\) in the projective circle \(\mathbb R/\pi\mathbb Z\), and potential \(F(\theta)=w|\cos(\theta-\phi_1)|^p+(1-w)|\cos(\theta-\phi_2)|^p\). Evaluating at either node gives
\[
\max_\theta F(\theta)\ge\max(w,1-w)\ge\frac12.
\]
The two nodes divide the projective circle of circumference \(\pi\) into two gaps. One gap has length \(L\ge\pi/2\). Its midpoint has projective angular distance \(L/2\ge\pi/4\) to *both* nodes, hence
\[
\min_\theta F(\theta)\le \cos^p(L/2)\le2^{-p/2}.
\]
Since \(c_p\le1/2\) for \(p\ge2\), and \(c_p\ge2^{-p/2}\) by Jensen applied to the mean of two orthogonal components, the signs are consistent and
\[
\mathfrak D_p(\mu)\ge
\max\left\{\frac12-c_p,\ c_p-2^{-p/2}\right\}.
\]
A one-node rule is included by taking a coincident two-node representation, for which the first inequality is strict.

**2. Sharpness and uniqueness.** For the equally weighted orthogonal rule,
\[
F_0(\theta)=\frac12\bigl(|\cos\theta|^p+|\sin\theta|^p\bigr).
\]
Set \(q=p/2\ge1\) and \(x=\cos^2\theta\). Then \(F_0=(x^q+(1-x)^q)/2\). Convexity of \(x^q\), or the elementary power-mean inequality, yields
\[
\min F_0=2^{-q},\qquad \max F_0=1/2.
\]
Thus the universal lower bound is attained. Suppose the two projective nodes are not perpendicular. Their larger gap has \(L>\pi/2\), so \(\min F<2^{-q}\), strictly losing whenever the negative error sets the bound. Also \(\max F>1/2\): at a heaviest node the value is at least \(\max(w,1-w)\), strictly above \(1/2\) if weights are unequal, and above \(1/2\) through the positive other-node contribution if equal. This strictly loses whenever the positive error sets the bound. If the nodes are perpendicular but weights are unequal, \(\max F\ge\max(w,1-w)>1/2\), so they cannot optimize in a positive-error-dominated regime. In a negative-error-dominated regime the derivative of \(F\) at the angular bisector is nonzero for unequal weights, giving \(\min F<2^{-q}\). At ties either argument applies. Therefore equality requires perpendicular axes and weights exactly \(1/2\). This also covers \(p=2\), when the sharp error is zero.

**3. Exact reentrant sign diagram.** Let \(X=\cos^2\Theta\), with \(\Theta\) uniform modulo \(\pi\). Then \(X\) has the arcsine distribution \(\operatorname{Beta}(1/2,1/2)\) and \(c_p=\mathbb E[X^q]\). Introduce the three-point Lobatto functional
\[
Q(g)=\frac14g(0)+\frac12g(1/2)+\frac14g(1).
\]
It agrees with the arcsine expectation on every polynomial of degree at most three, since the first four moments of \(X\) are \(1,1/2,3/8,5/16\). Direct calculation gives
\[
2\left(\mathbb E[X^q]-Q(x^q)\right)
=2c_p-\frac12-2^{-q}.
\]
For \(g_\varepsilon(x)=(x+\varepsilon)^q\), the cubic Hermite interpolation polynomial matching values at \(0,1/2,1\) and the first derivative at \(1/2\) has remainder
\[
g_\varepsilon(x)-H_\varepsilon(x)
=\frac{g_\varepsilon^{(4)}(\xi_x)}{4!}
\,x(x-1)(x-1/2)^2.
\]
The polynomial factor is nonpositive on \([0,1]\), and
\[
g_\varepsilon^{(4)}(x)=q(q-1)(q-2)(q-3)(x+\varepsilon)^{q-4}.
\]
Because \(Q\) is supported on interpolation nodes, \(Q(g_\varepsilon-H_\varepsilon)=0\), whereas the arcsine expectation of the remainder has strict sign opposite that of the displayed product except at polynomial exponents. Letting \(\varepsilon\downarrow0\) preserves the non-strict sign by continuity. Strictness for noninteger \(q\notin\{1,2,3\}\) follows from the generalized Hermite remainder applied directly on every compact subinterval of \((0,1)\): the fourth derivative has constant nonzero sign there. Therefore
\[
2c_p-\frac12-2^{-p/2}\begin{cases}
<0,&2<p<4,\\
>0,&4<p<6,\\
<0,&p>6,
\end{cases}
\]
with zeros exactly at \(p=2,4,6\). This is precisely the difference between the magnitudes of negative and positive deviations for the optimal rule, proving the asserted two polarity reversals.

**4. Convex-body interpretation.** Interchanging surface-area integration and the directional rule gives
\[
\sum_jw_jB_pK(u_j)-\frac{c_pP(K)}2
=\frac12\int_{S^1}(F(v)-c_p)\,dS_K(v).
\]
Thus \(\mathcal E_p(\mu)\le\frac12\mathfrak D_p(\mu)\). If \(v_0\) maximizes the absolute potential discrepancy, choose long thin rectangles with long-edge outer normals \(\pm v_0\). Their normalized surface-area measures converge to \((\delta_{v_0}+\delta_{-v_0})/2\), and the integrand is even. Hence the upper bound is the supremum, proving the stated factor \(1/2\) and completing the geometric claim.

## Verification
Run `python verify.py` with Python 3 and no third-party packages. It independently compares the gamma normalization with numerical angular integration, reconstructs the exact orthogonal potential extrema for fourteen different exponents, checks the polarity on both sides of both transitions, and tests the two universal geometric lower-bound witnesses across 2,400 pseudorandom positive two-node rules. In the preparation of this result the checker reported 7,264 successful numerical comparisons. These finite tests are checks, not a substitute for the all-exponent proof above.

## Relationship to prior work
C. An, *Exact Finite Integral Geometry: Directional Kernels and Spherical Designs* (arXiv:2609.05869v1, first public 2026-09-05), establishes the universal norm reduction, spectral exactness criterion and the unique exact quadratic rule in its Theorem 5.2. We credit those results and do not claim novelty at \(p=2\). Its full text does not optimize two-view error at \(p>2\), nor classify the \(p=4,6\) error-polarity switches.

The earlier published finding *Sharp positive two-direction quadrature for subquadratic cosine brightness* (2026) treats \(0<p<2\), with the orthogonal rule as optimizer; that exponent range is disjoint from the strict superquadratic range proved here. Another earlier result, *Sharp positive \(N\)-direction Cauchy quadrature and angular rigidity*, treats the Cauchy exponent \(p=1\) and all positive node counts. The current new claim is the complete \(p>2\) two-view minimax formula, its rigidity and the twice-reentrant sign classification; none follows from a theorem establishing only exactness at \(p=2\) or impossibility of exactness for non-even exponents.

## Limitations
The rule is positive, normalized, calibrated, nonadaptive and supported on at most two unoriented planar directions. Signed rules, more nodes, nonplanar bodies, additional kernel classes and the \(0<p<2\) result are outside the new theorem. The supremum over planar convex bodies need not be attained by a full-dimensional body; thin rectangles approach it. The short elementary proof does not itself establish global historical priority, and relevant unindexed sources may exist.

## References
1. C. An, *Exact Finite Integral Geometry: Directional Kernels and Spherical Designs*, arXiv:2609.05869v1 (2026-09-05), especially Theorems 3.2, 4.3 and 5.2. https://arxiv.org/abs/2609.05869
2. *Sharp positive two-direction quadrature for subquadratic cosine brightness* (2026), pre-existing published mathematical result, subquadratic case \(0<p<2\). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-positive-two-direction-quadrature-for-subquadratic-cosine--35c0341352f2
3. *Sharp positive \(N\)-direction Cauchy quadrature and angular rigidity* (2026), classical Cauchy case \(p=1\). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-positive-n-direction-cauchy-quadrature-and-angular-rigidit--33b1062b46ae
4. C. An, *Gauss--Chebyshev Quadrature, \(\mathbb S^1\)-Designs, and the Planar Minkowski Inverse Problem*, arXiv:2610.11814v1 (2026-10-08), on related circle quadrature and inverse Minkowski geometry. https://arxiv.org/abs/2610.11814
