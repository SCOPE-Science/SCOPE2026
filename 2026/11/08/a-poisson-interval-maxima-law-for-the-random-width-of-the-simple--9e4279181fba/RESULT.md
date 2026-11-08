# A Poisson interval-maxima law for the random width of the simplex-sum associahedron

## Finding

Let \(n\ge 3\), write \(e_1,\ldots,e_n\) for the standard unit vectors in \(\mathbb R^n\), and form the path-associahedron realization
\[
K_n=\sum_{1\le i\le j\le n}\operatorname{conv}\{e_i,\ldots,e_j\}.
\]
The sum is a Minkowski sum. The affine span of \(K_n\) has direction space \(H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}\). Let \(W_n\) be the length of its orthogonal projection onto a uniformly random unit direction in \(H_n\). Put
\[
a_n=\Phi^{-1}(1-1/n),
\]
where \(\Phi\) is the standard normal distribution function. Let \(\Pi^+\) and \(\Pi^-\) be independent Poisson point processes on \((0,1)\times\mathbb R\), both of intensity \(du\,e^{-z}dz\). For \(0\le s<t\le1\), define
\[
M_{\Pi}(s,t)=\sup\{z:(u,z)\in\Pi,\ s<u<t\},\qquad
\mathcal Z(\Pi)=\int_0^1\int_s^1 M_{\Pi}(s,t)\,dt\,ds.
\]
The supremum is almost surely finite on every interval of positive length; the integral exists in every finite \(L^p\) space. Then
\[
\boxed{\frac{a_n\sqrt n}{n^2}W_n-\frac{n+1}{n}a_n^2
\ \xrightarrow{d}\ \mathcal Z(\Pi^+)+\mathcal Z(\Pi^-).}
\]
The convergence includes first and second moments. The limiting law is nondegenerate and non-Gaussian, with
\[
\boxed{\mathbb E[\mathcal Z(\Pi^+)+\mathcal Z(\Pi^-)]=\gamma-\frac32,}
\]
where \(\gamma\) is Euler's constant. In particular,
\[
\boxed{\mathbb EW_n=\frac{n^{3/2}}{a_n}
\left(a_n^2+\gamma-\frac32+o(1)\right).}
\]
There is also an exact finite-dimensional mean-width formula. Write
\[
\mu_{n-1}=\mathbb E\chi_{n-1}
=\sqrt2\,\frac{\Gamma(n/2)}{\Gamma((n-1)/2)}.
\]
Then
\[
\boxed{
\mathbb EW_n=\frac{2}{\mu_{n-1}}\sum_{k=1}^{n}(n-k+1)
\int_0^\infty\left[1-\Phi(x)^k-(1-\Phi(x))^k\right]dx.}
\]
Finally, with \(\mathcal Z=\mathcal Z(\Pi^+)\),
\[
\boxed{\lim_{n\to\infty}\frac{a_n^2}{n^3}\operatorname{Var}(W_n)
=2\operatorname{Var}(\mathcal Z)\in(0,\infty).}
\]
These statements refer to this explicit unweighted Euclidean realization, rather than to every affine realization of the associahedron.

## Assumptions and scope

The indices in the Minkowski sum include every nonempty consecutive interval of \([n]\), exactly once. The singleton summands translate the body and do not affect width. The uniform direction is Haar-uniform on the unit sphere of the \((n-1)\)-dimensional Euclidean space \(H_n\), with the metric inherited from \(\mathbb R^n\). No random choice of polytope or random sample of its vertices is involved.

The point processes have infinitely many points below each fixed height on every nonempty horizontal interval, but only finitely many above any fixed height on \((0,1)\). Consequently their interval maxima are finite almost surely. Their one-interval distribution is exactly
\[
\mathbb P\{M_{\Pi}(s,t)\le z\}=\exp[-(t-s)e^{-z}].
\]
Thus \(M_{\Pi}(s,t)\) has the distribution of \(\log(t-s)+G\), where \(G\) is a standard Gumbel variable. In particular its \(L^p\) norm is at most a constant (depending on \(p\)) times \(1+|\log(t-s)|\). Minkowski's integral inequality ensures that \(\mathcal Z(\Pi)\) has every finite moment.

## Proof

**1. Exact Gaussian representation.** For any deterministic vector \(g\in\mathbb R^n\), the support of the simplex \(\operatorname{conv}\{e_i,\ldots,e_j\}\) in direction \(g\) is \(\max_{i\le r\le j}g_r\). Additivity of support functions therefore gives, for the width numerator,
\[
S_n(g)=\sum_{1\le i\le j\le n}
\left(\max_{i\le r\le j}g_r-\min_{i\le r\le j}g_r\right).
\]
Let \(G_1,\ldots,G_n\) be independent standard normals and put \(\bar G=n^{-1}\sum_iG_i\), \(R_n=(\sum_i(G_i-\bar G)^2)^{1/2}\). The vector \((G_i-\bar G)/R_n\) is Haar-uniform on the unit sphere of \(H_n\). Since subtracting \(\bar G\) leaves every interval range unchanged,
\[
W_n\ \stackrel d=\ S_n(G)/R_n.
\]
Moreover \(R_n\) has the \(\chi_{n-1}\) distribution and is independent of the direction (and therefore of \(S_n(G)/R_n\)). Hence \(\mathbb ES_n(G)=\mu_{n-1}\mathbb EW_n\). Symmetry of Gaussian minima and maxima, followed by grouping intervals by their length \(k\), gives the finite-dimensional formula in the finding: for \(M_k\) the maximum of \(k\) independent standard normals,
\[
\mathbb ES_n(G)=2\sum_{k=1}^n(n-k+1)\mathbb EM_k,\quad
\mathbb EM_k=\int_0^\infty[1-\Phi(x)^k-(1-\Phi(x))^k]dx.
\]

**2. Joint extreme-point process.** Define two marked empirical point measures
\[
\Xi_n^+=\sum_{i=1}^n\delta_{(i/n,\,a_n(G_i-a_n))},\qquad
\Xi_n^-=\sum_{i=1}^n\delta_{(i/n,\,a_n(-G_i-a_n))}.
\]
The standard Gaussian tail ratio, for each fixed real \(z\), is
\[
n\,\mathbb P\{G_1>a_n+z/a_n\}\longrightarrow e^{-z}.
\]
Rarity, asymptotic spatial uniformity of the deterministic grid, independence across indices, and disjointness of upper and lower extreme events at a single index show by the Laplace-functional criterion that
\[
(\Xi_n^+,\Xi_n^-)\ \xrightarrow{d}\ (\Pi^+,\Pi^-)
\]
in the product vague topology on locally finite point measures above every bounded-below mark level. In particular the two limiting processes are independent.

**3. Control of all interval lengths.** Define \(Y_{n,k}=a_n(M_k-a_n)\). The following bound is sufficient for discarding short intervals: for every fixed \(p<\infty\) there is \(C_p\) such that, for all sufficiently large \(n\),
\[
\|Y_{n,k}\|_p\le
\begin{cases}
C_p\log n,&1\le k<\sqrt n,\\
C_p(1+\log(n/k)),&\sqrt n\le k\le n.
\end{cases}
\]
Here is a direct verification of the nonstandard uniform estimate. For \(z\ge0\), the increasing Gaussian hazard rate and \(\overline\Phi(a_n)=1/n\) yield
\[
\mathbb P(Y_{n,k}>z)\le(k/n)e^{-z}.
\]
For \(0\le z\le a_n^2\), integration of the Gaussian hazard (bounded below by its positive argument) yields
\[
\mathbb P(Y_{n,k}<-z)
\le\exp[-(k/n)e^{z/2}].
\]
Writing \(\ell=\log(n/k)\) and integrating these tails, splitting the negative tail at \(2\ell\), gives the second bound up to \(z=a_n^2\). Beyond that point, \(a_n-z/a_n\le0\), and the remaining integral is bounded by Gaussian tails multiplied by \(2^{-(k-1)}\), which is negligible for \(k\ge\sqrt n\). For \(k<\sqrt n\), the elementary Gaussian maximal inequality \(\|M_k\|_p\le C_p\sqrt{\log(k+1)}\) gives the first bound.

Consequently the total scaled contribution of intervals of length at most \(\varepsilon n\), after centering each maximum by \(a_n\), has \(L^p\) norm at most
\[
C_p\varepsilon(1+|\log\varepsilon|)+o(1)
\]
for every fixed \(\varepsilon>0\). Indeed, there are \(n-k+1\) intervals of length \(k\), and this is the bound for the corresponding weighted sum divided by \(n^2\). The same bound holds for interval minima by symmetry.

**4. Convergence of the integrated extrema.** For intervals whose lengths are at least \(\varepsilon n\), restrict the point processes initially to marks above a fixed lower cutoff and use the continuous mapping theorem. A finite cover by horizontal subintervals of length below \(\varepsilon\) shows that the maximum over each retained macroscopic interval exceeds the cutoff with probability approaching one as the cutoff tends to minus infinity. The functional is almost surely continuous because the Poisson points have distinct positions and marks and the exceptional interval endpoints have Lebesgue measure zero. The scaled discrete double sum is a Riemann approximation to the continuous integral. The \(L^p\) estimate in step 3 then permits \(\varepsilon\downarrow0\), establishing joint convergence, with moment convergence through order four,
\[
\frac1{n^2}\sum_{1\le i\le j\le n}
 a_n\left(\max_{i\le r\le j}G_r-a_n\right)
\ \xrightarrow{d}\ \mathcal Z(\Pi^+),
\]
and the analogous independent limit for the minima of the same Gaussian sample.

**5. Haar normalization.** There are \(N_n=n(n+1)/2\) intervals. Write \(F_n\) for the sum of both centered discrete extrema in step 4. Then an exact algebraic identity is
\[
\frac{a_n\sqrt n}{n^2}W_n-\frac{2N_n}{n^2}a_n^2
=\frac{\sqrt n}{R_n}F_n
+\left(\frac{\sqrt n}{R_n}-1\right)\frac{2N_n}{n^2}a_n^2.
\]
For sufficiently large \(n\), chi-square inverse-moment formulas give \(\|\sqrt n/R_n-1\|_4=O(n^{-1/2})\). Since \(a_n^2=O(\log n)\) and \(F_n\) is bounded in \(L^4\), both normalization errors tend to zero in \(L^2\). This proves the stated law and convergence of the first two moments.

**6. Constants, strict randomness and non-Gaussianity.** The one-interval Gumbel law gives
\[
\mathbb E\mathcal Z
=\int_0^1(1-\ell)(\log\ell+\gamma)\,d\ell
=\frac\gamma2-\frac34.
\]
The mean and variance assertions follow. The limit has strictly positive variance: increasing a Poisson mark in the central third of the horizontal interval changes a positive-measure set of interval maxima. It is not Gaussian. More quantitatively, split the process into independent marks above and below zero. With fixed positive probability, the integral generated by the lower part exceeds a fixed negative constant. Independently, with probability bounded below by \(c e^{-T}\), there is a mark above \(T\) at position in \([1/3,2/3]\); this raises the integral by at least \((2/9)T\) relative to the lower-mark process. Hence the upper tail of \(\mathcal Z\) has an exponential lower bound, which is incompatible with any Gaussian upper tail. The same argument, requiring the independent second copy to exceed a fixed constant, applies to their sum.

## Verification

Run `python3 verify_path_width.py` from the folder containing the file. The script uses only Python's standard library. It independently computes all interval ranges by both direct enumeration and a monotone-stack identity; verifies the two-point (segment) boundary; checks the Poisson interval-maxima integral against midpoint quadrature on a fixed marked configuration; and makes seeded finite-sample checks of the Gaussian and Poisson scalings. The executed script returned `INTERVAL_ASSOCIAHEDRON_WIDTH_AND_POISSON_CHECKS_PASSED`. Such finite sampling cannot establish the limiting theorem; the proof is the tail bound, point-process convergence, and uniform integrability argument above.

For a finite Poisson cutoff \(T>0\), the limiting integral is reproducible without gridding all intervals. If the finitely many marks above \(-T\) have positions \(u_j\) and values \(z_j\), let \(\ell_j\) and \(r_j\) be the nearest positions of strictly higher marks on the left and right, using the domain endpoints if none exists. Then
\[
\int_{0<s<t<1}\max\{-T,M_{\Pi}(s,t)\}\,ds\,dt
=-\frac T2+\sum_j(z_j+T)(u_j-\ell_j)(r_j-u_j).
\]
The right-hand side is the exact Cartesian-tree formula checked by the verifier. Letting \(T\to\infty\) recovers \(\mathcal Z(\Pi)\) in every finite \(L^p\).

## Relationship to prior work

The simplex-sum realization is classical; the study of graph associahedra and interval building sets in Padrol--Pilaud--Poullot (arXiv:2109.09200, first posted 2021-09-19) provides the literature lead. Postnikov's 2005 preprint on generalized permutohedra gives earlier background for simplex Minkowski sums. Kabluchko--Litvak--Zaporozhets (arXiv:1511.08479, 2015) treats random-projection widths of regular simplices, cubes and cross-polytopes and supplies the natural Gaussian maximum comparison. The 2026 interval-hypergraphic paper (arXiv:2606.18376) examines vertex/face combinatorics. None of the inspected results yields the correlated all-interval extremal functional or the displayed non-Gaussian width limit for this particular realization. This is an originality assessment based on inspected sources and searches, not a guarantee of exhaustive priority.

## Limitations

The theorem does not cover general weights on the interval simplices, arbitrary affine realizations of the associahedron, or random projections to subspaces of dimension greater than one. The limiting variance is specified exactly as a finite positive Poisson-functional variance, but no elementary closed form is asserted. The result does not claim an explicit convergence rate. Independent checking of historical priority and of the proof has not been performed. Numerical checks are finite corroboration, not substitutes for point-process arguments.

## References

1. A. Padrol, V. Pilaud, G. Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200 (first posted 2021-09-19), https://arxiv.org/abs/2109.09200.
2. A. Postnikov, *Permutohedra, associahedra, and beyond*, arXiv:math/0507163 (first posted 2005-07-07), https://arxiv.org/abs/math/0507163.
3. Z. Kabluchko, A. E. Litvak, D. Zaporozhets, *Mean width of regular polytopes and expected maxima of correlated Gaussian variables*, arXiv:1511.08479 (first posted 2015-11-26), https://arxiv.org/abs/1511.08479.
4. J. Bastidas, F. Gélinas, V. Pilaud, G. Poullot, A. Sack, E. Tzanaki, *Interval hypergraphic polytopes (or deformed associahedra), Tamari interval posets, and weeping willows*, arXiv:2606.18376 (first posted 2026-06-16), https://arxiv.org/abs/2606.18376.
