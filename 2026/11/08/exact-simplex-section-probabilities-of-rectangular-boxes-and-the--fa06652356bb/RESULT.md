# Exact simplex-section probabilities of rectangular boxes and the complete affine-cube polygon law

## Finding

**Theorem (a sharp all-dimensional law and its three-dimensional specialization).** Fix an integer \(d\ge3\) and positive side lengths \(a_1,\ldots,a_d\). Put \(B=\prod_{i=1}^d[0,a_i]\). Draw an affine hyperplane in \(\mathbb R^d\) from Euclidean-motion-invariant hyperplane measure, conditioned to meet \(B\). Let \(N\) denote the number of vertices of the almost-surely nondegenerate section \(B\cap H\). Then the exact probability that the section is a \((d-1)\)-simplex is
\[
\boxed{\Pr(N=d)=\frac{\sqrt{2\pi}}{\sum_{i=1}^d a_i}\int_0^\infty\prod_{i=1}^d \operatorname{erfc}\!\left(\frac{t}{\sqrt2\,a_i}\right)\,dt.}
\]
The function is symmetric and strictly Schur-concave in the side lengths at fixed sum. Hence the unique maximizer, up to uniform scaling, is the cube. Its sharp probability \(p_d^*\) satisfies
\[
\boxed{p_d^*=\frac{\sqrt{2\pi}}d\int_0^\infty\operatorname{erfc}\!\left(\frac{t}{\sqrt2}\right)^d dt,\qquad\lim_{d\to\infty}d^2p_d^*=\pi.}
\]
For the unit cube in dimension three the **entire** polygon-type distribution is explicit. Define
\[
q_3=2-\frac{4\sqrt2}{\pi}\arctan\sqrt2,\qquad
q_6=\frac{2\sqrt3}{3}-\frac{4\sqrt2}{\pi}\arctan\frac1{\sqrt2},
\]
\[
q_5=q_3-2q_6,\qquad q_4=1-2q_3+q_6.
\]
Then \(\Pr(N=j)=q_j\) for \(j=3,4,5,6\), and all other values have probability zero. Numerically,
\[
(q_3,q_4,q_5,q_6)=(0.279825723213,\ 0.486796243994,\ 0.186930342373,\ 0.046447690420).
\]
In particular, \(\mathbb E[N]=4\); this expectation is previously known under uniform random affine-section sampling, whereas the displayed complete probability vector and the simplex-event shape optimization are the asserted refinements.

## Assumptions and scope

An unoriented hyperplane can be represented as \(H(u,s)=\{x:u\cdot x=s\}\) with \(u\in S^{d-1}\), \(s\in\mathbb R\), identifying \((u,s)\) and \((-u,-s)\). Its motion-invariant measure is a constant multiple of \(d\sigma(u)\,ds\), where \(d\sigma\) is spherical area. **Conditioning on intersection with the box weights the normal direction in proportion to the box's width** \(w(u)=\sum_i a_i|u_i|\). It is not the model that first chooses a Haar-uniform normal and *then* independently chooses a uniform intercept for that normal. The measure-zero planes through vertices or containing edges are excluded. A \((d-1)\)-dimensional section is a simplex if and only if it has exactly \(d\) vertices.

There are no restrictions on side lengths beyond strict positivity. The three-dimensional formulas refer to ordinary planar polygon sections of a cube, not central sections or shadows.

## Proof

**1. The simplex event is exactly a singleton-vertex cut.** Reflect coordinates so that the coordinates of a generic normal have positive signs. A hyperplane section of the box has one vertex for each intersected box edge. Orient the edge graph of the box from the lower to the higher projected vertex level. For an intercept between projected vertex levels, the crossed box edges are the edge boundary of a proper nonempty vertex subset \(S\) of the \(d\)-cube graph.

For \(d\ge3\), any nontrivial edge cut in the \(d\)-cube has at least \(d\) edges, and equality occurs only when \(S\) or its complement is a singleton. For completeness, prove this by induction on \(d\). The case \(d=3\) follows by partitioning vertices into the two square faces: each proper nonempty face-subset contributes at least two internal boundary edges, while edges between faces count its symmetric difference. A cut of three edges therefore isolates a single vertex. For the induction step, write \(S=S_0\sqcup S_1\) in the two opposite \((d-1)\)-faces, and note
\[
|\partial S|=|\partial S_0|+|\partial S_1|+|S_0\triangle S_1|.
\]
If both face-subsets are proper and nonempty, the first two terms sum to at least \(2(d-1)>d\) for \(d\ge4\). If a face-subset is empty or full, either the separating contribution is at least \(2^{d-1}>d\), or induction gives at least \(d-1\) internal crossings and at least one separating crossing. Equality then forces precisely a singleton or a complementary singleton. Thus the minimum cut classification holds.

For a fixed normal \(u\), the interval of intercepts cutting off the unique minimum-projection vertex has length \(m(u)=\min_i a_i|u_i|\). The analogous interval near the maximum-projection vertex has the same length. The equality cases are null sets, so the total intercept measure yielding a simplex is exactly \(2m(u)\). The total admissible intercept measure is \(w(u)\). Consequently,
\[
\Pr(N=d)=\frac{2\,\mathbb E_{U\sim\mathrm{Haar}}\min_i a_i|U_i|}{\mathbb E_{U\sim\mathrm{Haar}}\sum_i a_i|U_i|}.
\]

**2. Gaussian minimum integral.** Let \(G_i\) be independent standard normal random variables, put \(R=(\sum_iG_i^2)^{1/2}\), and \(U=G/R\). The direction \(U\) is Haar-uniform and independent of \(R\). Taking expectations in the homogeneous degree-one numerator and denominator above cancels \(\mathbb E R\). Since \(\mathbb E|G_1|=\sqrt{2/\pi}\) and
\[
\mathbb E\min_i(a_i|G_i|)=\int_0^\infty\Pr\{a_i|G_i|>t\text{ for all }i\}\,dt
=\int_0^\infty\prod_i\operatorname{erfc}\left(\frac{t}{\sqrt2 a_i}\right)dt,
\]
the exact formula follows. The interchange uses Tonelli's theorem on a nonnegative integrand.

**3. Unique cubic optimality among boxes.** For each fixed nonnegative vector \(x\), the function \(a\mapsto\min_i a_ix_i\) is concave as the pointwise minimum of affine functions. Averaging over Haar directions preserves concavity, and exchangeability of the coordinate absolute values makes the expectation symmetric. It is strictly increased by replacing any unequal pair \((a_i,a_j)\) by its arithmetic mean twice: write the two transposed side-length vectors, apply the concavity inequality, and note strictness on the positive-measure set where \(|U_i|\) and \(|U_j|\) are sufficiently close and both small enough that the other positive-coordinate products exceed these two. On this set the active minimum switches under swapping the unequal pair. The denominator \(\mathbb E\sum_i a_i|U_i|\) depends only on \(\sum_i a_i\); thus the simplex probability is strictly Schur-concave at fixed sum. Averaging unequal pairs leads to the equal-length maximizer and proves uniqueness.

**4. The dimensional asymptotic.** For equal side lengths, put \(Q(t)=\Pr\{|G_1|>t\}=\operatorname{erfc}(t/\sqrt2)\). Since \(Q(t)=1-\sqrt{2/\pi}\,t+O(t^3)\) at zero and \(Q(t)\) has a Gaussian tail, a change of variables \(t=s/d\) followed by dominated convergence (split first at \(s=d\)) gives
\[
\lim_{d\to\infty}d\int_0^\infty Q(t)^d\,dt=\sqrt{\pi/2}.
\]
Multiplying by \(\sqrt{2\pi}/d\) proves the sharp limit \(d^2p_d^*\to\pi\).

**5. The cubic polygon spectrum: combinatorial reduction.** For the unit cube and an octant-normal with absolute components sorted as \(a\ge b\ge c>0\), let \(L_j(u)\) be the total intercept length producing \(j\) section vertices. The projected cube-vertex levels are the eight subset sums of \(a,b,c\). When \(a<b+c\), the successive polygon types are \(3,4,5,6,5,4,3\); otherwise they are \(3,4,5,4,5,4,3\). Hence
\[
L_3(u)=2c=2\min_i|u_i|,\qquad L_6(u)=(b+c-a)_+.
\]
The sum of lengths is \(a+b+c\). Moreover each of the twelve cube edges contributes its projected length to the integrated section-vertex count, giving \(\sum_j jL_j(u)=4(a+b+c)\) **for each normal**. Therefore \(\mathbb E[N]=4\), and with \(q_3+q_4+q_5+q_6=1\), one has \(q_5+2q_6=q_3\). It remains to evaluate \(q_3\) and \(q_6\).

**6. Exact triangular probability.** The orientational average of the smallest absolute normal coordinate is \(\frac{12}{\pi}I\), where
\[
I=\int_{0\le x\le y\le z,\ x^2+y^2+z^2=1}x\,d\sigma
=\frac12\int_{\pi/4}^{\pi/2}\frac{\cos^2\theta}{1+\cos^2\theta}\,d\theta
=\frac\pi8-\frac{\arctan\sqrt2}{2\sqrt2}.
\]
For the first integral, project the ordered spherical octant onto the \((y,z)\)-plane: \(x\,d\sigma=dy\,dz\), the polar angle ranges from \(\pi/4\) to \(\pi/2\), and the radial lower bound is \((1+\cos^2\theta)^{-1/2}\). Since \(\mathbb E\sum_i|U_i|=3/2\), the formula \(q_3=2-4\sqrt2\arctan\sqrt2/\pi\) follows.

**7. Exact hexagonal probability.** On the ordered positive spherical region
\[
\Omega=\{(x,y,z)\in S^2:x\ge y\ge z\ge0,\ x<y+z\},
\]
the hexagonal-intercept length is \(f=y+z-x\). The region is a spherical triangle with vertices \((1,1,1)/\sqrt3\), \((1,1,0)/\sqrt2\), \((2,1,1)/\sqrt6\). Write \(\eta=\arctan(1/\sqrt2)\). The geodesic side \(x=y\) has length \(\eta\), and the side \(x=y+z\) has length \(\pi/6\). Since \(\Delta_{S^2} f=-2f\), the spherical divergence theorem gives
\[
\int_\Omega f\,d\sigma
=\frac12\left(\sqrt3\,\frac\pi6-\sqrt2\,\eta\right).
\]
Indeed, the outward unit normals to the three geodesic boundary arcs \(x=y\), \(y=z\), and \(x=y+z\) have directional derivatives of \(f\) equal to \(\sqrt2\), \(0\), and \(-\sqrt3\), respectively. The six coordinate orders and eight octants give factor \(48/(4\pi)=12/\pi\) for the orientational average. Divide by \(\mathbb E(a+b+c)=3/2\) to find \(q_6=2\sqrt3/3-4\sqrt2\eta/\pi\). The other two probabilities follow from normalization and the established first moment. \(\square\)

## Verification

The standalone `verify.py` requires Python 3 standard library only. Execute `python3 verify.py` in a directory containing the file. It checks all 1331 integer triples of side-direction products in the range one through eleven, 120 high-dimensional generic configurations in dimensions three through six, independent quadrature of the one-dimensional minimum integral, analytic probability normalization and first moments, and width-weighted Gaussian-normal numerical integration over 600,000 sampled directions. The output ends with `CUBE_AFFINE_CROFTON_VERIFICATION_OK`. Separately, 2,000,000 random cube-section normal/intercept pairs were evaluated by enumerating intersected edges, with deviations below \(0.00011\) from the four stated probabilities. These finite checks do not substitute for the analytic all-dimensional proof.

## Relationship to prior work

Lonke's arXiv:math/9812123 studies Haar-random **central linear** sections of cubes; its exact mean-face results cannot be substituted for translated Crofton hyperplanes. Marichal and Mossinghoff's arXiv:math/0607715 gives exact **volume** formulas for fixed cube halfspace slices and hyperplane sections, not the rotation-translation-averaged distribution of polygon types. Swan's arXiv:1808.09482 proves the exact expected number of vertices for Crofton-random affine cube sections and even parallelotopes; the mean \(4\) for a three-cube is therefore **prior art**, not asserted as new. These facts constrain the scope of the claim. A published central-section cuboid hexagon probability is similarly a distinct experiment, because the translation coordinate is held at zero. The contribution asserted here is the minimum-face-event probability and strict shape law in arbitrary dimension, its sharp \(\pi/d^2\) asymptotic, and the full noncentral cube polygon distribution.

## Limitations

The sampled hyperplanes use Euclidean-motion-invariant measure conditioned to meet the box; conclusions do not transfer to Haar-uniform normals followed by independent uniform intercepts. The all-dimensional theorem determines the probability of simplex sections, not full section-face vectors in dimensions four and above. The four-point polygon distribution is exact only for the three-dimensional cube. The maximization concerns **orthogonal boxes** with positive lengths and fixed sum, not arbitrary parallelotopes or general convex bodies. Searching indexed records cannot establish absolute historical novelty; obscure stereological tables or unpublished analyses may contain equivalent special cases. No independent mathematical audit is asserted.

## References

1. Y. Lonke, *On random sections of the cube*, initial arXiv public version 1998-12-21, arXiv:math/9812123; *Discrete & Computational Geometry* 23 (2000), 157–169. https://arxiv.org/abs/math/9812123.
2. J.-L. Marichal and M. J. Mossinghoff, *Slices, slabs, and sections of the unit hypercube*, initial arXiv public version 2006-07-27, arXiv:math/0607715; *Online Journal of Analytic Combinatorics* 3 (2008), 1–11. https://arxiv.org/abs/math/0607715.
3. H. Swan, *Expected Number of Vertices of a Hypercube Slice*, initial arXiv public version 2018-08-28, arXiv:1808.09482. https://arxiv.org/abs/1808.09482.
