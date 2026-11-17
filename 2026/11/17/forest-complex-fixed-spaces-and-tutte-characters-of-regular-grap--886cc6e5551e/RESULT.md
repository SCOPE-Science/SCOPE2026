# Forest-complex fixed spaces and Tutte characters of regular graph covers

## Finding
Let \(p:X\to B\) be a finite connected regular graph cover, with finite deck group \(\Gamma\) acting freely on vertices **and edges**, without edge inversions. Loops and parallel edges in the quotient are allowed; all graph incidences are retained. Write \(\mathcal F(Y)\) for the simplicial complex of acyclic edge sets of a graph \(Y\), and \(T_Y\) for its graphic Tutte polynomial. For **every** subgroup \(H\leq\Gamma\), put \(Q_H=X/H\), and let \(q_H=|V(Q_H)|\). There is an explicit PL-homeomorphism
\[
 |\mathcal F(X)|^H\ \cong_{\rm PL}\ |\mathcal F(Q_H)|.
\]
For \(q_H\geq2\), this classifies the full fixed-space homotopy type as
\[
 |\mathcal F(X)|^H\simeq\bigvee^{T_{Q_H}(0,1)}S^{q_H-2},
\]
where a zero multiplicity means contractible. If \(q_H=1\), the fixed space is empty and the augmented homology of the empty complex has its single generator in degree \(-1\).

More strongly, put \(v=|V(X)|\). The sole potentially nonzero reduced rational homology of \(\mathcal F(X)\) is in degree \(v-2\); its **complete deck-group character**, for every \(g\in\Gamma\), is
\[
 \operatorname{tr}\left(g\mid \widetilde H_{v-2}(\mathcal F(X);\mathbb Q)\right)
 =(-1)^{v-q_g}T_{Q_{\langle g\rangle}}(0,1),
 \qquad q_g=v/|\langle g\rangle|.
\]
In particular the actual orbit-space quotient has reduced rational homology concentrated in degree \(v-2\), with rank
\[
 \dim_{\mathbb Q}\widetilde H_{v-2}(|\mathcal F(X)|/\Gamma;\mathbb Q)
 =\frac1{|\Gamma|}\sum_{g\in\Gamma}(-1)^{v-q_g}T_{Q_{\langle g\rangle}}(0,1).
\]
The graph-cover hypothesis is essential: free action on graph vertices alone does **not** suffice if an element reverses and stabilizes an edge.

## Assumptions and scope
The original and quotient graphs are finite, connected undirected graphs, allowing multiple edges and loops. A regular covering is understood in the ordinary topological/voltage-graph sense: \(\Gamma\) acts freely on graph vertices and edges, and the incidence-preserving quotient is locally bijective on directed edge germs. This excludes stabilised undirected edges that are reversed by an element. Every subgroup acts with the same freeness property. The forest complex has all edge subsets that contain no ordinary graph cycles (including loops and parallel-edge digons). Loops are automatically absent from independent subsets. By convention \(\{\emptyset\}\) has empty geometric realization and one reduced augmented homology generator in degree \(-1\).

## Proof
**1. Orbit forests are exactly forests downstairs.** Fix \(H\leq\Gamma\), and denote the quotient projection by \(\pi:X\to Q_H\). Because the action is free on edges, the edge fibers of \(\pi\) are exactly the \(H\)-orbits. Every \(H\)-invariant edge set has the form \(\pi^{-1}(S)\) for a unique subset \(S\subseteq E(Q_H)\).

If \(S\) is a forest, each component of \(Q_H[S]\) is a tree (isolated vertices included). The restriction of a graph cover to the preimage of a tree is a disjoint union of copies of that tree: choose a vertex over its root and use the unique tree paths to lift all vertices and edges. Thus \(\pi^{-1}(S)\) is a forest.

Conversely, if \(S\) contains a cycle (including a loop or a parallel-edge digon), choose a cyclic reduced closed walk \(W\) in \(Q_H[S]\). Lift it from a vertex above its basepoint. Its endpoint differs from the start by an element of the finite deck group \(H\). Repeating \(W\) a finite number of times closes its lift. Since \(W\) is cyclically non-backtracking, the resulting closed lift contains a graph cycle. Therefore \(\pi^{-1}(S)\) is not a forest. We have proved \(S\in\mathcal F(Q_H)\iff\pi^{-1}(S)\in\mathcal F(X)\).

**2. Actual geometric fixed points.** In any simplex of \(\mathcal F(X)\), an \(H\)-fixed barycentric point has equal weights on all edges of each \(H\)-orbit. Send the vertex \([e]\) of \(\mathcal F(Q_H)\) to the uniform barycenter of the \(H\)-orbit of any lift of \(e\), and extend affinely over faces. Step 1 makes this well-defined on precisely the forest simplices. Every geometric fixed point occurs uniquely in its image. Its inverse reads off the total weight of each edge orbit. These maps are inverse PL maps after taking the orbit-barycenter subdivision. This proves the fixed-space claim, including emptiness when \(q_H=1\).

**3. Integral fixed-space topology.** The graphic matroid of a connected \(q\)-vertex graph has rank \(q-1\). Its independence complex is shellable and, for \(q\ge2\), homotopy equivalent to \(T_Y(0,1)\) spheres of dimension \(q-2\), with loops omitted. This is the classical matroid independence-complex theorem, not a new shellability claim. Apply it to each \(Q_H\) and to \(X\). For \(q=1\) the independence complex is \(\{\emptyset\}\), handled by the augmented convention.

**4. Rational characters and quotient.** Let \(g\in\Gamma\), and write \(H=\langle g\rangle\). The reduced Lefschetz number of the simplicial automorphism \(g\) equals the reduced Euler characteristic of its geometric fixed space (use a barycentric subdivision). By steps 2–3 this is \((-1)^{q_g-2}T_{Q_H}(0,1)\), also for \(q_g=1\) by the augmented convention. The reduced rational homology upstairs is concentrated in degree \(v-2\). Hence the Lefschetz number also equals \((-1)^{v-2}\) times the required trace, giving the claimed sign \((-1)^{v-q_g}\). Finally, taking finite-group invariants over \(\mathbb Q\) computes homology of the geometric orbit quotient: barycentric subdivision makes cell stabilizers act trivially on individual cells, so the rational chain complex of the quotient is the invariant rational chain complex. Averaging the characters produces the final formula.

## Verification
The standalone `checks/verify.py` independently builds voltage-derived cyclic regular covers for nine parameter sets, with degrees two, three and four, including loops, parallel edges, and a two-sheeted cover of \(K_4\). It exhaustively compares quotient forests with lifted forest sets for every edge-orbit subset and independently evaluates every cyclic-deck-element signed simplicial-chain Lefschetz trace. It also checks a **noncyclic** Klein-four regular cover and each of its five subgroups, including the whole group. The code uses Python's standard library only and produces the exact transcript in `checks/verify_output.txt`.

For the Klein-four cover of the three-parallel-edge graph with voltages \(0,(1,0),(0,1)\), the covering graph is the eight-vertex crown graph \(K_{4,4}\setminus M\). Its top reduced homology has rank \(64\), each nonidentity deck element has trace \(4\), and the full deck-fixed space is three points (reduced zeroth Betti number \(2\)). Averaging shows the actual fourfold orbit quotient has **\(19\)** rational top-dimensional homology classes. For a two-sheeted connected cover of \(K_4\) with one nontrivial edge voltage, the ambient rank is \(36\), the deck-involution trace is \(6\), and the two eigenspaces have ranks \(21\) and \(15\).

## Relationship to prior work
Ardila–Castillo–Samper (arXiv:1410.3870, first posted October 14, 2014) supply the shellability and Tutte/homotopy input, but do not formulate the graph-cover geometric fixed-space identification. Fiala–Klavík–Kratochvíl–Nedela (arXiv:1503.06556, first posted March 23, 2015) study regular graph-cover projections, including subtleties of fixed/reversed edges and half-edge quotients; their graph-cover theory does not compute the forest-complex fixed-point spaces or homological characters. Moci–Pezzoli (arXiv:2001.03760, first posted January 2020) provide general equivariant matroid homology representation comparison theorems and special graph classes; they do not give this all-regular-cover Tutte-character formula. Related published fixed-forest identifications concern complete graphs under free vertex permutations, or particular bipartite exchanges; they do not provide the uniform covering criterion for arbitrary graphs and all deck subgroups. The new claim is the quotient-forest PL correspondence and its resulting universal group character, **not** matroid shellability, covering-space path lifting, or the general Lefschetz theorem.

## Limitations
The theorem requires a finite connected covering graph with a deck action free on edges; it does not address arbitrary vertex-free automorphisms with inverted fixed edges, non-regular covers, infinite graphs, or the complete integral deck-group module upstairs. The rational character determines the rational isomorphism class, not integral extensions. The numerical test cases do not prove the infinite family; the proof is the covering/lift argument. An equivalent unindexed formulation in covering-matroid literature cannot be excluded. Publication priority remains subject to independent examination.

## References
1. F. Ardila, F. Castillo, J. A. Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870 (2014), especially introduction and Theorem 1.3. https://arxiv.org/abs/1410.3870
2. J. Fiala, P. Klavík, J. Kratochvíl, R. Nedela, *3-connected Reduction for Regular Graph Covers*, arXiv:1503.06556 (2015), introduction and treatment of half-edges. https://arxiv.org/abs/1503.06556
3. L. Moci, G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760 (2020), especially Sections 1, 4 and 6. https://arxiv.org/abs/2001.03760
