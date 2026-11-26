# Exact \(k\)-limited domination and optimal-set counts for crown graphs
## Finding
Let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph for \(n\ge3\), with deleted matching pairs \((a_i,b_i)\). For every integer \(k\ge1\), its \(k\)-limited domination number is
\[
\gamma_k^{\mathrm L}(\operatorname{Cr}_n)=
\begin{cases}
2(n-k-1),&1\le k\le n-2\text{ and }\left\lceil\frac{n-2}{2}\right\rceil\le k\le n-3,\\
2(n-k),&1\le k\le n-2\text{ and the preceding window does not hold},\\
2,&k\ge n-1.
\end{cases}
\]
Moreover the minimum \(k\)-limited dominating sets are completely classified. If \(1\le k\le n-2\) lies in the saving window and \(r=n-k-1\), every minimum set chooses \(r\) vertices from each shore with disjoint deleted-matching index sets, so their number is \(\binom nr\binom{n-r}{r}\). Outside that window but still with \(1\le k\le n-2\), every minimum set chooses \(n-k\) vertices independently from each shore, so their number is \(\binom{n}{n-k}^2\). For \(k\ge n-1\), the minimum sets are exactly the \(n\) deleted matching pairs. Thus deleting a perfect matching from \(K_{n,n}\) lowers the published value \(2(n-k)\) by exactly two precisely in the stated intermediate-capacity window.

Equivalently, in the nontrivial range \(1\le k\le n-2\), put \(q=n-k\) and \(r=q-1\). The value drops from the complete-bipartite baseline \(2q\) to \(2r\) exactly when two disjoint \(r\)-subsets of the deleted-matching index set can be chosen and \(r\ge2\), namely when \(2r\le n\) and \(r\ge2\).

## Assumptions and scope
All graphs are finite, simple, and undirected. The crown graph \(\operatorname{{Cr}}_n\) is \(K_{n,n}\) with a perfect matching \(\{{a_i b_i:1\le i\le n\}}\) removed. We take \(n\ge3\), so the graph is connected. A set \(D\) is \(k\)-limited dominating if it dominates every vertex outside \(D\) and every vertex of \(D\) has at most \(k\) neighbors outside \(D\). Since \(\Delta(\operatorname{{Cr}}_n)=n-1\), the genuinely constrained range is \(1\le k\le n-2\); for \(k\ge n-1\) the parameter is ordinary domination.

## Proof
Write
\[
S=\{{i:a_i\in D\}},\qquad T=\{{i:b_i\in D\}},\qquad s=|S|,\quad t=|T|.
\]
In the constrained range, a feasible set must meet both shores. If it missed one shore, every unselected vertex on that shore would force the opposite shore to be wholly selected, and then a selected vertex would have \(n-1>k\) neighbors outside. Moreover, domination forces \(s,t\ge2\): if, say, \(S=\{{j\}}\), then the unselected vertex \(b_j\) has no selected neighbor.

Put \(q=n-k\) and \(r=q-1\). If \(S\cap T\ne\varnothing\), choose \(i\in S\cap T\). The selected vertex \(a_i\) sees exactly \(n-t\) vertices outside \(D\), because its unique nonneighbor \(b_i\) is selected. Hence \(t\ge q\); by symmetry \(s\ge q\). Conversely, \(s,t\ge q\) makes every selected vertex satisfy the capacity bound and, since \(q\ge2\), also gives domination. Thus the intersecting-support minimum is \(2q\).

If \(S\cap T=\varnothing\), every selected \(a_i\) has its missing mate \(b_i\) outside \(D\), so it sees exactly \(n-t-1\) outside neighbors. Hence \(t\ge r\), and symmetrically \(s\ge r\). Conversely, disjoint supports with \(s,t\ge r\) satisfy the capacity bound; domination additionally requires \(s,t\ge2\). Therefore a set of size \(2r\) exists exactly when \(r\ge2\) and two disjoint \(r\)-subsets fit in \([n]\), that is, \(2r\le n\). In terms of \(k\), this is precisely
\[
\left\lceil\frac{n-2}{2}\right\rceil\le k\le n-3.
\]
If this condition fails, no disjoint-support set beats \(2q\), while taking arbitrary \(q\)-subsets on both shores attains \(2q\). At the endpoint \(k=n-2\), the formal disjoint lower bound would use one vertex per shore, but such a pair never dominates the two unmatched mates; the true minimum is therefore \(4=2q\).

For the counts, in the saving window every minimum set has \(s=t=r\) and disjoint supports, giving \(\binom nr\binom{{n-r}}r\) choices. Outside the window, every minimum set in the constrained range has \(s=t=q\), and every pair of \(q\)-subsets is feasible, giving \(\binom nq^2\). Finally, for \(k\ge n-1\) ordinary domination applies. A two-vertex set dominates the crown graph exactly when it is one deleted matching pair \(\{{a_i,b_i\}}\), yielding value \(2\) and exactly \(n\) minimum sets.

## Verification
The standalone verifier checks the theorem in two independent finite ways. It enumerates all feasible support-size/intersection profiles for every \(3\le n\le50\) and every \(1\le k\le n-1\), including exact minimum-set counts. Separately, it brute-forces every pair of vertex subsets on the two shores for \(3\le n\le6\). The replay output is stored with the verifier. These finite checks are stress tests only; the universal result follows from the support-intersection proof above.

## Relationship to prior work
Božović, Radić, Kovijanić-Vukićević, and Tepeh introduced \(k\)-limited domination and determined the complete-bipartite value. For \(K_{n,n}\) and \(1\le k<n\), their Proposition 1(iv) gives \(\gamma_k^{{\mathrm L}}(K_{n,n})=2(n-k)\). The present theorem shows exactly when deleting one perfect matching preserves this value and when it lowers it by two, while also classifying and counting all optimum sets.

The same paper proves that on a \(d\)-regular graph, \(k\)-limited domination equals \((1,d-k)\)-domination. This identity alone does not evaluate crown graphs. Searches under both terminologies, together with crown, deleted-perfect-matching, and exact-formula aliases, did not locate a statement implying the theorem. A previous exact result for complete multipartite graphs does not cover crown graphs: for \(n\ge3\), the nonadjacency relation in a crown graph is not the part-equivalence relation of a complete multipartite graph.

## Limitations
The theorem is restricted to crown graphs and does not evaluate arbitrary bipartite graphs with a partial matching deleted. The literature comparison included the initiating full article, the complete-bipartite theorem, the regular-graph bridge, recent follow-up abstracts, semantic-index searches, and prior local findings. An older or poorly indexed result under \((1,t)\)-domination or \((0,k)\)-pitchfork terminology remains a residual originality risk. The finite verifier is not a proof for unbounded \(n\).

## References
1. D. Božović, G. Radić, Ž. Kovijanić-Vukićević, A. Tepeh, “On \(k\)-limited domination in graphs,” arXiv:2606.22422, first public 2026-06-21; Computational and Applied Mathematics, DOI 10.1007/s40314-026-03902-2.
2. A. Tepeh, “On \(k\)-limited domination: complexity and Cartesian products,” arXiv:2606.22428, first public 2026-06-21.
3. G. Radić, A. Tepeh, “On \(1\)-limited and \((1,2)\)-domination in cubic graphs,” arXiv:2610.01796, first public 2026-10-01.
