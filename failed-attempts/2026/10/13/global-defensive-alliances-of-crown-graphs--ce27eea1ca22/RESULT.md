# Global defensive alliances of crown graphs
## Finding
Let \(\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\}\) for \(n\ge3\). For a vertex set \(S\), partition the index set \([n]\) into four types: \(P\) consists of indices with \(a_i\in S\) and \(b_i\notin S\); \(R\) consists of indices with \(a_i\notin S\) and \(b_i\in S\); \(C\) consists of indices with both endpoints in \(S\); and \(W\) consists of indices with neither endpoint in \(S\). Put \(p=|P|\), \(r=|R|\), \(c=|C|\), \(w=|W|\), and
\[
q=\left\lfloor\frac{n-1}{2}\right\rfloor.
\]

A nonempty set \(S\) is a defensive alliance exactly in the following two cases:
\[
c=0,\quad p\ge q,\quad r\ge q,
\]
or
\[
c>0,\quad p+c\ge q+1,\quad r+c\ge q+1.
\]
For every \(n\ge5\), each such defensive alliance is automatically a dominating set and its induced subgraph is connected. Thus, for \(n\ge5\), the defensive alliances and the global defensive alliances coincide.

Define the global defensive-alliance cardinality enumerator by
\[
\mathcal A_n(x)=\sum_{S\text{ global defensive alliance}}x^{|S|}.
\]
Then, for \(n\ge5\),
\[
\mathcal A_n(x)=
\sum_{\substack{p,r\ge q\\p+r\le n}}
\frac{n!}{p!\,r!\,(n-p-r)!}x^{p+r}
+
\sum_{\substack{c\ge1,\ p,r\ge0\\p+c\ge q+1,\ r+c\ge q+1\\p+r+c\le n}}
\frac{n!}{p!\,r!\,c!\,(n-p-r-c)!}x^{p+r+2c}.
\]
The small cases are
\[
\mathcal A_3(x)=9x^4+6x^5+x^6
\]
and
\[
\mathcal A_4(x)=36x^4+48x^5+28x^6+8x^7+x^8.
\]
Consequently,
\[
\gamma_a(\operatorname{Cr}_n)=
\begin{cases}
4,&n\in\{3,4\},\\
2\left\lfloor\frac{n-1}{2}\right\rfloor,&n\ge5,
\end{cases}
\]
and, when \(n\ge5\), the number of minimum global defensive alliances is
\[
\frac{n!}{q!^2(n-2q)!}.
\]
The foundational result \(\gamma_a(K_{n,n})=2\lfloor n/2\rfloor\) therefore shows a parity-sensitive perturbation: deleting one perfect matching lowers the global defensive-alliance number by two exactly for even \(n\ge6\), while for odd \(n\ge5\) the minimum cardinality is unchanged.

## Assumptions and scope
Graphs are finite and simple. The defensive-alliance convention is the one used by Haynes, Hedetniemi, and Henning: a nonempty \(S\subseteq V(G)\) is defensive when
\[
|N[v]\cap S|\ge |N(v)\cap(V(G)\setminus S)|
\]
for every \(v\in S\), and it is global when it is also dominating. The result concerns the crown graph \(\operatorname{Cr}_n\) with the specified deleted perfect matching. The enumerator \(\mathcal A_n(x)\) is defined here only as the size generating function of global defensive alliances; it is not the later bivariate defensive-alliance polynomial.

## Proof
Every vertex of \(\operatorname{Cr}_n\) has degree \(n-1\). For a selected vertex \(v\), the defensive inequality is equivalent to
\[
2\deg_S(v)\ge n-2,
\]
so \(\deg_S(v)\ge q\), where \(q=\lfloor(n-1)/2\rfloor\).

Let \(A_S=\{i:a_i\in S\}\) and \(B_S=\{i:b_i\in S\}\). If \(i\in P\), then every selected \(B\)-vertex is adjacent to \(a_i\), hence
\[
\deg_S(a_i)=r+c.
\]
If \(i\in C\), then the selected vertex \(b_i\) is precisely the one selected \(B\)-vertex not adjacent to \(a_i\), so
\[
\deg_S(a_i)=r+c-1.
\]
The symmetric formulas for selected \(B\)-vertices are \(p+c\) on \(R\) and \(p+c-1\) on \(C\).

If \(c=0\), nonemptiness together with the defensive inequalities forces both sides to be represented and gives exactly \(p,r\ge q\). If \(c>0\), the vertices indexed by \(C\) impose the stronger inequalities \(p+c,r+c\ge q+1\); these imply the weaker inequalities needed by vertices in \(P\) and \(R\). This proves the defensive-alliance classification.

For domination, an unselected vertex \(a_i\) fails to be dominated exactly when the selected \(B\)-indices are contained in \(\{i\}\). Thus every unselected \(A\)-vertex is dominated once \(|B_S|\ge2\), and symmetrically every unselected \(B\)-vertex is dominated once \(|A_S|\ge2\). When \(n\ge5\), \(q\ge2\), so either defensive case forces both \(|A_S|\) and \(|B_S|\) to be at least two. Hence every defensive alliance is global.

For the small values \(n=3,4\), one has \(q=1\). If \(c=0\), a side containing exactly one selected vertex leaves its matched opposite vertex undominated, so globality requires \(p,r\ge2\); for \(n=3\) this is impossible. If \(c>0\), the defensive inequalities already give \(|A_S|,|B_S|\ge2\), so domination is automatic. Summing the corresponding multinomial state counts gives the two displayed exceptional polynomials.

For connectedness when \(n\ge5\), if \(c=0\) then \(G[S]\cong K_{p,r}\), because the selected index sets are disjoint. If \(c>0\), then \(|A_S|,|B_S|\ge q+1\ge3\), and \(G[S]\) is a complete bipartite graph with a matching deleted. Such a graph is connected when both part sizes are at least three. Thus every defensive alliance is connected as well as global.

For \(n\ge5\), an index in \(P\) contributes one selected vertex, an index in \(R\) contributes one, an index in \(C\) contributes two, and an index in \(W\) contributes zero. The number of sets with fixed \((p,r,c,w)\) is
\[
\frac{n!}{p!\,r!\,c!\,w!}.
\]
Substituting the two exact feasibility conditions and \(w=n-p-r-c\) yields the displayed enumerator.

Finally, when \(c=0\), every feasible set has size at least \(2q\), and equality is attained by \(p=r=q\). When \(c>0\), the two inequalities imply
\[
|S|=(p+c)+(r+c)\ge2q+2,
\]
so the minimum for \(n\ge5\) is \(2q\). At equality the state counts are uniquely \(p=r=q\), \(c=0\), \(w=n-2q\), giving exactly
\[
\frac{n!}{q!^2(n-2q)!}
\]
minimum sets.

## Verification
The accompanying `verify.py` directly enumerates all \(2^{2n}\) vertex subsets for every \(3\le n\le9\). It independently tests the defensive inequality, domination, and induced connectivity from the graph definition; compares those tests with the four-state classification; compares the size counts with the closed multinomial formula and the two exceptional polynomials; and checks the minimum-value and minimum-count formulas. The finalized package replay returned:

`VERIFY_OK n_range=3..9 subset_checks=349504 defensive_sets=101028 global_sets=100972 connected_checks=100835 coefficient_checks=91 minimum_checks=7 max_order=18`

The computation verifies finite instances only. The infinite statement is established by the preceding proof.

## Relationship to prior work
Haynes, Hedetniemi, and Henning introduced the global defensive-alliance parameter and proved, for complete bipartite graphs with both part sizes at least two,
\[
\gamma_a(K_{r,s})=\left\lfloor\frac r2\right\rfloor+\left\lfloor\frac s2\right\rfloor.
\]
Their full paper explicitly treats complete and complete bipartite graphs but contains no crown-graph or deleted-perfect-matching result. The present theorem gives the exact set-level classification after deleting a perfect matching from \(K_{n,n}\), not merely a bound or scalar minimum.

The later defensive-alliance-polynomial paper gives a bivariate polynomial for connected induced subsets and computes it for complete bipartite graphs among several standard classes. Its searchable full text has no occurrence of “crown” or “perfect matching.” The object there is also not the same as the global defensive-alliance size enumerator defined here. For \(n\ge5\), the present automatic-globality theorem explains why the crown family is a particularly clean bridge between the defensive and global notions.

The closest internal comparison results found concerned strong defensive alliances of complete multipartite graphs and global offensive alliances of complete multipartite graphs. Neither applies: a crown graph is not complete multipartite for \(n\ge3\), and both the alliance inequality and the side on which it is imposed differ from the present defensive-global statement.

## Limitations
The novelty claim is the exact crown-graph classification, enumerator, automatic-globality/connectedness theorem, minimum count, and parity-sensitive comparison with \(K_{n,n}\). It does not claim to introduce defensive alliances, global alliances, or the later defensive-alliance polynomial. The literature search cannot exclude every unindexed or differently titled source; crown graph, complete bipartite graph minus a perfect matching, complete bipartite graph minus a one-factor, and bipartite Kneser \(H(n,1)\) aliases were checked. The exact public-date anchor used here is the paper's stated publication date, \(2003\)-\(12\)-\(08\); its earlier submission date is not treated as evidence of public availability.

## References
1. T. W. Haynes, S. T. Hedetniemi, and M. A. Henning, “Global defensive alliances in graphs,” *Electronic Journal of Combinatorics* 10 (2003), R47. DOI: 10.37236/1740. The paper states “Submitted: Jan 18, 2002; Accepted: Nov 26, 2003; Published: Dec 8, 2003” and lists MR Subject Classifications 05C69 and 05C05.
2. H. Ibrahim, “Defensive alliance polynomial,” arXiv:1811.10089 (2018). The paper defines the bivariate defensive-alliance polynomial and includes complete bipartite graphs among its computed classes.
