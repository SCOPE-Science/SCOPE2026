# Integral homotopy types of multipath complexes of bidirected friendship graphs

## Finding

For every integer \(m\ge2\), the multipath complex of the fully bidirected friendship graph satisfies
\[
X_m\simeq S^{m-1}\vee\bigvee^{2m} S^m.
\]
For \(m=1\), the complex is \(S^1\sqcup S^1\). In particular, for all \(m\ge2\), \(\widetilde H_{m-1}(X_m;\mathbb Z)\cong\mathbb Z\) and \(\widetilde H_m(X_m;\mathbb Z)\cong\mathbb Z^{2m}\), with all other reduced integral homology groups zero. This is a homotopy classification, not merely a Betti-number calculation.

## Assumptions and scope

Fix an integer \(m\ge1\). The simple undirected friendship graph \(F_m\) has vertices \(h,a_i,b_i\) for \(1\le i\le m\), and exactly the three undirected edges \(ha_i,hb_i,a_ib_i\) on each triangle. The digraph \(\overleftrightarrow F_m\) has both oriented arcs on every undirected edge. A multipath is a spanning arc-subgraph whose weakly connected components are isolated vertices or simple directed paths. The complex \(X_m\) has one vertex for each directed arc; a collection of arc-vertices spans a simplex exactly when the arcs form a multipath. Define peripheral arcs \(p_i=(a_i,b_i)\), \(q_i=(b_i,a_i)\) and let \(A\subseteq X_m\) be the subcomplex containing no hub-incident arc. Then \(A=*_{i=1}^m\{p_i,q_i}\cong S^{m-1}\), where each two-point factor is a discrete zero-sphere.

## Proof

**1. Classification of hub patterns.** For a nonempty simplex \(\sigma\), let \(H(\sigma)\) be its subset of arcs incident with \(h\). Since each selected vertex has indegree and outdegree at most one and directed cycles are prohibited, \(H\) is empty, one arc, or an incoming/outgoing pair. An incoming/outgoing pair cannot use the same non-hub endpoint (a directed two-cycle). A pair in different petals is allowable. In a single petal exactly two such pairs are allowable, namely \(a_i\to h\to b_i\) and \(b_i\to h\to a_i\).

Fix \(H\) and consider its fiber in the nonempty face poset. Peripheral arcs in any petal not touched by \(H\) are independently either omitted, chosen as \(p_i\), or chosen as \(q_i\), never both. If \(H\) consists of one arc, or a pair in different petals, any petal touched by \(H\) has exactly one compatible peripheral orientation: \(h\to a_i\) or \(b_i\to h\) permits \(p_i\), whereas \(h\to b_i\) or \(a_i\to h\) permits \(q_i\). This compatibility is unaffected by hub arcs in a different petal. If \(H\) is the two-arc path within one petal, neither peripheral arc of that petal can be used: one creates a directed triangle and the other violates an in/out-degree bound. All other petals remain independent.

**2. An acyclic matching.** The assignment \(\sigma\mapsto H(\sigma)\) is order-preserving from the nonempty face poset into the Boolean poset of hub-arc sets. Construct an acyclic matching independently in each fiber and unite them by the poset patchwork lemma (an oriented gradient cycle cannot traverse distinct fibers, because its hub set could only decrease).

For the empty-hub fiber, write its nonempty faces as nonempty words of length \(m\) over \(\{0,p,q\}\), where \(0\) denotes an omitted peripheral arc. For a face not containing every \(q_i\), let \(j\) be the least index with no \(q_j\). Pair it by toggling \(p_j\), unless this produces the excluded empty face. This pairing is well-defined, leaves precisely the singleton \(p_1\) and the top face \(q_1\cdots q_m\) critical, and is acyclic: along a reversed matched edge \(j\) stays fixed, while an unmatched downward cover can only weakly decrease the least index lacking \(q_j\); at fixed index the presence of \(p_j\) can only increase on gradient edges.

For a fiber whose hub set is a singleton or consists of two arcs in different petals, toggle the unique allowed peripheral orientation in a chosen touched petal. All faces are paired; this is acyclic because along oriented matched edges that orientation is added and its removal is the matched edge. For a fiber with a two-arc path in petal \(i\), use the same least-index-missing-\(q_j\) toggle on all petals except \(i\), now including the empty peripheral word (the fixed two hub arcs already make the face nonempty). Exactly one critical face remains: the two hub arcs together with \(q_j\) for all \(j\ne i\). It has dimension \(m\). There are two possible hub paths per petal, hence exactly \(2m\) such critical faces. The patchwork lemma therefore produces, for \(m\ge2\), one critical 0-cell, one critical \((m-1)\)-cell and exactly \(2m\) critical \(m\)-cells, and no other critical cells. In the case \(m=1\), the empty-hub fiber leaves two critical vertices, while the two same-petal path fibers each leave one critical edge.

**3. A simplicial retraction and the attaching maps.** Define \(r:X_m\to A\) on arc-vertices: it fixes every \(p_i,q_i\); it sends \(h\to a_i\) and \(b_i\to h\) to \(p_i\); and it sends \(h\to b_i\) and \(a_i\to h\) to \(q_i\). In any allowed simplex, every hub arc's image is the same peripheral orientation as any peripheral arc simultaneously selected in its petal. The two allowable hub arcs in one petal also have identical images. Consequently no image simplex contains both \(p_i\) and \(q_i\); hence \(r\) is simplicial and restricts to the identity on \(A\). It follows that inclusion \(A\hookrightarrow X_m\) is split-injective on integral homology.

For \(m\ge2\), the acyclic matching yields a CW model with one point, one \((m-1)\)-cell and \(2m\) cells of dimension \(m\). Its \((m-1)\)-skeleton is \(S^{m-1}\). The cellular boundary from dimension \(m\) to \(m-1\) must vanish: otherwise the resulting \(H_{m-1}\) could not contain the direct summand \(H_{m-1}(A;\mathbb Z)\cong\mathbb Z\), since the CW model has only one generator in dimension \(m-1\). Each top-cell attaching map \(S^{m-1}\to S^{m-1}\) therefore has degree zero. For every \(m\ge2\), these maps are nullhomotopic because \(\pi_{m-1}(S^{m-1})\cong\mathbb Z\) and degree classifies such maps. The claimed wedge decomposition follows. For \(m=1\), direct enumeration gives two disjoint three-cycles, hence two disjoint circles.

## Verification

The standalone `verify_friendship.py` reconstructs every face using directed-degree and directed-cycle tests, builds the hub-fiber matching, independently checks every Hasse incidence and global acyclicity, and verifies the simplicial retraction. It also directly computes reduced mod-two simplicial homology for \(1\le m\le4\). The recorded runs for \(1\le m\le6\) found respectively 13, 101, 585, 2,889, 12,933, and 54,189 faces including the empty face. The verified Morse vectors for \(m=2,3,4,5,6\) are respectively \((1,1,4)\), \((1,0,1,6)\), \((1,0,0,1,8)\), \((1,0,0,0,1,10)\), and \((1,0,0,0,0,1,12)\). The finite tests corroborate, but do not replace, the unrestricted combinatorial proof above.

Run `python3 verify_friendship.py` with standard Python 3. No libraries beyond the standard library are needed.

## Relationship to prior work

Caputi, Collari and Smith (2026) calculate connectivity and homology for **single** bidirected polygonal digraphs, and ask for further homotopy classifications. Caputi, Collari, Di Trani and Smith (2022/2024) develop dynamical-module decompositions and results for directed paths, polygons, small grids, and tournaments. A friendship digraph has multiple directed three-cycles meeting at one hub; these families and their stated homotopy theorems do not give the present multi-petal integral decomposition. The present argument instead uses a fiberwise Morse matching and a compatible simplicial retraction. In particular, a result about ordinary undirected matching complexes of Dutch windmills does not imply the theorem: a bidirected multipath complex retains directed paths and excludes directed cycles, and it is generally not that ordinary matching complex.

## Limitations

The result assumes all three undirected edges of each petal are fully bidirected, every petal is triangular, petals meet only at their shared hub, and the multipath condition excludes all directed cycles. It makes no claim for longer petals, partial orientations, or general cactus graphs. The homotopy classification is proved by a standard discrete-Morse existence theorem plus elementary attaching-map arguments; no independent external mathematical audit is asserted. The finite verification cannot by itself establish the all-parameter theorem.

## References

- L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first public January 9, 2026. https://arxiv.org/abs/2601.05670
- L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (2022); *Mathematika* 70 (2024), e12235. https://arxiv.org/abs/2208.04656
- R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (standard discrete-Morse framework).
