# Exact Mahler products of cactus symmetric edge polytopes and a cycle-parity asymptotic

## Finding

For every finite connected simple cactus graph \(G=(V,E)\) on \(N\ge2\) vertices, write
\[
H_V=\{x\in\mathbb R^V:\sum_{v\in V}x_v=0\},\qquad
P_G=\operatorname{conv}\{\pm(e_u-e_v):\{u,v\}\in E\}\subset H_V.
\]
The polar \(P_G^\circ\) and both volumes use the Euclidean inner product and \((N-1)\)-dimensional Hausdorff volume within \(H_V\). Set
\[
\mathcal R(G)=\frac{(N-1)!}{4^{N-1}}\operatorname{vol}_{N-1}(P_G)\operatorname{vol}_{N-1}(P_G^\circ).
\]
A cactus has each of its 2-connected blocks equal to a single edge or a simple cycle. If its cycle blocks have lengths \(n_1,\ldots,n_r\ge3\), counted with multiplicity, then
\[
\boxed{\mathcal R(G)=\prod_{i=1}^r\rho_{n_i},\qquad
\rho_n=\frac{n\binom{n-1}{\lfloor(n-1)/2\rfloor}}{2^{n-1}(n-1)!}
\sum_{j=0}^{\lfloor n/2\rfloor}(-1)^j\binom nj\left(\frac n2-j\right)^{n-1}.}
\]
The empty product for trees is \(1\). Every factor is rational. The first values are
\[
\rho_3=\frac98,\quad \rho_4=1,\quad \rho_5=\frac{575}{512},\quad
\rho_6=\frac{33}{32},\quad \rho_7=\frac{41209}{36864},\quad
\rho_8=\frac{151}{144}.
\]
Moreover the explicit **parity-resolved second-order profile** is
\[
\boxed{\rho_n=\frac{2\sqrt3}{\pi}\begin{cases}
1-\dfrac{2}{5n}+O(n^{-2}),& n\ \mathrm{even},\\[2mm]
1+\dfrac{1}{10n}+O(n^{-2}),& n\ \mathrm{odd},
\end{cases}\qquad n\to\infty.}
\]
The error bounds are absolute along their respective parity subsequences. In particular long even cycles approach the universal limit from below and long odd cycles from above; the statement does not claim global monotonicity in cycle length.

## Assumptions and scope

A cactus is connected, simple, and has each edge in at most one simple cycle; its block decomposition is consequently by edges and simple cycles. Each cyclic block contributes one factor even when several blocks meet at articulation vertices. The graph may have bridges and arbitrarily many block intersections, but is unweighted. Only origin-symmetric Mahler products are addressed; no universal extremality claim among all convex bodies or all graphs is made. The normalized ratio is affine invariant under coordinate changes on \(H_V\).

## Proof

**1. Multiplicativity under articulation.** Suppose connected graphs \(G_1,G_2\) share exactly one vertex and no edges. Their incidence-root spans form a direct sum of vector spaces inside \(H_V\): a vector supported on the vertices of each graph and having sum zero on that support belongs to a complementary subspace. Under this (not necessarily orthogonal) linear identification, \(P_{G_1\cup G_2}\) is the free sum \(\operatorname{conv}((P_{G_1},0),(0,P_{G_2}))\). If \(K\) and \(L\) are origin-symmetric full-dimensional convex bodies of dimensions \(a\) and \(b\), then the free sum has volume
\[
\operatorname{vol}_{a+b}(K\oplus_1 L)
=\frac{a!b!}{(a+b)!}\operatorname{vol}_a(K)\operatorname{vol}_b(L).
\]
For example, this follows by integrating the radial gauge of one factor over slices of the other: each fiber at \(x\in K\) is \((1-\|x\|_K)L\), and the layer-cake integral is \(\int_K(1-\|x\|_K)^b\,dx=\operatorname{vol}(K)a!b!/(a+b)!\). The polar of the free sum is the Cartesian product \(K^\circ\times L^\circ\). Hence
\[
\mathcal R(K\oplus_1L)=\mathcal R(K)\mathcal R(L),
\]
with normalizations \(a!/4^a\), \(b!/4^b\), and \((a+b)!/4^{a+b}\). An edge block corresponds to an interval and has \(\mathcal R=1\). Induction on the block-cut tree reduces the assertion to simple cycles.

**2. Cycle polar as a diagonal cube section.** Fix \(n\ge3\), label the cycle vertices cyclically, and let \(a_i=e_i-e_{i+1}\) with \(e_{n+1}=e_1\). Then \(\sum_i a_i=0\) and every proper subset of \(n-1\) edge roots is linearly independent in the \((n-1)\)-space \(H_n\). The operator
\[
T:H_n\to H_n,\qquad T(x)=(\langle x,a_i\rangle)_{i=1}^n
\]
is invertible, since its eigenvalues on the nonconstant Fourier modes are \(1-\exp(2\pi i j/n)\), for \(1\le j<n\). Thus \(|\det(T)|=n\). The polar is exactly
\[
P_{C_n}^\circ=T^{-1}(Z_n),\qquad Z_n=[-1,1]^n\cap H_n,
\]
so \(\operatorname{vol}_{n-1}(P_{C_n}^\circ)=\operatorname{vol}_{n-1}(Z_n)/n\).

Let \(f_n\) be the density of the sum of \(n\) independent uniforms on \([0,1]\). A coarea calculation with normal vector \((1,\ldots,1)\) gives
\[
\operatorname{vol}_{n-1}(Z_n)=2^{n-1}\sqrt n\,f_n(n/2),
\quad
f_n(n/2)=\frac1{(n-1)!}\sum_{j=0}^{\lfloor n/2\rfloor}(-1)^j\binom nj(\tfrac n2-j)^{n-1}.
\]
The second identity follows from the inclusion-exclusion density of a sum of \(n\) uniforms (the Irwin–Hall law). In particular,
\[
\operatorname{vol}_{n-1}(P_{C_n}^\circ)=\frac{2^{n-1}}{\sqrt n}f_n(n/2).
\]

**3. Cycle primal volume.** Each vertex of \(Z_n\) has all but at most one coordinate at a bound \(\pm1\). For \(n=2m+1\), its vertices are exactly the words with \(m\) plus signs, \(m\) minus signs, and one zero: there are \(n\binom{n-1}{m}\) of them. Their polar facets in \(P_{C_n}\) are simplices with \(n-1\) signed edge roots. A cone from the origin to each facet has volume \(\sqrt n/(n-1)!\), since the edge-root matrix with any one column deleted has Gram determinant \(n\).

For \(n=2m\), vertices of \(Z_n\) are balanced words with \(m\) plus and \(m\) minus signs, numbering \(\binom nm\). A corresponding polar facet is the convex hull of \(m\) positive roots and \(m\) negative roots, with the two simplices' barycenters coinciding, since \(\sum_i a_i=0\). It can be triangulated into \(m\) simplices by taking all \(m\) negative vertices and omitting each of the \(m\) positive vertices in turn. Each cone to such a simplex again has volume \(\sqrt n/(n-1)!\). Because \(m\binom nm=n\binom{n-1}{m-1}\), both parities give
\[
\operatorname{vol}_{n-1}(P_{C_n})
=\frac{\sqrt n}{(n-1)!}\,n\binom{n-1}{\lfloor(n-1)/2\rfloor}.
\]
Multiplying this with the polar volume, then multiplying by \((n-1)!/4^{n-1}\), proves the displayed rational factor formula. Multiplicativity proves the cactus statement.

**4. Parity-resolved asymptotics.** Write \(b_n=2^{-(n-1)}\binom{n-1}{\lfloor(n-1)/2\rfloor}\); the preceding formulas give \(\rho_n=n b_n f_n(n/2)\). The central density admits the Fourier integral
\[
f_n(n/2)=\frac2\pi\int_0^\infty\left(\frac{\sin t}{t}\right)^n dt.
\]
As \(t\to0\), \(\log(\sin t/t)=-t^2/6-t^4/180+O(t^6)\). Substituting \(t=s/\sqrt n\) into the central portion of this integral gives, using the Gaussian fourth moment \(27\),
\[
f_n(n/2)=\sqrt{\frac6{\pi n}}\left(1-\frac3{20n}+O(n^{-2})\right).
\]
The expansion is justified by dominated Laplace integration: on a fixed small neighborhood of zero the logarithm has a uniform sixth-order Taylor remainder; away from that neighborhood the absolute value of \(\sin t/t\) is uniformly less than one, with the tail controlled by a power of \(t\). Finally, Stirling's formula for central binomial coefficients gives
\[
b_n=\sqrt{\frac2{\pi n}}\begin{cases}
1-\dfrac1{4n}+O(n^{-2}),&n\ \mathrm{even},\\[2mm]
1+\dfrac1{4n}+O(n^{-2}),&n\ \mathrm{odd}.
\end{cases}
\]
Multiplication yields the two different coefficients \(-2/5\) and \(+1/10\) and common limit \(2\sqrt3/\pi\).

## Verification

Execute the companion file from this package with `python check_cactus_mahler.py` in an environment containing Python, NumPy, and SciPy. It performs exact-rational evaluations of the cycle formula through length \(19\), checks specified exact low-dimensional values and parity examples, and independently computes primal and polar convex-hull volumes for cycles of lengths \(3\) through \(8\), trees, and several two-block cactus graphs. The expected completion line is `CACTUS_MAHLER_CHECKS_PASSED 12 hull tests, rational cycles 3..19`. All \(12\) numerical hull comparisons use relative tolerance at most \(5\times10^{-7}\). These finite computations corroborate, but do not prove, the universal or asymptotic assertions; those follow from the preceding analytic argument.

## Relationship to prior work

Alexander–Fradelizi–García-Lirola–Zvavitch (arXiv:1911.10642, §§3,5) studied Mahler products of graph-induced Lipschitz-free balls, already established the free-sum mechanism under graph gluing, and explicitly identified the four-cycle equality case. The free-sum principle and that equality case are **not** new here. Kálmán–Tóthmérész (arXiv:2201.10501, §6) established cycle symmetric-edge Ehrhart and primal-volume information; the primal volume alone is **not** new. Bartha–Fodor–González Merino (arXiv:2005.08292, Introduction) studied the exact diagonal cube-section volume, its integral, and its leading limit; neither the section formula nor the leading limit alone is claimed as new. D'Alì–Juhnke-Kubitzke–Koch (arXiv:2307.04933, §5) related polar Ehrhart data to cuts and regular matroid flows. The new assessed claim is the **evaluated joint primal–polar cycle product, its all-cactus block formula, and its explicit odd/even correction coefficient**. Those evaluated conclusions were not located in the examined sources. These relationships reduce the originality margin and must be considered during independent priority checking.

## Limitations

Only simple, connected, unweighted cactus graphs are treated. This is an exact family formula, not a new general Mahler inequality or an optimization over all graphs. The parity asymptotics are subsequential and do not assert global monotonicity for all dimensions. The proof uses familiar free-sum, Fourier, and central-binomial techniques; earlier equivalent evaluations, including formulations in finite Lipschitz-free or flow-polytope terminology, may exist. Only a self-review has occurred; there is no independent mathematical audit or formal proof certification.

## References

1. M. Alexander, M. Fradelizi, L. C. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642 (first version 2019-11-24), particularly §§3 and 5.
2. F. A. Bartha, F. Fodor, B. González Merino, *Central diagonal sections of the n-cube*, arXiv:2005.08292 (first version 2020-05-17).
3. T. Kálmán, L. Tóthmérész, *Ehrhart theory of symmetric edge polytopes via ribbon structures*, arXiv:2201.10501 (first version 2022-01-25).
4. A. D'Alì, M. Juhnke-Kubitzke, M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933 (first version 2023-07-10).
5. H. Ohsugi, A. Tsuchiya, *Symmetric edge polytopes and matching generating polynomials*, arXiv:2008.08621 (first version 2020-08-19); this paper's cactus result concerns graph suspensions.
