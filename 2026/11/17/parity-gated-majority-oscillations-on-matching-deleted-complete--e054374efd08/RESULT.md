# Parity-gated majority oscillations on matching-deleted complete graphs

## Finding

Let \(r\ge1\) and \(u\ge0\) be integers, and let \(G_{r,u}\) be the graph obtained from the complete graph on \(2r+u\) labelled vertices by deleting \(r\) pairwise disjoint edges. Thus there are \(r\) distinguished nonadjacent pairs and \(u\) vertices adjacent to every other vertex. Under synchronous binary majority with ties retained, let \(H(r,u)\) denote the number of fixed configurations and \(C_2(r,u)\) the number of distinct primitive temporal two-cycles (not the number of their constituent configurations).

Put \(h=r+(u-1)/2\) when \(u\) is odd. With the convention that a binomial coefficient is zero when its lower argument is not an integer in the permitted range, the exact census is

\[
H(r,u)=\begin{cases}2+2^r,&u=0,\\2,&u\ge1,\end{cases}
\]

\[
C_2(r,u)=\begin{cases}
\dfrac12\left(\binom{2r}{r}-2^r\right),&u=0,\\[2pt]
\dfrac12\binom{2r+u}{r+u/2},&u\ge2\text{ even},\\[2pt]
\binom{r}{\lfloor r/2\rfloor},&u=1,\\[2pt]
\binom{r}{(h+1)/2},&u\ge3\text{ odd and }h\text{ odd},\\[2pt]
0,&u\ge3\text{ odd and }h\text{ even}.
\end{cases}
\]

For odd \(u\ge3\), the primitive two-cycles exist precisely when \(r\ge(u+1)/2\) and \(r+(u-1)/2\) is odd. Consequently, every initial configuration reaches a **uniform consensus state** if and only if this odd-\(u\) condition fails with \(u\ge3\): equivalently, \(u\ge3\) is odd and either \(r<(u+1)/2\) or \(r+(u-1)/2\) is even. For even \(u\), every initial configuration reaches a fixed point or two-cycle within one update; for odd \(u\), within three updates. Equivalently, for the global map \(F\),

\[
F^3=F\quad (u\text{ even}),\qquad F^5=F^3\quad (u\text{ odd}).
\]

These are equalities of maps on the full configuration space, not statements about typical initial configurations.

## Assumptions and scope

Each vertex has a bit in \(\{0,1\}\). All vertices update simultaneously: a vertex takes the strict majority of its open neighbors, and in an exact tie retains its previous bit. The graph is simple and undirected, and the removed edges form a matching. All counts concern labelled configurations, while the count \(C_2\) identifies the two phases of each cycle as one orbit. Both \(r\) and \(u\) are allowed to vary without a size cutoff. The formula covers the cocktail-party graph when \(u=0\), and its joins with a complete graph when \(u>0\).

## Proof

Write \(N=2r+u\) and \(S\) for the number of one-bits in a configuration. A member of a deleted-edge pair \((a,b)\) sees exactly \(S-a-b\) one-neighbors, independently of whether it is \(a\) or \(b\). A universal vertex in state \(x\) sees \(S-x\) ones. The pair degrees are \(N-2\), and the universal degrees are \(N-1\). These identities give the following complete transition rules.

**Even \(u\).** Here \(N=2q\). If \(S<q\), the entire graph becomes zero after one update; if \(S>q\), it becomes one. At \(S=q\), each pair of type \(00\) becomes \(11\), each \(11\) becomes \(00\), and each mixed pair retains its two individual bits. Every universal bit flips. This operation preserves \(S=q\) and is an involution. Thus precisely the \(\binom{N}{q}\) balanced states, together with the two uniform states, are periodic. When \(u=0\), a balanced state is fixed exactly when every pair is mixed, giving \(2^r\) such fixed states. When \(u\ge2\), no balanced state is fixed because the universal bits flip. Division by two of the remaining periodic states proves both even-\(u\) cycle formulas, and the transition rule proves \(F^3=F\).

**Odd \(u\).** Here \(N=2h+1\), with \(h=r+(u-1)/2\). Any \(S\le h-1\) becomes uniformly zero; any \(S\ge h+2\) becomes uniformly one. At \(S=h\), the update makes every universal vertex zero, changes each pair \(00\) to \(11\), and changes every other pair to \(00\). At \(S=h+1\), it makes every universal vertex one, changes each pair \(11\) to \(00\), and changes every other pair to \(11\). In particular, after one update from either critical level, all pairs are uniform and all universal bits agree.

Consider such a post-update state, with \(b\) of the \(r\) pairs equal to \(11\). If all universal bits are zero, its number of ones is \(2b\). If \(2b=h\), the next state has \(2r-h=h+1-u\) ones and all universal bits zero; it remains at the critical level only for \(u=1\), in which case the pairs swap and swap back. If \(2b=h+1\), the next state has \(2r-(h+1)+u=h\) ones and all universal bits one. The following update returns to the preceding state. The latter kind of two-cycle has one uniquely designated phase with universal bits zero and exactly \((h+1)/2\) occupied pairs. It occurs only when \(h\) is odd, and contributes \(\binom r{(h+1)/2}\) two-cycles, provided the index lies between zero and \(r\).

If instead all universal bits are one, the state has \(2b+u\) ones. At \(S=h\), it is the counterpart of the preceding cross-level cycle. At \(S=h+1\), its successor retains all universal bits one and has \(h+u\) ones. This stays critical exactly when \(u=1\), giving a same-level pair-swapping two-cycle. There are no other periodic states, since any move outside the two critical levels leads to a uniform state at the next update.

For \(u=1\) and even \(r=h\), each of the universal-zero and universal-one same-level families contains \(\binom r{r/2}\) periodic states; every cycle contains two states of the same family. Hence the total number of two-cycles is \(\binom r{r/2}\). For \(u=1\) and odd \(r\), the cross-level family gives \(\binom r{(r+1)/2}=\binom r{\lfloor r/2\rfloor}\) cycles. For odd \(u\ge3\), only the cross-level family remains, giving the stated formula and existence criterion. In all odd cases only the two uniform states are fixed. Finally, every nonuniform initial state either reaches a uniform state immediately or enters a critical-level post-update state. At most one further update can leave the critical levels, and the next update reaches consensus. Thus first periodic entry takes at most three steps, proving \(F^5=F^3\).

## Verification

Two standalone Python implementations are included. `verify_labelled.py` computes every neighborhood majority directly from its labelled graph and exhaustively tests all configurations for \(44\) parameter pairs with \(r\ge1\), \(0\le u\le7\), and \(2r+u\le15\): \(261804\) labelled states altogether. It verifies fixed-point and primitive two-cycle counts and both return-map identities. `verify_profiles.py` independently enumerates weighted pair-type profiles, uses the common-neighborhood formula rather than graph adjacency, and compares exact weighted counts over \(288\) parameter pairs with \(1\le r\le18\), \(0\le u\le15\). Both reproduced their included output files. These finite checks corroborate, but do not replace, the all-size case proof above.

For example, \((r,u)=(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,7)\) have respectively \(27,6,126,4,462,0,1\) primitive two-cycles. This illustrates the nonmonotone odd-\(u\) extinction and reappearance not present in an unqualified eventual-period theorem.

## Relationship to prior work

Goles and Olivos established eventual periods at most two for symmetric threshold systems, including this update as a special case; their published abstract does not supply the present matching-deleted-clique orbit census or one-/three-step bounds. Benjamini, Chan, O'Donnell, Tamuz, and Tan (arXiv:1405.2486v1, Section 1 and Section 3) treat majority evolution on unimodular and random graphs and cite the general finite period-two theorem, but do not derive these exact matching-deletion formulas. Turau (arXiv:2202.01580v1, Sections 1–3) characterizes periodic states for **trees**: this does not cover the dense family here, except at isolated small parameter values. Indexed mathematical descriptions of parity automata on complete multipartite graphs use XOR, not majority, and their orbit formulas cannot be substituted for nonlinear majority dynamics. Prior majority results on crown, prism, and Möbius-ladder graphs concern different graph families. No implication deriving the present formulas from these inspected statements was identified.

## Limitations

The finding applies only to binary synchronous open-neighborhood majority with retained ties on graphs formed by deleting a matching from a complete graph. It does not cover directed or asynchronous updates, weighted edges, or arbitrary missing-edge graphs. It enumerates periodic states and bounds entry times but does not provide a full count by each transient-entry time. Related classical threshold papers were available in abstract rather than complete text, so a historically equivalent specialized calculation cannot be categorically excluded. This is a mathematical proof with corroborating computations, not an independent external validation.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: https://doi.org/10.1016/0012-365X(80)90121-1 .
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (public version dated 2014-05-11). https://arxiv.org/pdf/1405.2486 .
3. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580v1 (2022). https://arxiv.org/pdf/2202.01580 .
