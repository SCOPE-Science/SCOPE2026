# A boundary-defect census of minimum isolating sets on uniform loose hyperpaths

## Finding
For integers \(r\ge3\) and \(m\ge1\), let \(P_m^{(r)}\) be the labelled \(r\)-uniform loose hyperpath with hyperedges \(E_1,\ldots,E_m\) in their natural order. Adjacent hyperedges intersect at one distinct junction vertex; nonadjacent hyperedges are disjoint. Write \(M_{m,r}\) for the number of minimum *isolating vertex sets*, where a set is isolating when its closed neighborhood intersects every hyperedge.

Put \(q=\lceil m/4\rceil\), \(t=4q-m\in\{0,1,2,3\}\), and \(a=r-1\). Then \(\iota(P_m^{(r)})=q\) and
\[
M_{m,r}=\begin{cases}
1,&t=0,\\
1+qa,&t=1,\\
1+2qa+\binom{q}{2}a^2,&t=2,\\
1+(3q-2)a+3\binom{q}{2}a^2+\binom{q}{3}a^3,&t=3.
\end{cases}
\]
These count actual labelled vertex subsets, without identifying automorphic or reversal-equivalent sets. For example, for \(r=3\), the counts at \(m=1,\ldots,12\) are \(3,5,3,1,21,13,5,1,59,25,7,1\). The unique optimum at length \(4q\) consists of junctions between hyperedges \(E_{4j+2}\) and \(E_{4j+3}\), \(0\le j<q\).

## Assumptions and scope
Every hyperedge has exactly \(r\) distinct vertices. For \(m\ge2\), there is one junction vertex between each consecutive pair, no junction vertex is reused, and all other vertices belong to one hyperedge. For \(m=1\), the hypergraph consists of one \(r\)-vertex hyperedge. The hypergraph closed neighborhood \(N[S]\) consists of \(S\) and all vertices sharing a hyperedge with a member of \(S\). The isolation condition is \(E_i\cap N[S]\ne\varnothing\) for every \(i\in\{1,\ldots,m\}\). This is ordinary edge isolation, equivalent to \(K_r^{(r)}\)-isolation in an \(r\)-uniform hypergraph.

## Proof
**1. Interval representation and the optimum.** Index the hyperedges by \(1,\ldots,m\). Each private vertex in \(E_i\) has closed neighborhood equal to \(E_i\), so it isolates exactly the indexed edges in \([i-1,i+1]\cap[1,m]\). Each junction vertex \(E_j\cap E_{j+1}\) has closed neighborhood \(E_j\cup E_{j+1}\), so it isolates exactly \([j-1,j+2]\cap[1,m]\). Thus any chosen vertex isolates at most four hyperedges and \(\iota\ge\lceil m/4\rceil=q\). Conversely the junctions indexed \(2,6,10,\ldots\), with the last selected junction shifted at most two positions to the left when needed, give a cover by at most \(q\) vertices for \(m\ge2\). For \(m=1\), any vertex isolates the edge. Thus \(\iota=q\).

**2. Defect variables are unique.** For a minimum isolating set \(S\) of size \(q\), map every selected vertex to its *unclipped* integer interval: a private vertex in \(E_i\) gives \([i-1,i+1]\) (width three), and a junction vertex \(E_j\cap E_{j+1}\) gives \([j-1,j+2]\) (width four). A minimum isolating set is inclusion-minimal, so no two selected intervals contain one another. Sorting them by their left endpoints, their right endpoints are then also strictly increasing. Denote these intervals by \([s_h,u_h]\), \(h=1,\ldots,q\). Their union covers all hyperedge indices \(1,\ldots,m\).

Let \(p_h=1\) for a private-vertex interval (width three), and \(p_h=0\) for a junction interval (width four). Let \(b_0=1-s_1\), \(b_q=u_q-m\), and \(d_h=u_h+1-s_{h+1}\) for \(1\le h<q\). Here \(b_0,b_q\in\{0,1\}\), because all candidate starts are at least zero and all candidate ends are at most \(m+1\); the cover must contain both endpoints. The integers \(d_h\ge0\) measure overlaps, since the intervals cover every integer and have increasing endpoints. Comparing the sum of their widths with the number \(m\) of covered hyperedge indices gives the exact identity
\[
4q-m=\sum_{h=1}^q p_h +\sum_{h=1}^{q-1}d_h+b_0+b_q. \tag{1}
\]
Since \(t=4q-m\le3\), every overlap is at most three. If \(d_h=3\), the adjacent \(p_h,p_{h+1}\) must both be zero, otherwise the right side of (1) is at least four. Consequently \(d_h<4-p_h\) and \(d_h<4-p_{h+1}\) for every \(h\), and the reconstructed intervals always have strictly increasing starts and ends.

Conversely, any collection of binary variables \(p_1,\ldots,p_q\), \(b_0,b_q\), and nonnegative integer overlaps \(d_1,\ldots,d_{q-1}\) satisfying (1) uniquely reconstructs intervals by \(s_1=1-b_0\), \(u_h=s_h+3-p_h\), and \(s_{h+1}=u_h+1-d_h\). They cover \(1,\ldots,m\), their starts and ends increase strictly, and the terminal equality forces \(u_q=m+b_q\). Every private interval has start in \([0,m-1]\); every junction interval has start in \([0,m-2]\). Thus these are precisely valid hyperpath vertex choices with multiplicities described next. There is no overcount: distinct selected subsets yield distinct interval choices and private-vertex labels.

**3. Private multiplicities and boundary generating function.** Put \(a=r-1\). An interior private interval has \(r-2=a-1\) possible vertices, whereas a private interval at the first or final hyperedge has \(r-1=a\) possible vertices. The first private interval is at the first edge exactly when \(b_0=1\); the last private interval is at the final edge exactly when \(b_q=1\). For \(q=1,m=1\), both endpoint bonuses apply to the same edge, giving \(r=a+1\) private choices, as required.

Introduce a formal defect marker \(z\). For \(q\ge2\), choosing each overlap contributes \((1-z)^{-1}\); the \(q-2\) interior selected intervals contribute \(1+(a-1)z\); and summing over the two endpoint overhang bits gives the factor \(1+az+az^2\) at each end. Hence the number of minimum sets for defect \(t\le3\) is
\[
M_{4q-t,r}=[z^t]\frac{(1+(a-1)z)^{q-2}(1+az+az^2)^2}{(1-z)^{q-1}},\qquad q\ge2. \tag{2}
\]
This generating function is an *exact near-minimum enumeration*, not an asymptotic approximation. For \(q=1\), explicitly summing both endpoint bits and the single private/junction choice gives
\[
H_1(z)=1+(a+1)z+(2a+1)z^2+(a+1)z^3.
\]
For \(q\ge2\), expansion of (2) through degree three yields the four stated expressions. The same expressions at \(q=1\) agree with \(H_1\), so the theorem holds for all \(m\ge1\). In particular at \(t=0\), equation (1) forces all intervals to be width four with no overlap or boundary overhang, proving the unique extremal pattern.

## Verification
The included standalone Python 3 script `verify.py` constructs the actual labelled hyperedges and checks all \(q\)-subsets directly for \(1\le m\le13\), \(r\in\{3,4,5\}\); these 39 literal-graph checks are independent of the interval proof. It also implements a separate weighted-interval dynamic program and verifies all 640 pairs \(1\le m\le80\), \(3\le r\le10\), plus the uniqueness and endpoint identities. The reported replay terminates with `VERIFY_OK`. These finite tests corroborate but do not replace the all-parameter proof above.

## Relationship to prior work
Baluci and Borg, *Isolation of \(k\)-cliques in uniform hypergraphs*, arXiv:2611.17489v1, first publicly posted 2026-11-12, proves general sharp upper bounds on the minimum isolating-set **size**, not the number of minimum sets for loose hyperpaths. Li, Zhang and Qu, *The isolation number of uniform hypertrees*, arXiv:2611.24477v1, posted 2026-11-18, proves order bounds and structural equality characterizations, not this exact multiplicity polynomial. The established loose-hypercycle minimum-isolation enumeration concerns circular intervals and does not supply the path endpoint contributions in (2); for instance a four-edge loose hyperpath has one optimum whereas a four-edge loose hypercycle has four. General subtree-transversal packing lemmas determine optima in some incidence-tree settings but do not directly count all optimum vertex subsets with endpoint multiplicities.

## Limitations
Only the minimum-cardinality isolating sets of *loose hyperpaths* are counted. All larger isolating sets, general nonpath hypertrees, and other forbidden hypergraphs are outside the result. The proof assumes \(r\ge3\), distinct junctions, and labelled vertices; it does not claim priority certification by an independent mathematical review. A possible unnoticed earlier path-specific enumeration remains a historical-priority risk.

## References
1. M. Baluci and P. Borg, *Isolation of \(k\)-cliques in uniform hypergraphs*, arXiv:2611.17489v1 (first submitted 2026-11-12). https://arxiv.org/abs/2611.17489
2. M. Li, S. Zhang and J. Qu, *The isolation number of uniform hypertrees*, arXiv:2611.24477v1 (submitted 2026-11-18). https://arxiv.org/html/2611.24477v1
3. M. Li, S. Zhang and C. Ye, *Partial domination of hypergraphs*, Graphs and Combinatorics 40 (2024), 109. https://doi.org/10.1007/s00373-024-02840-2
4. I. Bárány, J. Edmonds and L. A. Wolsey, *Packing and covering a tree by subtrees*, Combinatorica 6 (1986), 221–233.
