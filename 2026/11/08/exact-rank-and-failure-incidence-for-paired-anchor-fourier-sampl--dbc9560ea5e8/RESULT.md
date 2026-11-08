# Exact rank and failure incidence for paired-anchor Fourier sampling on even semiprime cycles

## Finding
For every odd prime \(p\), the paired-anchor four-measurement family below has an exact rank dichotomy, governed by simultaneous midpoint congruences. Every sampling matrix has rank three or four. Rank three occurs exactly when the two row-pair centers agree and either the underlying pairs coincide or the two off-anchor measurements have opposite offsets.

The number of singular row/column-set pairs is
\[
\boxed{\frac{p^2(p-1)^2(3p-7)}4}.
\]
The singular fraction in this canonical four-by-four family is
\[
\boxed{\frac{3p-7}{p(p-1)(p-2)}}\sim\frac3{p^2}.
\]
This measures the exact risk of nonunique interpolation when one frequency is sampled on both parity channels and the remaining two samples are taken on a single parity channel.

## Assumptions and scope
Let \(p\ge3\) be an odd prime, \(G=\mathbb Z_2\times\mathbb F_p\), \(\zeta=e^{2\pi i/p}\), and use the unnormalized Fourier pairing
\[
 F((\epsilon,x),(\eta,y))=(-1)^{\epsilon\eta}\zeta^{xy}.
\]
Choose unordered two-element sets \(A=\{a_1,a_2\}\), \(B=\{b_1,b_2\}\) independently in \(\mathbb F_p\), including the case \(A=B\). The row set is \(R=(\{0\}\times A)\cup(\{1\}\times B)\). Choose a parity \(\eta\in\mathbb Z_2\), an anchor frequency \(y_0\in\mathbb F_p\), and an unordered two-element set \(\{y_1,y_2\}\subset\mathbb F_p\setminus\{y_0\}\). The four-column set is
\[
 C=\{(0,y_0),(1,y_0),(\eta,y_1),(\eta,y_2)\}.
\]
All these four columns are distinct. All sums, products, differences, and division by two in indexed congruences are in \(\mathbb F_p\).

**Theorem.** For these and only these choices,
\[
\operatorname{rank}_{\mathbb C}F[R,C]=3
\iff
(a_1+a_2=b_1+b_2)\ \text{and}\ (A=B\ \text{or}\ y_1+y_2=2y_0).
\]
Otherwise the rank is four. This is not a classification of all four-by-four minors of the full Fourier matrix of \(G\).

## Proof
**1. Reduce to two signed exponential differences.** Add and subtract the two anchor columns. The resulting vectors are supported separately in the two parity row blocks and are linearly independent. Divide the rows by their nonzero anchor characters. Modulo the span of these two vectors, an extra column at \(y=y_0+t\) has coordinates proportional to
\[
 D_A(t)=\zeta^{a_1t}-\zeta^{a_2t},\qquad
 D_B(t)=\zeta^{b_1t}-\zeta^{b_2t}.
\]
The common factor \((-1)^\eta\) on the second coordinate is harmless. Thus the four-by-four minor is singular if and only if
\[
 D_A(t_1)D_B(t_2)=D_A(t_2)D_B(t_1),
 \qquad t_i=y_i-y_0\ne0,\quad t_1\ne t_2.
\]
Each difference is nonzero, since its two row indices differ and \(p\) is prime. Consequently, even when the determinant vanishes the two anchor vectors and either extra vector are independent; the rank is exactly three.

**2. Force equal row-pair sums.** Put \(s_A=a_1+a_2\), \(s_B=b_1+b_2\) and \(r=(a_1-a_2)/2\), \(s=(b_1-b_2)/2\). Define \(S_v(t)=\zeta^{vt}-\zeta^{-vt}\), a nonzero purely imaginary number for \(v,t\ne0\). Then \(D_A(t)=\zeta^{s_A t/2}S_r(t)\), and similarly for \(B\). The determinant equality implies
\[
 \zeta^{(s_A-s_B)(t_1-t_2)/2}
 =\frac{S_r(t_2)S_s(t_1)}{S_r(t_1)S_s(t_2)}\in\mathbb R\setminus\{0\}.
\]
For an odd prime, the only real \(p\)-th root of unity is \(1\). Since \(t_1\ne t_2\), necessarily \(s_A=s_B\).

**3. A fourth-moment obstruction.** With equal row-pair sums, the condition is
\[
 S_r(t_1)S_s(t_2)-S_r(t_2)S_s(t_1)=0.
\]
In the integral group ring \(\mathbb Z[\mathbb F_p]\), write \([u]\) for the basis element at \(u\), and define
\[
 \mu=([rt_1]-[-rt_1])*([st_2]-[-st_2])
 -([rt_2]-[-rt_2])*([st_1]-[-st_1]).
\]
Here \(*\) is additive convolution. The displayed root-of-unity identity says \(\sum_u\mu(u)\zeta^u=0\), and \(\sum_u\mu(u)=0\). The minimal polynomial \(1+X+\cdots+X^{p-1}\) shows that these two statements force every integer coefficient \(\mu(u)\) to be zero: the coefficient polynomial of degree at most \(p-1\) is a multiple of the minimal polynomial, and its value at one is zero.

In particular its fourth residue moment vanishes modulo \(p\). Direct expansion gives
\[
 \sum_{u\in\mathbb F_p}\mu(u)u^4
 =16rst_1t_2(r^2-s^2)(t_1^2-t_2^2)=0
 \quad\text{in }\mathbb F_p.
\]
As \(2,r,s,t_1,t_2\) are units, either \(r^2=s^2\) or \(t_1^2=t_2^2\). Equal pair sums and \(r^2=s^2\) mean precisely that the unordered pairs \(A,B\) are equal. Otherwise \(t_1=-t_2\), since the offsets are distinct. Conversely, if \(A=B\) the two signed differences are identical; if the sums agree and \(t_1=-t_2\), each centered difference is odd, so the determinant identity holds. This completes the rank classification.

**4. Exact incidence.** Set \(m=(p-1)/2\). There are \(\binom p2=pm\) unordered row pairs. For each prescribed sum in \(\mathbb F_p\) exactly \(m\) such pairs exist. There are therefore \(pm\) choices with \(A=B\), and \(pm(m-1)\) choices with equal sums but unequal pairs. The first type is singular for every one of the \(2p\binom{p-1}2=2pm(p-2)\) admissible column sets; the second type is singular for exactly \(2pm\) column sets, since for each anchor the symmetric off-anchor pair is \(\{y_0\pm t\}\) with \(m\) choices. Hence
\[
 N_3=pm\cdot 2pm(p-2)+pm(m-1)\cdot2pm
 =\frac{p^2(p-1)^2(3p-7)}4.
\]
The total number is \(T=\binom p2^2\,2p\binom{p-1}2\); subtracting gives the rank-four count. Dividing yields \(N_3/T=(3p-7)/(p(p-1)(p-2))\).

## Verification
Run `python3 checker.py` with Python 3.8 or later. It tests the determinant reduction using *exact integer coefficients* in the cyclic group ring: because the coefficient sum is zero, the corresponding cyclotomic value vanishes exactly when all coefficients vanish. The checker exhausts every configuration for \(p=3,5,7,11\), both parity choices, and checks both the rank criterion and the closed incidence formula. It also performs fixed-seed exact spot checks for \(p=13,17,19,23\). Its final output is `PAIR_ANCHOR_FOURIER_RANK_CENSUS_PASS`. These experiments are corroboration, not the proof of the infinitely quantified theorem.

## Relationship to prior work
The prime-cyclic full-spark principle of Chebotarev is presented with a proof by Tao, *An uncertainty principle for cyclic groups of prime order* (arXiv:math/0308286, first posted 29 August 2003). It applies to the prime Fourier factor, not the paired-channel four-minor family on \(\mathbb Z_2\times\mathbb F_p\). Delvaux and Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices* (Report TW477, 2006; DOI 10.1016/j.laa.2007.05.009), study maximal rank-deficient blocks, rank-one tilings and Hamming numbers. The rank-three midpoint pattern and its exact four-minor incidence are not among the statements identified in the inspected sections. A published classification of singular three-by-three minors on even semiprime cycles concerns smaller minors; it does not imply this exact four-by-four classification on its face.

## Limitations
The theorem is restricted to balanced rows and a two-channel column set with one doubly observed anchor frequency and two extra frequencies on a common parity channel. It does not classify arbitrary four-by-four Fourier minors, provide sharp smallest singular values on invertible configurations, or imply a full support-uncertainty classification. Priority remains bounded by the literature materially inspected and could be affected by an earlier equivalent framework. Independent mathematical validation has not been performed.

## References
- Terence Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, version 1 submitted 2003-08-29; see Lemmas 1.2–1.3.
- Steven Delvaux and Marc Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, Report TW477 (November 2006), *Linear Algebra Appl.* 426 (2007), 349–367, DOI: 10.1016/j.laa.2007.05.009; see Sections 2–4 and Theorems 14 and 20.
- *Singular three-by-three Fourier minors on even semiprime cycles*, publicly indexed result, 2026-10-11, for minor-size comparison only; its complete proof was not accessed.
