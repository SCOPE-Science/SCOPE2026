# Antiflag mobility and the two-sensor boundary in projective-plane incidence networks

## Finding
Let \(\Pi\) be any finite projective plane of order \(q\ge 2\), and let \(H(\Pi)\) be its point–line incidence graph. Consider power domination with the standard initial closed-neighborhood observation and subsequent unique-unobserved-neighbor propagation.

**Two-sensor boundary.** The graph \(H(\Pi)\) has a power-dominating set with at most two vertices if and only if \(q=2\). In the latter case \(H(\Pi)\) is the Heawood graph and its minimum power-dominating sets are *exactly* the \(28\) nonincident point–line pairs (antiflags). Thus \(\gamma_P(H(\Pi))=2\) when \(q=2\), while \(\gamma_P(H(\Pi))\ge3\) for every existing plane with \(q\ge3\). No assertion about the exact minimum number of sensors at higher orders is made.

**Optimal placement mobility.** For \(q=2\), let \(B\) be the bipartite point–line *nonincidence* graph of the Fano plane. It is \(4\)-regular, with \(14\) vertices and \(28\) edges. If one minimum power-dominating pair can be changed to another by replacing one selected vertex, the resulting token-jump reconfiguration graph is precisely the line graph \(L(B)\). It is connected, \(6\)-regular, has \(28\) vertices, \(84\) edges, radius \(3\), and diameter \(3\). If a replacement is additionally required to traverse an edge of the *original incidence graph*, all \(28\) optimal pairs are isolated.

The unordered shortest-path distance distribution in \(L(B)\) is \(84\) pairs at distance \(1\), \(210\) at distance \(2\), and \(84\) at distance \(3\). Among the distance-two pairs, \(168\) have one geodesic and \(42\) have two; every distance-three pair has exactly four geodesics.

## Assumptions and scope
A finite projective plane of order \(q\) has \(v=q^2+q+1\) points and as many lines, each point lies on \(q+1\) lines, each line contains \(q+1\) points, and every two distinct points (respectively lines) share exactly one line (respectively point). The argument does not assume Desarguesian coordinates or that a plane exists for every integer order.

For \(S\subseteq V(H(\Pi))\), start with observed set \(N[S]\). Repeatedly, any already observed vertex with exactly one unobserved neighbor observes that neighbor. The set \(S\) is power dominating when the process observes every vertex. Token jumping exchanges a selected vertex for any previously unselected vertex, keeping a minimum power-dominating set. Token sliding adds the requirement that these two vertices are adjacent in \(H(\Pi)\). Reconfiguration graphs are simple undirected graphs.

## Proof
**1. Singleton obstruction for every \(q\ge2\).** Starting at one point, the only observed vertices are that point and its \(q+1\) incident lines. Each observed line has \(q\ge2\) unobserved point neighbors, and the selected point has none. Therefore propagation cannot start. The dual argument holds for one selected line.

**2. No pair works for \(q\ge3\).** By duality and exchanging the two selected vertices, there are three cases.

- For two selected points \(P,Q\), every initially observed line meets the selected points in one or two points, so retains at least \(q-1\ge2\) unobserved point neighbors; the two points have none. No propagation begins. The two-line case is dual.
- For a selected point \(P\) incident with a selected line \(\ell\), initially observed lines other than \(\ell\) meet the observed point set only in \(P\), leaving \(q\ge3\) unobserved neighbors. Initially observed points other than \(P\) lie on \(\ell\), and each retains \(q\ge3\) unobserved line neighbors. The selected vertices have no unobserved neighbors. No propagation begins.
- For a selected point \(P\) *not* incident with selected line \(\ell\), each observed line through \(P\) contains exactly two observed points at the outset, namely \(P\) and its unique intersection with \(\ell\); it therefore retains \(q-1\ge2\) unobserved points. Dually, each observed point on \(\ell\) has precisely two observed incident lines (\(\ell\) and the line through \(P\)), leaving \(q-1\ge2\) unobserved lines. Again propagation cannot begin.

The initial observed set is proper in all cases, establishing the claimed impossibility.

**3. Exact classification at \(q=2\).** Two selected points initially observe their five distinct incident lines. Their joining line has one unobserved point, so it can force that point. The four other observed lines still have two unobserved point neighbors apiece; the newly observed point has two unobserved line neighbors, so propagation then stops. Duality excludes two selected lines. An incident point–line pair has no available initial force by the second case above (with \(q=2\), the required unobserved counts are \(2\)).

For a nonincident pair \(\{P,\ell\}\), each of the three lines through \(P\) initially observes exactly two of its three point neighbors: \(P\) and its intersection with \(\ell\). Each forces its third point. Hence all seven points become observed. Each of the three points of \(\ell\) has then already observed two incident lines, \(\ell\) and the line joining it to \(P\), so it forces its third line. Thus every vertex is observed. Exactly \(7(7-3)=28\) antiflags exist. Part 1 excludes smaller power-dominating sets.

**4. Reconfiguration graph and distances.** Identify the optimum pair \(\{P,\ell\}\) with the edge \(P\ell\) of \(B\), where \(P\notin\ell\). Two such pairs differ in exactly one sensor if and only if their edges in \(B\) share an endpoint. Thus the jump graph is \(L(B)\). Each point is nonincident with four of the seven lines and vice versa, giving degree \(2(4-1)=6\) and \(28\cdot6/2=84\) jump edges. Every optimal pair contains one point and one line. Sliding one vertex across an original point–line incidence edge would result in two selected vertices on the same bipartition side, which cannot be optimal; hence all sliding states are isolated.

Fix antiflags \(s=(P,\ell)\) and \(t=(Q,m)\). If a coordinate agrees their jump distance is one (unless \(s=t\)). Suppose both coordinates differ. A length-two path exists exactly when at least one of \(P\notin m\) or \(Q\notin\ell\) holds: the relevant intermediate antiflag is \((P,m)\) or \((Q,\ell)\). If neither holds, then \(P\in m\), \(Q\in\ell\), and both intermediates fail; their distance is at least three. There are two lines avoiding both distinct points \(P,Q\), giving paths \((P,\ell)\to(P,k)\to(Q,k)\to(Q,m)\); dually two points avoiding both lines \(\ell,m\) give two further paths. These exhaust the four geodesics, so the distance is three.

For each fixed \(s\), six optimum pairs share one coordinate and six satisfy the distance-three conditions: choose one of the three lines \(m\) through \(P\), then one of the two points \(Q\) on \(\ell\) other than \(m\cap\ell\). The remaining \(28-1-6-6=15\) states are at distance two. Exactly three of those fifteen have both cross nonincidences and therefore two length-two geodesics; the other twelve have one. Multiplying by \(28/2\) gives all asserted unordered counts. Since every state has distance-three partners and all pairs are within distance three, radius and diameter are both three.

## Verification
The standalone programs `verify_fano.py` and `verify_dual.py` construct the Fano incidence graph independently, respectively by nonzero binary triples with orthogonality incidence and by the cyclic difference set \(\{0,1,3\}\) modulo seven. Both exhaustively classify the two-sensor power-dominating sets and recompute the jump graph, distance distribution and shortest-path counts. The first program also checks that all \(325\) two-vertex subsets fail to power dominate the \(26\)-vertex Desarguesian plane incidence graph at order three, corroborating but not proving the all-order obstruction. Run using `python3 verify_fano.py` and `python3 verify_dual.py` with no third-party packages.

## Relationship to prior work
The power-domination reconfiguration framework introduced by Bjorkman and coauthors provides the replacement operations but does not classify Fano antiflags or the nonincidence-line-graph metric. Brimkov and coauthors' power-domination polynomial study provides a general enumeration framework, not this Fano or higher-order projective-plane result. Closely related graph families and other optimum-set reconfiguration questions do not imply the stated observation-process classification. The Fano antiflags have different feasibility constraints from the **incident** flags occurring in prior connected-domination classifications of projective-plane incidence networks.

## Limitations
For orders at least three only the strict lower bound of three sensors is proved, not an exact power-domination number or a description of higher-budget solution spaces. The Fano shortest-path assertions concern unrestricted replacements among minimum solutions, not time-optimal propagation or multi-sensor simultaneous moves. Literature searches and relevant primary texts were reviewed, but unindexed historical equivalence or results under different terminology remain a priority risk. There is no independent mathematical audit.

## References
1. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob, C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798, first posted 2022-01-05; open full text at https://link.springer.com/article/10.1007/s44007-025-00187-5.
2. B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984, first posted 2018-05-28; full manuscript text at https://www.academia.edu/66666280/Power_domination_polynomials_of_graphs.
3. Standard finite projective-plane incidence definitions and Fano/Heawood identification: https://mathworld.wolfram.com/HeawoodGraph.html and https://en.wikipedia.org/wiki/Fano_plane.
