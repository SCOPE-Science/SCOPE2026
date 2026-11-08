# All-threshold sphere wedges for bouquets of quadrilaterals

## Finding
Let \(B_m\) be the graph obtained by identifying one vertex of each of \(m\) distinct four-cycles and otherwise keeping the cycles vertex-disjoint. For any integer \(k\ge4\), the \(k\)-robust clique complex \(\operatorname{Cliq}_k(B_m)\), comprising vertex subsets whose induced subgraphs have independence number at most \(k-1\), has integral homotopy type
\[
\bigl|\operatorname{Cliq}_k(B_m)\bigr|\simeq
\bigvee^{\binom{m}{k-1}} S^{2k-3}
\qquad(m\ge1,\ k\ge4).
\]
The empty wedge is a point. Thus \(m<k-1\) is the exact contractible regime, whereas \(m\ge k-1\) yields a nontrivial wedge of spheres. This includes \(\operatorname{Cliq}_4(B_3)\simeq S^5\), \(\operatorname{Cliq}_4(B_4)\simeq\bigvee^4S^5\), and \(\operatorname{Cliq}_5(B_5)\simeq\bigvee^5S^7\). The construction below also proves the formula for \(k=2,3\); these lower thresholds are included for completeness, not claimed as independent new contributions.

The homotopy equivalence is integral, not solely an equality of Euler characteristics or field-valued Betti numbers. In the noncontractible regime the only nonzero reduced integral homology is \(\widetilde H_{2k-3}\cong\mathbb Z^{\binom{m}{k-1}}\).

## Assumptions and scope
All graphs are finite, undirected, loopless and simple. Write the vertices of \(B_m\) as the common vertex \(v\) and three additional vertices \(a_i,b_i,c_i\) for each \(1\le i\le m\). The edges of the \(i\)-th quadrilateral are \(va_i,a_ib_i,b_ic_i,c_iv\), and there are no other edges. In particular the separate quadrilaterals share exactly the vertex \(v\), **not** an edge or a three-vertex path.

For \(S\subseteq V(B_m)\), let \(\alpha(B_m[S])\) be the maximum cardinality of an independent vertex subset of the induced graph. Define
\[
\operatorname{Cliq}_k(B_m)=\{S\subseteq V(B_m):\alpha(B_m[S])\le k-1\}.
\]
We use the nonempty-face poset for discrete Morse matching; the empty face is not a critical cell. The binomial coefficient is zero when its lower index exceeds its nonnegative upper index.

## Proof
**Exact face test.** For a subset \(S\) that does not contain \(v\), set \(e_i=|S\cap\{a_i,c_i\}|\in\{0,1,2\}\), let \(\epsilon_i\) indicate whether \(b_i\in S\), and put \(B(S)=\sum_i\epsilon_i\). Removing \(v\) disconnects the graph into the \(m\) paths \(a_i-b_i-c_i\). An independent set in one such path uses either the chosen endpoints or the chosen middle vertex. Consequently
\[
\alpha(B_m[S])=\sum_{i=1}^m\max(e_i,\epsilon_i).
\tag{1}
\]
An independent set in \(B_m[S\cup\{v\}]\) either omits \(v\), when its maximum cardinality is (1), or contains \(v\), when it can use precisely the selected middle vertices and no selected endpoints. Therefore
\[
\alpha(B_m[S\cup\{v\}])=
\max\left\{\sum_i\max(e_i,\epsilon_i),\ 1+B(S)\right\}.
\tag{2}
\]
These identities hold for every choice of \(S\), including the empty subset.

**Explicit matching.** First match every nonempty face \(S\) omitting \(v\) to the face \(S\cup\{v\}\), whenever the latter is a face. The vertex \(\{v\}\) stays unpaired. Every other face containing \(v\) is paired in this first stage. Equations (1)–(2) show that all remaining faces are \(v\)-free and satisfy
\[
\sum_i\max(e_i,\epsilon_i)\le k-1,\qquad B(S)=k-1.
\tag{3}
\]
Indeed a \(v\)-free face survives precisely when adjoining \(v\) would violate the independence bound. Since \(B(S)\le\sum_i\max(e_i,\epsilon_i)\), equality \(B(S)=k-1\) follows.

Let \(I=\{i:b_i\in S\}\). Equation (3) forces \(|I|=k-1\), \(e_i=0\) for \(i\notin I\), and \(e_i\le1\) for \(i\in I\). Hence each remaining face has **exactly** the form
\[
\{b_i:i\in I\}\ \cup\ T,
\quad |I|=k-1,\quad T\cap\{a_i,c_i\}\in\{\varnothing,\{a_i\},\{c_i\}\}\ (i\in I),
\]
with no other vertices. For each \(i=1,\ldots,m\), in increasing order, match every still-unpaired face omitting \(a_i\) to its coface obtained by adjoining \(a_i\), whenever both are still unpaired. In the block with fixed \(I\), this matches the local state \(\varnothing\) against \(\{a_i\}\) and leaves only \(\{c_i\}\). After all stages the only unpaired faces, apart from \(\{v\}\), are
\[
Q_I=\{b_i,c_i:i\in I\},\qquad I\in\binom{[m]}{k-1}.
\tag{4}
\]
There are \(\binom m{k-1}\) such faces, each with \(2k-2\) vertices and hence dimension \(2k-3\). If \(m<k-1\), none exist.

**Global acyclicity, including cross-block incidences.** Orient an unmatched face-cover relation downward and a matched relation upward. The indicator of the presence of \(v\) never decreases along a directed edge: every possible cover removing \(v\) from a face of cardinality at least two is one of the first-stage matched relations, oriented upward. A directed cycle therefore has constant \(v\)-indicator. A cycle consisting of \(v\)-containing faces is impossible because within that stratum all arrows strictly decrease dimension.

In the \(v\)-free stratum, \(B(S)\) never increases along an arrow. The only upward arrows add an \(a_i\); every downward arrow deletes one vertex. Thus a cycle has constant \(B\). When \(B\le k-2\), all faces in this stratum were matched with \(v\), so there are no upward arrows inside the stratum and no cycle. The remaining possibility is \(B=k-1\). A directed cycle then preserves the entire index set \(I\), because downward arrows can only delete middle vertices and no upward arrow adds them. Thus it lies in a single block described after (3).

In that block, the state of each selected arm is one of \(0,a,c\), meaning no endpoint, the endpoint \(a_i\), or the endpoint \(c_i\). All edges removing a \(c_i\) are unmatched and oriented \(c\to0\), so the number of \(c\)-states cannot increase; a cycle must keep the set of \(c\)-states fixed. If not every state is \(c\), let \(j\) be the first selected index not in state \(c\). The construction matches \(0\leftrightarrow a\) at index \(j\), orienting \(0\to a\), while at all later indices an edge \(a\to0\) is oriented downward. With the \(c\)-states fixed, the \(j\)-state cannot decrease and later \(a\)-states cannot increase. No directed cycle is possible. The unique all-\(c\) state is critical. This proves acyclicity on the *entire* Hasse graph, not only within isolated blocks.

**Homotopy conclusion.** Forman's discrete Morse theorem gives a CW complex with one zero-cell and precisely \(\binom m{k-1}\) cells of dimension \(2k-3\), and no other cells. Because \(k\ge4\) (indeed \(k\ge2\) suffices), every attaching sphere maps into a zero-skeleton consisting of a single point. All attaching maps are nullhomotopic. The CW complex is exactly a wedge of the claimed spheres, proving the theorem including the empty-wedge boundary.

## Verification
The standalone `verify.py` reconstructs each graph from its edge list and computes every induced-subgraph independence number using a vertex-deletion dynamic program, independently of (1)–(2). It then forms the complete robust clique complex, carries out the indicated face-cover matching, checks the exact critical-face set and pair counts, and topologically sorts the **entire directed Hasse graph** to confirm acyclicity. For small cases it additionally evaluates every candidate independent \(k\)-subset directly.

The executed code passed all \(30\) parameter pairs \(1\le m\le6\), \(2\le k\le6\), including the nontrivial cases \((m,k)=(5,4)\) with 3,201 nonempty faces, 1,595 matching pairs, and ten critical five-cells; and \((m,k)=(6,6)\) with 99,747 nonempty faces, 49,870 matching pairs, and six critical nine-cells. Full output is included in `verify_output.txt`, and the run ended with `ALL_VERIFY_OK`.

The finite checks confirm the implementation and local formulas. The proof for every integer \(m\ge1\) and \(k\ge4\) is symbolic and does not extrapolate finite enumeration.

## Relationship to prior work
Filakovský [1], first publicly posted February 11, 2026, studies robust clique complexes of square-sequence graphs obtained by *edge* gluing or *corner* completion of quadrilaterals. Theorem 1.2 treats the third threshold, while Corollary 1.3 treats arbitrary thresholds when all steps are edge gluing. A bouquet \(B_m\) with \(m\ge2\) is **not** a square-sequence graph in that sense: it has a cut vertex, and each new quadrilateral shares only one vertex and contributes three new vertices. Accordingly, the all-threshold bouquet formula does not follow from those theorems or their proposed extension to square-sequence graphs.

Kim and Lew [2] introduced the bounded-independence complexes under the notation \(I_k(G)\), equivalent to \(\operatorname{Cliq}_k(G)\), and studied collapsibility bounds rather than this integral homotopy classification. An indexed result [3] establishes a sphere-wedge theorem for the third threshold on connected bipartite graphs, so the case \(k=3\) is not an originality claim here. Previously indexed finite four-threshold calculations for grids and short square sequences do not cover the two-parameter vertex-bouquet theorem. The new contribution is the complete \(k\ge4\) classification with a uniform globally acyclic matching.

## Limitations
The formula concerns one-vertex bouquets of unfilled four-cycles, not arbitrary cactus graphs or edge-glued square complexes. It gives ordinary (nonequivariant) integral homotopy types, not equivariant decompositions or assertions of shellability. The topological theorem does not claim the novelty of the existing third-threshold case. A logically stronger unindexed result may exist; independent review has not been performed.

## References
[1] M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first posted 2026-02-11. https://arxiv.org/html/2602.11365

[2] M. Kim and A. Lew, *Complexes of graphs with bounded independence number*, arXiv:1912.12605, first posted 2019-12-29; Israel Journal of Mathematics 249 (2022), 83–120. https://arxiv.org/abs/1912.12605

[3] *A three-sphere wedge theorem for robust clique complexes of all connected bipartite graphs*, indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-sphere-wedge-theorem-for-robust-clique-complexes-of-all--8d06720b1a2b .
