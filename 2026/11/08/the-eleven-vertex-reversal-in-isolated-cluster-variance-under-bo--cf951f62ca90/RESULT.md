# The eleven-vertex reversal in isolated-cluster variance under bond percolation on trees

## Finding

Let \(T\) be any tree on \(n\ge 3\) vertices. Retain each edge independently with probability \(1/2\), and let \(Z_T\) be the number of isolated vertices in the resulting random spanning subgraph (equivalently, the number of singleton percolation clusters). Write \(V(T)=\operatorname{Var}(Z_T)\).

**Sharp first reversal.** For every \(3\le n\le 10\), the star \(K_{1,n-1}\) uniquely minimizes \(V(T)\) among unlabeled \(n\)-vertex trees. For \(n=11\), the unique minimizer is the double star whose two adjacent central vertices have degrees \(5\) and \(6\). Its exact variance and the star variance are
\[
V(D_{5,6})=\frac{10239}{4096},\qquad
V(K_{1,10})=\frac{2632703}{1048576},\qquad
V(K_{1,10})-V(D_{5,6})=\frac{11519}{1048576}>0.
\]
Furthermore, for **every** \(n\ge11\), a balanced double star of order \(n\) has strictly smaller variance than the star. Thus order eleven is exactly the first order at which the star ceases to minimize isolated-cluster variance. No assertion about the globally minimizing shape for \(n\ge12\) is made.

## Assumptions and scope

Trees are finite, simple, connected, and unweighted. Edges are retained or removed independently with equal probabilities. Isolation refers to degree zero **after** edge retention; it does not refer to random deletion of whole vertices. Uniqueness of an extremal shape is up to graph isomorphism. The double star \(D_{a,b}\) has adjacent center vertices of degrees \(a,b\ge2\), with \(a-1\) and \(b-1\) pendant neighbors, hence exactly \(a+b\) vertices. The general non-minimality assertion uses \(a=\lfloor n/2\rfloor\), \(b=\lceil n/2\rceil\).

## Proof

**1. Exact variance for any finite simple graph.** For each vertex \(v\), let \(I_v\) indicate that all its incident edges are deleted, so \(Z_T=\sum_v I_v\). If \(d(v)\) is its degree, then \(\Pr(I_v=1)=2^{-d(v)}\). For nonadjacent vertices the incident edge sets are disjoint and the indicators are independent. For adjacent vertices \(u,v\), the single shared edge is required absent by both, giving \(\Pr(I_u=I_v=1)=2^{-(d(u)+d(v)-1)}\). Therefore
\[
\boxed{V(T)=\sum_{v\in V(T)}\bigl(2^{-d(v)}-4^{-d(v)}\bigr)+\sum_{uv\in E(T)}2^{-(d(u)+d(v)-1)}.}\tag{1}
\]
This formula is a direct second-moment identity, not itself claimed novel.

**2. Star and double-star formulas.** Summing (1) over degree-one leaves and the one center in a star gives
\[
V(K_{1,n-1})=\frac{n-1}{4}+\frac{n}{2^{n-1}}-\frac1{4^{n-1}}.\tag{2}
\]
Similarly, the double star has \(n-2\) leaves, one center-center edge, and \(a-1\) and \(b-1\) leaf-center edges, yielding
\[
V(D_{a,b})=\frac{n-2}{4}+\frac a{2^a}+\frac b{2^b}-\frac1{4^a}-\frac1{4^b}+\frac1{2^{n-1}},\qquad n=a+b.\tag{3}
\]
Putting \((a,b)=(5,6)\) in (2)–(3) proves the three exact rational values stated above.

**3. An infinite-order strict comparison.** Take balanced \(a,b\), with \(n\ge11\). The function \(k\mapsto k2^{-k}\) is strictly decreasing for integers \(k\ge2\). Because \(a,b\ge5\) and one of them is at least \(6\),
\[
\frac a{2^a}+\frac b{2^b}\le\frac5{2^5}+\frac6{2^6}=\frac14,\tag{4}
\]
with equality only at \(n=11\). Also the arithmetic-geometric mean inequality implies
\[
4^{-a}+4^{-b}\ge 2\sqrt{4^{-a-b}}=2^{1-n},\tag{5}
\]
with equality only when \(a=b\). Equations (3)–(5) prove \(V(D_{a,b})<(n-1)/4\), because the inequalities cannot both be equalities for \(n\ge11\). Equation (2) gives \(V(K_{1,n-1})>(n-1)/4\) for all \(n\ge3\). Hence every star of order at least eleven has a strictly better double-star competitor.

**4. Exhaustive finite boundary and uniqueness.** For \(3\le n\le11\), use the attached standalone `verify.py` to enumerate *all* unlabeled trees, not a sample. The enumeration starts with the one-vertex tree. From every representative of order \(m\), it attaches a new leaf to every one of its \(m\) vertices and then identifies isomorphic outputs using the canonical unrooted tree code. This is complete by induction: every tree with at least two vertices contains a leaf; deleting that leaf yields a smaller tree appearing in the preceding family, and reattaching it recreates the original tree. The code is isomorphism-complete because recursive rooted branch codes are canonical, and the center(s) of a tree are canonical under isomorphism. Thus deduplicating by the one-center code, or by the sorted pair of two-center rooted codes, neither loses nor spuriously merges a tree isomorphism class. This exhausts every finite order specified, not an arbitrarily bounded search within an infinite domain.

The code evaluates (1) with exact rational arithmetic and checks the unique minimizer and minimum for each order. For orders \(3,4,5,6,7,8,9,10,11\), the numbers of isomorphism classes are respectively \(1,2,3,6,11,23,47,106,235\). Every order through ten has precisely one minimizer, the star. At order eleven, precisely one tree has variance \(10239/4096\), namely \(D_{5,6}\), while every other tree has larger variance. Together with step 3, this proves the stated sharp first reversal and its unique eleven-vertex extremizer.

## Verification

Run `python3 verify.py` with Python 3 standard library. Its deterministic output ends `VERIFY_OK 18909 exact assertions / checks`. The checks include independent enumeration over all \(2^{n-1}\) retained-edge configurations for every tree through seven vertices, independent Prüfer-word enumeration of all labeled trees through seven vertices, comparisons with the pairwise-covariance formula, canonical unlabeled-tree enumeration through eleven vertices, and exact double-star inequalities through order one hundred. The proof of the all-order result is steps 1–3, not the finite numerical test. The all-orders minima beyond eleven are not inferred from computation.

## Relationship to prior work

Lanchier and La Salle (2021), arXiv:2111.01982, study first and second moments of the **size of a uniformly rooted percolation cluster** on finite regular graphs, using isolated-vertex events for a bound. Their Theorems 1 and 2 do not optimize the variance of the **total count of isolated clusters** over trees. Jevtić, Lanchier and La Salle (2020) study cluster-size moments on paths, rings and stars; those are distinct random variables from \(Z_T\). The present elementary variance identity is standard indicator covariance calculus. The asserted contribution is the sharp eleven-vertex extremal reversal, its unique eleven-vertex minimizer, and the strict witness at all larger orders. These comparisons establish no claim of absolute historical priority.

## Limitations

The finite minimum classification is a reproducible exact exhaustive computation, with a mathematical completeness proof for its tree generator. A second implementation could independently cross-check the canonical-code generator; the direct-edge enumeration provides independent checks of the variance formula, not of the entire isomorphism census. The manuscript does not classify global minimizers for order twelve or larger, other retention probabilities, or general connected graphs with cycles. Historical novelty cannot be established by failed indexing searches, and no independent mathematical audit has been performed.

## References

1. N. Lanchier and A. La Salle, *First and second moments of the size distribution of bond percolation clusters on regular graphs*, arXiv:2111.01982v1, publicly posted November 3, 2021. https://arxiv.org/html/2111.01982v1
2. P. Jevtić, N. Lanchier and A. La Salle, *First and second moments of the size distribution of bond percolation clusters on rings, paths and stars*, Statistics & Probability Letters 161 (2020), 108714. https://doi.org/10.1016/j.spl.2020.108714
3. P. N. Timonin, *Clusters' size-degree distribution for bond percolation*, arXiv:1704.07915, publicly posted April 25, 2017. https://arxiv.org/abs/1704.07915
