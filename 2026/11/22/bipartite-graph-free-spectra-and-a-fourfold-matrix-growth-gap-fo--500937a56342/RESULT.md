# Bipartite-graph free spectra and a fourfold matrix growth gap for a six-element semiring

## Finding
Let \(S=\{\infty,\omega,a,b,c,d\}\) be the six-element additively idempotent semiring from Jiao (2026): addition is the join operation of the three chains \(b<d<\infty\), \(c<a<\infty\), and \(\omega<\infty\), with no other nontrivial comparisons, and multiplication is commutative, with \(ab=bc=cd=\omega\) and all other products equal to \(\infty\). Work in the constant-free signature \((+,\cdot)\). For a variety \(\mathcal V\), write \(f_{\mathcal V}(r)\) for the cardinality of its relatively free algebra on \(r\ge1\) generators. Let \(B_n\) be the number of simple bipartite graphs on \(n\) specified labelled vertices, including isolated vertices; \(B_0=1\).

**Theorem.** For every integer \(r\ge1\) and every matrix size \(k\ge2\),
\[
 f_{\mathsf V(S)}(r)=\sum_{\ell=0}^r\binom r\ell B_{r-\ell},\qquad
 f_{\mathsf V(M_k(S))}(r)=\sum_{\ell=0}^r\binom r\ell 2^{(r-\ell)^2}.
\]
The second formula is a direct count using Jiao's previously proved ordered-quadratic normal forms and separation lemma, not an independently claimed discovery. The new scalar formula arises from an exact bijection between nonabsorbing scalar term functions and pairs consisting of a chosen set of linear variables and a bipartite graph on the remaining labelled variables. The ratio of logarithmic free spectra is sharp:
\[
 \log_2 f_{\mathsf V(S)}(r)=\frac{r^2}{4}+O(r),\qquad
 \log_2 f_{\mathsf V(M_k(S))}(r)=r^2+o(1),\qquad
 \lim_{r\to\infty}\frac{\log_2 f_{\mathsf V(M_k(S))}(r)}{\log_2 f_{\mathsf V(S)}(r)}=4.
\]
In addition, the scalar free-spectrum exponential generating function has the explicit bipartite-graph square-root form
\[
 \sum_{r\ge0}F_r\frac{z^r}{r!}
 =e^z\left(\sum_{n\ge0}\frac{z^n}{n!}\sum_{j=0}^n\binom nj 2^{j(n-j)}\right)^{1/2},
\]
where \(F_0=1\) is a formal generating-function convention and \(F_r=f_{\mathsf V(S)}(r)\) for \(r\ge1\); no nullary free algebra is asserted.

## Assumptions and scope
The signature consists of binary addition and multiplication only; there are no distinguished constants. The element \(\infty\) is the greatest additive element and the common value of every product of three factors. The equalities of term functions are tested on all assignments from \(S\) or \(M_k(S)\), respectively. The stated values are finite because each term admits a bounded-degree normal form. The bipartite graphs are simple, undirected, labelled, and may be disconnected or have isolated vertices. The matrix result uses the ordinary full matrix semiring with entrywise addition and matrix multiplication. Its complete ordered-word separation is attributed to Jiao's Lemmas 4.5–4.6.

## Proof
**1. Reduction to linear-plus-graph expressions.** Distribute any term into a finite sum of monomials. In \(S\), any monomial of length at least three is the constant term function \(\infty\), which absorbs every additive summand. The same is true if a squared variable appears, since every square is \(\infty\). If a variable \(x\) appears both as a linear summand and as a factor of any quadratic summand \(xy\), then the identity \(x+xy=\infty\) reduces the whole polynomial to the absorbing function. Idempotence removes repeated terms and commutativity identifies \(xy\) with \(yx\). Consequently every term function is either absorbing or represented by
\[
 P_{L,G}=\sum_{x\in L}x+\sum_{\{u,v\}\in E(G)}uv,
\]
where \(L\) is a subset of the \(r\) generators, \(G\) is a simple undirected graph on the complementary generators, and \(L\) and \(E(G)\) are not both empty. An empty sum is omitted, not interpreted as a constant; for the zero-support case the absorbing term is represented by a cube.

**2. Exact nonabsorbing criterion.** Products can equal \(\omega\) precisely for pairs of labels linked by the path \(a-b-c-d\); otherwise the product is \(\infty\). If \(G\) has an odd cycle, no assignment of its vertices to this path can make every edge product \(\omega\), because the path is bipartite. Thus some quadratic summand is always \(\infty\) and \(P_{L,G}\) is the absorbing function. Conversely, if \(G\) is bipartite, assign its two color classes to \(b,c\), and assign each variable in \(L\) to \(\omega\). Every summand evaluates to \(\omega\), so \(P_{L,G}\) is not absorbing. This handles disconnected graphs, empty graphs and isolated vertices.

**3. Distinct linear supports.** Let \(P_{L_1,G_1}\) and \(P_{L_2,G_2}\) be nonabsorbing with \(L_1\ne L_2\). Reverse indices if needed and select \(x\in L_1\setminus L_2\). Properly color \(G_2\) by \(b,c\), and put all variables of \(L_2\) at \(\omega\). The second polynomial evaluates to \(\omega\). Because \(x\notin L_2\), its value is \(b\) or \(c\). The first polynomial contains \(x\), so its value is at least \(x\) in the additive order and cannot be \(\omega\), which is incomparable with \(b,c\). Hence the functions differ.

**4. Distinct edge supports.** Let \(L_1=L_2=L\) and \(G_1\ne G_2\); choose an edge \(xy\) of \(G_1\setminus G_2\), reversing roles if needed. We construct a graph homomorphism from the bipartite graph \(G_2\) to the four-vertex path \(a-b-c-d\) sending \(x,y\) to nonadjacent path vertices. If \(x,y\) lie in separate connected components, orient their independent bipartite two-colorings to send both to \(b\). If they belong to the same bipartition class, an ordinary \(b,c\) coloring sends both to \(b\). Otherwise they lie in opposite bipartition classes of the same component and, since \(xy\notin E(G_2)\), have odd graph distance at least three. Let \(d(v)\) be graph distance from \(x\). Send distances \(0,1,\text{even}\ge2,\text{odd}\ge3\) to \(a,b,c,d\), respectively. Every edge connects distances differing by exactly one (bipartiteness excludes equal distance); the assigned labels are adjacent in the path. In particular \(x\mapsto a\) and \(y\mapsto d\), which are not adjacent. Color the other components by \(b,c\). Set every variable in \(L\) to \(\omega\). Then every edge in \(G_2\) evaluates to \(\omega\), whereas \(xy\) in \(G_1\) evaluates to \(\infty\). Thus the two polynomials differ. This proves injectivity of the graph parametrization.

**5. Cardinality and generating functions.** For each \(\ell\), choose the linear-support set \(L\) in \(\binom r\ell\) ways, then a labelled bipartite graph on its \(r-\ell\) remaining vertices in \(B_{r-\ell}\) ways. Exclude the empty \(L\), empty-graph case, but include the one absorbing term function: these two adjustments cancel. This proves the scalar formula. For the matrix variety, Jiao's Lemmas 4.5–4.6 already establish that distinct ordered quadratic supports \(E\subseteq ([r]\setminus L)^2\) give distinct nonabsorbing functions, even with loops, and the same empty-case cancellation gives the stated matrix formula.

A labelled bipartite graph with a chosen proper two-coloring on \(n\) vertices is counted by \(T_n=\sum_{j=0}^n\binom nj 2^{j(n-j)}\). Every connected bipartite graph has exactly two proper colorings, so the exponential-formula identity \(T(z)=B(z)^2\) holds, where \(B(z)=\sum_{n\ge0}B_n z^n/n!\). Choosing \(L\) independently multiplies the exponential generating function by \(e^z\), proving the square-root formula.

**6. Sharp growth ratio.** Fix a balanced partition of \([r]\) to obtain \(B_r\ge 2^{\lfloor r^2/4\rfloor}\). Assigning an ordered bipartition to a labelled bipartite graph gives \(B_n\le2^n 2^{\lfloor n^2/4\rfloor}\). Therefore
\[
 2^{\lfloor r^2/4\rfloor}\le f_{\mathsf V(S)}(r)
 \le \sum_{\ell=0}^r\binom r\ell 2^{r-\ell}2^{\lfloor(r-\ell)^2/4\rfloor}
 \le3^r2^{\lfloor r^2/4\rfloor}.
\]
For matrix spectra, the term \(\ell=0\) is \(2^{r^2}\), and
\[
 1\le\frac{f_{\mathsf V(M_k(S))}(r)}{2^{r^2}}
 \le\sum_{\ell=0}^r\binom r\ell 2^{-r\ell}
 =(1+2^{-r})^r\longrightarrow1,
\]
using \((r-\ell)^2-r^2\le-r\ell\). Taking logarithms yields the announced limits.

## Verification
A standalone pure-Python checker `verify_free_spectrum.py` derives \(B_n\) through degree eight by exact binomial convolution and agrees with independent exhaustive enumeration of all labelled simple graphs through five vertices. For ranks one through four it evaluates every regular commutative normal form on all \(6^r\) scalar assignments, detects exactly the odd-cycle collapse to the absorbing term function, and asserts that all bipartite representatives are pairwise distinct. It reproduces the following values (the second column is scalar, the third is matrix):

| \(r\) | \(f_{\mathsf V(S)}(r)\) | \(f_{\mathsf V(M_k(S))}(r)\) |
|---:|---:|---:|
|1|2|3|
|2|5|21|
|3|17|567|
|4|86|67689|
|5|677|33887403|
|6|8225|68921796861|
|7|149102|563431696713567|
|8|3917681|18451249599365935569|

These checks are finite corroboration only; the arguments above prove the statements for all ranks.

## Relationship to prior work
Jiao, arXiv:2611.14551v1 (posted 2026-11-01), defines precisely the semiring used here (Section 4.1), proves a size-independent finite identity basis for \(M_k(S)\), \(k\ge2\) (Theorem 4.3), and gives complete ordered-quadratic normal forms with separation (Lemmas 4.5–4.6). In particular the matrix free-spectrum formula above is implied by and directly counted from those already established lemmas; no priority is claimed for that part. Lyu, Ren and Yue, arXiv:2604.18588 (first posted 2026-03-14), establish a complete identity basis and the scalar variety's subvariety structure, including relevant path/bipartiteness phenomena; the theorem does not claim these identities or bipartiteness ideas as discoveries. The added result is the full labelled bipartite-graph parametrization of scalar term functions, its exact rank enumeration, and the derived sharp comparison with the matrix spectra. Jiao and Shao, arXiv:2609.32356, study free-algebra growth for a different upper-triangular Boolean matrix semiring. Neither that semiring nor its free-spectrum calculations are identified with \(S\). This explicit counting result may be implied in principle by older equational descriptions; the proof and comparison, not the underlying structural lemmas, are the contribution.

## Limitations
No nullary free-algebra claim is made. No formula for the finer automorphism group, multiplication table, or identity basis is claimed. The matrix spectrum is an already implied consequence of a primary-source lemma. The scalar graph count is exact, but the historical-priority assessment is based on the inspected papers and indexed searches rather than an exhaustive survey of all literature; an unindexed earlier free-spectrum computation may exist. This is a self-review; independent audit has not been performed.

## References
1. Jun Jiao, *Finite bases for matrix semirings: transfer theorems and nilpotent counterexamples*, arXiv:2611.14551v1, 2026-11-01. https://arxiv.org/html/2611.14551v1 . Sections 4.1–4.2, especially Theorem 4.3 and Lemmas 4.5–4.6.
2. Simin Lyu, Miaomiao Ren, Mengya Yue, *A new limit variety of additively idempotent semirings*, arXiv:2604.18588, initially submitted 2026-03-14; https://arxiv.org/abs/2604.18588 . Full-text sections on the six-element semiring, term identities, and bipartiteness.
3. Jun Jiao and Xiaolei Shao, *The finite basis problem for \(2\times2\) triangular Boolean matrix semirings and incidence semirings*, arXiv:2609.32356, 2026-09-26; https://arxiv.org/abs/2609.32356 . Section on different-semiring free-algebra growth.
