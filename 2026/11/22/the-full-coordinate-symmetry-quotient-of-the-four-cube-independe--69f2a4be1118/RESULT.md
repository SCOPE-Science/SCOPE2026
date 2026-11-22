# The full coordinate-symmetry quotient of the four-cube independence complex is collapsible

## Finding

Let \(Q_4\) be the sixteen-vertex binary four-cube graph with edges between bit words at Hamming distance one, let \(K=\operatorname{Ind}(Q_4)\), and let \(G=\operatorname{Aut}(Q_4)\). The ordinary geometric quotient **collapses to a point**:

\[
\boxed{|K|/G\ \searrow\ \{\mathrm{point}\}.}
\]

More precisely, a regular CW model obtained by taking orbits of the simplices of the barycentric subdivision of \(K\) has the number of cells in dimensions \(0\) through \(7\)
\[
(20,133,501,1217,1895,1800,945,210).
\]
A certificate gives exactly \(3360\) elementary free-face/coface removals, leaving one vertex. Therefore \(|K|/G\) is contractible, has zero reduced integral homology and trivial fundamental group, and has trivial simple-homotopy obstruction. The underlying space \(|K|\simeq\bigvee^7 S^3\) is not contractible, as was previously known.

## Assumptions and scope

Identify the vertices with the binary words \(\mathbb F_2^4\), indexed by integers from \(0\) to \(15\); two vertices form a cube edge exactly when their Hamming distance is one. A face of \(K\) is a subset with no cube edge. The full automorphism group comprises the sixteen bit translations followed by all twenty-four permutations of bit positions, so \(|G|=384\). Indeed, after choosing the image of vertex zero, an automorphism permutes its four neighbors; these choices determine all other vertices inductively from cube-distance and common-neighbor structure. We consider the ordinary quotient of the *geometric realization*, not the quotient graph's independence complex or a homotopy-orbit space. The result is not asserted for other cube dimensions or proper symmetry subgroups.

The orbit-cell complex \(Y\) is formed from the barycentric subdivision \(\operatorname{sd}K\), whose vertices are the nonempty faces of \(K\) and whose simplices are strict inclusion chains of nonempty faces. Every group element preserves the size of a face. Hence if it setwise stabilizes a chain, it fixes each member individually, so this action has no inversions; its orbit cells form a regular finite CW complex homeomorphic to \(|K|/G\). Its incidences are obtained by deleting one member of a representative chain. In a strict chain, deletions have distinct cardinality signatures, and hence distinct orbit facets, eliminating degenerate face identifications.

## Proof

**Complete face and symmetry universe.** Enumerate all membership masks \(1\) through \(2^{16}-1\); a mask is a face precisely when no selected vertex differs by one bit from another selected vertex. This gives exactly \(742\) nonempty faces, by cardinality \((16,88,208,228,128,56,16,2)\). Generate all \(384\) affine signed-coordinate maps explicitly. A strict flag is an increasing sequence of such face masks. The number of distinct flags is exactly \(2,199,938\), independently determined by summing the ordered-Bell numbers \(1,3,13,75,541,4683,47293,545835\) over the faces of cardinalities one through eight. (The enumeration of chains inside every containing face processes additional duplicates, which are discarded before counting distinct flags.)

**Exact orbit and incidence structure.** Apply each of the \(384\) maps to every representative flag and identify equal transformed flags. This yields exactly \(6721\) flag orbits with the displayed dimension-by-dimension cell vector. Each cell is represented in the certificate by its unique numeric index and one increasing chain of face masks. Orbit representatives are validated by a second standalone algorithm that builds the full flag-to-orbit dictionary and checks that it contains exactly \(2,199,938\) distinct flags. This independent cardinality check proves exhaustiveness, not just sampling. For every cell, deleting any one chain member gives the boundary facet's unique orbit index.

**An explicit collapse.** The accompanying certificate lists \(3360\) pairs \((f,c)\) of cell indices. In the surviving subcomplex at each step, the verifier checks (i) both cells are present; (ii) the dimension of \(c\) exceeds that of \(f\) by one; (iii) \(f\) is a facet of \(c\); and (iv) \(c\) is the *only* surviving immediate coface of \(f\). The surviving cells form a subcomplex inductively; uniqueness of the immediate coface prevents any higher-dimensional cell from containing \(f\), because such a cell would supply an additional immediate coface. Therefore each indicated pair is a genuine elementary free-face collapse of this regular CW complex. After all \(3360\) pairs, precisely one dimension-zero cell remains, since \(6721-2\cdot3360=1\), and the verifier checks its dimension. A composition of elementary collapses is a strong deformation retraction. This proves the boxed result.

## Verification

The complete certificate is `q4_orbit_certificate.txt`. Run `python3 verify_q4_orbit.py q4_orbit_certificate.txt` with Python 3 and no external packages. The verifier reconstructs every independent subset, all \(384\) automorphisms, their action on independent face masks and all flag orbits. It proves the flag coverage by an independent ordered-Bell count, independently reconstructs every orbit-cell incidence, and checks every collapse against the then-surviving cell poset. Its final line is:

`VERIFY_OK_Q4_INDEPENDENCE_FULL_ORBIT_COLLAPSIBLE faces=742 flags=2199938 group=384 cells=6721 collapses=3360 remaining_vertex=0`

The independently supplied `compute_q4_orbit.cpp` reconstructs and regenerates the entire certificate. Compile with `g++ -std=c++17 -O2 compute_q4_orbit.cpp -o compute_q4_orbit`, then run `./compute_q4_orbit q4_orbit_certificate.txt`; the Python verifier then checks it. These computations are exhaustive over a completely specified *finite* universe, not experiments supporting an extrapolation to higher-dimensional cubes.

## Relationship to prior work

Kozlov's work on simple homotopy and elementary collapses [1] provides a classical methodological setting, not this particular full-orbit calculation. Bousquet-Mélou, Linusson, and Nevo [2] study the independence complexes of open and cylindrical square grids and explain limitations of their methods for toroidal grids. Barmak's general graph-independence theorems [3] do not identify this geometric full-symmetry quotient. Jonsson [4] studies crosspolytope homology cycles of periodic grids, but its full text was not accessible in the present literature comparison; its abstract is not evidence of a full quotient calculation.

The exact four-cube independence complex was previously shown to be \(\bigvee^7S^3\) [5]. Its full rational homology representation was determined [6,7], and in particular the ordinary full-group quotient was **already known to be rationally acyclic** [7]. A further work [8] determined the full integral representation lattice in degree three. None of the inspected claims, proofs, or supplied results identifies the integral homotopy or simple-homotopy type of the ordinary quotient. Rational acyclicity and even the integral representation lattice do not imply contractibility: they do not preclude torsion, nontrivial fundamental group, or a nontrivial simple-homotopy type of the quotient. The new assertion is specifically the complete \(3360\)-pair collapse to a point.

## Limitations

Only the sixteen-vertex four-cube and the ordinary quotient by its full automorphism group are covered. This is not a classification of all group quotients of cube independence complexes, nor a general result in arbitrary cube dimension. Its correctness uses a finite exhaustive computation; the accompanying independent certificate verifier provides direct proof replay, while no outside scientific validation is asserted. Originality is relative to literature inspected and indexed results, not a proof that an equivalent unindexed calculation cannot exist. Jonsson's directly related periodic-grid paper could be inspected only through bibliographic information and abstract; an equivalent hidden result there cannot be categorically ruled out, though its stated focus is different.

## References

[1] D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, first posted 2005-03-28, arXiv:math/0503613. https://arxiv.org/abs/math/0503613

[2] M. Bousquet-Mélou, S. Linusson, E. Nevo, *On the independence complex of square grids*, first posted 2007-01-30, arXiv:math/0701890. https://arxiv.org/abs/math/0701890

[3] J. A. Barmak, *Star clusters in independence complexes of graphs*, first posted 2010-07-02, arXiv:1007.0418. https://arxiv.org/abs/1007.0418

[4] J. Jonsson, *Certain Homology Cycles of the Independence Complex of Grids*, Discrete & Computational Geometry 43 (2010), 927–950, DOI:10.1007/s00454-009-9224-9. https://doi.org/10.1007/s00454-009-9224-9

[5] *The four-cube independence complex is a wedge of seven three-spheres*, published result. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-four-cube-independence-complex-is-a-wedge-of-seven-three-sph--9947aaad144c/RESULT.md

[6] *The full hyperoctahedral homology representation of the four-cube independence complex*, published result. https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-the-full-hyperoctahedral-homology-representation-of-the-four-cub--d5fe6b1e159f/RESULT.md

[7] *Complete hyperoctahedral homology character of the four-cube independence complex*, published result. https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-complete-hyperoctahedral-homology-character-of-the-four-cube-ind--70251f458fd4/RESULT.md

[8] *Eight minimum-support octahedral spheres give the integral hyperoctahedral module of the four-cube independence complex*, published result. https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-eight-minimum-support-octahedral-spheres-give-the-integral-hyper--1740b146ec04/RESULT.md
