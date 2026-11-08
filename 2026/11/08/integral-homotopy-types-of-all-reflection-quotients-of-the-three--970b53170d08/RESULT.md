# Integral homotopy types of all reflection quotients of the three-by-four grid matching complex

## Finding
Let \(G=P_3\square P_4\) be the ordinary nearest-neighbor rectangular grid, let \(X=\mathcal M(G)\) be its matching complex, and let \(R\) reverse the three rows while \(C\) reverses the four columns. The natural full grid automorphism group is \(K=\langle R,C\rangle\cong C_2\times C_2\). For the **geometric orbit quotient** of \(|X|\), not the Borel construction, the four nontrivial subgroup quotients have exact **integral homotopy types**
\[
\begin{aligned}
|X|/\langle R\rangle&\simeq\bigvee^{5}S^3,\\
|X|/\langle C\rangle&\simeq\bigvee^{4}S^3,\\
|X|/\langle RC\rangle&\simeq\bigvee^{6}S^3,\\
|X|/K&\simeq\bigvee^{3}S^3.
\end{aligned}
\]
All four quotients are simply connected, have torsion-free integral homology concentrated in degree three, and have no nonzero reduced homology in other degrees. This four-part classification is a single claim about the complete nontrivial subgroup lattice of the natural rectangle symmetry group. The unquotiented homotopy type \(X\simeq\bigvee^9 S^3\) is an input, independently checked here, and is not claimed as a new result.

## Assumptions and scope
The graph has vertices \((i,j)\), \(0\leq i<3\), \(0\leq j<4\), with edges between pairs of Manhattan distance one. A matching is a subset of the seventeen graph edges no two of which share a vertex; its edge-set is a simplex in \(X\). The involutions are \(R(i,j)=(2-i,j)\) and \(C(i,j)=(i,3-j)\), acting on matching edges and on the geometric realization. The letter \(K\) denotes their Klein-four group. The topological quotient is the quotient space by the **actual geometric action**, so a simplex permuted nontrivially by a stabilizer is not naively identified with a simplex on vertex orbits. All homology is unreduced in degree zero and reduced otherwise.

## Proof
**1. An independently verified integral Morse model for the unquotiented complex.** Label the graph edges by zero-based indices: first the eight vertical edges in row-major column order, then the nine horizontal edges in row-major order. Enumerate a simplex exactly when its edges are pairwise vertex-disjoint. The resulting counts, from dimensions zero through five, are
\[
(17,102,267,302,123,11).
\]
Use the pivot order
`(5,12,6,7,13,8,9,10,4,3,14,15,11,1,0,16,2)`.
At each pivot, match every still-unmatched face not containing that pivot with the face obtained by adding it, if both are present and still unmatched. This constructs exactly \(406\) disjoint codimension-one face pairs and leaves **one zero-dimensional** and **nine three-dimensional** critical faces. Independently orient every unmatched Hasse incidence downward and every matched incidence upward. The explicit finite directed graph has \(822\) vertices and \(2,894\) cover incidences; a full topological sort removes all \(822\) vertices, proving acyclicity. Forman's discrete-Morse theorem therefore gives a CW model with one zero-cell and nine three-cells and no others:
\[
X\simeq\bigvee^{9} S^3.
\]
In particular \(X\) is simply connected and its integral homology is free.

**2. Exact quotient chain complexes, with stabilizers handled correctly.** The barycentric subdivision has one vertex per nonempty face of \(X\) and a \(k\)-simplex for every strict chain of \(k+1\) nonempty faces. Direct enumeration gives \(144{,}500\) such chains. The \(K\)-action (and each subgroup action) preserves face cardinality, so it is **without inversions** on this subdivision: any group element stabilizing a chain preserves each rank and fixes all vertices of the chain. Therefore each geometric quotient has a regular orbit-cell decomposition with one \(k\)-cell per group orbit of \(k\)-chains. Its integral cellular boundary, in increasing face-cardinality orientation, is
\[
\partial [F_0\subsetneq\cdots\subsetneq F_k]
  =\sum_{j=0}^{k}(-1)^j
   [F_0\subsetneq\cdots\widehat{F_j}\cdots\subsetneq F_k],
\]
with repeated target-orbit incidences added with their proper multiplicities. In particular, reduction modulo two yields the exact quotient boundary matrices checked by `verify.py`, **not** the generally incorrect boundary matrices of a naive vertex-orbit simplicial complex.

Here is the exhaustive certificate. Each row lists the quotient cell counts by dimensions \(0,\dots,5\), the ranks of its mod-two boundary maps \(d_1,\dots,d_5\), and its mod-two Betti numbers \(b_0,\dots,b_5\):

| Group | Cell counts | Mod-two boundary ranks | Mod-two Betti numbers |
|---|---|---|---|
| \(\langle R\rangle\) | \(423,5239,18468,26976,17280,3960\) | \(422,4817,13651,13320,3960\) | \(1,0,0,5,0,0\) |
| \(\langle C\rangle\) | \(444,5331,18576,27012,17280,3960\) | \(443,4888,13688,13320,3960\) | \(1,0,0,4,0,0\) |
| \(\langle RC\rangle\) | \(429,5246,18456,26964,17280,3960\) | \(428,4818,13638,13320,3960\) | \(1,0,0,6,0,0\) |
| \(K\) | \(237,2705,9318,13512,8640,1980\) | \(236,2469,6849,6660,1980\) | \(1,0,0,3,0,0\) |

The executable independently builds the face poset, all flags, orbit maps and boundary columns, verifies the boundary-square identity, and uses exact \(\mathbf F_2\) pivot elimination. Thus the finite ranks above are exhaustive, not samples or floating-point estimates.

**3. Rational and integral homology.** For any subgroup \(H\leq K\), the subdivision-chain orbit complex over \(\mathbb Q\) is the coinvariant complex of \(C_*(\mathrm{sd}\,X;\mathbb Q)\). The coinvariant functor for a finite group is exact over \(\mathbb Q\), so
\[
H_i(|X|/H;\mathbb Q)\cong H_i(X;\mathbb Q)_H.
\]
By step 1, reduced rational homology is zero except possibly in degree three. The alternating sums of the four displayed quotient cell vectors give the ordinary Euler characteristics \(-4,-3,-5,-2\); hence the **rational** third Betti numbers are, respectively, \(5,4,6,3\). They agree exactly with the independently computed mod-two Betti numbers.

The same coinvariant argument works over \(\mathbb Z[1/2]\), because every subgroup order is a power of two and hence invertible there. As \(H_*(X;\mathbb Z[1/2])\) is free, its finite-group coinvariants are direct summands of free \(\mathbb Z[1/2]\)-modules and have no odd-primary torsion. Agreement between all mod-two Betti numbers and rational Betti numbers, together with the universal coefficient theorem, rules out **all** two-primary torsion in every degree. Thus each quotient has free integral homology solely in degree three with the corresponding rank.

**4. Fundamental groups and homotopy types.** The horizontal grid edge in the middle row between the two central columns is preserved setwise by **every** symmetry in \(K\); it is therefore a common fixed *vertex* of the matching complex. By the finite-group orbit-space fundamental-group theorem (Armstrong), since \(X\) is simply connected and every element of each subgroup fixes a point, all four quotient spaces are simply connected. Their vanishing integral second homology then implies vanishing \(\pi_2\), by Hurewicz. Consequently the degree-three Hurewicz maps are isomorphisms. Choose a \(\mathbb Z\)-basis of each free third homology group, represent it by maps of three-spheres, and wedge those maps. The resulting map from the corresponding sphere bouquet is an integral homology equivalence between simply connected CW complexes; the homological Whitehead theorem makes it a homotopy equivalence. This proves all four boxed decompositions.

## Verification
Run `python3 verify.py` from the standalone package. It uses only the Python standard library and prints `ALL_VERIFY_OK` after rebuilding everything from the graph definition, checking every incidence and chain-orbit boundary, and verifying the asserted exact mod-two ranks. The recorded exact output is in `verification_output.txt`. The finite checker is part of the proof certificate for the finite combinatorial calculations; the deductions about odd-primary torsion, fundamental groups and integral homotopy types use the mathematical arguments above. The independent signed-chain Lefschetz calculations obtain row, column and half-turn traces \(1,-1,3\) on the known nine-dimensional rational third homology, providing a second check of the rational ranks.

## Relationship to prior work
Chauhan, Sharma and Shukla, arXiv:2609.27366v1 (first publicly posted September 23, 2026), prove general connectivity and homology bounds for three-row grid matching complexes and explicitly tabulate the **unquotiented** homology, including rank nine at width four. Their Conjecture 4.1 concerns the unquotiented complexes, not the geometric symmetry orbit spaces.

The published mathematical records *Orthogonal-reflection Lefschetz formulas for \(3\times n\) grid matching complexes* and *Half-turn Lefschetz characters and full symmetry quotients of \(3\times n\) grid matching complexes* determine alternating rational symmetry traces and the Klein-four quotient's Euler characteristic for every width. Those prior formulas already imply the **rational ranks** here when combined with the known concentration of unquotiented homology. The present claim is strictly more topological: it determines the four geometric quotients' integral homology, excludes two-primary torsion by exhaustive quotient boundary computations, proves their fundamental groups vanish, and thereby determines their full integral homotopy types. No new all-width Lefschetz formula or unquotiented Betti number is claimed.

## Limitations
The four classifications concern this one natural \(3\times4\) rectangle and the three order-two subgroups and full subgroup of its natural Klein-four automorphism group. They do not prove the all-width wedge conjecture, determine quotient spaces at other widths, or identify equivariant homotopy splittings of the unquotiented space. The finite computational certificate is exhaustive for this rectangle only. An equivalent implicit quotient-homotopy argument in an unindexed source remains possible.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366v1 (2026-09-23), https://arxiv.org/html/2609.27366, Theorems 1.2–1.3 and Table 1 / Conjecture 4.1.
2. *Orthogonal-reflection Lefschetz formulas for \(3\times n\) grid matching complexes*, public mathematical record (2026-10-11), exact full text compared for its rational trace formulas.
3. *Half-turn Lefschetz characters and full symmetry quotients of \(3\times n\) grid matching complexes*, public mathematical record (2026-10-11), exact full text compared for its quotient Euler formulas and explicit limitation to alternating rational homology.
4. M. A. Armstrong, *The fundamental group of the orbit space of a discontinuous group*, Proc. Cambridge Philos. Soc. 64 (1968), 299–301; used for the simply-connected quotient conclusion.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145; used for the explicit acyclic matching.
