# The super-domination polynomial first loses the super-coalition number on five vertices

## Finding

For connected simple graphs of order at least three, the polynomial counting super dominating sets by size does not determine the super-coalition number. The minimum order of this obstruction is five. The path \(P_5\) and complete bipartite graph \(K_{2,3}\) each have super-domination polynomial \(z^5+5z^4+6z^3\), but their super-coalition numbers are \(4\) and \(3\), respectively.

The distinction persists on six vertices even if one seeks to recover the full partition spectrum. There are two connected graphs, specified below, both with polynomial \(z^6+6z^5+6z^4\), whose numbers of unordered coalition partitions into \((2,3,4)\) blocks are respectively \((19,39,0)\) and \((19,42,2)\).

## Definitions

A set \(D\) is super dominating if for each \(u\notin D\) some \(v\in D\) has \(N(v)\setminus D=\{u\}\). Write \(S_G(z)=\sum_D z^{|D|}\), summed over these sets, and denote the minimum size by \(\gamma_{\rm sp}(G)\). A super-coalition partition is an unordered partition into nonempty blocks, none individually super dominating, each having a different block with which its union is super dominating. The maximum block count is the super-coalition number \(C_s(G)\). The graph \(H\) has vertex set \(V(G)\) and an edge \(uv\) when \(V(G)\setminus\{u,v\}\) is super dominating.

## Proof

Two distinct omitted vertices must have distinct witnesses, so \(\gamma_{\rm sp}(G)\ge\lceil |V(G)|/2\rceil\). For a graph without isolated vertices, all single-vertex omissions are feasible. A pair \(\{u,v\}\) can be omitted precisely when, outside the pair, there is a neighbour of \(u\) not adjacent to \(v\) and a neighbour of \(v\) not adjacent to \(u\). This test computes \(H\) directly. If \(\gamma_{\rm sp}\ge n-2\), then \(S_G(z)=z^n+n z^{n-1}+|E(H)|z^{n-2}\).

On five vertices the size lower bound gives \(\gamma_{\rm sp}\ge3\). Five singleton blocks cannot all have partners because a pair of singletons is too small. Four blocks must have sizes \(2,1,1,1\), and each singleton can partner only with the two-vertex block. Thus four blocks exist exactly when the three singletons form a triangle in \(H\): their three possible omitted pairs must all be feasible. To check the examples, number the path vertices \(0,1,2,3,4\) in order. Writing \(ij\) for \(\{i,j\}\), the pair test gives
\[
E(H(P_5))=\{03,04,12,13,14,23\}.
\]
In particular \(1,2,3\) form a triangle. For \(K_{2,3}\), omitted vertices in distinct parts can be witnessed by selected vertices in the opposite respective parts; vertices in the same part have identical adjacency outside the pair. Hence \(H(K_{2,3})=K_{2,3}\), with six edges and no triangles. Take any two vertices of the same part as singletons, and their complement as the third block. The large block is not super dominating (the two omitted vertices are in the same part), and its union with either singleton is super dominating. Thus the two graphs do have the claimed numbers, and counting feasible omissions gives their common polynomial.

For a connected graph of order three, every two-vertex set is super dominating and no singleton is, so \(C_s=3\). On four vertices the same pair test gives the following table; the H-edge entry for the path uses the vertex order \(0,1,2,3\). The connected four-vertex graphs are exhausted by the two trees, the cycle and triangle with pendant vertex, the diamond, and the complete graph (sort by edge count).

| Graph | Feasible omitted pairs |
|---|---|
| \(P_4\) | \(03,12\) |
| \(K_{1,3}\) | none |
| \(C_4\) | the four cycle edges |
| triangle with pendant vertex | none |
| \(K_4\) minus an edge | none |
| \(K_4\) | none |

For a four-singleton partition, the two singleton blocks of a pair can partner exactly when their complementary pair is in \(H\). For \(P_4\) and \(C_4\) the graph of complementary pairs has no isolated vertices, giving \(C_s=4\). In all other rows there is no four-block partition, but there is a three-block partition of type \(2,1,1\): the two-vertex class is non-super-dominating and can partner with either singleton. Hence \(C_s=3\) in those rows. The polynomial determines the row's value of \(C_s\) through the coefficient of \(z^2\). This proves minimality.

For the six-vertex assertion, use the labelled vertex set \(\{0,\ldots,5\}\) and original edge sets
\[
 E(G_1)=\{02,03,04,05,12,13\},\qquad
 E(G_2)=\{01,02,04,05,12,13,15,23,24\}.
\]
For both graphs no triple is feasible, as can be checked by the witness test in the following finite form: for each three-element \(U\), form \(\{N(v)\cap U:v\notin U\}\); this family never contains all three singleton subsets of \(U\). Larger omissions are impossible by the size lower bound. The pair test gives
\[
 E(H(G_1))=\{02,03,12,13,14,15\},\qquad
 E(H(G_2))=\{01,02,12,34,35,45\}.
\]
Thus their polynomial agrees. The two feasible-pair graphs have, respectively, six and nine two-edge matchings, no perfect matchings, and zero and two triangles. The established two-deletion census [2] gives \(c_3=15+3\cdot6+m_2-2m_3\) and \(c_4=t\) at order six. The unordered bipartitions are all eligible except those with a super-dominating block, which rule out exactly six singleton omissions and six feasible two-vertex omissions, giving \(c_2=31-6-6=19\). More than four blocks cannot have a successful pairwise union, because at least three vertices would be omitted. This gives the stated spectra.

## Reproduction and limits

The five-vertex obstruction and its cutoff follow directly from the pair lists, four-vertex table, and block arguments. The original standalone `verify.py` checks the six-vertex example by exact enumeration of the witness condition and unordered set partitions; it is not needed for the cutoff. The question here is the loss of information when only the sizes of the super dominating sets are retained, not when their vertex labels are retained.

## Relationship to prior work

Alikhani and Ghanbari [1] introduce super-coalition partitions and study their maximal size. References [2] and [3] already give the two-deletion triangle criterion, the three-block count including its six-vertex correction, and the full spectrum for order at least seven. The contribution here is the explicit nondetermination by the super-domination set polynomial at the smallest connected order, with an additional six-vertex witness at which the three-block counts also differ. It does not claim a new general census.

1. S. Alikhani and N. Ghanbari, *Super Coalition Number in Graphs*, arXiv:2607.22686.
2. *A triangle criterion and exact optimal-partition census for super coalitions near maximal super domination*, [research record](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-a-triangle-criterion-and-exact-optimal-partition-census-for-supe--7b990ea0b4cf).
3. *Universal matching–triangle enumerator for super-coalition partitions at deficiency two*, [research record](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-universal-matching-triangle-enumerator-for-super-coalition-parti--9a591f121323).
