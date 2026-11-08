# A sharp Mahler-product hierarchy for complete-bipartite symmetric edge polytopes

## Finding
For positive integers \(p,q\), let \(N=p+q\), and consider the symmetric edge polytope of the complete bipartite graph:
\[
P_{p,q}=\operatorname{conv}\{\pm(e_i-e_{p+j}):1\le i\le p,\ 1\le j\le q\}\subset H,\quad H=\{x\in\mathbb R^N:\sum_i x_i=0\}.
\]
All volumes are intrinsic Euclidean volumes of dimension \(N-1\), and the polar is taken inside \(H\). Its polar volume is
\[
\operatorname{vol}_{N-1}(P_{p,q}^{\circ})=\frac{2^{N-1}p!q!}{\sqrt N\,(N-1)!}.
\]
Put \(A_n(t)=\sum_{i=0}^{n}\binom ni^2t^i(1-t)^{n-i}\) and \(B_r(t)=r A_{r-1}(t)/2^{r-1}\). Each \(B_r\) is a probability density on \([0,1]\). The complete volume-product formula is
\[
R(p,q):=\frac{(N-1)!}{4^{N-1}}\operatorname{vol}(P_{p,q})\operatorname{vol}(P_{p,q}^{\circ})
=\int_0^1 B_p(t)B_q(t)\,dt
=\frac{p!q!}{(N-1)!}\sum_{i=0}^{\min(p-1,q-1)}\frac{\binom{p-1}{i}\binom{q-1}{i}\binom{2i}{i}}{4^i}.
\]
The normalized Mahler product is exactly one if and only if \(\min(p,q)\le2\), and is strictly greater than one otherwise. Whenever \(p\ge2\) and \(q\ge3\), it increases strictly on replacing \(p\) by \(p+1\), and symmetrically for the other class. For each fixed \(p\ge1\),
\[
\lim_{q\to\infty}R(p,q)=\frac{p\binom{2p-2}{p-1}}{4^{p-1}}.
\]
For \(m=\min(p,q)\ge4\),
\[
\frac{\sqrt m}{8}\le R(p,q)\le \frac{m\binom{2m-2}{m-1}}{4^{m-1}}.
\]
In particular, the product ratio is of order \(\sqrt{\min(p,q)}\) as both class sizes grow. For instance, \(R(3,3)=81/80\). This statement separates the classical exact polytope volume from the new polar-volume and Mahler-product conclusions.

## Assumptions and scope
The integers \(p,q\) are at least one; \(N\ge2\); the convex body is full-dimensional in \(H\), with the standard Euclidean scalar product. The polar is \(P_{p,q}^{\circ}=\{z\in H:|z_i-z_{p+j}|\le1\text{ for all }i,j\}\). The Mahler benchmark \(4^{N-1}/(N-1)!\) is the volume product of a standard centrally symmetric parallelotope or cross-polytope in dimension \(N-1\). No lower bound for arbitrary symmetric bodies is asserted.

## Proof
**Step 1: an exact Minkowski-sum cross-section formula.** Write \(\Delta_n=\operatorname{conv}(0,e_1,\ldots,e_n)\). For \(0\le t\le1\), the coordinates of \(t\Delta_n+(1-t)(-\Delta_n)\) satisfy \(\sum_i(x_i)_+\le t\) and \(\sum_i(-x_i)_+\le1-t\). On an orthant with exactly \(i\) positive coordinates, the volume is \(t^i(1-t)^{n-i}/(i!(n-i)!)\). Summing over all \(\binom ni\) choices and dividing by \(\operatorname{vol}(\Delta_n)=1/n!\) gives \(A_n(t)\). Affine invariance proves the same ratio for any \(n\)-simplex; the \(n=0\) convention is one.

**Step 2: volume of the symmetric edge polytope.** Let the left and right coordinate sums define their own zero-mean subspaces, orthogonal to the axial direction \(a=((1/p)\mathbf 1_p,-(1/q)\mathbf1_q)\), of norm \(\sqrt{N/(pq)}\). The positive vertex face lies at axial level \(+a\) and is a product of a centered \((p-1)\)-simplex and the negative of a centered \((q-1)\)-simplex; the opposite face is its negative. A section at interpolation parameter \(t\in[0,1]\) is therefore the product of the corresponding Minkowski interpolations. The intrinsic volumes of these base simplices are \(\sqrt p/(p-1)!\) and \(\sqrt q/(q-1)!\), with the zero-dimensional convention one. The inter-face Euclidean altitude is \(2\sqrt{N/(pq)}\). Fubini yields
\[
\operatorname{vol}(P_{p,q})=\frac{2\sqrt N}{(p-1)!(q-1)!}\int_0^1 A_{p-1}(t)A_{q-1}(t)\,dt.
\]

**Step 3: the intrinsic polar volume.** Write a polar point's two blocks as \(u_i,v_j\), modulo simultaneous translation. Fix the unique minimal left coordinate at zero, which gives \(p\) equipotent regions up to measure-zero ties. For the remaining \(p-1\) left coordinates in \([0,M]\), with maximum \(M\in[0,2]\), the permitted interval for each right coordinate is \([M-1,1]\), of length \(2-M\). The gauge-to-orthogonal-projection Jacobian is exactly \(N^{-1/2}\): the Gram matrix of the \(N-1\) projected coordinate vectors is \(I_{N-1}-\mathbf1\mathbf1^{\mathsf T}/N\), with determinant \(1/N\). Consequently, for \(p\ge2\),
\[
\operatorname{vol}(P_{p,q}^{\circ})=\frac{p(p-1)}{\sqrt N}\int_0^2 M^{p-2}(2-M)^q\,dM
=\frac{2^{N-1}p!q!}{\sqrt N\,(N-1)!},
\]
using the beta integral. For \(p=1\), the gauged polar is a \(q\)-cube of side two, whose intrinsic volume is \(2^q/\sqrt{q+1}\), the same formula. Multiplication with Step 2 gives the overlap representation.

**Step 4: the finite sum and densities.** The normalization \(\int_0^1 A_{r-1}(t)\,dt=2^{r-1}/r\) follows by integrating each beta monomial: \(\binom{r-1}{i}^2\int_0^1t^i(1-t)^{r-1-i}\,dt=\binom{r-1}{i}/r\). The published \(h^*\)-polynomial formula for complete-bipartite symmetric edge polytopes [1, Theorem 1.1], evaluated at one and converted using the covolume \(\sqrt N\) of the root lattice in \(H\), gives
\[
\operatorname{vol}(P_{p,q})=\frac{\sqrt N\,2^{N-1}}{(N-1)!}\sum_{i=0}^{\min(p-1,q-1)}\frac{\binom{p-1}{i}\binom{q-1}{i}\binom{2i}{i}}{4^i}.
\]
Combining with Step 3 proves the displayed finite-sum formula independently of any numerical extrapolation.

**Step 5: threshold and monotonicity.** Let \(h=t(1-t)\). The constant-term identity
\[
A_n(t)=\operatorname{CT}_{z}\left(1+\sqrt h(z+z^{-1})\right)^n
=\sum_{k=0}^{\lfloor n/2\rfloor}\binom n{2k}\binom{2k}{k}h^k=:C_n(h)
\]
shows \(B_1=B_2=1\), while each \(B_r\), for \(r\ge3\), is strictly increasing as a function of \(h\) on \([0,1/4]\). Because \(t\) uniformly distributed on \([0,1]\) gives a nonconstant \(h\), the strict Chebyshev covariance inequality implies \(\int_0^1B_pB_q\,dt>\int B_p\int B_q=1\) for \(p,q\ge3\). The other cases equal one.

For \(r\ge2\), the ratio \(C_r(h)/C_{r-1}(h)\) is strictly increasing for positive \(h\): on shared indices \(k\), the coefficient ratios are \(\binom r{2k}/\binom{r-1}{2k}=r/(r-2k)\), strictly increasing with \(k\); a new highest-degree term when present only strengthens the increase. Equivalently, cross-multiplication has positive coefficients after pairing smaller and larger indices. Hence the density ratio \(B_{r+1}(t)/B_r(t)\) strictly increases in \(h\). Since both densities integrate to one, a second strict covariance inequality with the increasing function \(B_q(h)\) gives \(R(r+1,q)>R(r,q)\) when \(q\ge3\). Symmetry establishes the remaining cases.

**Step 6: limits and growth.** The mixture representation \(B_q(t)=2^{1-q}\sum_{i=0}^{q-1}\binom{q-1}{i}\,q\binom{q-1}{i}t^i(1-t)^{q-1-i}\) is a mixture of uniform order-statistic densities: choose \(I\sim\operatorname{Bin}(q-1,1/2)\), then take order statistic \(I+1\) of \(q\) independent uniforms. Its mean is \(1/2\) and variance is \(q/[2(q+1)(q+2)]\), which tends to zero. Therefore \(B_q(t)dt\) converges weakly to point mass at \(1/2\), and for fixed \(p\), \(R(p,q)\to B_p(1/2)=p\binom{2p-2}{p-1}/4^{p-1}\), by Vandermonde's identity.

Put \(m=\min(p,q)\). Coordinatewise monotonicity and symmetry give \(R(p,q)\ge R(m,m)=\int B_m^2\) and \(R(p,q)\le\sup B_m=B_m(1/2)\) (the inequalities also hold for \(m\le2\), with equality). For \(m\ge4\), Chebyshev's inequality and the variance above give probability at least \(1/2\) in the interval \([1/2-1/\sqrt m,\,1/2+1/\sqrt m]\). Cauchy–Schwarz on that interval yields \(\int B_m^2\ge(1/2)^2/(2/\sqrt m)=\sqrt m/8\). Finally the central-binomial asymptotic \(\binom{2m-2}{m-1}/4^{m-1}\sim1/\sqrt{\pi(m-1)}\) gives the claimed sharp-form upper bound and uniform square-root growth.

## Verification
Run `python3 check_biclique_mahler.py` with Python 3, NumPy and SciPy. Exact rational arithmetic verifies independent expansions of the overlap and the published \(h^*\)-specialization for all \(1\le p,q\le12\), checks the equality boundary and all applicable strict monotonicity comparisons, and verifies the constant-term and moment identities. Separately, convex-hull calculations use an orthonormal basis of the zero-sum subspace and compute both primal and polar intrinsic volumes for seven small graph sizes. The printed success markers are `exact_integral_hstar_and_monotonicity_144_pairs PASSED` and `CONVEX_HULL_CHECKS_PASSED 7`. Numerical hulls are finite consistency checks, not proofs of the all-dimensional statements.

## Relationship to prior work
Higashitani, Jochemko and Michałek [1] already give the complete-bipartite \(h^*\)-polynomial, which determines the primal volume. That exact prior formula is used in Step 4; no primal-volume novelty is claimed. Chen, Davis and Korchevskaia [2] describe face/facet subgraphs for symmetric edge polytopes, not the intrinsic dual volume, overlap law, or Mahler inequalities. The polar is also identifiable with the Lipschitz polytope of the graph metric, an established dual description rather than a new polarity. The new contribution consists of the exact polar-volume computation together with the normalized product overlap and its rigid equality threshold, monotonicity and two-scale asymptotics. Related metric-duality terminology may conceal earlier equivalent results; this historical priority is not independently certified.

## Limitations
The theorem applies only to complete bipartite graphs, with canonical root coordinates and intrinsic Euclidean polarity. It does not characterize Mahler products of arbitrary graphs, general metrics, or arbitrary centrally symmetric convex bodies. The constant \(1/8\) in the uniform lower bound is not claimed optimal. The square-root law requires both part sizes to grow; at fixed part size the exact finite limit applies instead. Literature comparison does not establish global historical uniqueness. All mathematical checks described here were made without an independent audit.

## References
[1] A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, first posted 2018-07-20, Theorem 1.1 and Sections 3–4. https://arxiv.org/abs/1807.07678

[2] T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, first posted 2021-07-26, Sections 3–4. https://arxiv.org/abs/2107.12315
