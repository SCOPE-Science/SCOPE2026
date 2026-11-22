# A sharp six-cell positive one-twentieth decomposition of the regular decagon

## Finding

Draw every diagonal of a regular decagon, retain the ten boundary sides, and let an **elementary cell** mean a bounded face of the resulting planar straight-line graph. The graph has exactly **220** elementary cells, in exactly **twelve distinct area classes**. Let \(A\) be the area of the decagon. Then:

1. There exist **six pairwise interior-disjoint elementary cells** whose combined area is exactly \(A/20\).
2. No union of five or fewer elementary cells has area \(A/20\). Hence **six is the sharp minimum**.
3. There are **exactly two possible area-class multiplicity patterns** for a minimal six-cell union: classes \(4,8,11,11,11,11\) or \(7,8,10,11,11,11\). Their total number of distinct six-cell subsets, with cells individually distinguished, is **8,778,000**.
4. The complete twelve-class normalized-area spectrum, including multiplicities, is given below. In particular, one six-cell witness is one cell of each of classes 7, 8 and 10 and three distinct cells of class 11 (indices starting from zero in increasing area order):

\[
\left(-\frac45+\frac{9\sqrt5}{25}\right)
+\left(\frac1{20}-\frac{\sqrt5}{50}\right)
+\left(\frac12-\frac{11\sqrt5}{50}\right)
+3\left(\frac1{10}-\frac{\sqrt5}{25}\right)
=\frac1{20}.
\]

This gives a positive (coefficients zero or one), rather than signed, realization of the decagonal area fraction appearing in OEIS A401643. No connectedness requirement is imposed on the union.

| Class | Exact area divided by \(A\) | Number of cells |
|---:|---|---:|
| 0 | \(-21/20+47\sqrt5/100\) | 10 |
| 1 | \(-1/5+9\sqrt5/100\) | 20 |
| 2 | \(-29/40+13\sqrt5/40\) | 20 |
| 3 | \(1/8-11\sqrt5/200\) | 20 |
| 4 | \(-2/5+9\sqrt5/50\) | 20 |
| 5 | \(1/4-11\sqrt5/100\) | 20 |
| 6 | \(23/40-51\sqrt5/200\) | 20 |
| 7 | \(-4/5+9\sqrt5/25\) | 10 |
| 8 | \(1/20-\sqrt5/50\) | 20 |
| 9 | \(9/10-2\sqrt5/5\) | 10 |
| 10 | \(1/2-11\sqrt5/50\) | 30 |
| 11 | \(1/10-\sqrt5/25\) | 20 |

These positive integer multiplicities sum to 220 and their area-weighted sum is one.

## Assumptions and scope

Use the regular convex decagon with vertices numbered cyclically \(0,1,\ldots,9\), and all \(\binom{10}{2}=45\) vertex-to-vertex segments. Coincident intersections of three or more diagonals count as **one vertex** in the planar graph. A cell is a nonempty connected component of the decagon's interior after removing all diagonals, with its open interior used for overlap. Cell boundary intersections do not contribute area. The theorem is exact, and does not assume a particular radius or orientation. The witness's selected cells need not form a connected set.

## Proof

**Exact coordinate field.** Apply the nonsingular affine map \((x,y)\mapsto (x,y/\sin(\pi/5))\) to a unit-circumradius regular decagon with vertex zero at \((1,0)\). Put
\[
 c=\frac{1+\sqrt5}{4},\qquad s^2=\frac{5-\sqrt5}{8}.
\]
Starting at \((X_0,Y_0)=(1,0)\), obtain all ten vertices by the recurrence
\[
 (X_{j+1},Y_{j+1})=(cX_j-s^2Y_j,\ X_j+cY_j).
\]
Thus every vertex and every intersection of distinct nonparallel chord lines lies in \(K=\mathbb Q(\sqrt5)\) in these coordinates. Affine transformations preserve which faces are bounded and every ratio of areas. The transformed decagon has total area exactly 5 (shown by the shoelace sum). The `K` class in `decagon_exact.py` stores every field element as two rational coefficients and compares signs exactly by comparing squares in \(\mathbb Q\) where necessary; no floating-point comparison occurs in the certificate.

**Exhaustive face determination.** For each of the 45 segments, intersect it with every other segment by solving two scalar linear equations in \(K\); retain exactly the intersections with both closed-segment parameters between zero and one, inclusive. The endpoint and intersection set of each original segment is split into consecutive pieces. Deduplicate identical intersection points and undirected segment pieces, forming a finite embedded planar graph. Sort neighbors of every vertex by the sign of a \(K\)-valued cross product and an exact half-plane predicate. Traversing each directed edge with the next clockwise neighbor at its endpoint enumerates each face boundary exactly once, including the exterior face. All faces have nonzero signed shoelace area.

These deterministic rules give **171 distinct graph vertices, 390 edges, and 221 faces**. Euler's identity \(171-390+221=2\) provides an independent topological consistency check. Exactly one face has negative signed area (the exterior), leaving 220 positive-area cells. Evaluating their signed shoelace sums and dividing by the transformed decagon area 5 yields precisely the twelve pairs of rational coefficients in the displayed table, with precisely the stated multiplicities. The sum of all bounded areas equals 5. `decagon_exact.py` performs every step in exact arithmetic from the definitions above; the finite loop covers every chord pair and every directed segment-piece halfedge.

**Attaining witness.** The displayed four-term identity selects one face of each of types 7, 8 and 10 and three distinct faces of type 11. There are respectively 10, 20, 30 and 20 available faces in those classes, so these selections can be made with no duplicated cell. The certificate selects the six bounded-face indices \(0,17,1,10,23,34\) in its deterministic face enumeration. It recalculates their combined signed shoelace area directly, confirming exactly \(5/20\) in transformed coordinates.

**Minimality.** Write the normalized cell area of class \(j\) as \(a_j+b_j\sqrt5\), where the twelve pairs are explicitly given in the table. A union of at most five cells would imply
\[
 \sum_{j=0}^{11}m_j a_j=\frac1{20},\qquad
 \sum_{j=0}^{11}m_j b_j=0,
 \qquad m_j\in\{0,1,2,3,4,5\},\quad \sum_j m_j\le5.
\]
This necessary condition permits **repeated classes without multiplicity restrictions**, so its failure proves the stronger impossibility. The certificate exhausts every nondecreasing sequence of at most five class indices, prunes only when its exact positive area exceeds \(1/20\), and checks both independent rational coefficients at every node. It visits 6,186 candidate-prefix states and finds zero matches. Every possible multiset is encountered because any multiset has a unique nondecreasing sequence; pruning is legitimate because every class area is strictly positive. Hence no union of at most five cells has the required area. The same exact class-multiset enumeration at size six produces exactly two solutions, with index patterns \((4,8,11,11,11,11)\) and \((7,8,10,11,11,11)\). Every choice of distinct cells of the specified classes is valid, because the cells have disjoint interiors and area is additive. There are respectively
\[
inom{20}{1}inom{20}{1}inom{20}{4}=1{,}938{,}000
\quad	ext{and}\quad
inom{10}{1}inom{20}{1}inom{30}{1}inom{20}{3}=6{,}840{,}000
\]
choices, giving \(8{,}778{,}000\) minimizing sets in total. Thus the minimality and the complete equality-class classification follow.

## Verification

Execute `python3 decagon_exact.py` with Python 3 and its standard library, with no additional files or installed packages. The exact checker raises an assertion on any discrepancy. Its output reports 171 vertices, 390 edges, 221 faces, 220 bounded faces, twelve exact area types and multiplicities, and **zero exact targets among all 6,186 searched prefixes of size at most five**, and the **two and only two size-six class patterns**. It then prints the six explicit witness faces and independently recomputes the witness shoelace sum. The output's decimal approximations are presentation only and are never used in a proof decision. The exhaustive computation is finite, not a sample of infinitely many configurations: every chord and every induced cell of this single decagon is represented.

## Relationship to prior work

Felix Huber's OEIS A401643, dated 31 October 2026, establishes \(a(10)=20\) as the largest denominator allowed by signed combinations of distinct elementary-cell areas, and explicitly asks whether the extremal reciprocal can always be obtained by an **unsigned** union. The present result proves the positive realization for \(n=10\), determines the complete decagonal cell-area spectrum, and gives the **minimum six-cell support** for such a realization. The signed denominator formula itself is *not* claimed as new. Huber's linked note illustrates positive realizations for the nonagon, which is a distinct polygon.

Inoue and Watanabe, arXiv:2610.22970 (first publicly posted 16 October 2026), classify rational area unions for partitions produced by **two crossing congruent diagonals**, not the elementary cells of the **simultaneous arrangement of all 35 diagonals**. Their theorem neither gives the twelve-class decagon spectrum nor implies the six-cell positive-minimality statement. Related indexed findings on regular decagons concern unrelated invariants such as curvature and line-incidence arithmetic, and do not imply the present cell-subset result. The full Zenodo note underlying A401643 was not accessible for a comprehensive within-document priority check; this is a material residual historical-priority risk, not evidence of absence.

## Limitations

This settles only the regular decagon's positive representation of \(1/20\) and its minimum number of cells, not the general positive-representation question for arbitrary numbers of sides. It classifies the two allowed six-cell area-class patterns and counts every minimizing set, but does not require or prove their connectedness. No independent third-party mathematical audit has been performed. A priority assessment could change upon inspection of Huber's full Zenodo note or unindexed earlier enumerations.

## References

- Felix Huber, *OEIS A401643: Signed-area lattice of a regular polygon*, dated 31 October 2026; https://oeis.org/A401643 . Describes \(a(10)=20\), the positive-representation question, and the regular nonagon example.
- Felix Huber, *The Area Lattice of a Regular Polygon: Rational Fractions and Signed Cell Decompositions*, Zenodo, 31 October 2026, DOI https://doi.org/10.5281/zenodo.23841077 . Full text inaccessible during this check.
- Shoichi Inoue and Keiichi Watanabe, *Rational Area Profiles of Regular Polygons Cut by Two Congruent Diagonals*, arXiv:2610.22970, 16 October 2026; https://arxiv.org/abs/2610.22970 .
