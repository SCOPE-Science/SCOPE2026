# Universal first path-homology barcodes with unchanged reachability topology

## Finding

Let \(\mathcal B=\{[b_i,d_i):1\le i\le k\}\) be any finite multiset of intervals with \(k\ge0\), \(0\le b_i<d_i\le\infty\). There is a filtration \((D_t)_{t\ge0}\) of finite simple directed **acyclic** graphs on the same finite vertex set, with inclusions for increasing \(t\), such that:

1. The reachability order of every \(D_t\) is the same linear order. In particular its reachability/concatenation Alexandrov vertex topology is constant and contractible (whether the convention takes upper or lower sets).
2. Its integral **regular GLMY path homology** satisfies
   \[
   H_0^{\mathrm{path}}(D_t;\mathbb Z)\cong\mathbb Z,\qquad
   H_1^{\mathrm{path}}(D_t;\mathbb Z)\cong
   \bigoplus_{i:b_i\le t<d_i}\mathbb Z,\qquad
   H_q^{\mathrm{path}}(D_t;\mathbb Z)=0\quad(q\ge2).
   \]
3. The inclusion-induced maps in degree one identify the persistent homology module *integrally*, with distinguished primitive generators, with \(\bigoplus_i\mathbb Z_{[b_i,d_i)}\). Here an interval module is \(\mathbb Z\) on the interval and zero otherwise, with identity maps between its nonzero terms. Thus over every field the complete degree-one barcode is exactly \(\mathcal B\), with no extra intervals.

The empty barcode is realized by a directed path alone. Endpoint values need not be integers, and \(d_i=\infty\) is permitted. A finite interval has strictly positive length; ephemeral zero-length intervals are not asserted.

## Assumptions and scope

All graphs are simple, without loops or multiarcs. For a graph \(D\), let \(A_p(D)\) be the free integral group on allowed regular directed \(p\)-paths, and define
\[
\Omega_p(D)=\{c\in A_p(D):\partial c\in A_{p-1}(D)\},\qquad
\partial(v_0,\ldots,v_p)=\sum_{j=0}^p(-1)^j(v_0,\ldots,\widehat v_j,\ldots,v_p).
\]
For \(p=0\), the usual convention is \(\Omega_0=A_0\); \(H_*^{\mathrm{path}}\) is homology of this integral subcomplex. Acyclicity ensures vertices are never repeated along an allowed path, so the regular versus nonregular convention does not change the present calculation. Filtrations add edges without deleting vertices. Topology refers to reachability (the transitive closure), not the discrete edge-adjacency topology.

## Proof

**Construction.** If \(k>0\), put \(V=\{0,1,\ldots,3k\}\). Include the \(3k\) covering arcs \(j\to j+1\) for every \(t\). For block \(i\), put \(x=3(i-1)\), \(y=x+1\), \(z=x+2\), \(w=x+3\). Add the *birth arc* \(x\to w\) exactly when \(t\ge b_i\). Add the *death arc* \(x\to z\) exactly when \(t\ge d_i\), omitting it permanently if \(d_i=\infty\). Because \(b_i<d_i\), each block has only three states: a length-three directed path, a path with its long shortcut, and a path with both shortcuts. Every arc points strictly forward, and the covering arcs already imply \(u\leadsto v\) exactly for \(u\le v\), independent of \(t\). This proves the topology assertion.

**Single-block integral calculation.** Write \(e_{uv}\) for the directed edge \(u\to v\). The underlying undirected graph is connected, and its integral cycle rank in degree one is \(0\), \(1\), or \(2\) in the three respective states, because it has \(3\), \(4\), or \(5\) edges on four vertices.

Before the birth, \(\Omega_2=0\): any allowed two-path has a unique nonallowed shortcut face. During the active interval, this remains true; the long shortcut \(x\to w\) is not a shortcut for either allowed two-path. A primitive generator for the first homology is
\[
\gamma=e_{xw}-e_{xy}-e_{yz}-e_{zw}.
\]
After the death, the two allowed two-paths
\[
\alpha=(x,y,z),\qquad\beta=(x,z,w)
\]
individually belong to \(\Omega_2\), and
\[
\partial(\alpha+\beta)=e_{xy}+e_{yz}+e_{zw}-e_{xw}=-\gamma.
\]
Moreover \(\partial\alpha\) and \(\partial\beta\) are a **primitive** basis of the full integral cycle lattice: their coefficients at \(e_{xy}\) and \(e_{zw}\), respectively, form an identity minor, and all cycle-lattice ranks are two. These exhaust \(\Omega_2\), since the remaining allowed two-path \((y,z,w)\) has the unique nonallowed face \((y,w)\). No \(\Omega_p\) with \(p\ge3\) survives: the only candidate three-path is \((x,y,z,w)\), whose boundary contains the nonallowed two-path \((x,y,w)\), and there are no longer allowed paths. Consequently all blocks have zero homology in dimensions \(p\ge2\), and the local active class dies exactly when the short arc is inserted.

**Gluing and persistence.** Adjacent blocks meet only in their common vertex, with no arcs bypassing the shared vertex into another block. An allowed path using vertices of distinct blocks must pass through their common articulation vertex. For \(p\ge2\), deleting such a separating vertex gives a **nonallowed** face. That face uniquely specifies the original crossing path: the articulation vertex has a unique possible insertion position between the two blocks. Therefore its coefficient cannot cancel with any other allowed path in an \(\Omega_p\)-chain. Thus no crossing paths enter \(\Omega_p\) for \(p\ge2\), and \(\Omega_p\) splits over the individual blocks in these dimensions. In degree one the cycle lattice of the one-vertex union of the block graphs is the direct sum of their integral cycle lattices. Since the block boundaries split as well, the first path homology is the direct sum of the active \(\gamma_i\) classes, and higher homology vanishes. All identifications are by the actual displayed integer chains, with no rationalization or torsion assumptions. Since each inclusion adds only its specified block arc, the maps preserve each generator until it becomes \(-\partial(\alpha_i+\beta_i)\), when it maps to zero. This proves the full integral persistence assertion. Connectedness gives \(H_0=\mathbb Z\).

For \(k=0\), choose a single-vertex directed graph and its constant filtration; the same conclusions hold with an empty degree-one barcode.

## Verification

The supplied dependency-free `verify.py` constructs allowed paths and solves the integral path-complex boundary-invariance equations by exact rational Gaussian elimination; this is a **finite consistency check**, not a substitute for the preceding integral proof. It verified all \(3^k\) stage-state combinations for \(1\le k\le3\): a total of \(39\) states, as well as five stages of an overlapping two-interval example \([1,3),[2,4)\). It checked acyclicity, covering edges, the predicted degree-one ranks and the vanishing of all higher ranks. Integral primitivity and persistence maps are proved directly above, not inferred from the rational checks.

To reproduce: run `python3 verify.py` beside this file, using Python 3 and no third-party dependencies.

## Relationship to prior work

Muranov and Muranova (2026) formulate path complexes with concatenation, the induced vertex topology, and the relationship to digraphs; their paper provides the immediate setting but not this prescribed persistence construction. Hepworth and Roff (2023) show reachability homology and path homology can distinguish different properties already at a fixed graph. Thus *static* failure of reachability topology to determine path homology is prior knowledge, not claimed new here. Chaplin, Harrington and Tillmann (2024) develop grounded persistent path homology of weighted digraphs, which is a different filtration and different persistent descriptor; the present theorem is specifically ordinary integral GLMY path homology under directly prescribed edge insertions.

The advance here is a uniform exact realization of **every finite collection of arbitrary positive-length degree-one intervals, including finite deaths and integral persistence maps**, under a filtration whose reachability order never changes.

## Limitations

This is an existence construction with a fixed finite vertex set of \(3k+1\) vertices (for \(k>0\)); it does not assert minimality, realization by a graph-distance filtration, stability of the barcode, arbitrary non-free integral persistence modules, or arbitrary higher-degree barcodes. The exact theorem does not identify its barcodes with the distinct grounded persistent path homology invariant. Independent external mathematical validation has not been performed. Complete publication-priority certainty is not claimed.

## References

1. Yu. Muranov and A. Muranova, *Path complexes with concatenation and their relation to digraphs* (2026), arXiv:2611.15308v1, https://arxiv.org/abs/2611.15308 (first public 11 November 2026).
2. R. Hepworth and E. Roff, *The Reachability Homology of a Directed Graph* (2023), arXiv:2312.01378, https://arxiv.org/abs/2312.01378.
3. T. Chaplin, H. A. Harrington and U. Tillmann, *Grounded Persistent Path Homology: A Stable, Topological Descriptor for Weighted Digraphs* (2024), DOI:10.1007/s10208-024-09679-2, https://doi.org/10.1007/s10208-024-09679-2.
4. T. Chaplin, *First Betti number of the path homology of random directed graphs* (2022), https://doi.org/10.1007/s41468-022-00108-3.
