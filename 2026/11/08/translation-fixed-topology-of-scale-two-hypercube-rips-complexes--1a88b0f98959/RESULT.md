# Translation-fixed topology of scale-two hypercube Rips complexes

## Finding
For every integer \(n\geq 2\), identify the vertices of the binary hypercube \(Q_n\) with \(\mathbb F_2^n\), equipped with Hamming distance. Let \(X_n=\operatorname{VR}(Q_n;2)\) be the *inclusive* Vietoris–Rips simplicial complex: a finite vertex set is a face precisely when all its pairwise Hamming distances are at most two. The additive group \(T_n=\mathbb F_2^n\) acts by translations.

**Theorem (all nontrivial translation subgroups).** Let \(0\neq H\leq T_n\). Write \(\operatorname{wt}(h)\) for Hamming weight and \(d=\dim_{\mathbb F_2}H\). There are precisely three possibilities for the *geometric* fixed-point space:
\[
 |X_n|^H\ \cong_{\mathrm{PL}}\
 \begin{cases}
 |Q_{n-1}|,& d=1\text{ and }\operatorname{wt}(h)\in\{1,2\}\text{ for }H=\{0,h\},\\
 \displaystyle\coprod_{j=1}^{2^{n-2}}\{\mathrm{point}\},&d=2\text{ and }\max_{h\in H}\operatorname{wt}(h)\leq2,\\
 \varnothing,&\text{otherwise}.
 \end{cases}
\]
Here \(|Q_{n-1}|\) is the one-dimensional graph realization (NOT the cubical ball). Thus the first case is homotopy equivalent to \(\bigvee^{\,1+(n-3)2^{n-2}}S^1\), including the contractible case \(n=2\). The second has reduced integral zeroth homology of rank \(2^{n-2}-1\); no other reduced homology occurs in either case.

In the second case, \(H\) is necessarily, up to coordinate permutation, either the coordinate plane \(\langle e_1,e_2\rangle\) or the even-weight two-plane \(\langle e_1+e_2,e_1+e_3\rangle\). No translation subgroup of rank three or higher has geometric fixed points at this scale.

For example, at \(n=4\), every one-coordinate or two-coordinate translation involution fixes the graph \(Q_3\) up to PL homeomorphism: this is a wedge of five circles, even though the ambient complex has reduced integral homology concentrated in degree three.

## Assumptions and scope
All groups are finite. Fixed points mean points of the geometric realization fixed simultaneously by all elements of \(H\), **not** the simplicial subcomplex on fixed vertices (indeed a nonzero translation fixes no original vertex). The action is the ordinary simplicial action induced by translating binary words. The fixed-set homeomorphisms are nonequivariant; no normalizer-equivariant splitting is asserted. The graph realization \(|Q_{n-1}|\) has edges but no higher-dimensional cube cells.

## Proof
**1. Orbit-barycenter model.** For a finite simplicial complex \(K\) with simplicial \(H\)-action, each fixed point has barycentric weights constant on every vertex orbit. Its support is an invariant face. Conversely, assigning weights to the barycenters of whole vertex orbits gives exactly the fixed points. Therefore \(|K|^H\) is PL homeomorphic to the realization of the orbit complex \(K_H\): its vertices are those \(H\)-orbits that are themselves faces, and several orbit vertices span a simplex precisely when the union of their underlying orbits is a face. The barycenters have disjoint supports, so this map is a homeomorphism on each simplex, compatible across intersections.

**2. Which subgroups have admissible orbits?** The vertex orbits of \(H\) on \(Q_n\) are the cosets \(x+H\). Their diameter is the common number \(\max_{h\in H}\operatorname{wt}(h)\). Hence if some element of \(H\) has weight at least three, the orbit complex has no vertices and the fixed-point space is empty.

Suppose now that all nonzero elements of \(H\) have weight at most two. If \(H\) contains a weight-one element \(e_i\), then any independent element of weight at most two must be either \(e_j\) or \(e_i+e_j\) for some \(j\ne i\), since a disjoint weight-two word would have a weight-three sum with \(e_i\). Any further independent element has a weight-three-or-more sum with an element of the resulting coordinate plane. Thus \(H\) has dimension at most two and, if dimension two, is a coordinate plane.

If \(H\) has no weight-one element, all its nonzero elements have weight two. Two independent words have supports meeting in exactly one coordinate (otherwise their sum has weight four). After relabeling these are \(e_1+e_2\) and \(e_1+e_3\), whose sum is \(e_2+e_3\). A further independent weight-two word would have to intersect each of these three supports in exactly one coordinate; none exists outside their span. Thus \(H\) again has rank at most two, and in rank two it is the even-weight plane on three coordinates.

**3. Rank two.** Every coset \(x+H\) is an admissible orbit. Two distinct cosets can never form an orbit-complex edge: for the coordinate plane, their difference is nonzero outside the two support coordinates, and adding a suitable element of \(H\) produces two ones inside as well, giving distance at least three. For the even-weight plane on three coordinates, a difference outside \(H\) either has a nonzero outside coordinate (in which case one may choose an element of \(H\) to leave two ones inside) or has odd parity in the three coordinates (in which case one may choose an element to obtain three ones inside). In either case the union has diameter at least three. All \(2^{n-2}\) cosets therefore become isolated vertices.

**4. Rank one generated by weight one.** Permute coordinates so that \(H=\langle e_1\rangle\). Represent its \(2^{n-1}\) cosets by \((0,z)\), with \(z\in\mathbb F_2^{n-1}\). The maximal distance between vertices of two distinct cosets is \(1+\operatorname{wt}(z-z')\). Therefore they form an edge exactly when \(\operatorname{wt}(z-z')=1\). The orbit complex is exactly the graph \(Q_{n-1}\), with no triangles and hence no higher faces.

**5. Rank one generated by weight two.** Permute coordinates so that \(H=\langle e_1+e_2\rangle\). Represent cosets by \((0,b,z)\), with \(b\in\mathbb F_2\) and \(z\in\mathbb F_2^{n-2}\). Two distinct cosets have union of diameter at most two exactly when their \(b\)-coordinates differ and their \(z\)-coordinates differ in at most one place. Thus the orbit graph is the Cayley graph of \(\mathbb F_2^{n-1}\) with generating vectors \((1,0)\) and \((1,e_j)\) for \(1\le j\le n-2\). These \(n-1\) vectors form a basis. A linear change of coordinates identifies this graph with \(Q_{n-1}\). It is bipartite, so the orbit complex has no higher faces. This completes the PL-homeomorphism classification.

Finally \(Q_{n-1}\) is connected and has \(2^{n-1}\) vertices and \((n-1)2^{n-2}\) edges. Its first Betti number is \(1+(n-3)2^{n-2}\). All these graphs and discrete sets have torsion-free integral homology.

## Verification
A separate exhaustive enumerator, `verify.py`, constructs *all* binary linear subspaces by closure under span for dimensions \(2\le n\le6\). For each nonzero subgroup it independently lists cosets, accepts orbit vertices by pairwise diameter tests, determines orbit-complex edges by all underlying pairwise distances, tests for triangles, and compares the resulting graph with the predicted cube or discrete set. All \(3,282\) nontrivial subgroups in these dimensions passed. The program also verifies every eligible rank-one subgroup in dimensions seven and eight, yielding \(3,346\) total tested subgroups. The recorded result is `ALL_VERIFY_OK`. This finite enumeration corroborates but does not replace the all-dimensional proof.

Run from a directory containing `verify.py` and install the dependency listed in `requirements.txt`; execute `python verify.py`. The recorded output is `verify_output.txt`.

## Relationship to prior work
Adamaszek and Adams established the nonequivariant wedge-of-three-spheres homotopy type of \(\operatorname{VR}(Q_n;2)\). Bendersky, Elia, and Grbić (arXiv:2605.00705, first posted 2026-05-01) treat connectivity, cohomology, and explicit cross-polytope classes. Galetto, Montaño, and Wellner (arXiv:2606.20784, posted 2026-06-18) determine characteristic-zero homology representations of the full hyperoctahedral group. Their accessible full research text concerns *ambient* homology and representation theory rather than geometric fixed-point homeomorphism types of every translation subgroup. The present theorem identifies fixed-point spaces at the level of homeomorphism, which cannot be read off merely from rational ambient homology characters. Existing general equivariant Rips and orbit-complex methods provide background, not this parameter-complete classification.

A related published mathematical record determines a symmetry character for the **intrinsic Čech** complex of binary hypercubes; this is a different simplicial complex from the Vietoris–Rips complex considered here. Another record concerns the **penultimate** Rips scale and gives a graph-theoretic reduction of the ambient complex, not subgroup fixed-point homeomorphisms.

## Limitations
Only the *translation* subgroup lattice is classified, not arbitrary affine automorphisms combining translations and coordinate permutations. The statement is restricted to inclusive Rips scale two and binary hypercubes. It does not compute the normalizer action on the fixed-point homology or provide an equivariant splitting of the ambient space. Searches and inspected source text cannot rule out equivalent results in unindexed or inaccessible literature. Independent mathematical audit has not been performed.

## References
1. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (first posted 2021-03-01). https://arxiv.org/abs/2103.01040
2. M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips Complex of a Hypercube Graph*, arXiv:2605.00705 (first posted 2026-05-01). https://arxiv.org/abs/2605.00705
3. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first posted 2026-06-18). https://arxiv.org/abs/2606.20784
4. M. Varisco and M. C. B. Zaremsky, *Equivariant Morse theory on Vietoris–Rips complexes and universal spaces for proper actions*, arXiv:1909.04487 (first posted 2019-09-10). https://arxiv.org/abs/1909.04487
