# Crown-line geometry and frozen universal states in complete-prism zero forcing

## Finding

For each integer \(n\ge4\), let \(H_n=K_n\square K_2\), with two labeled cliques \(A=\{A_i:i\in[n]\}\) and \(B=\{B_i:i\in[n]\}\), and only the matching edges \(A_iB_i\) between them. A *standard zero-forcing set* initially colors certain vertices blue; whenever a blue vertex has exactly one white neighbor, that neighbor becomes blue. The *minimum-zero-forcing token-jump graph* \(R_{\mathrm{TJ}}(H_n)\) has all minimum forcing sets as vertices and joins two whenever one selected vertex is exchanged for any unselected vertex. The *token-slide graph* \(R_{\mathrm{TS}}(H_n)\) allows that exchange only across an edge of \(H_n\).

Let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph with its canonical matching removed, let \(L(G)\) be the line graph, and let \(K_1\vee G\) denote adjoining one universal vertex. **Then the exact isomorphism types are**
\[
\boxed{R_{\mathrm{TJ}}(H_n)\cong 2\bigl(K_1\vee L(\operatorname{Cr}_n)\bigr),\qquad
R_{\mathrm{TS}}(H_n)\cong 2K_1\sqcup 2L(\operatorname{Cr}_n).}
\]
Here \(2G\) denotes two disjoint copies of \(G\), not multiplication of a vertex count. In particular, the common state set has \(2n(n-1)+2\) members (a previously determined count); the jump graph has two components, each of radius one and diameter two, while the slide graph has exactly four components: two isolated vertices and two \(n(n-1)\)-vertex, \(2(n-2)\)-regular components of radius and diameter three. The transition counts are, respectively,
\[
\boxed{|E(R_{\mathrm{TJ}}(H_n))|=2n(n-1)^2,\qquad |E(R_{\mathrm{TS}}(H_n))|=2n(n-1)(n-2).}
\]
The isolated slide states are exactly the two full clique layers; each is universal in its jump component.

The complete distance formula in either nontrivial slide component is obtained by labeling its states by ordered pairs \((a,b)\in[n]^2\) with \(a\ne b\):
\[
d\bigl((a,b),(c,d)\bigr)=\begin{cases}
0&(a,b)=(c,d),\\
1&a=c\text{ or }b=d,\\
3&(c,d)=(b,a),\\
2&\text{otherwise}.
\end{cases}
\]
Each nontrivial slide configuration has exactly one antipode, represented by \((b,a)\), and there are exactly \(2(n-2)\) distinct shortest three-slide routes to it. Thus the total number of unordered diametral pairs over both nontrivial components is exactly \(n(n-1)\). The within-component unordered-pair distance enumerator, summed over the two nontrivial slide components, is
\[
\boxed{n(n-1)\left[2(n-2)t+(n-1)(n-2)t^2+t^3\right].}
\]
No distance is asserted between distinct disconnected components.

## Assumptions and scope

The graph is simple and undirected, its two layers are labeled, and the parameter is any integer \(n\ge4\); there is no quotient by automorphisms. Only standard (not skew, positive-semidefinite, or leaky) zero forcing is used. All reconfiguration states are globally minimum-cardinality forcing sets, and every intermediate state must be minimum. Distances are graph-theoretic shortest-path lengths inside one connected reconfiguration component. The small boundary \(n=3\) is intentionally excluded because the two types of mixed minimum sets then admit cross-layer transitions not present at larger orders.

## Proof

**1. All minimum states.** Each vertex of \(H_n\) has degree \(n\). Fewer than \(n\) initially blue vertices cannot make a first force: any blue vertex has at least two white neighbors. Thus the minimum size is at least \(n\). Suppose that a forcing set \(S\) of size \(n\) makes its first force from a blue vertex \(v\). That vertex has exactly one white neighbor, so all other \(n-1\) blue vertices must be the other neighbors of \(v\). If \(v=A_b\), either its unique white neighbor is \(B_b\), yielding the full layer \(A\), or its unique white neighbor is \(A_a\) with \(a\ne b\), yielding
\[
S_A(a,b)=(A\setminus\{A_a\})\cup\{B_b\},\quad a\ne b.
\]
The symmetric alternatives are the full layer \(B\) and
\[
S_B(a,b)=(B\setminus\{B_a\})\cup\{A_b\},\quad a\ne b.
\]
Conversely the full layer \(A\) forces all of \(B\) by its matching edges, and for \(S_A(a,b)\) the vertex \(A_b\) first forces \(A_a\), after which the full layer forces all remaining vertices. Symmetry handles the other cases. Hence this list is exhaustive, every listed set is feasible, and the optimum is \(n\). For \(n\ge4\) the two mixed families are disjoint and each has \(n(n-1)\) members, giving the stated total.

**2. Complete exchange adjacencies.** In the family \(\{S_A(a,b):a\ne b\}\), two distinct sets differ by exactly one exchange if and only if their missing \(A\)-indices are the same, \(a=c\), or their included \(B\)-indices are the same, \(b=d\). These are exactly the edge adjacencies of the line graph of \(\operatorname{Cr}_n\), whose edges are naturally the ordered pairs \((a,b)\) with \(a\ne b\). The full layer \(A\) exchanges with every one of these states. No state in this family exchanges with a state from the \(B\)-majority family: their numbers of selected \(A\)-vertices differ by at least two for \(n\ge4\). The full layers also have no cross-family exchanges. The analogous statement holds with \(A\) and \(B\) interchanged. Hence the jump graph is exactly two cones over \(L(\operatorname{Cr}_n)\).

**3. Sliding adjacencies.** Two mixed \(A\)-states that share their missing index change only the chosen \(B\)-vertex; these changed vertices lie in the same complete clique. Two that share their included \(B\)-index change only the omitted \(A\)-vertex; again the exchanged vertices are adjacent. Thus every line-graph adjacency within each mixed family is a slide. But the exchange from full \(A\) to \(S_A(a,b)\) replaces \(A_a\) by \(B_b\). These vertices are adjacent across the two layers exactly when \(a=b\), a case forbidden by minimal forcing. Thus full \(A\) is slide-isolated, and so is full \(B\). There are no other jumps to turn into slides. This proves the slide-graph isomorphism.

**4. Exact counts and distances.** The crown graph has \(m=n(n-1)\) edges, each with two endpoints of degree \(n-1\). Thus each vertex of its line graph has degree \(2(n-2)\), and its total number of edges is \(m(n-2)\). Adding a universal vertex adds \(m\) edges, so each cone has \(m(n-1)\) edges, proving both transition counts. Since the line graph is connected, each cone has radius one and diameter two (it is not complete). The slide graph has the claimed component sizes and degrees.

Two distinct crown edges \((a,b)\) and \((c,d)\) are adjacent in the line graph if and only if \(a=c\) or \(b=d\). If they have no endpoint in common, a two-edge path exists whenever at least one of the cross edges \((a,d)\) or \((c,b)\) is a legal crown edge. Both cross edges fail precisely when \(a=d\) and \(c=b\), namely when the target is \((b,a)\). In that case choose any \(e\notin\{a,b\}\): the chain \((a,b),(a,e),(b,e),(b,a)\) is a path of length three. This proves the displayed distance formula and uniqueness of the antipode. All geodesics to \((b,a)\) must begin by keeping the first or the second coordinate. In the first case their forced form is \((a,b),(a,e),(b,e),(b,a)\); in the second it is \((a,b),(e,b),(e,a),(b,a)\). The intermediate label \(e\) is any of the \(n-2\) remaining indices. These are distinct paths, and there can be no others; the multiplicity is therefore exactly \(2(n-2)\). Reversal partitions the \(m\) vertices in each line-graph component into \(m/2\) unordered antipodal pairs, giving \(m\) such pairs across both components. At each mobile state there are \(2(n-2)\) neighbors at distance one, \((n-1)(n-2)\) vertices at distance two and one at distance three. Taking half of the ordered counts over the \(2m\) mobile states gives the displayed distance enumerator.

## Verification

Two independent standard-library Python files are supplied. `verify_bruteforce.py` constructs the original \(2n\)-vertex graphs directly, enumerates **every** initially blue subset of size at most \(n\) for \(4\le n\le8\), simulates standard forcing, derives legal exchanges and slides from the underlying graph edges, and checks state lists, components, degrees, transitions, all-pairs distances, unique antipodes, and shortest-path multiplicities. `verify_structure.py` independently constructs the abstract off-diagonal ordered-pair network and checks degree/edge identities for \(4\le n\le12\) and at orders 15, 25 and 50, with complete all-pairs BFS and shortest-path counts through order 12. Both scripts ran successfully; reproducible commands and output appear in `VERIFICATION.md`. These finite checks corroborate but are not substitutes for the all-order proof.

## Relationship to prior work

Geneson, Haas and Hogben (arXiv:2009.00220, first available September 1, 2020) introduced the fixed-size zero-forcing exchange graph, proved generic disconnectedness phenomena and analyzed other named graph families; their inspected manuscript does not provide the complete-prism isomorphisms, sliding classification or distance spectrum. A separately available complete zero-forcing polynomial and exact optimum-state classification for \(K_n\square K_2\) already determines the minimum size \(n\) and count \(2n(n-1)+2\); **neither number is claimed as original here**. Its result does not itself state the exchange and sliding configuration graphs, isolated full-layer states, line-graph distances or antipodal geodesic counts. The later work of Bong et al. (arXiv:2501.03642, 2025) develops universal reconfiguration tools and studies PSD and skew forcing, not this standard-forcing exact complete-prism pair. Distinct previous results about ordinary cycle prisms \(C_n\square K_2\) and about zero forcing *on the crown graph itself* are not results about the present configuration graph, though the crown line graph occurs as its precise geometric representation.

## Limitations

The classification covers complete prisms \(K_n\square K_2\) at \(n\ge4\), not ordinary cyclic prisms, higher rook graph dimensions, or other forcing rules. An isolated vertex has no finite eccentricity to other components. The optimum count and static membership description have been determined previously; the new claim is their precise relocation geometry and geodesic structure. Unindexed or inaccessible equivalent literature remains a historical-priority risk.

## References

1. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1 (2020-09-01); later Discrete Applied Mathematics 329 (2023), 126–139. https://arxiv.org/abs/2009.00220 .
2. *Complete zero-forcing and minimal-fort distributions for matched pairs of cliques*, research record with a complete available result and proof, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-zero-forcing-and-minimal-fort-distributions-for-matched--7e7715a7522c .
3. N. Bong et al., *Reconfiguration of Minimum PSD Forcing Sets and Minimum Skew Forcing Sets*, arXiv:2501.03642v1 (2025-01-07), https://arxiv.org/abs/2501.03642 .
