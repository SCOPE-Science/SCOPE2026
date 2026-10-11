# Paired-domination polynomials of finite-field unit dot-product graphs

## Finding

Let \(q>2\) be a prime power, put \(m=q-1\), and let \(UD(\mathbb F_q\times\mathbb F_q)\) be the unit dot-product graph. Define \[E_m(x)=\sum_{j\ge1}\binom{m}{2j}x^{2j},\qquad B_m(x)=\sum_{j=1}^{m}\binom{m}{j}^2x^{2j}.\] Let \(f(q)=1\) if \(q\) is even, \(f(q)=2\) if \(q\equiv1\pmod4\), and \(f(q)=0\) if \(q\equiv3\pmod4\). Then the paired-domination polynomial is \[D_{\mathrm{pr}}(UD(\mathbb F_q\times\mathbb F_q),x)=E_m(x)^{f(q)}B_m(x)^{(m-f(q))/2}.\] Consequently \[\gamma_{\mathrm{pr}}=m+f(q)=\begin{cases}q,&q\text{ even},\\q+1,&q\equiv1\pmod4,\\q-1,&q\equiv3\pmod4,\end{cases}\] and the number of minimum paired dominating sets is \[\binom{m}{2}^{f(q)}m^{m-f(q)}.\] The polynomial determines \(q\): in even characteristic its leading coefficient is \(m\) and its degree is \(m^2-1\), while in odd characteristic it is monic of degree \(m^2\). For \(q=2\), the graph is \(K_1\) and has no paired dominating set.

The formula comes from the self-orthogonal projective slopes. The classes fixed by the involution
\[
a\longmapsto -a^{-1}
\]
produce complete components, while the remaining classes occur in complete-bipartite pairs.

## Assumptions and scope

Let \(q>2\) be a prime power, let
\[
R=\mathbb F_q\times\mathbb F_q,
\]
and let \(UD(R)\) be the graph whose vertices are the units of \(R\), so every vertex is a pair
\[
(a,b)\in(\mathbb F_q^*)^2.
\]
Distinct vertices \((a,b)\) and \((c,d)\) are adjacent exactly when
\[
ac+bd=0.
\]

A paired dominating set is a dominating set whose induced subgraph has a perfect matching. Its counting polynomial is
\[
D_{\mathrm{pr}}(G,x)=\sum_k d_{\mathrm{pr}}(G,k)x^k.
\]

Put \(m=q-1\), and define
\[
E_m(x)=\sum_{j\ge1}\binom{m}{2j}x^{2j},
\qquad
B_m(x)=\sum_{j=1}^{m}\binom{m}{j}^2x^{2j}.
\]

## Proof

Every unit vector can be written uniquely as
\[
u(1,a),\qquad u,a\in\mathbb F_q^*.
\]
For a fixed slope \(a\), let
\[
X_a=\{u(1,a):u\in\mathbb F_q^*\}.
\]
Then \(|X_a|=m\). Two vertices in slope classes \(X_a\) and \(X_b\) are adjacent exactly when
\[
1+ab=0,
\]
that is,
\[
b=-a^{-1}.
\]
Thus the component structure is governed by the involution
\[
\iota(a)=-a^{-1}
\]
on \(\mathbb F_q^*\).

A fixed point satisfies
\[
a^2=-1.
\]
If \(q\) is even, then \(-1=1\) and Frobenius injectivity gives the unique solution \(a=1\). If \(q\) is odd, there are two fixed points when \(-1\) is a square, equivalently when \(q\equiv1\pmod4\), and none when \(q\equiv3\pmod4\). Hence the number of fixed slopes is
\[
f(q)=
\begin{cases}
1,&q\text{ even},\\
2,&q\equiv1\pmod4,\\
0,&q\equiv3\pmod4.
\end{cases}
\]
Each fixed slope gives a component \(K_m\), and each nonfixed two-cycle of \(\iota\) gives a component \(K_{m,m}\). Therefore
\[
UD(R)\cong f(q)K_m\;\sqcup\;\frac{m-f(q)}2K_{m,m}.
\tag{1}
\]

For \(K_m\), every nonempty vertex set dominates, and the paired condition is exactly that its cardinality be even. Thus
\[
D_{\mathrm{pr}}(K_m,x)=E_m(x).
\tag{2}
\]
For \(K_{m,m}\), a paired dominating set must meet both bipartition classes. If it takes \(j\) vertices from one side and \(k\) from the other, the induced \(K_{j,k}\) has a perfect matching exactly when \(j=k\). Hence
\[
D_{\mathrm{pr}}(K_{m,m},x)=B_m(x).
\tag{3}
\]

Paired domination is componentwise on a disjoint union: every component must be dominated internally, and a perfect matching cannot use edges between components. Multiplying (2) and (3) according to (1) yields
\[
D_{\mathrm{pr}}(UD(R),x)
=
E_m(x)^{f(q)}B_m(x)^{(m-f(q))/2}.
\]

The smallest exponent of both \(E_m\) and \(B_m\) is \(2\), so
\[
\gamma_{\mathrm{pr}}(UD(R))
=2f(q)+m-f(q)
=m+f(q).
\]
This is the stated three-case formula.

The coefficient of the minimum-degree term is obtained by taking two vertices in every clique component and one vertex from each side of every biclique component:
\[
[x^{m+f(q)}]D_{\mathrm{pr}}
=
\binom{m}{2}^{f(q)}(m^2)^{(m-f(q))/2}
=
\binom{m}{2}^{f(q)}m^{m-f(q)}.
\]

The total number of paired dominating sets is also explicit:
\[
D_{\mathrm{pr}}(UD(R),1)
=
(2^{m-1}-1)^{f(q)}
\left(\binom{2m}{m}-1\right)^{(m-f(q))/2}.
\]

Finally, the polynomial determines \(q\). If \(q\) is odd, then \(m\) is even, every component polynomial has leading coefficient \(1\), and the full graph itself is paired dominating, so the polynomial is monic of degree
\[
m^2.
\]
Hence \(m=\sqrt{\deg D_{\mathrm{pr}}}\). If \(q\) is even, then \(m\) is odd. The unique clique component can contribute at most \(m-1\) selected vertices, with coefficient \(m\), while every biclique can contribute all \(2m\) vertices. Therefore the polynomial has degree
\[
m^2-1
\]
and leading coefficient \(m\). In either case \(q=m+1\) is recovered.

For \(q=2\), \(UD(R)=K_1\), so no paired dominating set exists.

## Verification

The accompanying `verify.py` constructs the actual unit dot-product graphs for \(q=3\), \(q=4\), and \(q=5\). The \(q=4\) arithmetic is implemented directly in
\[
\mathbb F_2[t]/(t^2+t+1).
\]
For these three fields it exhaustively enumerates all vertex subsets, tests domination and perfect matchings, and compares the resulting coefficient vector with the closed formula. The largest global enumeration is the \(16\)-vertex graph at \(q=5\), so all \(2^{16}\) subsets are examined.

It also checks the minimum exponent, total number of paired dominating sets, leading coefficient, degree, and polynomial recovery of \(q\) for \(q\in\{7,8,9,11,13,16\}\).

Exact output:

```text
VERIFY_OK
brute_actual_fields=q3,q4,q5
largest_global_subset_enumeration=2^16
component_profiles=q3:K2,2;q4:K3+K3,3;q5:2K4+K4,4
formula_and_reconstruction_checks=q7,q8,q9,q11,q13,q16
```

These finite checks are corroborative. The theorem for arbitrary prime powers is proved by the slope involution and the componentwise paired-domination count.

## Relationship to prior work

Badawi introduced the dot-product graph framework for commutative rings and classified the paper under primary MSC \(13A15\). Abdulla and Badawi later gave the complete component decomposition of the unit dot-product graph over finite fields: one clique plus bicliques in characteristic two, only bicliques when \(q\equiv3\pmod4\), and two cliques plus bicliques when \(q\equiv1\pmod4\). Their work studies graph structure rather than paired domination.

Saleh and Megahed subsequently studied ordinary domination for unit dot-product graphs and obtained ordinary domination values, but they do not discuss paired domination or paired-domination polynomials. The paired-domination polynomial itself was introduced in general graph theory in September 2016.

The result here is the exact paired-domination enumerator for the finite-field unit dot-product family. The matching condition detects precisely the self-orthogonal slope classes \(a^2=-1\): ordinary domination treats every field case through the same scale \(q-1\), whereas paired domination changes by \(0\), \(1\), or \(2\) according to the number of fixed slopes. Targeted searches for paired domination, paired-domination polynomial, unit dot-product graph, and finite-field dot-product graph combinations found no prior statement of the formula.

## Limitations

The theorem concerns the unit dot-product graph on two coordinates over a finite field. It does not treat higher-dimensional dot-product graphs, unit dot-product graphs over arbitrary finite rings, or the total and zero-divisor dot-product graphs.

The graph decomposition itself is known; the new claim is the paired-domination polynomial, its minimum and counting consequences, and polynomial recovery of \(q\).

No claim is made that the paired-domination polynomial is a complete invariant outside this family.

## References

1. A. Badawi, “On the Dot Product Graph of a Commutative Ring,” *Communications in Algebra* 43 (2015), 43–50. DOI: 10.1080/00927872.2014.897188. Published online 1 August 2014.
2. M. Abdulla and A. Badawi, “On the Dot Product Graph of a Commutative Ring II,” *International Electronic Journal of Algebra* 28 (2020), 61–74. DOI: 10.24330/ieja.768135.
3. D. Saleh and N. Megahed, “Dot product graphs and domination number,” *Journal of the Egyptian Mathematical Society* 28 (2020), Article 31. DOI: 10.1186/s42787-020-00092-6.
4. Puttaswamy, A. Alwardi, and S. R. Nayaka, “Introduction to Paired Domination Polynomial of a Graph,” *International Journal of Physical and Mathematical Sciences* 10(9) (2016), conference dates 26–27 September 2016.
