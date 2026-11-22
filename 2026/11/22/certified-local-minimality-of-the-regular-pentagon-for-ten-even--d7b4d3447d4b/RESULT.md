# Certified local minimality of the regular pentagon for ten even distance energies

## Finding

Let \(P\subset\mathbb R^2\) be a nondegenerate convex pentagon and, for an even integer \(k\ge6\), set

\[
\Phi_k(P)=\operatorname{area}(P)^{-(k+4)/2}
\int_P\int_P \lVert x-y\rVert^k\,dx\,dy.
\]

**Theorem.** For every \(k\in\{6,8,10,12,14,16,18,20,22,24\}\), the regular pentagon is a strict local minimizer of \(\Phi_k\) among convex pentagons, modulo Euclidean similarities. More precisely, after fixing two labeled adjacent vertices to their regular positions, the six-dimensional transverse Hessian is positive definite. Every pivot in an exact-integer outward-enclosure \(LDL^{\mathsf T}\) calculation of the normalized Hessian \(B_m/E_m\), with \(m=k/2\), is greater than \(1/5\).

## Assumptions and scope

Vertices are counterclockwise labeled, distinct, and form a convex pentagon sufficiently close to a regular one. The functional is unchanged by translations, rotations, reflections and positive uniform scalings. Fixing the first two vertices provides a smooth local chart for the six remaining degrees of freedom modulo orientation-preserving similarities.

For the proof use coordinates \((X,Y)\), with the true Euclidean point \((X,sY)\), where \(s=\sin(2\pi/5)>0\) and \(\lambda=s^2=(5+\sqrt5)/8\). Put \(c=(\sqrt5-1)/4\), \(d=-(\sqrt5+1)/4\), \(q=(\sqrt5-1)/2\). The regular vertices in these coordinates, taken cyclically, are

\[
v_0=(1,0),\quad v_1=(c,1),\quad v_2=(d,q),\quad v_3=(d,-q),\quad v_4=(c,-1).
\]

The six variables are the two coordinates of each of \(v_2,v_3,v_4\), with \(v_0,v_1\) fixed. The origin remains in the polygon for small perturbations, so it decomposes into the five oriented triangles \((0,v_i,v_{i+1})\), with indices cyclic modulo five.

## Proof

**1. Exact polynomial moments.** Write \(M_{p,r}=\int_{\widetilde P}X^pY^r\,dX\,dY\) in the scaled-coordinate polygon. For all integers \(p,r\ge0\), the elementary simplex-beta integral yields

\[
M_{p,r}=\sum_{i=0}^{4}\det(v_i,v_{i+1})
\sum_{a=0}^{p}\sum_{b=0}^{r}
\binom pa\binom rb\frac{(a+b)!(p+r-a-b)!}{(p+r+2)!}
X_i^aY_i^b X_{i+1}^{p-a}Y_{i+1}^{r-b}.
\]

This identity holds for every sufficiently close convex perturbation, not just the regular polygon. Define \(A=M_{0,0}>0\). For each integer \(m\ge3\), expand the squared Euclidean distance and obtain the *exact polynomial* double integral

\[
E_m=\sum_{j=0}^{m}\binom mj\lambda^{m-j}
\sum_{a=0}^{2j}\sum_{b=0}^{2(m-j)}
(-1)^{a+b}\binom{2j}a\binom{2(m-j)}b
M_{2j-a,\,2(m-j)-b}M_{a,b}.
\]

Thus \(\Phi_{2m}=s^{-m}E_m/A^{m+2}\). All derivatives needed below are derivatives of explicit finite polynomials, with coefficients in \(\mathbb Q(\sqrt5)\).

**2. Stationarity and the transverse Hessian.** At a regular pentagon, dihedral invariance forces each vertex component of the gradient of the similarity-invariant functional to be radial and equal under cyclic rotation. Its common radial coefficient vanishes by scale invariance, proving full first-order stationarity. Equivalently \(E_m'=(m+2)(E_m/A)A'\) at the regular configuration.

Put \(c_m=m+2\), and use primes for derivatives in the six free vertex coordinates. At stationarity,

\[
D^2\Phi_{2m}=s^{-m}A^{-c_m}B_m,\qquad
B_m=E_m''-c_m\frac{E_m}{A}A''
-c_m(c_m-1)\frac{E_m}{A^2}A'A'^{\mathsf T}.
\]

Since \(s,A,E_m>0\), the Hessian is positive definite exactly when the real symmetric \(6\times6\) matrix \(B_m/E_m\) is positive definite.

**3. Validated positive pivots.** The accompanying stand-alone `pentagon_interval.py` implements the moment formula, its derivatives through order two (by a 28-coefficient jet) and an interval \(LDL^{\mathsf T}\) elimination for each \(m=3,4,\ldots,12\). Every interval endpoint is a signed integer representing a multiple of \(10^{-40}\); all arithmetic is outward rounded using integer floor and ceiling. An enclosure of \(\sqrt5\) is constructed by the integer square root of \(5\cdot 10^{80}\). No floating-point arithmetic contributes to any positivity decision.

The supplied `certificate_results.txt` records all ten minimal pivot lower bounds. The smallest across the cases occurs at \(m=3\), and is strictly greater than \(0.21549\). The checker additionally asserts that **each** pivot lower endpoint exceeds exactly \(1/5\) (a rational comparison performed with integers). Division is only by intervals certified to exclude zero. The Hessian entries, their interval widths, and the elimination are recomputed from scratch by the complete source code. The stationarity residual is contained in narrow intervals around zero; exact stationarity was independently proved above by symmetry.

Consequently \(B_m/E_m\) and the six-dimensional transverse Hessian are strictly positive for each listed exponent. The Taylor expansion of the smooth finite-dimensional functional yields strict local minimality on the chart. Every nearby convex pentagon has a unique representative there up to an orientation-preserving similarity, proving the theorem.

## Verification

Run `python pentagon_interval.py` with standard Python; the program asserts all ten positive-definiteness certificates and terminates with the `CERTIFIED` line. The included `certificate_results.txt` is the captured output. Its lowest *integer lower bound* is `2154909090615892595078279210699395506949` at denominator \(10^{40}\), greater than \(1/5\).

A separate `pentagon_quadrature.py` uses NumPy and 14-point Gauss–Legendre quadrature per triangular coordinate to evaluate the double moments independently; a tensor polynomial rule is exact in real arithmetic for the relevant polynomial integrands, up to floating-point summation. For the two endpoint exponents, its agreement is better than \(3\times10^{-15}\) relative. This numerical agreement is supplementary: the rigorous positivity certificate depends only on integer intervals and the analytic moment identities. Reproduction logs are included as `independent_quadrature_results.txt`.

## Relationship to prior work

Bogosel, Bucur and Fragalà (2023, arXiv:2302.11677v1), Section 3.1 and the Appendix, explicitly compute **numerical** vertex Hessians for the same area-normalized distance-power energies with \(N=5,\ldots,10\) and even \(k\le24\), reporting four zero similarity modes and positive transverse modes. Their numerical observation, objects, parameters, and computational approach are essential prior work and are not claimed as new. The distinct claim here is a rigorous, independently reproducible *outward-integer-interval* proof of the full ten-exponent local-minimality statement for pentagons. The numerical observations alone do not supply a certified positive-eigenvalue argument.

Bonacini, Cristoferi and Topaloglu (2021/2022) prove polygonal Riesz inequalities for triangles and quadrilaterals with decreasing interaction kernels, rather than the positive-power pentagonal local problem. Bogosel and Bucur (2024) prove a local polygonal Faber–Krahn assertion for the first Dirichlet eigenvalue, a different shape functional. Historical mathematical priority is subject to independently finding any earlier rigorous equivalent certificate.

## Limitations

Only the local convex five-vertex problem and the ten listed even powers are established. Neither global minimality nor the range of all real powers is asserted; nothing is inferred for arbitrary polygons with more sides. The proof relies on a small exact-integer arithmetic checker whose implemented operations and moment derivation are provided for independent inspection. The same-source prior numerical experiments are acknowledged, and an independent mathematical audit remains unperformed.

## References

1. B. Bogosel, D. Bucur and I. Fragalà, *The nonlocal isoperimetric problem for polygons: Hardy–Littlewood and Riesz inequalities*, arXiv:2302.11677v1, first posted 2023-02-22. https://arxiv.org/html/2302.11677v1 . Relevant: §3.1 (reported numerical Hessians), §3.3 (quadrature), §9.3 (vertex Hessian).
2. M. Bonacini, R. Cristoferi and I. Topaloglu, *Riesz-type Inequalities and Overdetermined Problems for Triangles and Quadrilaterals*, arXiv:2103.06657v3. https://arxiv.org/html/2103.06657v3 .
3. B. Bogosel and D. Bucur, *Polygonal Faber-Krahn inequality: Local minimality via validated computing*, arXiv:2406.11575, first posted 2024-06-17. https://arxiv.org/abs/2406.11575 .
