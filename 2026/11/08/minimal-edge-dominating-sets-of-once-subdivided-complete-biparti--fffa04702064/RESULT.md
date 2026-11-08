# Minimal edge-dominating sets of once-subdivided complete bipartite graphs

## Finding

For integers \(m,n\ge1\), let \(H_{m,n}=S(K_{m,n})\) be the graph obtained by subdividing each edge of the labeled complete bipartite graph once. An *edge-dominating set* \(D\subseteq E(H_{m,n})\) meets the closed edge-neighborhood of every edge, where two edges are adjacent when they share an endpoint. It is *inclusion-minimal* if no proper subset is edge-dominating. Let \(M_{m,n}(z)=\sum_D z^{|D|}\), summed over every inclusion-minimal edge-dominating set.

Then the complete polynomial is
\[
\boxed{\begin{aligned}
M_{m,n}(z)={}&z^m\bigl((n+z^{n-1})^m-n^m\bigr)\\
&+z^n\bigl((m+z^{m-1})^n-m^n\bigr)\\
&+\bigl(n^m m^n-mn^m-nm^n+mn\bigr)z^{m+n}.
\end{aligned}}
\]
Equivalently, its first summand counts configurations with \(k\ge1\) inactive vertices in the \(m\)-side, weighted by \(\binom mk n^{m-k}z^{m+(n-1)k}\); the second is symmetric; the final summand counts configurations with no inactive original vertices.

For \(m,n\ge2\), the minimum and maximum cardinalities are respectively \(m+n-1\) and \(mn\); the number of minimum sets is \(mn^{m-1}+nm^{n-1}\). For \(s=\min\{m,n\}\ge3\), the cardinality \(mn-s+1\) occurs, but none of the \(s-2\) integers \(mn-s+2,\ldots,mn-1\) occurs. For every \(n\ge1\), \(M_{1,n}(z)=2^nz^n\). Thus the family has unbounded gaps among cardinalities of inclusion-minimal edge-dominating sets.

## Assumptions and scope

All graphs are finite, simple, and labeled. Fix disjoint original parts \(A\) and \(B\) of cardinalities \(m,n\ge1\). For each \(a\in A\), \(b\in B\), introduce a private subdivision vertex \(s_{ab}\). Its two incidence edges are denoted \([a,b]_a=as_{ab}\) and \([a,b]_b=bs_{ab}\). Labels make these edges distinguishable even for \(m=n\). The word *minimal* always means inclusion-minimal, not merely minimum cardinality.

For an edge set \(D\), an original vertex \(v\in A\cup B\) is *active* when at least one selected incidence edge touches \(v\), and *inactive* otherwise. Write \(I(D)\) for the inactive original vertices. Each selected incidence edge is assigned to its original endpoint, so every \(D\) has a unique representation as directed incidences \(v\to w\) along base edges \(vw\).

## Proof

**Edge-domination criterion.** Consider the incidence edge \([a,b]_a\). Its only neighboring edges in \(H_{m,n}\) are other incidence edges touching the original vertex \(a\) or the opposite incidence edge \([a,b]_b\). Thus \([a,b]_a\) is dominated precisely when \(a\) is active or \([a,b]_b\in D\). By symmetry, \([a,b]_b\) is dominated precisely when \(b\) is active or \([a,b]_a\in D\). Consequently \(D\) edge-dominates if and only if, for every inactive original vertex, the opposite incidence edge is selected along *every* base edge incident to it. No two inactive vertices may be adjacent. As the base graph is complete bipartite, either \(I(D)=\varnothing\), or \(I(D)\) is a nonempty subset of exactly one of \(A,B\).

**Nonempty inactive side.** Suppose \(I(D)=I\subseteq A\) and \(|I|=k\ge1\). The criterion forces all \(kn\) incidences \([a,b]_b\) with \(a\in I\), \(b\in B\). They make every \(b\in B\) active. Every \(a\in A\setminus I\) must select at least one of its \(n\) own incidences to be active. In a minimal set, it selects *exactly one*: deleting one of two such incidences leaves both its original endpoint and every opposite endpoint active, and hence leaves domination unchanged. Likewise, every nonforced selected incidence \([a,b]_b\) with \(a\in A\setminus I\) is redundant, because \(b\) remains active via its forced incidences and \(a\) is already active. Thus the only minimal candidates are precisely the \(kn\) forced incidences plus one chosen \([a,b]_a\) for each \(a\notin I\).

Conversely, each such candidate is inclusion-minimal. A forced incidence \([a,b]_b\) is the sole way to dominate \([a,b]_a\), because \(a\) is inactive. Removing the unique selected incidence at any \(a\in A\setminus I\) makes \(a\) inactive while no opposite incidence \([a,b]_b\) (for \(a\notin I\)) is selected, so domination fails. The candidate size is \(nk+(m-k)=m+(n-1)k\), and for each \(I\) there are \(n^{m-k}\) choices. Summing \(\binom mk\) labeled choices for \(I\) gives the first polynomial summand. Interchanging \(A,B\) gives the second summand. The two families are disjoint because \(I(D)\) is uniquely determined.

**No inactive originals.** If \(I(D)=\varnothing\), every original vertex has at least one selected incidence. Minimality forces *exactly one* at each original vertex: when one vertex selects two or more, deleting one leaves that vertex active and the opposite original vertex active, so the edge-domination criterion remains true. Conversely, in an exactly-one selection, deleting \(v\to w\) makes just the source \(v\) inactive. The remaining incidences dominate if and only if *every* neighbor of \(v\) selected its incidence toward \(v\). Therefore the exactly-one selection is inclusion-minimal if and only if no original vertex receives selections from all its neighbors.

There are \(n^m m^n\) exactly-one selections: each \(a\in A\) chooses one of its \(n\) neighbors, and each \(b\in B\) chooses one of its \(m\) neighbors. The nonminimal event that all \(B\)-vertices select the same particular \(a\in A\) has \(n^m\) configurations; the union of these events has \(mn^m\) configurations (different choices of recipient are disjoint, since \(n\ge1\)). Symmetrically, all \(A\)-vertices select one particular \(b\in B\) accounts for \(nm^n\) configurations. Their intersections consist of one configuration for each ordered pair \((a,b)\), altogether \(mn\). Inclusion-exclusion yields \(n^m m^n-mn^m-nm^n+mn\) minimal configurations, each of cardinality \(m+n\). The inactive and active families are disjoint and exhaustive, proving the polynomial.

**Extremal cardinalities and gaps.** For \(m,n\ge2\), the nonempty-inactive contributions have exponents \(m+(n-1)k\) and \(n+(m-1)k\). Their minima, at \(k=1\), equal \(m+n-1\); the no-inactive exponent \(m+n\) cannot be smaller. Their maxima, at \(k=m\) or \(k=n\), equal \(mn\); the no-inactive exponent satisfies \(m+n\le mn\) except at \((2,2)\), where equality still holds. Thus both extremes are attained. The coefficient of the smallest degree comes from \(k=1\) in the two inactive orientations and equals \(mn^{m-1}+nm^{n-1}\).

For \(3\le m\le n\), the next-largest exponent below \(mn\) in the two inactive families is \(mn-(m-1)\), attained by taking \(n-1\) inactive vertices in \(B\). Every other non-top inactive term is no larger. The no-inactive exponent \(m+n\) also satisfies \(m+n\le mn-m+1\). Therefore \(mn-m+1\) occurs, while the \(m-2\) intervening integers below \(mn\) do not. Symmetry yields the claim for any \(s=\min\{m,n\}\ge3\). Finally, for \(m=1\), the formula simplifies by direct substitution to \(M_{1,n}(z)=2^nz^n\); each subdivided arm contributes either of its two edges.

## Verification

Run the included `verify.py` with Python 3.9 or later; only the standard library is required. The script constructs the subdivided bipartite graph directly from its edges, computes every edge's closed edge-neighborhood, tests edge domination and minimality under every one-edge deletion, and compares these results against a separate incidence-family generator and the closed polynomial.

The verified execution was: `VERIFY_OK exact_cases=11 exhaustive_subsets=403028 exact_minimal_sets=1334 additional_cases=7 generated_tested=138494 all_coefficients=PASS all_families=PASS upper_gaps=PASS stars=PASS`. Exhaustive testing covers eleven labeled bipartition-size pairs through a maximum of eighteen graph edges; seven larger pairs test generated configurations and coefficients without claiming exhaustive coverage. The symbolic upper-gap consequence is checked for all pairs with both part sizes from three to fourteen. The proof, not these finite computations, establishes the statement for unrestricted \(m,n\).

## Relationship to prior work

Anderson, Kuenzel, and Rall (arXiv:2110.07133, first posted October 14, 2021) study well-edge-dominated graphs and give structural characterizations for triangle-free nonbipartite graphs, split graphs, and Cartesian products, including the earlier complete-bipartite *unsubdivided* case. Their treatment does not provide the present polynomial for one-subdivided bicliques. Frendrup, Hartnell, and Vestergaard (2010) already characterize graphs of girth at least five having all minimal edge-dominating sets of one size; this implies the qualitative failure of equicardinality in \(S(K_{m,n})\) when both parameters exceed one. That qualitative consequence is **not** claimed as new.

Horton and Kilakos (1993) proved \(\gamma'(S(G))=|V(G)|-\alpha_2(G)\), where \(\alpha_2(G)\) is the largest set with pairwise distance at least three. Applied to a nontrivial biclique, this already yields the minimum cardinality \(m+n-1\); it is recovered, **not newly asserted**, here. Kanté, Limouzy, Mary, Nourine, and Uno (arXiv:1404.3501) give a general polynomial-delay algorithm for listing minimal edge-dominating sets, which does not by itself yield the exact closed two-parameter enumerator, labeled multiplicities or the missing-cardinality interval. The proposed contribution is specifically the complete distribution and structural three-case classification.

## Limitations

The statement concerns labeled, once-subdivided complete bipartite graphs and ordinary edge domination. It is not a result for unsplit bicliques, arbitrary base graphs, or total/connected edge domination. Published minimum-cardinality and qualitative well-edge-dominated facts are pre-existing. Publication priority is provisional: particularly, the full text of Horton--Kilakos (1993) was not accessible, although its detailed abstract was read, and different terminology in unindexed literature could conceal related enumerations. No independent mathematical audit has been performed.

## References

1. S. E. Anderson, K. Kuenzel, D. F. Rall, *On well-edge-dominated graphs*, arXiv:2110.07133 (v1 October 14, 2021), https://arxiv.org/abs/2110.07133.
2. A. Frendrup, B. Hartnell, P. D. Vestergaard, *A note on equimatchable graphs*, Australas. J. Combin. **46** (2010), 185–190, https://ajc.maths.uq.edu.au/pdf/46/ajc_v46_p185.pdf.
3. J. D. Horton, K. Kilakos, *Minimum Edge Dominating Sets*, SIAM J. Discrete Math. **6** (1993), 375–387, https://doi.org/10.1137/0406030.
4. M. M. Kanté, V. Limouzy, A. Mary, L. Nourine, T. Uno, *Polynomial Delay Algorithm for Listing Minimal Edge Dominating sets in Graphs*, arXiv:1404.3501 (2014), https://arxiv.org/abs/1404.3501.
