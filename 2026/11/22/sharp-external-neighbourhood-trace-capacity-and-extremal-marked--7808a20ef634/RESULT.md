# Sharp external neighbourhood-trace capacity and extremal marked-edge rigidity in finite line graphs

## Finding

Let \(G\) be any finite simple undirected graph, let \(S\subseteq E(G)\) consist of \(m\ge1\) marked edges, and let \(L(G)\) be the line graph. The **external trace family** is
\[
\mathcal T(G,S)=\{N_{L(G)}(e)\cap S:e\in E(G)\setminus S\}.
\]
Write \(M_m=\max_{G,S:|S|=m}|\mathcal T(G,S)|\). Then
\[
M_1=2,\qquad M_{2k}=1+\binom{3k}{2}\quad(k\ge1),\qquad
M_{2k+1}=2+\binom{3k+1}{2}\quad(k\ge1).
\]
For a marked-edge graph \(F=(V(S),S)\), without isolated vertices, the complete list of underlying structures that **can** attain \(M_m\) is:

- \(m=1\): \(K_2\).
- \(m=2\): \(P_3\), or \(2K_2\).
- \(m=2k\ge4\): \(kP_3\).
- \(m=2k+1\ge3\): \(kP_3\sqcup K_2\), or \((k-1)P_3\sqcup K_{1,3}\).

Here \(P_3\) means a path with two edges. Each listed form does attain \(M_m\) when the ambient graph contains all edges on \(V(S)\) and two additional unmarked vertices. For a smaller ambient graph, attainment requires that every possible distinct external trace actually be represented. In particular, the asymptotic optimum is \(9m^2/8+O(m)\).

## Assumptions and scope

Graphs are finite and simple, with no assumption of connectedness or domination. An edge outside \(S\) is permitted to have no marked-edge neighbour: the empty trace counts once if realized. The result counts distinct external open-neighbourhood profiles only, not the number of vertices having these profiles; marked vertices themselves are not included. The classification is of the graph formed by marked edges, not of the entire ambient graph.

## Proof

**Reduction to a completed ambient graph.** Fix \(S\) and let \(W\) be its endpoint set. It suffices to count possible traces in the complete graph on \(W\) and two extra vertices: it contains all original potential unmarked edges between marked endpoints, has an unmarked edge from each endpoint to an outside vertex, and has an unmarked edge between the two fresh vertices. Thus all possible profiles appear there, and every smaller ambient graph realizes a subfamily.

For each \(v\in W\), set \(\sigma(v)=\{f\in S:v\in f\}\). Every external edge with endpoints \(u,v\) has trace \(\sigma(u)\cup\sigma(v)\), assigning the empty signature to a fresh unmarked vertex. All signatures are nonempty on \(W\). Signatures of distinct marked endpoints coincide **only** when the endpoints form an isolated \(K_2\) component in the marked-edge graph: if two endpoints have the same nonempty incident-edge set, every one of these edges must join the same two endpoints, and simplicity forces that set to be a singleton. Hence, if \(r\) is the number of distinct nonempty signatures and \(\ell\) the number of \(K_2\) components, then \(r=|W|-\ell\).

**Universal counting bound.** There is at most one empty trace, at most \(r\) individual-signature traces, and at most \(\binom r2\) further traces from unordered pairs of distinct signatures. For each marked edge not belonging to a \(K_2\) component, its two endpoint signatures are distinct and unique to that endpoint pair; their pair cannot come from an unmarked edge. Such pairs remove \(m-\ell\) candidates. For each \(P_3\) component, the two leaves form a legitimate unmarked-edge pair, but the union of their two singleton signatures equals the signature at the middle vertex. These additional \(p\) duplicates, where \(p\) is the number of \(P_3\) components, occur in distinct components and are disjoint from the excluded marked-edge pairs. Consequently,
\[
|\mathcal T(G,S)|\le 1+r+\binom r2-(m-\ell)-p.
\tag{1}
\]
No claim that the three broad categories of traces are otherwise disjoint is needed for the upper bound.

**Signature deficit.** A connected component with \(e\) edges has \(v\le e+1\) incident vertices. Its contribution to \(D=3m-2r\) equals \(3e-2(v-\mathbf1_{\{e=1\}})\). For an isolated marked edge \(K_2\), this contribution is \(1\); for a connected component with \(e\ge2\), it is at least \(e-2\), and equals zero precisely for \(P_3\). In particular \(D\ge\ell\ge0\), and \(D=0\) forces every component to be \(P_3\).

**Even case.** If \(m=2k\), then \(r\le3k\). At \(r=3k\), the deficit is zero, so \(F=kP_3\), \(\ell=0\), and \(p=k\). Bound (1) becomes \(1+\binom{3k}{2}\). If \(r\le3k-1\), use \(\ell\le3m-2r\) in (1) and discard \(p\ge0\):
\[
|\mathcal T|\le1+\binom r2-r+2m
\le1+\binom{3k}{2}-(2k-2).
\]
For \(k\ge2\), this is strictly smaller. For \(k=1\), all two-edge marked graphs are either \(P_3\) or \(2K_2\); both attain four traces in the completed ambient graph.

**Odd case.** If \(m=2k+1\) with \(k\ge1\), then \(r\le3k+1\). When \(r\le3k\), the same argument gives
\[
|\mathcal T|\le 3+k+\binom{3k}{2}
=2+\binom{3k+1}{2}-(2k-1),
\]
strictly smaller than the claimed optimum. Thus equality requires \(r=3k+1\), or \(D=1\). The component deficits force either \(k\) copies of \(P_3\) and one \(K_2\), or \(k-1\) copies of \(P_3\) and a three-edge tree. A three-edge tree is either \(K_{1,3}\) or \(P_4\). For \(P_4\) with consecutive marked edges \(ab,bc,cd\), the two distinct permissible endpoint pairs \(\{a,c\}\) and \(\{b,d\}\) produce the same external trace \(\{ab,bc,cd\}\); this is an additional collision not charged in (1). Therefore \(P_4\) is strictly subextremal. Each of the other two structures reaches \(2+\binom{3k+1}{2}\) in the completed ambient graph: all remaining pair unions are distinct except the \(k\) or \(k-1\) middle-vertex identities from the \(P_3\) components already charged in (1). For \(m=1\), the two attainable traces are \(\varnothing\) and the unique marked edge.

## Verification

The accompanying `verify_line_graph_profiles.py` is a standalone Python standard-library program. It exhaustively lists every marked-edge graph using up to seven labelled endpoints and at most seven marked edges, computes the exact saturated trace family, checks the bound and the iff classification for every case, and checks explicit extremizers for twelve sizes of each infinite family. It reports `VERIFY_OK 215896`. Exhaustive finite checks do not replace the proof for arbitrary \(m\); the reduction, deficit bound, and collision classification establish that generality.

## Relationship to prior work

Berthe et al. (2026) study neighbourhood complexity in graph classes constrained by treewidth and pathwidth; that motivates the present unrestricted-line-graph maximum but does not state this line-graph bound or equality classification. Foucaud et al. (2013) study codes identifying **all** graph edges under stronger code hypotheses, leading to a different quadratic edge bound; arbitrary external trace sets in this result need not dominate or identify marked edges. Foucaud and Henning (2016) introduce edge-locating-dominating sets using the same external-trace notion, but their main theorems bound the size of locating-dominating sets, rather than the maximum number of distinct external traces for a prescribed number of marks. The claimed contribution is the exact unrestricted external-type maximum and complete marked-edge extremizers, not the definition of edge-location or general quadratic growth.

## Limitations

The theorem is specific to line graphs of finite simple graphs, open external traces, and unconstrained ambient graph size. It does not assert the same extremum for connected base graphs under other restrictions, closed traces, all-vertex identification, or bounded degree. Historical priority is provisional: broader unindexed material may contain an equivalent extremal statement. No independent mathematical or historical-priority audit has been completed.

## References

1. L. Berthe et al., *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, 2026 preprint, https://arxiv.org/abs/2607.16889 (first public posting 18 July 2026).
2. F. Foucaud, S. Gravier, R. Naserasr, A. Parreau, P. Valicov, *Identifying codes in line graphs*, J. Graph Theory **73** (2013), 425–448; accessible full preprint https://arxiv.org/abs/1107.0207 (initial preprint 2011).
3. F. Foucaud and M. A. Henning, *Location-Domination in Line Graphs*, 2016 preprint https://arxiv.org/abs/1506.02623 (available full version).
