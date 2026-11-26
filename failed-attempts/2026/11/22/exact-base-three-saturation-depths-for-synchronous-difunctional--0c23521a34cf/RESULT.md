# Exact base-three saturation depths for synchronous difunctional closure

## Finding
Let \(A\) and \(B\) be disjoint finite nonempty sets and \(R\subseteq A\times B\) an arbitrary relation. At each synchronous round, impose **all** instances of the difunctional (or Z-closed/rectangular) rule
\[
(a,b),(a',b),(a',b')\in R_t\quad\Longrightarrow\quad(a,b')\in R_{t+1},
\]
where \(R_0=R\) and previously present pairs are retained. Let \(G_R\) be the undirected bipartite graph with shores \(A,B\) and edges \(R\). Write \(d_R(a,b)\) for shortest-path length in \(G_R\), with \(d_R(a,b)=\infty\) if no path exists.

**Exact trajectory theorem.** For every integer \(t\ge0\) and each \((a,b)\in A\times B\),
\[
(a,b)\in R_t\quad\Longleftrightarrow\quad d_R(a,b)\le3^t.
\]
Consequently the final relation is precisely the union of complete bipartite relations between the opposite shores of each nontrivial connected component of \(G_R\); it is the least difunctional extension of \(R\).

Let \(D_R\) be the largest **finite** distance from a left vertex to a right vertex of \(G_R\), and set \(D_R=1\) when \(R=\varnothing\). The exact number \(\tau(R)\) of strict synchronous updates, i.e. the least \(t\) with \(R_{t+1}=R_t\), is
\[
\tau(R)=\min\{t\in\mathbb N_0:3^t\ge D_R\}.
\]
In particular, for \(p=|A|\), \(q=|B|\), \(h=\min(p,q)\),
\[
\boxed{\max_{R\subseteq A\times B}\tau(R)=\min\{t\in\mathbb N_0:3^t\ge 2h-1\}.}
\]
The upper bound is attained for every pair \((p,q)\) by an alternating path using \(h\) vertices from each shore, with any surplus vertices isolated.

There is also an exact edge-arrival profile for the extremal alternating path. With \(h\) vertices on each shore, put
\[
J_t=\min\left\{h,\left\lfloor\frac{3^t+1}{2}\right\rfloor\right\}.
\]
Then, at the end of round \(t\), the number of pairs present is exactly
\[
|R_t|=J_t(2h-J_t),
\]
and the number added **at** round \(t\ge1\) is the difference between consecutive displayed values.

## Assumptions and scope
The two shores are typed and disjoint, including if the original relation is presented on equal underlying sets; the converse \(R_t^{-1}\) reverses shores. A synchronous update evaluates every premise on the previous round's relation, not on newly inserted pairs of the same round. Repeated vertices in a witness are permitted, but they are not required by the proof. No connectedness or nonemptiness of \(R\) is assumed. Distances are finite only within a connected component. The sharp bound is for both shore sizes specified, rather than merely their sum.

Difunctionality is the property \(S\circ S^{-1}\circ S\subseteq S\), equivalently that each connected bipartite component of the incidence graph is complete bipartite. The rule and the full closure are classical; the theorem concerns the exact intermediate layers, the sharp **parallel** evaluation depth, and its extremal edge-arrival law.

## Proof
**1. One-step operation.** A pair \((a,b')\) is added precisely when there is a three-edge alternating walk \(a-b-a'-b'\) in \(G_{R_t}\). Thus \(R_{t+1}=R_t\cup(R_t\circ R_t^{-1}\circ R_t)\), and the union is actually redundant since \(R_t\subseteq R_t\circ R_t^{-1}\circ R_t\) (repeat an edge). All updates remain inside original bipartite connected components.

**2. Exact distance induction.** For \(t=0\), distance at most one from \(A\) to \(B\) is exactly an edge of \(R\). Suppose the assertion holds at round \(t\) and let \(L=3^t\), an odd positive integer. If \((a,b)\in R_{t+1}\), its three witness edges correspond to original alternating walks of lengths at most \(L\). Their concatenation gives an original \(a\)-to-\(b\) walk of length at most \(3L\), proving \(d_R(a,b)\le3L\).

Conversely, suppose \(d_R(a,b)=\ell\le3L\). Since \(a\) and \(b\) are on opposite shores, \(\ell\) is a positive odd integer. If \(\ell\le L\), the pair is already present by induction. Otherwise \(L<\ell\le3L\), and every odd integer in this interval is the sum of three positive odd integers each at most \(L\): start from \(1+1+1\), and distribute the even increment \(\ell-3\) among three terms, each having capacity \(L-1\). Partition a shortest path into three consecutive segments of those lengths. Each segment connects opposite shores and is present as a relation edge (in the appropriate direction) at round \(t\), by induction. The Z-rule then inserts \((a,b)\) at round \(t+1\). This proves the equivalence for all finite graphs and all rounds.

**3. Fixed point and exact time.** A component containing an edge has vertices on both shores. At the first \(t\) such that \(3^t\ge D_R\), every cross-shore pair in each component has appeared; the resulting disjoint bicliques are difunctional and hence stable. If \(3^t<D_R\), a finite-distance pair is absent. That absent pair must eventually be added: it is included once \(3^u\ge D_R\). An increasing finite sequence cannot be stable at an earlier step and later change, since the update map is deterministic. Therefore the least fixed-point round is the stated \(\tau(R)\). For the empty relation, \(D_R=1\) by convention and \(R_t=\varnothing\) at all rounds.

**4. Sharp shore-size cutoff.** Any shortest path between opposite shores is simple and has odd length \(2j-1\), using exactly \(j\) distinct vertices of each shore. Thus \(j\le h\) and \(D_R\le2h-1\). For equality, take the path \(a_1-b_1-a_2-b_2-\cdots-a_h-b_h\); its endpoints have distance \(2h-1\). Extra vertices, if any, can be isolated. This gives equality in the universal round cutoff for all \(p,q\ge1\), including \(h=1\), for which closure is already complete.

**5. Exact path arrival profile.** On the alternating path with \(2h\) vertices, there are exactly \(2h-(2j-1)=2(h-j)+1\) unordered opposite-shore pairs at distance \(2j-1\), for each \(j=1,\ldots,h\). (Every such pair has its left endpoint at one of the \(2h-(2j-1)\) possible path positions.) The exact-distance theorem includes precisely those indices \(j\le J_t\). Summing gives \(\sum_{j=1}^{J_t}(2h-2j+1)=J_t(2h-J_t)\).

**6. Comparison with the anchored Z-closure iteration.** A previously published approach fixes the outer two factors at the original relation, giving \(T_0=R\) and
\[
T_{t+1}=R\circ T_t^{-1}\circ R.
\]
For this **different** iteration the analogous exact graph-distance law is
\[
(a,b)\in T_t\quad\Longleftrightarrow\quad d_R(a,b)\le 2t+1.
\]
Indeed, each three-factor witness has its first and last segments of length one, and its middle segment of length at most \(2t+1\), giving the forward bound. Conversely, an odd original shortest path of length at most \(2t+3\) either was previously present or can be split after its first and before its last edge, with the middle odd segment of length at most \(2t+1\). On the extremal alternating path with \(h\) vertices in each shore, this anchored update requires exactly \(h-1\) rounds, whereas fully synchronous self-composition requires \(\min\{t:3^t\ge2h-1\}\) rounds. This quantitative comparison is a corollary about two explicit algorithms, not an attribution of the anchored algorithm to this result.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. The verifier implements the Z-shaped completion rule directly from triples of old edges, independently computes shortest-path distances by breadth-first search on the original bipartite graph, and compares every full intermediate relation with the distance threshold. It additionally checks the exact stabilization round against the computed cross-diameter, exhaustively enumerates every incidence matrix for shore-size pairs \((1,1),(1,5),(2,3),(3,3),(3,4),(4,4)\), tests 1,400 seeded random larger matrices, and checks explicit sharp alternating paths for \(h=1,\ldots,25\). It also independently computes the anchored relation update of Cao–Chen–Kerre, compares its exact \(2t+1\) metric law and its linear sharp path depth with direct matrix updates.

The checked run emitted `VERIFY_OK 71642 exhaustive and random matrices; 25 sharp paths; anchored-rule comparison`. This is finite corroboration only; the preceding induction and simple-path extremal argument establish the unrestricted theorem.

## Relationship to prior work
Riguet's classical difunctional-closure relation and later coalgebraic presentations already identify the limiting closure as \(R\circ(R^{-1}\circ R)^*\). That formula implies which edges eventually appear, but by itself does not specify the exact intermediate relations produced by one **fixed synchronous Z-rule**, their metric birth times or the optimal finite-shore number of rounds. The contribution here is the exact \(3^t\) law, the graph-dependent and sharp dimension-dependent stopping rule, and the full size profile of extremal paths. It should not be construed as a new definition or an invention of difunctional closure.

Cao, Chen and Kerre (2010, displayed definition before their Lemma 2) use the **anchored** recurrence \(T_{t+1}=R\circ T_t^{-1}\circ R\), while their \(R^*\) is the eventual Z-closure. Its use of the original \(R\) in both outer factors is a material distinction: it grows the original graph-distance radius as \(2t+1\), not \(3^t\). Section 6 of the proof derives the sharp linear versus logarithmic round comparison. The historical anchored definition and final fixed point are fully credited; neither is claimed new.

Uezato (2026) examines complexity of relation-algebra compositions and circuits, providing a recent impetus to distinguish relation-algebraic output expressibility from the stages needed by a particular closure evaluation. Its studied formulas, circuit lower bounds and model constructions are not the synchronous Z-rule. Zarrad and Gumm discuss difunctional closures in coalgebraic bisimulations; Backhouse and Voermans concern the algebraic core and indices of relations. Neither inspected portion states the synchronous distance law or its sharp cutoff. The present priority comparison is best-knowledge, not a claim that all older literature has been exhausted.

## Limitations
This is a special monotone, simultaneous inference strategy, not a bound for arbitrary fair sequential firing, general binary Horn rules, or arbitrary relation-algebra circuit evaluation. The empty-relation convention is explicit. The extremal path edge count concerns that construction only, not every relation with the same stabilization time. The result follows from a short graph-distance induction and elementary bipartite path counting; no additional complexity-theoretic lower bound is asserted. Independent mathematical verification and exhaustive historical-priority review have not been performed.

## References
1. Yuya Uezato and Yoshiki Nakamura (revised preprint), *An Exponential Succinctness Gap between Three-Variable Logic and the Calculus of Relations*, first posted 22 September 2026, arXiv:2609.26778. https://arxiv.org/abs/2609.26778
2. Mehdi Zarrad and H. Peter Gumm, *Transitivity and Difunctionality of Bisimulations*, available full-text reproduction, Section 2, Definition 1 and its closure equation. https://www.mathematik.uni-marburg.de/~gumm/Papers/Transitivity_and_Difunctionality_of_Bisimulation.pdf
3. Roland Backhouse and Ed Voermans, *The Index and Core of a Relation: With Applications to the Axiomatics of Relation Algebra*, arXiv:2309.02017, 2024. https://arxiv.org/abs/2309.02017
4. Yongzhi Cao, Guoqing Chen and Etienne E. Kerre, *Bisimulations for Fuzzy-Transition Systems*, arXiv:1012.2148, first posted 10 December 2010, definition of Z-closure preceding Lemma 2 and its anchored relation iteration. https://arxiv.org/abs/1012.2148 (full-text reproduction inspected at https://www.academia.edu/70936277/CAO_CHEN_AND_KERRE_BISIMULATIONS_FOR_FUZZY_TRANSITION_SYSTEMS_1_Bisimulations_for_Fuzzy_Transition_Systems)
5. J. Riguet, classical difunctional-closure formula, as credited and restated in references 2–3; the original text was not inspected directly.
