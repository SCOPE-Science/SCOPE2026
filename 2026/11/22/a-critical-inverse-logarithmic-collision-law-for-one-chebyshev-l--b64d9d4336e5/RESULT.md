# A critical inverse-logarithmic collision law for one Chebyshev–Lobatto node

## Finding

For every integer \(n\ge3\), write \(x_{j,n}=\cos(j\pi/n)\), \(0\le j\le n\). Choose integers \(m_n\) satisfying \(1\le m_n\le n-2\) and \(m_n/n\to a\in(0,1)\). Replace exactly \(x_{m_n,n}\) by
\[
y_n=\cos((m_n+1-\varepsilon_n)\pi/n),
\qquad 0<\varepsilon_n<1,
\qquad\varepsilon_n\longrightarrow0,
\]
leaving every other Chebyshev–Lobatto node fixed. Let \(\Lambda_n\) be the uniform operator norm of degree-at-most-\(n\) interpolation from \(C([-1,1])\) to itself at these \(n+1\) distinct nodes. Put \(c_n=\varepsilon_n\log n\).

**Sharp crossover.** For \(c\in(0,\infty]\), put \(b_c=1+1/c\), with \(1/\infty=0\). Let \(s_c\in(0,1/2)\) be the unique solution of
\[
\pi(s_c^2+b_cs_c)\cos(\pi s_c)=b_c\sin(\pi s_c).
\]
Whenever \(c_n\to c\in(0,\infty]\),
\[
\boxed{\displaystyle
\lim_{n\to\infty}\frac{\Lambda_n}{\log n}
=K(c):=\frac{2}{\pi}\sin(\pi s_c)\left(1+\frac{b_c}{s_c}\right).}
\tag{1}
\]
The universal constant and scalar optimizer are independent of the bulk index ratio \(a\). Every exact maximizer \(z_n^*\in[-1,1]\) of the Lebesgue function, expressed as \(z_n^*=\cos\theta_n^*\), satisfies
\[
\frac{n\theta_n^*}{\pi}-m_n\longrightarrow-s_c,
\]
and the explicit points \(\cos((m_n-s_c)\pi/n)\) asymptotically attain (1).

At the other side of the transition, whenever \(c_n\to0\),
\[
\boxed{\displaystyle\lim_{n\to\infty}\varepsilon_n\Lambda_n=2.}\tag{2}
\]
Thus \(\varepsilon_n\log n\asymp1\) is the exact transition scale between logarithmic interpolation stability and collision-dominated amplification for this one-node family; indeed, for all sufficiently large \(n\), uniformly over \(0<\varepsilon_n<1/2\), \(\Lambda_n\asymp\log n+\varepsilon_n^{-1}\), where the implied constants may depend on \(a\).

The transition is already visible in the more informative **local profile**: if \(c_n\to c\in(0,\infty]\), then, uniformly for \(u\) in any fixed bounded interval,
\[
\frac{\lambda_n\bigl(\cos((m_n+u)\pi/n)\bigr)}{\log n}
\longrightarrow
\frac{2}{\pi}\left|\frac{\sin(\pi u)}{u}\right|
\left(|u-1|+\frac1c\right),
\tag{3}
\]
where the quotient at zero has its continuous value \(\pi\). In particular \(K(1)=4.143338556577\ldots\), while \(K(\infty)=2.251670218254\ldots\); these exceed the unperturbed coefficient \(2/\pi\).

## Assumptions and scope

The norm is the real or complex scalar sup-norm interpolation-operator norm on continuous functions over the **entire** interval \([-1,1]\), not an evaluation norm at a selected point. Node ordering is by increasing angular index; replacing the index \(m_n\) by a point a fraction \(\varepsilon_n\) of one mesh interval before the *following* angular node is the only perturbation. All limits are taken with the bulk-location condition and \(\varepsilon_n\downarrow0\) in the sense \(\varepsilon_n\to0\), without monotonicity. Equation (1) does not assert a uniform-in-\(c\) remainder as \(c\downarrow0\), and (2) does not assert a limiting maximizing offset. Natural logarithms are used. The sharpness of the bounded asymptotic follows from explicit evaluation points and maximum localization.

## Proof

**A. Exact cardinal replacement.** For clarity suppress \(n\), set \(m=m_n\), \(\delta=1-\varepsilon_n\), \(y=\cos((m+\delta)\pi/n)\), and write \(L_j\) for the ordinary Chebyshev–Lobatto Lagrange cardinal of degree \(n\). Let \(\widetilde L_j\) denote the new cardinals. The exact polynomial identities are
\[
\widetilde L_m(z)=\frac{L_m(z)}{L_m(y)},\quad
\widetilde L_j(z)=L_j(z)-\frac{L_j(y)}{L_m(y)}L_m(z)
\qquad(j\ne m).
\tag{4}
\]
Equivalently, by comparing nodal products, for \(j\ne m\),
\[
\widetilde L_j(z)=L_j(z)
\frac{z-y}{z-x_m}\frac{x_j-x_m}{x_j-y},
\tag{5}
\]
with removable singularities interpreted continuously. These identities are valid for every \(n\), not asymptotic approximations.

**B. Intact-grid estimates and collision size.** For \(z=\cos\theta\), the ordinary cardinal is
\[
L_j(\cos\theta)=
\frac{-(-1)^j\sin\theta\sin(n\theta)}
{n d_j[\cos\theta-\cos(j\pi/n)]},
\qquad d_j=\begin{cases}2,&j=0,n,\\1,&1\le j\le n-1.\end{cases}
\tag{6}
\]
The nodal values are interpreted by continuity. The classical uniform Lebesgue estimate is \(\max_z\sum_j|L_j(z)|=(2/\pi)\log n+O(1)\). Since \(m/n\to a\in(0,1)\), (6) gives
\[
L_m(y)=\varepsilon_n(1+o(1)),\qquad
L_{m+1}(y)=1+O(\varepsilon_n),\qquad
\sum_{j\notin\{m,m+1\}}|L_j(y)|=O_a(\varepsilon_n\log n).
\tag{7}
\]
The last bound follows directly by splitting at \(|j-m-1|\le\eta n\) for fixed small \(\eta>0\): the cardinal for each \(j\notin\{m,m+1\}\) is bounded by \(C_a\varepsilon_n/(1+|j-m-1|)\) in that range, and by \(C_a\varepsilon_n/n\) outside; summing gives the harmonic factor. For the uniform order estimate when \(0<\varepsilon_n<1/2\), (6) gives \(L_m(y)\asymp_a \sin(\pi\varepsilon_n)/(1-\varepsilon_n)\asymp\varepsilon_n\) and \(|L_{m+1}(y)|\le C_a\sin(\pi\varepsilon_n)/\varepsilon_n\le C_a\), all uniformly for sufficiently large \(n\). Formula (6) also implies the global bulk-cardinal bound
\[
|L_m(\cos\theta)|\le\frac{C_a}{1+|u|},
\qquad u=\frac{n\theta}{\pi}-m,
\tag{8}
\]
and the compact-offset estimate \(L_m(\cos((m+u)\pi/n))=[\sin(\pi u)/(\pi u)](1+O_{R,a}(n^{-1}))\) for \(|u|\le R\), with continuous values at integers. In fact the factor multiplying the sinc is \(\sin((m+u)\pi/n)\) divided by the average of the sine over the angular interval from \(m\pi/n\) to \((m+u)\pi/n\), which stays bounded away from zero for bounded \(u\) and bulk \(m\).

**C. Exact local profile.** Fix \(R>0\) and set \(z_n(u)=\cos((m+u)\pi/n)\) for \(|u|\le R\). For the two distinguished indices, (4), (7), and the compact-offset convergence give, uniformly over this interval,
\[
|\widetilde L_m(z_n(u))|+|\widetilde L_{m+1}(z_n(u))|
=\frac{2}{\varepsilon_n}\left|\frac{\sin(\pi u)}{\pi u}\right|(1+o(1))+O_R(1),
\tag{9}
\]
where the \(o(1)\) may be chosen uniform for the bounded offsets. To control the remaining indices, write \(j=m+r\), \(r\notin\{0,1\}\), and combine (5) and (6). For any fixed \(M>2(R+3)\), in the range \(M<|r|\le\eta n\), Taylor expansion of cosine differences around the bulk node yields
\[
|\widetilde L_{m+r}(z_n(u))|
=\frac{|\sin(\pi u)|}{\pi|u|}\,|u-\delta|
\left(\frac1{|r|}+O_R\left(\frac1{r^2}+\frac1n\right)\right).
\tag{10}
\]
The formula and its error are uniform for \(|u|\le R\) and \(0<\varepsilon_n<1/2\), including the removable value \(u=0\). Explicitly, the pre-expanded rational factor is \(|r|/(|u-r|\,|r-\delta|)\); its difference from \(1/|r|\) is \(O_R(r^{-2})\). Each of the finitely many remaining \(|r|\le M\), excluding \(0,1\), contributes \(O_R(1)\) uniformly because its node stays a full mesh interval from \(y\); the distant region \(|r|>\eta n\) also contributes \(O_R(1)\) in total by (5)–(6). Both signs of \(r\) contribute \(\log n+O(1)\) to the harmonic sum. Consequently
\[
\sum_{j\notin\{m,m+1\}}|\widetilde L_j(z_n(u))|
=\frac2\pi\left|\frac{\sin(\pi u)}u\right|\,|u-\delta|\log n+O_{R,a}(1),
\tag{11}
\]
where the estimate is uniform for \(\varepsilon_n\to0\). If \(c_n\to c>0\), divide (9)–(11) by \(\log n\), use \(\delta\to1\), and obtain (3). This also applies to \(c=\infty\), when the distinguished pair's contribution to the normalized limit vanishes.

**D. All global maxima localize.** By (4), the triangle inequality, and (7), for every \(z=\cos\theta\),
\[
\lambda_n(z)\le \lambda_n^{(0)}(z)
+\frac{|L_m(z)|}{|L_m(y)|}\left(1+\sum_{j\ne m}|L_j(y)|\right)
\le \frac2\pi\log n+O_a(1)
+C_a\frac{\varepsilon_n^{-1}+\log n}{1+|u|}.
\tag{12}
\]
If \(c_n\to c\in(0,\infty]\), then for any \(R\ge1\),
\[
\limsup_{n\to\infty}\sup_{|u|\ge R}\frac{\lambda_n(z_n(u))}{\log n}
\le\frac2\pi+\frac{C_{a,c}}R.
\tag{13}
\]
The local profile at \(u=-1/2\) is strictly greater than \(2/\pi\), so \(R\) can be chosen once and for all such that all exact maximizers have \(|u|<R\) for sufficiently large \(n\). The compact-uniform convergence (3) therefore reduces the global operator norm and every maximizer's limits to the global maximum of the scalar profile.

**E. Unique scalar maximum.** Multiply (3) by \(\pi/2\) and put \(b=1+1/c\ge1\). On negative offsets \(u=-s\), \(s>0\), the profile becomes \(|\sin(\pi s)|(1+b/s)\). Its value at \(s=1/2\) is \(1+2b\), exceeding all values at \(s\ge1\), which are at most \(1+b\). For \(1/2<s<1\), reflecting \(s\) to \(1-s\) strictly increases the expression. For positive \(u\in(0,1)\), the value \(\sin(\pi u)(b-u)/u\) is strictly less than the negative-offset value at \(-u\). For \(u\ge1\), it is at most \(\max\{1,b-1\}<1+2b\). The continuous value at \(u=0\) equals \(\pi b\), below the maximum on the negative axis, because the latter has positive right derivative at the origin. Finally, on \(0<s<1/2\),
\[
h_b(s)=\sin(\pi s)+b\frac{\sin(\pi s)}s
\]
is strictly concave: both terms have negative second derivatives, with \(\sin(\pi s)/s=\pi\int_0^1\cos(\pi st)\,dt\). It has \(h_b'(0+)=\pi>0\) and \(h_b'(1/2)=-4b<0\). Thus there is exactly one maximizer \(s_c\in(0,1/2)\), whose first-order condition is the displayed equation. Equations (1), the witness, and convergence of every maximizing offset follow from compact localization and uniqueness.

**F. Collision regime.** When \(c_n=\varepsilon_n\log n\to0\), multiply the first, *exact* inequality of (12) by \(\varepsilon_n\) and use \(\sup_z|L_m(z)|=1+o(1)\), which follows from the compact-offset sinc limit and the exterior bound (8), to obtain \(\limsup\varepsilon_n\Lambda_n\le2\). At the *removed* original grid point \(z=x_m\), (4) gives exactly
\[
\lambda_n(x_m)=\frac{1+\sum_{j\ne m}|L_j(y)|}{|L_m(y)|}.
\tag{14}
\]
Using (7) and \(c_n\to0\) yields \(\varepsilon_n\lambda_n(x_m)\to2\), giving the matching lower bound and (2). For the uniform order estimate, the uniform bounds in B give (12) without requiring \(\varepsilon_n\to0\), hence \(\Lambda_n=O_a(\log n+1/\varepsilon_n)\). At \(u=-1/2\), (11) gives a uniform lower bound of order \(\log n\) since \(\delta>1/2\), and (14) and \(|L_m(y)|\le C_a\varepsilon_n\) give a uniform lower bound of order \(1/\varepsilon_n\). Their maximum is at least a constant times their sum.

## Verification

The accompanying standalone standard-library `checker.py` evaluates finite-degree Chebyshev cardinal polynomials directly from (6). It independently compares the two exact displaced-cardinal formulas (4) and (5), checks the partition of unity, verifies uniqueness of the proposed scalar optimizers against a fine real mesh, and tests finite-degree asymptotic witnesses without mistaking them for infinite proofs. Run `python3 checker.py` in the same directory. The observed output is `NEAR_COLLISION_CHEB_DIAGNOSTIC_OK 4563` (4,563 assertions). The limiting claims, sharpness, and uniqueness are established by the analytic argument, not by the finite checks.

## Relationship to prior work

Wu [1] provides perturbation stability criteria for Chebyshev–Lobatto interpolation and an obstruction from near-colliding nodes, but does not determine the inverse-logarithmic **collision separation** crossover for a single moved node or the limiting maximizers. [2] gives a complete logarithmic coefficient for moving one bulk node by a **fixed** angular mesh fraction \(0<\tau<1\) and explicitly excludes fractions depending on \(n\) and the approach to collision \(\tau\to1\). Its limiting fixed-fraction coefficients do not justify exchanging limits in (1)–(2): the extra \(1/c\) arises from two nearly singular cardinal functions, invisible at fixed \(\tau\). [3] deletes a node and simultaneously decreases interpolation degree; its linear growth law is therefore a distinct problem, not a stronger formulation of the present full-degree collision. The standard barycentric formulas [4] underlie the exact identities but do not constitute the limiting calculation.

## Limitations

The theorem treats exactly one bulk node tending toward its immediate neighbor and excludes simultaneous or arbitrary perturbations. The critical and supercritical logarithmic limits require the specified limits of \(c_n\), and no rate of convergence is asserted. The coefficient is defined through a unique scalar critical point rather than elementary radicals. The uniqueness statement concerns asymptotic *maximizing locations*, not a claim that a finite-degree Lebesgue function has a unique maximizer. Publication priority is assessed against the specified accessible sources and search records, not an exhaustive mathematical bibliography. No formal verification or expert attestation is claimed.

## References

1. H.-N. Wu, *When do perturbed Chebyshev–Lobatto points remain Chebyshev?*, arXiv:2606.23409, first publicly posted 2026-06-22. https://arxiv.org/abs/2606.23409
2. *Sharp logarithmic amplification from one displaced Chebyshev–Lobatto node*, published record dated 2026-11-17. https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-sharp-logarithmic-amplification-from-one-displaced-chebyshev-lob--c68d83ac7ece
3. *Single-erasure boundary layers for Chebyshev–Lobatto interpolation*, published record dated 2026-10-18. https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-single-erasure-boundary-layers-for-chebyshev-lobatto-interpolati--a3c5beff381f
4. J.-P. Berrut and L. N. Trefethen, *Barycentric Lagrange interpolation*, SIAM Review 46 (2004), 501–517. https://doi.org/10.1137/S0036144502417715
