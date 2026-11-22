# Minimum semidefinite forcing on path powers: a connected clique–path exchange graph

## Finding

**Theorem.** Fix integers \(k\ge2\) and \(n\ge k+2\). Let \(H=P_n^k\) be the \(k\)-th ordinary graph power of the path with ordered vertices \(1,\ldots,n\). Then the positive-semidefinite zero-forcing number is \(Z_+(H)=k\). Every minimum PSD zero-forcing set belongs to precisely one of the following three families:

\[
\begin{aligned}
L_i&=\{1\}\cup\bigl(\{2,\ldots,k+1\}\setminus\{i\}\bigr),&&2\le i\le k+1,\\
R_j&=\{n\}\cup\bigl(\{n-k,\ldots,n-1\}\setminus\{j\}\bigr),&&n-k\le j\le n-1,\\
C_a&=\{a,a+1,\ldots,a+k-1\},&&2\le a\le n-k.
\end{aligned}
\]

In particular, there are exactly \(n+k-1\) minimum sets. Let \(\mathcal R_+(H)\) have these minimum sets as vertices, with two sets adjacent if their symmetric difference has size two. Then \(\mathcal R_+(H)\) is connected, with

\[
\operatorname{diam}\mathcal R_+(H)=n-k,
\]

and

\[
|E(\mathcal R_+(H))|=
\begin{cases}
k^2+2k,&n=k+2,\\
k^2+n+1,&n=k+3,\\
k^2+n,&n\ge k+4.
\end{cases}
\]

For comparison, ordinary zero forcing on the same graph has exactly the \(2k\) minimum sets \(L_i,R_j\). Their one-exchange graph is disconnected for \(n\ge k+4\); thus the PSD rule replaces two separated ordinary-minimum families with a connected chain of interior configurations.

## Assumptions and scope

Graphs are finite, simple, undirected, and unweighted. The path power has edge \(uv\) exactly when \(1\le |u-v|\le k\). In ordinary zero forcing a blue vertex forces its unique white neighbor. Under the PSD rule, if the current white induced graph has components \(W_1,\ldots,W_t\), a blue vertex may force a vertex \(w\in W_h\) when \(w\) is its unique neighbor **within that component**, even if it has neighbors in other white components. A PSD forcing set eventually colors the entire graph blue. Minimum means minimum cardinality; the reconfiguration adjacency is exchange of one blue vertex, *not* token sliding along an original edge. Only \(k\ge2\), \(n\ge k+2\) are claimed.

## Proof

**1. Connectivity and the lower bound.** Every set of fewer than \(k\) deleted vertices leaves \(H\) connected: list the remaining vertices in increasing path order; any two consecutive survivors are separated by at most \(k-1\) deleted positions and hence adjacent in \(H\). The minimum vertex degree in \(H\) equals \(k\), achieved only by the two endpoints. If fewer than \(k\) vertices are blue, all whites form a single component, and every blue vertex has at least \(k-(k-2)=2\) white neighbors. No PSD force can start. Hence \(Z_+(H)\ge k\).

**2. Complete classification at size \(k\).** Let \(S\) be a \(k\)-set. If \(H-S\) is disconnected, consider two successive white vertices in path order belonging to different white components. Their path-index difference is at least \(k+1\), so at least \(k\) indices strictly between them must belong to \(S\). As \(|S|=k\), these are exactly \(k\) consecutive internal positions. Thus \(S=C_a\) for a unique \(2\le a\le n-k\). Conversely any such \(C_a\) disconnects the white graph into a left and a right interval.

If \(H-S\) is connected, a first PSD force is an ordinary force. The forcing blue vertex has at least \(k-1\) blue neighbors, so its degree is at most \(k\). Only endpoints have degree \(k\). If the forcing vertex is \(1\), the seed must be \(L_i\) for a unique index \(i\); if it is \(n\), the seed must be \(R_j\). This proves necessity.

Each \(L_i\) succeeds: vertex \(1\) forces its unique initially white neighbor \(i\), leaving the first \(k+1\) vertices blue. Thereafter vertex \(s\) forces \(s+k\) in order for \(s=2,3,\ldots,n-k\); the reversed argument works for every \(R_j\). Each \(C_a\) also succeeds under the PSD rule: its left and right white intervals are distinct components. The blue vertex \(a+k-1\) has precisely one neighbor \(a-1\) in the left component, which it forces; similarly vertex \(a\) forces \(a+k\) in the right component. Repeating the outward process with the newly extended blue interval forces the left and right components completely. Consequently \(Z_+(H)=k\), and the three families are exhaustive.

The families are disjoint: every \(L_i\) includes \(1\) and excludes \(n\), every \(R_j\) includes \(n\) and excludes \(1\), while each \(C_a\) includes neither endpoint. Their cardinalities are \(k,k,n-k-1\), respectively, giving \(n+k-1\).

**3. Complete exchange adjacency.** Two distinct \(k\)-sets are exchange-adjacent exactly when they intersect in \(k-1\) vertices. All \(L_i\) form a clique \(K_k\), as do all \(R_j\). The internal \(C_a\) form the path \(C_2-C_3-\cdots-C_{n-k}\). Every \(L_i\) is adjacent to \(C_2\). When \(n\ge k+3\), exactly \(L_2\) is additionally adjacent to \(C_3\). Dually every \(R_j\) is adjacent to \(C_{n-k}\), and when \(n\ge k+3\), exactly \(R_{n-1}\) is additionally adjacent to \(C_{n-k-1}\). No other endpoint-to-interior exchanges exist, by comparing the interval overlaps.

There are cross-edges between the \(L\) and \(R\) cliques only when \(n\le k+3\): for \(n=k+2\) these cross-edges form a matching of \(k\) pairs \(L_iR_i\); for \(n=k+3\) there is exactly the edge \(L_2R_{n-1}\); and for \(n\ge k+4\) there are none. These assertions follow by intersecting the ranges \([1,k+1]\) and \([n-k,n]\): the two selected sets can share \(k-1\) vertices only in the listed cases. This is the complete adjacency description.

All families connect to the interior path, so the exchange graph is connected. Counting its edges gives the claimed three cases: two \(K_k\)'s contribute \(k(k-1)\) edges, the internal path contributes \(n-k-2\), the two terminal attachments contribute \(2k\), the two extra near-terminal edges contribute two when present, and the cross-edges contribute \(k\), one, or zero according to the three regimes.

**4. Exact diameter.** If \(n=k+2\), the single interior node is adjacent to both endpoint cliques, giving diameter two. If \(n=k+3\), the interior path has two nodes and every pair is at distance at most three; vertices \(L_i\) with \(i\ne2\) and \(R_j\) with \(j\ne n-1\) are at distance exactly three. For \(n\ge k+4\), every left-clique vertex reaches any right-clique vertex along the interior path in at most \(n-k\) steps, and all other pairs have no larger distance. For the reverse inequality, define an integer-valued function on the reconfiguration vertices by giving the \(L\)-vertices values zero except \(L_2\) value one, giving \(C_a\) value \(a-1\), and giving the \(R\)-vertices value \(n-k\) except \(R_{n-1}\) value \(n-k-1\). Every reconfiguration edge changes this value by at most one. Any \(L_i\), \(i\ne2\), and \(R_j\), \(j\ne n-1\), therefore have distance at least \(n-k\), proving equality.

**5. Ordinary comparison.** With a \(k\)-vertex initial blue set the ordinary rule needs an initial force, and a blue forcing vertex must have degree at most \(k\). This forces an endpoint vertex and precisely the corresponding \(L_i\) or \(R_j\) configuration. Both families succeed by step 2. For \(n\ge k+4\) there are no exchange edges between the two endpoint cliques, so the ordinary minimum reconfiguration graph is disconnected. This comparison is included for contrast; ordinary optimal path-power seed classifications are already known.

## Verification

The standalone `verify_psd_path_powers.py` performs independent complete subset enumeration for every \(4\le n\le14\) and \(2\le k\le\min(n-2,6)\). It constructs the graph from distances, iterates the PSD white-component forcing rule, checks the asserted exact set family, tests the lower bound by enumerating all seeds of size \(k-1\), independently tests ordinary forcing, constructs the token-jumping graph directly, and checks connectivity, edge count, and diameter by breadth-first search. It examines 45 parameter pairs and prints `VERIFY_OK`. These finite tests corroborate, but do not replace, the unrestricted proof above.

## Relationship to prior work

Abiad, Flagg, Ghasemi Nezhad and Zeijlemaker (2026) establish ordinary zero-forcing values for graph powers, including \(Z(P_n^k)=k\), and PSD monotonicity under increasing the power; their relevant statements do not enumerate minimum PSD initial sets or determine their exchange graph. Fallat, Meagher and Yang (2015) give an algorithm for optimal PSD forcing on chordal graphs, including the path powers as a subclass, but not the present two-parameter complete minimum-set census or the optimal-set exchange geometry. Published enumerations of ordinary minimum forcing seeds on powers of paths and their exchange graphs address the stronger ordinary forcing rule: the ordinary minimum sets are precisely the endpoint configurations, while the PSD rule also admits internal separators. Thus the PSD count, extra configurations, edge counts and diameter are not implications of the identified ordinary results.

## Limitations

The graph-power radius is restricted to \(2\le k\le n-2\). For \(k=1\), all singletons are minimum PSD seeds and their one-exchange graph is complete; for \(k\ge n-1\), the path power is complete and this theorem's family formula does not apply. The result concerns minimum-cardinality initial sets only, not all PSD forcing sets, throttling, propagation time, or positive semidefinite matrix realizations. Literature comparison was bounded: inaccessible or unindexed earlier work may affect historical priority. No independent mathematical audit has been performed.

## References

1. A. Abiad, M. Flagg, S. Ghasemi Nezhad and S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892 (first public version 2026-10-02), https://arxiv.org/abs/2610.03892 .
2. S. Fallat, K. Meagher and B. Yang, *On the Complexity of the Positive Semidefinite Zero Forcing Number*, arXiv:1407.7017 (2014), https://arxiv.org/abs/1407.7017 .
3. N. H. Bong, J. Carlson, B. Curtis, R. Haas and L. Hogben, *Isomorphisms and properties of TAR reconfiguration graphs for zero forcing and other X-set parameters*, arXiv:2205.09668 (2022), https://arxiv.org/abs/2205.09668 .
4. *Exact optimal zero-forcing seed classifications for powers of paths and cycles* (2026), published mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-optimal-zero-forcing-seed-classifications-for-powers-of-pa--816bf7a10356 .
5. *A connectivity dichotomy for minimum zero forcing on powers of paths and cycles* (2026), published mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-connectivity-dichotomy-for-minimum-zero-forcing-on-powers-of-p--8f1eaf3a981b .
