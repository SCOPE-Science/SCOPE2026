# All maximal independent sets of two-token complete-bipartite graphs

## Finding

**Theorem.** Let \(m,n\ge 2\) be integers and let \(H=F_2(K_{m,n})\) be the ordinary (single-token-move) two-token graph of the labelled complete bipartite graph \(K_{m,n}\). Let \(M_{m,n}(z)=\sum_S z^{|S|}\), where the sum is over all inclusion-maximal independent sets \(S\subseteq V(H)\). With \(\binom ab=0\) for \(0\le a<b\), the entire cardinality enumerator is

\[
M_{m,n}(z)=z^{\binom m2+\binom n2}
+\sum_{\substack{1\le r\le m,\ m-r\ne1}}
 \sum_{\substack{1\le s\le n,\ n-s\ne1}}
 \binom mr\binom ns\,
 z^{\binom{m-r}{2}+\binom{n-s}{2}+rs}.
\]

Every maximal independent set is counted exactly once. Consequently, their **total number** is
\[
M_{m,n}(1)=1+(2^m-m-1)(2^n-n-1).
\]

Write \(2\le m\le n\). The **independent domination number**, the minimum cardinality of a maximal independent set, is
\[
i(H)=\begin{cases}
2,&m=n=2,\\
2n-3,&m=2,\ n\ge3,\\
\binom m2+n-m,&3\le m\le n.
\end{cases}
\]
For \(3\le m<n\), there are exactly \(m\binom n2\) sets attaining this minimum. For \(m=n\ge3\), the number of minimum sets is
\[
m\binom m2+\sum_{r=2}^{m-2}\binom mr\bigl(\binom mr+\binom m{r+1}\bigr).
\]
For \(m=2,n=3\), there are \(3\) minimum sets; for \(m=2,n\ge4\), there are \(\binom n2+\binom n3\); for \(m=n=2\), there is one. Thus the theorem gives both all facets of the independence complex and their complete dimension distribution.

## Assumptions and scope

All graphs are finite, undirected, simple, and labelled. The graph \(K_{m,n}\) has two distinguished vertex classes \(X,Y\) with \(|X|=m\), \(|Y|=n\). The vertices of \(H\) are the unordered two-element subsets of \(X\cup Y\). Two such subsets are adjacent precisely when their symmetric difference is an edge of \(K_{m,n}\) (that is, one token moves across the bipartition while the other remains fixed). The generating function counts distinct subsets of the labelled token-configurations, not graph-isomorphism classes, not ordinary independent sets, and not general dominating sets. An independent set is maximal if no further token-configuration can be added to it; equivalently it dominates the graph \(H\).

## Proof

**Step 1: the three layers and their adjacency.** There are three disjoint types of token-configurations: \(\binom X2\), \(\binom Y2\), and \(X\times Y\) (the last interpreted as unordered pairs with one endpoint in each part). None of the three types has internal edges in \(H\); a pair \(\{x,x'\}\in\binom X2\) is adjacent to the mixed configurations \(\{x,y\}\) and \(\{x',y\}\) for every \(y\in Y\); and symmetrically for \(\binom Y2\). There are no other edges.

**Step 2: rigidity of a maximal independent set.** Let \(S\) be any maximal independent set, and let \(A\subseteq X\) consist of vertices occurring in selected configurations of type \(\binom X2\). Define \(B\subseteq Y\) analogously. As these are endpoint supports of collections of pairs, \(|A|,|B|\) are each zero or at least two. Put \(R=X\setminus A\), \(T=Y\setminus B\). Independence forces every selected mixed configuration into \(R\times T\). Conversely, every configuration of \(R\times T\) is nonadjacent to every configuration already in \(S\): it touches neither a selected same-side pair nor another mixed configuration. By maximality it must be included. Hence the selected mixed configurations are **exactly** \(R\times T\).

If \(R\times T=\varnothing\), then \(S\) contains no mixed configuration. Every same-side configuration, being nonadjacent to every member of \(S\), must therefore be selected. This is the single exceptional maximal independent set \(S=\binom X2\cup\binom Y2\).

Otherwise \(R\ne\varnothing\) and \(T\ne\varnothing\). Any same-side configuration \(\{a,a'\}\in\binom A2\) is nonadjacent to \(R\times T\), and same-side configurations have no mutual edges. Hence maximality forces **all** of \(\binom A2\) into \(S\). Likewise all of \(\binom B2\) must be selected. Thus
\[
S=\binom A2\;\cup\;\binom B2\;\cup\;(R\times T),
\]
where \(R,T\) are nonempty and \(|A|,|B|\in\{0,2,3,\ldots\}\). The representation is unique because the within-side selected-pair supports recover \(A,B\) from \(S\).

**Step 3: sufficiency.** Choose any such \(A,B,R,T\). The displayed union is independent by Step 1. Every missing mixed configuration has its \(X\)-endpoint in \(A\) or its \(Y\)-endpoint in \(B\). A nonempty \(A\) has at least two vertices and all pairs inside \(A\) are selected, so a mixed configuration with \(X\)-endpoint in \(A\) is adjacent to a selected pair inside \(A\); similarly for \(B\). Every missing pair within \(X\) has an endpoint in nonempty \(R\) and hence is adjacent to a selected mixed configuration using that endpoint and any element of nonempty \(T\). The argument for missing pairs within \(Y\) is symmetric. Thus every omitted configuration is dominated and the union is maximal. The exceptional union of all same-side pairs is also maximal because every mixed configuration has a neighbour among them when \(m,n\ge2\).

**Step 4: enumeration.** Set \(r=|R|\), \(s=|T|\). The restrictions are \(1\le r\le m\), \(m-r\ne1\), and the analogous restrictions on \(s\). There are \(\binom mr\binom ns\) choices. Each choice gives a unique set of cardinality \(\binom{m-r}2+\binom{n-s}2+rs\). Including the single exceptional set proves the polynomial formula. Independently choosing \(R\) in \(2^m-m-1\) ways (all nonempty subsets except the \(m\) subsets of size \(m-1\)) and \(T\) in \(2^n-n-1\) ways proves the total-count formula.

**Step 5: minimum size and minimum-set counts.** Assume \(m\le n\). For a nonexceptional set write \(a=m-r\) and \(b=n-s\), so \(b\in\{0,2,3,\ldots,n-1\}\). Its size admits the exact decomposition
\[
\binom a2+\binom b2+rs
=\binom m2+r(n-m)+\frac{(b-r)(b-r-1)}2.
\]
The final factor is nonnegative for every integer \(b-r\), and vanishes exactly when \(b=r\) or \(b=r+1\). If \(m\ge3\), \(r\ge1\) gives the lower bound \(\binom m2+n-m\), realized by \(r=1\), \(b=2\). If \(m=2\), the permissible \(r\) is \(2\); for \(n\ge3\), choose \(b=2\), yielding \(2n-3\). If \(m=n=2\), the exceptional set has size \(2\) and the only nonexceptional set has size \(4\). In every other case, the exceptional set is larger than the displayed minimum.

For \(m<n\), \(m\ge3\), equality forces \(r=1,b=2\), producing \(m\binom n2\) choices. For \(m=n\ge3\), equality requires \(b=r\) or \(r+1\); the admissible possibilities are \(r=1,b=2\), or \(2\le r\le m-2\) with \(b=r\) or \(r+1\). Counting these gives the balanced minimum-set formula. For \(m=2\), equality instead forces \(r=2\) and \(b=2\) or \(3\), subject to \(b\le n-1\), giving the remaining counts. All cases are exhaustive.

## Verification

The standalone file `artifacts/verify.py` requires only Python's standard library. Running `python artifacts/verify.py` enumerates maximal cliques of the **independently constructed complement** of the token graph to enumerate maximal independent sets for all \(2\le m,n\le5\), compares their complete labelled sets and size distributions with the structural classification, and verifies independence, domination, the full polynomial, the total-count formula, and the minimum-set formulas for further parameters. The successful replay ends in `VERIFY_OK`. These finite checks corroborate the symbolic proof but do not replace it.

## Relationship to prior work

The exact maximum independent-set size of \(F_2(K_{m,n})\) is known from de Alba, Carballosa, Leaños and Rivera (2016/2020), and the absence of well-coveredness for nontrivial bipartite token graphs was established by Abdelmalek, the Vander Meulens and Van Tuyl (2020/2023). In 2026, Chinman and collaborators computed ordinary domination numbers for the same token-graph family, and Acosta Troncoso, Caldera Caldera and Rivera independently determined that parameter with a general characterization of **dominating** subsets. The latter characterization supplies related feasibility conditions, but does not classify or enumerate the maximal **independent** subsets. The present rigidity, all-size polynomial, total count, independent domination formula, and minimum-set census are separate statements; no claim is made about historical priority beyond the inspected literature.

## Limitations

The result applies only to ordinary two-token graphs of complete bipartite graphs with both parts of size at least two. The polynomial counts all inclusion-maximal independent sets, not all independent sets and not minimal dominating sets lacking independence. This is a mathematical proof with finite computational checks, not an independent mathematical audit. Full text of one highly relevant October 2026 preprint was not accessible during comparison; its abstract states results on ordinary domination numbers, and overlap risk remains.

## References

1. N. Chinman, A. Cortijo, B. Pedroni, I. Seong, L. Stenger, *The domination number of the \(k\)-token graph of the complete bipartite graph \(K_{m,n}\)*, arXiv:2610.28936, first public 2026-10-20, https://arxiv.org/abs/2610.28936.
2. E. Acosta Troncoso, I. Caldera Caldera, L. M. Rivera, *The domination number of the \(2\)-token graph of the complete bipartite graph*, arXiv:2610.31557, first public 2026-10-22, https://arxiv.org/abs/2610.31557.
3. F. M. Abdelmalek, E. Vander Meulen, K. N. Vander Meulen, A. Van Tuyl, *Well-covered token graphs*, arXiv:2010.04539, first public 2020-10-09, https://arxiv.org/abs/2010.04539.
4. H. de Alba, W. Carballosa, J. Leaños, L. M. Rivera, *Independence and matching numbers of some token graphs*, arXiv:1606.06370, first public 2016-06-21, https://arxiv.org/abs/1606.06370.
