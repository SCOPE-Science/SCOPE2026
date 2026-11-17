# Sharp mean-distance collapse for parallel-arm metric graphs

## Finding
Let \(m\geq4\), let \(G\) consist of two vertices joined by \(m\) internally disjoint metric edges of arbitrary positive lengths \(\ell_1,\ldots,\ell_m\), and let \(L=\sum_i\ell_i\). For independent normalized-arclength-uniform points \(X,Y\) in \(G\), write \(\rho(G)=\mathbb E[d_G(X,Y)]\). Then
\[
\boxed{\rho(G)>\frac{2m-3}{4(m-1)^2}L.}
\]
The bound is the sharp infimum for fixed \(L\), but never an attained minimum among strictly positive arm lengths. If \(\ell_i^{(j)}>0\) with fixed total \(L\) approaches this bound, then, after permuting the arms for each \(j\), the ordered length vector tends to
\[
\bigl(0,L/(m-1),\ldots,L/(m-1)\bigr).
\]
Conversely, every such sequence approaches the bound. In contrast, the equal-length \(m\)-arm graph has \(\rho(G)/L=(2m-1)/(3m^2)\), strictly greater for \(m\ge4\). For three arms the sharp minimum is instead the equilateral graph, with normalized mean \(5/27\); that three-arm case is contextual and not claimed as novel.

## Assumptions and scope
Each edge is a full closed metric segment, with intrinsic shortest-path distance on the quotient graph and one-dimensional Hausdorff measure on its edges (vertices have zero measure). The two samples are independent with law \(L^{-1}ds\). The arms are allowed to have different positive lengths. No assumption that each edge itself is a shortest pole-to-pole path is made. All inequalities are for every real positive length vector with \(m\ge4\); the zero-arm vector is only a metric limit and is excluded from the class.

## Proof
Let \(k=m-1\) and order the lengths \(a=\ell_1\le b_1\le\cdots\le b_k\), writing \(B=\sum_i b_i\), \(S_2=\sum_i b_i^2\), \(S_3=\sum_i b_i^3\), and \(L=a+B\). Define \(T=\int_G\int_G d_G(x,y)\,ds_x\,ds_y=L^2\rho(G)\).

**Pair integrations.** The integral over two points of the shortest arm is \(a^3/3\). On another single arm of length \(p\ge a\), a shorter path between its points may go around the other way through the shortest arm; integrating the minimum of the direct separation \(t\) and \(p+a-t\) gives
\[
K(p,a)=2\int_0^p(p-t)\min(t,p+a-t)\,dt
=\frac{a^3-3a^2p+3ap^2+3p^3}{12}.
\]
For two distinct arms of lengths \(p\le q\), the two routes directly through the poles contribute, before the possible shorter third-arm route, the ordered integral
\[
J(p,q)=\int_0^p\int_0^q\min(x+y,p+q-x-y)\,dy\,dx
=\frac{p(p+q)^2}{4}-\frac{p^3}{3}.
\]
The shortest possible additional pole-to-pole route uses the arm of length \(a\). The improvement over the preceding integrand is zero for any pair involving this shortest arm. For a pair of arms of lengths \(p,q\ge a\), elementary integration in coordinates centered at the two arm midpoints yields the improvement
\[
R(p,q;a)=\frac12\int_a^p(p-t)(q-t)\,dt
=\frac{(p-a)^2(q-p)}4+\frac{(p-a)^3}{6}.
\]
Indeed, with centered coordinates \(u=x-p/2\), \(v=y-q/2\), the baseline is \((p+q)/2-|u+v|\); the alternative is \((p+q)/2+a-|u-v|\). Their positive difference is \((2\min(|u|,|v|)-a)_+\) on opposite-sign quadrants and zero elsewhere. There is no other shorter route: a shortest path between two points of distinct arms either passes through a common pole or traverses one shortest pole-to-pole edge.

Summing both orders for every distinct pair, and all same-arm integrals, simplifies exactly to
\[
\boxed{T=\frac{2k^2-3k+4}{12}a^3+\frac{5-2k}{4}a^2B+\bigl(\frac a4+\frac B2\bigr)S_2+\frac a2B^2-\frac14S_3.}\tag{1}
\]
This identity is valid for ties and all real positive lengths; it is an exact integral, not an asymptotic approximation.

**Balancing all but the shortest arm.** For fixed \(a,B\), the dependence on the remaining arms in (1) is \(\tfrac14\sum_i f(b_i)\), where \(f(t)=t^2(a+2B-t)\). Whenever \(a\le x<y\) are two of these lengths,
\[
f'(y)-f'(x)=(y-x)\bigl(2a+4B-3(x+y)\bigr)>0,
\]
because \(x+y\le B\). Moving \(x,y\) toward their common mean therefore strictly decreases \(f(x)+f(y)\) unless they coincide. Repeated pairwise averaging, or compactness followed by the same strict exchange argument, proves that at fixed \(a,B\) the unique minimizer satisfies \(b_1=\cdots=b_k=B/k\). This balancing is compatible with the order condition \(b_i\ge a\).

**One-variable minimization and sharpness.** By scaling set \(L=1\), write \(b=(1-a)/k\), and note \(0\le a\le1/(k+1)\). On this balanced family (1) gives
\[
\Phi_k(a)=\frac{2k^2-3k+4}{12}a^3+\frac{k(5-2k)}4a^2b+\frac{k(2k+1)}4ab^2+\frac{k(2k-1)}4b^3.
\]
Direct differentiation and factorization yield
\[
\Phi_k'(a)=\frac{k-1}{4k^2}\bigl((k+1)a-1\bigr)
\bigl((2k^2+3k-3)a-(2k-3)\bigr).
\]
For all \(k\ge2\), the sole interior stationary point is a strict maximum (the derivative changes from positive to negative), so the minima over the compact interval occur at endpoints. There,
\[
\Phi_k(0)=\frac{2k-1}{4k^2},\qquad
\Phi_k\!\left(\frac1{k+1}\right)=\frac{2k+1}{3(k+1)^2},
\]
and their difference (second minus first) is
\[
\frac{(k-1)(2k^2-3k-3)}{12k^2(k+1)^2}.
\]
It is positive for every integer \(k\ge3\), and negative for \(k=2\). Thus for \(m=k+1\ge4\), the *only* minimizer in the ordered closed simplex of nonnegative lengths is \(a=0\) with all \(k\) others equal. Positive lengths rule out equality; continuity proves approachability. Strict pairwise balancing, strict endpoint comparison, and compactness yield the stated characterization of *every* minimizing sequence. Rescaling to general \(L\) concludes the proof. The three-arm comparison follows at \(k=2\).

## Verification
Run `python code/check_mean_distance.py` after installing `numpy>=1.24`. The checker independently integrates the shortest of all pole and third-arm routes by tensor Gauss–Legendre quadrature on each ordered edge pair; it compares eight genuinely weighted configurations with the cubic expression and checks 2,000 independently generated positive length vectors for each number of arms from three through nine. The marker `BANANA_METRIC_MEAN_QUADRATURE_AND_BOUNDARY_TESTS_OK` indicates these tests passed. Symbolic differentiation of the displayed elementary polynomial independently checks the factorization. The proof above supplies the general exact integration and global bound; finite computation alone is not used to infer the theorem.

## Relationship to prior work
Continuous mean distance on weighted metric graphs is studied in Garijo–Márquez–Silveira (2023), including general computation algorithms, and in Baptista–Kennedy–Mugnolo (2024), which proves the universal lower bound \(\rho(G)\ge (2E-1)L/(4E^2)\) for an arbitrary graph with \(E\) edges, with equality only at the equilateral flower. That bound is strictly weaker when applied to these \(m\)-edge two-pole graphs. The latter paper also gives the exact mean for the \((m-1)\)-petal equal-length flower, equal to the **boundary value** here; that boundary formula is not newly claimed. The nontrivial contribution is the strict, sharp optimization across all positive-length *parallel-arm* metrics, the uniqueness of the collapse regime, and the distinction between three and four arms. Earlier Doyle–Graver mean-distance work is relevant but its full text was unavailable for decisive theorem-by-theorem comparison; priority remains provisional. The metric-graph geometric setting is also treated, for a different invariant, by Dey–Shi–Wang (2015).

## Limitations
This result concerns only two-pole graphs with \(m\) parallel arcs, not arbitrary metric graphs, trees, random discrete vertices, spectral gap, or nonuniform sampling. It supplies neither a complete distance distribution nor a finite positive-length minimizer. The 1982 Doyle–Graver paper could not be inspected in full; the originality comparison is therefore provisional. No independent audit has been performed.

## References
1. T. K. Dey, D. Shi, Y. Wang, *Comparing Graphs via Persistence Distortion*, arXiv:1503.07414, first publicly available 2015-03-25, https://arxiv.org/abs/1503.07414 (geometry of continuous metric graphs; not a mean-distance result).
2. D. Garijo, A. Márquez, R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, Results in Mathematics 78 (2023), article 139, https://doi.org/10.1007/s00025-023-01902-w.
3. L. N. Baptista, J. B. Kennedy, D. Mugnolo, *Mean Distance on Metric Graphs*, Journal of Geometric Analysis 34 (2024), article 137, https://doi.org/10.1007/s12220-024-01574-0.
4. J. K. Doyle, J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory 6 (1982), pp. 453–471, https://doi.org/10.1002/jgt.3190060410 (full text not accessible for direct comparison).
