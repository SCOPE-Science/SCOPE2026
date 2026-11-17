# A free cyclic homotopy five-sphere from the five-vertex tournament non-strong-connectivity complex

## Finding
Let \(T\) be the regular five-vertex tournament with vertex set \(\mathbb Z/5\mathbb Z\) and directed arcs \(i\to i+1\) and \(i\to i+2\). Let \(K\) be the simplicial complex on its ten arcs, whose faces are exactly the arc subsets that do not span a strongly connected digraph on all five vertices. Then
\[
 |K|\simeq S^5,\qquad \text{the natural }C_5\text{-action on }|K|\text{ is free}.
\]
Its geometric quotient \(Q=|K|/C_5\) consequently satisfies
\[
 \pi_1(Q)\cong H_1(Q;\mathbb Z)\cong\mathbb Z/5\mathbb Z,
 \qquad H_j(Q;\mathbb Q)\cong H_j(S^5;\mathbb Q)\quad(j\ge0).
\]
The computation supplies a natural regular tournament, rather than a symmetric digraph containing two-cycles, whose non-strong-connectivity complex is an integral homotopy sphere with a free symmetry and torsion in the quotient.

## Assumptions and scope
Everything here concerns precisely the ten-arc regular tournament on five vertices. The graph is a *spanning* digraph: every subset of arcs retains all five vertices. A spanning digraph is strongly connected when each vertex is reachable from every vertex by a directed path, allowing length zero at the starting vertex. Faces include the empty arc set; its geometric realization contributes no point. The action rotates vertex labels modulo five and hence permutes the ten arc vertices. No statement is made about larger tournaments.

## Proof
Index the ten arcs in the order \((i,i+1),(i,i+2)\) for \(i=0,1,2,3,4\), and encode a subset by its ten-bit integer \(f\). A finite enumeration of all \(2^{10}=1024\) subsets, checking directed reachability from each of the five vertices, gives precisely \(901\) faces including the empty face. The face numbers by dimensions \(-1,0,1,\ldots,7\) are \((1,10,45,120,210,250,185,70,10)\).

For a reproducible explicit acyclic discrete Morse matching, start with all \(901\) faces, including the empty face, and process the ten arc indices in the fixed order
\[
 (8,2,5,9,7,1,6,0,4,3).
\]
At each index, pair every still-unpaired face \(f\) not containing that arc with \(f\cup\{i\}\), whenever both remain, and delete both from the unpaired set. There are \(450\) pairs and one remaining face, integer bitmask \(189\), of size six (dimension five). The empty face is paired with the vertex of index eight. Remove just that empty-face pair, leaving the index-eight vertex critical. The resulting ordinary matching on the \(900\) nonempty faces has exactly two critical simplices, of dimensions zero and five.

The finite checker constructs *every* codimension-one face incidence among these \(900\) nonempty faces. It orients each incidence upward when matched and downward otherwise, and applies an exact topological sorting procedure. All \(900\) faces are removed by topological sorting. Thus the directed Hasse graph has no cycle, certifying acyclicity of the entire matching rather than relying on a homology rank or a heuristic. Forman's discrete Morse theorem therefore gives a CW model with precisely one zero-cell and one five-cell; its attaching map is necessarily constant, proving \(|K|\simeq S^5\).

For any nonidentity rotation, the ten arcs partition into two orbits of five arcs each, one orbit of differences one and one of differences two. Either complete orbit is a directed Hamiltonian five-cycle, hence strongly connected. A simplex stabilized by a nonidentity rotation would therefore have to contain one complete arc orbit, impossible for a face of \(K\). Every point fixed by a simplicial permutation must have support a union of complete vertex orbits. Hence the action is free on \(|K|\), not merely free on its arc vertices.

The quotient map is consequently a regular covering with deck group \(C_5\). Since \(|K|\simeq S^5\) is simply connected, it is the universal covering; thus \(\pi_1(Q)\cong C_5\), and its abelianization is \(H_1(Q;\mathbb Z)\cong C_5\). Over \(\mathbb Q\), homology of a finite group quotient of a free action identifies with invariant homology. The one-dimensional top rational homology representation of an order-five group must be trivial (its rational scalar has fifth power one), giving one degree-five class. All other positive rational homology vanishes.

## Verification
Run `python3 verify.py` with standard Python. The script independently enumerates arc subsets via five-root breadth-first reachability, constructs every matching pair, checks a complete oriented Hasse graph for absence of directed cycles, computes all reduced mod-two Betti numbers, and checks every nonidentity rotation's two five-arc orbits. Its exact terminal output is in `verification_output.txt`. The homotopy equivalence uses the acyclic matching, not extrapolation from the mod-two calculation. The rational quotient calculation uses finite-group transfer; it does not depend on an unproved integral Smith normal form of the quotient.

## Relationship to prior work
Hultman's *Directed Subgraph Complexes* (2004) studies non-strong-connectivity complexes and proves uniform sphere-wedge conclusions under a 2-dense hypothesis. The regular five-tournament has no directed two-cycles and therefore does not meet that hypothesis. Björner and Welker's *Complexes of Directed Graphs* studies the earlier directed graph complex setting; its available abstract and bibliographic record alone do not determine whether equivalent specialized cases appear in the inaccessible full text. The finding here is limited to the concrete five-tournament homotopy and its free rotational quotient; no earlier general theorem is presented as new.

## Limitations
No classification of all strongly connected tournaments, higher-order regular tournaments, the full integral quotient homology, or the quotient's homeomorphism type is claimed. The acyclic Morse certificate is finite and reproducible; its independence from the proof is limited to the directly checked combinatorial conditions. Equivalent results in insufficiently accessible literature remain an originality risk, and independent mathematical audit has not been performed.

## References
- Axel Hultman, *Directed Subgraph Complexes*, Electronic Journal of Combinatorics **11** (2004), R75. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r75/pdf/
- Anders Björner and Volkmar Welker, *Complexes of Directed Graphs*, SIAM Journal on Discrete Mathematics **12** (1999), 413–424. https://doi.org/10.1137/S0895480198338724
- Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
