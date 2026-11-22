# Integral sphere wedges for the dual four- and five-cut complexes of the Petersen line graph

## Finding

Let \(P=\operatorname{KG}(5,2)\) denote the Petersen graph, and let \(G=L(P)\) be its fifteen-vertex line graph. Its ordinary cut complexes \(\Delta_k(G)\) for \(k=4,5\) have Alexander duals \(D_k=\Delta_k(G)^\vee\) satisfying

\[
D_4\simeq\bigvee^{196}S^2,
\qquad D_5\simeq\bigvee^{624}S^3.
\]

In particular, integral combinatorial Alexander duality determines all reduced integral homology groups of the original cut complexes:

\[
\widetilde H_i(\Delta_4(G);\mathbb Z)\cong
\begin{cases}\mathbb Z^{196},&i=10,\\0,&i\ne10,\end{cases}
\quad
\widetilde H_i(\Delta_5(G);\mathbb Z)\cong
\begin{cases}\mathbb Z^{624},&i=9,\\0,&i\ne9.\end{cases}
\]

This is a complete *integral* homotopy classification of the Alexander duals, not merely a calculation of rational Betti numbers.

## Assumptions and scope

The Petersen graph is modeled on the ten two-subsets of \(\{0,1,2,3,4\}\), with two vertices adjacent exactly when disjoint. Its fifteen edges are ordered lexicographically by pairs of endpoints. These ordered edges form the vertices \(\{0,\ldots,14\}\) of \(G\); two vertices in \(G\) are adjacent precisely when the corresponding edges of \(P\) share an endpoint. Thus \(G\) is a simple four-regular graph with thirty edges.

For \(k\in\{4,5\}\), write \(\mathcal B_k\) for the set of all \(k\)-element subsets \(B\subseteq V(G)\) for which the induced subgraph \(G[B]\) is disconnected. The ordinary cut complex \(\Delta_k(G)\) has facets \(V(G)\setminus B\) as \(B\) ranges over \(\mathcal B_k\). Its combinatorial Alexander dual is therefore exactly

\[
D_k=\{F\subseteq V(G):\text{no }B\in\mathcal B_k\text{ is contained in }F\}.
\]

The empty face is understood; only nonempty faces are represented in the certificates. No other graphs or cut thresholds are covered.

## Proof

**Exact finite construction.** The included `verify.py` builds \(P\) and \(G\) from these definitions, enumerates all disconnected \(k\)-subsets, and tests every subset of the fifteen vertices against the displayed avoidance criterion. For \(k=4\), there are 1,185 forbidden sets and 767 nonempty dual faces, with face vector by dimension \((15,105,455,180,12)\). For \(k=5\), there are 2,556 forbidden sets and 2,457 nonempty dual faces, with face vector \((15,105,455,1365,447,70)\).

**Explicit acyclic matching.** Fix vertex order \(0,1,\ldots,14\). Starting with all nonempty faces of \(D_k\), visit vertices in ascending order. At stage \(j\), pair each still-unmatched face \(F\) not containing \(j\) with \(F\cup\{j\}\), provided both faces are still unmatched. Remove both from subsequent stages. Because a face has only one partner under a fixed vertex toggle, the pairs at each stage are disjoint; the program confirms disjointness and face membership. This defines a partial matching on every cover relation of the nonempty face poset.

Reverse the orientation of every matched cover in the downward-directed Hasse diagram. The verifier explicitly generates **every** cover relation and performs a complete topological sort of the resulting directed graph. It processes all 767 vertices and 2,355 covers for \(D_4\), and all 2,457 vertices and 9,690 covers for \(D_5\). Thus no directed cycle remains: this is an acyclic discrete-Morse matching, not a sampled gradient-path check.

The matching has exactly 285 pairs in the first case and 916 in the second. The complete critical-cell enumerations are

\[
\begin{array}{c|c|c}
 &\text{critical zero-cells}&\text{other critical cells}\\\hline
D_4&1&196\text{ of dimension }2\\
D_5&1&624\text{ of dimension }3
\end{array}
\]

and **no critical cells in any other dimension**. Forman's discrete-Morse CW theorem yields one zero-cell and only cells in the indicated common higher dimension. Since all higher-cell attaching maps land in a point, these CW complexes are wedges of the stated spheres. This proves both homotopy equivalences over \(\mathbb Z\), without relying on mod-two calculations to infer integral topology.

**Passing to cut complexes.** Combinatorial Alexander duality on fifteen vertices gives

\[
\widetilde H_i(\Delta_k(G);\mathbb Z)
\cong\widetilde H^{12-i}(D_k;\mathbb Z).
\]

As the dual complexes are the displayed sphere wedges, their reduced integral cohomology is torsion-free and concentrated in degree two or three. Substituting these degrees proves the asserted complete reduced integral homology of both cut complexes.

## Verification

Run `python3 verify.py` in the directory containing the supplied source. It uses the Python standard library only; it exhaustively constructs the actual complexes and verifies matching-pair membership, stage disjointness, all critical dimensions, the entire acyclic Hasse orientation, and mod-two chain ranks. Its exact machine-readable output is in `verification-output.json`. The matching-pair serialization SHA-256 checksums are `0d5449f99814d5588308f1285befcd368be6a6f44e2592f5c19145fe91aca377` for \(D_4\), and `2fe8b99bc5bc95c8fbc7694f8e32e406ba2a0ed78ecacc92902fc11ae3ed16fc` for \(D_5\).

Run `python3 independent_crosscheck.py` from the same directory for a separate enumeration of the *original* ordinary cut complexes and their mod-two simplicial boundary ranks. This reuses the canonical graph-construction helper but enumerates a different side of Alexander duality; its output appears in `independent-output.txt`. It finds respectively 31,999 and 30,309 nonempty cut faces, with the only reduced mod-two Betti numbers 196 in degree ten and 624 in degree nine. These ranks corroborate but are not substitutes for the complete integral Morse proof.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced ordinary cut complexes and developed graph-family topological methods in *Topology of Cut Complexes of Graphs* (arXiv:2304.13675, first public 2023-04-26). Their sequel (arXiv:2407.08158) develops disjoint-union, squared-path and grid cases. The present graph is the line graph of the Petersen graph, not the Petersen graph itself nor a complete-graph line graph. The dual complexes here have higher-dimensional faces and the graph contains triangles, so published high-girth four-cut classifications do not apply. Published calculations of the Petersen graph's cut complexes, the cuboctahedral three-cut complex, and the scale-three intrinsic Čech complex of the Petersen line graph concern different graphs, parameters or simplicial constructions, and do not establish these two dual sphere wedges. No uniqueness claim beyond the inspected literature is made.

## Limitations

The result is confined to the two indicated thresholds and the exactly specified fifteen-vertex graph. It does not determine homotopy types of the original cut complexes, equivariant homology representations, larger line-graph families, or other thresholds. The proof is finite and exhaustive but computational: its verification requires executing the included full face-poset and acyclicity checker; a shorter conceptual collapse rule or closed-form general-family theorem is not supplied. Equivalent unpublished or unindexed work could exist.

## References

- M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs* (2023 preprint; SIAM J. Discrete Math. 38 (2024)), https://arxiv.org/abs/2304.13675.
- M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II* (2024 preprint; SIAM J. Discrete Math. 39 (2025)), https://arxiv.org/abs/2407.08158.
- R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145; standard acyclic discrete-Morse correspondence.
- Combinatorial Alexander duality for finite simplicial complexes (standard integral formulation).
