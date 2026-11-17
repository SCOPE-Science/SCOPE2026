# Complete tetrahedral volume spectrum and rigid maximal disphenoids of the regular 24-cell

## Finding

Let \(C\subset\mathbb R^4\) be the **unit-circumradius regular 24-cell**, with vertex set
\[
V=\{\pm e_i:1\le i\le4\}\ \cup\
\left\{\tfrac12(\varepsilon_1,\varepsilon_2,\varepsilon_3,\varepsilon_4):\varepsilon_i\in\{-1,1\}\right\}.
\]
Among the \(\binom{24}{4}=10626\) unordered choices of four vertices, exactly 474 yield degenerate tetrahedra. Every nondegenerate tetrahedron has one of **ten** positive intrinsic Euclidean three-volumes. Writing \(D=2304\operatorname{Vol}_3(T)^2\), the complete exact spectrum is

| \(D\) | Number of four-vertex sets |
|---:|---:|
| 0 | 474 |
| 32 | 2016 |
| 64 | 1344 |
| 96 | 1152 |
| 128 | 2592 |
| 160 | 576 |
| 192 | 1152 |
| 256 | 192 |
| 288 | 864 |
| 448 | 192 |
| 512 | 72 |

The largest tetrahedron contained in \(C\), **even permitting arbitrary points of \(C\) as its four vertices**, has volume precisely
\[
\boxed{\max_{T\subseteq C}\operatorname{Vol}_3(T)=\frac{\sqrt2}{3}}.
\]
Exactly **72 geometric tetrahedra** attain it. Every maximizing tetrahedron is vertex-supported; all 72 lie in a **single orbit of the full 24-cell isometry group**. Each is a disphenoid with squared edge-length multiset
\[
\boxed{\{2,2,3,3,3,3\}},
\]
with the two shorter edges opposite. Each vertex belongs to exactly 12 maximizing tetrahedra, and no two distinct maximizing tetrahedra share three vertices. The next largest volume among vertex-supported tetrahedra is \(\sqrt7/6\), so the strict first spectral gap is
\[
\boxed{\frac{2\sqrt2-\sqrt7}{6}}.
\]
In contrast, the 24-cell contains exactly 48 vertex-supported equilateral tetrahedra of side \(\sqrt2\), each of volume \(1/3\): the largest tetrahedra are **nonregular** and larger by the factor \(\sqrt2\).

## Assumptions and scope

Intrinsic tetrahedral three-volume means the standard three-dimensional Euclidean Hausdorff measure in the affine hull of a nondegenerate four-point simplex in \(\mathbb R^4\). Distinct unordered four-element vertex subsets are counted once. A degenerate tetrahedron has zero three-volume. Only the finite **volume spectrum** is restricted to vertex choices; the maximum-volume claim and its complete equality classification allow four arbitrary points in the solid 24-cell. All lengths and volumes use the unit-circumradius normalization shown above; applying a uniform factor \(a>0\) multiplies the three-volumes by \(a^3\).

## Proof

**1. Exact integral Gram formula.** Double all vertex coordinates, obtaining the 24-point integer set
\[
W=\{\pm2e_i:1\le i\le4\}\cup\{(\varepsilon_1,\ldots,\varepsilon_4):\varepsilon_i\in\{-1,1\}\}.
\]
For four distinct points \(w_0,w_1,w_2,w_3\in W\), take the integer column vectors \(a=w_1-w_0\), \(b=w_2-w_0\), \(c=w_3-w_0\), and their Gram matrix \(G=(a,b,c)^\mathsf T(a,b,c)\). Since the original tetrahedron has edges \(a/2,b/2,c/2\), the standard Gram-volume identity gives
\[
\operatorname{Vol}_3(T)^2=\frac{\det G}{(3!)^2\,2^6}=\frac{\det G}{2304}.
\]
The determinant is a nonnegative integer. It is also independently given by Cauchy--Binet as the sum of the squares of the four \(3\times3\) minors of the \(4\times3\) edge matrix.

**2. Exhaustive integer certificate.** The accompanying complete standalone `CHECK.py` constructs exactly the 8 doubled coordinate-axis points and the 16 sign vectors; it enumerates all \(\binom{24}{4}=10626\) unordered four-subsets in a fixed lexicographic order. For each set, it calculates \(\det G\) both by the integer Gram determinant and independently by the four signed minors. The two formulas agree termwise. Summing by determinant gives exactly the eleven rows in the stated table, including degeneracy. Thus the sharp vertex-supported volume is \(\sqrt{512}/48=\sqrt2/3\), and exactly 72 four-subsets attain it. The next determinant value is 448, giving \(\sqrt{448}/48=\sqrt7/6\). Independent edge-distance calculations show that every maximizer has squared edge lengths \(2,2,3,3,3,3\) with disjoint short edges. The checker also verifies that each of the 24 vertices occurs in twelve maximizing quadruples; the corresponding 288 three-element subsets of maximizers are pairwise different. Every check is finite and exhaustive, not a numerical sampling claim.

**3. Symmetry rigidity.** Every ordered orthonormal 4-frame selected from \(V\) determines an orthogonal map taking the four standard coordinate vectors to that frame. The supplied integer checker enumerates precisely **1152** such frames. For each frame, it verifies explicitly that the associated orthogonal map permutes all 24 vertices, using only integer arithmetic after doubling coordinates. Therefore these are genuine isometries of \(C\). The orbit of one maximizing four-vertex set under all 1152 maps comprises exactly the 72 maximizing four-vertex sets. Thus there is a single symmetry orbit, without assuming a group-order formula in advance.

**4. No interior maximum tetrahedra.** Intrinsic three-volume is \(\|p_1\wedge p_2\wedge p_3\|/6\), with \(p_j=x_j-x_0\). Because the exterior product is alternating, it is affine linear in each of the four vertices separately when the other three are held fixed. Norm convexity implies that replacing any vertex in \(C=\operatorname{conv}V\) by some vertex of \(C\) cannot reduce a tetrahedron's three-volume. Repeating for four positions extends the sharp vertex-subset bound to **all** inscribed tetrahedra.

Suppose now a global maximizing tetrahedron has at least one nonvertex point \(p\) as a vertex. Hold \(p\) fixed and replace the other three tetrahedral vertices successively by vertices of \(C\), keeping the global maximum at each step. Write \(p=\sum_j\lambda_j v_j\), with at least two distinct \(v_j\in V\) having strictly positive weights. The wedge for \(p\) is the same convex combination of the wedges for the \(v_j\); the norm of each such wedge is bounded by the global maximum. Equality of the norm at \(p\) forces **every** positively weighted replacement \(v_j\) to give a globally maximizing vertex-supported tetrahedron alongside the fixed other three vertices. Two such quadruples would share those three vertices, contradicting the exhaustive no-shared-triple certificate in Step 2. Hence every maximizer is vertex-supported, and the 72 listed quadruples exhaust the unrestricted equality cases.

**5. Regular comparison.** The same exhaustive edge test finds precisely 48 vertex-supported equilateral quadruples, all with squared side length 2. Their regular-tetrahedron three-volume is \(1/3\), strictly smaller than the maximum \(\sqrt2/3\).

## Verification

Run `python3 CHECK.py` using Python 3.8 or later with only the standard library. The script checks all 10626 unordered quadruples using independent exact Gram and minor determinants, the entire frequency table, complete short-edge geometry and vertex incidence, all no-shared-triple relations, all 1152 orthogonal frame maps, the transitive orbit of 72 maximizers, and the 48 equilateral comparison sets. The exact success marker is `VERIFY_OK_24CELL_TETRA_SPECTRUM`. This finite certificate completely verifies the finite enumeration; the convexity and equality-rigidity arguments above are what extend it to tetrahedra with arbitrary nonvertex points.

## Relationship to prior work

Denney et al. (2019) give the 24-cell as the 24 unit quaternions comprising eight coordinate-axis vectors and sixteen half-sign vectors; their work treats incidences and 24-cells embedded in the 600-cell, not the three-volume spectrum of arbitrary four-point subsets of one 24-cell. The complete publicly available article was examined for the coordinate geometry and the stated 24-cell constructions.

Two publicly accessible research results treat **four-dimensional** 4-simplices (five vertices) in the regular 24-cell and its 16-cell truncation family, respectively. Their determinant and equality classifications do not imply the **three-dimensional** four-vertex volume spectrum or the 72 tetrahedron rigidity theorem. Published three-dimensional tetrahedron-volume censuses concern different containing solids. Classical regular-polytope facts describe the regular octahedral cells, inscribed 16-cells and their regular tetrahedra, but not the volume maximum among all nonregular tetrahedra in the solid 24-cell. The assertion of historical priority remains conditional on the accessible literature and indexed results checked.

## Limitations

The frequency table and orbit classifications are exact only for this fixed 24-vertex configuration, up to Euclidean similarities. No formula for a higher-dimensional analogue is claimed. The proof of the finite determinant classification is by fully specified exhaustive integer computation, with a second independent exact determinant implementation; it does not supply an independent pen-and-paper derivation of each multiplicity. The continuous maximum and uniqueness-of-vertex-support conclusion use the separate analytical reduction. Earlier unindexed Coxeter-theory volume tables could contain equivalent information; independent historical and mathematical review has not occurred.

## References

1. T. Denney, D. Hooker, D. Johnson, T. Robinson, M. Butler and S. Claiborne, *The Geometry of H4 Polytopes*, arXiv:1912.06156 (first public 2019-12-12), https://arxiv.org/abs/1912.06156.
2. *Exact largest-simplex volume and equality classification in the regular 24-cell* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-largest-simplex-volume-and-equality-classification-in-the--bda0674b8ea5.
3. *A sharp two-branch simplex-volume law along the 16-cell–24-cell truncation path* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-sharp-two-branch-simplex-volume-law-along-the-16-cell-24-cell--c20f16ef7970.
