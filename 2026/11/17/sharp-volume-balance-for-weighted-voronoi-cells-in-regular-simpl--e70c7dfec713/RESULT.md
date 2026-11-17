# Sharp volume balance for weighted Voronoi cells in regular simplices

## Finding
Let \(d\ge 2\) and let \(P\) be a Euclidean regular \(d\)-simplex with vertices indexed by \(I=\{0,\ldots,d\}\). For an arbitrary interior point \(B\), write its barycentric coordinates as \(b_j>0\), \(\sum_{j\in I}b_j=1\). For each vertex \(i\), take the convex hull \(C_i(B)\) of the perpendicular feet of \(B\) on the affine hulls of **all** faces containing vertex \(i\), including the vertex and \(P\) itself.

**Theorem.** In the canonical side-length \(\sqrt2\) realization, set the power weights of the vertex sites \(e_i\) to \(w_i=-2b_i\). For an arbitrary Euclidean regular simplex of edge length \(L\), the equivalent physical weights are \(w_i=-L^2b_i\). The resulting power diagram restricted to \(P\) has cells \(C_i(B)\). Every point of the interior of \(P\) lies in its orthogonal kernel. Each \(C_i(B)\) is a full-dimensional combinatorial \(d\)-cube with precisely the \(2^d\) face-projection feet as vertices. These \(d+1\) cells tile \(P\) face-to-face and are exactly the restrictions of the translated vertex-normal cones. Their normalized Euclidean volumes are the following explicit homogeneous polynomials:

\[
p_i(b):=\frac{\operatorname{vol}_d(C_i(B))}{\operatorname{vol}_d(P)}
=\sum_{S\subseteq I\setminus\{i\}}\frac{(-1)^{|S|}}{|S|+1}
\left(1-b_i-\sum_{j\in S}b_j\right)^d.
\]

For fixed \(b_i=t\in(0,1)\), the function \(p_i\) is **strictly Schur-concave** in the remaining \(d\) barycentric coordinates. In particular, with \(s=1-t\), its exact extremal interval over interior poles is

\[
\boxed{\frac{s^d}{d}<p_i(b)\le\frac{(d+1)^{d-1}}{d^d}s^d.}
\]

Equality at the upper bound occurs if and only if every other barycentric coordinate equals \(s/d\). The lower bound is a sharp infimum, approached when all remaining mass tends to one other vertex, and is not attained by an interior pole. The ratio of the sharp upper and lower constants is \((1+1/d)^{d-1}\), which increases to \(e\) as \(d\to\infty\). No extension to irregular simplices is asserted.

## Assumptions and scope
A regular simplex is congruent after a common scale change to \(\Delta_d=\{x\in\mathbb R^{d+1}:x_j\ge0,\ \sum_jx_j=1\}\), with its inherited Euclidean metric. Use this realization. Here \(B=b\), a face indexed by a nonempty \(T\subseteq I\) is \(F_T=\{x\in\Delta_d:x_j=0\text{ for }j\notin T\}\), and \(F_I=P\). All projected feet are relative-interior points because every \(b_j\) is strictly positive. With physical side length \(L\), squared distance differences are \(\|x-v_i\|^2-\|x-v_j\|^2=-L^2(x_i-x_j)\), which checks the physical weight scaling. The power-cell convention in our canonical coordinates is \(x\in C_i(B)\) when \(\|x-e_i\|^2-w_i\le\|x-e_j\|^2-w_j\) for every \(j\); since all vertex norms are one, this is equivalent to \(x_i-b_i\ge x_j-b_j\). The weight normalization is essential: adding a common constant to all weights leaves the diagram unchanged. A cell is a geometric, not necessarily metric, cube: its face poset is that of the standard \(d\)-cube. Schur-concavity means that any nontrivial equalizing transfer between two of the other coordinates strictly **increases** the cell-volume fraction; equivalently, strict majorization away from coordinate permutations decreases it.

## Proof
**1. Orthogonal projections and the full kernel.** The orthogonal projection of \(b\) onto the affine span of \(F_T\) has coordinates
\[
q_T(b)_j=\begin{cases}
 b_j+\frac{1}{|T|}\sum_{k\notin T}b_k,&j\in T,\\
0,&j\notin T.
\end{cases}
\]
The formula follows by least squares with the single constraint that the coordinates in \(T\) sum to one. Its coordinates in \(T\) are positive. Hence every interior \(b\) projects into the relative interior of every face, so the orthogonal kernel is exactly \(\operatorname{int}\Delta_d\).

**2. The exact cells and their vertices.** The normal cone at vertex \(e_i\), in the direction space of the simplex, consists of the vectors whose \(i\)-th coordinate is maximal. Hence its translate at \(b\), restricted to \(\Delta_d\), is
\[
D_i(b)=\left\{x\in\Delta_d:x_i-b_i\ge x_j-b_j\ \text{for all }j\in I\right\}.
\]
At any \(x\in\Delta_d\), the deviations sum to zero, so their maximum is nonnegative. Put \(T=\{j:x_j-b_j=x_i-b_i\}\) and \(Z=\{j:x_j=0\}\). If \(x\in D_i(b)\), the two sets are disjoint (at a zero coordinate the deviation is \(-b_j<0\)). The potentially active facet inequalities at \(x\) are precisely \(|T|-1\) tie conditions and \(|Z|\) zero-coordinate conditions. For a vertex, at least \(d\) independent conditions are necessary. Since \(T\cap Z=\varnothing\), there are at most \(d\); equality forces \(T\cup Z=I\), and the unique solution is exactly \(q_T(b)\) with \(i\in T\). Conversely, at every such \(q_T(b)\), the \(d\) selected tie-or-zero equations are linearly independent on \(\sum x_j=1\), so \(q_T(b)\) is a vertex. Thus \(D_i(b)=\operatorname{conv}\{q_T(b):i\in T\}=C_i(B)\). Each of the \(d\) other indices independently chooses a zero-coordinate facet or an equal-deviation facet, and these paired facets have the cube incidence pattern. The cells cover \(P\) because every vector of deviations has a maximizing index. Two cells meet along common supporting hyperplanes of tied maxima; hence the tiling is face-to-face.

**3. Exact volume.** Let \(X\) be uniform in \(\Delta_d\), equivalently \(\operatorname{Dirichlet}(1,\ldots,1)\). Its cell label \(i\) is the unique maximizer of \(X_j-b_j\), almost surely. Writing \(u=X_i-b_i\ge0\), the remaining coordinates have sum \(1-b_i-u\) and must obey \(X_j\le b_j+u\). Inclusion-exclusion for the truncated simplex gives the cross-section density
\[
d\sum_{S\subseteq I\setminus\{i\}}(-1)^{|S|}
\left(1-b_i-\sum_{j\in S}b_j-(1+|S|)u\right)_+^{d-1}.
\]
Integration over \(u\ge0\), using \(\int_0^\infty d(A-cu)_+^{d-1}\,du=A^d/c\) for \(A\ge0,c>0\), proves the displayed subset polynomial. This is a probability, so it is the normalized Euclidean cell volume regardless of the common side-length scale.

**4. Strict pairwise balancing.** Fix \(i\) and two different indices \(j,k\ne i\), holding \(b_i\), all other \(b\)'s, and \(B_0=b_j+b_k>0\) fixed. Fix \(u=X_i-b_i\) and every \(X_\ell\) for \(\ell\notin\{i,j,k\}\), so the residual available to \(X_j,X_k\) is \(r\ge0\). Conditional on these values the length of the feasible segment for \(X_j\) is
\[
\left|[0,r]\cap[r-b_k-u,\ b_j+u]\right|.
\]
The second interval has fixed length \(B_0+2u-r\) and midpoint \(r/2+(b_j-b_k)/2\). Its overlap length with the centered interval \([0,r]\) is nonincreasing with \(|b_j-b_k|\), and symmetric in the sign. All other eligibility constraints are independent of the split. Integrating proves pairwise-balancing monotonicity.

For strictness, assume for example \(b_j>b_k\), and take the other \(X_\ell\)'s near their respective \(b_\ell\)'s and \(u\) in a small open interval strictly between \(B_0/4\) and \(B_0/4+(b_j-b_k)/4\). At their central values, \(r=B_0-u\); equalizing \(b_j,b_k\) makes both caps \(B_0/2+u\) at least \(r\), while the smaller original cap \(b_k+u\) is less than \(r\). Both comparisons persist on a positive-volume neighborhood, and the centered overlap is strictly longer. Therefore every nontrivial pair balancing strictly increases \(p_i\). Repeated balancing and the standard characterization of majorization by such transfers yield strict Schur-concavity.

**5. Sharp constants.** By strict Schur-concavity the upper extremizer at fixed \(b_i=t\) is \(b_j=s/d\) for all \(j\ne i\). Substitution into the volume polynomial yields
\[
\frac{s^d}{d^d}\sum_{k=0}^d\frac{(-1)^k}{k+1}\binom dk(d-k)^d
=\frac{(d+1)^{d-1}}{d^d}s^d.
\]
The equality is the vanishing \((d+1)\)-st finite difference of the degree-\(d\) polynomial \(z^d\), together with \(\binom dk/(k+1)=\binom{d+1}{k+1}/(d+1)\). At an extreme vector of the closed \(d\)-coordinate simplex, one other coordinate is \(s\) and all remaining are zero. The polynomial reduces to
\[
s^d\sum_{k=0}^{d-1}\frac{(-1)^k}{k+1}\binom{d-1}{k}=\frac{s^d}{d},
\]
using the binomial integral of \((1-z)^{d-1}\) over \([0,1]\). Strict Schur-concavity proves no interior pole attains the lower extreme. Finally \(d\,(d+1)^{d-1}/d^d=(1+1/d)^{d-1}\to e\).

## Verification
A standalone standard-library checker is included as `verify_simplex.py`. It compares the inclusion-exclusion polynomial with **independently computed exact rational determinant volumes**: each cubical cell is triangulated into \(d!\) flag simplices with vertices \(q_{\{i\}},q_{\{i,j_1\}},\ldots,q_I\). It checks the equality of these rational volumes in dimensions two through six, the exact balanced and extreme formulas, the sharp bounds, strict pair-balancing on rational examples, and the partition identity \(\sum_i p_i=1\). These finite checks are not used in place of the all-dimensional proof. For example, when \(d=3\) and \(b=(4,1,2,3)/10\), the four exact volume fractions are \(3/25,21/50,83/300,11/60\), summing to one.

## Relationship to prior work
The motivating direction is the calculation of *restricted or clipped power-diagram cells*, emphasized in the September 8, 2025 preprint by Xiao, Cao and Chen (arXiv:2509.07175, latest available version February 16, 2026). Its Sections III, IV and VII-C develop simplex-cell intersection algorithms and weighted lifting; it does **not** derive all-dimensional closed volume formulas or the strict balancing theorem. Budninskiy, Liu, Tong and Desbrun (2016) establish power-diagram geometry and its barycentric-coordinate applications (Sections 2.1–2.5); those constructions are established background, not claimed here.

Two later November 10, 2026 manuscripts by Jan Pavlík study orthogonal-cutout constructions, including a centered regular-simplex cuboidal subdivision (arXiv:2611.13896, Proposition 5.6) and the orthogonal-kernel framework (arXiv:2611.14277). Their centered geometry is acknowledged, and the present theorem does not assert priority for the existence of cubical subdivisions, normal-cone partitioning, or elementary perpendicular feet. In particular, the new claim is the **all-interior weight-dependent normalized volume polynomial plus strict Schur balance and sharp fixed-coordinate interval**. We inspected the relevant propositions and appendices of both later papers and found no statement implying these exact volume laws. We found no published equivalent in targeted searches, but cannot exclude an unindexed earlier computation.

## Limitations
The proof applies to Euclidean regular simplices with interior poles and does not assert the analogous all-interior conclusion for arbitrary polytopes or irregular simplices. The endpoint lower bound is not achieved by an interior pole. General volume-integration and majorization principles are classical and are not claimed as new. Historical priority could be affected by earlier specialized literature on unequal-pole cubical simplex decompositions or by independently unpublished calculations; no priority guarantee is asserted. The verifier checks finite dimensions, not infinite quantifiers.

## References
1. Y. Xiao, J. Cao and Z. Chen, *Efficient Computation of Voronoi Diagrams Using Point-in-Cell Tests*, arXiv:2509.07175, first posted September 8, 2025 (see Sections III, IV and VII-C of the February 2026 revision). https://arxiv.org/abs/2509.07175
2. M. Budninskiy, B. Liu, Y. Tong and M. Desbrun, *Power Coordinates: A Geometric Construction of Barycentric Coordinates on Convex Polytopes*, ACM Trans. Graphics 35(6), 241 (2016), Sections 2.1–2.5. https://www.geometry.caltech.edu/pubs/BLTD16.pdf
3. J. Pavlík, *Face lattices of polytopes and bipolar polytopes*, arXiv:2611.13896 (November 10, 2026), Proposition 5.6 and related definitions. https://arxiv.org/abs/2611.13896
4. J. Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277 (November 10, 2026), Sections 3–6. https://arxiv.org/abs/2611.14277
