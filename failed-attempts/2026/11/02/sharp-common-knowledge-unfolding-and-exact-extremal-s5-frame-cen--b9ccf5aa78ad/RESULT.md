# Sharp common-knowledge unfolding and exact extremal S5-frame census

## Finding

Fix integers \(n\ge2\) and \(k\ge2\). For a finite classical \(k\)-agent S5 frame \(\mathcal F=(W,E_1,\ldots,E_k)\) with \(|W|=n\), let \(D(\mathcal F)\) be the smallest number of everybody-knows iterations sufficient to agree with common knowledge for **every** event on \(W\). Then \(D(\mathcal F)\le n-1\), and equality holds precisely when the union of the agents' equivalence relations, with loops discarded, is one spanning undirected path.

The entire equality class has an exact all-size census. Write \(F_{n,k}\) for the number of **ordered** \(k\)-tuples of equivalence relations on the fixed labelled carrier \([n]\) satisfying \(D(\mathcal F)=n-1\). Define \(u_1(s)=1\) for \(1\le s\le k\), and recursively for every \(\ell\ge1\)
\[
 u_{\ell+1}(s)=\sum_{t=1}^{k-s}\binom{k-s}{t}u_\ell(t),\qquad 1\le s\le k,
\]
where an empty sum is zero. Then
\[
 \boxed{F_{n,k}=\frac{n!}{2}\sum_{s=1}^k\binom{k}{s}\,u_{n-1}(s).}
\]
For two agents this specializes to \(F_{2,2}=3\) and \(F_{n,2}=n!\) for every \(n\ge3\). For three agents, \(F_{2,3}=7\), \(F_{3,3}=36\), \(F_{4,3}=360\), and \(F_{5,3}=4320\). On the one-world carrier the maximum depth is zero and the unique relation tuple realizes it.

## Assumptions and scope

The carrier \(W\) is a **nonempty finite labelled set**, and the \(k\) knowledge relations \(E_i\subseteq W^2\) are equivalence relations, with agents individually named. There are no structural restrictions connecting distinct agents' partitions. The result concerns classical finite S5 frames, equivalently the discrete-intuitionistic-order subcase of an S5 epistemic frame; it does not assert the same bound for nontrivial intuitionistic orders.

For an event \(X\subseteq W\), let
\[
 K_i(X)=\{w\in W:[w]_{E_i}\subseteq X\},\qquad
 E(X)=\bigcap_{i=1}^{k}K_i(X),\qquad E^0(X)=X,\quad E^{r+1}(X)=E(E^r(X)).
\]
Let \(G\) be the undirected simple graph with an edge \(\{w,v\}\) for \(w\ne v\) when \(wE_iv\) for at least one agent \(i\). Define
\[
 C(X)=\{w\in W:\operatorname{Comp}_{G}(w)\subseteq X\},\qquad
 D(\mathcal F)=\min\{r\ge0: \forall X\subseteq W,\ E^r(X)=C(X)\}.
\]
The fixed-point semantics \(C(X)\) is common knowledge of the proposition whose truth set is \(X\); arbitrary events can be named by one propositional variable.

## Proof

**(1) Reachability and sharp depth.** For every integer \(r\ge0\), induction gives
\[
 E^r(X)=\{w\in W:\text{every vertex at graph distance at most }r\text{ from }w\text{ lies in }X\}.
\]
At \(r=0\) this says \(w\in X\). The inductive step quantifies over the union of all one-step agent successors. Therefore \(D(\mathcal F)\) equals the maximum of the graph diameters of the connected components of \(G\), with singleton diameter zero. For a component of size \(m\), every two vertices are linked by a simple path of length at most \(m-1\); hence \(D(\mathcal F)\le n-1\). If the depth equals \(n-1\), some component must contain all \(n\) worlds, and a geodesic of length \(n-1\) exhausts its vertices. An extra nonconsecutive edge would shorten that geodesic, so \(G\) is exactly a path. Conversely the endpoints of a spanning path have distance \(n-1\); taking \(X\) to omit one endpoint proves that the bound is attained and that no earlier iteration suffices.

**(2) Agent subsets on path edges.** Fix an undirected labelled spanning path \(w_1-\cdots-w_n\). For each edge \(e_j=\{w_j,w_{j+1}\}\), let \(S_j=\{i\in[k]:w_jE_iw_{j+1}\}\). Because the union graph contains the edge, \(S_j\ne\varnothing\). Adjacent subsets \(S_j\) and \(S_{j+1}\) are disjoint: otherwise the common agent relates three successive vertices and, by transitivity, adds a forbidden shortcut edge. Conversely, any nonempty subsets \(S_1,\ldots,S_{n-1}\subseteq[k]\) with \(S_j\cap S_{j+1}=\varnothing\) define uniquely the \(k\) agent partitions: for each agent use precisely its marked edges as two-point classes and leave all other vertices singleton. The marked edges of any one agent form a matching, so these really are equivalence relations and their union graph is exactly the chosen path. This is a two-way correspondence, including cases where several agents share a single edge.

**(3) Counting without overidentifying agents.** For a prescribed initial edge label \(S\) of size \(s\), the remaining \(\ell-1\) labels are counted by \(u_\ell(s)\). The next label is any nonempty \(t\)-subset of \([k]\setminus S\), yielding exactly the recurrence in the finding. Summing over the \(\binom{k}{s}\) choices of first label counts all admissible label sequences. There are \(n!/2\) distinct undirected spanning paths on \([n]\) for \(n\ge2\), because reversal gives the same path and each labelled path has precisely two orientations. Multiplying proves the displayed formula. For \(k=2\) and at least two edges the only admissible sequences alternate the singleton labels, so there are exactly two sequences and \(F_{n,2}=n!\) for \(n\ge3\); the single-edge case admits three nonempty labels.

## Verification

The accompanying standalone `checker.py` generates all equivalence relations as set partitions; independently forms their union graph and computes its diameter by breadth-first expansion. It compares direct counts to the transfer recurrence for all carriers through six worlds with two agents, through five worlds with three agents, and also the one-agent boundary through five worlds. It checks that every extremal graph on at least three worlds has exactly \(n-1\) undirected edges, and verifies the stated numerical special cases. Execute `python checker.py` in a directory containing this file; the expected terminal marker is `ALL_CHECKS_OK`. The proof above, not exhaustive small-carrier testing, establishes the formula for every \(n,k\) in scope.

## Relationship to prior work

Zenger's *Intuitionistic Common Knowledge* (first posted May 1, 2026) provides the S5 epistemic/common-knowledge semantics and the classical S5 embedding that motivates a finite approximation question. In the discrete-order S5 subcase its common-knowledge operator quantifies over the reflexive transitive closure of the union of agent relations. The reachability interpretation itself is standard in the earlier common-knowledge literature, including Halpern and Moses. The contribution claimed here is not that known semantics but the sharp **uniform finite unfolding depth**, the full structural characterization of equality cases, and their exact all-agent labelled enumeration. Neither the inspected treatment of common-knowledge semantics nor the closest finite-partition probability studies states these three joint conclusions. The transfer recurrence is related to walks on the graph of disjoint nonempty subsets of an agent set; such combinatorial reformulations are potential sources of older equivalent enumerations.

## Limitations

The results classify only the **maximal possible** unfolding depth; they do not count frames at each smaller depth, and they do not determine truth of arbitrary fixed formulas. The free finite S5 setting is essential: additional frame constraints or a nontrivial intuitionistic order can change the answer. The accessible literature comparison does not establish historical uniqueness; older enumeration or finite-epistemic-model work might contain an equivalent count under different terminology. No independent audit is claimed.

## References

1. Lukas Zenger, *Intuitionistic Common Knowledge*, arXiv:2605.00523 (initial public version, 2026-05-01), Sections 2.2 and 4.1, https://arxiv.org/abs/2605.00523.
2. Joseph Y. Halpern and Yoram Moses, *Knowledge and Common Knowledge in a Distributed Environment*, Journal of the ACM 37 (1990), 549–587; publicly accessible preprint arXiv:cs/0006009, https://arxiv.org/abs/cs/0006009.
