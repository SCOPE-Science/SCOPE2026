# Facet-gluing twists change the connectivity of doubled polygon-join spheres

## Finding
Let \(m,n\ge4\) be integers and assume **at least one is odd**. Denote by \(C_m\) and \(C_n\) the *unfilled* simplicial polygons of the stated lengths, with vertices \(a_i\) and \(b_j\) (indices cyclic). Let \(X=C_m*C_n\), a triangulated three-sphere. Choose the tetrahedron \(F=\{a_0,a_1,b_0,b_1\}\). Let \(Z_\phi\) be the simplicial connected sum of two copies of \(X\), obtained by removing \(F\) as a maximal face on each copy and identifying their tetrahedral boundaries using a bijection \(\phi\) of the four vertices.

**Theorem.** Let \(P=\{\{a_0,a_1\},\{b_0,b_1\}\}\) be the marked perfect matching of the four vertices of \(F\). If \(\phi(P)=P\), the simplicial double \(D^2(Z_\phi)\) has precisely two components of respective integral homotopy types
\[
\bigvee^{2mn-2m-2n+1} S^1\qquad\text{and}\qquad\bigvee^{2mn+1} S^1.
\]
If \(\phi(P)\ne P\), its double is connected and has integral homotopy type
\[
D^2(Z_\phi)\simeq \bigvee^{4mn-2m-2n+1} S^1.
\]
Exactly \(8\) of the \(24\) bijections preserve the marked matching. In both cases the doubled graph has \(2(m+n+mn)-6\) vertices and \(6mn-6\) edges.

For \((m,n)=(4,5)\), these give respectively two wedges of \(23\) and \(41\) circles, or one wedge of \(63\) circles. The corresponding simplicial three-spheres have the identical face vector \((14,52,76,38)\); the change in double connectivity is caused solely by the facet identification.

## Assumptions and scope
For a finite simplicial complex \(Y\), the double \(D^2(Y)\) has a vertex for each edge of \(Y\); two such vertices span an edge precisely when the original edges are disjoint and together form a tetrahedron of \(Y\). Since each \(Z_\phi\) has dimension three, its double is a graph (no triangles or higher-dimensional faces). A simplicial connected sum along tetrahedral facets removes those two top-dimensional simplices but retains and identifies the full boundaries. Every resulting \(Z_\phi\) is a combinatorial three-sphere: it is two punctured three-spheres glued along their bounding two-spheres.

The parity assumption is essential for the stated two-component decomposition of the *unglued* double. We make no claim for the even-even case. All homology and homotopy assertions are integral, and \(\bigvee^rS^1\) means a wedge of exactly \(r\) circles (where all displayed ranks here are positive).

## Proof
**1. Double of one polygon join.** Every tetrahedral facet is \(\{a_i,a_{i+1},b_j,b_{j+1}\}\), with \(mn\) choices. There are \(m+n\) same-factor edges and \(mn\) cross-factor edges in \(X\). Of the three opposite-edge partitions of each tetrahedron, one pairs its same-factor edges. These edges in the double form the complete bipartite graph \(A=K_{m,n}\) on the \(m\) first-factor cycle edges and \(n\) second-factor cycle edges. The other two partitions pair cross-factor edges, and form \(B=C_m\times C_n\), the **categorical** graph product: its vertices are \((i,j)\), and it has edges \((i,j)\sim(i\pm1,j\pm1)\). Thus \(D^2(X)=A\sqcup B\). The group generated in \(\mathbb Z/m\times\mathbb Z/n\) by \((1,1)\) and \((1,-1)\) has index \(\gcd(2,m,n)\). Since at least one length is odd, \(B\) is connected. Here \(A\) has \(m+n\) vertices and \(mn\) edges, while \(B\) has \(mn\) vertices and \(2mn\) edges.

**2. Excising the marked tetrahedron does not disconnect the pieces.** Removing \(F\) deletes one edge of \(A\), which remains connected since \(m,n\ge4\). It also deletes precisely two edges of \(B\): with vertex coordinates \((0,0),(1,1)\) and \((0,1),(1,0)\). Each admits a three-edge detour avoiding *both* deleted edges:
\[
(0,0)\to(1,-1)\to(2,0)\to(1,1),
\]
\[
(0,1)\to(1,2)\to(2,1)\to(1,0).
\]
The bounds \(m,n\ge4\) guarantee that no detour traverses a deleted edge. Replacing the deleted edges by these detours in any original path proves that the punctured graph \(B^-\) remains connected. The punctured \(A^-\) is also connected. On the six double vertices arising from the edges of \(F\), exactly the two marked same-factor edges belong to \(A^-\); the other four belong to \(B^-\).

**3. Effect of gluing.** The double of the connected sum is obtained by taking two copies of \(A^-\sqcup B^-\), then identifying their six boundary double vertices using the edge bijection induced by \(\phi\). This follows directly from the definition: all tetrahedra except the excised ones remain in one original summand, and the six edges of the identified tetrahedral boundaries are the only identified graph vertices. The gluing adds no new tetrahedra and hence no new edges of the double.

If \(\phi(P)=P\), the two pairs of connected \(A^-\) pieces glue to one component and the two connected \(B^-\) pieces glue to another, since all six port identifications preserve the partition of sizes two and four. Otherwise an \(A^-\) port on one side is identified to a \(B^-\) port on the other. Because the two perfect matchings differ, the port identifications connect **all four** previously connected pieces; the resulting double is connected. A vertex permutation preserves an unordered perfect matching exactly when it belongs to its order-eight stabilizer in \(S_4\), leaving sixteen mixing permutations.

**4. Ranks and homotopy.** Prior to gluing, each punctured \(A^-\) has \(m+n\) vertices and \(mn-1\) edges; each punctured \(B^-\) has \(mn\) vertices and \(2mn-2\) edges. In the aligned case, identifying their two (respectively four) port vertices yields component size pairs
\[
(v_A,e_A)=(2(m+n)-2,\,2mn-2),\quad
(v_B,e_B)=(2mn-4,\,4mn-4).
\]
The connected graph cycle ranks \(e-v+1\) are therefore \(2mn-2m-2n+1\) and \(2mn+1\). In the mixing case, all six port identifications lie in one connected graph, with
\[
(v,e)=(2(m+n+mn)-6,\,6mn-6),
\]
and rank \(4mn-2m-2n+1\). Any connected finite graph contracts a spanning tree to a wedge of exactly its cycle rank many circles. This proves the full integral homotopy assertions.

The face vector of \(X\) is \((m+n,\,m+n+mn,\,2mn,\,mn)\). Subtracting the duplicated tetrahedral boundary faces and the two excised tetrahedra gives the \(\phi\)-independent connected-sum vector
\[
\bigl(2(m+n)-4,\;2(m+n+mn)-6,\;4mn-4,\;2mn-2\bigr).
\]

## Verification
The standalone program `check_sphere_double_sum.py` constructs every tetrahedron of the join directly, independently constructs all double vertices and opposite-edge adjacency relations, and constructs facet-glued connected sums from explicit vertex equivalence classes. It checks the closed formulas for both the aligned and mixed identifications for **16** integer pairs \((m,n)\) with \(4\le m,n\le8\) and at least one odd. A second standalone program, `validate_gluing_types.py`, enumerates **all 24** tetrahedral identifications at \((4,5)\): exactly eight have two components with cycle ranks \((23,41)\), and sixteen have a single component of rank \(63\). Run both with `python3`; Python's standard library is sufficient. Exact observed output is included in `verification_output.txt`.

The numerical experiments are finite checks only; the unrestricted assertion follows from the four-step symbolic proof above. The executable programs independently reconstruct complexes from facets rather than inputting their asserted double decomposition.

## Relationship to prior work
Lesh, Schreiner and Wahl introduced simplicial doubling and proved a broad weak Cohen–Macaulay connectivity estimate; that theorem does not determine the dependence of a three-sphere's double on a tetrahedral connected-sum gluing. The existing exact decomposition for \(D^2(C_m*C_n)\) concerns the **unglued** sphere. Its two graph components are input data; it does not describe removal of a facet, the six-port identification, or the two homotopy outcomes depending on a matching stabilizer. A published calculation for doubles of cyclic four-polytope boundaries concerns different triangulations and a parity transition, not a connected-sum gluing dependence.

The contribution here is the uniform *gluing-twist dichotomy*, its exact integral homotopy ranks, and equal-face-vector examples of connectivity change. These conclusions are not claimed for general three-sphere connected sums.

## Limitations
The proof is restricted to two identical polygon-join spheres with \(m,n\ge4\) and at least one odd. The even-even case can have additional components before gluing and is excluded. An unpublished or differently formulated connected-sum calculation might still cover these examples; the checked source comparisons do not constitute an independent novelty certification. No assertion about the fundamental group of the **original** three-spheres differs between the two gluings, and no equivariant homotopy decomposition is claimed.

## References
1. Kathryn Lesh, Bridget Schreiner, Nathalie Wahl, *The double of a simplicial complex*, arXiv:2506.10436, first public version June 12, 2025; sections 1–3 (definition 2.1 and theorem A). https://arxiv.org/abs/2506.10436
2. *Parity components and contractible symmetry quotients in doubles of joined polygons*, previously established exact decomposition for an unglued polygon join (scientific comparison of statement and hypotheses).
3. *Parity and dihedral homology of the doubled cyclic four-polytope boundary*, published research finding (comparison of related but different simplicial spheres).
