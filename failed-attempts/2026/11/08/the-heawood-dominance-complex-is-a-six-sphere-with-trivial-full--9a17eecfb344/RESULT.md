# The Heawood dominance complex is a six-sphere with trivial full symmetry action

## Finding
Let \(H\) be the Heawood graph, the point–line incidence graph of the Fano plane, and let \(\mathcal D(H)\) denote its dominance complex: a vertex subset \(F\) is a simplex when \(V(H)\setminus F\) is a dominating set. Then
\[
\mathcal D(H)\simeq S^6,\qquad
\widetilde H_i(\mathcal D(H);\mathbb Z)=
\begin{cases}\mathbb Z&i=6,\\0&i\ne6.\end{cases}
\]
The natural action of the full graph automorphism group \(\operatorname{Aut}(H)\), of order \(336\), on \(\widetilde H_6(\mathcal D(H);\mathbb Z)\) is trivial.

More precisely, every perfect matching of \(H\) defines a cross-polytopal subcomplex homeomorphic to \(S^6\) by choosing at most one endpoint of each matching edge. Its fundamental cycle represents a **primitive generator** of the integral sixth homology. In particular, for the matching between the corresponding point and line labels, this embedded sphere induces an isomorphism on integral sixth homology.

The complex has \(8,850\) nonempty simplices, reaches dimension \(9\), and is not pure. Its \(65\) inclusion-maximal faces have dimensions \(6,7,8,9\), in multiplicities \(2,28,14,21\). Thus the six-sphere homotopy type is not visible from the maximal simplex dimension.

## Assumptions and scope
All constructions are finite and integral. Label the point vertices \(P_i=i\) and the line vertices \(L_j=7+j\), for \(i,j\in\{0,\ldots,6\}\), with an edge \(\{P_i,L_j\}\) exactly when
\[
(j-i)\bmod 7\in\{0,1,3\}.
\]
This is a point–line labeling of the unique order-two projective plane. Write \(N[v]\) for the closed neighborhood of a graph vertex. The face condition is, equivalently,
\[
F\in\mathcal D(H)\iff N[v]\not\subseteq F\quad\text{for all }v\in V(H).
\]
A face of dimension \(k\) has \(k+1\) vertices. A simplicial chain is oriented using ascending vertex labels. No graph loops, repeated edges, coefficient-field restrictions, or asymptotic assumptions are imposed.

## Proof
**Finite homotopy certificate.** Enumerate the \(2^{14}\) subsets of \(V(H)\) using the closed-neighborhood criterion; independently enumerate them by directly checking whether the complementary set dominates. Both procedures yield exactly the same \(8,851\) faces including the empty face, with cardinality vector
\[
(1,14,91,364,987,1862,2394,1962,931,224,21),
\]
where the initial entry counts the empty face and entry \(k+1\) counts \(k\)-simplices. The complete executable verifier implementing both tests accompanies this result.

Construct a matching on the augmented face poset as follows. Start with every face unmatched. For \(i=0,1,\ldots,13\) in turn, pair each currently unmatched face \(F\) not containing \(i\) with \(F\cup\{i\}\) whenever both are still unmatched. Each pair is removed before the next stage. Finally discard the pair between the empty face and \(\{P_0\}\), and work in the ordinary nonempty face poset. This gives exactly \(4,424\) pairs and the two critical cells \(\{P_0\}\) (dimension zero) and \(\{L_0,\ldots,L_6\}\) (dimension six).

For the necessary nonstandard check, construct **every** Hasse incidence between nonempty faces. Direct all unmatched cover relations from higher to lower dimension and reverse the matched cover relations. An exhaustive topological sort visits all \(8,850\) face-poset vertices over all \(52,304\) Hasse incidences. Thus there is no directed cycle, proving this is an acyclic discrete-Morse matching. A separate reverse-vertex-order construction leaves one critical vertex and one critical six-cell and passes the same complete acyclicity test. Forman's discrete Morse theorem identifies \(\mathcal D(H)\) with a CW complex having only one zero-cell and one six-cell. The attaching map of the six-cell goes to a point, proving \(\mathcal D(H)\simeq S^6\) integrally and as a homotopy equivalence, not just a field-homology calculation.

**Explicit primitive geometric generator.** The seven edges \(\{P_i,L_i\}\) form a perfect matching. The join of the seven zero-spheres \(\{P_i,L_i\}\), where each factor has its two isolated vertices, is the boundary of the seven-dimensional cross polytope. Every face chooses at most one endpoint from each matching edge, so it cannot contain the closed neighborhood of any vertex: each \(N[v]\) contains the matched pair through \(v\). Hence the cross-polytopal sphere is contained in \(\mathcal D(H)\). Its oriented fundamental chain is the join product of the seven differences \([P_i]-[L_i]\). Direct signed boundary cancellation verifies that it is a six-cycle \(Z\) supported on \(128\) facets.

The whole-point face \(P=\{P_0,\ldots,P_6\}\) belongs to \(\mathcal D(H)\), but has no seven-dimensional coface: adding any one line vertex leaves that line itself outside the complementary dominating set, with none of its point-neighbors in the complement. Therefore the coefficient-of-\(P\) cochain is a cocycle. It evaluates to \(+1\) on \(Z\). Since \(H_6(\mathcal D(H);\mathbb Z)\cong\mathbb Z\), this forces \([Z]\) to be primitive and hence a generator. The same proof works for any perfect matching, using the all-point part face as the evaluation cocycle: its coefficient in the corresponding oriented cross-polytopal cycle is always \(\pm1\).

**Full integral symmetry character.** The graph is connected bipartite, with parts consisting of all points and all lines. Each bipartition-preserving graph automorphism induces an automorphism of the seven-point Fano plane. Exhaustive enumeration of all \(7!\) point permutations preserving the seven three-point line sets yields exactly \(168\) such automorphisms, all **even** point permutations. Therefore they act as \(+1\) on the generator: they fix the all-point face and preserve its orientation, so its primitive-coefficient cocycle evaluates to \(+1\) on the image of \(Z\).

The incidence-preserving duality \(s(P_i)=L_{-i}\), \(s(L_j)=P_{-j}\), with subscripts modulo seven, exchanges the two parts. Its orientation action on the ordered all-line face is the sign of \(i\mapsto-i\), which is \(-1\) (three transpositions). The coefficient of the all-line facet in \(Z\) is also \(-1\), so the image \(s_*Z\) has coefficient \(+1\) on the all-point facet. Consequently \(s_*[Z]=[Z]\). Every part-swapping graph automorphism is the composition of \(s\) with a part-preserving automorphism. Thus all \(336\) automorphisms act trivially on \(H_6\).

**Sharpness of the domination–vertex-cover bound.** The seven matching edges force every vertex cover of \(H\) to have size at least seven, while the seven point vertices form a vertex cover. Thus \(\tau(H)=7\). The exact six-sphere classification gives mod-two homological connectivity five, so the inequality \(\operatorname{conn}_{\mathbb F_2}(\mathcal D(H))+2\le\tau(H)\) holds with equality \(5+2=7\).

## Verification
Run `python3 heawood_dominance_verify.py` using a standard Python 3 interpreter. The verifier has no third-party dependencies. It independently implements the two face conditions, checks the face and maximal-face vectors, constructs two full acyclic matchings and checks every Hasse incidence by directed topological sort, verifies the signed cycle and isolated coface obstruction, counts the \(168\) bipartition-preserving automorphisms, and checks the duality sign. The exact output from one execution is embedded as `verification_output.txt`.

The finite check exhausts the entire labeled simplicial complex, not a sample. The topological deduction invokes the standard discrete-Morse equivalence after the complete acyclicity checks. The proof does not require inferring integral homology from modular ranks.

## Relationship to prior work
Matsushita (arXiv:2009.04145, first publicly posted 2020-09-09) introduced the vertex-cover lower-bound formulation for the connectivity of dominance complexes and recalled known sphere computations for forests, chordal graphs and cycles. Its Theorem 1 supplies an inequality rather than a Heawood homotopy or symmetry classification.

Matsushita and Wakatsuki (arXiv:2312.02639, first publicly posted 2023-12-05) establish the Alexander-dual identity between dominance and neighborhood complexes, and classify examples based on cycles and products of paths. Those results do not include this nonchordal Fano-plane incidence graph, do not determine its integral homotopy type and do not imply the full action on its homology.

The graph's perfect matching and Fano incidence symmetry are standard. Their existence alone does not force the stated homotopy type for arbitrary regular bipartite graphs: the exact acyclic matching is the additional required calculation. The dimension, primitive generator, and symmetry statement here are compared at the level of mathematical implications, not only titles or keywords.

## Limitations
This is an exact classification for the Heawood graph only. It does not assert a general formula for projective-plane incidence graphs of larger order, a homeomorphism of the entire nonpure complex with a sphere, or an equivariant homotopy equivalence. The finite code is an explicit, replayable certificate but has not received independent external audit. Absence of equivalent work from the consulted records cannot logically establish exhaustive global novelty; work available only through abstracts or inaccessible manuscripts remains a residual risk.

## References
1. T. Matsushita, *Dominance complexes and vertex cover numbers of graphs*, arXiv:2009.04145, originally submitted 2020-09-09. https://arxiv.org/abs/2009.04145
2. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, originally submitted 2023-12-05. https://arxiv.org/abs/2312.02639
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. (Standard discrete-Morse theorem.)
