# Quadratic reproduction obstructs Gini contraction in discrete least-squares projection

## Finding

For every integer \(n\ge2\) and polynomial degree \(0\le d\le n-1\), let \(P_{n,d}\) be the equal-weight Euclidean least-squares projector on the samples at the consecutive nodes \(0,1,\ldots,n-1\) onto polynomial values of degree at most \(d\). For the complete-pair Gini seminorm
\[
G_n(x)=\sum_{0\le i<j<n}|x_i-x_j|,
\]
its exact nonexpansivity classification is
\[
\boxed{\|P_{n,0}\|_{G_n}=0,\qquad
\|P_{n,d}\|_{G_n}=1\ (d=1\text{ or }d=n-1),\qquad
\|P_{n,d}\|_{G_n}>1\ (2\le d\le n-2).}
\]
The strict inequality uses the single-coordinate datum \(e_0\), for every interior polynomial degree and dimension. The sharper mechanism is independent of polynomial bases: **any Euclidean orthogonal projection onto a subspace containing the sampled constant, linear, and quadratic vectors but not \(e_0\) strictly amplifies \(G_n\) on \(e_0\)**.

The quadratic case has a persistent quantitative effect: for the degree-two projectors,
\[
\boxed{\lim_{n\to\infty}\frac{G_n(P_{n,2}e_0)}{G_n(e_0)}=\frac{189}{125}.}
\]
This is the limiting amplification **of that explicit input**, not an asserted limit of the sharp operator norm. At four nodes, the sharp degree-two norm is exactly \(17/15\), attained by \(e_0\).

## Assumptions and scope

All input vectors are real; the observation nodes are distinct and equally spaced; the least-squares weights are equal and positive. The projector uses the ordinary Euclidean inner product on \(\mathbb R^n\), not a graph-smoothing stencil. The induced Gini coefficient means
\[
\|T\|_{G_n}=\sup_{G_n(x)>0}\frac{G_n(Tx)}{G_n(x)}.
\]
Every projector here fixes constants, so the quotient seminorm is well-defined. Define \(e_0=(1,0,\ldots,0)\). For an abstract subspace \(U\), assume \(n\ge3\), \(\mathbf 1\in U\), \((i)_{i=0}^{n-1}\in U\), \((i^2)_{i=0}^{n-1}\in U\), and \(e_0\notin U\).

## Proof

**1. A moment obstruction for any quadratic-reproducing orthogonal projector.** Let \(P_U\) be the Euclidean orthogonal projection onto \(U\), and put \(q=P_Ue_0\). Orthogonality and reproduction of the three sampled monomials imply
\[
\sum_{i=0}^{n-1}q_i=1,\qquad
\sum_{i=0}^{n-1}i q_i=0,\qquad
\sum_{i=0}^{n-1}i^2 q_i=0.
\]
The exact identity \(|a|=a+2(-a)_+\) yields
\[
G_n(q)=\sum_{i<j}(q_i-q_j)+2\sum_{i<j}(q_j-q_i)_+
=n-1+2\sum_{i<j}(q_j-q_i)_+.
\]
Suppose the excess were zero. Then \(q_0\ge q_1\ge\cdots\ge q_{n-1}\). Write \(a_i=i q_i\) for \(1\le i\le n-1\). The first-moment condition says \(\sum_i a_i=0\). By monotonicity, all positive \(a_i\) precede all negative \(a_i\). If both signs occur, choose any real \(r\) strictly between the last positive and first negative indices. Then
\[
\sum_{i=1}^{n-1}i a_i=\sum_{i=1}^{n-1}(i-r)a_i<0,
\]
contrary to the second-moment condition. If both signs do not occur, their zero sum forces every \(a_i=0\). In either case the second condition therefore forces \(q_i=0\) for \(i\ge1\), and \(q_0=1\); hence \(q=e_0\in U\), a contradiction. Consequently
\[
G_n(P_Ue_0)>n-1=G_n(e_0).
\]
This proves the abstract obstruction without any numerical enumeration or asymptotics.

**2. Classification by polynomial degree.** Let \(V_{n,d}=\{(p(i))_{i=0}^{n-1}:\deg p\le d\}\). For \(d=0\), \(P_{n,0}\) produces a constant vector and the Gini norm is zero. For \(d=n-1\), polynomial interpolation makes \(P_{n,n-1}\) the identity, hence norm one. For \(d=1\), set \(\mu=(n-1)/2\) and \(S=\sum_i(i-\mu)^2\). The fitted slope is \(b=S^{-1}\sum_i(i-\mu)x_i\), so
\[
G_n(P_{n,1}x)=|b|\sum_{i<j}(j-i)
=\left|\sum_{i<j}(x_j-x_i)\right|\le G_n(x),
\]
where \(\sum_{i<j}(j-i)=2S\) and \(\sum_{i<j}(x_j-x_i)=2\sum_i(i-\mu)x_i\). Every strictly increasing input attains equality. Finally, for \(2\le d\le n-2\), \(V_{n,d}\) contains the three monomials but not \(e_0\): an interpolating polynomial for \(e_0\) would have \(n-1\) distinct zeros with degree at most \(n-2\). Step 1 applies and proves strict amplification. This completes the all-degree classification.

**3. An exact first example.** In dimension four, the quadratic projection of \(e_0\) is
\[
P_{4,2}e_0=(19,3,-3,1)/20.
\]
The output Gini value is \(17/5\) while \(G_4(e_0)=3\), so the ratio is \(17/15\). For the sharp upper bound, the positive and negative level-set decomposition of any vector reduces the induced norm of any constant-preserving linear operator to binary input cuts. Enumerating the 14 nontrivial subsets of four nodes (or the seven complementary pairs) gives no ratio above \(17/15\); the exact standalone checker reconstructs the projector by rational Gram inversion and verifies this enumeration.

**4. Persistent quadratic amplification.** For \(n\ge3\), discrete orthogonalization of \(1\), \(z_j=j-(n-1)/2\), and \(r_j=z_j^2-(n^2-1)/12\) gives the explicit endpoint column
\[
(P_{n,2}e_0)_j=\frac{3[10j^2+(6-12n)j+3n^2-3n+2]}{n(n+1)(n+2)}.
\]
Uniformly in the sampled index \(j\), we have
\[
n(P_{n,2}e_0)_j=k(j/(n-1))+O(n^{-1}),\qquad
k(t)=9-36t+30t^2.
\]
Consequently a two-dimensional Riemann sum gives
\[
\lim_{n\to\infty}\frac{G_n(P_{n,2}e_0)}{n-1}
=\int_{0<u<v<1}|k(u)-k(v)|\,du\,dv.
\]
Since \(\int_0^1 k(t)\,dt=1\) and \(\int_0^1 t k(t)\,dt=0\), the oriented integral is \(1\). Also
\[
k(u)-k(v)=(v-u)[36-30(u+v)],
\]
which is negative precisely when \(u+v>6/5\). Changing variables to \(s=u+v\) evaluates twice the negative contribution as
\[
\frac12\int_{6/5}^{2}(30s-36)(2-s)^2\,ds=\frac{64}{125}.
\]
The absolute integral is therefore \(1+64/125=189/125\), proving the limit. It is a witness lower bound for the asymptotic sharp norms, not an equality claim for those norms.

## Verification

The standalone dependency-free Python file `polynomial_gini_verifier.py` constructs exact Gram matrices with `fractions.Fraction`, tests the four-site sharp binary-cut norm, checks all interior degrees \(2\le d\le n-2\) for \(4\le n\le11\), tests degree-zero, affine and interpolating boundary cases through ten sites, compares the quadratic endpoint column with the closed formula, and verifies the rational integral \(189/125\). Its output includes `EXACT_FOUR_SITE_SHARP_NORM_17_OVER_15_PASSED`, `EXACT_ALL_POLYNOMIAL_DEGREE_CASES_PASSED 36`, and `EXACT_CONTINUUM_INTEGRAL_189_OVER_125_PASSED`. The exhaustive finite experiments do not prove the all-dimensional theorem; that proof is in Steps 1–4.

## Relationship to prior work

Savitzky and Golay (1964) established polynomial least-squares smoothing procedures; Persson and Strang (2003) develop discrete polynomial smoothing and orthogonal-kernel descriptions. Cohen, Davenport, and Leviatan (2011) discuss stability and accuracy of least-squares approximation in other norms. A closely related published result, *Arithmetic lattice phases in the boundary sensitivity of quadratic discrete least squares* (2026), computes the degree-two equispaced **endpoint evaluation \(\ell^\infty\) row norm** and a second-order arithmetic asymptotic; its detailed kernel provides a related building block, but its stated theorem does not give a complete-pair Gini operator coefficient, the moment obstruction, or an all-degree classification. The present endpoint Gini calculation is a different functional of the kernel, and the arbitrary-degree conclusion uses only moment reproduction and nonmembership of the endpoint impulse in the fitting subspace.

## Limitations

This theorem classifies the **nonexpansive versus amplifying** degrees; it does not supply the exact sharp Gini coefficient for every interior degree and dimension. The limit \(189/125\) concerns a fixed input sequence for degree two, not the sharp norm limit. All observations are equally weighted and equally spaced; unequal weights or nonuniform designs are not covered by the stated all-degree classification. Although the compared sources do not imply the complete classification, historical priority cannot be guaranteed against unindexed or inaccessible treatments. No independent audit has been performed.

## References

1. A. Savitzky and M. J. E. Golay, *Smoothing and Differentiation of Data by Simplified Least Squares Procedures*, *Analytical Chemistry* **36** (1964), 1627–1639. DOI: 10.1021/ac60214a047; full text also reprinted in NASA technical report, https://ntrs.nasa.gov/api/citations/19700027052/downloads/19700027052.pdf.
2. P.-O. Persson and G. Strang, *Smoothing by Savitzky-Golay and Legendre Filters* (2003), https://persson.berkeley.edu/pub/persson03smoothing.pdf.
3. A. Cohen, M. A. Davenport, and D. Leviatan, *On the stability and accuracy of least squares approximations*, arXiv:1111.4422 (first submitted 18 November 2011), https://arxiv.org/abs/1111.4422.
4. *Arithmetic lattice phases in the boundary sensitivity of quadratic discrete least squares*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-arithmetic-lattice-phases-in-the-boundary-sensitivity-of-quadrat--584e5565b3bb.
