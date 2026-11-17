# Exact period and leading parity oscillation for the three-block cyclic polytope

## Finding

For every integer \(a\ge2\), define the full-dimensional rational polytope
\[
C_a=\left\{(x_{ij})\in\mathbb R_{\ge0}^{3a}:
R_1+R_2\le1,\ R_2+R_3\le1,\ R_3+R_1\le1\right\},
\qquad R_i=\sum_{j=1}^a x_{ij}.
\]
Let \(L_a(q)=\#(qC_a\cap\mathbb Z^{3a})\) for integers \(q\ge0\), and \(F_a(z)=\sum_{q\ge0}L_a(q)z^q\). Then the *reduced rational denominator* of \(F_a\) is exactly
\[
\boxed{(1-z)^{3a+1}(1+z)^{3a-2}}.
\]
Thus the minimum Ehrhart quasiperiod is exactly \(2\), with no period collapse. Moreover, there are unique polynomials \(P_a,Q_a\in\mathbb Q[q]\) such that
\[
L_a(q)=P_a(q)+(-1)^q Q_a(q),
\quad \deg P_a=3a,\quad \deg Q_a=3a-3,
\]
and their oscillatory leading coefficient is
\[
\boxed{[q^{3a-3}]Q_a(q)=\frac{1}{2^{3a+1}((a-1)!)^3}.}
\]
Equivalently, the coefficient of \((1+z)^{-(3a-2)}\) in the principal part of \(F_a\) at \(z=-1\) is
\[
\boxed{\frac{(3a-3)!}{2^{3a+1}((a-1)!)^3}.}
\]
This determines the first periodic Ehrhart coefficient and its exact size in every block dimension.

## Assumptions and scope

The parameter \(a\) is an integer at least \(2\); the dilation \(q\) is any nonnegative integer. The ambient lattice is the ordinary \(\mathbb Z^{3a}\). The three blocks have equal size \(a\), and *all three* pairwise block-sum constraints are imposed. The scalar case \(a=1\), whose exact enumeration is classical, is not asserted as new. No claim is made here about cycles of five or more blocks.

## Proof

Put \(w_a(r)=\binom{r+a-1}{a-1}\). This is the number of nonnegative integer vectors of length \(a\) with coordinate sum \(r\). Hence, for any \(q\ge0\), the lattice-point count is
\[
L_a(q)=\sum_{\substack{r_1,r_2,r_3\ge0\\r_i+r_j\le q\ (i<j)}}w_a(r_1)w_a(r_2)w_a(r_3).
\]
For fixed nonnegative block sums, the smallest allowable dilation is
\[
M(r_1,r_2,r_3)=\max_{i<j}(r_i+r_j)=r_1+r_2+r_3-\min_i r_i.
\]
Therefore, in formal power series,
\[
F_a(z)=\frac1{1-z}\sum_{r_1,r_2,r_3\ge0}\left(\prod_iw_a(r_i)\right)z^{M(r_1,r_2,r_3)}.
\]
For any integer \(s\ge0\) and \(0\le h\le s\), use the exact identity
\[
\frac{z^{s-h}}{1-z}=\frac{z^s}{1-z}+\sum_{t=1}^{h}z^{s-t}.
\]
Apply this with \(s=r_1+r_2+r_3\) and \(h=\min_i r_i\), and exchange finite coefficients of the nonnegative series. Define
\[
A_{a,t}(z)=\sum_{u\ge0}\binom{t+u+a-1}{a-1}z^u.
\]
The resulting *exact all-dilation identity* is
\[
\tag{1}\boxed{F_a(z)=\frac1{(1-z)^{3a+1}}+\sum_{t\ge1}z^{2t}A_{a,t}(z)^3.}
\]
Because \(\binom{t+u+a-1}{a-1}\) is a polynomial of degree \(a-1\) in \(u\), its generating function \(A_{a,t}(z)\) is rational with denominator dividing \((1-z)^a\). Its numerator is polynomial in \(t\) of degree \(a-1\). In particular, *as a polynomial in* \(t\), its leading coefficient is
\[
\tag{2}[t^{a-1}]A_{a,t}(z)=\frac1{(a-1)!(1-z)}.
\]
For any integer \(j\ge0\), the rational function \(S_j(y)=\sum_{t\ge1}t^jy^t\) has a pole of exact order \(j+1\) at \(y=1\), with leading local behavior \(j!/(1-y)^{j+1}\). Expand \(A_{a,t}(z)^3\) as a polynomial in \(t\) of degree \(d=3a-3\). Formula (1) expresses \(F_a(z)\) as a finite linear combination of the rational functions \(S_j(z^2)\) with coefficients having no poles away from \(z=1\). Thus its only possible poles are \(z=1\) and \(z=-1\).

At \(z=-1\), the term with \(j=d\) is the only one with pole order \(d+1\). By (2) its coefficient is \(1/((a-1)!)^3(1-z)^3\). Since \(1-z^2=(1-z)(1+z)\),
\[
\tag{3}
\lim_{z\to-1}(1+z)^{d+1}F_a(z)
=\frac{d!}{((a-1)!)^3\,2^{d+4}}
=\frac{(3a-3)!}{((a-1)!)^3\,2^{3a+1}}>0.
\]
No lower-power term in \(t\) can cancel this pole, so \(z=-1\) is an actual pole of order \(3a-2\). By the rational Ehrhart theorem, because \(C_a\) is bounded and full-dimensional in \(\mathbb R^{3a}\), \(F_a(z)\) has a pole of exact order \(3a+1\) at \(z=1\). Together these establish the stated *reduced denominator*.

Partial fractions at the only two poles give a unique decomposition \(L_a(q)=P_a(q)+(-1)^qQ_a(q)\), with degrees \(3a\) and \(d\), respectively. Finally, the coefficient of \(z^q\) in \((1+z)^{-(d+1)}\) is \((-1)^q\binom{q+d}{d}\). Inserting (3) gives precisely the claimed leading coefficient of \(Q_a\). A pole at \(-1\) rules out an ordinary Ehrhart polynomial, while the source's half-integrality bound gives quasiperiod dividing two, so the minimum quasiperiod is exactly two. \(\square\)

## Verification

The standalone `verify.py` checks the direct three-height enumeration against the independent minimum-layer decomposition for \(a=1,\dots,5\) and \(q=0,\dots,12\). For \(a=1,2,3\) it independently constructs the entire generating function as an exact rational function using finite symbolic power sums, checks its first thirteen coefficients, and evaluates the pole coefficient at \(z=-1\). It passes \(110\) exact assertions.

In particular, its exact results for \(a=2\) and \(a=3\) are
\[
F_2(z)=\frac{(1+z+z^2)(1+3z+10z^2+3z^3+z^4)}{(1-z)^7(1+z)^4},
\]
\[
F_3(z)=\frac{1+7z+48z^2+116z^3+251z^4+264z^5+251z^6+116z^7+48z^8+7z^9+z^{10}}{(1-z)^{10}(1+z)^7}.
\]
Finite tests are corroboration only; proof of the unrestricted statement is analytic (1)–(3).

## Relationship to prior work

Jiang, Yang, and Zhong (arXiv:2607.22008, first public July 24, 2026) defined these cyclic block polytopes and established that odd-cycle cases have vertex denominator exactly two and Ehrhart quasiperiod *dividing* two. Their result does not itself exclude period collapse, nor give the order and leading Laurent coefficient of the pole at \(z=-1\). The present result identifies the exact reduced Ehrhart-series denominator and leading parity oscillation of the smallest odd cycle with arbitrarily large block size.

Bóna, Ju, and Yoshida (arXiv:math/0606163) give the exact scalar triangular-cycle case \(a=1\), which is therefore explicitly excluded from the new-claim range. Hamano, Hibi, and Ohsugi (arXiv:1603.09613) treat the graph-based fractional stable-set polytope with *individual-coordinate edge inequalities*, not the stronger pairwise block-*sum* inequalities when \(a\ge2\). Classical results on period collapse show why the half-integrality of vertices alone does not prove exact quasiperiodicity.

## Limitations

The result is specifically for three equally sized blocks; there is no classification of the exact minimum quasiperiod for all odd cycle lengths. The rational generating function is determined structurally but no simple coefficientwise closed form for the full numerator is claimed. Historical priority is subject to independent literature review; unindexed equivalent formulations remain possible.

## References

1. Xinru Jiang, Shuai Yang, Yueming Zhong, *Transfer Matrices and Ehrhart Theory for Path and Cyclic Block Polytopes*, arXiv:2607.22008v1 (2026-07-24), https://arxiv.org/abs/2607.22008.
2. Miklós Bóna, Hyeong-Kwan Ju, Ruriko Yoshida, *On the Enumeration of Certain Weighted Graphs*, arXiv:math/0606163v1 (2006-06-07), https://arxiv.org/abs/math/0606163.
3. Ginji Hamano, Takayuki Hibi, Hidefumi Ohsugi, *Ehrhart series of fractional stable set polytopes of finite graphs*, arXiv:1603.09613v2 (2016-11-29), https://arxiv.org/abs/1603.09613.
4. T. B. McAllister and K. M. Woods, *The minimum period of the Ehrhart quasi-polynomial of a rational polytope*, J. Combin. Theory Ser. A 109 (2005), 345–352, https://doi.org/10.1016/j.jcta.2004.08.006.
