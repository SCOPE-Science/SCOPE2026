# Exact algebraic-boundary degrees for intersection bodies of cross-polytopes

## Finding
Let \(n\ge4\), let \(B_1^n=\{y\in\mathbb R^n:\sum_{i=1}^n|y_i|\le1\}\), and let its intersection body \(I B_1^n\) have radial function \(\rho(u)=\operatorname{Vol}_{n-1}(B_1^n\cap u^\perp)\) for every Euclidean unit vector \(u\). Its real algebraic boundary has **exactly \(2^n\) pairwise distinct, absolutely irreducible hypersurface components**, each of exact polynomial degree \(\binom n2\). Consequently the union has degree \(2^n\binom n2\), and none of its components is linear.

There is an explicit equation for each component. Put \(m=\binom n2\), \(c_n=2^{n-1}/(n-1)!\), and define
\[
D_n(a)=\prod_{1\le i<j\le n}(a_i+a_j),\qquad
\Delta_n(a)=\prod_{1\le i<j\le n}(a_i-a_j),
\]
\[
P_n(a)=\frac{1}{\Delta_n(a)}\sum_{i=1}^n(-1)^{i-1}a_i^{2n-3}
\prod_{\substack{1\le k<l\le n\\k,l\ne i}}(a_k^2-a_l^2).
\]
The quotient defining \(P_n\) is a polynomial with integer coefficients, homogeneous of degree \(m-1\). For each sign vector \(\varepsilon\in\{-1,1\}^n\), define the polynomial
\[
F_\varepsilon(x)=D_n(\varepsilon_1x_1,\ldots,\varepsilon_nx_n)-c_n P_n(\varepsilon_1x_1,\ldots,\varepsilon_nx_n).
\]
The algebraic boundary is exactly the union of their zero varieties. Each \(F_\varepsilon\) is absolutely irreducible, and no two are associated.

In particular, in dimension four the homogeneous polynomials are \(D_4=\prod_{i<j}(a_i+a_j)\) and \(P_4=e_2(a)e_3(a)-e_1(a)e_4(a)\), where \(e_j\) denotes the \(j\)-th elementary symmetric polynomial. The four-dimensional cross-polytope therefore has precisely **16 distinct sextic components**. The dimension-three specialization agrees with the eight cubic branches obtained from \(P_3=e_2\) but is not claimed as new here.

## Assumptions and scope
All volumes are intrinsic Euclidean Hausdorff volumes, and all polynomials are in standard Cartesian coordinates. The algebraic boundary is the real Zariski closure of the *topological* boundary, not the topological boundary itself. The polynomial equations may thus have additional real points outside the actual intersection body. Distinctness and irreducibility are asserted even over \(\mathbb C\); no claim is made about the number of connected real patches of the full zero varieties. On open coordinate orthants, where all \(a_i=|u_i|>0\), the radial formula used below extends continuously through repeated coordinates and coordinate hyperplanes.

## Proof
**1. Central-section density.** Let \(X_1,\ldots,X_n\) be independent standard Laplace variables, each with density \(e^{-|t|}/2\), and put \(S=\sum_i u_iX_i\). For a Euclidean unit vector \(u\), the coarea identity and positive homogeneity of \(\|y\|_1\) give
\[
 f_S(0)=2^{-n}\int_{u^\perp}e^{-\|y\|_1}\,d\mathcal H^{n-1}(y)
 =\frac{(n-1)!}{2^n}\operatorname{Vol}_{n-1}(B_1^n\cap u^\perp).
\]
Fourier inversion with \(a_i=|u_i|\) gives
\[
f_S(0)=\frac1{2\pi}\int_{\mathbb R}\prod_{i=1}^n\frac{dt}{1+a_i^2t^2}.
\]
For distinct positive \(a_i\), partial fractions and \(\int_{\mathbb R}(1+a_i^2t^2)^{-1}dt=\pi/a_i\) yield
\[
\rho(u)=c_n\sum_{i=1}^n\frac{a_i^{2n-3}}{\prod_{j\ne i}(a_i^2-a_j^2)}
 =c_n\frac{P_n(a)}{D_n(a)}.
\]
The formula on positive directions extends by continuity. The last equality follows after bringing the rational sum over the common denominator \(\prod_{i<j}(a_i^2-a_j^2)=\Delta_n(a)D_n(a)\).

**2. Polynomiality and exact reduced denominator.** The numerator of the fraction over \(\Delta_nD_n\) is alternating in the \(a_i\), so it is divisible in \(\mathbb Z[a_1,\ldots,a_n]\) by the Vandermonde \(\Delta_n\). This proves that \(P_n\) is a polynomial of degree \(m-1\). To show it shares no factor with \(D_n\), consider any factor \(a_i+a_j\) and choose generic complex values with \(a_j\to-a_i\ne0\), all remaining squared parameters distinct and different from \(a_i^2\). In the partial-fraction sum, the \(i,j\) terms together have nonzero principal part
\[
\frac{a_i^{2n-4}}{(a_i+a_j)\prod_{k\ne i,j}(a_i^2-a_k^2)},
\]
while every other term stays finite. Thus \(P_n/D_n\) has a genuine pole along each \(a_i+a_j=0\), proving \(\gcd(P_n,D_n)=1\) over \(\mathbb C\).

**3. Irreducibility.** As \(\deg D_n=m\) and \(\deg P_n=m-1\), homogenizing \(D_n-c_nP_n\) in a new variable \(z\) gives \(D_n(a)-c_nzP_n(a)\). This is a primitive polynomial of degree one in \(z\) over \(\mathbb C[a_1,\ldots,a_n]\). It is irreducible by Gauss's lemma because \(P_n,D_n\) are coprime. Dehomogenizing at \(z=1\) preserves irreducibility (a nontrivial factorization would homogenize). Signed coordinate substitutions preserve absolute irreducibility. The degree of every \(F_\varepsilon\) is exactly \(m\).

**4. Geometry and distinctness.** Every boundary ray with all coordinate signs \(\varepsilon_i\) meets the boundary at \(x=\rho(u)u\). By homogeneity of \(P_n,D_n\), the equality \(\rho(u)=c_nP_n(|u|)/D_n(|u|)\) is equivalent to \(F_\varepsilon(x)=0\). The graph of positive radial distance over an open spherical orthant contains a relatively open smooth real hypersurface patch. It is Zariski dense in the irreducible variety \(F_\varepsilon=0\), and the finitely many orthants cover a dense part of the topological boundary. Thus the algebraic closure is exactly the union of these component varieties.

If \(\varepsilon'\ne\pm\varepsilon\), the top-degree forms \(D_n(\varepsilon x)\) and \(D_n(\varepsilon' x)\) have different linear-factor sets: some pair \((i,j)\) has a different sign product \(\varepsilon_i\varepsilon_j\). If \(\varepsilon'=-\varepsilon\), the top-degree form changes by \((-1)^m\) but the lower homogeneous term changes by \((-1)^{m-1}\); because neither term vanishes identically they cannot be proportional. Hence the \(2^n\) irreducible equations are all nonassociated, proving the count and degrees.

## Verification
A standalone Python checker `verify.py` separately constructs hyperplane-section vertices from intersections with the cross-polytope edges and computes their intrinsic convex-hull volumes; these are compared with the Laplace/partial-fraction formula at randomly sampled distinct positive normal coordinates for dimensions \(2\) through \(5\). It also evaluates the exact Vandermonde divisibility, polynomial degree, coprimality, and rational identities for dimensions \(2\) through \(4\). The actual run reported 250 successful assertions. These finite computations are consistency checks only; the all-dimensional irreducibility and component count follow from the analytic proof above.

## Relationship to prior work
Berlow, Brandenburg, Meroni and Shankar established semialgebraicity and general degree bounds for algebraic boundaries of intersection bodies of polytopes and explicitly studied cubes. In their centered symmetric-polytope bound, a generic section with \(n(n-1)\) vertices gives an upper bound of \(\binom n2\); the present calculation proves that this bound is **exact in every cross-polytope orthant**, with no denominator cancellation, and proves pairwise distinctness across all orthants. Their methods do not by themselves state this exact cross-polytope family classification. Brandenburg and Meroni subsequently studied translated bodies and convexity, rather than these exact degrees. Brazitikos and Pandis use the same established Laplace–Fourier section integral while studying **extremal restricted section volumes**, not algebraic irreducibility or component degrees. Thus neither the Fourier representation nor the general semialgebraic framework is claimed as novel.

## Limitations
The result addresses the centered standard cross-polytope and its intersection body, not arbitrary centrally symmetric polytopes, noncentral sections or translated cross-polytopes. It classifies the algebraic variety, not detailed topology of the real patches. The originality comparison covers the primary accessible literature and specified related indexed records, but unindexed equivalent computations remain possible. Independent validation has not been performed.

## References
1. K. Berlow, M.-C. Brandenburg, C. Meroni and I. Shankar, *Intersection Bodies of Polytopes*, arXiv:2110.05996, first publicly posted 2021-10-12; Beiträge zur Algebra und Geometrie 63 (2022), 419–439. https://arxiv.org/abs/2110.05996 ; https://doi.org/10.1007/s13366-022-00621-7.
2. M.-C. Brandenburg and C. Meroni, *Intersection bodies of polytopes: translations and convexity*, Journal of Algebraic Combinatorics 60 (2024), 127–143. https://doi.org/10.1007/s10801-024-01328-9.
3. S. Brazitikos and C. Pandis, *Restricted Hyperplane Sections of the Cross-Polytope and the Simplex*, arXiv:2606.07163 (2026), especially the Laplace Fourier identity and Section 5. https://arxiv.org/abs/2606.07163.
