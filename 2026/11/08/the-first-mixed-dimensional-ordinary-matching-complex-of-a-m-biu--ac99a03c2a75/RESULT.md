# The first mixed-dimensional ordinary matching complex of a Möbius ladder

## Finding
Let \(G=M_{16}\) have vertex set \(\mathbb Z/16\mathbb Z\), with all cycle edges \(\{i,i+1\}\) and eight antipodal edges \(\{i,i+8\}\) (residues modulo 16). Its **ordinary** matching complex \(\mathcal M(G)\) contains every set of pairwise vertex-disjoint edges, whether or not the matching extends to a perfect matching. There is an integral homotopy equivalence
\[
\boxed{\mathcal M(M_{16})\simeq\bigvee^{2}S^{4}\vee\bigvee^{4}S^{5}.}
\]
Its only nonzero reduced integral homology groups are \(\widetilde H_4\cong\mathbb Z^2\) and \(\widetilde H_5\cong\mathbb Z^4\). This is the first member of the Möbius-ladder family with reduced integral homology in two different dimensions: the members on four through fourteen vertices each have homology supported in exactly one degree. The assertion of first occurrence is restricted to this ordered family, beginning with the four-vertex graph.

## Assumptions and scope
Edges are indexed by the lexicographically sorted 24 unordered pairs. A simplex is encoded by the 24-bit mask of its selected edges. The empty mask is retained for reduced chains. These definitions fix the graph and the ordinary matching complex uniquely. The result is **only** for sixteen graph vertices; the initial-family comparison checks the even vertex counts four through fourteen as separate finite complexes. No assertion about a uniform all-size formula is made.

## Proof
**1. Exact finite cell decomposition.** Build the face set recursively: begin with the empty set; in edge order, adjoin an edge to precisely those previously constructed matchings with disjoint endpoints. This gives all faces by induction on the processed edges. There are 11,394 faces including the empty face; their counts by dimension minus-one through seven are
\[
(1,24,228,1096,2834,3880,2588,696,47).
\]

**2. A verified acyclic matching.** In ascending edge order, pair every currently unpaired face not containing that edge with its one-edge extension, if both faces remain unpaired. All other faces persist to the next stage. Exactly 5,673 disjoint cover pairs arise. Reverse those matched cover incidences and point every other cover incidence from larger face to smaller face. Exhaustive topological sorting of the resulting directed graph on 11,394 face masks with 55,280 incidences visits all vertices, proving the matching is acyclic. Its only critical faces have dimensions three (two faces), four (23), and five (23). The empty face is paired with a vertex; discarding the empty face and leaving that vertex unmatched supplies the ordinary CW basepoint without affecting the higher critical cells or differential matrices. Forman's discrete Morse theorem therefore gives a CW model with one 0-cell and no 1- or 2-cells, two 3-cells, 23 4-cells, and 23 5-cells.

**3. Integral Morse matrices.** For each matched lower face \(a\) with partner upper face \(b\), express \(a\) in terms of the other codimension-one faces of \(b\) using the signed simplicial boundary and its unit coefficient at \(a\). Recursively project each face to critical faces in its dimension; matched upper faces project to zero. The acyclic orientation ensures termination. Applying this projection to the signed boundary of every critical face constructs the integer Morse differentials. Their only potentially nonzero matrices are \(D_4\) of size \(2\times23\) and \(D_5\) of size \(23\times23\). Exact arithmetic gives \(D_4D_5=0\), Smith invariant factors \((1,1)\) for \(D_4\), and 19 unit invariant factors for \(D_5\). The first two columns of \(D_4\) form a unimodular \(2\times2\) matrix. The embedded certificate records all 5,673 pairs, critical masks and every entry of the two matrices; the verifier reconstructs and checks them.

**4. From integral chains to homotopy.** With only a 0-cell below dimension three, the initial 3-skeleton is \(S^3\vee S^3\). Hurewicz identifies its third homotopy group with \(\mathbb Z^2\). The unimodular two-column minor of \(D_4\) therefore allows the two 3-cells to cancel against two 4-cells after cellular basis changes. The resulting 4-skeleton is a wedge of 21 four-spheres. The image of the 5-cell boundary map is primitive of rank 19 in its 21-dimensional fourth chain group: \(D_5\) has 19 unit Smith factors, its image lies in \(\ker D_4\), and that inclusion remains primitive after the earlier cancellation. Since \(\pi_4(\bigvee^{21}S^4)\cong\mathbb Z^{21}\), cellular basis changes and 19 further cell cancellations remove 19 four/five-cell pairs. The remaining complex is a wedge of two four-spheres and four five-spheres, establishing the claimed **integral homotopy equivalence**.

**5. First mixed-dimensional occurrence.** The second verifier independently rebuilds the initial finite sequence of ordinary matching complexes on four, six, eight, ten, twelve and fourteen vertices. The nonzero reduced integral Betti profiles are respectively \(\widetilde\beta_0=2\), \(\widetilde\beta_1=4\), \(\widetilde\beta_2=6\), \(\widetilde\beta_2=2\), \(\widetilde\beta_3=10\), and \(\widetilde\beta_4=16\). The same exact acyclic matching and integer Smith procedure verifies these finite cases. Thus no earlier member has reduced homology in two degrees.

## Verification
Execute `python3 verify_m16.py` and `python3 verify_first_mixed.py` in the directory containing the two scripts and `morse_certificate.json`. Python 3 with SymPy is required. The first program enumerates the complete face poset, constructs and validates all pairs, checks acyclicity, rebuilds both integer Morse boundary matrices, verifies all invariant factors, compares to the saved certificate, and independently computes the full mod-two simplicial boundary ranks. The expected final markers are `ALL_VERIFY_OK` and `FIRST_MIXED_AT_M16_OK`. The exact outputs are recorded in `verification_output.txt`; the certificate can be recreated with `python3 generate_morse_certificate.py`.

## Relationship to prior work
Agarwal and Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph* (arXiv:2608.30601, first submitted 2026-08-31), classify vertex-independence complexes and **perfect matching** complexes of Möbius ladders. The ordinary matching complex of all partial matchings is different: their theorem gives \(\mathcal M_p(M_{16})\simeq S^3\vee S^3\), while the complex here is 3-connected and has two nonzero higher homology degrees. The distinction is not a renaming, and knowing the homotopy type of the perfect-matching subcomplex does not determine its larger ordinary matching complex. The published Wagner-graph and Möbius–Kantor-graph matching-complex calculations concern different graphs; the latter has 16 vertices but different incidence structure and wedge multiplicities. No exact prior classification for this sixteen-vertex Möbius ladder was identified in the checked literature.

## Limitations
The finite exhaustive certificate does not prove an infinite-family formula. The argument does not construct an equivariant wedge splitting or classify the inclusion of the perfect-matching subcomplex at all ladder sizes. Unindexed or inaccessible stronger results could affect the assessment of novelty. Independent mathematical validation has not been performed.

## References
- A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601, initial public version 2026-08-31; revised 2026-09-14, https://arxiv.org/abs/2608.30601.
- R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145.
- D. Kozlov, *Combinatorial Algebraic Topology*, Springer, 2008, discrete Morse theory and cellular chain complexes.
