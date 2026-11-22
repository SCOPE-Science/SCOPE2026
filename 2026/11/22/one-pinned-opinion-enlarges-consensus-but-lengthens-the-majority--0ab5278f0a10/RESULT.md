# One pinned opinion enlarges consensus but lengthens the majority clock on the four-cube

## Finding

For synchronous binary neighbor-majority dynamics with incumbent tie retention on the sixteen-vertex Boolean four-cube, permanently pin the vertex labelled zero to opinion one. On the resulting \(2^{15}=32{,}768\) initial configurations, the exact finite transition graph contains **425 fixed configurations** and **301 primitive temporal two-cycle orbits**, and no other periodic orbits. Its sharp first-periodic-entry time is **six** updates:

\[
P^8=P^6,\qquad P^7\ne P^5.
\]

Exactly 24 configurations first reach a periodic state at update six. The all-one equilibrium attracts precisely **9,383** initial configurations; the polarized equilibrium where only the pinned vertex is one attracts **3,696**. Among the same 32,768 initial configurations, ordinary unpinned majority reaches all-one from exactly **8,229** states, whereas pinning reaches it from **9,383**: **1,154** gain eventual unanimity and **none** loses it. Thus the single fixed positive opinion strictly enlarges the all-one basin while increasing the sharp periodic-entry time from four to six.

The full first-entry-time \(T\) and eventual primitive-period \(p\) census is:

| \(T\) | \(p=1\) | \(p=2\) |
| ---: | ---: | ---: |
| 0 | 425 | 602 |
| 1 | 5,490 | 3,187 |
| 2 | 12,713 | 3,562 |
| 3 | 5,171 | 172 |
| 4 | 1,224 | 0 |
| 5 | 198 | 0 |
| 6 | 24 | 0 |

These fourteen table cells sum to \(32{,}768\); the table has eleven nonzero cells. The only periodic state attainable at time six is fixed, and every eventual two-cycle is entered by time three.

## Assumptions and scope

The vertex set of \(Q_4\) is \(V=\{0,1,\ldots,15\}\), where labels are four-bit strings. The neighbor set of \(v\) is \(\{v\oplus 1,v\oplus2,v\oplus4,v\oplus8\}\), with bitwise XOR \(\oplus\). Each configuration is a word \(x\in\{0,1\}^{16}\); write \(c_v(x)=\sum_{u\sim v}x_u\). Ordinary majority \(F\) is defined at each vertex by

\[
(Fx)_v=\begin{cases}1,&c_v(x)\ge3,\\0,&c_v(x)\le1,\\x_v,&c_v(x)=2.\end{cases}
\]

For the pinned map \(P\), set \((Px)_0=1\) regardless of neighboring opinions and apply the displayed ordinary rule at all other vertices. Its invariant configuration space is \(\Omega=\{x:x_0=1\}\). Every result about \(P\) below concerns the labelled space \(\Omega\), not all sixteen-bit initial words. For a given map, its first periodic-entry time \(T(x)\) is the least \(t\ge0\) for which \(F^t(x)\) or \(P^t(x)\), respectively, is periodic; the eventual primitive period is the least positive period of this periodic orbit. Basins count complete starting words, rather than just recurrent words. The ordinary comparison uses exactly the same initial subset \(\Omega\).

## Proof

**Exact transition reduction and exhaustive certificate.** Represent a full configuration by the integer \(s=\sum_{v=0}^{15}2^vx_v\), which runs over all integers from zero to \(65{,}535\). The pinned space consists exactly of the odd integers; identify it with the integers \(i=(s-1)/2\) from zero through \(32{,}767\). Each of the two accompanying standalone programs computes the successor of every state from the explicit neighbor relation and three-case rule above, using integer arithmetic only. The `check_a.cpp` program builds a complete functional digraph, removes noncyclic vertices by indegree pruning, identifies the remaining disjoint directed cycles, and propagates first-entry depths and attracting-cycle IDs backward through the removed vertices. The distinct `check_b.py` program constructs the bits and neighborhood sums separately and finds cycles and entrance depths by successor-path tracing with a first-visit dictionary instead of indegree pruning. Both programs independently enumerate all 32,768 pinned states *and* all 65,536 ordinary states, and they agree on each displayed period, first-entry count, basin size and matched-initial-state comparison. Their complete source code is included. An exact finite enumeration of all possible labelled configurations is a proof of these finite counts; no random sampling or extrapolation is used.

In particular, there are 425 recurrent singletons and 301 recurrent two-cycles, and every state enters one of these by step six. This verifies \(P^8=P^6\) on the entire finite domain. The witness full-word path is

\[
35537\longrightarrow35025\longrightarrow32977\longrightarrow209
\longrightarrow81\longrightarrow17\longrightarrow1\longrightarrow1.
\]

Only the final word is periodic, so its first periodic-entry time is six. Hence \(P^7\ne P^5\), establishing sharpness. The programs count 24 words at this maximum depth.

**Consensus gain and zero loss.** The strict-majority-with-tie-retention function is monotone in each neighbor bit and in its own bit. Therefore \(F\) is coordinatewise order preserving. Moreover \(Px\ge Fx\) for all \(x\in\Omega\), because pinning forces one coordinate to one without altering the other local rules. By induction, for every \(x\in\Omega\) and every \(t\ge0\),

\[
P^t(x)\ge F^t(x)
\]

coordinatewise: if \(P^t(x)\ge F^t(x)\), monotonicity gives \(F(P^t(x))\ge F(F^t(x))\), and pinning can only raise the left-hand successor. Thus any ordinary trajectory from \(\Omega\) that reaches the all-one word must also reach it under pinning no later than the same update. The finite exact basin comparison counts 8,229 ordinary all-one trajectories and 9,383 pinned all-one trajectories, establishing precisely 1,154 **gains** and zero **losses**. The clamped all-one basin and the single-positive equilibrium basin are counted as 9,383 and 3,696 by the same full functional-graph decomposition.

**No unstated extension.** The proof establishes an exact result for this sixteen-vertex graph and one fixed positive vertex. Vertex transitivity makes all choices of the pinned vertex conjugate. Global bit complementation gives the corresponding statement for a permanently fixed zero vertex and the opposite consensus. Neither equivalence implies analogous numerical results for higher-dimensional hypercubes, different thresholds, or stochastic/asynchronous updates.

## Verification

With a C++17 compiler and Python 3, in the directory containing the embedded files run:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic check_a.cpp -o check_a
./check_a > check_a_output.txt
python3 check_b.py > check_b_output.txt
```

The outputs `check_a_output.txt` and `check_b_output.txt` included with the record were obtained by these commands. Both checkers assert the critical totals, all period/entry populations, extremal witnesses, pinned basins and ordinary comparison. For reproducibility the displayed table is also supplied as `census.csv`. There are exactly \(2^{15}\) pinned and \(2^{16}\) unpinned configurations. The checked assertions cover the full transition graph, not only an attractor sample or witness trajectory.

## Relationship to prior work

The classical Goles–Olivos period-two theorem and the general voting-time framework of Kaaser, Mallmann-Trenn and Natale concern periods or voting-time bounds for symmetric deterministic threshold processes; their stated general results do not supply the exact 425/301 orbit split, eleven nonzero first-entry cells, individual basins, or the 1,154-state pinned-versus-ordinary comparison. A published exact four-cube census for **ordinary unpinned majority** gives 702 fixed configurations, 885 primitive two-cycles and a four-update sharp settling bound. That ordinary result is the credited baseline and is not claimed as new. In contrast the present map has a permanently imposed value at a single site, a different restricted state space, and exact paired-input attraction counts. Work on stochastic or asynchronous stubborn voters is not equivalent to this deterministic synchronous finite map.

## Limitations

This is an exact finite enumeration for the labelled four-cube with one fixed site, not an all-dimensional theorem or a causal claim about social networks. The monotonicity-based non-loss argument is general for this local rule, but the 1,154 gain, 425/301 count and six-step cutoff are graph-specific computational facts. The two checkers have separate transition and graph algorithms but were prepared in the same research context and are not independent external validation. Unindexed historical calculations could contain equivalent numerical populations. The self-review has been completed; no independent external audit is asserted.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
2. D. Kaaser, F. Mallmann-Trenn, and E. Natale, *On the Voting Time of the Deterministic Majority Process*, initial public arXiv version 2015-08-14, arXiv:1508.03519, DOI: 10.4230/LIPIcs.MFCS.2016.55. https://arxiv.org/abs/1508.03519
3. *Thirty geometric recurrent classes and a sharp four-step clock for majority dynamics on the four-cube*, public exact ordinary-map census. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-thirty-geometric-recurrent-classes-and-a-sharp-four-step-clock-f--c8cd34678da7
4. A. Mukhopadhyay, R. Mazumdar, and R. Roy, *Voter and Majority Dynamics with Biased and Stubborn Agents*, Journal of Statistical Physics (2020), DOI: 10.1007/s10955-020-02625-w. https://link.springer.com/article/10.1007/s10955-020-02625-w
