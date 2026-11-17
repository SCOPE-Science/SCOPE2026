# Bidirected vertex whiskering collapses every multipath complex to a cross-polytope sphere

## Finding

Let \(D\) be **any** finite loopless directed graph on \(n\geq1\) vertices; antiparallel core arcs are permitted. Add one new leaf \(w_v\) at every core vertex \(v\), together with both arrows \(v\to w_v\) and \(w_v\to v\), and leave all original core arrows intact. Denote the resulting bidirectionally whiskered digraph by \(W^{\pm}(D)\). For the multipath simplicial complex \(X\), there is an explicit sequence of elementary simplicial collapses

\[
X(W^{\pm}(D))\ \searrow\ \mathop{\ast}_{v\in V(D)}\{v\to w_v,\ w_v\to v\}\ \cong\ \partial\Diamond^n\ \cong\ S^{n-1}.
\]

The symbol \(\{v\to w_v,w_v\to v\}\) denotes the **discrete two-vertex complex** rather than an edge. Thus for every core digraph, irrespective of its orientation, cycles, branching, or number of arcs, the whiskered multipath complex is a single integral sphere. Its only nonzero reduced integral homology is

\[
\widetilde H_{n-1}(X(W^{\pm}(D));\mathbb Z)\cong\mathbb Z.
\]

Every automorphism of \(D\) permutes the whisker pairs. On the displayed homology generator, its induced action is the sign of its permutation of the \(n\) core vertices. This assertion concerns the induced homology action and does not require an equivariant collapse.

## Assumptions and scope

A directed graph here is finite, has distinct vertices, has no loops, and has at most one arrow for each **ordered** pair of distinct vertices. Both opposite arrows may be present. There may be no core arrows at all; the statement includes this case. Each new leaf \(w_v\) is distinct from every core vertex and every other leaf. There are no arrows between leaves or additional arrows joining a leaf to the core.

The vertices of \(X(G)\) are the arrows of \(G\), and a finite arrow set is a face exactly when its induced directed subgraph is a disjoint union of vertex-simple directed paths, including isolated vertices. Equivalently, all indegrees and outdegrees are at most one and there is no directed cycle; a reciprocated two-arrow pair constitutes a directed cycle of length two and cannot be a face. The empty arrow set is a face. An elementary simplicial collapse removes a face with a unique immediate coface together with that coface. The complex \(\partial\Diamond^n\) is the boundary of the \(n\)-dimensional cross-polytope, with \(n=1\) interpreted as \(S^0\).

## Proof

Write \(A\) for the set of core arrows, and denote the two pendant arrows at \(v\) by \(a_v:v\to w_v\) and \(b_v:w_v\to v\). For any legal face \(F\), its **core part** \(R=F\cap A\) is itself a legal multipath of the original digraph.

**1. Every nonempty core part has a free endpoint.** Fix any nonempty legal core-arrow set \(R\). The selected core digraph has indegree and outdegree at most one and contains no directed cycles, so every nontrivial connected component is a directed path. At least one such path has a source and a sink. Choose deterministically, for example, the least labeled core vertex \(p(R)\) incident to exactly one arrow in \(R\). Such a vertex exists. If it has an outgoing core arrow but no incoming one, set \(\lambda_R=b_{p(R)}\); if it has an incoming core arrow but no outgoing one, set \(\lambda_R=a_{p(R)}\).

**2. The pendant toggle is legal throughout the core fiber.** For every legal face \(F\) whose core part is exactly \(R\), the arrow opposite to \(\lambda_R\) is prohibited: it would duplicate the existing incoming or outgoing core arrow at \(p(R)\). Adjoining \(\lambda_R\) when absent cannot duplicate any incoming or outgoing arrow, because the corresponding slot at \(p(R)\) is unoccupied and its leaf has no other incident arrows. It cannot close a directed cycle because the new leaf has no other incident arrow. Therefore the faces in the fixed nonempty core fiber \(\{F:F\cap A=R\}\) are paired **without exceptions** by the involution \(F\mapsto F\triangle\{\lambda_R\}\).

**3. These are genuine elementary simplicial collapses.** Order all nonempty legal core parts \(R\) by decreasing size, breaking ties arbitrarily. Process each \(R\) in this order. Within its fiber, take lower faces \(F\) not containing \(\lambda_R\), in decreasing size, and remove \(F\) and \(F\cup\{\lambda_R\}\). When a pair is removed, its lower face has no other immediate coface left: adjoining any **different core arrow** would yield a strictly larger core part, whose entire fiber was already removed; adjoining any **other pendant arrow** produces a larger face in the same core fiber, which was removed earlier (if legal). The remaining immediate coface is exactly \(F\cup\{\lambda_R\}\). Hence \(F\) is a free face and each pair is an ordinary elementary simplicial collapse, not merely a Morse equivalence. Ties within a fiber cause no difficulty because distinct lower faces of equal size are not comparable. This completely removes all faces with nonempty core parts.

**4. Identify the survivor and its integral homology.** A face with empty core part consists exclusively of pendant arrows. For each \(v\), at most one of \(a_v,b_v\) may occur because together they form a directed two-cycle. There are no restrictions between different pendant pairs. Thus the surviving subcomplex is the simplicial join of \(n\) discrete two-point sets. It is exactly the cross-polytope boundary \(\partial\Diamond^n\), a triangulated \((n-1)\)-sphere. The explicit collapse yields the integral homotopy and homology assertions, including for \(n=1\) and for an edgeless core.

**5. Natural symmetry.** Each core automorphism acts on \(W^{\pm}(D)\), preserves the pendant-only subcomplex, and permutes its \(n\) two-point factors without exchanging the two arrows *within* a factor. The inclusion of the surviving subcomplex induces an integral homology isomorphism and is automorphism-equivariant (the individual collapses need not be). On the join's top reduced homology, a transposition of two zero-sphere factors has sign \((-1)^{(0+1)(0+1)}=-1\). Thus any core automorphism acts by the sign of its underlying vertex permutation, as claimed.

## Verification

The standalone standard-library script `verify.py` constructs the arc list and legal multipath faces by a constraint-based depth-first search. On test instances small enough for the comparison, it independently enumerates every arc subset and checks indegree/outdegree and acyclicity. It then replays the exact decreasing-core/decreasing-face collapse order from the proof, confirming at **every** pair that the lower face has precisely one remaining immediate coface. Finally it compares the entire surviving augmented face set with the expected join of \(n\) zero-spheres, checks its \(3^n\) augmented faces, the pair counts and its reduced Euler characteristic. The archived `verification_output.json` was produced by running `python3 verify.py`.

All 24 selected test digraphs pass, including edgeless cores, directed and bidirected paths, directed and bidirected cycles, complete bidirected digraphs, and a mixed cyclic digraph, for up to six core vertices. The tests cover 34,838 augmented faces and execute 15,622 free-face pairs. They corroborate the explicit all-parameter proof; finite enumeration alone does not establish it.

## Relationship to prior work

Caputi, Collari and Smith [1], first publicly posted January 9, 2026, classify multipath complexes of **bare** bidirected paths and polygons, with further specifically attached polygon gadgets. Their descriptions do not cover adjoining two opposite pendant arrows at **every** vertex of an arbitrary core digraph. Caputi, Collari, Di Trani and Smith [2] develop the multipath homotopy theory and dynamical region decompositions; the present collapse is a new vertex-decoration stabilization rather than a restatement of a bare-path classification. The earlier path-poset framework [3] supplies the definitions, not this conclusion.

Two especially close public computations were compared in full: [4] classifies coherently directed cycles with **one singly oriented** pendant arrow per core vertex, with an orientation-sensitive ball/sphere dichotomy; its single-arrow constraint is incompatible with the opposite-arrow whiskers here. [5] proves a cross-polytope collapse for **once-subdivided forests with all arcs bidirected**, using a leaf-edge induction. Its hypothesis that the core be a once-subdivided forest does not subsume arbitrary original cores, and its sphere dimension depends on the original **edge** count rather than the core vertex count. No exact equivalent or stronger covering statement was found in the inspected primary texts, the published-result comparisons, or the available earlier claims. This is a best-knowledge priority assessment, not a proof that equivalent work cannot exist.

## Limitations

The conclusion relies on **one distinct leaf with both pendant orientations at every core vertex** and on the no-directed-cycle definition of the multipath complex. It does not establish a corresponding sphere collapse for single-orientation whiskers, missing whiskers, several leaves per vertex, loops, or arbitrary directed-edge-set complexes using different cycle conventions. The collapse order uses vertex labels and is not claimed to be equivariant; only the induced homology action is identified. An independent mathematical audit has not been performed, and unindexed equivalent literature remains possible.

## References

[1] L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first public January 9, 2026, especially Propositions 2.3 and 2.6 and Theorems 2.8 and 2.10. https://arxiv.org/abs/2601.05670

[2] L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (public August 2022), especially multipath definitions and dynamical-region methods. https://arxiv.org/abs/2208.04656

[3] L. Caputi, C. Collari and S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, arXiv:2110.11206. https://arxiv.org/abs/2110.11206

[4] *An orientation dichotomy for directed sunlet multipath complexes*, public research result, October 18, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-an-orientation-dichotomy-for-directed-sunlet-multipath-complexes--d4202e50c4ca

[5] *Crosspolytopal collapse of multipath complexes of bidirected subdivided forests*, public research result, October 25, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-crosspolytopal-collapse-of-multipath-complexes-of-bidirected-sub--a365e2daebfe
