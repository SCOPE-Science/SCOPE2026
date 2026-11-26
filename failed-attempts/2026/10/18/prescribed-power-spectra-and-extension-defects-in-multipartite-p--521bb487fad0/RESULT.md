# Prescribed-power spectra and extension defects in multipartite partial-automorphism monoids

## Finding

**Theorem.** Let \(G=K_{n_1,\ldots,n_r}\) be the finite simple complete multipartite graph with \(r\ge1\) and positive part sizes \(n_i\), and let \(d\ge1\). A partial automorphism is an isomorphism between vertex-induced subgraphs. Define
\[
P_{G,d}(z)=\sum_{\substack{f\in\operatorname{PAut}(G)\\ f^d=\operatorname{id}_{\operatorname{dom}f}}}z^{|\operatorname{dom}f|}.
\]
For nonnegative \(s\) and positive \(e\), let \(T_s(e)\) be the number of permutations in \(S_s\) whose \(e\)-th power is the identity. Thus \(T_0(e)=1\), and for \(s\ge1\),
\[
T_s(e)=\sum_{\substack{1\le j\le s\\j\mid e}}\binom{s-1}{j-1}(j-1)!\,T_{s-j}(e).
\]
For \(s\ge1\), put \(W_{s,0}(d)=1\); for \(m\ge1\) define
\[
W_{s,m}(d)=\sum_{\substack{1\le \ell\le m\\\ell\mid d}}\binom{m-1}{\ell-1}(\ell-1)!\,(s!)^{\ell-1}T_s(d/\ell)W_{s,m-\ell}(d).
\]
Given a selection profile \(\mathbf a=(a_1,\ldots,a_r)\) with \(0\le a_i\le n_i\), set
\[
m_s(\mathbf a)=|\{i:a_i=s\}|\quad(s\ge1),\qquad
m_{s,t}(\mathbf a)=|\{i:a_i=s,\ n_i=t\}|\quad(s,t\ge1).
\]
Then the *complete prescribed-power rank polynomial* is
\[
\boxed{P_{G,d}(z)=\sum_{\mathbf a}z^{\sum_i a_i}\left(\prod_{i=1}^r\binom{n_i}{a_i}\right)\left(\prod_{s\ge1}W_{s,m_s(\mathbf a)}(d)\right).}
\]
Let \(E_{G,d}(z)\) count each such \(f\) only if it extends to an automorphism \(g\in\operatorname{Aut}(G)\) with \(g^d=1\). Then
\[
\boxed{E_{G,d}(z)=\sum_{\mathbf a}z^{\sum_i a_i}\left(\prod_{i=1}^r\binom{n_i}{a_i}\right)\left(\prod_{s,t\ge1}W_{s,m_{s,t}(\mathbf a)}(d)\right).}
\]
In particular, for involutions (allowing the identity), the obstruction to power-preserving global extension is sharp already at rank two:
\[
\boxed{[z^2]\bigl(P_{G,2}(z)-E_{G,2}(z)\bigr)=\sum_{\substack{1\le i<j\le r\\n_i\ne n_j}}n_i n_j.}
\]
Consequently \(P_{G,2}=E_{G,2}\) precisely when all original part sizes are equal (including the one-part case). These formulas count partial maps, not their possible global extensions, and apply for every positive \(d\) and every multipartite size profile.

## Assumptions and scope

All graphs are finite, simple and undirected; the parts of \(G\) are distinguished vertex subsets but the formulas are invariant under reordering them. We use composition of partial bijections with the empty partial map allowed. The identity \(\operatorname{id}_{\varnothing}\) contributes the constant coefficient one. The condition \(f^d=\operatorname{id}_{\operatorname{dom}f}\) is equality of partial maps; it is not a condition on an arbitrarily chosen extension of \(f\). Empty factors in finite products are one, and \(W_{s,m}(d)\) is only needed for \(s\ge1\). The polynomial \(E\) tests extension by *a global automorphism of order dividing \(d\)*, which is stronger than unrestricted extension.

## Proof

**1. Reduction to induced automorphism groups.** If \(f:U\to V\) is a partial bijection satisfying \(f^d=\operatorname{id}_U\), then for every \(u\in U\), \(f(u)\) is in the domain of the next iterate, so \(f(U)\subseteq U\). Finiteness and bijectivity imply \(f(U)=U\), so \(V=U\). Conversely, an automorphism of \(G[U]\) with \(d\)-th power the identity satisfies the partial-map equation. Therefore the count is a sum, over vertex subsets \(U\), of the numbers of \(d\)-torsion elements in \(\operatorname{Aut}(G[U])\).

**2. The selected-part decomposition.** Choose \(a_i=|U\cap V_i|\), where \(V_i\) is the original \(i\)-th independent part. There are \(\prod_i\binom{n_i}{a_i}\) such subsets. The nonadjacency equivalence classes in \(G[U]\) are precisely its nonempty selected parts. An automorphism may permute equal-size classes and independently permute elements inside each class, but cannot exchange classes of different selected sizes. Hence
\[
\operatorname{Aut}(G[U])\cong\prod_{s\ge1}(S_s\wr S_{m_s(\mathbf a)}).
\]
This remains true when there is just one nonempty selected class and when the domain is empty.

**3. Counting each wreath-product power equation.** A permutation of \(s\) points satisfies \(h^e=1\) exactly when each cycle length divides \(e\). Split by the length \(j\) of the cycle containing point one to obtain the recurrence for \(T_s(e)\). For \(S_s\wr S_m\), consider the outer permutation's cycle containing the first of the \(m\) classes. If its length is \(\ell\), the wreath element's \(d\)-th power can be the identity only if \(\ell\mid d\). On this cycle, the product \(h\in S_s\) of its \(\ell\) internal permutations must satisfy \(h^{d/\ell}=1\). Choose \(\ell-1\) internal permutations arbitrarily; the last is uniquely determined by the chosen cycle product. Thus the internal assignments number \((s!)^{\ell-1}T_s(d/\ell)\). Choosing and ordering the \(\ell-1\) other classes contributes \(\binom{m-1}{\ell-1}(\ell-1)!\); the remainder contributes \(W_{s,m-\ell}(d)\). Summation gives exactly the stated recurrence. Multiplying over selected sizes and summing the subset profiles proves \(P_{G,d}\).

**4. Power-preserving extension.** Every global automorphism of \(G\) permutes original independent parts only among parts of identical original size. A partial automorphism that stabilizes its domain can therefore extend globally only when its induced permutation of nonempty selected classes also preserves their original sizes \(n_i\). This is precisely the subgroup
\[
\prod_{s,t\ge1}(S_s\wr S_{m_{s,t}(\mathbf a)})
\]
of the selected-domain automorphism group. The condition is also sufficient while preserving the power equation: on any cycle of equal-original-size parts, extend the prescribed bijections between equal-size selected subsets to bijections of the full parts; choose the complementary bijections so that their ordered product around the cycle is the identity. Thus the resulting full permutation has \(d\)-th power the identity both on selected vertices (by the hypothesis on \(f\)) and on complementary vertices. Fix every unselected original part. Consequently each element of the displayed subgroup extends to a global \(d\)-torsion automorphism, and summing over selected profiles proves \(E_{G,d}\).

**5. Exact first obstruction.** Every partial identity extends. On any two-element domain the induced graph is an edge or two isolated vertices, each with an identity and one transposition. The transposition within one original part extends to a global involution, and a transposition between original parts of equal full size extends by interchanging those full parts. If the two vertices belong to original parts with different full sizes, the transposition cannot extend, since all graph automorphisms preserve full part sizes. There are exactly \(n_i n_j\) unordered such pairs from parts \(i,j\). Hence the displayed rank-two obstruction count and the homogeneous-versus-unequal-size dichotomy follow.

## Verification

The standalone Python 3 file `checker.py` evaluates the recurrences and independently enumerates all selected-domain permutations, checking the induced-graph adjacency relation and the \(d\)-th power. It also independently enumerates all global automorphisms of order dividing \(d\), restricts them to invariant domains, and compares the resulting exact sets with the extension-refined formula. In all 45 combinations of nine size profiles and \(d\in\{1,2,3,4,6\}\), both polynomial identities match brute force. An independent enumeration tests the symmetric-group recurrence for seven values \(0\le s\le6\) and eight values \(1\le d\le8\), covering 56 cases. The rank-two obstruction identity is checked in all nine profiles. The checker prints `ALL_EXACT_CHECKS_PASSED` and `POWER_PRESERVING_EXTENSION_CHECKS_PASSED`.

For example, the coefficients from rank zero upward for \(G=K_{3,2}\) and \(d=2\) are \((1,5,20,22,26,8)\), and for \(G=K_{2,2,2}\) they are \((1,6,30,56,66,36,20)\). The rank-two nonextension counts are respectively \(6\) and \(0\). More generally \(P_{G,1}(z)=(1+z)^{|V(G)|}\), since the only first roots of each partial identity are partial identities.

## Relationship to prior work

Jajcay, Jajcayová, Szakács and Szendrei (2018) establish that group \(\mathcal H\)-classes of the induced-subgraph partial-automorphism monoid are the automorphism groups of their domains; their paper studies inverse-monoid characterizations and Green relations, not the displayed prescribed-power and extension-refined enumerators. Chih and Plessas (2015/2017) treat graph-derived inverse semigroups and their idempotent/ideal structures. Gardiner's finite homogeneous-graph classification already includes complete multipartite graphs with equal part sizes; the all-equal-size boundary alone is not claimed as new. The present statement adds exact rank-wise counts for all positive powers and quantifies the complement through the explicit extension-defect polynomial and sharp rank-two coefficient.

The symmetric-group cycle recurrence, wreath-product structure and elementary orbit counting are standard ingredients; originality is assessed for the joint closed parameterized enumerators and the exact power-preserving extension defect, not for these ingredients separately.

## Limitations

This is a theorem for **complete multipartite** graphs only; arbitrary graphs need not admit such a selected-part decomposition. The polynomial counts roots of partial identities, not all elements of the inverse monoid (some partial maps have unequal domain and range). The verification is finite and is not a substitute for the all-size proof above. An independent audit has not been performed. Equivalent counts might exist in unindexed permutation-cycle or graph-monoid literature, and one relevant computational survey of partial graph automorphisms could not be inspected in full; this remains an originality risk.

## References

1. R. Jajcay, T. Jajcayová, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, first public preprint 2018-09-12, arXiv:1809.04422 (particularly Sections 3–6).
2. B. Chih and G. Plessas, *Graphs and Their Associated Inverse Semigroups*, arXiv:1506.02093 (2015), especially the definitions and idempotent semilattices.
3. A. Gardiner, *Homogeneous graphs and stability*, J. Austral. Math. Soc. 21 (1976), 371–375, DOI:10.1017/S144678870001867X (context for the previously known unrestricted extension criterion).
4. T. Jajcayová, *On Computational Aspects of Finding Inverse Monoids of Partial Automorphisms*, RIMS Kôkyûroku 2229 (2022); bibliographic entry and abstract available; full text not verified during this investigation.
