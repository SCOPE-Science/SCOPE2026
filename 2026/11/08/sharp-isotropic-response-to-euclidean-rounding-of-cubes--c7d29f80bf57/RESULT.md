# Sharp isotropic response to Euclidean rounding of cubes

## Finding
Let \(C_d=[-1,1]^d\), let \(B_d\) be the Euclidean unit ball, and let \(d\ge2\) be an integer. For \(t\ge0\), set \(K_d(t)=C_d+tB_d\). Define the affine-invariant squared isotropic constant by
\[
L(K)^2=\frac{\bigl(\det\operatorname{Cov}(X_K)\bigr)^{1/d}}{\operatorname{vol}_d(K)^{2/d}},
\]
where \(X_K\) is uniform in a full-dimensional \(d\)-body \(K\).

**All-dimensional onset.** For every fixed integer \(d\ge2\),
\[
L(K_d(t))^2=\frac1{12}-\frac{(d-1)(4-\pi)}{48}t^2+O_d(t^3)\qquad(t\downarrow0).
\]
In particular, the first derivative at the unrounded cube vanishes and the second right derivative is strictly negative. Extending to the signed Euclidean parallel-body family by taking \(K_d(t)=C_d\mathbin{\sim}(-t)B_d\) when \(-1<t<0\) (where \(\sim\) denotes Minkowski erosion), the function \(t\mapsto L(K_d(t))^2\) is constant at \(1/12\) on \((-1,0]\), is once differentiable at \(0\), and is not twice differentiable there.

**Complete three-dimensional profile.** For \(d=3\), define
\[
\begin{aligned}
V(t)&=8+24t+6\pi t^2+\frac{4\pi}{3}t^3,\\
S(t)&=8+40t+(24+14\pi)t^2+(40+4\pi)t^3+6\pi t^4+\frac{4\pi}{5}t^5.
\end{aligned}
\]
Then for every \(t\ge0\),
\[
\boxed{L(K_3(t))^2=\frac{S(t)}{3V(t)^{5/3}}.}
\]
This function is **strictly decreasing** for every \(t>0\), with its unique maximum on \([0,\infty)\) at \(t=0\) and no attained minimum. Its endpoint values are
\[
L(K_3(0))^2=\frac1{12},\qquad
\lim_{t\to\infty}L(K_3(t))^2=\frac1{5(4\pi/3)^{2/3}}.
\]
Thus the signed three-dimensional profile is flat for inner rounding and strictly decreasing for every positive outer rounding radius.

## Assumptions and scope
All volumes, moments and covariance matrices use standard Euclidean Lebesgue measure and coordinates. The cube has half-edge length one, so the parameter is dimensionless. Every \(t\ge0\) is included, not only infinitesimal rounding; the negative-parameter statement concerns only \(-1<t<0\) where the eroded cube has positive volume. The all-dimensional formula is a fixed-dimension asymptotic as \(t\downarrow0\), not a uniform-in-dimension estimate. The all-radius strict monotonicity is proved only in dimension three.

## Proof
**1. A partition for exact polynomial moments.** Up to sets of measure zero, every point of \(K_d(t)\) lies in a unique stratum where exactly \(k\) of its absolute coordinates exceed one, with \(0\le k\le d\). For a fixed set of \(k\) such coordinates, their excesses \(u_i=|x_i|-1\) lie in the positive orthant of the \(k\)-ball of radius \(t\), while the remaining coordinates range independently over \([-1,1]\). There are \(\binom dk\) choices and \(2^k\) signs. Thus with \(\kappa_k=\pi^{k/2}/\Gamma(k/2+1)\),
\[
\operatorname{vol}_d(K_d(t))=\sum_{k=0}^d\binom dk2^{d-k}\kappa_k t^k.
\]
For any nonnegative integer multi-index \((m_1,\ldots,m_k)\), the exact positive-orthant moment is
\[
\int_{u_i\ge0,\,\sum_i u_i^2\le t^2}\prod_i u_i^{m_i}\,du
=\frac{t^{k+\sum_i m_i}}{2^k}
\frac{\prod_i\Gamma((m_i+1)/2)}{\Gamma(1+(k+\sum_i m_i)/2)}.
\]
It follows directly by the substitution \(z_i=u_i^2\) and the Dirichlet simplex integral. On each stratum the quadratic integrand is the sum of the \(d-k\) inside squares, whose mean is \((d-k)/3\), and the \(k\) outside squares \((1+u_i)^2\). This determines the full unnormalized radial second moment
\(S_d(t)=\int_{K_d(t)}\|x\|_2^2dx\) and its coefficients exactly.

**2. Universal quadratic term.** The first three volume coefficients, divided by \(2^d\), are
\[
1,\quad d,\quad \frac{\pi d(d-1)}8.
\]
The first three coefficients of \(S_d(t)\), divided by \(d2^d/3\), are
\[
1,\quad d+2,\quad 3+\frac{\pi(d+4)(d-1)}8.
\]
Indeed the linear part comes from the \(2d\) faces; at quadratic order the linearly rising face-square term and the codimension-two quarter-disks both contribute. Sign permutations and coordinate permutations force \(\operatorname{Cov}(X_{K_d(t)})=\bigl(S_d(t)/(dV_d(t))\bigr)I_d\). Therefore
\[
L(K_d(t))^2=\frac{S_d(t)}{dV_d(t)^{1+2/d}}.
\]
Expanding the denominator via the binomial theorem, the linear coefficient cancels identically. The coefficient of \(t^2\), relative to its constant value \(1/12\), equals \((d-1)(\pi-4)/4\). This proves the asserted \(-(d-1)(4-\pi)/48\) coefficient, strictly negative since \(\pi<4\).

For \(-1<t<0\), the erosion satisfies \(C_d\mathbin{\sim}(-t)B_d=[-1-t,1+t]^d\): a centered ball fits exactly when each coordinate is at least its radius from the corresponding coordinate facet. Positive homotheties preserve \(L\). Hence \(L^2\) is identically \(1/12\) for \(-1<t\le0\), while the right second derivative at zero is \(-(d-1)(4-\pi)/24\). Both one-sided first derivatives vanish, but the second derivatives do not agree.

**3. Full three-dimensional moment calculation.** The same stratification separates the interior cube, six face regions, twelve edge regions, and eight corner regions. Their volumes are respectively
\[
8,\qquad24t,\qquad6\pi t^2,\qquad\frac{4\pi}3t^3.
\]
Integrating \(\|x\|^2\) on these regions gives respectively
\[
\begin{aligned}
&8,\\
&40t+24t^2+8t^3,\\
&14\pi t^2+32t^3+3\pi t^4,\\
&4\pi t^3+3\pi t^4+\frac{4\pi}5t^5.
\end{aligned}
\]
For example the edge integral is over a quarter-disk in the two excess coordinates and an independent coordinate in \([-1,1]\); the corner integral is over an octant of a three-ball. The orthant formula in Step 1 evaluates both without approximation. Summation gives exactly \(V(t)\) and \(S(t)\) in the finding.

**4. Strict monotonicity, including every radius.** Differentiation yields the exact identity
\[
5V'(t)S(t)-3V(t)S'(t)=8t\sum_{j=0}^4c_jt^j,
\]
where
\[
\begin{aligned}
c_0&=24(4-\pi), & c_1&=8(19\pi-54),\\
c_2&=-480+32\pi+42\pi^2,&c_3&=24\pi(\pi-3),\\
c_4&=\pi(16-5\pi).&&
\end{aligned}
\]
All five coefficients are strictly positive. For \(c_0,c_3,c_4\), use \(3<\pi<22/7<16/5<4\); for \(c_1,c_2\), use \(\pi>31/10\) and the fact that their expressions increase with positive \(\pi\). In particular, \(c_2>-480+32(31/10)+42(31/10)^2>0\). Consequently
\[
\frac{d}{dt}L(K_3(t))^2
=-\frac{5V'(t)S(t)-3V(t)S'(t)}{9V(t)^{8/3}}<0\quad(t>0).
\]
At \(t=0\) the expression is \(1/12\). The leading terms as \(t\to\infty\) are \(V(t)\sim(4\pi/3)t^3\) and \(S(t)\sim(4\pi/5)t^5\), yielding the displayed ball limit. Strict decrease precludes any attained minimum at a finite nonnegative radius.

## Verification
The accompanying standalone program `check.py` reconstructs the exact moments from the multivariate Dirichlet integral rather than from the displayed volume and moment polynomials. It checks the polynomial identity for the derivative certificate, verifies the five strict coefficient inequalities using rational enclosures of \(\pi\), independently verifies the universal symbolic quadratic coefficient in \(d\), and compares exact formulas to deterministic numerical integration on three positive radii. Run it with `python check.py` in an environment with SymPy, NumPy and SciPy; the exact symbolic checks still execute if the numerical packages are unavailable. A finite numerical test is not used to infer positivity for all radii: that claim follows from the explicit five positive coefficients.

## Relationship to prior work
Richter and Saorín Gómez study the monotonicity of the isoperimetric quotient and other quermassintegral quotients along inner and outer parallel bodies. These quantities depend on mixed volumes, whereas the squared isotropic constant depends on the full interior covariance and its determinant; their theorems do not supply the stated derivative sign. Kipp studies isotropic constants and structural restrictions on maximizers, including centrally symmetric and zonotopal cases, but does not derive the Euclidean-ball rounding profile. A sharp range result for Hanner polytopes concerns finite polytope sums and products; the bodies \(C_d+tB_d\) with \(t>0\) have spherical curved patches and are not covered by that Hanner classification. The result here is an exact, dimension-sensitive covariance statement for a particular smooth deformation. These comparisons do not establish unconditional historical priority.

## Limitations
The strict global inequality is established for the three-cube only; higher-dimensional all-radius monotonicity is not proved. The universal quadratic term is for each fixed dimension and does not imply a uniform joint limit in dimension and radius. No assertion is made for arbitrary convex bodies, arbitrary gauges or non-Euclidean roundings. The numerical integration and symbolic checker are corroborating aids, not independent mathematical certification. Earlier formulations using mechanical inertia terminology could exist despite the cited searches.

## References
- Christian Richter and Eugenia Saorín Gómez, *On the monotonicity of the isoperimetric quotient for parallel bodies*, arXiv:2003.14182, first public version 2020-03-31; Journal of Geometric Analysis 32 (2022), article 15. https://arxiv.org/abs/2003.14182
- Christian Kipp, *Isotropic constants and platonic solids*, arXiv:2407.01353, first public version 2024-07-01. https://arxiv.org/abs/2407.01353
- Christian Kipp, *Shadow Systems, Decomposability and Isotropic Constants*, Discrete & Computational Geometry 76 (2026), DOI 10.1007/s00454-026-00829-7. https://doi.org/10.1007/s00454-026-00829-7
