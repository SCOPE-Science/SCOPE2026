# Idempotent-commutant rank polynomials recover the element orders of finite regular groups

## Finding

Let \(G\) be any finite group of order \(n\ge 1\), acting on its underlying set by left multiplication. Let \(\mathcal R(G)\) be the inverse monoid of restrictions of this regular action, including the empty partial map. The domain rank of a partial bijection \(s\) is \(\rho(s)=|\operatorname{dom}s|\). Define the idempotent-commutant rank polynomial, with ordered pairs and including the empty map, by
\[
P_G(y)=\sum_{e\in E(\mathcal R(G))}\sum_{s\in\mathcal R(G):\,es=se}y^{\rho(s)}.
\]
For an element \(g\in G\), write \(o(g)\) for its order, and for every divisor \(\ell\mid n\) write \(a_\ell(G)=|\{g\in G:o(g)=\ell\}|\). Then the exact identity for every \(n\) and every finite group is
\[
\boxed{P_G(y)=2^n(1+y)^n+\sum_{\substack{\ell\mid n\\\ell>1}}a_\ell(G)\left[\bigl((2+y)^\ell+y^\ell\bigr)^{n/\ell}-2^n\right].}
\]
The polynomial determines the entire element-order distribution of \(G\). More precisely, put
\[
H_{n,\ell}(y)=\bigl((2+y)^\ell+y^\ell\bigr)^{n/\ell}-(2+y)^n.
\]
For every divisor \(\ell>1\) of \(n\), the first nonzero coefficient is
\[
[y^\ell]H_{n,\ell}(y)=\frac n\ell 2^{n-\ell},\qquad [y^j]H_{n,\ell}(y)=0\quad(0\le j<\ell).
\]
Consequently the coefficients \(a_\ell(G)\) are recovered uniquely by triangular coefficient extraction in increasing order of \(\ell\). In particular, for finite groups of equal order the polynomials coincide if and only if the element-order histograms coincide. The degree of the polynomial is \(n\), so the group order itself is recovered as well.

For a cyclic group, this becomes the explicit divisor formula
\[
P_{C_n}(y)=2^n(1+y)^n+\sum_{\substack{\ell\mid n\\\ell>1}}\varphi(\ell)\left[\bigl((2+y)^\ell+y^\ell\bigr)^{n/\ell}-2^n\right].
\]
For even group orders, writing \(t(G)\) for the number of elements of order two, the ungraded total has the uniform asymptotic refinement
\[
P_G(1)=4^n+t(G)10^{n/2}+O\bigl(n\,28^{n/3}\bigr),
\]
as \(n\) tends to infinity through even group orders; the implicit constant is absolute.

## Assumptions and scope

A partial map is represented by its domain and its images. Multiplication is ordinary composition of partial maps (the choice of written order does not affect commutativity). For \(B\subseteq G\), the restriction of translation by \(g\) to \(B\) is \(s_{g,B}:B\to gB\), \(x\mapsto gx\). For nonempty \(B\), each such restriction identifies \(g\) uniquely: two distinct left translations disagree at every point. The empty restriction is a single zero map independent of \(g\). All idempotents of \(\mathcal R(G)\) are the partial identities \(e_A\), \(A\subseteq G\); their semilattice is the full Boolean lattice. No hypothesis of commutativity on \(G\) is imposed. The polynomial counts ordered pairs \((e,s)\), not unordered pairs or only nonzero maps.

## Proof

**Commutation criterion.** Fix \(A,B\subseteq G\), \(g\in G\), and set \(s=s_{g,B}\). The composite \(s\circ e_A\) has domain \(B\cap A\), while \(e_A\circ s\) has domain \(\{x\in B:gx\in A\}\). Both maps take their defined inputs \(x\) to \(gx\). Therefore
\[
e_As=se_A\quad\Longleftrightarrow\quad
(\forall x\in B)\ \bigl(x\in A\iff gx\in A\bigr).
\]

**Cycle calculation.** Suppose \(g\) acts as a cycle of length \(\ell\) on one orbit. Choosing \(B\) picks \(j\) of the \(\ell\) directed edges \(x\to gx\). If \(j<\ell\), the selected edges form a forest with \(\ell-j\) connected components, and the criterion requires membership in \(A\) to be constant on each component, giving \(2^{\ell-j}\) choices. For \(j=\ell\), the connected cycle permits exactly two choices of \(A\), not one. Hence the rank generating polynomial for pairs of restrictions and idempotent domains on one orbit is
\[
\sum_{j=0}^{\ell-1}\binom\ell j2^{\ell-j}y^j+2y^\ell=(2+y)^\ell+y^\ell.
\]
A nonidentity element of order \(\ell\) has \(n/\ell\) regular-action cycles of length \(\ell\). Choices on different cycles are independent, yielding the \(n/\ell\)-th power of the displayed polynomial.

**Empty-restriction correction.** For the identity \(g=1\), every domain \(B\) commutes with every partial identity, contributing exactly \(2^n(1+y)^n\). For each \(g\ne1\), all \(2^n\) choices of \(A\) with \(B=\varnothing\) describe a previously counted same zero map; subtract \(2^n\). For nonempty \(B\) uniqueness of the extending left translation ensures no other duplication. Grouping by orders proves the boxed identity, including \(n=1\).

**Reconstruction.** Subtract the universal baseline
\[
Q_G(y)=P_G(y)-2^n(1+y)^n-(n-1)\bigl((2+y)^n-2^n\bigr).
\]
Then \(Q_G(y)=\sum_{\ell\mid n,\,\ell>1}a_\ell(G)H_{n,\ell}(y)\). The binomial expansion
\[
H_{n,\ell}(y)=\sum_{j=1}^{n/\ell}\binom{n/\ell}{j}
(2+y)^{n-j\ell}y^{j\ell}
\]
shows that its \(y\)-adic valuation is exactly \(\ell\) and the leading coefficient is \((n/\ell)2^{n-\ell}\). Starting with the smallest divisor of \(n\) exceeding one, subtract the previously determined terms, and divide the coefficient at \(y^\ell\) by this strictly positive integer. This recursively gives every \(a_\ell(G)\), while \(a_1(G)=1\). Conversely the displayed polynomial plainly depends only on these counts. The coefficient of \(y^n\) is positive, so the degree equals \(n\). In \(\mathcal R(G)\), domain rank also equals the number of atoms of \(E(\mathcal R(G))\) below \(s^{-1}s\), so the statistic is intrinsic under abstract inverse-monoid isomorphism.

**Cyclic and asymptotic specializations.** The cyclic order count is \(a_\ell(C_n)=\varphi(\ell)\). At \(y=1\), a group element of order \(\ell\) contributes \((3^\ell+1)^{n/\ell}-2^n\) beyond the identity. The function \(x\mapsto(3^x+1)^{1/x}\) is strictly decreasing for \(x>0\), because \(\log(3^x+1)/x=\log3+\log(1+3^{-x})/x\) has negative derivative. The order-two contribution is \(10^{n/2}-2^n\); every order at least three contributes at most \(28^{n/3}\) in absolute value, and there are fewer than \(n\) such elements. The discarded \(2^n\) terms are absorbed in \(O(n28^{n/3})\), proving the uniform asymptotic formula.

## Verification

The independent direct-check script `verify.py` enumerates all partial restrictions as explicit tuples with an undefined symbol, and tests \(e_As=se_A\) by composing the actual partial maps, without relying on the derived commutation criterion. Its exhaustive cases are cyclic groups of orders one through seven, the Klein four-group, the symmetric group of degree three in its regular action, and the dihedral group of order eight in its regular action. It separately tests the coefficient-based recovery of element-order counts and the cyclic identities through order 150. Execution finished with `VERIFY_OK`. In particular,
\[
P_{C_4}(y)=16+160y+176y^2+96y^3+24y^4,
\]
whereas for the Klein four-group,
\[
P_{C_2\times C_2}(y)=16+160y+192y^2+112y^3+28y^4.
\]
These finite tests corroborate, but do not replace, the all-group proof.

## Relationship to prior work

Fernandes [1] defined and analyzed the cyclic inverse monoid of restrictions of a regular cyclic action, including its cardinality, rank, and presentations. Its construction and cardinality are prerequisites, not new results here. Fernandes and Paulista [2] studied restrictions of dihedral actions as partial isometries of cycle graphs and computed Green relations, cardinalities, and rank, but not the present idempotent-relative commutation polynomial. The new contribution is the all-finite-group commutation-rank formula and the triangular reconstruction of the element-order profile from this intrinsic monoid statistic. Standard cycle-index and centralizer techniques are acknowledged as relevant background. A general centralizer-enumeration or cycle-index theorem not located in the inspected primary materials could imply the counting identity, though the reconstruction statement is separately established.

## Limitations

The regular action is essential to uniqueness of the extending translation on a nonempty domain. The result does not apply verbatim to arbitrary faithful nonregular permutation actions or to all partial permutations. This invariant determines the element-order histogram, not necessarily the group isomorphism type. The asymptotic statement requires even group orders and is uniform as stated. Independent mathematical audit and comprehensive publication-priority certification have not been performed.

## References

[1] V. H. Fernandes, *On the cyclic inverse monoid on a finite set*, arXiv:2211.02155v1 (publicly available 2022-11-03); published in *Asian-European Journal of Mathematics* 17 (2024), 2450017. https://arxiv.org/abs/2211.02155

[2] V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196 (2022). https://arxiv.org/abs/2205.02196

[3] J. Konieczny, *Regular, inverse, and completely regular centralizers of permutations*, *Mathematica Bohemica* 128 (2003), 179–186. https://www.dml.cz/handle/10338.dmlcz/134038 (background and residual comparison risk; only publicly available abstract inspected).
