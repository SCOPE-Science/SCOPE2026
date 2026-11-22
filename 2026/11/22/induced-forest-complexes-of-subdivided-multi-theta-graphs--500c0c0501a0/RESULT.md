# Induced-forest complexes of subdivided multi-theta graphs

## Finding
Let \(m\ge3\), let \(\ell_1,\ldots,\ell_m\ge2\) be integers, and let \(\Theta(\ell_1,\ldots,\ell_m)\) be the simple graph consisting of \(m\) internally vertex-disjoint paths of respective edge lengths \(\ell_i\) between the same distinct poles. Put \(N=2+\sum_{i=1}^m(\ell_i-1)\). Let \(\mathcal F_\infty(G)\) be the simplicial complex on \(V(G)\) whose faces are exactly the vertex subsets inducing forests. Then, integrally,
\[
\mathcal F_\infty\bigl(\Theta(\ell_1,\ldots,\ell_m)\bigr)\simeq \bigvee^{m-1}S^{N-m}.
\]
In particular, the number of sphere summands depends only on the number of arms, whereas subdividing an arm increases the sphere dimension by one. This is a statement about homotopy types, not a canonical suspension map between complexes.

## Assumptions and scope
All graphs are finite, simple, and undirected. Every arm has at least one internal vertex, so the shortest cycle has length at least four. The poles are the only shared vertices of different arms. No extra edges are present. The integer \(m\) is at least three, the \(\ell_i\) are unrestricted positive integers at least two, and \(N-m=2+\sum_i(\ell_i-2)\ge2\). The simplicial complex contains the empty face. Homotopy equivalence is ordinary geometric-realization homotopy equivalence; all homology statements use \(\mathbb Z\).

## Proof
Write the poles as \(s,t\) and the pairwise disjoint nonempty internal vertex sets as \(A_i\), with \(|A_i|=\ell_i-1\). A simple cycle in this graph is precisely the union of two complete distinct pole-to-pole arms: leaving one pole along one arm and returning along another is forced by the degree-two property of every internal vertex. Consequently the **minimal nonfaces** of \(K=\mathcal F_\infty(G)\) are the sets
\[
C_{ij}=\{s,t\}\cup A_i\cup A_j\qquad(1\le i<j\le m).
\]
For a simplicial complex \(K\) on the full \(N\)-element vertex set, its combinatorial Alexander dual is \(K^*=\{\sigma\subseteq V:V\setminus\sigma\notin K\}\). From the displayed complete list of minimal nonfaces, the maximal simplices of \(K^*\) are exactly
\[
F_{ij}=\bigcup_{k\notin\{i,j\}}A_k\qquad(1\le i<j\le m).
\]
This dual contains neither pole. Choose a representative \(a_i\in A_i\) for every arm. In \(K^*\), each other vertex \(v\in A_i\setminus\{a_i\}\) is simplicially dominated by \(a_i\): every maximal simplex containing \(v\) contains \(a_i\). Removing dominated vertices by elementary simplicial collapses (one at a time) leaves exactly
\[
L=\{\sigma\subseteq\{a_1,\ldots,a_m\}:|\sigma|\le m-2\},
\]
the \((m-3)\)-skeleton of the \((m-1)\)-simplex. Its reduced integral homology is free of rank \(m-1\) in degree \(m-3\), and vanishes in every other degree. For example, boundaries of the \(m-1\) different \((m-2)\)-simplices on all representatives except one of \(a_1,\ldots,a_{m-1}\) supply a basis. This also follows from the augmented exact simplicial chain complex of the full simplex, so there is no torsion.

Combinatorial Alexander duality over \(\mathbb Z\) now gives
\[
\widetilde H_j(K;\mathbb Z)\cong\widetilde H^{N-j-3}(K^*;\mathbb Z)=
\begin{cases}\mathbb Z^{m-1},&j=N-m,\\0,&j\ne N-m.\end{cases}
\]
As the graph has no triangles, every vertex triple induces a forest. Hence \(K\) contains the complete two-skeleton of the \((N-1)\)-simplex and is simply connected. Because \(d=N-m\ge2\), the Hurewicz theorem gives spherical representatives for a basis of \(\widetilde H_d(K;\mathbb Z)\). The resulting map \(\bigvee^{m-1}S^d\to K\) is an isomorphism on all integral homology groups, and both spaces are simply connected CW complexes. The homological Whitehead theorem makes it a homotopy equivalence, proving the claim.

## Verification
The companion `verify.py` independently builds each graph from its edges, exhaustively checks the induced-forest definition on every vertex subset, reconstructs the Alexander dual using complementary cycle vertex sets, checks the full two-skeleton and the domination condition for repeated arm vertices, computes all reduced mod-two Betti numbers by binary boundary-matrix elimination, and verifies reduced Euler characteristic. It passes ten nontrivial choices of three, four, and five arms, including unequal subdivisions, with at most nine vertices. Run with `python3 verify.py`; expected output is in `verification_output.txt`. These finite tests do not prove arbitrary arm counts or lengths: that is the role of the preceding argument.

## Relationship to prior work
Carnero Bravo's *The Forest Filtration of a Graph* (first arXiv public version 2023-07-25, arXiv:2307.13271) defines this precise vertex-induced-forest complex, analyzes chorded cycles (Proposition 25), cactus graphs (Theorem 31), and complete bipartite graphs (Theorem 34). The complete bipartite instance \(K_{2,m}=\Theta(2,\ldots,2)\) of the present formula is therefore a **known special case**, not a novel result. A chorded cycle includes a direct pole edge and is not in the stated domain. A multi-theta graph with at least three arms is not a cactus, since its distinct cycles share both pole vertices. The variable-length, every-arm-subdivided classification is not supplied by those statements; the explicit dual-collapse argument addresses that gap.

Przytycki and Silvero, *Khovanov homology, wedges of spheres and complexity* (2024), Example 3.8, analyze ordinary graph independence complexes of theta graphs. That construction forbids adjacent vertex pairs and is mathematically distinct from the induced-forest complex, which forbids complete cycle vertex sets. Its homotopy classifications do not imply the formula here.

## Limitations
The result neither treats arms without internal vertices, nor graphs with additional chords, nor the intermediate bounded-degree complexes \(\mathcal F_d(G)\) for finite \(d\), nor natural maps between complexes of differently subdivided graphs. General indexed searches and available mathematical records revealed no statement that covers the full variable-length claim, but this does not exclude unpublished, unindexed, or differently named equivalent work. The homotopy equivalence is not asserted equivariant under arm permutations; the proof determines only the ordinary integral homotopy type.

## References
1. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first posted 2023-07-25, https://arxiv.org/abs/2307.13271 . Sections 2, 3 and 4, especially Proposition 25 and Theorems 31 and 34.
2. J. H. Przytycki and M. Silvero, *Khovanov homology, wedges of spheres and complexity*, Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas 118 (2024), article 102; https://doi.org/10.1007/s13398-024-01594-z , Example 3.8.
3. A. Hatcher, *Algebraic Topology*, Cambridge University Press (2002): Hurewicz and Whitehead theorems and Alexander duality background.
