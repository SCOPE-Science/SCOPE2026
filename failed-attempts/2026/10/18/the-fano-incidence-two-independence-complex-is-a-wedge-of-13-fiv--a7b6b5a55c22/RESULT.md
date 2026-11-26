# The Fano-incidence two-independence complex is a wedge of \(13\) five-spheres

## Finding
Let \(H\) be the Heawood graph, the incidence graph of the Fano projective plane. Let \(\operatorname{Ind}_2(H)\) be its two-independence complex: a nonempty vertex set is a simplex exactly when every connected component of its induced graph has at most two vertices. Then
\[
\operatorname{Ind}_2(H)\simeq\bigvee^{13}S^5.
\]
This is an **integral homotopy classification**, not merely a determination of field-dependent Betti numbers.

## Assumptions and scope
Label the seven points by \(p\in\mathbb Z/7\) and the seven lines by \(\ell\in\mathbb Z/7\). Incidence is \(p\in\{\ell,\ell+1,\ell+3\}\pmod 7\). The associated bipartite graph has fourteen vertices and twenty-one edges. Number its vertices by integers from \(0\) through \(13\), using point labels first and adding seven to each line label. A simplex is encoded by a positive fourteen-bit integer, with bit \(v\) set when vertex \(v\) belongs to it. The induced graph has all components of order at most two **if and only if** every selected vertex has at most one selected neighbor. There is no restriction on the number of different disjoint two-vertex components.

## Proof
**Complete face set.** Enumerate every integer mask from \(1\) through \(2^{14}-1\). Keep a mask precisely if every selected vertex has at most one neighbor inside it, as tested against the explicit twenty-one graph edges. The resulting entire face set has face vector, in dimensions zero through six,
\[
(14,91,322,651,728,392,58),
\]
with exactly \(2256\) nonempty simplices. Every nonempty subset of each retained face satisfies the same local degree bound, confirming that this is a simplicial complex.

**Explicit discrete-Morse pairing.** In the following precise order of vertex bits,
\[
(11,2,10,9,7,1,12,13,8,0,4,3,6,5),
\]
start with all simplices unmatched. For each bit \(v\), inspect in increasing integer order all currently unmatched masks \(L\) not containing that bit; if the mask \(U=L\cup\{v\}\) is also currently unmatched, match \(L\) with \(U\) and immediately remove both from the unmatched set. Pairing occurs only between two nonempty faces. This deterministic procedure produces exactly \(1121\) matched pairs. The only unmatched face in dimension zero is the mask \(2048\). The thirteen unmatched dimension-five masks are
\[
(363,377,627,4697,5057,8314,8664,9058,12345,12593,12712,13065,13842).
\]
No critical faces have any other dimension.

**Acyclicity is exhaustive, not inferred.** Construct the entire directed Hasse diagram of the nonempty-face poset: orient an incident cover from an upper face down to a lower face, reversing exactly those edges belonging to matched pairs. The graph has \(2256\) nodes and \(10150\) directed cover relations. Its topological-sort procedure visits all \(2256\) nodes. Hence it is a directed acyclic graph, and the matching is an acyclic discrete-Morse matching by definition. The standalone verifier reconstructs the graph, faces, pairs and all directed cover relations independently from these instructions.

**Deduction of integral homotopy type.** Forman's discrete-Morse theorem gives a CW complex homotopy equivalent to \(\operatorname{Ind}_2(H)\), with exactly one zero-cell and thirteen five-cells and no other cells. Every attaching map for a five-cell has target the zero-skeleton, a single point, and therefore is null. The resulting CW space is homeomorphic to a wedge of thirteen five-spheres. This gives the claimed homotopy equivalence with integral coefficients and no torsion assumption.

## Verification
Run the standalone standard-library script `python3 verify_heawood.py`. It reconstructs all \(2^{14}-1=16383\) nonempty candidate subsets, confirms the face vector and the closure property, recomputes \(1121\) pairs, checks \(10150\) cover relations and the complete acyclic topological order, and independently computes the mod-two simplicial boundary ranks \((13,78,244,407,321,58)\). The resulting reduced mod-two Betti vector by degrees zero through six is \((0,0,0,0,0,13,0)\), consistent with the integral homotopy proof. The packaged `verification_output.txt` records an actual successful run ending in `VERIFY_OK`. The exhaustive directed acyclicity check, rather than the finite homology calculation by itself, is the critical proof certificate.

## Relationship to prior work
Sawant's 2026 theorem on vertex decomposability of higher independence complexes treats **trees**, not the cubic girth-six Heawood incidence graph. Ghosh and Selvaraja's work on shellability of higher independence complexes treats specialized graph classes such as block graphs; Abdelmalek and collaborators' work treats chordal graphs, a class excluding Heawood. Established calculations of the **ordinary** Heawood independence complex concern subsets inducing no edges, whereas the present complex additionally permits vertex-disjoint graph edges. Published ordinary or perfect matching complexes instead use graph edges as simplicial vertices, so neither their statements nor their homotopy classifications imply this result. No equivalent published computation was identified in targeted searches, though unindexed literature may exist.

## Limitations
The theorem concerns precisely the fourteen-vertex Fano-plane incidence graph and its two-independence complex; it does not classify higher-order projective-plane incidence graphs, other higher-independence parameters, or the action of the full graph automorphism group. The combinatorial certificate is finite and exhaustive for this graph, not a computational proof for an infinite family. The novelty comparison is limited to accessible indexed literature. Independent external validation has not been performed.

## References
1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150 (first public version 2026-05-24).
2. A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614.
3. A. Abdelmalek et al., *Chordal Graphs, Higher Independence and Vertex Decomposable Complexes*, arXiv:2106.10863.
4. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145.
