# A cone-graph model for the layer-swap fixed forest complex of a bipartite double cover

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph with at least one vertex. Construct a bipartite graph \(B(G)\) with vertex set \(V\times\{+,-\}\), containing the matching edge \(v^+v^-\) for every \(v\in V\) and, for every edge \(uv\in E\), both cross-edges \(u^+v^-\) and \(v^+u^-\). Let \(\tau\) exchange the two layers. For any finite graph \(X\), let \(\mathcal F(X)\) be its **edge-forest complex**: vertices are edges of \(X\), and simplices are edge sets containing no graph-theoretic cycle. Let \(G^\star\) be the cone graph formed by adjoining one apex \(\star\) adjacent to every vertex of \(G\).

**Theorem.** There is a canonical, natural in graph isomorphisms, \(\operatorname{Aut}(G)\)-equivariant PL homeomorphism

\[
\big|\mathcal F(B(G))\big|^{\langle\tau\rangle}
\;\cong_{\mathrm{PL}}\;
\big|\mathcal F(G^\star)\big|.
\]

The action on the right fixes the apex. More precisely, the orbit-vertex simplicial model for the fixed space is *simplicially isomorphic* to \(\mathcal F(G^\star)\); the isomorphism maps the singleton orbit \(\{v^+v^-\}\) to the cone edge \(\star v\) and the two-element orbit \(\{u^+v^-,v^+u^-\}\) to the base edge \(uv\).

For the special case \(G=K_n\), one has \(B(G)=K_{n,n}\). For every \(n\ge2\), the classical matroid shellability theorem therefore gives

\[
\big|\mathcal F(K_{n,n})\big|^{\langle\tau\rangle}
\simeq \bigvee^{\,T_{K_{n+1}}(0,1)} S^{n-1},
\]

where \(T_{K_{n+1}}\) is the ordinary Tutte polynomial of the complete graph's graphic matroid. For \(n=2,3,4,5\), the sphere multiplicities are respectively \(1,6,51,560\). These multiplicities and the nonequivariant matroid shellability theorem are known; the proposed contribution is the natural fixed-space identification that transports them.

## Assumptions and scope

Graphs are finite, loopless, simple, and undirected; isolated vertices are permitted. The graph cone adds exactly one new apex connected once to each original vertex. The layer-swap acts on \(B(G)\) by \(v^\pm\mapsto v^\mp\); it acts on the **edge vertices** of the forest complex and hence on its geometric realization. The fixed set is the geometric fixed-point space, not the induced subcomplex on individually fixed edges. No hypothesis of connectivity, bipartiteness, vertex transitivity, or nonempty edge set is imposed on \(G\). For a one-vertex graph, both sides are points. The equivariance concerns the simultaneous natural \(\operatorname{Aut}(G)\)-action; it does not classify fixed points of additional subgroups of the full automorphism group of \(B(G)\).

## Proof

**1. Geometric fixed-point model.** For a finite simplicial complex with a simplicial action of an involution, every fixed point has barycentric coordinates constant on each involution orbit of vertices. For a vertex orbit \(O\), put the sum of its barycentric coordinates at the new orbit vertex; this identifies the geometric fixed space piecewise linearly with the simplicial complex whose vertices are vertex orbits and whose faces are precisely families of orbits having union a face of the original complex. Here the original vertices are the edges of \(B(G)\). Its edge orbits are exactly the singleton matching edges and the paired cross-edges displayed above.

**2. The double-cover cycle test.** Consider any selection \(A\subseteq E(G)\) of paired cross-edge orbits, and a selection \(R\subseteq V\) of singleton matching-edge orbits. If \(A\) contains a graph cycle of length \(\ell\), its double-cover lift contains a cycle: it is two disjoint cycles of length \(\ell\) when \(\ell\) is even and one cycle of length \(2\ell\) when \(\ell\) is odd. Thus the selected edges of \(B(G)\) can form a forest only when \(A\) is a forest.

Conversely, suppose \(A\) is a forest. For each connected tree component \(T\) of \((V,A)\), choose a bipartition of \(T\). The paired cross-edges over \(T\) form two disjoint copies of \(T\): the sign changes across each base edge, and the chosen bipartition separates the two lifted components. Each selected matching edge at \(v\in T\cap R\) joins these two tree copies. Adding zero or one such bridge preserves acyclicity. Adding two distinct such bridges creates a cycle (travel between their endpoints along the unique path in each tree copy). Components of \((V,A)\) never acquire cross-connections through these matching edges. Hence the selected \(B(G)\) edges are a forest **if and only if** \(A\) is a forest and every component of \((V,A)\) contains at most one vertex of \(R\).

**3. Comparison with the cone.** In \(G^\star\), the edge set corresponding to \((A,R)\) consists of the base edges \(A\) and apex edges \(\{\star v:v\in R\}\). If \(A\) contains a cycle, so does this set. If \(A\) is a forest, two apex edges whose endpoints lie in the same component close a cycle through the apex; at most one apex edge per component leaves a forest. Thus the cone forest test is *identical* to the double-cover test in Step 2. The orbit-to-cone edge bijection consequently preserves all faces in both directions. By Step 1 it gives the claimed PL homeomorphism.

**4. Naturality and the complete-graph consequence.** Every \(\phi\in\operatorname{Aut}(G)\) acts simultaneously on the two layers, commutes with \(\tau\), and maps each of the stated edge orbits to the orbit associated with \(\phi\)'s image of its cone edge. The simplicial isomorphism is therefore equivariant. When \(G=K_n\), the doubled graph is exactly \(K_{n,n}\), and the cone is \(K_{n+1}\). For \(n\ge2\), the latter's graphic matroid has rank \(n\) and no coloops. Classical shellability of matroid independence complexes gives a wedge of \(T_{K_{n+1}}(0,1)\) spheres of dimension \(n-1\). This final wedge statement is a consequence of prior shellability, not a new shellability theorem. \(\square\)

## Verification

The accompanying standard-library Python program `verify_cone_cover.py` independently constructs the cover and cone edge lists, checks the layer-swap orbits, and compares both forest predicates for **every** orbit-subset. It also verifies compatibility with each automorphism of every test graph. It exhaustively checks all \(75\) labeled simple graphs on one through four vertices, plus seven structurally distinct five-vertex graphs. In total it compares \(49{,}302\) invariant edge selections. The checks reproduce the face counts of the cone forests of \(K_3,K_4,K_5,K_6\), including the values underlying the displayed four sphere multiplicities. Reproduce with `python3 verify_cone_cover.py`. The finite tests do not purport to prove the theorem for graphs of unbounded order; Steps 1–4 give the general proof.

## Relationship to prior work

The equivalence between graph forests and graphic-matroid independent sets, and the shellability of matroid independence complexes, are classical. Ardila–Castillo–Samper's 2014 preprint provides a particularly explicit shellability theorem and the known \(T_M(0,1)\) sphere multiplicity formula. Neither specifies this layer-swap fixed space or the cone-graph orbit model. Prior symmetry calculations for complete bipartite graphic-matroid complexes concern integral homology representations rather than this canonical geometric fixed space. Other fixed-space identifications for matching complexes of graph prisms use different graph constructions and a different simplicial complex. Accordingly the theorem is not presented as a new proof of matroid shellability, nor as a claim about matching-complex fixed spaces.

## Limitations

The theorem treats the specified layer-swap involution and the graph \(B(G)\) with its diagonal matching. Removing that matching changes the orbit-to-cone correspondence. Its right-hand side is an ordinary graphic-matroid independence complex, whose homotopy type is classically understood; the contribution is the exact natural fixed-point model. No complete \(\operatorname{Aut}(B(G))\)-subgroup classification, quotient-space classification, or independent publication-priority certification is asserted. An equivalent formulation in the language of signed graphs, rooted forests, or graph coverings cannot be excluded without a broader bibliographic audit.

## References

1. Federico Ardila, Federico Castillo, José Alejandro Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870, first submitted October 14, 2014; in particular its introductory matroid-topology survey and independence-complex shelling theorem. https://arxiv.org/abs/1410.3870 ; complete online text: https://arxiv.org/html/1410.3870v2.
2. Related preprint, *The full integral automorphism module of the \(K_{2,n}\) forest complex*, October/November 2026 public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-full-integral-automorphism-module-of-the-k-2-n-forest-comple--85376ba6b470 (different sizes and module-level rather than geometric-fixed-space statement).
3. Related preprint, *Layer-exchange fixed points of matching complexes of arbitrary graph prisms*, October 2026 public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-layer-exchange-fixed-points-of-matching-complexes-of-arbitrary-g--dfba27ec3a3c (matching complexes of graph prisms, not graphic-matroid forest complexes of diagonal-augmented bipartite double covers).
