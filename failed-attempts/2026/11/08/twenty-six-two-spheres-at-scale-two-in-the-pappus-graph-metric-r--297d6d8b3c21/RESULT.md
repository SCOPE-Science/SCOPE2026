# Twenty-six two-spheres at scale two in the Pappus graph metric Rips filtration

## Finding
For the 18-vertex Pappus graph \(P\), let \(K_r=\operatorname{VR}_{\le r}(P)\) be the inclusive Vietoris–Rips complex on its vertices with unit-edge shortest-path distance. Its **previously unclassified scale-two stage** has integral homotopy type
\[
\boxed{K_2\simeq\bigvee^{26}S^2.}
\]
In particular, the inclusion \(K_1\hookrightarrow K_2\) kills all ten integral degree-one generators, and precisely 26 degree-two classes are born at scale two and die at scale three. Combining this new stage with the elementary scale-zero/one/four descriptions and the previously known (not claimed new) scale-three sphere-wedge gives
\[
K_r\simeq
\begin{cases}
18\text{ points},&0\le r<1,\\
\bigvee^{10}S^1,&1\le r<2,\\
\bigvee^{26}S^2,&2\le r<3,\\
\bigvee^{64}S^5,&3\le r<4,\\
\text{point},&r\ge4.
\end{cases}
\]
The complete reduced integral persistence interval decomposition has exactly 17 degree-zero intervals \([0,1)\), ten degree-one intervals \([1,2)\), 26 degree-two intervals \([2,3)\), and 64 degree-five intervals \([3,4)\), with no others. In particular these are also the barcodes over any field. The novelty assertion is the scale-two integral homotopy classification and the resulting previously missing persistence segment, **not** the previously known scale-three homotopy type or symmetry computations.

## Assumptions and scope
The vertex set of \(P\) is \(\mathbb Z/18\mathbb Z\), represented by \(0,\ldots,17\). Join consecutive residues \(i\) and \(i+1\); additionally join \(i\) to \(i+d_i\), where all residues are modulo 18 and \((d_0,\ldots,d_{17})=(5,7,-7,7,-7,-5)\) repeated three times. Regard all edges as undirected, merging duplicates. This is the standard LCF description of the Pappus configuration's Levi graph. It has 18 vertices, 27 edges, is cubic and bipartite with parts \(X=\{0,2,\ldots,16\}\) and \(Y=\{1,3,\ldots,17\}\), has girth six, and has graph diameter four. The metric is shortest-path length **only on the 18 vertices**, with each edge of length one; no metric-graph ball or Čech construction is involved. For real \(r\ge0\), a nonempty vertex subset is a face of \(K_r\) exactly when every pair of its vertices has distance at most \(r\). All thresholds are inclusive and all changes occur at integer values.

## Proof
**1. Complete graph-distance structure.** Breadth-first search from the given LCF edges, or the explicit finite distance verification accompanying this proof, shows every vertex has one vertex at distance zero, three at distance one, six at distance two, six at distance three, and two at distance four. Distance-four adjacency consists of six vertex-disjoint three-cycles (each displayed set is a clique in the graph whose edges denote distance four):
\[
\begin{gathered}
\{0,10,14\},\ \{2,6,16\},\ \{4,8,12\},\\
\{1,11,15\},\ \{3,7,17\},\ \{5,9,13\}.
\end{gathered}
\]
This is an exhaustive assertion about all \(\binom{18}{2}=153\) vertex pairs, verified from the completely specified graph. Distinct vertices in the same bipartition class are at distance two except when they belong to one of those triples, when they are at distance four. An opposite-part pair has distance one if incident and distance three if not. The absence of four-cycles means two vertices of one part have at most one common neighbor in the other part.

**2. The two side complexes.** Let \(A=K_2[X]\) and \(B=K_2[Y]\) denote the full induced subcomplexes. The forbidden distance-four pairs split each part of nine vertices into three groups of three. Thus, as **simplicial complexes**, both are joins of three discrete three-point complexes:
\[
A\cong B\cong D_3*D_3*D_3\simeq\bigvee^{8}S^2,
\]
where \(D_3\) denotes three isolated points. The join formula follows from \(\widetilde H_0(D_3;\mathbb Z)\cong\mathbb Z^2\) and the standard based join/suspension equivalence; equivalently the two-point rank in each of three factors produces \(2^3=8\) two-sphere summands. Hence \(A\) and \(B\) are connected and simply connected.

**3. A cover whose intersection is the original graph.** Write \(\Delta(S)\) for a simplex on \(S\), and \(N_P(v)\) for the set of three graph-neighbors of vertex \(v\). Define
\[
\begin{aligned}
U&=A\ \cup\ \bigcup_{y\in Y}\bigl(\{y\}*\Delta(N_P(y))\bigr),\\
V&=B\ \cup\ \bigcup_{x\in X}\bigl(\{x\}*\Delta(N_P(x))\bigr).
\end{aligned}
\]
Every mixed clique of \(K_2\) either has at most one vertex in \(X\) or at most one vertex in \(Y\): a mixed clique with two of each would create a four-cycle in \(P\). Consequently \(K_2=U\cup V\). The two subcomplexes meet in precisely the graph \(P\), because their common simplices consist of all vertices and the original incidence edges, with no higher-dimensional common face. Hence \(U\cap V=P=K_1\).

Each \(y\in Y\) occurs in exactly one cone \(\{y\}*\Delta(N_P(y))\) of \(U\), with its base contained in \(A\). Removing these cone apexes by elementary simplicial collapses shows \(U\simeq A\), and symmetrically \(V\simeq B\). Thus both \(U\) and \(V\) are simply connected. Since \(P\) is a connected graph, every map \(P\to U\) and every map \(P\to V\) is nullhomotopic: a spanning-tree contraction reduces such a map to a map from a wedge of circles, and all its loops vanish in the simply connected targets.

Finite simplicial inclusions are cofibrations. Their homotopy pushout therefore splits, using the two null attaching maps, as
\[
K_2=U\cup_P V\simeq U\vee V\vee\Sigma P.
\]
The connected graph \(P\) has \(27-18+1=10\) independent loops, so \(P\simeq\bigvee^{10}S^1\) and \(\Sigma P\simeq\bigvee^{10}S^2\). It follows that
\[
K_2\simeq\bigvee^{8+8+10}S^2=\bigvee^{26}S^2,
\]
integrally and at the level of homotopy type, not merely in mod-two homology.

**4. Full filtration and persistence.** For \(0\le r<1\), the complex consists of 18 isolated vertices. For \(1\le r<2\), it is exactly the triangle-free graph \(P\), hence \(\bigvee^{10}S^1\). For \(3\le r<4\), the sole forbidden pairs are precisely the distance-four pairs in the six disjoint triples displayed in Step 1. Thus \(K_3\) is **exactly** the join of six copies of \(D_3\), equivalent to \(\bigvee^{2^6} S^5=\bigvee^{64}S^5\). This scale-three description is already known and is included for completeness rather than claimed as a new result. At \(r\ge4\), all vertex pairs are adjacent and \(K_r\) is a full simplex.

The reduced degree-zero map from scale zero to one kills all 17 initial components. Degree-one homology is nonzero only on \([1,2)\), degree two only on \([2,3)\), and degree five only on \([3,4)\). Since there are no repeated nonzero reduced homology degrees at adjacent scales, every positive-degree persistence module splits into precisely the intervals stated above; no nontrivial persistence-map ambiguity remains. The integral homotopy equivalences also imply torsion-freeness in every stage.

## Verification
The included Python 3 standard-library program `verify_pappus_rips.py` reconstructs the graph independently from its LCF code, performs 18 complete breadth-first searches, tests all distance-four pairs against the six specified triples, checks the side-complex and union/intersection descriptions, and enumerates all 225 scale-two nonempty simplices. An independently implemented staged-toggle matching pairs 99 face pairs in this scale-two complex, leaving **one critical vertex and 26 critical 2-cells**. A topological sort of the entire directed Hasse graph, involving all 225 faces, proves this matching acyclic. Forman's discrete-Morse theorem thus independently certifies the same integral 26-sphere homotopy type, without relying on the pushout argument. Exact binary boundary eliminations give reduced mod-two ranks 26 in degree two at scale two and 64 in degree five at scale three, matching the integral structural proof. The program enumerates all 4095 nonempty scale-three simplices and verifies they equal the join-of-six-triads construction; it confirms diameter four. These computations are exhaustive finite checks. They are not used to infer an unproved infinite-family assertion. The supplied output ends with `PAPPUS_RIPS_EXACT_FINITE_CHECK_PASS`.

Run from the directory containing the included verifier:
```
python3 verify_pappus_rips.py
```

## Relationship to prior work
Adamaszek [1] identifies graph-power clique complexes with shortest-path Vietoris–Rips complexes, and proves collapses for graphs of girth at least \(3r+1\). The Pappus graph has girth six, below the radius-two requirement of seven, and its scale-two sphere wedge is not implied by that theorem. His paper is the archive-era source motivating the graph-metric problem; it does not classify the present graph. Larrión, Pizaña and Villarroel-Flores [2], and Kawamura [3], establish general fundamental-group and relative-homology relations for clique complexes of bipartite graph squares. Their inspected theorems provide constraints and comparison tools, but neither computes the scale-two Pappus flag complex's 26 integral sphere summands or its persistence intervals.

A published projective-plane incidence graph calculation [4] gives a different graph family: the Pappus \((9_3)\) configuration has nine points and nine lines, whereas a projective plane of order two has seven points and seven lines, one of order three has thirteen of each, and no finite projective plane has exactly nine points. A published affine-plane incidence calculation [5] likewise concerns a different point-line count and parallel-class geometry; it cannot be specialized to this eighteen-vertex graph. A same-graph Pappus **Čech** complex calculation [6] finds 44 second-homology spheres at Čech parameter three: its faces arise from unions of graph neighborhoods about edges, not the pairwise graph-distance clique rule, so it does not cover this result. An earlier graph-metric scale-three Pappus sphere-wedge calculation is expressly excluded from the novelty assertion. The missing scale-two homotopy and barcode segment were not found in the inspected indexed statements; an unindexed equivalent classification cannot be ruled out.

## Limitations
The novel assertion concerns one naturally specified finite incidence graph at one graph-metric scale; it does not establish a general result for all cubic girth-six, distance-regular, or partial-geometric incidence graphs. The persistence classification uses unit edge weights, finite vertex shortest-path distances, inclusive thresholds, and reduced integral homology. The proof gives no equivariant representation or canonical persistence bases. The finite exact checks are reproducible but do not provide independent mathematical peer review. Publication priority may be affected by unindexed or inaccessible equivalent work. The scale-three statement is previously known, not independently novel here.

## References
[1] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (first submitted 2011-04-03), Proposition 2.2 and Sections 2–3; https://arxiv.org/abs/1104.0433 .

[2] F. Larrión, M. A. Pizaña and R. Villarroel-Flores, *The fundamental group of the clique graph*, *European Journal of Combinatorics* **30** (2009), 288–294; DOI: 10.1016/j.ejc.2007.12.006.

[3] K. Kawamura, *A variant of the bipartite relation theorem and its application to clique graphs*, *Contributions to Discrete Mathematics* **6** (2011), 91–100; DOI: 10.55016/ojs/cdm.v6i2.62059.

[4] *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*, public full mathematical statement and proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3 .

[5] *Affine-plane incidence Rips complexes have two sphere dimensions*, public full mathematical statement and proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-affine-plane-incidence-rips-complexes-have-two-sphere-dimensions--3087baeea0a4 .

[6] *The scale-three graph Čech nerve of the Pappus graph is a wedge of forty-four two-spheres*, public full mathematical statement and proof, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-scale-three-graph-ech-nerve-of-the-pappus-graph-is-a-wedge-o--2ff2beca323b .

[7] E. W. Weisstein, *Pappus Graph*, MathWorld; https://mathworld.wolfram.com/PappusGraph.html .
