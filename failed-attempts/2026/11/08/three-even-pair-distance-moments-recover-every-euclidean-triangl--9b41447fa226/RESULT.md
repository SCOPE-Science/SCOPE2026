# Three even pair-distance moments recover every Euclidean triangle: a sharp moment region

## Finding

Let \(T\) be any nondegenerate Euclidean triangle, and let \(X,Y\) be independent area-uniform points of \(T\). Set \(M_k=\mathbb E\|X-Y\|^{2k}\) for \(k=1,2,3\). Denote the three **squared** side lengths by \(x,y,z\), and their elementary symmetric polynomials by \(e_1=x+y+z\), \(e_2=xy+xz+yz\), and \(e_3=xyz\). Then

\[
M_1=\frac{e_1}{18},\qquad
M_2=\frac{e_1^2-2e_2}{60},\qquad
M_3=\frac{23e_1^3-62e_1e_2+20e_3}{4200}.
\]

Consequently the first three even moments of the distance determine the triangle uniquely up to Euclidean congruence, without labeled points or known scale. The explicit inverse is

\[
e_1=18M_1,\qquad e_2=\frac{e_1^2-60M_2}{2},\qquad
 e_3=\frac{4200M_3-23e_1^3+62e_1e_2}{20}.
\]

The unordered squared sides are precisely the roots of \(u^3-e_1u^2+e_2u-e_3\). This is a **sharp minimality result**: the first two moments never distinguish all triangles except at the equilateral moment pair.

Here is the complete feasible region for the first two moments and for the third moment conditional on them. Necessarily and sufficiently,

\[
M_1>0,\qquad \frac95M_1^2\le M_2<\frac{27}{10}M_1^2.
\]

For such a pair, set \(r=\sqrt{e_1^2-3e_2}\), using the inverse formulas above, and

\[
e_{3,\pm}=\frac{e_1(9e_2-2e_1^2)\pm2r^3}{27},\qquad
M_{3,\pm}=\frac{23e_1^3-62e_1e_2+20e_{3,\pm}}{4200}.
\]

Exactly the **closed** interval \(M_{3,-}\le M_3\le M_{3,+}\) is realized by nondegenerate Euclidean triangles with those first two moments. At its endpoints, two squared sides coincide; except when \(r=0\), the two endpoint triangles are distinct. Every intermediate value is attained, and each admissible triple determines exactly one triangle congruence class. Equivalently, a proposed moment triple is realizable exactly when the above first-two conditions and third-moment interval hold.

Already the first two moments recover the ordinary area \(\mathcal A\) by the exact identity

\[
\mathcal A^2=\frac{81}{4}M_1^2-\frac{15}{2}M_2.
\]

## Assumptions and scope

The parent triangle has three positive side lengths satisfying strict triangle inequalities; no acuteness or special symmetry assumption is made. Sampling is independent and uniform with respect to ordinary two-dimensional area, **not** boundary arclength and not a chord process conditioned on a random intersecting line. The moments are raw powers of the Euclidean distance, not centered moments, and the reconstruction is up to rigid motions including reflections. Three moments mean the moments of orders two, four, and six in distance.

## Proof

Label the triangle vertices \(v_1,v_2,v_3\). The barycentric coordinates \(\Lambda=(\Lambda_1,\Lambda_2,\Lambda_3)\) and \(\Mu=(\Mu_1,\Mu_2,\Mu_3)\) of the independent points are independent Dirichlet\((1,1,1)\) vectors. Put \(d_i=\Lambda_i-\Mu_i\); then \(\sum_i d_i=0\). The Euclidean polarization identity gives exactly

\[
\|X-Y\|^2=-x d_2d_3-y d_1d_3-z d_1d_2.
\]

For nonnegative integers \(k_1,k_2,k_3\), direct integration of the constant-density barycentric simplex shows

\[
\mathbb E\prod_{i=1}^3\Lambda_i^{k_i}
=\frac{2\prod_i k_i!}{(2+\sum_i k_i)!}.
\]

Expanding the first, second and third powers of the polarization identity and applying this factorial rule twice gives, without geometric approximation,

\[
\begin{aligned}
\mathbb E\|X-Y\|^{2}&=(x+y+z)/18,\\
\mathbb E\|X-Y\|^{4}&=(x^2+y^2+z^2)/60,\\
\mathbb E\|X-Y\|^{6}&=
[23(x^3+y^3+z^3)+7\sum_{i\ne j}x_i^2x_j-28xyz]/4200.
\end{aligned}
\]

The last expression equals \((23e_1^3-62e_1e_2+20e_3)/4200\) by Newton's identities. These equations are triangular in \(e_1,e_2,e_3\), with nonzero coefficient of each newly introduced invariant, proving the stated inverse and its uniqueness.

Heron's identity, applied to the positive square roots of \(x,y,z\), says \(16\mathcal A^2=4e_2-e_1^2\). It follows from the moment equations that the area formula holds. Since \(x,y,z>0\) and the triangle inequalities are strict, \(4e_2>e_1^2\). Also \(e_2\le e_1^2/3\), with equality only for \(x=y=z\). Translating these two inequalities proves the asserted first-two-moment region. Every admissible value occurs on the continuous isosceles family \(x=y=(e_1+r)/3\), \(z=(e_1-2r)/3\), where \(r\) varies from zero to just below \(e_1/2\).

Fix an admissible \(e_1,e_2\). The equations \(x+y+z=e_1\) and \(x^2+y^2+z^2=e_1^2-2e_2\) cut out a circle in the affine plane (a point when \(r=0\)). The smallest coordinate anywhere on that circle is \((e_1-2r)/3>0\), because \(e_2>e_1^2/4\). Every triple on the circle therefore has positive coordinates and satisfies Heron's strict triangle condition. It represents a genuine triangle.

The continuous product \(xyz\) attains its extrema on the compact circle. At an extremum, Lagrange multipliers for fixed sum and sum of squares (whose constraint gradients are independent when \(r>0\)) imply \(1/t=\alpha+2\beta t\) for each \(t\in\{x,y,z\}\), by differentiating \(\log(xyz)\). But the quadratic equation \(2\beta t^2+\alpha t-1=0\) has at most two roots; hence at least two coordinates coincide. Thus extrema are isosceles triples. The two possibilities are the permutations of

\[
\left(\frac{e_1+r}{3},\frac{e_1+r}{3},\frac{e_1-2r}{3}\right)
\quad\text{and}\quad
\left(\frac{e_1-r}{3},\frac{e_1-r}{3},\frac{e_1+2r}{3}\right).
\]

Their products are \(e_{3,-}\) and \(e_{3,+}\) respectively. Connectedness of the feasible circle supplies every intermediate product, and the positive coefficient \(20/4200\) transfers the exact interval to \(M_3\).

For an explicit demonstration that two moments do not suffice when \(r>0\), take the two isosceles squared-side multisets

\[
(2+1/\sqrt3,2+1/\sqrt3,2-2/\sqrt3)
\quad\text{and}\quad
(2-1/\sqrt3,2-1/\sqrt3,2+2/\sqrt3).
\]

Both are nondegenerate, have \(e_1=6\) and \(e_2=11\), hence \(M_1=1/3\), \(M_2=7/30\), but their sixth moments differ by \(2/(315\sqrt3)>0\). More generally, the two distinct conditional endpoints prove the necessity of the third moment for every nonequilateral feasible first-two pair.

## Verification

The accompanying `verify.py` regenerates all three moment polynomials with exact rational Dirichlet factorial arithmetic, checks the inverse and Heron substitutions symbolically, verifies the two noncongruent extremal examples and the algebraic endpoint construction, and separately compares formulas against direct coordinate-based random sampling for eight triangles with 180,000 independent pairs each. Exact algebra, not simulation, proves the theorem. The observed verification line was `PAIR_TRIANGLE_INVERSE_OK exact_polynomials=3 inverse=3 conditional_envelope=2 isosceles_pair=2 monte_carlo_shapes=8 samples_each=180000`.

## Relationship to prior work

The random distance law for two interior-uniform points in an arbitrary triangle was developed by Tong, Ahmadi and Pan (2013), with follow-up computational work by Tong and Pan (2016). A general formula for **all** distance moments for such point pairs is already given in Proposition 4 of *Moments of volumes of lower-dimensional random simplices are not monotone* (2017). Consequently, **the existence of explicit moments and the three displayed forward moment polynomials are not separately claimed as new**: they follow by specializing known general moment formulas (and are independently rederived here for transparency).

The specific mathematical assertion is instead the *minimal finite inverse theorem*, together with the **complete sharp conditional moment region**, endpoint classification and simple two-moment area reconstruction. The cited prior statements compute forward moments or distributions from specified geometry; they do not in their inspected statements classify which triples of low-order distance moments identify a triangle, or characterize the feasible moment region. Earlier regular-polygon results, such as Bäsel's 2012 work, apply to more symmetric subfamilies rather than this arbitrary-triangle inverse classification.

## Limitations

No stability bound under noisy, empirically estimated moments is claimed: near repeated squared-side roots, the inverse is poorly conditioned. The theorem does not extend to arbitrary polygons, higher-dimensional simplices, weighted sampling or boundary-uniform sampling. The 2013 preprint's accessible online representation was incomplete in the inspected retrieval, so its uninspected portions remain a historical-priority risk. The general 2017 forward-moment formula is directly relevant and acknowledged. Priority beyond the searched and inspected sources has not been independently established; this is a mathematical proof with a self-review, not an independent audit.

## References

1. F. Tong, M. Ahmadi, and J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498, first posted 2013-11-29. https://arxiv.org/abs/1312.2498
2. F. Tong and J. Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407, first posted 2016-01-21. https://arxiv.org/abs/1602.03407
3. *Moments of volumes of lower-dimensional random simplices are not monotone*, *Monatshefte für Mathematik*, Proposition 4 (general moments for two uniform points in an arbitrary triangle), DOI:10.1007/s00605-017-1077-3. https://link.springer.com/article/10.1007/s00605-017-1077-3
4. H. Li and X. Qiu, *Moments of Distance from a Vertex to a Uniformly Distributed Random Point within Arbitrary Triangles*, *Mathematical Problems in Engineering* (2016), DOI:10.1155/2016/8371750. https://onlinelibrary.wiley.com/doi/10.1155/2016/8371750
5. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first posted 2012-04-12. https://arxiv.org/abs/1204.2707
