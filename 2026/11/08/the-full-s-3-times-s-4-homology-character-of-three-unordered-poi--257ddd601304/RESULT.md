# The full \(S_3\times S_4\) homology character of three unordered points on \(K_{3,4}\)

## Finding

Let \(G=K_{3,4}\) be the geometric complete bipartite graph, and let
\(B_3(G)=\{\{x_1,x_2,x_3\}\subseteq |G|:x_i\ne x_j\text{ for }i\ne j\}\)
be its configuration space of three **unordered** collision-free particles. Its full graph-automorphism group is \(\operatorname{Aut}(G)=S_3\times S_4\), acting by independent permutations of the parts.
Write \(V^{(\lambda)}_r\) for the rational Specht module of \(S_r\) with partition \(\lambda\), and \(\varepsilon_3=V^{(1,1,1)}_3\). Then the **complete positive-degree rational homology representation** is
\[
\begin{aligned}
H_1(B_3(G);\mathbb Q)&\cong V^{(2,1)}_3\boxtimes V^{(3,1)}_4,\\
H_2(B_3(G);\mathbb Q)&\cong
\varepsilon_3\boxtimes\big(V^{(3,1)}_4\oplus V^{(2,1,1)}_4\oplus 2V^{(2,2)}_4\big)\\
&\qquad\oplus V^{(2,1)}_3\boxtimes\big(V^{(1,1,1,1)}_4\oplus V^{(3,1)}_4\oplus V^{(2,1,1)}_4\oplus V^{(2,2)}_4\big),\\
H_i(B_3(G);\mathbb Q)&=0\qquad(i\ge3).
\end{aligned}
\]
The rational Betti vector is \((1,6,28,0,\ldots)\). Neither \(H_1\) nor \(H_2\) has a nonzero class fixed by the full automorphism group. The new part of the result is the 28-dimensional second-homology classification and its full symmetry representation; the rank and natural description of first homology are included to pin down the character argument.

For complete identification, if \(\mu\vdash 3\) and \(\nu\vdash4\) are the permutation cycle types, the character on the corresponding conjugacy class is as follows. The first two entries identify \(\mu\) and \(\nu\); class sizes sum to \(144\).

| Cycle type in \(S_3\) | Cycle type in \(S_4\) | Size | \(\operatorname{tr}H_1\) | \(\operatorname{tr}H_2\) |
|---|---|---:|---:|---:|
| \((1,1,1)\) | \((1,1,1,1)\) | 1 | 6 | 28 |
| \((1,1,1)\) | \((2,1,1)\) | 6 | 2 | -2 |
| \((1,1,1)\) | \((2,2)\) | 3 | -2 | 4 |
| \((1,1,1)\) | \((3,1)\) | 8 | 0 | -2 |
| \((1,1,1)\) | \((4)\) | 6 | -2 | -2 |
| \((2,1)\) | \((1,1,1,1)\) | 3 | 0 | -10 |
| \((2,1)\) | \((2,1,1)\) | 18 | 0 | 0 |
| \((2,1)\) | \((2,2)\) | 9 | 0 | -2 |
| \((2,1)\) | \((3,1)\) | 24 | 0 | 2 |
| \((2,1)\) | \((4)\) | 18 | 0 | 0 |
| \((3)\) | \((1,1,1,1)\) | 2 | -3 | 1 |
| \((3)\) | \((2,1,1)\) | 12 | -1 | 1 |
| \((3)\) | \((2,2)\) | 6 | 1 | 1 |
| \((3)\) | \((3,1)\) | 16 | 0 | -2 |
| \((3)\) | \((4)\) | 12 | 1 | 1 |

## Assumptions and scope

All homology is singular homology with rational coefficients unless otherwise indicated. Part sizes are exactly three and four; particle number is exactly three. The graph is treated as a geometric one-dimensional CW complex, not as a discrete vertex set. Only the natural graph-automorphism action is classified, not the action of an arbitrary homeomorphism of the underlying topological space. The graph's two parts have unequal sizes, so the full combinatorial automorphism group is exactly \(S_3\times S_4\).

Subdivide each of the twelve graph edges once. The resulting graph has \(19\) vertices, \(24\) edges, and every original vertex has degree at least three. Every shortest path between distinct original essential vertices has two edges, and each simple cycle has at least eight edges. These meet the standard sufficient-subdivision conditions for the three-point Abrams unordered cubical configuration model: essential-to-essential paths have at least \(3-1\) edges and simple cycles at least \(3+1\) edges. The cubical model therefore computes the actual configuration-space homology, with the group action respected by the symmetric subdivision.

## Proof

**Cubical chain model.** A cubical cell is an unordered triple of original/subdivision vertices and open subdivided edges such that the closures of the three chosen cells are pairwise disjoint. The degree is the number of chosen open edges. Order each directed subdivided edge by increasing endpoint label, and order the occupied edge factors by the prescribed edge index. The differential replaces each occupied edge in turn by its terminal vertex minus its initial vertex, with the usual alternating product sign. Exact enumeration gives the chain-group dimensions
\[
(\dim C_0,\dim C_1,\dim C_2,\dim C_3)=(969,3264,3510,1192).
\]
The supplied executable builds the complete cubical boundary maps, checks \(\partial_1\partial_2=\partial_2\partial_3=0\) over the integers on every generating cell, and obtains ranks over \(\mathbb F_3\) of \((968,2290,1192)\) for \((\partial_1,\partial_2,\partial_3)\). Every nonzero minor modulo three is nonzero over \(\mathbb Q\), so these are lower bounds on the rational ranks.

**Rank upper bounds and exactness.** The first boundary has rank at most \(969-1=968\); the third has rank at most \(1192\), so the corresponding rational ranks equal their lower bounds. There is a natural, automorphism-equivariant 'sum of particle trajectories' map \(H_1(B_3(G);\mathbb Q)\to H_1(G;\mathbb Q)\). Every four-cycle in \(G\) is a trajectory for one particle with the other two particles fixed at two of the three original vertices outside that cycle. These loops map to the corresponding four-cycles. Four-cycles span \(H_1(K_{3,4};\mathbb Q)\), of dimension \(12-7+1=6\); hence the trajectory map is surjective. Therefore \(\dim H_1(B_3(G);\mathbb Q)\ge6\), giving
\[
\operatorname{rank}_{\mathbb Q}\partial_2\le 3264-968-6=2290.
\]
The computed lower bound is equal to this upper bound, so the rational ranks are **exactly** \((968,2290,1192)\), and the Betti numbers are \((1,6,28,0)\). In particular \(H_3=0\); there are no higher cells.

**First-homology representation.** The trajectory map is a rational isomorphism by the equal dimensions. Orient all original edges from the three-vertex part to the four-vertex part. The graph cycle representation is the tensor product of the two rational augmentation representations; hence \(H_1\cong V_3^{(2,1)}\boxtimes V_4^{(3,1)}\). If \(f_3\) and \(f_4\) are the numbers of fixed vertices of the two permutations, this gives
\[\chi_1(g)=(f_3-1)(f_4-1).\]

**Second-homology character.** For each automorphism, act on the entire cubical complex. Fixed cubical generators contribute their orientation sign, including the sign of the permutation of occupied edges; no edge-orientation reversal occurs for these part-preserving graph automorphisms. Write \(L(g)=\sum_{d=0}^3(-1)^d\operatorname{tr}(g\mid C_d)\). The Lefschetz trace identity, \(H_0=\mathbb Q\), and \(H_3=0\) give
\[\chi_2(g)=L(g)-1+\chi_1(g).\]
The supplied verifier exhaustively checks all \(144\) automorphisms, including their signed fixed cubes, and verifies equivariance of the integral boundary maps on complete representatives of all fifteen conjugacy classes. This gives the fifteen character values in the table. Taking inner products with the ordinary rational irreducible characters of \(S_3\) and \(S_4\) yields exactly the displayed direct-sum decomposition. Summing either character over all \(144\) automorphisms gives zero, proving the assertions about fixed classes.

## Verification

Run `python3 proof/verify_k34.py` from the containing directory, with Python 3 and no third-party packages; the exact expected output is in `proof/verify_k34.out`. The executable enumerates all \(8,935\) cubical generators, tests both integral chain-square identities on all \(4,702\) cells of degrees two and three, and computes the three differential ranks over primes \(2\), \(3\), \(5\), and \(1,000,000,007\). Their respective rank triples are \((968,2289,1192)\) and \((968,2290,1192)\) for the other three primes. The displayed result uses the rank lower/upper-bound proof, not a mistaken inference that a single modular computation equals a rational rank. The \(144\) signed Lefschetz computations and exact character inner products are all checked. Final marker: `K34_THREE_UNORDERED_CHARACTER_PASS`.

## Relationship to prior work

Farley and Sabalka (2004 arXiv preprint; published 2005) develop the discrete-Morse approach to unordered graph braids, not this full representation. Ko and Park (2011 preprint; published 2012) give the general formula for \(H_1\); for the three-connected nonplanar graph \(K_{3,4}\), it implies the known integral first homology \(\mathbb Z^6\oplus\mathbb Z/2\), without determining the second-homology representation.

Maciążek and Sawicki (2019), *Non-abelian Quantum Statistics on Graphs*, calculate configuration homology for \(K_{3,3}\) and the \(K_{2,p}\) family, but neither the three-particle \(K_{3,4}\) character nor an implication yielding the fifteen-class table. Their general results for certain graphs of maximum degree three or having at most one higher-degree vertex do not encompass \(K_{3,4}\), which has three vertices of degree four. Ramos and Yun (2026), *Computing stable homology representations of graph configuration spaces*, study two particles on balanced complete bipartite graphs with a diagonal symmetric-group action and a three-particle case on complete graphs. Its published results do not determine the present three-particle, unbalanced \(S_3\times S_4\) representation.

An existing mathematical-record result computes the **Morse complex** of \(K_{3,4}\); that simplicial complex of acyclic vector fields is not the unordered configuration space studied here. Prior results for three unordered points on \(K_{3,3}\) likewise concern a distinct graph and do not imply the new second-homology character. These comparisons concern exact mathematical statements and implications, not just title matches. No assertion of absolute publication priority is made.

## Limitations

The classification is rational, not an integral determination of \(H_2\), integral representation lattices, a cohomology ring, the fundamental group, or equivariant homotopy type. Modular rank jumps do not by themselves establish an integral Smith normal form. The theorem concerns one natural graph with precisely three particles, not an unrestricted formula for all complete bipartite graphs. Unindexed or presently inaccessible equivalent work remains possible; independent mathematical verification has not been performed.

## References

1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539, first public version 2004-10-25; *Algebraic & Geometric Topology* 5 (2005), 1075–1109. https://arxiv.org/abs/math/0410539
2. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648, first public version 2011-01-13; *Discrete & Computational Geometry* 48 (2012), 915–963. https://arxiv.org/abs/1101.2648
3. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, *Communications in Mathematical Physics* (2019). https://doi.org/10.1007/s00220-019-03583-5
4. E. Ramos and C. H. Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813 (2026). https://arxiv.org/abs/2606.13813
