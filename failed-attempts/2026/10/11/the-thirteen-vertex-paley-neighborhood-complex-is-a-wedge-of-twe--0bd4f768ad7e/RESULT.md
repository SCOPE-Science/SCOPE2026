# The thirteen-vertex Paley neighborhood complex is a wedge of twenty-five two-spheres

## Finding
Let \(P_{13}\) be the Paley graph with vertex set \(\mathbb F_{13}\) and edges \(\{u,v\}\) whenever \(u-v\) is a nonzero quadratic residue. Its **open** Lovász neighborhood complex, whose nonempty faces are vertex sets sharing a graph neighbor, has the integral homotopy type
\[
\mathcal N(P_{13})\simeq\bigvee^{25}S^2.
\]
In particular, it is simply connected, its only nonzero reduced integral homology group is \(\widetilde H_2\cong\mathbb Z^{25}\), and it has no integral homology torsion. Furthermore \(\chi(P_{13})=5\), while Lovász's lower bound based on the ordinary connectivity of \(\mathcal N(P_{13})\) gives \(\chi(P_{13})\ge4\), a strict one-color gap.

## Assumptions and scope
The vertex labels are the integers \(0,1,\ldots,12\) reduced modulo \(13\). The nonzero quadratic residues are exactly
\[
Q=\{1,3,4,9,10,12\}.
\]
Thus \(N(v)=v+Q\), without including \(v\) itself. A nonempty set \(\sigma\) is a face of \(\mathcal N(P_{13})\) exactly when \(\sigma\subseteq v+Q\) for some \(v\in\mathbb F_{13}\). There are thirteen distinct maximal five-dimensional faces, one for each \(v\). The claim concerns this ordinary abstract simplicial complex, not its closed-neighborhood variant, clique complex, independence complex or equivariant box complex. No assertion is made for other Paley orders or arbitrary six-regular circulants.

## Proof
**Finite face description.** Enumerate all nonempty subsets of the thirteen translated sets \(v+Q\), taking their union and removing duplicates. Its face vector, in dimensions zero through five, is
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(13,78,221,195,78,13),
\]
with exactly \(598\) nonempty faces. This is an exhaustive finite enumeration, not a sample: every face is by definition contained in one of these thirteen six-element maximal faces.

**Explicit acyclic Morse matching.** Encode each nonempty face \(\sigma\) by the bitmask \(m(\sigma)=\sum_{v\in\sigma}2^v\). Process the thirteen vertex labels in the fixed order
\[
(4,2,6,5,10,12,3,11,0,7,8,1,9).
\]
At the stage for a label \(v\), pair each still-unmatched face not containing \(v\) with the still-unmatched face obtained by adjoining \(v\), whenever both belong to the remaining set. Remove both faces before advancing to the next label. The complete deterministic implementation is `verify_paley13.py`. It constructs exactly \(286\) disjoint pairs, leaving exactly one critical vertex (label \(4\)) and \(25\) critical two-dimensional faces, with no other critical faces.

**Acyclicity of the matching.** The code also explicitly generates every covering incidence between nonempty faces of consecutive dimensions. For a paired incidence it orients the lower-to-upper arrow, while for every unpaired incidence it orients the arrow upper-to-lower. There are exactly \(2067\) such incidences. Kahn's full topological-sort algorithm visits all \(598\) faces; if any directed cycle existed, this would be impossible. The exhaustive directed-graph verification proves that the pairing is a discrete gradient vector field, not merely a favorable count of unmatched faces.

**Homotopy conclusion.** Forman's discrete Morse theorem gives a CW complex homotopy equivalent to \(\mathcal N(P_{13})\), with exactly one zero-cell and twenty-five two-cells and no one-cells or other cells. Every two-cell attaches to the single-point one-skeleton by the constant map. Therefore the CW complex is a wedge of twenty-five two-spheres, with integral homotopy equivalence and no undetected attaching maps.

**Chromatic comparison.** The six vertices nonadjacent to zero are \(\{2,5,6,7,8,11\}\); their induced graph is a triangular prism with the two vertex-disjoint triangles \(\{2,5,6\}\) and \(\{7,8,11\}\). If an independent set of \(P_{13}\) contained four vertices, translation would put zero into it, and the other three would lie in this six-vertex graph. At most one can be selected from each of its two triangles, a contradiction. Conversely \(\{0,2,7\}\) is independent, so the independence number is three. Consequently \(\chi(P_{13})\ge\lceil13/3\rceil=5\). The assignments of colors to successive vertices \(0,\ldots,12\)
\[
(0,1,2,1,2,0,3,0,1,4,2,4,3)
\]
are a proper five-coloring, proving equality. Since a wedge of two-spheres is one-connected but not two-connected, the connectivity formulation of Lovász's theorem gives the lower bound four, not five.

## Verification
Run both embedded Python programs from the same directory using an ordinary Python 3 interpreter:

```bash
python3 verify_paley13.py
python3 crosscheck_paley13.py
```

Both use only the Python standard library. The primary program regenerates the nonzero squares, every simplex, the matching and all directed covering incidences, verifies their complete topological ordering, and lists the critical faces. The second program independently enumerates all \(8191\) nonempty subsets of the thirteen-element ground set and checks common-neighbor membership directly. It reconstructs all simplicial boundary matrices and computes exact row-reduction ranks over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_{101}\), obtaining boundary ranks \((12,66,130,65,13)\) and reduced Betti vector \((0,0,25,0,0,0)\) in each field. It also verifies the displayed five-coloring and absence of an independent four-set containing zero. The finite-field checks corroborate but do not replace the integral homotopy proof via the acyclic Morse matching.

## Relationship to prior work
Lovász introduced open-neighborhood complexes as topological obstructions to graph colorings. Matoušek and Ziegler compare these obstruction methods and associated box complexes, without classifying this thirteen-vertex simplicial complex. Matsushita analyzes fundamental groups of neighborhood complexes using graph-theoretic constructions but does not give the higher-dimensional homotopy type here. Shukla's explicit homotopy classification applies to graphs of maximum degree at most three and **four-regular** circulants; the present graph is a **six-regular** circulant, isomorphic to the Cayley graph of the quadratic residue connection set \(\{\pm1,\pm3,\pm4\}\). Thus no cited graph-family theorem implies this twenty-five-sphere decomposition.

## Limitations
The proof is finite and reproducible; it does not establish a formula for other Paley graphs or classify all conference graphs. The signed integral simplicial homology matrices are not independently reduced over \(\mathbb Z\); this is not needed for the homotopy conclusion because the complete acyclic matching leaves only zero- and two-cells. Calculations of homology over a finite collection of fields would not by themselves rule out integral torsion or determine homotopy type. The statement about colorings uses only the connectivity form of Lovász's bound and does not determine the possibly stronger equivariant-index bound. Priority against unindexed literature is not certified.

## References
- T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first publicly submitted 2012-10-10, particularly the definition in Section 4 and Theorem 1.1.
- S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first publicly submitted 2018-02-13, Theorems 2.1–2.6.
- J. Matoušek and G. M. Ziegler, *Topological lower bounds for the chromatic number: A hierarchy*, arXiv:math/0208072, first publicly submitted 2002-08-09, Sections 1 and 5.
- L. Lovász, *Kneser's conjecture, chromatic number, and homotopy*, Journal of Combinatorial Theory Series A 25 (1978), 319–324, DOI:10.1016/0097-3165(78)90022-5.
