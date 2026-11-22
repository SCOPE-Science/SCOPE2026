# A sharp Cayley-core approximation for unrooted forests of thin complete bipartite graphs

## Finding

Fix an integer \(a\ge2\). Label the two parts of \(K_{a,b}\) as \(A=\{1,\ldots,a\}\) and \(B=\{1,\ldots,b\}\), and choose uniformly from all *unrooted spanning forests*: acyclic subsets of the edge set, with every vertex retained, including isolated vertices. Write \(F_{a,b}\) for the total number of these forests.

For \(b\ge a-1\), let \(E_{a,b}\) be the event that exactly \(a-1\) vertices of \(B\) have degree two, every other vertex of \(B\) has degree zero or one, and suppressing the degree-two vertices leaves a tree on all \(a\) vertices of \(A\). Define \(Q_{a,b}\) by this explicit sampling procedure:

1. Choose a uniformly random labelled Cayley tree on \(A\).
2. Select \(a-1\) distinct labelled vertices of \(B\) uniformly and biject them uniformly to the tree's \(a-1\) edges; subdivide every tree edge at its assigned vertex of \(B\).
3. Independently for every remaining vertex of \(B\), choose one of \(a+1\) equally likely states: isolated, or connected by one edge to any specified vertex of \(A\).

**Theorem.** If \(P_{a,b}\) denotes the uniform unrooted spanning-forest law, then \(Q_{a,b}=P_{a,b}(\cdot\mid E_{a,b})\), and

\[
\begin{aligned}
|E_{a,b}|&=a^{a-2}(b)_{a-1}(a+1)^{b-a+1},\\
d_{\mathrm{TV}}(P_{a,b},Q_{a,b})
&=1-\frac{a^{a-2}(b)_{a-1}(a+1)^{b-a+1}}{F_{a,b}}\\
&=\frac{\kappa_a}{b}+O_a(b^{-2})\qquad (b\to\infty),
\end{aligned}
\]

where \((b)_j=b(b-1)\cdots(b-j+1)\),

\[
\begin{aligned}
T_1&=1,\quad T_s=s^{s-2}\quad(s\ge2),\\
H_a&=\frac12\sum_{s=1}^{a-1}\binom as T_sT_{a-s}
+\begin{cases}0,&a=2,\\3\binom a3a^{a-4},&a\ge3,\end{cases}\\
\kappa_a&=\frac{(a+1)H_a}{a^{a-2}}>0.
\end{aligned}
\]

The term \(a=2\) is an illustrative already-known special case of the two-hub connection probability, not a historical-priority claim. The new structural statement concerns the general fixed-shore regime, especially \(a\ge3\), and the exact conditional law and first correction.

The complete first two orders of unrooted forest enumeration are

\[
F_{a,b}=a^{a-2}(b)_{a-1}(a+1)^{b-a+1}
+H_a(b)_{a-2}(a+1)^{b-a+2}
+O_a\bigl(b^{a-3}(a+1)^b\bigr).
\]

In particular \(\kappa_2=3\), \(\kappa_3=16/3\), \(\kappa_4=135/16\), and \(\kappa_5=312/25\).

## Assumptions and scope

All graphs are finite, simple and labelled. Forests are *edge subsets*, not rooted forests, weighted by one each; the empty edge subset is included. The side of size \(a\) is held fixed while \(b\to\infty\). The event and exact conditional construction require \(a\ge2\) and \(b\ge a-1\); no balance assumption is imposed. Total variation is \(d_{\mathrm{TV}}(P,Q)=\sup_C|P(C)-Q(C)|\) on the same finite sample space of edge subsets. The error notation \(O_a\) permits constants depending on fixed \(a\), not uniform in \(a\).

## Proof

**1. An incidence-hyperforest rank bound.** Given any acyclic edge subset, call a vertex \(v\in B\) *special* if its degree is at least two. Each special vertex of degree \(d\) is represented by a hyperedge on its \(d\) neighbours in \(A\). The bipartite incidence graph of these hyperedges is acyclic, because it is obtained by discarding degree-zero and degree-one vertices of \(B\) from an acyclic graph. If its connected components on \(A\) number \(c\), elementary tree edge counting gives

\[
\sum_{v\in B\colon\deg(v)\ge2}(\deg(v)-1)=a-c\le a-1.
\]

In particular, the number \(k\) of special vertices never exceeds \(a-1\). Non-special vertices of \(B\) have exactly \(a+1\) unrestricted choices, so when a fixed acyclic special incidence pattern is assigned to a prescribed collection of \(k\) labelled vertices, every remaining vertex of \(B\) contributes a factor \(a+1\).

**2. The unique top-degree pattern.** If \(k=a-1\), each special vertex must have degree exactly two and the rank identity forces \(c=1\). Thus the pair-neighbourhoods of the special vertices are precisely the edges of a labelled spanning tree on \(A\). Conversely, every such assignment is acyclic. There are \(a^{a-2}\) core trees by Cayley's formula, \((b)_{a-1}\) assignments of distinct labelled vertices of \(B\) to their edges, and \((a+1)^{b-a+1}\) choices for the other vertices. This proves the exact count of \(E_{a,b}\), and, since each construction specifies exactly one distinct forest, proves the claimed conditional law \(P_{a,b}(\cdot\mid E_{a,b})=Q_{a,b}\). The identity for total variation is the elementary exact identity \(d_{\mathrm{TV}}(P,P(\cdot\mid E))=P(E^c)\).

**3. The complete next-degree patterns.** Suppose \(k=a-2\). The rank bound implies that either all \(a-2\) special vertices have degree two, or precisely one has degree three and all others have degree two. In the first case the pair-neighbourhoods form a labelled forest on \(A\) with precisely two connected components, counted by

\[
N_2(a)=\frac12\sum_{s=1}^{a-1}\binom as T_sT_{a-s}.
\]

In the second case, the three neighbours of the degree-three vertex are a specified triple \(U\subseteq A\); contracting this triple to one vertex gives a labelled tree on \(a-2\) vertices, whose edges incident to the contracted vertex can independently choose any of three endpoints in \(U\). For \(a\ge4\), the weighted Prüfer-code identity for a distinguished vertex of weight three gives

\[
\sum_{\tau\text{ tree on }a-2\text{ vertices}}3^{\deg_\tau(U)}=3a^{a-4}.
\]

For \(a=3\), the contracted tree is a single vertex, contributing one, agreeing with \(3a^{a-4}=1\). For \(a=2\), the degree-three case is impossible. Choosing \(U\) in \(\binom a3\) ways produces exactly the second summand in \(H_a\). Neither pattern may have an additional incidence cycle, and each counted contracted tree lifts to a unique special hyperforest for every choice of its endpoint attachments. Label the \(a-2\) special vertices in \((b)_{a-2}\) ways, and choose each remaining vertex independently in \(a+1\) ways: the complete contribution from \(k=a-2\) is

\[
H_a(b)_{a-2}(a+1)^{b-a+2}.
\]

**4. Control of the remainder.** For each fixed \(a\), the collection of possible special-neighbourhood patterns is finite: each neighbourhood is a subset of \(A\) with at least two elements and there are at most \(a-1\) such neighbourhoods. For \(k\le a-3\), assigning the \(k\) special labels and choosing all ordinary states gives, uniformly in \(b\), at most \(C_a b^{a-3}(a+1)^b\) forests for an \(a\)-dependent finite constant \(C_a\). (When \(a=2\) this remainder is empty.) Combining the exactly enumerated two top cases gives the displayed two-term formula. As \(b\to\infty\) at fixed \(a\), the ratio of its next-order term to its leading term is

\[
\frac{H_a(b)_{a-2}(a+1)^{b-a+2}}
{a^{a-2}(b)_{a-1}(a+1)^{b-a+1}}
=\frac{(a+1)H_a}{a^{a-2}(b-a+2)}
=\frac{\kappa_a}{b}+O_a(b^{-2}).
\]

Since the remaining terms are \(O_a(b^{-2})\) relative to the leading term, dividing by \(F_{a,b}\) gives the stated exact sharp first-order total-variation expansion. Positivity follows from \(N_2(a)>0\).

**5. Component consequences.** Under the exactly conditional law \(Q_{a,b}\), exactly one connected component contains edges and all vertices of \(A\). Every other component is an isolated vertex of \(B\). If \(X\) counts these isolated vertices, then

\[
X\ \sim\ \operatorname{Bin}\!\left(b-a+1,\frac1{a+1}\right).
\]

Thus the same binomial distribution approximates the isolated-vertex count under the original uniform-forest law with total-variation error at most \(\kappa_a/b+O_a(b^{-2})\). If \(L\) denotes the largest-component order, the conditional identity is \(L=a+b-X\); consequently \(L/b\to a/(a+1)\) in probability under \(P_{a,b}\), and

\[
\frac{L-\frac{a}{a+1}b}{\frac{\sqrt{ab}}{a+1}}\ \Longrightarrow\ N(0,1).
\]

These assertions follow from the elementary binomial law and the vanishing total-variation error, not from a separate infinite-graph theorem.

## Verification

The standalone dependency-free script `verify.py` implements three independent finite evaluations: exhaustive original edge-subset enumeration on small bicliques; exact enumeration of all admissible ordered special-neighbourhood hyperforests; and a distinct recurrence obtained by choosing the connected component of one specified small-side vertex. All agree for the tested ranges. The script additionally verifies both first two special-neighbourhood coefficients and evaluates the finite discrepancy against the stated first-order constant. Run `python3 verify.py` with Python 3.9 or newer. Finite tests corroborate the proof but are not used to extrapolate it.

## Relationship to prior work

Wu, Lu and Dong (2026, arXiv:2611.18076v1, first posted November 13) discuss spanning-forest bounds and use sparse-side complete bipartite graphs to disprove a degree-product inequality. Their construction uses independent choices of isolated vertices and leaves on the large side, but it does not count or classify the typical additional degree-two vertices, recover a uniform Cayley tree, or give this sharp conditional total-variation approximation. Stones (2014) computes fixed-edge forest counts in bicliques by exhaustive combinatorial enumeration, rather than the fixed-small-side limiting conditional structure. Stark (2013) studies \(a\to\infty\) with the other side relatively close, and supplies exact forest-count generating functions, but his asymptotic theorem does not apply to fixed \(a\) and does not give this structural concentration result. Dong and Ge (2022) count *spanning trees containing a prescribed forest*, which is a different probability measure and question. Other work on complete-graph massive spanning forests involves a different host and component-root weighting.

Published comparison records include a two-hub uniform-forest connection probability \(3/(b+3)\) on \(K_{2,b}\), corresponding to the already-understood \(a=2\) case; a rooted biclique forest component-count order; and an exact Cayley-core approximation for *spanning trees of complete split graphs*. They do not imply the general \(a\ge3\) unrooted-biclique law. In particular, a graph family or measure sharing the phrase 'Cayley core' is not an equivalent statement. The distinction is a comparison of mathematical implications, not a reliance on titles or absence of search hits.

## Limitations

The coefficient \(\kappa_a\), the remainder estimate, and the Gaussian consequence hold for each fixed \(a\), not uniformly as \(a\) grows with \(b\). The theorem does not provide a closed elementary formula for \(F_{a,b}\) at arbitrary simultaneous parameter growth. The total-variation approximation is on the full labelled forest space and is exact only after conditioning on \(E_{a,b}\). The \(a=2\) connectivity probability is already in earlier indexed work; originality is asserted only for the joint general structural/quantitative conclusion. Historical priority remains provisional pending external independent audit.

## References

1. T. Wu, S. Lu and X. Dong, *Upper bounds for the number of spanning forests of a graph*, arXiv:2611.18076v1 (first public version 2026-11-13). https://arxiv.org/abs/2611.18076
2. R. J. Stones, *Computing the number of h-edge spanning forests in complete bipartite graphs*, Discrete Mathematics & Theoretical Computer Science 16 (2014), 313–326. https://doi.org/10.46298/dmtcs.1248
3. D. Stark, *The asymptotic number of spanning forests of complete bipartite labelled graphs*, Discrete Mathematics 313 (2013), 1256–1261. https://doi.org/10.1016/j.disc.2012.10.026
4. F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, Journal of Graph Theory 101 (2022), 79–94. https://arxiv.org/abs/2103.05294
5. M. D'Achille, N. Enriquez and P. Melotti, *Massive Spanning Forests on the Complete Graph: Exact Distribution and Local Limit*, Random Structures & Algorithms 68 (2026), e70048. https://doi.org/10.1002/rsa.70048
