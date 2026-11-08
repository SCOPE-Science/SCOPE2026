# Parity boundary layers for periodic linear-spline least-squares projection

## Finding
Let \(n\ge3\), and let \(P_n\) be the real \(L^2(\mathbb T)\)-orthogonal projector onto continuous, piecewise-affine, periodic functions on the uniform \(n\)-knot partition of \(\mathbb T=\mathbb R/\mathbb Z\). View it as a map \(L^\infty(\mathbb T)\to C(\mathbb T)\), and write \(\Lambda_n=\|P_n\|_{L^\infty\to L^\infty}\). Put
\[
q=2-\sqrt3,\qquad b_j^{(n)}=\frac{\sqrt3[(-q)^j+(-q)^{n-j}]}{1-(-q)^n},\quad 0\le j\le n,\quad b_n^{(n)}=b_0^{(n)}.
\]
For \(a,b\in\mathbb R\setminus\{0\}\) define
\[
J(a,b)=\begin{cases}
 (|a|+|b|)/2,&ab>0,\\
 (a^2+b^2)/(2(|a|+|b|)),&ab<0.
\end{cases}
\]
Then the following is an **exact finite-dimensional formula**, valid for every \(n\ge3\):
\[
\boxed{\Lambda_n=\sum_{j=0}^{n-1}J(b_j^{(n)},b_{j+1}^{(n)})},\qquad 1<\Lambda_n<2.
\]
All and only the knot locations are norming evaluation points. For a prescribed knot, the \(L^\infty\)-unit inputs attaining its evaluation norm are almost everywhere the sign of that knot's signed evaluation kernel (or its negative).

The finite-period loss from the sharp cardinal value \(2\) has a parity-dependent boundary layer. For integers \(m\to\infty\),
\[
\boxed{2-\Lambda_{2m}=C_{\mathrm e}q^m+O(q^{2m}),\qquad
2-\Lambda_{2m+1}=C_{\mathrm o}q^m+O(q^{2m}).}
\]
The coefficients are **explicit, strictly positive, and unequal**:
\[
\begin{aligned}
C_{\mathrm e}&=\frac{2\sqrt3(1-q)^2}{1+q}
 \sum_{j=0}^{\infty}\frac{q^j}{1+q^{2j+1}}
 =1.6830464193182701\ldots,\\
C_{\mathrm o}&=\frac{4\sqrt3}{1+q}
\left[\frac{q^2}{2}+\frac{q^2}{1-q}
-\frac{(1-q)^2}{2}\sum_{j=1}^{\infty}\frac{q^{3j}}{1-q^{2j}}\right]
=0.7011506234329134\ldots.
\end{aligned}
\]
The series converge geometrically, giving effective rigorous error bounds by comparison with geometric tails. For example, \(\Lambda_3=16/9\), \(\Lambda_4=17/9\), and \(\Lambda_5=257/132\). These finite-knot data are checks, not a substitute for the general proof.

## Assumptions and scope
The base measure is Lebesgue probability measure on the unit torus; knots are distinct and equally spaced; the spline degree is exactly one with periodic continuity. Real inputs are assumed, and operator norms use the essential-supremum input norm and supremum output norm. The domain is \(n\ge3\), excluding degenerate two-knot wraparound conventions. Normalized coordinates \(y=nt\) make every element length one; this change of scale does not change \(\Lambda_n\).

## Proof
**1. Projector kernel and exact finite formula.** In unit-element coordinates, the periodic nodal hat basis has Gram matrix \(G=(4I+S+S^{-1})/6\), where \(S\) is cyclic shift. Its row sum is one and its eigenvalues \((4+2\cos(2\pi k/n))/6\) are positive. Define the cardinal inverse-row sequence \(c_j=\sqrt3(-q)^{|j|}\), for all integers \(j\). Since \(q+q^{-1}=4\), direct substitution gives \((4c_j+c_{j-1}+c_{j+1})/6=\delta_{j0}\). Its periodization
\[
b_j^{(n)}=\sum_{\ell\in\mathbb Z}c_{j+\ell n}
=\frac{\sqrt3[(-q)^j+(-q)^{n-j}]}{1-(-q)^n}
\]
is therefore exactly the first inverse Gram row for every \(n\ge3\). The evaluation kernel at the knot \(0\) is the periodic, continuous, piecewise-linear interpolation of these values. On each unit segment its signed endpoint values are \(b_j^{(n)}\) and \(b_{j+1}^{(n)}\). Integrating the absolute value of a linear interpolant proves the two cases in \(J\), and hence the exact sum.

**2. Norming locations and strict upper bound.** For an evaluation point \(x\) inside an edge, its kernel is a convex combination of the two endpoint kernels. The \(L^1\) norm is therefore bounded by the common knot value \(\Lambda_n\). The bound is strict in the edge interior because the adjacent evaluation kernels have opposite signs on an open interval near one of their knots: the inverse Gram entries at graph distance zero and one have opposite signs. This also proves the equality statement for inputs using the equality condition in \(L^\infty\)–\(L^1\) duality. The cardinal piecewise-linear kernel \(k\) interpolating \(c_j\) is even, and direct geometric integration gives
\[
\int_{\mathbb R}|k(y)|\,dy
=\frac{\sqrt3(1+q^2)}{1-q^2}=2.
\]
Because the periodic kernel is \(k_n(y)=\sum_{\ell\in\mathbb Z}k(y+\ell n)\), the triangle inequality gives \(\Lambda_n\le2\). It is strict: the two leading translates, \(k(y)\) and \(k(y-n)\), have opposite signs on a nonempty open interval near \(n/2\). Since the projector fixes constants, \(\Lambda_n\ge1\); its kernel takes negative values, so \(\Lambda_n>1\).

**3. Reduce the exponential loss to local overlaps.** Put \(\delta_n=2-\Lambda_n\). Splitting the periodic sum into its two nearest translates and all remaining ones, the triangle inequality and \(\int_{|y|\ge n}|k(y)|\,dy=O(q^n)\) give
\[
\delta_n=\int_0^n\bigl(|k(y)|+|k(y-n)|-|k(y)+k(y-n)|\bigr)\,dy+O(q^n).
\]
Let \(T\) be the (nonperiodic) linear interpolant with \(T(j)=(-q)^j\) for every integer \(j\), including negative integers. For \(n=2m+\varepsilon\), \(\varepsilon\in\{0,1\}\), substitute \(y=m+s\) and use evenness of \(k\):
\[
\delta_n=\sqrt3 q^m\int_{-m}^{m+\varepsilon}
\left(|T(s)|+|T(\varepsilon-s)|-|T(s)+T(\varepsilon-s)|\right)\,ds+O(q^{2m}).
\]
The nonnegative integrand is bounded by \(2\min(|T(s)|,|T(\varepsilon-s)|)\), which is at most \(Cq^{|s|}\) outside a fixed compact interval. Extending the integral to all of \(\mathbb R\) changes it by \(O(q^m)\). This proves the claimed remainder order and reduces each coefficient to an explicit integral of piecewise-linear functions.

**4. Compute both overlap coefficients.** Write \(a=q/(1+q)\), \(b=1/(1+q)\). On \(s=j+u\), \(0\le u\le1\), the two relevant nodal interpolants are
\[
T(j+u)=(-q)^j(1-(1+q)u),\quad
T(-j-u)=(-q)^{-j}(1-(1+q^{-1})u).
\]
For \(\varepsilon=0\), and \(j\ge0\), they have opposite signs precisely on \((a,b)\). Their smaller absolute value has triangular integral
\[
\int_a^b\min\big(q^j[1-(1+q)u],q^{-j}[(1+q^{-1})u-1]\big)du
=\frac{(1-q)^2 q^j}{2(1+q)(1+q^{2j+1})}.
\]
Using reflection symmetry and \(|u|+|v|-|u+v|=2\min(|u|,|v|)\) when \(uv<0\), and zero otherwise, yields \(C_{\mathrm e}\) above.

For \(\varepsilon=1\), reflect about \(s=1/2\). On \([1/2,1]\), the contributing integral of the smaller absolute value is \(q^2/[2(1+q)]\). For each \(j\ge1\), on \([j,j+1]\), opposing signs occur on \(u\in[0,a)\) and \(u\in(b,1]\). Integrating their smaller magnitudes gives
\[
\frac{q^{j+1}}{1+q}-\frac{(1-q)^2q^{3j}}{2(1+q)(1-q^{2j})}.
\]
Summing and multiplying by \(4\sqrt3\) gives \(C_{\mathrm o}\). Both integrals are positive. To compare constants explicitly, truncating each positive geometrically convergent series after 12 terms and using \(q\in(0.2679491924311227,0.2679491924311228)\) yields, with strict rational interval bounds, \(1.6830<C_{\mathrm e}<1.6831\) and \(0.7011<C_{\mathrm o}<0.7012\). Thus the parity coefficients differ, and the theorem is proved.

## Verification
Run `python3 checks/check_periodic_projection.py` using the Python standard library. It independently inverts rational Gram matrices and integrates the resulting kernels for \(3\le n\le21\), compares the exact results with the geometric closed form, and checks the leading coefficients by a second integral construction. Exact finite checks do not replace the proof of the asymptotic statements.

## Relationship to prior work
Passenbrunner's 2011 result establishes a monotonicity theorem and a limiting constant \(2\) for equally spaced **interval** splines, with boundary knots; it does not identify periodic even/odd finite-period corrections. Passenbrunner's 2016 periodic-spline analysis establishes uniform boundedness and almost-everywhere convergence for arbitrary knots and orders, rather than the sharp uniform linear-spline norm and its parity-resolved exponentially small defect. Antonopoulos and Dougalis (2021) derive stability estimates via cyclic Gram inverses and note that the order-two inverse entries are explicitly computable; their stability bounds do not state the two overlap coefficients here. General graph projector methods can supply finite-knot formulas for even cycles, so the substantive additional assertion is the **exact parity-resolved boundary-layer law** and norming-location result, not mere existence of an inverse Gram formula.

## Limitations
No result is asserted for nonuniform knots, degree greater than one, higher-dimensional simplicial splines, or variation of the ambient input/output \(L^p\) exponents. The result does not assert monotonicity of \(\Lambda_n\) in \(n\). The decimal coefficients are approximations of the explicitly defined convergent series. The argument is analytical; finite checker tests are supporting consistency evidence. Potential equivalent uncatalogued spline-projection formulas remain a literature risk. Independent mathematical validation has not been performed.

## References
1. M. Passenbrunner, *Monotonicity of the Lebesgue constant for equally spaced knots*, arXiv:1103.1949v1, publicly submitted 2011-03-10. https://arxiv.org/abs/1103.1949
2. M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, arXiv:1608.06720v1, publicly submitted 2016-08-24. https://arxiv.org/abs/1608.06720
3. D. C. Antonopoulos and V. A. Dougalis, *On the stability of the \(L^2\) projection and the quasiinterpolant in the space of smooth periodic splines*, arXiv:2106.09060v1, publicly submitted 2021-06-16. https://arxiv.org/abs/2106.09060
