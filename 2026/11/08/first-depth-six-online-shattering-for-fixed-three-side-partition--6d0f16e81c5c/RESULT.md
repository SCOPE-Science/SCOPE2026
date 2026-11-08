# First depth-six online shattering for fixed-three-side partitions

## Finding

Consider the concept family \(\mathcal H_{n,3}\) of all **unlabeled** bipartitions of \([n]\) into nonempty blocks of sizes \(3\) and \(n-3\), queried by pairwise same-block membership. At \(n=9\),
\[
\operatorname{VCdim}(\mathcal H_{9,3})=5,\qquad
\operatorname{Ldim}(\mathcal H_{9,3})=6.
\]
Furthermore, nine is the **smallest** ground-set order \(n\ge4\) for which \(\operatorname{Ldim}(\mathcal H_{n,3})\ge6\): it is strictly less than six for \(4\le n\le8\), and at least six for every \(n\ge9\). This does not determine the exact Littlestone dimension for \(n>9\).

## Assumptions and scope

Vertices are labeled \(0,1,\dots,n-1\); queries are unordered pairs \(\{u,v\}\) of distinct vertices. The Boolean answer is one precisely when both vertices lie in the same block. A complete depth-\(d\) mistake tree has a query at every internal node; every binary root-to-leaf answer sequence must be realized by some hypothesis. The VC dimension uses one fixed query support for all answer patterns. No stochastic assumption and no graph-cut orientation is imposed. At \(n=9\), the three-element block is uniquely identified by its set of vertices.

## Proof

**Number of concepts and adaptive upper bound.** There are exactly \(\binom93=84\) concepts at \(n=9\). A complete binary mistake tree of depth \(d\) requires at least \(2^d\) distinct concepts: a single concept cannot realize two different leaf traces because those traces first disagree at one common node. Since \(64\le84<128\), the Littlestone dimension is at most six. For \(4\le n\le8\), the number of partitions is at most \(\binom n3\le\binom83=56<64\), including the case of equal block sizes, when the count is smaller. Thus none has dimension six. For \(n>9\), take every three-element block inside the first nine vertices and put all remaining vertices in the larger block; restricting all queries to the first nine vertices reproduces the full nine-vertex concept class.

**Explicit adaptive lower bound.** The included `depth6_tree.json` is a complete depth-six binary query tree with \(63\) internal nodes and \(64\) leaves, using just eight distinct unordered pairs. Each leaf records a three-element-block witness. The separate `verify_three_block_cut.py` checks every node, all sixty-four root-to-leaf traces, and the witnesses against the literal same-block relation \(\mathbf1[(u\in A)=(v\in A)]\). Hence the Littlestone dimension at \(n=9\) is at least six, establishing the equality and the claimed sharp first order. The certificate is finite and fully included, not a probabilistic search result.

**Static lower bound.** Consider the five pairs \(\{0,i\}\) for \(1\le i\le5\). For any requested zero/one pattern, choose the three-element block among vertices \(1,\dots,8\), omitting vertex \(0\). The affirmative leaves must also be omitted; the negative leaves must be included. If there are \(k\) negative leaves, then choose all of them if \(k\le3\), filling the remaining positions from the three unused vertices \(6,7,8\); if \(k>3\), instead put \(0\) in the three-element block and choose the complementary pattern. Equivalently, direct enumeration in the checker gives all \(32\) traces. (For an elementary uniform construction without cases, if there are at most three negatives choose \(A\) to contain exactly the negative leaves, adding unused vertices; if there are at least four negatives choose \(A\) to contain \(0\) and precisely the positive leaves, adding unused vertices. The available three unused vertices always suffice.) Thus \(\operatorname{VCdim}\ge5\).

**Static upper bound.** Suppose a six-edge support is shattered. Its graph must be acyclic: on a cycle, labeling all but one edge affirmative and the last edge negative violates transitivity of same-block membership. Any six-edge forest on nine vertices has three connected components, with sorted sizes among
\[
(1,1,7),\ (1,2,6),\ (1,3,5),\ (1,4,4),\ (2,2,5),\ (2,3,4),\ (3,3,3).
\]
For each component of size \(t_i\), arbitrarily color its vertices in two colors with \(c_i\) and \(t_i-c_i\) vertices, and label each forest edge positive exactly when its endpoints have the same color. Because each component is a tree, any globally consistent binary cluster labeling must agree with this coloring or its complement on that component. Therefore the possible sizes of the designated three-vertex block are exactly the sums of one term from each pair \(\{c_i,t_i-c_i\}\). For the seven component-size profiles above, choose respectively
\[
(c_1,c_2,c_3)=(0,0,0),(0,1,0),(0,0,1),(0,0,0),(0,0,0),(0,0,2),(0,0,1).
\]
Direct substitution verifies that no such sum equals three, so the induced answer pattern is not realizable. Therefore no six-edge support is shattered. Since a shattered larger support would contain a shattered six-edge sub-support, \(\operatorname{VCdim}\le5\).

## Verification

Run `python verify_three_block_cut.py depth6_tree.json` with Python 3 standard library only. The script independently verifies all sixty-four leaf traces and sixty-three queries, that every leaf witness has three distinct vertices, that the five-edge star realizes all thirty-two patterns, and that all seven forest profiles have a three-block obstruction. The recorded successful output is `THREE_BLOCK_PARTITION_CHECKS_PASS depth=6 leaves=64 queries=63 distinct_queries=8 VC_lower_traces=32 VC_upper_profiles=7`. An optional dynamic-programming reproducer `construct_depth6_tree.py` regenerates the tree using the exact Littlestone recurrence; the certificate and checker do not depend on this search program.

## Relationship to prior work

Li, Song and Zhang (2021) introduce same-cluster queries for learning partitions without assuming the cluster count. Lutz, de Panafieu, Scott and Stein (2021) study pairwise active clustering, average query counts, and random models of partitions. Their inspected full texts do not state a worst-case adaptive shattering tree for the fixed \(3\)-versus-\(6\) profile, nor an exact Littlestone value six. Earlier finite-partition shattering results already cover aspects of the fixed-profile **VC** calculation, and a smaller fixed-profile separation example; neither establishes the nine-point depth-six lower bound. The new contribution is the explicit sharp depth-six online threshold, not the general idea of same-cluster learning or existing static results.

## Limitations

Exact dimensions of the full fixed-three-side family for \(n>9\) are not asserted. The depth-six tree establishes a lower bound only there. Historical uniqueness has not been independently established: another description of this finite concept family in graph-cut or partition learning literature may subsume the result. Computer verification validates the included finite certificate; it is not an independent scientific audit.

## References

- Yi Li, Yan Song, Qin Zhang, *Learning to Cluster via Same-Cluster Queries*, arXiv:2108.07383v1 (first public 2021-08-17), https://arxiv.org/abs/2108.07383.
- Quentin Lutz, Élie de Panafieu, Alex Scott, Maya Stein, *Active clustering for labeling training data*, arXiv:2110.14521v1 (first public 2021-10-27), https://arxiv.org/abs/2110.14521.
