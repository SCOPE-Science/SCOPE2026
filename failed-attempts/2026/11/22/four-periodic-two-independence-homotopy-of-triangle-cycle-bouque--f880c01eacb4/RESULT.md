# Four-periodic two-independence homotopy of triangle-cycle bouquets

## Finding
For each integer \(n\ge3\), let \(B_n=C_3\vee C_n\) be the simple graph made by identifying exactly one vertex of a triangle with one vertex of an \(n\)-cycle, with no other identified vertices or edges. Let \(\operatorname{Ind}_2(B_n)\) consist of those vertex subsets whose induced graph has every connected component of order at most two. Then, for every integer \(k\ge0\) in a case whose cycle length is at least three,
\[
\operatorname{Ind}_2(B_n)\simeq
\begin{cases}
\bigvee^3 S^{2k+1}, & n=4k+3,\\
\bigvee^2 S^{2k-1}, & n=4k\quad(k\ge1),\\
\{\mathrm{point}\}, & n=4k+1\quad(k\ge1),\\
S^{2k+1}, & n=4k+2\quad(k\ge1).
\end{cases}
\]
These are integral homotopy equivalences. The sphere multiplicities are exactly three, two, zero, and one in the respective residue classes. The empty wedge denotes a contractible space.

## Assumptions and scope
All graphs are finite, undirected, simple and unweighted. Label the cycle vertices \(0,1,\ldots,n-1\) modulo \(n\), and add vertices \(a,b\) with edges \(0a,0b,ab\). Besides these three triangle edges, the graph has the \(n\) cycle edges. Thus \(B_n\) has \(n+2\) vertices and \(n+3\) edges, and it is a two-cycle cactus with one shared cut vertex. Even at \(n=3\), the two triangles share only vertex \(0\).

An admissible face is exactly a vertex subset inducing graph of maximum degree at most one: if some component has three or more vertices, it contains a vertex of induced degree at least two, and conversely such a degree immediately certifies a component of order at least three. This equivalent test is used by the verifier. A matching of faces is acyclic if reversing its matched face-cover arrows in the directed face-poset Hasse diagram creates no directed cycle. We use an augmented face matching in which the empty face may be paired; this supplies the usual additional basepoint zero-cell.

## Proof
**1. Path reduction.** Write \(P_m\) for the path with \(m\) vertices and \(A_m=\operatorname{Ind}_2(P_m)\), with the convention that \(A_0=\{\emptyset\}\) has only the empty face. Match each face not containing the first endpoint of \(P_m\) to the face obtained by inserting that endpoint whenever both faces are admissible. For \(m\ge4\), the unmatched faces are precisely
\[
\{2,3\}\cup\tau,\qquad \tau\in A_{m-4},
\]
where vertices \(1,4\) are absent and \(\tau\) lies on the residual path \(5,\ldots,m\). Indeed, inserting vertex \(1\) can fail only when vertices \(2\) and \(3\) are selected; then vertex \(4\) must be absent. Every remaining selected component is independently admissible on that residual path. Repeat the same endpoint toggle on the residual path, so that every iteration deletes four path vertices and adds two compulsory face vertices.

At the base, \(A_0\) has one critical empty face; \(A_1\) and \(A_2\) have no critical face after augmented toggling, while \(A_3\) has exactly one critical edge \(\{2,3\}\). The preceding reduction handles \(m=4\) and all larger lengths. It follows by induction that the augmented matching on \(A_m\) has either no critical face or exactly one, as follows:
\[
\begin{array}{c|c}
m\pmod4&\text{critical face dimension}\\
0& m/2-1\\
1,2&\text{none}\\
3&(m-1)/2.
\end{array}
\]
For \(m=0\), the first displayed dimension equals \(-1\), the dimension of the empty face. It is used as a base convention, not as a claim about a realized negative-dimensional sphere.

**2. The triangle pivot.** Begin an augmented matching of \(\operatorname{Ind}_2(B_n)\) by toggling triangle vertex \(a\). An unmatched face must exclude \(a\), include the common vertex \(0\), and include exactly one of \(b,1,n-1\). The reason is that \(a\) can be added unless \(0\) already has one of these neighbors selected, and \(0\) cannot have two selected neighbors in an admissible face. For \(n\ge4\), this partitions the unmatched faces into three incomparable families:
\[
\begin{array}{c|c|c}
\text{compulsory edge}&\text{other forbidden cycle vertices}&\text{free path complex}\\
\{0,b\}&\{1,n-1\}&A_{n-3}\text{ on }2,\ldots,n-2\\
\{0,1\}&\{2,n-1\}&A_{n-4}\text{ on }3,\ldots,n-2\\
\{0,n-1\}&\{1,n-2\}&A_{n-4}\text{ on }2,\ldots,n-3.
\end{array}
\]
The vertex \(b\) is absent in the last two families. Every residual selected set is free to be any face in its indicated path two-independence complex, because the compulsory two-vertex connected component is isolated from it. For \(n=3\), all three families consist of their compulsory edges alone; there are no residual vertices.

**3. Acyclicity and enumeration.** In each residual path family, use the endpoint toggles from Step 1. All these matchings are contained in the single global sequence of element toggles
\[
a,0,1,2,\ldots,n-1,b.
\]
The first toggle removes all faces on which \(a\) is addable. Among the three remaining families, an endpoint toggle is first possible at vertex \(2\) (the \(\{0,b\}\) and \(\{0,n-1\}\) families) or vertex \(3\) (the \(\{0,1\}\) family). Following any unmatched endpoint toggle, the next three vertices are respectively compulsory, compulsory, forbidden, and the fourth is the next possible toggle. The global order hence implements exactly the path reductions. Sequential element toggling is an acyclic face-poset matching (the elementary patchwork/element-matching lemma); the same fact can be verified directly by the monotonicity of the first still-unmatched toggle. In particular this is an all-length construction, not an inference from finite computations.

Each critical face of a residual path family acquires two compulsory vertices, raising its dimension by two. For \(n\ge4\), the critical faces thus consist of one shifted copy of the path matching on \(A_{n-3}\) and two shifted copies of that on \(A_{n-4}\). Insert their path residue classes from Step 1. If \(n=4k+3\), all three families contribute one critical \((2k+1)\)-face; if \(n=4k\), only the last two contribute a \((2k-1)\)-face each; if \(n=4k+1\), all three have no critical faces; and if \(n=4k+2\), only the first contributes one \((2k+1)\)-face. For \(n=3\), there are directly three critical edges. This proves the claimed counts and dimensions for every permitted \(n\).

**4. From Morse cells to homotopy.** The initial augmented toggle pairs the empty face with the vertex \(\{a\}\). If one works with the nonempty face poset instead, leave \(\{a\}\) unmatched, yielding exactly one critical zero-cell plus the critical faces described above. Because every other critical cell for each fixed \(n\) has the same positive dimension, its CW model has one vertex and only \(r\) cells of a common dimension \(d\ge1\). Their attaching maps land in that vertex (for \(d=1\)) or in the vertex-only lower skeleton (for \(d\ge2\)); the model is exactly \(\bigvee^r S^d\). If \(r=0\), it is a point. This establishes the *integral homotopy*, not merely Betti numbers or Euler characteristics. \(\square\)

## Verification
Run `python3 code/verify.py` using Python 3 with the standard library. The entire stdout is recorded in `code/expected_output.txt`. The program independently enumerates all vertex subsets for each integer \(3\le n\le16\), checks the induced-degree condition, constructs the three-fiber acyclic matching, constructs the global sequential-toggle matching, verifies equality of the two matchings, tests the complete directed Hasse diagram for cycles, counts critical faces and independently checks the reduced Euler characteristic. For \(3\le n\le10\), a separate mod-two simplicial boundary rank computation also checks all reduced Betti numbers without using the Morse reduction. The last output line must be `PASS: exhaustive checks of each claimed finite instance`.

The tested range is finite corroboration. The proof for all \(n\) is the explicit length-four recursive matching above; no finite computation is used to extrapolate that induction. The verifier does not assess any external independent audit.

## Relationship to prior work
Sawant (2026) proves vertex decomposability for the higher independence complexes of **trees** and states the relationship to three-vertex-path-free complexes. The present graphs have two cycles and are not trees. Deshpande and Singh (2020, 2021 revision) determine path, cycle, fully whiskered, complete multipartite and perfect-tree examples; their path matching theory is a useful comparison but their listed family formulas do not classify a triangle glued to a cycle. Daundkar, Panja and Prasad (2023) study vertex-glued graphs for **ordinary** independence complexes, which forbid even a selected edge and are not the present two-independence complexes. Abdelmalek et al. (2021) give general results for chordal graphs and trees; \(B_n\) has an induced chordless cycle for \(n\ge4\), and the exceptional \(B_3\) exact multiplicity does not follow from a general sphere-wedge existence statement.

In particular, the vertex-gluing graph operation does not turn the two-independence complex into the join of the component complexes: when the common vertex is selected, it couples the two petals by the induced-component-size constraint. The three-fiber resolution of that coupling is the nontrivial calculation here.

## Limitations
The claim is restricted to exactly one triangle petal and one cycle petal, glued at one vertex, and to component-size threshold two. It does not cover multiple attached cycles, general cactus graphs, larger thresholds, shellability or equivariant homotopy actions. The finite verifier is not an alternative proof of the infinite statement. Independent mathematical validation has not been performed, and unindexed equivalent literature remains a priority risk.

## References
- R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1, first posted May 24, 2026. https://arxiv.org/html/2605.25150v1
- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first posted January 15, 2020. https://arxiv.org/html/2001.05448v2
- N. Daundkar, S. Panja, and S. Prasad, *Independence complexes of wedge of graphs*, arXiv:2303.08798, first posted March 15, 2023. https://arxiv.org/abs/2303.08798
- F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first posted June 21, 2021. https://arxiv.org/abs/2106.10863
