# Exact Euclidean two-face area spectrum of cycle cosmological polytopes

## Finding

For the cosmological polytope of the cycle \(C_n\), in its canonical standard-coordinate Euclidean embedding, the complete area spectrum of the entire two-dimensional face set has **seven triangular area classes and one square class** when \(n\ge6\). The listed classes with zero multiplicity are simply absent at \(n=4,5\).

| Triangle area | Multiplicity for \(n\ge4\) |
|---|---:|
| \(\sqrt{15}/2\) | \(8n\) |
| \(\sqrt5\) | \(15n(n-4)\) |
| \(\sqrt{23}/2\) | \(14n\) |
| \(3\sqrt3/2\) | \(9n(n-4)(n-5)/2\) |
| \(\sqrt7\) | \(6n\) |
| \(2\sqrt2\) | \(3n(n-3)+12n(n-4)\) |
| \(\sqrt{39}/2\) | \(5n\) |

There are exactly \(n\) further two-faces, all **squares of Euclidean area \(4\)**. For \(n=3\), the triangles instead have areas \(\sqrt3,2,\sqrt7\), with respective multiplicities \(4,12,27\), and the three quadrilateral faces are area-four squares.

A uniformly sampled two-face for \(n\ge4\) is an equilateral triangle of area \(3\sqrt3/2\) with probability
\[
\frac{9(n-4)(n-5)}{9n^2-21n+14}=1-\frac{20}{3n}+O(n^{-2}).
\]
Here "uniformly" means one face is selected with equal probability from the finite face set, not by surface-area weighting. Thus almost every two-face is equilateral as the cycle grows. The combined planar areas of the two-faces sum to \((27\sqrt3/4)n^3+O(n^2)\); this sum is *not* the classical surface area or an intrinsic volume of the high-dimensional polytope.

## Assumptions and scope

Fix an integer \(n\ge3\), with indices interpreted cyclically. Let \(x_0,\dots,x_{n-1},y_0,\dots,y_{n-1}\) be the standard orthonormal basis of \(\mathbb R^{2n}\). Set
\[
 p_i=x_i+x_{i+1}-y_i,\qquad
 q_i=x_i-x_{i+1}+y_i,\qquad
 r_i=-x_i+x_{i+1}+y_i,
\]
where \(i+1\) is reduced modulo \(n\). Let \(P_n=\operatorname{conv}\{p_i,q_i,r_i:0\le i<n\}\). These are the standard cosmological polytope vertices associated to the undirected cycle; a common homothety would rescale all areas quadratically, so the coordinate normalization is essential.

A two-face is a *proper exposed face of intrinsic affine dimension two*. Its area is the ordinary two-dimensional Hausdorff measure in its affine span, with the Euclidean metric inherited from \(\mathbb R^{2n}\). Areas are counted by distinct faces, not by triangles in a triangulation. The known face classification of Kühne–Monin implies that all two-faces are triangles or four-vertex quadrilaterals, and the quadrilaterals are exactly the \(n\) node faces.

## Proof

**1. Exhaustive face types.** Use the established face criterion and its cycle specialization [2, Sections 3 and 5]. A triple of distinct vertices is a two-face precisely in one of the following cases: (a) its vertices arise from three different edge indices, except that in \(C_3\) the two globally coherently directed triples \(\{q_i\}\) and \(\{r_i\}\) are excluded; (b) two vertices from one index are the pair \(q_i,r_i\), and the third is any one of \(p_j,q_j,r_j\) with \(j\ne i\). No triple drawing all three vertices from one index is a two-face. Moreover, [2] identifies precisely one quadrilateral face per graph node. This completes the combinatorial enumeration, without assuming every vertex triple is facial.

**2. The metric computation.** All generating vertices have squared norm three. The pair \(q_i,r_i\) at one index has squared separation eight. Between different indices, the squared separation is six if their graph edges are disjoint, and is four or eight when the edges share a node, depending on whether the signs of that node coordinate agree or disagree. At a prescribed endpoint, precisely two of \(p_i,q_i,r_i\) have sign \(+1\), and one has sign \(-1\); therefore for a pair of incident graph edges, five of the nine label pairs agree and four disagree.

For squared side lengths \(a,b,c\) of any nondegenerate triangle, Heron's formula in Gram form gives
\[
16\operatorname{Area}^2=4ab-(a+b-c)^2.
\]
Consequently the integer \(4\operatorname{Area}^2\) is the convenient area-class label.

**3. A doubled edge index.** There are \(n\) choices of the doubled index. Each edge of \(C_n\) has two adjacent edges, giving \(6n\) triangles with squared side pattern \((8,4,8)\), hence area label \(4\operatorname{Area}^2=28\). For each doubled index there are \(n-3\) nonadjacent edges, each with three possible vertex labels, giving \(3n(n-3)\) triangles with side pattern \((8,6,6)\), area label \(32\).

**4. Three distinct edge indices, \(n\ge4\).** Classify three-element subsets of the edge set by the number of consecutive pairs within the cycle. The numbers with zero, one, or two such pairs are, respectively,
\[
 t_0=\frac{n(n-4)(n-5)}6,\qquad t_1=n(n-4),\qquad t_2=n.
\]
The formulas follow by selecting three disjoint edge locations, a unique adjacent pair, or one consecutive three-edge path; they also hold at the boundary orders \(4,5\). (A three-edge subset of a cycle of length four is a path; the two outer edges are disjoint.)

For each type-zero subset all \(3^3=27\) vertex selections have squared sides \((6,6,6)\) and label \(27\). For type one, the 5 matching-sign choices at the one shared node and the 4 opposing-sign choices, multiplied by 3 labels on the other edge, give 15 triangles with label \(20\) and 12 with label \(32\) per subset.

For a consecutive three-edge path, the middle edge vertex has one of the three endpoint sign patterns \((+,+),(+,-),(-,+)\). Summing independently over three labels on each outer edge yields exactly 8 choices with both adjacent pairs agreeing, 14 with exactly one disagreeing, and 5 with both disagreeing. The corresponding squared side patterns are \((4,4,6),(4,8,6),(8,8,6)\), giving labels \(15,23,39\) in that order. Multiplying by \(t_2=n\), and combining with the doubled-index counts, gives each of the seven formula entries. Their sum equals \(27\binom n3+3n(n-1)\), the previously known number of triangular two-faces [2]; this consistency is not itself the proof of the metric shells.

**5. The triangular cycle \(n=3\).** The doubled-index triangles contribute 18 faces of label \(28\), as in step 3. Among the 27 triples with one chosen vertex from each graph edge, exactly two consistent directed cycle triples are not faces. Directly summing the three endpoint-sign comparisons over the remaining 25 assignments yields 4 of label \(12\), 12 of label \(16\), and 9 of label \(28\). The combined multiplicities are therefore \(4,12,27\), accounting for all 43 triangular faces.

**6. Quadrilateral areas.** At node \(i\), the quadrilateral has vertices \(p_{i-1},r_{i-1},p_i,q_i\). Its opposite vertex pairs share midpoint \(x_i\); its two diagonals are orthogonal, each of squared length eight. Thus it is a square with area half the product of the diagonal lengths, namely four. This holds also for \(n=3\). The face classification ensures these are all quadrilaterals.

**7. Asymptotics.** There are \(27\binom n3+3n(n-1)+n=\frac n2(9n^2-21n+14)\) two-faces in all, while the equilateral ones counted in step 4 number \(\frac92n(n-4)(n-5)\). Their ratio is the displayed formula. The asserted area sum is dominated by the \(27t_0\sim(9/2)n^3\) equilateral triangles, each of area \(3\sqrt3/2\); all remaining families contribute \(O(n^2)\).

## Verification

`verify_area_spectrum.py` is standalone Python 3 code using only the standard library. Execute `python verify_area_spectrum.py`. It constructs the literal integer-coordinate vertices, enumerates every triangular face according to the published cycle criterion, computes \(4\operatorname{Area}^2\) with integer arithmetic, and checks each area multiplicity for every \(3\le n\le12\). It independently checks the midpoint, perpendicularity and lengths of every quadrilateral's diagonals, and compares the total triangle count with the published face-count formula. A passing run prints `COSMO_CYCLE_FACE_AREA_EXACT_PASS n=3..12`. These finite tests are corroborative, not a substitute for the all-\(n\) proof above.

## Relationship to prior work

Arkani-Hamed, Benincasa and Postnikov [1] introduced the cosmological polytopes and their standard embedding. Kühne and Monin [2] establish the complete face criterion and enumerate the two-face counts for cycles (including the exceptional triangular cycle). These are essential inputs, and their combinatorial results are *not* claimed as new. The present result supplies the **evaluated Euclidean area multiset**, rigid square areas, and an asymptotic metric concentration statement: neither the \(f\)-vector alone nor the combinatorial face classification states this metric distribution. The metric is not invariant under arbitrary affine realization changes; the standard coordinate embedding is part of the theorem.

## Limitations

Historical priority beyond the inspected published and indexed literature is not certified. An equivalent computation could occur in unindexed work or be implicitly embedded in a source treating this exact coordinate model. The theorem concerns simple cycles, not arbitrary multigraphs or general cosmological polytopes, and the sum of face areas is not the ambient polytope surface measure. No independent mathematical audit has been performed.

## References

[1] N. Arkani-Hamed, P. Benincasa and A. Postnikov, *Cosmological Polytopes and the Wavefunction of the Universe*, arXiv:1709.02813, initially public 2017-09-08. https://arxiv.org/abs/1709.02813

[2] L. Kühne and L. Monin, *Faces of Cosmological Polytopes*, arXiv:2209.08069, initially public 2022-09-16; Sections 3 and 5. https://arxiv.org/abs/2209.08069
