# Crown-graph power domination and nonmonotone reconfiguration thresholds

## Finding

For every integer \(n\ge4\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph with labeled shores \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i\) is adjacent to \(b_j\) exactly when \(i\ne j\). A set is power dominating if its closed neighborhood, followed by arbitrary repeated forcing of the sole unobserved neighbor of an observed vertex, observes the entire graph.

**Exact criterion.** A set \(S\subseteq A\cup B\) is power dominating if and only if either \(S\cap A\ne\varnothing\) and \(S\cap B\ne\varnothing\), or \(S\) is contained in one shore and has at least \(n-2\) vertices.

Therefore the all-set power domination polynomial and the inclusion-minimal-set polynomial are respectively

\[
\mathcal P_n(z)=\big((1+z)^n-1\big)^2+2\sum_{r=n-2}^{n}\binom nr z^r,
\qquad
\mathcal M_n(z)=n^2z^2+2\binom n2 z^{n-2}.
\]

In particular \(\gamma_P(\operatorname{Cr}_n)=2\) and the upper power domination number is \(\overline\gamma_P(\operatorname{Cr}_n)=n-2\). The minimal-set cardinality spectrum is \(\{2,n-2\}\), interpreted as the singleton \(\{2\}\) when \(n=4\). For \(n\ge6\) the cardinalities \(3,\ldots,n-3\) never occur.

Let \(\mathcal R_{n,k}\) be the token-addition/removal graph whose vertices are the power dominating sets of cardinality at most \(k\), with two sets adjacent when their symmetric difference is one vertex. Let \(c_n(k)\) be its number of connected components, for integers \(k\ge2\).

For \(n=4\), \(c_4(2)=28\) and \(c_4(k)=1\) for \(k\ge3\). For every \(n\ge5\),

\[
c_n(k)=\begin{cases}
n^2,&k=2,\\
1,&3\le k\le n-3,\\
1+2\binom n2,&k=n-2,\\
1,&k\ge n-1.
\end{cases}
\]

The middle range is empty if \(n=5\). Thus, for every \(n\ge6\), the budget-\(3\) graph is connected, the budget-\(n-2\) graph is disconnected, and the graph is connected again for every budget at least \(n-1\). The least connected budget is \(3\) and the stable connectivity threshold is \(n-1\) throughout \(n\ge6\).

## Assumptions and scope

All graphs are finite, simple and undirected. The integer \(n\) is at least \(4\). The initial observation is the **entire closed neighborhood** \(N[S]\), not just the initially selected vertices. A forcing move applies at an observed vertex with exactly one unobserved neighbor. The process ends once no force remains. An inclusion-minimal power dominating set has no proper power dominating subset. Monotonicity under adding selected vertices permits testing all one-vertex deletions for minimality. The token-addition/removal graph uses **all** power dominating sets up to the stated budget, not only minimum or inclusion-minimal ones. Budgets below \(2\) have no vertices and are outside the component statement.

## Proof

**1. Both-shore sets.** Fix any \(i,j\in[n]\). Start with \(\{a_i,b_j\}\). If \(i=j\), these two selected vertices observe every vertex in the initial domination step: \(a_i\) observes all \(b_\ell\) other than \(b_i\), which is selected, and \(b_i\) observes all \(a_\ell\) other than \(a_i\), which is selected. If \(i\ne j\), the only initially unobserved vertices are \(a_j\) and \(b_i\). Choose \(h\in[n]\setminus\{i,j\}\), which is possible since \(n\ge4\). The observed vertex \(a_h\) has exactly one unobserved neighbor, \(b_i\), and the observed vertex \(b_h\) has exactly one unobserved neighbor, \(a_j\). Both vertices are therefore forced. Every selected set meeting both shores contains one such pair and is power dominating by monotonicity.

**2. One-shore sets.** By shore symmetry, let \(S\subseteq A\) and write \(r=|S|\). If \(r=0\), the graph is not observed. If \(r=1\), say \(S=\{a_i\}\), the initially unobserved vertices are \(b_i\) and the \(n-1\) vertices of \(A\setminus\{a_i\}\). Each observed \(b_j\) for \(j\ne i\) has exactly \(n-2\ge2\) unobserved neighbors, and \(a_i\) has none. No force is possible. If \(r\ge2\), all of \(B\) is observed after the initial step, because each \(b_j\) misses only \(a_j\) among its potential neighbors. The unobserved set consists of \(q=n-r\) vertices in \(A\). If \(q\ge3\), every observed \(b_j\) has at least \(q-1\ge2\) unobserved neighbors and no force is possible. If \(q=2\), writing the unobserved vertices as \(a_p,a_q\) with distinct indices, the observed vertex \(b_p\) forces \(a_q\), and \(b_q\) forces \(a_p\). If \(q=1\), some \(b_j\) with \(j\ne p\) forces the sole unobserved \(a_p\); if \(q=0\), all vertices were already observed. This proves the exact criterion for every \(n\ge4\).

**3. Enumeration and inclusion-minimality.** A mixed set is specified uniquely by a nonempty subset of each shore, giving \(\big((1+z)^n-1\big)^2\). Pure sets meeting the threshold have \(2\binom nr\) choices of cardinality \(r\) for \(n-2\le r\le n\). The two classes are disjoint, proving the all-set polynomial. Every mixed pair is inclusion-minimal because singletons fail. Every pure set of size \(n-2\) is inclusion-minimal because all its proper subsets are smaller pure sets and fail. Every larger mixed set contains a mixed pair; every larger pure set contains a pure set of size \(n-2\). Thus the stated classes exhaust the inclusion-minimal sets, proving \(\mathcal M_n\), the two extremal sizes and the absent-cardinality interval.

**4. Mixed-set reconfiguration.** For each \(k\ge3\), all mixed power dominating sets of size at most \(k\) form one connected component: delete selected vertices while keeping one from each shore to reach a mixed pair. Two pairs \(\{a_i,b_j\}\) and \(\{a_p,b_q\}\) can be connected by changing first the \(A\)-coordinate and then the \(B\)-coordinate, each change made by temporarily adding one token (size \(3\)) and deleting the old token. For \(k=2\), the mixed pairs have no neighbors in \(\mathcal R_{n,2}\), since singletons fail.

**5. Component counts.** If \(n\ge5\) and \(k<n-2\), no pure power dominating set occurs. Hence \(c_n(2)=n^2\), and \(c_n(k)=1\) for \(3\le k\le n-3\). At \(k=n-2\), exactly \(2\binom n2\) pure power dominating sets appear, all with cardinality exactly \(k\). Each is isolated: every deletion fails, and no addition remains within budget. The remaining mixed component is connected, giving \(c_n(n-2)=1+2\binom n2\). At \(k\ge n-1\), any pure power dominating set can delete within its shore until it reaches a pure set of size \(n-2\), then add a vertex of the opposite shore to join the mixed component. All sets are therefore connected. For \(n=4\), every power dominating set of size \(2\) is inclusion-minimal; there are \(\binom82=28\) isolated sets at budget \(2\). Every pure pair connects to the mixed component by adding an opposite-shore vertex when the budget reaches \(3\), and higher budgets add no disconnected components. This establishes the complete connectivity profile.

## Verification

The standalone file `verify_crown.py` builds crown adjacency lists directly from the relation \(a_i b_j\iff i\ne j\). It enumerates all vertex subsets for each \(n=4,5,6,7,8\), simulates the closed-neighborhood observation and all possible single-unobserved-neighbor forcing steps, and independently compares the result with the proposed shore-support criterion. It checks every coefficient of \(\mathcal P_n\) and \(\mathcal M_n\), and constructs each budgeted token-addition/removal graph by exact adjacency and graph traversal. In total it examines \(87{,}296\) subsets, confirming \(86{,}539\) power dominating sets, \(350\) inclusion-minimal sets, and \(25\) complete component counts. The program prints `VERIFY_OK` on success and needs only Python 3 standard-library modules.

These computations are finite cross-checks; the proof above establishes the statements for every integer \(n\ge4\).

## Relationship to prior work

Brimkov, Patel, Suriyanarayana and Teich (2018) introduce the power domination polynomial and prove general enumerative properties. The accessible complete article includes several explicit families but does not present the crown-graph all-set polynomial or budget-by-budget reconfiguration profile here.

Chandrasekaran and Sulthana (2019) study generalized \(k\)-power domination for crown graphs. Its publicly accessible text has ambiguities in typesetting and in the graph-model terminology. Its readable main results concern minimum cardinality and generalized forcing; they do not give an accessible statement of the exact all-set enumerator and token-addition/removal connectivity profile proved here. Priority comparisons involving that paper remain qualified by the source-access limitation.

Bjorkman, Bozeman, Ferrero, Flagg, Grood, Hogben, Jacob and Reinhart (2026) develop power-domination reconfiguration generally and exhibit nonmonotone connectivity for other graph families. Their general bound \(\overline\gamma_P(G)+1\le pd_0(G)\le\overline\gamma_P(G)+\gamma_P(G)\) gives only \(n-1\le pd_0(\operatorname{Cr}_n)\le n\) after substituting this theorem's sizes; it does not imply the exact threshold, intermediate component numbers, or the crown-specific budget profile. Nonmonotonicity itself is **not claimed to be new in general**.

Database and primary-literature searches using the synonyms crown graph, biclique crown, perfect-matching-deleted complete bipartite graph, power domination polynomial, and token-addition/removal reconfiguration did not identify equivalent or stronger coverage. Failure to find a source does not establish absolute publication priority.

## Limitations

The result is restricted to the standard closed-neighborhood power domination process on \(K_{n,n}\) with **a complete matching removed**, for \(n\ge4\). It does not extend automatically to partial-matching deletion, generalized \(k\)-power domination, connected power domination, token jumping, or token sliding. Computational verification ends at \(n=8\), although the proof is unrestricted. The 2019 same-family source has remaining text-access and interpretation risks; an unindexed equivalent result is possible. Independent external mathematical audit has not been performed.

## References

1. B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984 (first public version 2018-05-28), https://arxiv.org/abs/1805.10984.
2. S. Chandrasekaran, A. Sulthana, *k-Power Domination of Crown Graph*, International Journal of Applied Engineering Research **14** (2019), 3066–3068, https://www.ripublication.com/ijaer19/ijaerv14n13_11.pdf.
3. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob, C. Reinhart, *Power Domination Reconfiguration*, La Matematica **5** (2026), article 8, https://doi.org/10.1007/s44007-025-00187-5.
