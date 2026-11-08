# Sharp three-moment inverse and conditional volume envelope for rectangular boxes

## Finding
Let \(K=[0,a]\times[0,b]\times[0,c]\subset\mathbb R^3\), with \(a,b,c>0\). For two independent volume-uniform points \(X,Y\in K\), define \(M_j=\mathbb E\|X-Y\|^{2j}\), \(j=1,2,3\). The triple \((M_1,M_2,M_3)\) uniquely recovers the unordered edge lengths of \(K\). More strongly, the exact feasible set of triples is given below, including a sharp, two-phase range for the volume of every box having prescribed \((M_1,M_2)\).

Set
\[
 p_1=6M_1,\quad p_2=\frac{180}{7}(M_2-M_1^2),\quad p_3=\frac{945}{11}(M_3-3M_1M_2+2M_1^3).
\]
The squared edge lengths are exactly the three positive real roots, counted with multiplicity, of
\[
 T^3-p_1T^2+\frac{p_1^2-p_2}{2}T-\frac{p_1^3-3p_1p_2+2p_3}{6}=0.
\]
Define \(q=p_2/p_1^2\), \(r=\sqrt{(3q-1)/2}\), and \(V=abc\). Exactly the following data are feasible:
\[
 M_1>0,\qquad \frac{22}{15}M_1^2\le M_2<\frac{12}{5}M_1^2,
\]
with \(p_1,p_2,p_3\) as above and
\[
 V^2=\frac{p_1^3-3p_1p_2+2p_3}{6}.
\]
If \(0\le r<1/2\), then
\[
 \frac{p_1^3}{27}(1-3r^2-2r^3)\le V^2\le\frac{p_1^3}{27}(1-3r^2+2r^3).
\]
If \(1/2\le r<1\), the exact range is instead
\[
 0<V^2\le\frac{p_1^3}{27}(1-3r^2+2r^3).
\]
All values in the stated intervals occur. Upper volume equality is attained precisely at squared-edge profiles proportional to \((1-r,1-r,1+2r)\). For \(0<r<1/2\), lower volume equality is attained precisely at profiles proportional to \((1+r,1+r,1-2r)\). At \(r=0\) both bounds coincide and only cubes occur. At \(r\ge1/2\), zero volume is approached only through degenerating boxes and is never attained by a positive-volume box. Thus two moments do not generally recover the shape; three suffice, and the cutoff three is generically minimal.

## Assumptions and scope
The ambient metric is Euclidean; the box is a right rectangular solid with mutually orthogonal edges. Both points are independent and uniform with respect to three-dimensional volume. Rigid motions and permutations of side labels do not change the observed law. All positivity and endpoint statements concern \(a,b,c>0\); zero side lengths occur only as excluded limiting configurations. \(M_j\) are population moments, not estimates from a finite sample.

## Proof
Write \(t_1=a^2,t_2=b^2,t_3=c^2\). For two independent uniform random variables \(U,U'\) on \([0,1]\), put \(W=(U-U')^2\). An elementary integration of the triangular difference density gives
\[
 f_W(w)=w^{-1/2}-1\quad (0<w<1),\qquad \mathbb E W^j=\frac{2}{(2j+1)(2j+2)}.
\]
Consequently its first three cumulants are \(\kappa_1(W)=1/6\), \(\kappa_2(W)=7/180\), and \(\kappa_3(W)=11/945\). Independence of Cartesian coordinates gives the *identity in distribution* \(\|X-Y\|^2=\sum_{i=1}^3 t_iW_i\), where the \(W_i\) are independent copies of \(W\). Cumulant additivity and homogeneity then yield
\[
 \kappa_j(\|X-Y\|^2)=\kappa_j(W)\sum_i t_i^j\quad(j=1,2,3).
\]
Using the raw-to-cumulant formulas proves the displayed expressions for \(p_j=\sum_i t_i^j\). Newton's identities give the cubic. Since its three roots are positive and are exactly the \(t_i\), this recovers the box up to permutation.

To describe all feasible pairs \((M_1,M_2)\), normalize \(w_i=t_i/p_1\). Then \(w_i>0\), \(\sum_iw_i=1\), and \(\sum_iw_i^2=q\). The elementary Cauchy bound and strict positivity yield \(1/3\le q<1\), equivalent to the displayed moment-ratio bounds. Every such \(q\) is realized, for instance, by \(w=((1-r)/3,(1-r)/3,(1+2r)/3)\) with \(0\le r<1\).

At fixed \(q\), the feasible weights form the positive portions of the circle cut from the plane \(\sum w_i=1\) by the sphere \(\sum w_i^2=q\). Maximizing or minimizing \(g=\prod_iw_i\) in its interior yields the Lagrange equation \(1/w_i=\lambda+2\mu w_i\). Thus each stationary profile has at most two distinct weights. The only two such profiles up to permutation are
\[
 w^+=((1-r)/3,(1-r)/3,(1+2r)/3),\quad
 w^-=((1+r)/3,(1+r)/3,(1-2r)/3).
\]
The first is positive for all \(r<1\); the second is positive precisely when \(r<1/2\). Their products are respectively \((1-3r^2+2r^3)/27\) and \((1-3r^2-2r^3)/27\). For \(r<1/2\) the entire constraint circle is positive, so compactness and the stationary classification establish the closed range between these two products. For \(r\ge1/2\), feasible arcs terminate at profiles with one zero coordinate. The product approaches zero at those endpoints, while its positive maximum is attained at \(w^+\); continuity on each feasible arc supplies every intervening value. This proves the precise ranges and equality classes after multiplying by \(p_1^3\).

For generic minimality, the distinct positive triples of squared sides \(p_1w^+\) and \(p_1w^-\), whenever \(0<r<1/2\), have identical first two power sums and therefore identical \((M_1,M_2)\), but have different products and consequently different \(M_3\). Three moments are therefore needed on a nonempty open set of first-two-moment values. In the cube case \(r=0\), two moments do suffice, so the claim is *generic* rather than pointwise minimality.

## Verification
The included standalone algebraic checker `check_cuboid.py` reproduces the cumulants from exact rational moments, symbolically expands \(\mathbb E\|X-Y\|^2\), \(\mathbb E\|X-Y\|^4\), and \(\mathbb E\|X-Y\|^6\), checks Newton inversion for four positive profiles, establishes a noncongruent two-moment collision, and checks the endpoint factorizations. Supplemental random tests examined 12,000 positive triples for the sharp envelope and simulated 450,000 pairs in each of three boxes. Successful output: `CUBOID_INVERSE_OK exact_cumulants=3 inverse_shapes=4 nonunique_pair=1 envelope_samples=12000 direct_sample_shapes=3 samples_each=450000`. The exhaustive statements are established by the analytic proof, not by finite sampling.

## Relationship to prior work
Johan Philip, *The Probability Distribution of the Distance between Two Random Points in a Box* (2007), gives an explicit **forward** distance distribution for a three-dimensional rectangular box using convolution; its listed density breakpoints involve squared edges and their sums. Mathai, Moschopoulos, and Pederzoli (1999) treated random distances in a cube, including arbitrary forward moments. Their forward formulas are not claimed to be new here, and the complete distance histogram can already encode shape information. The distinct result here is an exact **finite three-moment reconstruction**, its generic optimality, and the complete sharp volume-feasibility interval conditioned on the first two moments, including the unattained boundary transition at \(q=1/2\). Clement (arXiv:1312.5292, first posted 2013-12-18) studies trajectories through boxes using different sampling measures. Holmin, Kurlberg, and Månsson (arXiv:1702.08096, posted 2017-02-26) recover box sides from discontinuities of **random line-intercept / billiard free-path** distributions, not the three independent interior-point distance moments studied here. The existence of these closely related inverse problems motivates distinguishing the underlying sampling law.

## Limitations
The theorem does not concern arbitrary skew parallelepipeds, unknown nonuniform point densities, intrinsic boundary distances, or finite-sample statistical stability. It does not establish novelty independently of all unindexed or historical literature; the finite-moment inverse and conditional-volume formulas should be assessed against additional specialized references. The analytic proof is self-contained; numerical tests cannot establish infinite or all-parameter claims.

## References
- J. Philip, *The Probability Distribution of the Distance between Two Random Points in a Box*, Royal Institute of Technology report TRITA MAT 07 MA 10 (December 2007), author-hosted text: https://people.kth.se/~johanph/habc.pdf.
- A. M. Mathai, P. Moschopoulos, G. Pederzoli, *Distance between random points in a cube*, Statistica 59 (1999), 61–81, https://doi.org/10.6092/issn.1973-2201/1104.
- G. T. Clement, *Joint probability density functions of random trajectories through a box*, arXiv:1312.5292, initial release 2013-12-18, https://arxiv.org/abs/1312.5292.
- S. Holmin, P. Kurlberg, D. Månsson, *On the free path length distribution for linear motion in an n-dimensional box*, arXiv:1702.08096, initial release 2017-02-26, https://arxiv.org/abs/1702.08096.
