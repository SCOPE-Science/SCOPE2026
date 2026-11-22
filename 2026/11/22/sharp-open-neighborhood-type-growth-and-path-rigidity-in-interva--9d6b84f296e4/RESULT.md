# Sharp open-neighborhood type growth and path rigidity in interval graphs

## Finding

Let \(G\) range over finite nonempty simple undirected interval graphs and let \(A\subseteq V(G)\) have size \(m\geq1\). Define the open-neighborhood one-variable type family
\[
\mathcal T(G,A)=\{N_G(v)\cap A:v\in V(G)\},\qquad t(G,A)=|\mathcal T(G,A)|.
\]
Here \(v\notin N_G(v)\), including when \(v\in A\). The **exact maximum** over all such \((G,A)\) is
\[
\max_{G,A:\,|A|=m}t(G,A)=
\begin{cases}2,&m=1,\\4,&m=2,\\1+\binom{m+1}{2}+m-2,&m\geq3.\end{cases}
\]
For \(m\geq3\), equality holds only if the induced graph \(G[A]\) is a chordless path whose left-to-right interval order is its path order. Conversely, every such ordered path can be extended by interval vertices to attain equality. In any interval representation with pairwise distinct marked endpoints, the equality case forces a left-to-right sequence of marked intervals with consecutive overlaps and no nonconsecutive overlaps.

The **smallest possible order** of an extremal graph is \(2\) for \(m=1\), \(4\) for \(m=2\), \(9\) for \(m=3\), and exactly \(1+\binom{m+1}{2}+m-2\) for every \(m\geq4\). In particular, open neighborhoods shatter three marked vertices of an interval graph, whereas four marked vertices cannot be shattered; the open-neighborhood VC dimension of the class is exactly three.

## Assumptions and scope

A finite interval graph has an interval \(I_v=[L_v,R_v]\) for each vertex and distinct vertices are adjacent precisely when the intervals intersect. All graph assertions use **open** neighborhoods, not distance-at-most-one (closed) neighborhoods. Without affecting adjacencies, a finite interval representation can be made generic so that all endpoints are distinct: infinitesimal overlap-preserving perturbations separate endpoints without altering any strict gap or previously present intersection. Fix a generic representation for the arguments below. The numerical upper bounds apply regardless of connectedness or representation chosen.

A *contiguous block* of marked intervals means consecutive indices under increasing left endpoint; empty block is permitted. The graph-order minimum counts every vertex, including those in \(A\).

## Proof

**1. Intersection queries.** Define \(\mathcal C_A\) as the subsets of \(A\) hit by arbitrary auxiliary closed intervals \(J\) (whether or not they already represent a vertex). Set
\[B_m=1+m+\binom m2=1+\binom{m+1}{2}.\]
Let \(c\) be the number of unordered *strict containment pairs* among the \(m\) marked intervals. Every nonempty hit set \(S\in\mathcal C_A\) is uniquely determined by an ordered pair \((i,j)\), where \(i\) has the smallest right endpoint among members of \(S\) and \(j\) the largest left endpoint. Indeed, if \(J=[u,v]\), its intersection constraints give
\[
S=\{k\in A:R_k\geq R_i\ \text{and}\ L_k\leq L_j\}.
\]
The reverse inclusion holds because \(R_k\geq R_i\geq u\) and \(L_k\leq L_j\leq v\) make \(I_k\cap J\ne\varnothing\). Distinct sets have distinct canonical pairs. A canonical pair with \(i\ne j\) must satisfy \(L_i<L_j\) and \(R_i<R_j\): since \(i\) minimizes right endpoints and \(j\) maximizes left endpoints, strictness follows from distinct endpoints. Thus each noncontainment pair contributes at most one non-diagonal canonical pair, every containment pair contributes none, and the diagonal contributes at most \(m\) pairs. Including the empty trace,
\[|\mathcal C_A|\leq B_m-c.\tag{1}\]

**2. Correcting self-incidence.** Every vertex outside \(A\) has an open trace in \(\mathcal C_A\). Each marked \(i\in A\) has its intersection query trace \(I_i\cap A\) with its own index removed. Hence
\[t(G,A)\leq|\mathcal C_A|+m-d,\tag{2}\]
where \(d\) is any lower bound for the number of marked vertices whose open trace already belongs to \(\mathcal C_A\), counting marked vertices rather than distinct traces.

Let \(a\) index the minimum marked right endpoint, and \(b\) the maximum marked left endpoint. The open trace of \(a\) is realized by an auxiliary point interval placed just to the right of \(R_a\): every other marked interval meeting \(I_a\) extends beyond \(R_a\), and no disjoint marked interval can contain that point. Symmetrically, the open trace of \(b\) is realized immediately left of \(L_b\). If \(a\ne b\), two marked vertices therefore give traces in \(\mathcal C_A\), so \(d\ge2\). If \(a=b\), all other marked intervals strictly contain \(I_a\), hence \(c\ge m-1\), and at least one marked trace lies in \(\mathcal C_A\), so \(d\ge1\).

For \(m\ge3\), equations (1)--(2) imply
\[t(G,A)\leq B_m+m-2.\tag{3}\]
More precisely, if \(c>0\), this inequality is strict: when \(a\ne b\), (1)--(2) give at most \(B_m+m-2-c\); when \(a=b\), they give at most \(B_m-(m-1)+m-1=B_m\), strictly less than \(B_m+m-2\) for \(m\ge3\). Thus *equality forces \(c=0\)*.

**3. Equality rigidity.** With no containment pairs, order marked intervals by left endpoints, also their order by right endpoints. Any auxiliary interval intersects a contiguous block of this order: if it meets intervals indexed \(i<k\), it also meets all intervening indices. The full family of all contiguous blocks has exactly \(B_m\) members. Equality in (3) forces (a) \(\mathcal C_A\) to consist of all these blocks, and (b) all \(m-2\) interior marked vertices to contribute distinct traces outside \(\mathcal C_A\).

For an interior index \(i\), realizing singleton block \(\{i\}\) requires an auxiliary interval beginning after \(R_{i-1}\) and ending before \(L_{i+1}\); hence \(R_{i-1}<L_{i+1}\). These inequalities for every \(i\) imply all nonconsecutive marked intervals are disjoint. Conversely, they ensure all contiguous blocks are possible. Now an interior marked vertex has open trace a subset of \(\{i-1,i+1\}\), and its trace lies outside the contiguous-block family precisely when it meets both immediate neighbors, yielding the noncontiguous trace \(\{i-1,i+1\}\). All interior vertices must do so. Therefore all successive marked intervals overlap and every nonconsecutive pair is disjoint: \(G[A]\) is the marked induced path. This proves necessity, and the explicit construction below proves sufficiency. The path's interval order is determined up to reversal.

**4. Witnesses and minimum order.** For \(m\ge3\), take
\[I_i=[4i,4i+6],\qquad 0\le i<m.\]
For each nonempty block \(\{i,i+1,\ldots,j\}\) a probe \(J_{i,j}=[4i+3,4j+3]\) meets exactly that block; a probe \([-2,-1]\) meets none. Thus \(\mathcal C_A\) is the family of all \(B_m\) contiguous blocks. The two endpoint marked vertices contribute singleton patterns \(\{1\}\) and \(\{m-2\}\). The \(m-2\) interior marked vertices contribute the noncontiguous patterns \(\{i-1,i+1\}\), which are pairwise distinct. Add one new interval-vertex for each contiguous-block trace not supplied by these endpoint vertices. For \(m=3\) the two endpoint singleton patterns coincide, so add \(B_m-1\) new vertices: graph order \(3+(B_m-1)=9\), and distinct-trace count \(B_m+1=8\). For \(m\ge4\) they differ, so add \(B_m-2\) new vertices, graph order \(m+B_m-2\), and all vertices have distinct traces, achieving the general lower bound \(|V(G)|\ge t(G,A)\).

In every extremal graph with \(m=3\), the marked induced path has the two endpoints with identical open traces \(\{\text{middle}\}\), so at least one duplicate vertex trace is inevitable, proving the sharp lower bound nine. For \(m=2\), two adjacent marked vertices have two distinct singleton open traces, and external probes supply the empty and full traces; exactly four vertices are necessary and sufficient. For \(m=1\), one marked vertex and one adjacent unmarked vertex supply the empty and singleton traces; two vertices are necessary and sufficient.

**5. VC boundary.** The \(m=3\) construction realizes all \(2^3\) subsets. The \(m=4\) bound is \(13<2^4\), excluding shattering of four vertices. Shattering of a larger set would shatter each of its four-subsets, so the maximal VC dimension is three.

## Verification

The standalone `verify.py` enumerates all perfect matchings of \(2m\) endpoints for \(1\le m\le6\), constructs the complete auxiliary-interval hit-set family, includes the marked vertices' diagonal-deleted profiles, and tests the exact maximum. There are respectively \(1,3,15,105,945,10395\) endpoint matchings. For \(m=3,4,5,6\) the endpoint pattern achieving the maximum is the unique proper consecutive-overlap path arrangement under fixed endpoint order. A separate constructive check builds extremal graphs for \(1\le m\le10\), including the nine-vertex exceptional case. Run `python3 verify.py`. Output concludes `VERIFY_OK`. This finite enumeration is corroboration; steps 1--5 prove the claims for arbitrary finite sizes.

## Relationship to prior work

The one-variable quantifier-free formula \(E(x,y)\), with \(y\) ranging over a parameter set, generates precisely the open-neighborhood types counted here. Dreier, Mählmann and Toruńczyk (2026) address far more general finite-model type counting and model checking, but their stated results are asymptotic/general and do not supply the interval-specific sharp coefficient, rigidity or minimum extremal order. Beaudou et al. (2025) introduce radius-dependent *closed* neighborhood/profile complexity (including distance zero), with bounds for different structural graph classes; they do not assert this open-neighborhood extremal theorem. The closed-neighborhood VC statement for interval graphs in Parreau's identifying-code presentation is about \(N[v]\), not \(N(v)\); self-incidence deletion is exactly the feature giving three-point open shattering. Related published finite interval-membership online-shattering results involve point-in-interval membership, not symmetric interval-graph adjacency traces. Exact historical priority remains subject to examination of earlier specialized incidence literature.

## Limitations

The result is specific to finite *interval intersection* graphs, open neighborhoods, and quantifier-free adjacency types. It does not assert the same formula for closed neighborhoods, general intersection graphs, higher-variable types, rank-dependent modal types, or online shattering. The endpoint-order uniqueness is a statement about marked intervals in a generic representation and the extremal induced path; it does not assert that the complete extremal graph is unique. Full text of the motivating November 2026 preprint could not be inspected in this study; only public metadata and abstract were accessible. No independent review or historical-priority certification is claimed.

## References

1. Jan Dreier, Nikolas Mählmann and Szymon Toruńczyk, *First-Order Model Checking on Monadically Dependent Graph Classes*, arXiv:2611.08143, first submitted November 5, 2026, https://arxiv.org/abs/2611.08143.
2. Laurent Beaudou, Jan Bok, Florent Foucaud, Daniel A. Quiroz and Jean-Florent Raymond, *Profile and Neighbourhood Complexity of Graphs with Excluded Minors and Tree-Structured Graphs*, 2025 open-access manuscript, https://perso.ens-lyon.fr/jean-florent.raymond/files/neighcplx.pdf.
3. Aline Parreau, *Identifying Codes and VC-Dimension*, 2013 seminar slides, https://perso.liris.cnrs.fr/aline.parreau/Research/Slides/seminaireCombgraph13.pdf.
4. Jan Dreier, Nikolas Mählmann, Rose McCarty, Michał Pilipczuk and Szymon Toruńczyk, *Neighborhood Complexity and Radius-1 Merge-Width in Monadically Dependent Graph Classes*, arXiv:2607.10941, July 2026, https://arxiv.org/abs/2607.10941.
