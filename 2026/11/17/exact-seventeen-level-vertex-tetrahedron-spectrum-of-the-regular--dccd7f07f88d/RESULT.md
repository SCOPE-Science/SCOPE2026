# Exact seventeen-level vertex-tetrahedron spectrum of the regular truncated octahedron

## Finding
Let \(P\subset\mathbb R^3\) be the regular truncated octahedron with vertices the 24 distinct signed coordinate permutations of \((0,1,2)\); its edge length is \(\sqrt2\) and its Euclidean volume is \(32\). For every four-element subset \(Q\) of the vertex set, let \(v(Q)\) be its ordinary, nonnegative tetrahedral volume, including zero for coplanar quadruples. **The complete exact spectrum** is
\[
\{v(Q):|Q|=4\}=\left\{\frac{j}{3}:j=0,1,\ldots,16\right\}.
\]
The multiplicity of \(v(Q)=d/6\), with \(d=0,2,\ldots,32\), is given below. The 17 entries sum to \(\binom{24}{4}=10626\).

| Absolute edge determinant \(d\) | Multiplicity | Absolute edge determinant \(d\) | Multiplicity |
|---:|---:|---:|---:|
| 0 | 846 | 18 | 408 |
| 2 | 552 | 20 | 480 |
| 4 | 1728 | 22 | 72 |
| 6 | 1152 | 24 | 468 |
| 8 | 1332 | 26 | 48 |
| 10 | 456 | 28 | 144 |
| 12 | 1872 | 30 | 24 |
| 14 | 360 | 32 | 30 |
| 16 | 654 | — | — |

In particular, the largest vertex-supported tetrahedral volume is \(16/3\), the *strictly second-largest vertex-supported volume* is \(5\), and the exact discrete gap is \(1/3\). The largest volume is attained by 30 tetrahedra in **exactly two noncongruent Euclidean classes**, which form signed-coordinate-permutation orbits of sizes 6 and 24. The respective sorted six-tuples of squared edge lengths are
\[
(12,12,12,12,16,16),\qquad(10,12,12,14,14,16).
\]
The 24 second-largest tetrahedra form a single such orbit, with squared-edge-length six-tuple \((10,10,12,14,14,18)\). Thus the maximal occupied fraction of the truncated-octahedral cell is \(1/6\), and the next discrete vertex-supported fraction is \(5/32\).

## Assumptions and scope
The metric is the inherited ordinary Euclidean metric, not a lattice-normalized volume. The polyhedron is precisely
\[
P=[-2,2]^3\cap\{x\in\mathbb R^3:|x_1|+|x_2|+|x_3|\le3\}.
\]
Its 24 vertices are exactly the points described above; the vertex order used in `SPECTRUM.csv` is Python's lexicographic order on the sorted set produced by `get_vertices()` in `verify.py`. A tetrahedron is counted **once per unordered four-vertex set**, regardless of degeneracy. Distinct volumes are exact rational values, not numerically clustered approximations. Statements about a second-largest value and multiplicity apply only to vertex-supported tetrahedra: allowing arbitrary points of \(P\) destroys any positive gap below the maximum. No assertion of novelty of the previously known maximum-volume bound itself is made.

## Proof
**1. Vertex and volume normalization.** Each of the six coordinate sections \(x_i=\pm2\) is a square with four vertices of the form \((\pm2,\pm1,0)\) and coordinate permutations. The other eight facets are the planes \(\pm x_1\pm x_2\pm x_3=3\), whose feasible sections are regular hexagons. Their intersections yield precisely the 24 permutations with independently signed nonzero entries. All these points lie on three independent supporting planes, and there are no additional vertices: intersections of three independent active inequalities of the six coordinate bounds and eight signed-sum bounds give only these feasible candidates. Adjacent vertices differ by a vector of norm \(\sqrt2\). In each coordinate orthant, inclusion–exclusion gives the region's volume as
\[
\frac{3^3-3(3-2)^3}{3!}=4.
\]
Eight orthants therefore give \(\operatorname{vol}_3(P)=32\).

**2. Arithmetic restriction.** Every vertex has odd integer coordinate sum. Each difference of two vertices consequently lies in the index-two sublattice \(\{z\in\mathbb Z^3:z_1+z_2+z_3\equiv0\pmod2\}\). Hence every three-edge determinant of a vertex tetrahedron is an even integer. Its volume is the determinant magnitude divided by six, so it lies in \(\frac13\mathbb Z_{\ge0}\).

**3. Exhaustive exact count.** `verify.py`, bundled with this result, generates the vertex set as all permutations of \((0,\pm1,\pm2)\) with independent signs, asserts it has exactly 24 elements, and visits every unordered four-element subset using `itertools.combinations(vertices,4)`. It applies the displayed exact three-by-three determinant formula in `det3`, takes absolute values, and accumulates the frequency dictionary `EXPECTED`. This is a finite complete enumeration of all \(10626\) cases, not sampling or an attempt to infer an infinite statement. The accompanying `SPECTRUM.csv` gives, for every attained determinant, its exact frequency and a concrete four-index witness in lexicographic vertex order. The verifier checks all 17 witness quadruples, totals, and frequencies.

**4. Symmetry and independent certificate.** A separate pass constructs all \(3!2^3=48\) signed-coordinate permutations and partitions the \(10626\) quadruples into exactly 265 disjoint group orbits. It rechecks determinant invariance on every orbit and obtains precisely the same multiplicities. At determinant magnitude 32 it finds exactly two orbits of sizes 6 and 24, with the distinct squared-distance signatures displayed in the finding; these signatures forbid congruence between the two classes, while each orbit supplies congruences within its class. At magnitude 30 the unique orbit has size 24 and the signature stated above.

The final check constructs the 24 *four-dimensional* permutations \(p=(a,b,c,d)\) of \((1,2,3,4)\). The map
\[
p\longmapsto\frac12(a+b-c-d,\ a-b+c-d,\ a-b-c+d)
\]
restricts to an orthogonal isometry from the fixed-sum hyperplane in \(\mathbb R^4\) onto \(\mathbb R^3\), mapping the permutation vertices bijectively to the displayed 24 vertices. For every quadruple of these four-dimensional vertices, the determinant of the \(3\times3\) Gram matrix of its three four-dimensional edge vectors equals the **square** of the three-dimensional edge determinant. The checker computes this Gram determinant directly in four dimensions, confirms it is a nonnegative perfect square, and independently reproduces all 17 frequency counts. Consequently the exact finite table and the top two orbit classifications follow.

## Verification
Run `python3 verify.py` with `SPECTRUM.csv` in the same directory using Python 3 and its standard library. The successful output is `TRUNCATED_OCTAHEDRON_TETRAHEDRAL_SPECTRUM_PASS quadruples=10626 levels=17 octahedral_orbits=265 max_orbits=6+24 second_orbit=24`. No floating-point arithmetic, external software, internet connection, or unavailable certificate is required. The checks reproduce the enumeration, the symmetry-orbit partition, the six-distance congruence invariants and the separate four-dimensional Gram calculation. The proof is a rigorously finite exhaustive certificate; the checker is not a general theorem prover about other polyhedra.

## Relationship to prior work
Lángi's 2021 study identifies the regular truncated octahedron as the volume-normalized minimum-mean-width parallelohedron and develops its zonotopal geometry, giving a natural metric reason to study this specific cell. Murphy and Weed's 2024 construction describes the regular truncated octahedron as the one-third vertex truncation of an octahedron, but treats face embeddings rather than all vertex tetrahedron volumes. A previously published exact study, *Sharp tetrahedral-volume profile in the cube–octahedron intersection family* (2026), already determines the **maximum** tetrahedral volume in the larger continuous family \([-1,1]^3\cap\{\|x\|_1\le c\}\), including the truncated-octahedral member \(c=3/2\), and the sharp occupancy ratio \(1/6\). The inspected result explicitly does **not** classify all maximizers and does not supply the complete 17-level vertex quadruple frequency distribution. This work claims only that distribution, its exact vertex-supported second level, and the two congruence types of the maximal vertex tetrahedra as contributions beyond that literature. A complete historical-priority guarantee is not asserted.

## Limitations
Only the fixed regular three-dimensional truncated octahedron and four **vertex** selections are covered, not general deformations, arbitrary interior points, or all tetrahedra in the solid. The entire spectrum is determined by a small exact finite computer-assisted enumeration; its source code must be reviewed to independently trust the count. The previously known maximum remains previously known. Database and keyword searches, even with inspected closely related full sources, cannot exclude all unindexed equivalent results.

## References
1. Zs. Lángi, *An isoperimetric problem for three-dimensional parallelohedra*, arXiv:2102.11621, first public 23 February 2021, https://arxiv.org/abs/2102.11621 .
2. T. Murphy and D. Weed, *Face embeddings of Archimedean solids*, arXiv:2404.15142, first public 23 April 2024, https://arxiv.org/abs/2404.15142 .
3. *Sharp tetrahedral-volume profile in the cube–octahedron intersection family*, publicly available result (11 October 2026), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-tetrahedral-volume-profile-in-the-cube-octahedron-intersec--9ba1a511dacf/RESULT.md .
