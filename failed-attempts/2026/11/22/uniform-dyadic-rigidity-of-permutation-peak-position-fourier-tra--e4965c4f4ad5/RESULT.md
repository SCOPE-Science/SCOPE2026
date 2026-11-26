# Uniform dyadic rigidity of permutation peak-position Fourier transforms

## Finding

For every integer \(n\ge 3\), write \(P(\pi)=\{i\in\{2,\ldots,n-1\}:\pi_{i-1}<\pi_i>\pi_{i+1}\}\) for the interior peak-position set of a permutation \(\pi\in\mathfrak S_n\). Let \(G_n=\mathbb F_2^{n-2}\), and define the integer counting kernel

\[
f_n(x)=\#\{\pi\in\mathfrak S_n:\mathbf1_{P(\pi)}=x\},\qquad x\in G_n.
\]

For each character indexed by \(S\subseteq\{2,\ldots,n-1\}\), define the unnormalized Walsh multiplier

\[
W_n(S)=\sum_{\pi\in\mathfrak S_n}(-1)^{|P(\pi)\cap S|}.
\]

**Theorem (uniform, sharp dyadic rigidity).** Put \(v=v_2(n!)=\sum_{r\ge1}\lfloor n/2^r\rfloor\). For **every** \(n\ge3\) and every \(S\),

\[
\boxed{W_n(S)\equiv n!\pmod{2^{v+1}},\qquad v_2(W_n(S))=v.}
\]

The uniform congruence modulus cannot be increased: for every singleton \(S=\{i\}\),

\[
W_n(\{i\})=\frac{n!}{3},\qquad v_2(W_n(\{i\})-n!)=v+1.
\]

Thus the convolution \(T_nh=f_n*h\) on the counting-measure Hilbert space \(\ell^2(G_n)\) is invertible for every \(n\ge3\), and

\[
\|T_n^{-1}\|_{\ell^2\to\ell^2}\le 2^{-v},\qquad
v_2(|\det T_n|)=2^{n-2}v.
\]

The norm inequality is not claimed to be sharp for every \(n\). For \(n=1,2\) the peak profile has zero coordinates, and its sole multiplier is \(n!\); the stated uniform sharpness is intended only for \(n\ge3\).

## Assumptions and scope

The permutation distribution is **uniform on all** \(n!\) permutations, with multiplicities retained when several permutations have the same peak profile. No cyclic end-point peaks are included. The group law is coordinatewise XOR. The Fourier transform and convolution use unnormalized counting sums, so there is no hidden normalization by \(2^{n-2}\) or \(n!\). The valuation \(v_2(m)\) is defined for a nonzero integer \(m\) as the highest exponent of \(2\) dividing \(m\); the theorem also proves the asserted multipliers are nonzero.

Let \(\mathbb Z_{(2)}=\{a/b\in\mathbb Q:b\text{ odd}\}\) be the rationals with odd reduced denominator. For such rationals, congruences modulo \(2\) mean congruences in this localization.

## Proof

**1. Odd-denominator alternating-block probabilities.** Let \(E_{2k+1}\) count permutations of \(2k+1\) labels satisfying the up-down inequalities \(a_1<a_2>a_3<a_4>\cdots<a_{2k}>a_{2k+1}\), and put

\[
b_k=\frac{E_{2k+1}}{(2k+1)!},\qquad k\ge0.
\]

Here \(b_0=1\). For \(k\ge1\), the maximum of an up-down permutation must occur at one of its \(k\) even positions. If the maximum lies at position \(2j+2\), the left and right subwords have lengths \(2j+1\) and \(2k-2j-1\), each with the same up-down pattern. Distributing the other \(2k\) labels between the two sides gives the exact recurrence

\[
E_{2k+1}=\sum_{j=0}^{k-1}\binom{2k}{2j+1}E_{2j+1}E_{2k-2j-1}.
\]

Dividing by \((2k)!\) yields

\[
(2k+1)b_k=\sum_{j=0}^{k-1}b_jb_{k-1-j}.
\]

The divisor \(2k+1\) is odd. Induction from \(b_0=1\) therefore establishes \(b_k\in\mathbb Z_{(2)}\) for all \(k\ge0\). Equivalently, \(\sum_{k\ge0}b_kz^{2k+1}=\tan z\), whose formal derivative is \(1+\tan^2z\). The recurrence proof above avoids any appeal to analytic convergence or a numerical assertion about tangent numbers.

**2. Every prescribed joint peak probability has odd denominator.** Choose independent continuous identically distributed uniform random variables \(U_1,\ldots,U_n\). Their relative ranks give a uniformly random permutation, so the peak-position indicators agree in law. For \(A\subseteq\{2,\ldots,n-1\}\), let \(p(A)\) be the probability that every position in \(A\) is a peak (peaks outside \(A\) are unrestricted). If \(A\) contains adjacent integers, then \(p(A)=0\), since adjacent local maxima are impossible.

Otherwise break \(A\) into its maximal components linked by differences of exactly two. A component of \(k\) peak positions \(i,i+2,\ldots,i+2k-2\) uses precisely the \(2k+1\) random variables \(U_{i-1},\ldots,U_{i+2k-1}\) and imposes one up-down ordering. It therefore has probability exactly \(b_k\). Distinct maximal components are separated by at least three peak positions, so their blocks of random variables are disjoint and their events are independent. Consequently,

\[
p(A)=\begin{cases}
0,&\text{if two elements of }A\text{ are adjacent},\\
\prod_{C\in\mathrm{comp}_2(A)}b_{|C|},&\text{otherwise},
\end{cases}
\]

where the empty product is \(1\). Step 1 gives \(p(A)\in\mathbb Z_{(2)}\) for **every** \(A\).

**3. Walsh expansion and exact valuation.** With \(I_i\) the indicator that \(i\) is a peak,

\[
\frac{W_n(S)}{n!}=\mathbb E\prod_{i\in S}(1-2I_i)
=\sum_{A\subseteq S}(-2)^{|A|}p(A).
\]

The empty term is \(1\). Every nonempty term belongs to \(2\mathbb Z_{(2)}\) by Step 2. Hence \(W_n(S)/n!\in1+2\mathbb Z_{(2)}\), a dyadic unit, and therefore \(W_n(S)-n!\) is divisible by \(2^{v+1}\) while \(v_2(W_n(S))=v\).

For any single interior position, the three relative ranks are uniform, and the central value is the largest with probability \(1/3\). Thus \(W_n(\{i\})=n!(1-2/3)=n!/3\), and the difference from \(n!\) equals \(-2n!/3\), with valuation exactly \(v+1\). This proves sharpness.

**4. Convolution consequences.** The normalized Walsh characters form an orthonormal basis of \(\ell^2(G_n)\), and counting convolution by \(f_n\) acts diagonally with eigenvalues exactly \(W_n(S)\). Since none vanishes, \(T_n\) is invertible and its inverse has Hilbert operator norm \(\max_S|W_n(S)|^{-1}\le2^{-v}\). The determinant is the product of the \(2^{n-2}\) eigenvalues, each of exact dyadic valuation \(v\); consequently \(v_2(|\det T_n|)=2^{n-2}v\). This is a valuation statement, not a formula for the determinant's odd part or sign.

## Verification

Run `python3 peak_profile_verify.py` with Python 3 and its standard library. The checker builds the Walsh transform independently using (i) joint-peak probabilities and the alternating-block recurrence, and (ii) descent-set inclusion-exclusion followed by a Walsh transform. These exact-integer/rational implementations agree at every character for \(3\le n\le15\). Direct iteration over all permutations gives a third independent check for \(3\le n\le9\). Each test also checks the asserted congruence, nonvanishing and singleton sharpness. These finite computations corroborate but do not replace the all-order argument above.

## Relationship to prior work

The underlying peak-position statistic and exact enumerative theory are classical. Billey, Burdzy and Sagan (arXiv:1209.0693v1, first submitted 2012-09-04) provide the general peak-set polynomial enumeration \(|P(A;n)|=p(A;n)2^{n-|A|-1}\) and individual formulas. Aguiar, Bergeron and Nyman (arXiv:math/0302278, 2003) study the peak algebra and its relationship to descent algebras; Diaz-Lopez, Harris, Insko and Perez-Lavin (arXiv:1505.04479, 2015) extend enumerative approaches across Coxeter types. The new conclusion here concerns the **complete family of additive Boolean Fourier characters** of the multiplicity-weighted peak-profile pushforward, including their uniform exact dyadic valuation and the sharp universal congruence. The cited peak-set counting and peak-algebra results do not state the present all-order Fourier nonvanishing result, and their displayed enumerative powers alone do not yield the exact factorial valuation without the local alternating-block argument.

## Limitations

The proof does not determine the full odd parts or signs of the multipliers, nor a sharp nonzero magnitude at every order. It addresses interior **position** peaks of ordinary permutations, not circular peaks, peak values, signed-permutation analogues or descent-profile convolutions. Originality was assessed against accessible relevant literature and database records, not a guarantee against all unpublished or unindexed equivalents. No independent mathematical review or audit is asserted.

## References

1. S. Billey, K. Burdzy and B. E. Sagan, *Permutations with Given Peak Set*, arXiv:1209.0693v1 (2012-09-04), https://arxiv.org/html/1209.0693v1 .
2. M. Aguiar, N. Bergeron and K. Nyman, *The Peak Algebra and the Descent Algebras of Types B and D*, arXiv:math/0302278 (2003), https://arxiv.org/abs/math/0302278 .
3. A. Diaz-Lopez, P. E. Harris, E. Insko and D. Perez-Lavin, *Peak Sets of Classical Coxeter Groups*, arXiv:1505.04479 (2015), https://arxiv.org/abs/1505.04479 .
4. Classical André alternating-permutation enumeration: odd-length Euler zigzag numbers are coefficients of \(\tan z\); the requisite recurrence is proved directly above.
