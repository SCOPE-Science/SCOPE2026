# A sharp first stability gap for vertex–tetrahedron distances in the Boolean four-cube

## Finding
Consider a full-dimensional four-simplex whose five vertices belong to the Boolean cube \(\{0,1\}^4\). Mark one vertex \(p\), and let \(T\) be the tetrahedron spanned by the other four vertices. The first two possible squared Euclidean distances are precisely \(1/4\) and \(1/3\), with no squared distance strictly between them. Consequently, every nonminimizing configuration satisfies the **sharp stability inequality**
\[
\operatorname{dist}(p,T)^2\geq\frac13=\frac14+\frac1{12}.
\]
There are exactly 16 minimizing marked simplices (one for each choice of \(p\)), all mutually equivalent under cubical symmetry. There are exactly **448** marked simplices at the sharp second level. Under the complete symmetry group of the Boolean four-cube these split into exactly **three** orbits of respective sizes **192, 192, 64**.

After mapping the marked vertex to \(0000\), representatives of the three second-level orbits are the following unordered sets of tetrahedron vertices (four-bit strings denote their coordinates):

- \(\{0001,0010,0100,1001\}\): fixed-marked-vertex orbit size 12, full orbit size 192;
- \(\{0001,0010,0100,1011\}\): fixed-marked-vertex orbit size 12, full orbit size 192;
- \(\{0001,0010,0100,1111\}\): fixed-marked-vertex orbit size 4, full orbit size 64.

The unique fixed-marked-vertex minimizer is \(\{0001,0010,0100,1000\}\).

## Assumptions and scope
All distances use the ordinary Euclidean norm of \(\mathbb R^4\). The five selected vertices must be *affinely independent*, so a genuine four-simplex is obtained. The tetrahedron comprises the convex hull of the four unmarked vertices, **not** their entire affine hull. Both the nondegeneracy condition and nonnegative barycentric coordinates are essential. The configurations are unordered in the tetrahedron vertices but marked by \(p\). The orbit counts refer to all 16 marked cube vertices and to the hyperoctahedral group of coordinate permutations and coordinate complements.

## Proof
A coordinate-complement isometry sends any marked Boolean vertex \(p\) to the origin. Its stabilizer in the full cube isometry group is exactly the permutation group on the four coordinates. It therefore suffices to inspect unordered four-element subsets \(T\) of the other fifteen vertices, up to coordinate permutation.

There are \(\binom{15}{4}=1365\) candidate tetrahedra. The corresponding simplex is four-dimensional exactly when the four vectors in \(T\), regarded as columns, have linearly independent span. The exact rank test in `verify.py` establishes that exactly 940 of the 1365 candidates satisfy this condition. This is an exhaustive, finite, independently replayable certificate, not a sample of instances.

For each of those 940 candidates, the distance to its convex hull is computed by exact rational arithmetic. Any minimizer of the strictly convex squared norm over \(T\) belongs to the relative interior of a unique face \(F\) of \(T\). It is the orthogonal projection of the origin to \(\operatorname{aff}(F)\). Thus one may inspect all 15 nonempty subsets of four vertices, compute the orthogonal projection by a rational Gram linear system, retain it only when its barycentric coordinates are nonnegative, and take the smallest squared norm. This argument proves the exhaustive procedure evaluates the true *convex-hull* distance, even if the minimizer lies on an edge or a triangle rather than in the tetrahedron's interior. Every candidate projection, feasibility inequality, rank decision, and squared distance is rational and exact.

The complete enumeration yields precisely one candidate with squared distance \(1/4\); precisely 28 with squared distance \(1/3\); and none with a value strictly between them. The next value is \(2/5\) (36 candidates), furnishing an extra consistency check on the strict gap. The unique minimum candidate has vertices the four standard basis vectors, and its closest point is \((1/4,1/4,1/4,1/4)\), giving squared distance \(1/4\).

The 28 second-level fixed-origin candidates decompose into three coordinate-permutation orbits. The verifier produces the three representatives above, checks that every member of each constructed orbit lies in the exact second-level set, and removes its members before taking the next orbit; their sizes are 12, 12, and 4, exhausting all 28. Since every marked vertex can be sent to the origin in exactly one coordinate-complement translation, the global counts multiply by 16. Hence the minimum count is \(16\), and the sharp second-level count is \(16\cdot28=448\), with orbit sizes \(16\cdot(12,12,4)=(192,192,64)\). No other choices or symmetry types remain.

## Verification
Run `python verify.py` with Python 3.10+; no external packages are required. The script performs all 1365 possible fixed-origin four-subset selections, exact rank testing, all 15 face-projection tests for each of 940 nondegenerate simplices, the complete squared-distance histogram, and the full coordinate-permutation orbit decomposition. It contains assertions for each theorem count and the sharp gap. Its printed output includes the first ten squared-distance shells and all three orbit representatives. A fresh replay completed successfully.

## Relationship to prior work
Deza and Pournin, *Flat simplices and kissing polytopes* (first arXiv version January 6, 2026), define opposite-face separation for lattice simplices and give the already known minimum distance \(\varepsilon_0(4,1)=1/2\) in their Table 2. The present result **does not claim that minimum as new**; it isolates the next attainable distance for *full-dimensional* Boolean four-simplices and completely classifies their near-minimizers under cube symmetry. The distinction between convex faces and affine hulls is also stressed in that work. Deza, Liu, and Pournin, *Small kissing polytopes*, study the minimum distance between general disjoint lattice polytopes, a different minimization class. Deza, Onn, Pokutta, and Pournin, *Kissing polytopes*, develop general bounds and computations but do not state the particular near-extremal point-to-tetrahedron orbit classification. The novelty comparison remains provisional, subject to possible unindexed equivalences.

## Limitations
This is a finite, dimension-four, Boolean-vertex stability classification, not an asymptotic bound or a claim in arbitrary dimension or for higher lattice coordinate ranges. The proof is a transparent exhaustive *exact rational* certificate relying on running `verify.py`, rather than a short purely symbolic case-free derivation. It does not classify the remaining distance spectrum by symmetry or imply algorithmic complexity bounds. Literature priority remains subject to independent examination. No independent mathematical audit has been performed.

## References
- Antoine Deza and Lionel Pournin, *Flat simplices and kissing polytopes*, arXiv:2601.03183v1 (2026-01-06), https://arxiv.org/pdf/2601.03183.
- Antoine Deza, Zhongyuan Liu, and Lionel Pournin, *Small kissing polytopes*, arXiv:2412.03479v1 (2024-12-04), https://arxiv.org/pdf/2412.03479.
- Antoine Deza, Shmuel Onn, Sebastian Pokutta, and Lionel Pournin, *Kissing polytopes*, arXiv:2305.18597 (2023), https://arxiv.org/pdf/2305.18597.
