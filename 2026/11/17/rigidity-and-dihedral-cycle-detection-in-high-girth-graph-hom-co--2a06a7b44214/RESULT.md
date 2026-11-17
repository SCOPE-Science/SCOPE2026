# Rigidity and dihedral cycle detection in high-girth graph Hom complexes

## Finding
For every even integer \(m\ge6\) and every finite connected simple graph \(H\) with at least one edge and girth \(g(H)\ge m-1\), the graph Hom complex has a complete decomposition up to (nonequivariant) homotopy:
\[
\operatorname{Hom}(C_m,H)\simeq |H\times K_2|\ \sqcup\ \bigsqcup^{2m c_m(H)}\{\mathrm{pt}\}.
\]
Every displayed point is actually an isolated vertex in the Hom complex. The remaining one or two connected components are homotopy equivalent to the respective components of the bipartite double-cover graph \(H\times K_2\). The dihedral action on connected components is explicit: the \(2m c_m(H)\) isolated vertices form \(c_m(H)\) free regular orbits under source \(D_m\); a one-step rotation exchanges the two remaining components if \(H\) is bipartite, while the source reflection fixing vertex zero preserves each. If \(H\) is nonbipartite, there is just one remaining component. In particular,
\[
\dim_{\mathbb Q}\widetilde H_0(\operatorname{Hom}(C_m,H);\mathbb Q)^{D_m}=c_m(H).
\]
This also determines the entire integral component-permutation lattice as \(\mathbb Z[D_m]^{c_m(H)}\oplus B_H\), where \(B_H\) is the rank-two rotation-swap module when \(H\) is bipartite and the rank-one trivial module otherwise.

## Assumptions and scope
The graph \(H\) is finite, simple, connected and has at least one edge. Girth is the length of a shortest simple cycle and is infinite for a forest. The domain \(C_m\) is the unlooped length-\(m\) cycle with \(m\) even and at least six. The graph Hom complex is the standard polyhedral complex with a cell for every assignment of a nonempty subset of \(V(H)\) to each source vertex, subject to complete adjacency for each source edge. Its vertices are ordinary graph homomorphisms. The product \(H\times K_2\) is the categorical graph product and hence the canonical bipartite double cover. Let \(c_m(H)\) be the number of unoriented, unbased simple cycles with \(m\) edges in \(H\). Write \(D_m\) for the order-\(2m\) dihedral group acting on source vertices by \(i\mapsto i+a\) and \(i\mapsto -i+a\).

## Proof
**1. Classification of closed walks.** A Hom vertex \(f\) is precisely an indexed closed walk \((v_0,\ldots,v_{m-1})\) of length \(m\) in \(H\). If any cyclic immediate backtracking occurs, namely \(v_{i-1}=v_{i+1}\), cancellation reduces the walk by two steps without changing the free homotopy class in the geometric graph \(|H|\). Repeated cancellation yields either a constant walk or a cyclically nonbacktracking closed walk shorter than \(m\). The latter, if nontrivial, contains a simple cycle of length at most \(m-2\), which is impossible since \(g(H)\ge m-1\). Thus any walk with a backtrack induces the trivial map on fundamental groups.

If no cyclic immediate backtrack occurs, the closed walk is simple: otherwise select a repeated pair of vertices at minimal positive cyclic separation. The enclosed subwalk gives a simple cycle of length at least \(g(H)\ge m-1\); the complementary nonempty closed segment would then have length at most one, impossible in a loopless simple graph. Hence such a walk traverses one simple \(m\)-cycle exactly once and has nontrivial fundamental-group image. There are exactly \(2m\) labeled oriented traversals per underlying simple \(m\)-cycle.

**2. Rigidity.** An adjacent Hom vertex obtained by changing only color at coordinate \(i\) must replace \(v_i\) by another common neighbor of the distinct vertices \(v_{i-1}\) and \(v_{i+1}\). Such another common neighbor would give a four-cycle. As \(g(H)\ge5\), none exists. Thus each simple-cycle traversal is an actual isolated zero-cell, not merely a homotopy class. Conversely all nontrivial-image Hom vertices are these isolated points; all other Hom vertices have trivial fundamental-group image.

**3. Remaining components.** Matsushita's Theorem 5.8 and Lemma 5.11 [1] prove, for a connected bipartite source and connected square-free target, that the null-image homomorphisms occupy exactly two components if the target is bipartite and exactly one otherwise, with each component homotopy equivalent respectively to \(|H|\) or to a connected double cover of \(|H|\). Since \(C_m\) is bipartite and \(g(H)\ge5\), these theorems apply. The canonical bipartite double cover is two copies of \(H\) if \(H\) is bipartite and a connected double cover otherwise, giving the claimed disjoint-union homotopy type. This step uses the published square-free Hom-complex theorem rather than claiming a new proof of that theorem.

**4. Source symmetry and integral detection.** Every unoriented simple \(m\)-cycle gives exactly \(2m\) oriented based traversals, a free transitive \(D_m\)-set under precomposition. This proves the regular integral component-lattice summands. For a bipartite target, the two null components are distinguished by the color class of the image of source vertex zero; a one-step source rotation swaps the classes, whereas source reflection \(i\mapsto-i\) fixes each. In the nonbipartite case there is a single null component. The rational invariant dimension of the reduced degree-zero homology is the number of component orbits minus one, namely \(c_m(H)\).

**5. Sharpness.** For every even \(m\ge8\), the target \(H=C_{m-2}\) has girth one below the stipulated bound. Its closed walk that traverses this shorter even cycle once and makes one two-step backtrack has nontrivial fundamental-group image but is not an injective \(m\)-cycle traversal. In particular, the stated exhaustive decomposition would omit its connected component. Thus the girth requirement cannot uniformly be weakened from \(m-1\) to \(m-2\).

## Verification
The standalone Python file `hom_even_girth_check.py` enumerates all length-\(m\) closed target walks, all one-coordinate Hom adjacencies, and their connected components, and tests rigidity, source-dihedral regularity, null-component parity and the cycle count in eight graph/source cases. For five cases with \(m=6\), it separately enumerates every multihomomorphism cell and checks the alternating Euler sum \(\chi=2-2\beta_1(H)+2mc_m(H)\). Its output is in `verification_output.txt`. These are finite independent checks; the proof for all permitted graphs comes from the structural closed-walk argument combined with [1].

## Relationship to prior work
Matsushita [1] gives the general square-free codomain component classification and precise null-component homotopy types; Fujii, Kimura and Nozaki [2] independently give an algorithmic classification. The present theorem specializes their structural machinery with a sharp girth hypothesis, derives a complete exact count of every additional component using simple cycles, and identifies the **integral source-dihedral component module and its cycle-detection invariant** for arbitrary high-girth targets. The cycle-to-cycle case fits the earlier classification of Čukić and Kozlov [3]. A later result on odd-cycle sources and high-girth targets concerns different (odd) source lengths and does not imply the even-source formula. Its indexed summary, not its full text, was available for comparison.

## Limitations
The result is a homotopy classification, not a canonical equivariant homotopy equivalence of spaces with \(H\times K_2\); the explicit equivariance assertion applies only to the permutation of connected components and integral degree-zero homology. The strong girth assumption excludes triangles and quadrilaterals, and the result does not classify target graphs of smaller girth or odd source cycles. Sharpness is demonstrated by even shorter cycles at lengths at least eight; no independent publication or peer audit is claimed. A complete literature uniqueness check cannot be guaranteed.

## References
[1] Takahiro Matsushita, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19144v1 (first posted 2024-12-26), Theorem 5.8 and Lemma 5.11. https://arxiv.org/html/2412.19144v1

[2] Soichiro Fujii, Kei Kimura, Yuta Nozaki, *Homotopy types of Hom complexes of graph homomorphisms whose codomains are square-free*, arXiv:2412.19039v1 (first posted 2024-12-26). https://arxiv.org/abs/2412.19039

[3] Sonja Lj. Čukić and Dmitry N. Kozlov, *The homotopy type of complexes of graph homomorphisms between cycles*, arXiv:math/0408015 (2004). https://arxiv.org/abs/math/0408015
