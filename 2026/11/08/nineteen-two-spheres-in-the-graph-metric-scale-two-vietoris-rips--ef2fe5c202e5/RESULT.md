# Nineteen two-spheres in the graph-metric scale-two Vietoris–Rips complex of the Desargues graph

## Finding
For the 20-vertex Desargues graph \(D=GP(10,3)\) with intrinsic unit-edge shortest-path distance, the inclusive radius-two Vietoris–Rips complex has integral homotopy type
\[
\operatorname{VR}_{\le2}(V(D),d_D)\simeq\bigvee^{19}S^2.
\]
It is simply connected, with \(\widetilde H_2\cong\mathbb Z^{19}\) and other reduced integral homology zero. The exact original face vector in dimensions zero through three is \((20,90,120,30)\).

## Assumptions and scope
Define \(GP(10,3)\) on 20 vertices \(u_i,v_i\), with \(i\in\mathbb Z/10\mathbb Z\), by the edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\), one of each kind for each \(i\). Give every edge length one; \(d_D\) denotes shortest-path graph distance. A nonempty set \(\sigma\) is a simplex precisely when \(d_D(x,y)\le2\) for every pair \(x,y\in\sigma\). This is not a geometric realization metric, an independence complex, a matching complex, or a Čech nerve.

## Proof
**Finite combinatorial model.** The accompanying `verify_desargues.py` builds the 30-edge graph directly from the displayed modular edge equations and computes all 20 breadth-first distance tables. By exhaustive testing of all pairs, triples, quadruples and five-subsets of its 20 vertices, it constructs exactly 20 zero-faces, 90 edges, 120 triangles, 30 tetrahedra and zero simplices with at least five vertices (if a larger clique existed it would contain a five-clique). Every claimed face is tested using the original graph metric, not a derived or weighted metric.

**Dimension reduction.** For every tetrahedron, consider its three-dimensional cofacets. The verifier recursively chooses a triangle contained in exactly one remaining tetrahedron and deletes the pair. In each of 30 iterations, it independently checks against *all remaining faces of greater dimension* that the chosen triangle is free. The resulting complex \(L\) has 20 vertices, 90 edges and 90 triangles, and \(|K|\simeq|L|\) by elementary collapses.

**Fundamental group.** A spanning tree of the 90-edge one-skeleton of \(L\) has 19 edges. A standard edge-path presentation of \(\pi_1(L)\) therefore has 71 generators (one per non-tree edge) and one relator for each of the 90 oriented triangle boundaries. Each relator is an explicit cyclically reduced word of at most three generators, formed using the orientations \(a<b\). The verifier checks 71 successive, exact Tietze eliminations: in each selected relator a generator occurs exactly once, so it is explicitly solved as a word in the other generators and substituted into *every* remaining relator; immediate cancellations and cyclic conjugations do not change the presented group. All 71 generators and every relator disappear. Consequently \(\pi_1(L)=1\). This is a nonabelian verification, not an inference from \(H_1=0\).

**Integral homotopy type.** Since \(L\) is a connected finite two-dimensional complex and \(\pi_1(L)=1\), its second homology is free abelian and \(H_1=0\). The Euler characteristic is \(20-90+90=20\), hence \(H_2(L;\mathbb Z)\cong\mathbb Z^{19}\). By the Hurewicz theorem, 19 classes in \(\pi_2(L)\) can be chosen to map to a basis of \(H_2(L;\mathbb Z)\), yielding a map \(\bigvee^{19}S^2\to L\) inducing an isomorphism on all integral homology. Both spaces are simply connected CW complexes, so Whitehead's theorem gives a homotopy equivalence. Together with the collapses this proves the finding.

## Verification
Run `python3 verify_desargues.py` from the directory containing that file. It uses only the Python standard library; no third-party graph data, hidden input files or random seed. The exact output is embedded in `verification_output.txt`. The checker tests each simplicial-collapse freeness condition and all 71 Tietze substitutions. A separate mod-two boundary computation gives ranks 19 and 71 and Betti numbers 0 and 19 in dimensions one and two, consistent with (but not substituting for) the nonabelian and integral argument.

## Relationship to prior work
Adams, Adetowubo, Barriga-Acosta, Feng and Sterling (first posted 2025-02-10, arXiv:2502.07134) study graph-metric Rips topology of torus grids, not this canonical girth-six cubic graph. Adamaszek (2011, arXiv:1104.0433) studies clique complexes of graph powers and includes the high-girth regime; this specific girth-six boundary graph requires separate calculation. A related indexed calculation gives the graph Čech nerve of the Desargues graph at radius 3/2 as a wedge of 49 two-spheres, which is a distinct simplicial construction. Indexed computations for independence and matching complexes of the same Desargues graph also treat different functors. Searches under the generalized-Petersen name, the Desargues–Levi name and scale-two graph Rips terminology found no equivalent 19-sphere determination; lack of an indexed result is not a proof of absolute novelty.

## Limitations
The claim concerns only the 20-vertex graph \(GP(10,3)\) at inclusive threshold two, not all generalized Petersen graphs, arbitrary cubic girth-six graphs or larger scales. The exact certificate and Tietze argument determine the ordinary homotopy type, but not an equivariant splitting or persistence maps. Literature indexing can miss relevant equivalent results. Independent review has not been performed.

## References
- H. Adams, B. Adetowubo, J. Barriga-Acosta, Z. Feng, R. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134 (first public 2025-02-10).
- M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (2011).
- Related graph Čech nerve calculation: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-scale-three-ech-nerve-of-the-desargues-graph-is-a-wedge-of-49-tw--eac77c714390 .
