# The Petersen higher-independence inclusion from cutoff two to three is a homotopy equivalence

## Finding
Let \(P\) be the Petersen graph, and define \(\operatorname{Ind}_r(P)\) to contain exactly those vertex subsets whose induced connected components each have at most \(r\) vertices. The natural simplicial inclusion
\[
\iota:\operatorname{Ind}_2(P)\hookrightarrow\operatorname{Ind}_3(P)
\]
is an **integral homotopy equivalence**, although the larger complex has 120 more nonempty simplices. In particular both complexes have the homotopy type \(S^3\), and \(\iota_*:\widetilde H_3(-;\mathbb Z)\to\widetilde H_3(-;\mathbb Z)\) is multiplication by \(+1\) for the explicit oriented generators below. The previously documented cutoff-two sphere is not presented as a new finding: the new result is the cutoff-three classification **and** the natural inclusion's integral degree.

## Assumptions and scope
Use the ten vertices \(v_0,\ldots,v_9\), listed lexicographically as two-element subsets of \(\{0,1,2,3,4\}\):
\[
(01),(02),(03),(04),(12),(13),(14),(23),(24),(34).
\]
Vertices are adjacent when the two subsets are disjoint. A face is encoded by the bit mask \(m=\sum_{i\in F}2^i\). Orient each simplex by increasing vertex index. Thus the signed simplicial boundary on the mask \(m\) is the sum obtained by removing its set bits in increasing order with alternating signs. The empty face participates in the augmented/reduced Morse chain complex. All chain groups, boundaries, and degrees below are over \(\mathbb Z\).

## Proof
**1. Exact complexes and acyclic matchings.** Reconstruct every mask between 0 and 1023 and test connected-component sizes of its induced Petersen subgraph. The cutoff-two face numbers by dimension \(-1,0,1,2,3,4,5\) are \((1,10,45,90,80,30,5)\); cutoff three has \((1,10,45,120,140,60,5)\). Thus the augmented face counts are 261 and 381. In each complex, iterate vertex indices 0 through 9 and match every still-unmatched face omitting the current vertex with its one-vertex extension if both remain unmatched. The attached standalone verifier constructs the **entire** Hasse digraph, reversing the matched incidences, and topologically sorts it. Both directed Hasse graphs are acyclic (870 and 1350 directed incidences, respectively). The cutoff-two matching has 130 pairs and one critical three-simplex (mask 912). The cutoff-three matching has 187 pairs, with critical simplex 530 in dimension two; 660, 712, 792, 808 in dimension three; and 944, 976 in dimension four. There are no other critical cells (the empty face is matched).

The elementary algebraic cancellation underlying discrete Morse theory expresses every matched lower simplex as an integral combination of the remaining critical simplices. For a matched pair \((a,b)\), with \(a\) a codimension-one face of \(b\) and incidence sign \(s=\pm1\), the projection satisfies
\[
\pi(a)=-s\sum_{c\in\partial b\setminus\{a\}}[b:c]\,\pi(c).
\]
An upper paired face projects to zero, while critical faces project to themselves. Acyclicity makes the recursion terminate. This rule computes integral Morse boundaries, not only mod-two ranks.

**2. Exact Morse boundary and the cutoff-three homotopy type.** The nonzero cutoff-three differentials, using the critical-cell order just stated, are
\[
\partial_3=\begin{pmatrix}-1&0&-1&0\end{pmatrix},\qquad
\partial_4=\begin{pmatrix}1&1\\0&1\\-1&-1\\1&0\end{pmatrix}.
\]
Direct multiplication gives \(\partial_3\partial_4=0\). The incidence \(-1\) from the 660-cell to the 530-cell is primitive: cancel this pair, leaving a wedge of three 3-cells (before the 4-cell attachments). Write \(x=[792]-[660]\), \(u=[712]\), and \(v=[808]\) for a basis of the remaining dimension-three cycle lattice. The two four-cell attaching degrees become \(-x+v\) and \(-x+u\). These are primitive and independent, and elementary integral basis changes cancel two further 3/4 pairs. Since all remaining cells after the first cancellation are in dimensions three and four, their attaching maps are completely classified by their integer degrees in \(\pi_3(\bigvee^3S^3)\cong\mathbb Z^3\). The resulting homotopy type is one three-sphere:
\[
\operatorname{Ind}_3(P)\simeq S^3.
\]
Likewise the cutoff-two acyclic matching, with exactly one reduced critical three-cell, yields \(\operatorname{Ind}_2(P)\simeq S^3\).

**3. The inclusion has integral degree one.** It is not enough to know both homotopy types. The explicit integral three-chain \(z\) is specified by the following paired lists of simplex masks and coefficients (all other coefficients zero):

```
SUPPORT = [15,113,135,147,165,177,267,275,329,337,402,525,526,
           549,585,609,624,646,676,688,778,840,848,898,912]
COEFF = [1,-1,-1,1,-1,1,1,-1,1,-1,1,-1,1,
         1,-1,1,-1,-1,-1,1,1,1,-1,-1,1]
```

Every listed mask is a face of the cutoff-two complex and has four set bits. Computing the signed **integral** boundary gives \(\partial z=0\). Exact projection along the two different acyclic matchings gives
\[
\pi_2(z)=[912],\qquad \pi_3(z)=-[660]+[792]=x.
\]
The first is the primitive cutoff-two generator; the second is the primitive cutoff-three generator after both four-cell relations. Thus \(\iota_*\) acts by degree \(+1\) on integral third homology. A map between spaces homotopy equivalent to \(S^3\) inducing an isomorphism on \(H_3(-;\mathbb Z)\) is a homotopy equivalence. This proves the claim.

## Verification
Run `python3 verify_petersen_independence.py` (Python 3, standard library only). It reconstructs the two complexes without any input file; verifies their enumerated f-vectors, matchings, every oriented Hasse incidence and complete acyclicity by topological sorting; recursively derives the signed integral Morse matrices; checks the explicit 25-simplex cycle, both integral projections, and the resulting degree-one map. Its successful exact execution yields `PETERSEN_IND2_TO_IND3_INTEGRAL_HOMOTOPY_EQUIVALENCE_OK`. The accompanying `verification_output.txt` is the output from this actual checker. No numerical approximation or unbounded-search inference is used: both complexes lie on exactly ten vertices and all their faces and Hasse incidences are checked.

## Relationship to prior work
Deshpande and Singh introduced higher independence complexes and studied specific graph families (arXiv:2001.05448, first public 2020-01-15). Deshpande, Shukla and Singh studied domination and connectivity bounds (arXiv:2001.06775), while Abdelmalek and coauthors studied chordal-graph families (arXiv:2106.10863). Neither classifies the cutoff-three Petersen complex or the map of consecutive cutoff stages. The previously published exact Petersen cutoff-two calculation, *The 2-independence complex of the Petersen graph is a 3-sphere* (public indexed research record), establishes only the starting sphere; two separate sphere homotopy types cannot imply that their **particular natural inclusion** is a homotopy equivalence. The new integral chain directly measures the map.

## Limitations
This is an exact finite-graph homotopy calculation and a two-stage inclusion theorem. It does not classify cutoffs four and above, higher independence complexes of other cubic graphs, or persistence for arbitrary graphs. The matching and integral chain calculations are fully reproducible; no independent audit was performed. Literature novelty is a best-knowledge assessment, not a theorem: equivalent results outside the inspected sources may exist.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (v1 public 2020-01-15), https://arxiv.org/abs/2001.05448.
2. P. Deshpande, S. Shukla, and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775 (2020), https://arxiv.org/abs/2001.06775.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (2021), https://arxiv.org/abs/2106.10863.
4. *The 2-independence complex of the Petersen graph is a 3-sphere*, public indexed result, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-the-2-independence-complex-of-the-petersen-graph-is-a-3-sphere--156dc9567f6a/RESULT.md.
