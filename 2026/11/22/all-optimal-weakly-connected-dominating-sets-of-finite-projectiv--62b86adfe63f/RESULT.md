# All optimal weakly connected dominating sets of finite projective-plane incidence graphs

## Finding
Let \(\Pi\) be **any** finite projective plane of order \(q\geq 2\), with point set \(\mathcal P\), line set \(\mathcal L\), and point--line incidence graph \(H_\Pi\). A weakly connected dominating set \(D\) is a vertex set for which the spanning subgraph formed by retaining precisely the edges with an endpoint in \(D\) is connected. Write \(N=q^2+q+1\).

**Theorem.** The weakly connected domination number is
\[
\gamma_w(H_\Pi)=2q+1.
\]
There are precisely two dual types of minimum sets. In the **line-pencil type**, choose a point \(c\), choose a line \(h\) through \(c\), select the other \(q\) lines of the pencil through \(c\), select the \(q\) points of \(h\setminus\{c\}\), and select **one further point** from the union of the \(q\) selected lines. The **point-pencil type** interchanges points and lines in the preceding prescription. Every minimum set occurs in exactly one of these two types and has a unique description within its type.

Consequently, the number of labelled minimum sets is
\[
2(q^2+q+1)(q+1)(q^2+1).
\]
Of these, exactly \(2N(q+1)\) select \(q\) mutually incident point--line pairs and have a **spanning-tree** weak-star subgraph; the remaining \(2N(q+1)q^2\) select exactly one incident point--line pair, and their weak-star subgraphs have cyclomatic number \(q-1\). The claim is conditional only on the existence of the finite plane; no coordinatization or Desarguesian assumption is used.

## Assumptions and scope
A finite projective plane of order \(q\) has \(N=q^2+q+1\) points and \(N\) lines; every point is incident with \(q+1\) lines, every line contains \(q+1\) points, any two points determine a unique line and any two lines meet at a unique point. The simple bipartite graph \(H_\Pi\) has \(2N\) vertices and is \((q+1)\)-regular. A *weak-star graph* of \(D\), denoted \(F_D\), has all \(2N\) vertices and edge set \(\{uv\in E(H_\Pi):u\in D\text{ or }v\in D\}\). A set is weakly connected dominating if and only if \(F_D\) is connected. The *selected-incidence count* \(e_D\) is the number of incidence edges with both endpoints in \(D\). An optimum is a set of minimum cardinality, rather than merely an inclusion-minimal set.

## Proof
**1. Sharp universal lower bound.** For \(s=|D|\), every edge of \(F_D\) is counted at least once among the \((q+1)s\) incidences of selected vertices, so \(|E(F_D)|\le(q+1)s\). Connectedness of a graph on \(2N\) vertices requires at least \(2N-1=2q^2+2q+1\) edges. With \(s\le2q\), the upper bound is at most \(2q(q+1)=2q^2+2q\), a contradiction. Hence \(s\ge2q+1\). Moreover, for an optimum-size candidate we have \(|E(F_D)|=(q+1)(2q+1)-e_D\), so connectedness implies \(e_D\le q\).

**2. A geometric connectivity criterion.** Suppose \(D\) selects at least one point and at least one line. Let \(P_D\) and \(L_D\) be its selected points and lines. If every unselected line contains a selected point, every unselected point lies on a selected line, and some selected point is incident with some selected line, then \(F_D\) is connected. Indeed, any two selected points are joined by a two-edge path through their common line (both edges survive); any two selected lines are similarly joined through their intersection point; the selected incidence edge joins these two connected cores. The domination conditions attach every other vertex. Conversely, all three conditions are necessary: an unselected vertex lacking a selected neighbor is isolated in \(F_D\); if no selected point meets a selected line, an edge of \(F_D\) cannot connect the point-selected component to the line-selected component (any such path would require an edge joining two unselected vertices). This criterion uses only projective-plane axioms.

**3. Shore balance.** Let \(s=2q+1\), \(a=|P_D|\), \(b=|L_D|\), so \(a+b=2q+1\). Neither \(a\) nor \(b\) can vanish: with no selected points, every unselected line is isolated and \(b<N\) (and dually). For \(a\ge1\), the \(a\) points meet at most \(1+aq\) lines: the first point meets \(q+1\) lines, and each additional point shares at least one of these, contributing at most \(q\) new lines. Therefore, domination of every unselected line requires
\[
b\ge N-(1+aq)=q(q+1-a).
\]
If \(q\ge3\) and \(1\le a\le q-1\), substituting \(b=2q+1-a\) gives the impossible inequality
\[
0\ge q(q+1-a)-(2q+1-a)\ge q-2>0.
\]
When \(q=2\), the only remaining possibility \(a=1\), \(b=4\) meets the inequality with equality: all four lines **not** incident with the unique selected point must be selected, so \(e_D=0\), contradicting the connectivity criterion. Thus \(a\ge q\) for all \(q\ge2\), and by duality \(b\ge q\). Hence the only possible shore sizes are \((a,b)=(q+1,q)\) or \((q,q+1)\).

**4. Concurrency is forced.** Consider \(a=q+1\) selected points and \(b=q\) selected lines. Because \(e_D\ge1\), at least one selected point lies on a selected line. Thus at most \(q\) selected points are **uncovered** by the selected lines. Every point not selected must be on a selected line, so the union of the \(q\) selected lines has size at least \(N-q=q^2+1\). But the union of \(q\) distinct projective lines has at most \((q+1)+(q-1)q=q^2+1\) points: after the first line, each new line meets the earlier union at least once. Equality forces all \(q\) lines to be concurrent: the first two meet at \(c\); every third and later line must meet their union in exactly one point, forcing it through \(c\). The case \(q=2\) is automatic.

Let \(h\) be the unique omitted line of this \(q\)-line pencil through \(c\). The points not covered by the selected lines are exactly the \(q\) points of \(h\setminus\{c\}\). Thus all these \(q\) points must be selected. One additional selected point \(x\) must lie in the pencil union (else there would be no selected incidence). There are exactly \(q^2+1\) choices for \(x\): the center \(c\) or one of the \(q^2\) off-center points of the selected lines.

**5. Sufficiency and enumeration.** Conversely, every set so constructed covers every unselected point (the only uncovered points are the chosen \(q\) points of \(h\setminus\{c\}\)). Every unselected line either equals \(h\), in which case it contains all \(q\) chosen off-center points of \(h\), or is another line not through \(c\), in which case its intersection with \(h\) is one of those chosen points. The selected point \(x\) is incident with a selected line. The connectivity criterion therefore applies. This proves existence and exhaustiveness for \((a,b)=(q+1,q)\); the other case is its dual. A pencil of \(q\ge2\) distinct lines determines its center and omitted line uniquely, so each type contributes \(N(q+1)(q^2+1)\) distinct sets. The two types have different shore sizes, hence are disjoint.

**6. Spanning-tree dichotomy.** If \(x=c\), all \(q\) selected lines meet the selected points at \(c\), so \(e_D=q\). There is one such \(x\) per center--omitted-line choice per dual type. If \(x\ne c\), then \(x\) belongs to exactly one selected line and \(e_D=1\). A connected graph with \(2N\) vertices and \((q+1)(2q+1)-e_D\) edges has cyclomatic number \((q+1)(2q+1)-e_D-(2N-1)=q-e_D\). Therefore \(x=c\) yields a spanning tree, while every off-center \(x\) yields cyclomatic number \(q-1\). This also proves the two stated refined counts.

## Verification
The proof above is valid for every finite projective plane, including non-Desarguesian examples. To test the finite boundary and enumerate the first two orders, two independently written standalone programs are included: `verify_plane_census.py` uses homogeneous coordinates, normalized vector incidence, and breadth-first traversal of retained edges; `verify_plane_census.cpp` uses affine points plus directions at infinity, explicit incidence pairs, and disjoint-set union. Both enumerate every candidate set of size \(2q+1\) on \(\operatorname{PG}(2,q)\) for \(q=2,3\), with the C++ program additionally exhausting all smaller cardinalities for both orders. The Python program constructs the two predicted geometric families and checks exact equality with the brute-force family.

| Plane order | Minimum size | All minimum sets | Selected-incidence count \(1\) | Selected-incidence count \(q\) |
|---|---:|---:|---:|---:|
| \(q=2\) | \(5\) | \(210\) | \(168\) | \(42\) |
| \(q=3\) | \(7\) | \(1040\) | \(936\) | \(104\) |

Compile with `c++ -std=c++17 -O2 verify_plane_census.cpp -o verify_plane_census` and run `./verify_plane_census`; run `python3 verify_plane_census.py`. Both rely only on the respective standard libraries. The embedded `COUNTS.txt` records the successful runs. These finite computations corroborate, but are not substituted for, the all-order proof.

## Relationship to prior work
Weakly connected domination, where selected closed stars remain connected after edges between unselected vertices are deleted, is an established notion in domination theory. Dunbar, Grossman, Hattingh, Hedetniemi and McRae (1997) discuss its basic parameters, complexity and general inequalities, including on bipartite graphs. Duckworth and Mans (2009) study random regular graphs and algorithms for the same parameter. Grossman (1997) studies strongly acyclic weak-star subgraphs, termed spanning star trees, which conceptually overlap the distinguished \(e_D=q\) subfamily. Samodivkin's arXiv preprint first posted on **2013-10-06** gives surface-dependent bounds for weakly connected domination, but not this incidence-geometry census. The present theorem instead exactly classifies every minimum weakly connected dominating set of any finite projective-plane incidence graph, distinguishes cyclic and acyclic retained subgraphs, and counts both types. The generic bounds alone do not determine these optimizer families. A possible uninspected Grossman full text is explicitly recorded as a residual priority risk.

## Limitations
The classification applies only to incidence graphs of finite projective planes, not arbitrary symmetric incidence structures or partial planes. The proof does not assert that planes of every positive order exist. It classifies minimum-cardinality sets, not all inclusion-minimal or all dominating sets. Independent scholarly priority review has not been performed. Some historical full texts were not accessible, and absence of a matching search result does not prove publication novelty.

## References
1. J. E. Dunbar, J. W. Grossman, J. H. Hattingh, S. T. Hedetniemi and A. A. McRae, *On weakly connected domination in graphs*, Discrete Mathematics 167/168 (1997), 261–269. Available text: https://www.academia.edu/106952987/On_weakly_connected_domination_in_graphs
2. W. Duckworth and B. Mans, *Connected domination of regular graphs*, Discrete Mathematics 309 (2009), 2305–2322, DOI: https://doi.org/10.1016/j.disc.2008.05.029 . Accessible full-text transcription: https://www.academia.edu/15659457/Connected_domination_of_regular_graphs
3. J. W. Grossman, *Spanning Star Trees in Regular Graphs*, Graphs and Combinatorics 13 (1997), 353–358, DOI: https://doi.org/10.1007/BF03353013 . Accessible preprint text: https://www.researchgate.net/publication/2687955_Spanning_Star_Trees_In_Regular_Graphs
4. J. W. Grossman, *Dominating sets whose closed stars form spanning trees*, Discrete Mathematics 169 (1997), 83–94, DOI: https://doi.org/10.1016/0012-365X(95)00334-S . Abstract inspected; full text not available in this review.
5. V. Samodivkin, *Upper bounds for domination related parameters in graphs on surfaces*, arXiv:1310.1610 (first posted 2013-10-06), https://arxiv.org/abs/1310.1610 .
