# Three-type radial stochastic dominance for the first sibling deficit

## Finding

For independent coupon draws on three types with any strictly positive nonuniform probability vector \(\mathbf p=(p_1,p_2,p_3)\), let \(\mathbf u=(1/3,1/3,1/3)\), \(\mathbf p(\theta)=\mathbf u+\theta(\mathbf p-\mathbf u)\), and \(U(\theta)\) denote the first sibling's number of missing types when the main collector first sees all three types. For all \(0\le\theta_1<\theta_2\le1\),

\[
\Pr(U(\theta_1)\ge k)>\Pr(U(\theta_2)\ge k),\qquad k=2,3.
\]

Since \(U(\theta)\in\{1,2,3\}\), this is strict radial *ordinary stochastic dominance* (not just a moment or generating-function comparison). In particular the uniform law is the unique stochastic maximum among positive sampling vectors at three types. Its upper-tail probabilities are \(\Pr(U(0)\ge2)=11/18\) and \(\Pr(U(0)=3)=2/9\).

## Assumptions and scope

All samples are iid, with replacement. The main collector keeps first appearances; all repeats pass to the first sibling, who keeps the first repeat of each type. The stopping time is the first collection of all three types by the main collector. Thus \(U\) counts types appearing exactly once at that time. Only three types and the first sibling (second album index) are considered. The strict assertions concern thresholds \(2\) and \(3\); the threshold \(1\) is certain.

## Proof

Write arbitrary positive rates as \(a,b,c\), with \(s=a+b+c\). Normalizing rates does not change the coupon-label sequence. Define

\[
H(a,b,c)=2\left(\frac{ab}{(a+b)^2}+\frac{ac}{(a+c)^2}+\frac{bc}{(b+c)^2}\right)
-\frac{2(ab+ac+bc)}{s^2}-\frac{6abc}{s^3},
\qquad K(a,b,c)=\frac{6abc}{s^3}.
\]

These are exactly \(\Pr(U\ge2)\) and \(\Pr(U=3)\). To derive \(H\), use independent Poisson clocks with these rates. Condition on type \(k\) being the last type first observed at time \(t\). For the other two types, the event that at least one was observed exactly once has unnormalized probability

\[
(a_i t)e^{-a_i t}(1-e^{-a_jt})+(a_jt)e^{-a_jt}(1-e^{-a_it})-a_i a_j t^2e^{-(a_i+a_j)t}.
\]

Multiplication by \(a_k e^{-a_k t}\), integration over \(t\ge0\), and summation over \(k\), using \(\int_0^\infty t e^{-\lambda t}dt=\lambda^{-2}\) and \(\int_0^\infty t^2 e^{-\lambda t}dt=2\lambda^{-3}\), yield \(H\). The identity for \(K\) follows independently because all three types are singleton at completion precisely when the first three draws have distinct labels.

For \(H\), define the radial dissipation

\[
R(a,b,c)=-\sum_{v\in\{a,b,c\}}\left(v-\frac{s}{3}\right)\partial_vH(a,b,c).
\]

By symmetry, order the rates \(a\ge b\ge c>0\) and put \(a=x+y+z\), \(b=y+z\), \(c=z\), where \(x,y\ge0\), \(z>0\). An exact polynomial identity gives

\[
R(a,b,c)=\frac{\mathcal P(x,y,z)}{3s^3(a+b)^3(a+c)^3(b+c)^3},
\qquad \mathcal P(x,y,z)=\sum_{j=0}^{10}z^j B_j(x,y).
\]

The complete, explicit polynomials \(B_j\) are displayed in `CERTIFICATE.md`. Every one of their monomial coefficients is nonnegative (79 nonzero coefficients in total), and

\[
B_{10}(x,y)=8448(x^2+xy+y^2).
\]

Hence \(R>0\) whenever \(x+y>0\). This is an elementary exact positivity certificate: the identity and all coefficients can also be recomputed by `verify.py`.

Along the ray \(\mathbf p(\theta)\) with \(\theta>0\), the sum of the coordinates is one and \(\mathbf p(\theta)-\mathbf u=\theta(\mathbf p-\mathbf u)\); therefore

\[
-\theta\frac{d}{d\theta}H(\mathbf p(\theta))=R(\mathbf p(\theta))>0.
\]

For the other nonconstant tail, \(K(\mathbf p(\theta))=6\prod_i p_i(\theta)\), and

\[
\theta\frac{d}{d\theta}\log K(\mathbf p(\theta))
=3-\frac13\sum_{i=1}^3\frac1{p_i(\theta)}<0
\]

by the strict harmonic-mean inequality, since \(\mathbf p(\theta)\ne\mathbf u\). Continuity at \(\theta=0\) gives strict inequality for every pair of distinct ray parameters as stated. The two tail inequalities and the certain threshold \(1\) completely determine ordinary stochastic order for \(U\in\{1,2,3\}\).

## Verification

`CERTIFICATE.md` supplies the complete positive-coefficient identity, including its denominator. `verify.py` rederives the exact derivative symbolically, checks the sign of every coefficient, and independently compares the tail formulae against a rational Markov-state recursion for all 216 integer triples in \(\{1,\ldots,6\}^3\). It also checks 12 strict finite ray comparisons. These finite examples are diagnostics; the symbolic identity and coefficient signs establish the continuum statement.

## Relationship to prior work

Doumas and Spektor (arXiv:2606.21591) and Long (arXiv:2606.29635) establish radial maximum principles for the *expectation* of the sibling deficit. Long (arXiv:2606.31391) establishes stronger probability-generating-function, Laplace-transform and all-binomial-moment orders, but Remark 5.6 explicitly leaves radial *ordinary stochastic order* open; those transform orders do not imply the two individual tail inequalities above. The present result proves the smallest nontrivial three-type, first-sibling instance of that stronger order, rather than asserting a solution for all numbers of types or sibling indices.

## Limitations

There is no claim for four or more coupon types, higher-index siblings, arbitrary comparisons not lying on a common ray from uniformity, or stronger orders such as likelihood-ratio or hazard-rate order. The coefficient positivity is proved for this specific three-type rational function. Earlier literature may contain an equivalent special-case inequality under another formulation; historical priority is not independently certified.

## References

- A. V. Doumas and S. Spektor, *Equal probabilities maximize the expected deficit in the siblings of the coupon collector*, arXiv:2606.21591, first posted 2026-06-19, https://arxiv.org/abs/2606.21591 .
- C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, arXiv:2606.29635, first posted 2026-06-28, https://arxiv.org/abs/2606.29635 .
- C. D. Long, *Radial Transform Extremality for the Siblings of the Coupon Collector*, arXiv:2606.31391, first posted 2026-06-30, https://arxiv.org/abs/2606.31391 .
