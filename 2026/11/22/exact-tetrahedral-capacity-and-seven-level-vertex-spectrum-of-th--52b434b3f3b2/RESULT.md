# Exact tetrahedral capacity and seven-level vertex spectrum of the truncated tetrahedron

## Finding
Let \(T\) be the Archimedean truncated tetrahedron obtained from a regular tetrahedron by removing a similar tetrahedron of linear scale \(1/3\) at each of its four vertices. Then the largest-volume tetrahedron contained in \(T\) occupies exactly
\[
\max_{p_0,p_1,p_2,p_3\in T}\frac{\operatorname{Vol}_3(\operatorname{conv}\{p_0,p_1,p_2,p_3\})}{\operatorname{Vol}_3(T)}=\frac6{23}.
\]
In the normalization below its maximal tetrahedron volume is \(16\), attained by exactly \(24\) unordered quadruples of vertices, all belonging to one orbit of the full tetrahedral symmetry group. The complete spectrum of the \(495=\binom{12}{4}\) unordered vertex-supported tetrahedra is:

| Tetrahedron volume | Number of vertex quadruples |
|---|---:|
| \(0\) | 78 |
| \(8/3\) | 48 |
| \(16/3\) | 192 |
| \(8\) | 27 |
| \(32/3\) | 120 |
| \(40/3\) | 6 |
| \(16\) | 24 |

Moreover, there are eight explicit two-dimensional families of optimal *nonvertex* tetrahedra. In each family three vertices are fixed in a triangle lying on one hexagonal face, while the fourth point varies freely in a triangular face on the opposite side of the solid. Every vertex-supported maximizer belongs to exactly one of these eight families. No claim is made that these exhaust all possible nonvertex maxima.

## Assumptions and scope
Take original regular-tetrahedron vertices \(u_0=(1,1,1)\), \(u_1=(1,-1,-1)\), \(u_2=(-1,1,-1)\), and \(u_3=(-1,-1,1)\). Number the twelve vertices \(v_{ij}=2u_i+u_j\), for \(0\le i,j\le3\), \(i\ne j\), in lexicographic order on directed index pairs. Then \(T=\operatorname{conv}\{v_{ij}\}\), with edge length \(2\sqrt2\). The theorem concerns Euclidean three-volume and all tetrahedra whose four points lie anywhere in \(T\). Quadruples are unordered and counted without multiplicities, while nonvertex families are continuous and not counted as finite vertex quadruples.

## Proof
**Reduction to vertices.** For fixed other three points, signed volume is an affine functional of the remaining point. Its absolute value is convex and reaches its maximum at a vertex of the convex polytope \(T\). Replacing each of four points successively by such a vertex cannot decrease the volume. Compactness supplies a maximum; hence the global maximum equals the maximum over the \(495\) distinct unordered vertex quadruples. Degenerate repeated vertices contribute zero.

**Exact exhaustive determinant computation.** For each increasing quadruple \(a<b<c<d\) in \(\{0,\ldots,11\}\), compute
\[
\Delta(a,b,c,d)=\bigl|\det(v_b-v_a,\ v_c-v_a,\ v_d-v_a)\bigr|.
\]
The stand-alone integer checker `check_tetrahedra.py` evaluates every one of the \(495\) determinants by the independent signed-permutation expansion, checks the seven exact determinant multiplicities \((0,78),(16,48),(32,192),(48,27),(64,120),(80,6),(96,24)\), and verifies the explicit eight facial families below. There are no floating-point steps in this finite exhaustive certificate. Consequently the maximum volume is \(96/6=16\), and precisely \(24\) vertex quadruples attain it. The maximum orbit under permutations of the four original vertices has \(24\) members and equals the complete set of vertex maximizers.

**Normalization and capacity.** The original tetrahedron with vertices \(3u_i\) has volume \(72\). Each removed corner is a tetrahedron similar by scale \(1/3\), of volume \(72/27\). Therefore \(\operatorname{Vol}_3(T)=72(1-4/27)=184/3\) and the maximal occupancy fraction is \(16/(184/3)=6/23\).

**Eight moving-apex families.** In zero-based lexicographic vertex numbering, the eight fixed-base triples and their opposite triangular-face vertex triples are

| Fixed base | Opposite triangular face |
|---|---|
| (0,4,6) | (9,10,11) |
| (0,5,9) | (6,7,8) |
| (1,3,7) | (9,10,11) |
| (1,8,9) | (3,4,5) |
| (2,3,10) | (6,7,8) |
| (2,6,11) | (3,4,5) |
| (4,8,10) | (0,1,2) |
| (5,7,11) | (0,1,2) |

For each row, all three signed determinants have identical sign and absolute value \(96\). Since signed volume is affine in the fourth point, it remains \(96/6=16\) throughout the entire opposite triangular face. The full families are two-dimensional because those faces have positive area. Their \(8\cdot3=24\) distinct vertex quadruples are exactly the finite maximizing set, as verified by the checker. The fixed-base triangles lie on hexagonal faces, which can be verified directly from the given integer coordinates and their supporting planes. This establishes the stated families, without requiring or asserting an exhaustive classification of arbitrary nonvertex maximizers.

## Verification
Run `python3 check_tetrahedra.py` with Python 3 standard library. The program checks all \(495\) determinant values with integer arithmetic, all seven spectrum multiplicities, the eight signed-affine facial families, transitivity of the \(24\)-element tetrahedral permutation action, and the total-volume and capacity arithmetic using exact rational numbers. The general vertex-reduction lemma and the affine moving-apex argument are mathematical proofs, not empirical inferences from the program. The finite list is complete because it enumerates all four-subsets of all twelve extreme points.

## Relationship to prior work
Jiao and Torquato's 2011 open-access paper describes the Archimedean truncated tetrahedron, its face geometry, and dense packings in three-space. Chen, Jiao, and Torquato (2014) study statistical-mechanical phases of packed truncated tetrahedra, not an internal tetrahedral volume extremum. Published geometrical computations for the regular truncated octahedron and rhombicuboctahedron involve different convex bodies and do not imply the exact seven-level spectrum, capacity, or eight optimal moving-apex constructions here. The generic fact that a largest contained simplex can be vertex-supported is classical and is used rather than asserted to be new.

## Limitations
This result fixes the equal-edge Archimedean truncation; it does not classify arbitrary truncation depths. The spectrum enumerates vertex-supported tetrahedra, not a finite spectrum of arbitrary interior quadruples. Eight positive-area families are exhibited but not proven to exhaust every continuous maximal family. The priority comparison is best knowledge from inspected open sources and search results; no independent historical-priority certification is claimed.

## References
- Y. Jiao and S. Torquato, *A Packing of Truncated Tetrahedra that Nearly Fills All of Space*, arXiv:1107.2300, originally posted 2011-07-12, https://arxiv.org/html/1107.2300v4 .
- D. Chen, Y. Jiao, S. Torquato, *Equilibrium Phase Behavior and Maximally Random Jammed State of Truncated Tetrahedra*, arXiv:1406.1535, originally posted 2014-06-05, https://arxiv.org/abs/1406.1535 .
- *Exact seventeen-level vertex-tetrahedron spectrum of the regular truncated octahedron*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-seventeen-level-vertex-tetrahedron-spectrum-of-the-regular--dccd7f07f88d .
- *Largest tetrahedra and sixteen movable-apex families in the rhombicuboctahedron*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-largest-tetrahedra-and-sixteen-movable-apex-families-in-the-rhom--eee1b2848255 .
