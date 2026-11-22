# Full clique and maximal-clique spectra of rank-one Boolean relation semigroups

## Finding
Let \(\mathcal R_n=\{0\}\cup\{X_{A,B}:\varnothing\ne A,B\subseteq[n]\}\), with \(X_{A,B}=A\times B\) regarded as a Boolean matrix and multiplied by relational composition. For any \(n\ge1\), let \(c_n(k,j)\) count unordered sets of pairwise-distinct, pairwise-commuting, nonzero rank-one relations containing exactly \(k\) idempotents and \(j\) square-zero elements. The empty set is counted with \(c_n(0,0)=1\).

Write \(s(j,h)\) for the **signed** Stirling numbers of the first kind, defined by \(s(0,0)=1\) and \(s(j,h)=s(j-1,h-1)-(j-1)s(j-1,h)\). Set
\[
F_n(k,h)=\sum_{a=0}^{h}\sum_{b=0}^{h}\sum_{c=0}^{k}(-1)^{a+b+c}\binom ha\binom hb\binom kc
\bigl(2^{k+h-a}+2^{k+h-b}+k-c-1\bigr)^n.
\]
Then the **complete idempotent/square-zero refined clique polynomial** is determined coefficientwise by
\[
\boxed{c_n(k,j)=\frac1{k!j!}\sum_{h=0}^{j}s(j,h)F_n(k,h).}
\]
All indices \(k,j\) are nonnegative; the formula vanishes for unattainable sizes. Its unrefined specialization is \(P_n(z)=\sum_{k,j\ge0}c_n(k,j)z^{k+j}\).

The **complete inclusion-maximal clique-size polynomial** has the following independent closed form. Let \({p\brace k}\) denote Stirling numbers of the second kind, with \({0\brace0}=1\), and define
\[
W(k,\ell,r)=\begin{cases}
2^{k(\ell+r)},&\ell\ge1,\ r\ge1,\\
(2^k-1)^{\ell+r},&\ell r=0,\ k\ge1,\\
0,&\ell r=0,\ k=0.
\end{cases}
\]
Then, for \(n\ge1\),
\[
\boxed{M_n(z)=\sum_{\ell+r+p=n}\binom{n}{p,\ell,r}
\sum_{k=0}^{p}{p\brace k}\,W(k,\ell,r)\,
 z^{k+(2^\ell-1)(2^r-1)}.}
\]
We use \(\binom{n}{p,\ell,r}=n!/(p!\ell!r!)\). Here \(M_n(z)\) records all inclusion-maximal cliques of the induced commuting graph on **every** nonzero rank-one Boolean relation, not only its idempotent vertices.

Every clique \(C\) corresponds bijectively to the commutative subsemigroup \(\{0\}\cup C\) of \(\mathcal R_n\); the maximal cliques correspond to maximal commutative subsemigroups **among subsemigroups containing zero**. Every maximal commutative subsemigroup of \(\mathcal R_n\) contains zero, because zero can always be adjoined, so these are precisely the maximal commutative subsemigroups of \(\mathcal R_n\). (The statement about maximality is inside \(\mathcal R_n\), not the entire semigroup of binary relations.)

For example,
\[
M_4(z)=29z+235z^2+254z^3+193z^4+8z^7+6z^9.
\]
Thus there are precisely \(725\) maximal cliques on the \(225\) nonzero rank-one relations when \(n=4\); clique sizes five, six, and eight do not occur among maximal cliques. The total number of cliques including the empty one is \(6042\).

## Assumptions and scope
All sets are labelled, and \(n\ge1\). Boolean matrix multiplication uses logical OR and AND. A nonzero rank-one Boolean matrix is a unique rectangle \(A\times B\) with \(A,B\ne\varnothing\). The graph vertex set comprises **all** these rectangles; the zero relation is not a vertex. A clique consists of pairwise-distinct vertices; an inclusion-maximal clique cannot be enlarged by another nonzero rank-one relation commuting with all its vertices. The variables \(k\) and \(j\) classify the vertex squares: \(X^2=X\) or \(X^2=0\). Both classes are counted, including mixed cliques.

## Proof
**Products and commutation.** For nonempty \(A,B,C,D\subseteq[n]\), multiplication is
\[
X_{A,B}X_{C,D}=\begin{cases}X_{A,D},&B\cap C\ne\varnothing,\\0,&B\cap C=\varnothing.\end{cases}
\]
Hence \(X_{A,B}\) is idempotent if and only if \(A\cap B\ne\varnothing\), and is square-zero otherwise. Two *distinct* rectangles commute exactly when \(B\cap C=\varnothing\) and \(D\cap A=\varnothing\): if both products are nonzero and equal, the uniqueness of rectangle supports gives \(A=C\) and \(B=D\), contradicting distinctness. If only one product is zero, they are unequal. Thus all products of distinct members of a clique are zero. Squares lie in \(\{0\}\cup C\), proving the claimed clique-to-subsemigroup correspondence. When \(n\ge2\), zero belongs to every maximal commutative subsemigroup because it can always be adjoined.

**Counting temporarily labelled cliques.** Give distinct names to \(k\) idempotent vertices and \(h\) square-zero vertex *positions*, initially allowing the latter positions to repeat the same rectangle. At any coordinate \(x\in[n]\), let \(I_A(x)\) and \(I_B(x)\) be the labels whose rectangles include \(x\) in the left and right support, respectively. Commutation between distinct labelled vertices, and the square-zero condition for a nilpotent label, imply precisely these coordinate types: (i) no membership; (ii) any nonempty collection of left labels only; (iii) any nonempty collection of right labels only; (iv) simultaneous left-and-right membership in exactly one idempotent label. The corresponding alphabet has cardinality \(2^{k+h+1}+k-1\).

To ensure every idempotent position is genuinely idempotent, require the private overlap symbol of each of the \(k\) labels to occur at least once. To ensure every nilpotent position is a nonzero relation, require its left support and right support each to occur at least once. Inclusion–exclusion on \(a\) absent nil-left labels, \(b\) absent nil-right labels and \(c\) absent private overlap symbols leaves
\[
2^{k+h-a}+2^{k+h-b}+k-c-1
\]
coordinate symbols. Taking its \(n\)-th power and summing the inclusion–exclusion signs gives \(F_n(k,h)\). Idempotent positions cannot coincide, since their private overlap sets are nonempty and disjoint. Nil positions can coincide, so this counts weakly distinct nil labels.

**Recovering distinct nil vertices.** The set of equalities among \(j\) ordered nil labels is a set partition. Its Möbius function from a partition of \(j\) labels into \(h\) blocks to the discrete partition sums to the signed Stirling coefficient \(s(j,h)\) when summed over all partitions with \(h\) blocks. Each merged block is one nil label and has exactly \(F_n(k,h)\) admissible assignments; hence the number of ordered tuples with *distinct* nil vertices equals \(\sum_hs(j,h)F_n(k,h)\). The idempotent and nil classes are disjoint by their squares, and every unordered clique has exactly \(k!j!\) labellings. This proves the displayed coefficient formula.

**Maximal cliques.** Given a clique \(C\), define the aggregate left and right support sets \(U=\bigcup_{X_{A,B}\in C}A\) and \(V=\bigcup_{X_{A,B}\in C}B\). If \(U\cup V\ne[n]\), a singleton diagonal rectangle on any unused coordinate commutes with every member of \(C\), so \(C\) is not maximal. Conversely, if \(U\cup V=[n]\), a new, distinct rectangle commuting with all of \(C\) must have its left support contained in \([n]\setminus V=U\setminus V=:L\) and its right support contained in \([n]\setminus U=V\setminus U=:R\). It must therefore be a square-zero rectangle \(A\times B\) with \(\varnothing\ne A\subseteq L\), \(\varnothing\ne B\subseteq R\). These rectangles commute mutually and with every member of \(C\). Consequently \(C\) is maximal exactly when \(U\cup V=[n]\) and it contains **all** \((2^{|L|}-1)(2^{|R|}-1)\) such rectangles.

Write \(p=|U\cap V|\), \(\ell=|L|\), \(r=|R|\), so \(p+\ell+r=n\). A coordinate of \(U\cap V\) can belong in both supports only of one idempotent, and must do so; thus those \(p\) coordinates split into \(k\) nonempty privately labelled idempotent roots. For unlabelled idempotents, this gives \({p\brace k}\) ways. Each coordinate of \(L\) is included independently in any subset of the \(k\) idempotents' left supports, and each coordinate of \(R\) in any subset of their right supports. If \(\ell,r>0\), the mandatory complete family of nil rectangles already covers both sets, so all \(2^{k(\ell+r)}\) decorations are allowed. If \(\ell r=0\), no nil rectangle exists and every coordinate on the remaining one-sided set must occur in at least one idempotent support; there are \((2^k-1)^{\ell+r}\) decorations when \(k\ge1\). There is no maximal clique with \(k=0\) and \(\ell r=0\) when \(n\ge1\). Choosing the labelled disjoint sets \(U\cap V,L,R\) contributes the multinomial coefficient. Every maximal clique has one and only one such description, proving \(M_n(z)\).

## Verification
Run the standalone Python standard-library checker with \(\texttt{python3 verify.py}\). It independently constructs each Boolean matrix as actual row bitmasks, multiplies all pairs directly (rather than using the support-based commutation characterization), constructs the adjacency graph, enumerates all cliques by recursive increasing-vertex expansion, tests maximality against the **full graph**, and compares every nonzero bivariate clique coefficient and every maximal clique-size coefficient with the two formulas. Cases \(1\le n\le4\) are exhaustive. The results are:

| \(n\) | Nonzero rank-one vertices | All cliques, including empty | Maximal cliques | Possible maximal sizes |
|---|---:|---:|---:|---|
| 1 | 1 | 2 | 1 | \(1\) |
| 2 | 9 | 11 | 8 | \(1,2\) |
| 3 | 49 | 123 | 65 | \(1,2,3\) |
| 4 | 225 | 6042 | 725 | \(1,2,3,4,7,9\) |

Expected last line: \(\texttt{VERIFY_OK}\). The finite enumeration independently corroborates small cases only; validity for every \(n\) follows from the bijective counting and maximality arguments.

## Relationship to prior work
The Boolean matrix-semigroup and rank-one rectangle multiplication are classical (Kim–Roush, 1981). Dolžan–Kokol Bukovšek–Oblak (arXiv 2010) examine diameters in full matrix-semiring commuting graphs, not these clique distributions. Paulista's 2025 completely \(0\)-simple Rees matrix analysis covers general commutation criteria and **clique numbers**: the maximum-size statement alone is not asserted as a new contribution here. A published result titled *Clique and maximal-clique enumerators for rank-one idempotent Boolean relations* gives the complete enumerators on the idempotent-only induced subgraph. Its all-clique coefficients are exactly the \(j=0\) specialization of our first formula, but its maximal-clique result concerns maximality only **within the smaller idempotent vertex set** and is not the displayed polynomial \(M_n\). The new claims are the full joint mixed idempotent/square-zero enumeration, the classification of maximal families in the complete rank-one semigroup, and their complete maximal-clique size spectrum.

## Limitations
The result concerns the rank-at-most-one Boolean-relation semigroup, not the entire monoid of arbitrary binary relations. The graph includes all nonzero rank-one relations; the zero relation is adjoined only for the semigroup correspondence. The formula is finite and explicit but not an asymptotic closed form. An earlier general all-clique enumerator for arbitrary Rees \(0\)-matrix semigroups may subsume this specialization; accessible relevant treatments and published records inspected here do not establish such coverage. A prior-idempotent specialization and general clique-number arguments are acknowledged. Independent proof and literature-priority assessment remain unperformed.

## References
1. K. H. Kim and F. W. Roush, *The algebraic structure of the semigroup of binary relations on a finite set*, Glasgow Mathematical Journal **22** (1981), 57–68, https://doi.org/10.1017/S0017089500004468.
2. D. Dolžan, D. Kokol Bukovšek and P. Oblak, *Diameters of commuting graphs of matrices over semirings*, arXiv:1012.5505v1 (first posted 2010-12-26), https://arxiv.org/abs/1012.5505.
3. T. Paulista, *Commuting graphs of completely 0-simple semigroups*, arXiv:2510.23871v1 (first posted 2025-10-27), https://arxiv.org/abs/2510.23871. See the clique-number results in Section 5.
4. *Clique and maximal-clique enumerators for rank-one idempotent Boolean relations*, published result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-clique-and-maximal-clique-enumerators-for-rank-one-idempotent-bo--a2f16599b2ee.
