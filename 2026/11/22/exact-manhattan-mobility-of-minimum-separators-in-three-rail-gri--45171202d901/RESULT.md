# Exact Manhattan mobility of minimum separators in three-rail grids

## Finding

Let \(n\ge3\). In the rectangular grid \(G_n=P_3\square P_n\), index vertices by \((r,c)\) with \(r\in\{0,1,2\}\) and \(0\le c<n\); edges join points differing by one in exactly one coordinate. Distinguish the terminal vertices \(s=(1,0)\) and \(t=(1,n-1)\). An \(s\)-\(t\) separator is a subset of \(V(G_n)\setminus\{s,t\}\) whose deletion disconnects these terminals.

Every minimum separator has three vertices, and the full set of minimum separators is exactly
\[
\mathcal S_n=\bigl\{S(i,j,k)=\{(0,i),(1,j),(2,k)\}:1\le j\le n-2,\ |i-j|\le1,\ |k-j|\le1\bigr\}.
\]
Consequently, \(|\mathcal S_n|=9(n-2)\).

Define the *token-slide reconfiguration graph* \(R_n\) on \(\mathcal S_n\) by joining two sets when one is obtained from the other by replacing exactly one selected vertex with an adjacent, previously unselected vertex of \(G_n\). Then \(R_n\) has \(16n-36\) edges, is connected, and is an isometric subgraph of the integer three-dimensional nearest-neighbor grid. Explicitly, for any two feasible triples,
\[
 d_{R_n}(S(i,j,k),S(i',j',k'))=|i-i'|+|j-j'|+|k-k'|.
\]
Writing \(E_n(i,j,k)\) for the eccentricity of this vertex in \(R_n\), the exact formula is
\[
 E_n(i,j,k)=2+\max\bigl\{|i-1|+|j-1|+|k-1|,\ |i-(n-2)|+|j-(n-2)|+|k-(n-2)|\bigr\}.
\]
The sharp radius and diameter are
\[
 \operatorname{rad}(R_n)=2+\left\lceil\frac{3(n-3)}2\right\rceil,\qquad
 \operatorname{diam}(R_n)=3n-5.
\]

## Assumptions and scope

The graph is simple, unweighted, and has open path boundaries, not periodic boundaries. Terminals are fixed at the middle-row endpoints and may never belong to a separator. Only *minimum-cardinality* separators are states, and each move slides one vertex along an original graph edge without permitting temporary non-minimum states. Different selected sets represent different states; there is no quotient by grid symmetries. All assertions hold for **every integer \(n\ge3\)**, including the three-column boundary case.

## Proof

**Step 1 (minimum size).** Three internally vertex-disjoint terminal paths run, respectively, through the upper row, along the internal vertices of the middle row, and through the lower row. Every separator meets each, so has at least three vertices. The three vertices of any internal column form a separator, proving that the minimum size is three. As the three paths are internally disjoint, every minimum separator contains exactly one vertex on each canonical path: an upper-row vertex \((0,i)\), a middle-row vertex \((1,j)\), and a lower-row vertex \((2,k)\), with \(1\le j\le n-2\) and \(0\le i,k\le n-1\).

**Step 2 (precise feasibility).** Suppose \(i\le j-2\). From \(s\), follow the middle row to column \(j-1\), move up, and continue along the upper row to column \(n-1\) and down to \(t\); all these vertices avoid the proposed separator. If \(i\ge j+2\), instead follow the upper row from column zero to column \(j+1\), move to the middle row there and proceed to \(t\). The analogous detours in the lower row show that any separator must have \(|i-j|\le1\) and \(|k-j|\le1\). Conversely, if these inequalities hold, delete the three selected vertices and classify the remaining vertices of each row as left or right of that row's deleted vertex. Horizontal edges do not cross from left to right; vertical edges between neighboring rows also cannot cross because their deleted column indices differ by at most one. Thus no path connects \(s\) on the left with \(t\) on the right. This proves the asserted classification and its \(9(n-2)\) count.

**Step 3 (slide graph).** A legal slide cannot change which canonical path contains its token, since every minimum separator meets each canonical path exactly once. Upper and lower vertices may therefore move only horizontally along their rows, as can the middle vertex; a vertical move leaves one row without a token. In the triple coordinates a slide changes exactly one coordinate by \(1\) or \(-1\) and remains inside the inequalities in Step 2. For fixed \(j\), the nine states form \(P_3\square P_3\), with twelve edges. Between consecutive central columns \(j\) and \(j+1\), an unchanged upper coordinate and lower coordinate must each belong to \(\{j,j+1\}\); hence there are exactly four cross-layer edges. There are \(n-2\) layers and \(n-3\) consecutive-layer interfaces, giving \(12(n-2)+4(n-3)=16n-36\) edges.

**Step 4 (geodesic convexity in the coordinate grid).** Let \(\mathcal T_n\subset\mathbb Z^3\) be the feasible triples from Step 2. Their coordinatewise minimum and maximum stay feasible, because the minimum and maximum operations preserve all inequalities of the form \(|x_a-x_b|\le1\) and the coordinate bounds. For comparable feasible triples \(x\le y\), an increasing coordinate-by-one path from \(x\) to \(y\) always exists. To prove this, whenever a pending coordinate cannot be increased, a tight inequality \(x_a=x_b+1\) must block it. Feasibility of \(y\) forces coordinate \(b\) also to be pending. Following blockers strictly decreases the current integer coordinate values, so a blocking cycle is impossible and at least one pending coordinate can be increased legally. Repeat until reaching \(y\). The reversed argument produces a decreasing path between any comparable pair. For arbitrary \(x,y\in\mathcal T_n\), put \(z=\min(x,y)\) coordinatewise and concatenate the decreasing path \(x\to z\) with the increasing path \(z\to y\). This uses exactly \(\sum_a|x_a-y_a|\) steps. Every slide changes one coordinate by one, so fewer steps are impossible. Connectivity and the stated distance formula follow.

**Step 5 (eccentricity).** Fix \((i,j,k)\in\mathcal T_n\). For a target middle coordinate \(q\) in \(1,\ldots,n-2\), the largest possible Manhattan distance to a feasible target \((u,q,v)\) is
\[
 |j-q|+\max_{u\in\{q-1,q,q+1\}}|i-u|+\max_{v\in\{q-1,q,q+1\}}|k-v|=2+|i-q|+|j-q|+|k-q|.
\]
This expression is convex in the real variable \(q\), so its maximum on the integer interval is attained at \(q=1\) or \(q=n-2\), giving the displayed eccentricity formula.

**Step 6 (radius and diameter).** Denote \(L=|i-1|+|j-1|+|k-1|\) and \(U=|i-(n-2)|+|j-(n-2)|+|k-(n-2)|\). The triangle inequality yields \(L+U\ge3(n-3)\), hence \(E_n(i,j,k)\ge2+\lceil3(n-3)/2\rceil\). For odd \(n=2m+1\), choosing \(i=j=k=m\) attains equality. For even \(n=2m\), choosing \((i,j,k)=(m,m-1,m)\) also attains equality. This proves the radius. For any two triples, \(|i-i'|,|k-k'|\le n-1\), and \(|j-j'|\le n-3\), so the diameter is at most \(3n-5\). Equality holds for \((i,j,k)=(0,1,0)\) and \((i',j',k')=(n-1,n-2,n-1)\), which are both feasible. \(\square\)

## Verification

Two standalone, standard-library Python verifiers accompany this result. Running `python3 grid_sep_exhaustive.py` checks every candidate triple vertex deletion directly against graph connectivity for each \(3\le n\le9\), rejects all two-vertex cuts, constructs actual graph-edge token slides, and compares every shortest-path distance with the closed formula. Running `python3 grid_sep_states.py` separately constructs the feasible integer triples, checks every pairwise reconfiguration distance and all formulas for \(3\le n\le24\). The actual reproducible outputs are included in `verification_output.txt`. The infinite assertion rests on Steps 1–6, not on these finite tests.

## Relationship to prior work

Gomes, Legrand-Duchesne, Mahmoud, Mouawad, Okamoto, dos Santos, and van der Zanden (2023) introduced a general shortest token-slide algorithm for minimum terminal separators; their canonical-path lemma and forward-moving theorem imply that distance is pathwise displacement **whenever a transformation is possible**. The present result credits that general mechanism and makes the additional, explicit three-rail classification, universal connectivity, number of states and edges, exact all-state eccentricity function, and sharp closed radius and diameter. These quantitative specializations are not stated in the inspected general paper. Gomes, Nogueira, and dos Santos (2020) studied broader separator reconfiguration and graph-class algorithms but did not give these concrete three-rail invariants in accessible summaries. Related exact results for other predicates on rectangular grids do not subsume minimum terminal separators. The originality assessment is qualified by the possibility of unindexed equivalent calculations.

## Limitations

The terminals lie specifically at the middle-row endpoints; changing their placement or increasing the number of rows may change the state geometry. The theorem does not assert the shortest token-*jumping* metric, any general grid-width formula, or uniqueness of the result in the entire literature. The proof is self-contained for the stated family; the finite programs only check bounded instances. An independent external mathematical audit has not been performed.

## References

1. G. C. M. Gomes, C. Legrand-Duchesne, R. Mahmoud, A. E. Mouawad, Y. Okamoto, V. F. dos Santos, T. C. van der Zanden, *Minimum Separator Reconfiguration*, arXiv:2307.07782, first public 2023-07-15; IPEC 2023, DOI: 10.4230/LIPIcs.IPEC.2023.9. https://arxiv.org/abs/2307.07782
2. G. C. M. Gomes, S. H. Nogueira, V. F. dos Santos, *Some Results on Vertex Separator Reconfiguration*, arXiv:2004.10873, first public 2020-04-22. https://arxiv.org/abs/2004.10873
3. MSC2020, 68R10, graph theory in computer science. https://mathscinet.ams.org/msc/msc2020.html?btn=Current&t=68R10
