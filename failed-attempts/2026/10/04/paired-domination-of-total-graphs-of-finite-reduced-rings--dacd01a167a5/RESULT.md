# Paired domination of total graphs of finite reduced rings

## Finding

Let \(R\cong\prod_{i=1}^r F_i\) be a finite reduced commutative ring with identity that is not a field, where \(r\ge2\), and put \(q=\min_i|F_i|\). For the total graph \(T_\Gamma(R)\), the paired-domination number is the least even integer at least \(q\): \[\gamma_{\mathrm{pr}}(T_\Gamma(R))=\begin{cases}q,&q\text{ even},\\q+1,&q\text{ odd}.\end{cases}\] Consequently, together with the known formula \(\gamma_t(T_\Gamma(R))=q\), paired and total domination coincide exactly when the smallest field factor has even order. If all field factors have the same odd order \(q\), then the three standard parameters are strictly nested: \[\gamma(T_\Gamma(R))=q-1<\gamma_t(T_\Gamma(R))=q<\gamma_{\mathrm{pr}}(T_\Gamma(R))=q+1.\]

Thus, on finite reduced nonfields, paired domination is controlled only by the parity and size of the smallest field factor, even though the ordinary domination number has an additional exceptional case when all factors are equal odd fields.

## Assumptions and scope

A finite reduced commutative ring with identity is a finite product of finite fields. Write
\[
R\cong F_1\times\cdots\times F_r,
\qquad r\ge2,
\]
and reorder the factors so that
\[
q=|F_1|=\min_i|F_i|.
\]

The total graph \(T_\Gamma(R)\) has vertex set \(R\); distinct vertices \(x,y\) are adjacent exactly when
\[
x+y\in Z(R).
\]
In a product of fields this is equivalent to
\[
x_i+y_i=0
\]
for at least one coordinate \(i\).

A paired dominating set is a dominating set whose induced subgraph has a perfect matching. Every paired dominating set is total dominating, because each selected vertex is matched to an adjacent selected vertex.

## Proof

Let \(D\) be any total dominating set of \(T_\Gamma(R)\). For each coordinate let
\[
\pi_i(D)=\{d_i:d\in D\}\subseteq F_i.
\]
Suppose every \(\pi_i(D)\) is a proper subset of \(F_i\). Choose
\[
x_i\in F_i\setminus(-\pi_i(D))
\]
for every \(i\), and put \(x=(x_1,\ldots,x_r)\). Then for every \(d\in D\) and every coordinate \(i\),
\[
x_i+d_i\ne0.
\]
Hence \(x+d\) is a unit of \(R\), so \(x\) is adjacent to no vertex of \(D\). This contradicts total domination. Therefore
\[
\pi_i(D)=F_i
\]
for some \(i\), and consequently
\[
|D|\ge |F_i|\ge q.
\tag{1}
\]

Every paired dominating set is total dominating and has even cardinality. Equation (1) therefore gives
\[
\gamma_{\mathrm{pr}}(T_\Gamma(R))
\ge
2\left\lceil\frac q2\right\rceil.
\tag{2}
\]

For the matching upper bound, choose a second factor \(F_2\) after relabeling if necessary and define
\[
D_0=\{(a,0,\ldots,0):a\in F_1\}.
\]
Then \(|D_0|=q\). Any two distinct vertices of \(D_0\) are adjacent, because their second-coordinate sum is zero. Thus
\[
T_\Gamma(R)[D_0]\cong K_q.
\tag{3}
\]

The set \(D_0\) is total dominating. Indeed, for any \(x=(x_1,\ldots,x_r)\), choose
\[
d=(-x_1,0,\ldots,0)\in D_0.
\]
If \(x\ne d\), then \(x\) is adjacent to \(d\) through the first coordinate. If \(x=d\), choose any other vertex of \(D_0\), which is adjacent to \(x\) by (3).

If \(q\) is even, the clique in (3) has a perfect matching, so \(D_0\) is paired dominating and
\[
\gamma_{\mathrm{pr}}(T_\Gamma(R))\le q.
\]
Together with (2), this gives
\[
\gamma_{\mathrm{pr}}(T_\Gamma(R))=q.
\]

Now assume \(q\) is odd. Choose a nonzero element \(c\in F_2\) and set
\[
e=(0,c,0,\ldots,0).
\]
Then \(e\) is adjacent to the zero vector \(0\in D_0\), because their first-coordinate sum is zero. Match \(e\) with \(0\), and pair the remaining \(q-1\) vertices of the clique \(D_0\) arbitrarily. This gives a perfect matching on
\[
D_0\cup\{e\}.
\]
Because \(D_0\) already totally dominates the graph, the enlarged set is paired dominating. Hence
\[
\gamma_{\mathrm{pr}}(T_\Gamma(R))\le q+1.
\]
Equation (2) gives equality.

The published reduced-ring domination theorem states
\[
\gamma_t(T_\Gamma(R))=q,
\]
and
\[
\gamma(T_\Gamma(R))=
\begin{cases}
q-1,&\text{if all field factors have the same odd order }q,\\
q,&\text{otherwise}.
\end{cases}
\]
Combining that theorem with the paired formula above yields the stated parameter phase diagram.

## Verification

The standalone `verify.py` builds products of finite fields using only their additive groups, which is sufficient because adjacency in the total graph depends only on whether a coordinate sum is zero. For nine small field-order profiles it constructs the entire graph and exhaustively searches ordinary, total, and paired dominating sets through the theoretical optimum. It includes prime-power examples such as \(\mathbb F_4\).

It then checks the canonical clique witness and its odd-order one-vertex extension on seven additional profiles, including factors of orders \(8\) and \(9\).

Exact output:

```text
profile=(2, 2) vertices=4 gamma=2 gamma_t=2 gamma_pr=2
profile=(2, 3) vertices=6 gamma=2 gamma_t=2 gamma_pr=2
profile=(2, 4) vertices=8 gamma=2 gamma_t=2 gamma_pr=2
profile=(3, 3) vertices=9 gamma=2 gamma_t=3 gamma_pr=4
profile=(3, 4) vertices=12 gamma=3 gamma_t=3 gamma_pr=4
profile=(3, 5) vertices=15 gamma=3 gamma_t=3 gamma_pr=4
profile=(4, 4) vertices=16 gamma=4 gamma_t=4 gamma_pr=4
profile=(3, 3, 3) vertices=27 gamma=2 gamma_t=3 gamma_pr=4
profile=(5, 5) vertices=25 gamma=4 gamma_t=5 gamma_pr=6
VERIFY_OK
exhaustive_profiles=9
witness_only_profiles=7
projection_lower_bound=proved_symbolically_in_RESULT
```

The finite checks are corroborative. The arbitrary product theorem is the projection lower bound and explicit matching construction above.

## Relationship to prior work

Anderson and Badawi introduced the total graph of a commutative ring, with adjacency defined by zero-divisor sums. Their later work continued the structural study of this graph in commutative algebra.

Tamizh Chelvam and Asir studied domination and several domination variants in total graphs of commutative rings. Their 2013 full text computes ordinary domination in Artinian settings but does not introduce paired domination. Shariatinia, Maimani, and Yassemi subsequently sharpened the reduced-ring case: for a finite reduced nonfield with smallest field factor order \(q\), they prove the exact ordinary-domination formula and the total-domination value \(q\). Their full text contains no paired-domination result.

The present theorem determines the next natural matching-constrained parameter on the same reduced-ring class. The projection argument independently recovers the lower bound \(q\) for total domination, while parity and the canonical clique determine exactly when a perfect matching costs one additional vertex.

The general graph-theoretic notion of paired domination predates these ring-graph papers. Targeted searches using “paired domination,” “total graph,” “commutative ring,” “reduced ring,” and “product of fields,” together with semantic database searches under equivalent parameter formulations, did not locate the formula above.

## Limitations

The reduced hypothesis is essential to this proof because it identifies the ring with a product of fields and makes zero divisors exactly the tuples with a zero coordinate. Finite local nonfields have a different total-graph structure and are not covered by this theorem.

The formula determines only the smallest field order and its parity through this domination parameter; it does not reconstruct all field factors or the ring isomorphism type.

No claim is made for paired-domination polynomials or for nonreduced finite rings.

## References

1. D. F. Anderson and A. Badawi, “The total graph of a commutative ring,” *Journal of Algebra* 320 (2008), 2706–2719. DOI: 10.1016/j.jalgebra.2008.06.028. Available online 26 July 2008.
2. D. F. Anderson and A. Badawi, “On the total graph of a commutative ring without the zero element,” *Journal of Algebra and Its Applications* 12 (2012), 1250074. DOI: 10.1142/S0219498812500740. Published 30 July 2012; AMSC 13A15, 05C99.
3. T. Tamizh Chelvam and T. Asir, “Domination in the Total Graph of a Commutative Ring,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 87 (2013), 147–158.
4. V. Shariatinia, H. R. Maimani, and S. Yassemi, “Domination number of total graphs,” *Mathematica Slovaca* 66 (2016), 1527–1535. DOI: 10.1515/ms-2016-0241.
5. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206.
