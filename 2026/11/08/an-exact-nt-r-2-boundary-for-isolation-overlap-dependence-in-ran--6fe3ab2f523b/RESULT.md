# An exact \(nt=r^2\) boundary for isolation–overlap dependence in random uniform hypergraphs

## Finding
Let \(H\) be a uniformly random simple \(r\)-uniform hypergraph with vertex set \([n]\) and exactly \(m\) hyperedges. Let \(I\) be its number of isolated vertices, and let \(T_t\) be the number of **unordered pairs of distinct present hyperedges** whose intersection has exactly \(t\) vertices. Define
\[
N=\binom nr,\qquad M=\binom{n-1}r,\qquad u=2r-t,\qquad
K_t=\frac12\binom nr\binom rt\binom{n-r}{r-t}.
\]
For all integers \(r\ge3\), \(1\le t\le r-1\), \(n\ge\max\{r+2,2r-t\}\), and \(2\le m\le M\),
\[
\boxed{
\frac{\operatorname{Cov}(I,T_t)}{\mathbb EI\,\mathbb ET_t}
=\frac{(n-u)N(N-1)}{nM(M-1)}-1
=\frac{N\bigl[(nt-r^2)N+n(r-t)\bigr]}{n^2M(M-1)}.
}
\]
Both expectations are strictly positive, and hence
\[
\boxed{\operatorname{sgn}\operatorname{Cov}(I,T_t)=
\begin{cases}-1,&nt<r^2,\\+1,&nt\ge r^2.\end{cases}}
\]
The sign is independent of the prescribed number \(m\) of hyperedges. For every fixed \(r\ge3\) and \(1\le t\le r-2\), the nondegenerate admissible sequence of vertex orders undergoes exactly one sign reversal, from negative to positive, at \(n=\lceil r^2/t\rceil\). For \(t=r-1\), all nondegenerate admissible orders give positive covariance.

For example, at \(r=3,t=1\), the covariance is negative for \(n=5,6,7,8\) and positive for every \(n\ge9\), for each \(2\le m\le\binom{n-1}{3}\). Its normalized value is exactly \(-1/34\) at \(n=8\) and \(1/165\) at \(n=9\); thus the boundary order has strictly positive covariance. There is no zero-covariance nondegenerate case in the stated domain.

## Assumptions and scope
Hyperedges are unordered \(r\)-subsets of \([n]\), with no replacement; exactly \(m\) are selected uniformly from all \(N\) candidates. An isolated vertex belongs to no selected hyperedge. An overlap pair is counted once, not twice, and intersection size is **exactly** \(t\), not at least \(t\). The falling factorial is \((a)_{\underline j}=a(a-1)\cdots(a-j+1)\). The conditions imply \(u\le n\), \(M\ge2\), and positive expectations.

If \(m<2\) or \(n<2r-t\), then \(T_t=0\). If \(m>M\), every vertex has positive degree and \(I=0\). These degenerate regimes have zero covariance and are intentionally excluded from the strict sign statement. The theorem uses a fixed-edge, not an independent-edge, model.

## Proof
**1. Pair and vacancy counting.** Choose the first hyperedge in \(N\) ways. A second one intersecting it in exactly \(t\) vertices has \(\binom rt\binom{n-r}{r-t}\) choices. Division by two yields \(K_t\). An arbitrary fixed pair of distinct candidate edges is selected with probability \((m)_{\underline2}/(N)_{\underline2}\). An arbitrary fixed vertex is isolated with probability \((M)_{\underline m}/(N)_{\underline m}\). Therefore
\[
\mathbb EI=n\frac{(M)_{\underline m}}{(N)_{\underline m}},\qquad
\mathbb ET_t=K_t\frac{(m)_{\underline2}}{(N)_{\underline2}}.
\]

**2. Conditional factorization.** Every potential pair counted by \(T_t\) has a union of exactly \(u=2r-t\) vertices. By symmetry, the fraction of such pairs avoiding a specified vertex is \((n-u)/n\). Conditional on that vertex being isolated, the selected hyperedges form a uniformly chosen \(m\)-subset of the \(M\) candidate edges not containing it. Consequently
\[
\mathbb E(T_t\mid v\text{ isolated})=
K_t\frac{n-u}{n}\frac{(m)_{\underline2}}{(M)_{\underline2}}.
\]
Using \(I=\sum_v\mathbf1\{v\text{ isolated}\}\), multiplying this equation by the isolation probability, and subtracting the product of the expectations gives
\[
\operatorname{Cov}(I,T_t)=\mathbb EI\,\mathbb ET_t
\left(\frac{n-u}{n}\frac{N(N-1)}{M(M-1)}-1\right).
\]
As \(M=(n-r)N/n\), straightforward expansion of the numerator yields
\[
(n-u)N(N-1)-nM(M-1)
=\frac Nn\bigl[(nt-r^2)N+n(r-t)\bigr].
\]
This proves the displayed exact covariance identities, including the asserted independence of \(m\) after normalization.

**3. A finite binomial lower bound.** Put \(s=r-t\), so \(1\le s\le r-1\). For \(n\ge\max\{r+2,r+s\}\),
\[
\binom nr\ge ns.
\]
Indeed, \(\binom nr/n=\binom{n-1}{r-1}/r\) increases with \(n\). If \(s=1\), it is at least \((r+1)/2>1\). If \(s\ge2\), then \(n\ge r+s\) and unimodality of binomial coefficients gives
\[
\binom{n-1}{r-1}\ge\binom{r+s-1}{s}
\ge\binom{r+s-1}{2}\ge rs.
\]
The last inequality follows from \(r(r-3)+s(s-3)+2\ge0\) for \(r\ge3\), \(2\le s\le r-1\). Equality in the bound \(\binom nr\ge ns\) within the admissible domain can occur only at \((r,s,n)=(3,2,5)\).

**4. Strict sign.** Write \(B=(nt-r^2)N+ns\). If \(nt\ge r^2\), then \(B>0\). Otherwise, \(d=r^2-nt\) is a positive integer, so \(B=-dN+ns\le-N+ns\le0\) by Step 3. Equality would require \(d=1\) and \(N=ns\). The only possible equality case in Step 3 has \((r,t,n)=(3,1,5)\), for which \(d=4\), so \(B<0\). This proves strictness. Finally, for \(t\le r-2\), the admissible starting order lies strictly below \(r^2/t\), whereas every order at least \(\lceil r^2/t\rceil\) lies on the positive side. For \(t=r-1\) the first nondegenerate order is \(r+2=\lceil r^2/(r-1)\rceil\). The complete sign classification follows.

## Verification
The standalone Python 3 program `verify.py` uses `fractions.Fraction` and integer arithmetic. It enumerates entire fixed-edge hypergraph sample spaces for 29 small parameter combinations, including negative and positive \(3\)-uniform overlap cases, and compares three independently computed quantities: \(\mathbb EI\), \(\mathbb ET_t\), and \(\operatorname{Cov}(I,T_t)\). It also tests the exact finite formula and sign boundary over thousands of larger parameter combinations. The actual package replay passed 110337 exact arithmetic assertions, including 29 exhaustive finite sample spaces. Enumeration is corroboration, not proof for all orders; Steps 1–4 provide the infinite proof.

Reproduce in Python 3 from a directory containing this document and `verify.py` by running `python verify.py` (no external packages). No randomness or simulation is used.

## Relationship to prior work
The fixed-edge hypergraph model \(H_r(n,m)\) is standard and appears explicitly in Behrisch, Coja-Oghlan and Kang's 2007 arXiv manuscript (revised 2014), which derives limit theorems for the order and edge count of the giant component. The model and parameterization are reused here, but the new variables are **isolated-vertex count** and **pairs of hyperedges with a specified exact intersection size**. Their large-component limit theorems do not state this finite mixed-covariance identity or the arithmetic threshold.

López (2013) studies node-neighbor distributions in an independent-edge uniform-rank hypergraph, including combinatorics of overlapping hyperedges. Node-neighbor distributions for one vertex under independent edge sampling do not imply the present cross-statistic covariance under sampling a fixed number of hyperedges. The overlap counting ideas are related, but neither the fixed-edge conditioning nor the sign classification is present in the passages inspected.

A related model in which labeled left vertices select hyperedges independently (so duplicate selections are permitted) has a different sampling law. Even if that model gives a vanishing normalized covariance at a square order, the present without-replacement law can be strictly positive there: for \(r=3,t=1,n=9\), the ratio is \(1/165\), not zero. Conditional sampling without replacement is therefore a substantive hypothesis, not a relabeling of the independent-row calculation.

The joint moment formula itself follows from elementary fixed-size sampling. The asserted contribution is the exact **density-independent covariance phase diagram** at \(nt=r^2\), including strictness over all nondegenerate orders and the lack of a zero state. Broad subhypergraph-count identities may implicitly yield the initial mixed moment; historical priority of the sharpened all-parameter sign classification is not independently established.

## Limitations
The result applies only to simple uniform hypergraphs, to two-edge motifs with a fixed positive overlap \(1\le t\le r-1\), and to the uniform **without-replacement** fixed-edge ensemble. It does not assert the same threshold for multihypergraphs, nonuniform edge sizes, Bernoulli independent edges, or motifs with three or more hyperedges. No independent audit has occurred. Relevant broad counting literature may contain implicit equivalent formulas even when the exact threshold is not stated explicitly.

## References
1. M. Behrisch, A. Coja-Oghlan, and M. Kang, *Local Limit Theorems and Number of Connected Hypergraphs*, arXiv:0706.0497, first version 2007-06-04; https://arxiv.org/abs/0706.0497 .
2. E. López, *The distribution of the number of node neighbors in random hypergraphs*, arXiv:1302.2830, first version 2013-02-12; https://arxiv.org/abs/1302.2830 .
