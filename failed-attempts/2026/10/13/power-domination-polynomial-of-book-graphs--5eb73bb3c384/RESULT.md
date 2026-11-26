# Power domination polynomial of book graphs
## Finding
For every integer \(n\ge2\), let \(B_n=K_{{1,n}}\mathbin{{\square}}P_2\) be the book graph with spine vertices \(u,v\). For each \(1\le i\le n\), page \(i\) has the two nonspine vertices \(a_i,b_i\) and edges \(uv,ua_i,a_ib_i,b_iv\).

A set \(S\subseteq V(B_n)\) is power dominating if and only if either

1. \(S\cap\{{u,v\}}\ne\varnothing\); or
2. \(S\cap\{{u,v\}}=\varnothing\) and at most one page pair \(\{{a_i,b_i\}}\) is disjoint from \(S\).

Therefore
\[
\mathcal P(B_n;x)=(2x+x^2)(1+x)^{{2n}}+(2x+x^2)^n+n(2x+x^2)^{{n-1}}.
\]
In particular, the total number of power dominating sets is
\[
3\cdot4^n+(n+3)3^{{n-1}}.
\]
For \(n=2\), every nonempty vertex set is power dominating, so there are six minimum singleton sets. For every \(n\ge3\), \(\gamma_P(B_n)=1\), and the only minimum power dominating sets are \(\{{u\}}\) and \(\{{v\}}\).

## Assumptions and scope
Graphs are finite, simple, and undirected. Power domination uses the standard two-stage rule: first observe the closed neighborhood of the initial set, then repeatedly let an observed vertex with exactly one unobserved neighbor observe that neighbor. The theorem covers every integer \(n\ge2\). The boundary graph \(B_1\cong C_4\) is deliberately excluded from the displayed formula because the page-only case has a degenerate empty-set overlap; its polynomial is \( (1+x)^4-1\).

## Proof
Suppose first that \(u\in S\) or \(v\in S\). By symmetry take \(u\in S\). The domination step observes \(u,v\) and every \(a_i\). Any unobserved \(b_i\) is then the unique unobserved neighbor of \(a_i\), so all such vertices are forced. Thus every set meeting the spine is power dominating.

Now suppose \(S\cap\{u,v\}=\varnothing\). If \(S\) meets a page, then after the domination step and at most one forcing step both spine vertices become observed: selecting \(a_i\) observes \(u\) and \(b_i\), after which \(b_i\) can observe \(v\); the case of selecting \(b_i\) is symmetric, and selecting both already observes both spine vertices. Once both spine vertices are observed, every page met by \(S\) is fully observed.

Let \(r\) be the number of page pairs disjoint from \(S\). If \(r=0\), observation is complete. If \(r=1\), the two spine vertices each have exactly one unobserved neighbor on the unique untouched page, so they force those two vertices and finish. If \(r\ge2\), then \(u\) has at least two unobserved neighbors \(a_i\) and \(v\) has at least two unobserved neighbors \(b_i\), while every observed page vertex has no neighbor on any untouched page. Hence no further force is possible and \(S\) is not power dominating. This proves the classification.

For the enumerator, sets meeting the spine contribute \( (2x+x^2)(1+x)^{{2n}}\). With no spine vertex selected, meeting every page contributes \( (2x+x^2)^n\), because each page contributes one of its three nonempty subsets. Leaving exactly one page untouched contributes \(n(2x+x^2)^{{n-1}}\). These cases are disjoint and exhaustive, proving the polynomial. Evaluation at \(x=1\) gives the stated total count. The coefficient of \(x\) is six when \(n=2\), and two when \(n\ge3\), yielding the minimum-set statements.

## Verification
The accompanying `verify_book_power.py` constructs \(B_n\), simulates the standard power-domination process independently of the structural criterion, exhausts every vertex subset for \(2\le n\le7\), and checks the classification, every coefficient of the closed formula, the total count, and the minimum-set count. The exhaustive computation is a finite check only; the all-orders claim rests on the proof above.

## Relationship to prior work
Haynes, Hedetniemi, Hedetniemi, and Henning introduced power domination in the electric-network setting; the original article records electronic publication on 10 September 2002 and classifies the subject under MSC 05C69. Brimkov, Patel, Suriyanarayana, and Teich introduced the power domination polynomial and developed decomposition formulas and several graph-family formulas. Their full preprint contains no occurrence of “book” or “Cartesian”, and its concluding questions explicitly ask for further nontrivial families to have their power dominating sets characterized or counted.

Kuriachan and Parthiban define the book graph and use its ordinary domination polynomial in their 2025 entropy paper. In the same full paper, the power-domination section names the families whose power domination polynomials are known or derived there—complete graphs, paths, cycles, wheels, stars and complements, windmills, friendship graphs, Dutch windmills, cone graphs, and fan graphs—but does not give a book-graph power domination polynomial. Thus the closest same-object source inspected does not cover the theorem here.

## Limitations
The theorem concerns ordinary power domination only, not connected, restricted, failed, or generalized \(k\)-power domination. It gives an exact formula for book graphs and does not assert a Cartesian-product formula for arbitrary factors. Literature searches cannot exclude every unindexed or differently named equivalent result; the principal residual originality risk is such an inaccessible or poorly indexed source.

## References
1. T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi, and M. A. Henning, “Domination in Graphs Applied to Electric Power Networks,” *SIAM Journal on Discrete Mathematics* 15(4), 519–529 (2002), DOI 10.1137/S0895480100375831.
2. B. Brimkov, R. Patel, V. Suriyanarayana, and A. Teich, “Power domination polynomials of graphs,” arXiv:1805.10984 (2018).
3. G. Kuriachan and A. Parthiban, “On Graph Entropy Measures Based on the Number of Dominating and Power Dominating Sets,” *Malaysian Journal of Mathematical Sciences* 19(1), 269–287 (2025), DOI 10.47836/mjms.19.1.14.
