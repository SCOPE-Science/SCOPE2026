# A complete signed correlation spectrum for Franel numbers modulo five

## Finding

Let the Franel numbers be
\[
F_n=\sum_{j=0}^{n}\binom nj^3\qquad(n\geq0),
\]
and write \(g(n)=\chi_5(F_n)\in\{-1,0,1\}\), where \(\chi_5\) is the quadratic character modulo \(5\), with \(\chi_5(0)=0\). For integers \(r\geq0\) and \(h\geq0\), define the *unwrapped* base-five block correlation
\[
S_r(h)=\sum_{0\leq n<5^r}g(n)g(n+h).
\]
The unwrapped convention is essential: \(n+h\) is not reduced modulo \(5^r\).

**Theorem.** For every fixed \(h\geq0\), the rational limit
\[
C(h)=\lim_{r\to\infty}4^{-r}S_r(h)
\]
exists, and \(S_r(h)-4^rC(h)\) is an integer constant for all sufficiently large \(r\) (depending on \(h\)). All its values are specified recursively by
\[
\begin{aligned}
C(0)&=1,& C(1)&=0,\\
C(5q)&=C(q), & C(5q+1)&=\tfrac14C(q+1),\\
C(5q+2)&=-\tfrac14C(q), & C(5q+3)&=-\tfrac14C(q+1),\\
C(5q+4)&=\tfrac14C(q).
\end{aligned}
\]
The last five rules are valid for every integer \(q\geq0\), with the self-referential \(C(1)\) equation resolved by the stated initial value. In particular, every nonzero \(C(h)\) is a signed integral power of \(4^{-1}\).

There is an **exact, complete spectrum across all short shifts**. For every integer \(r\geq1\), among the \(5^r\) shifts \(0\leq h<5^r\), exactly one has \(C(h)=1\) (namely \(h=0\)), exactly \((5^r-1)/2\) have \(C(h)=0\), and, for each \(1\leq j\leq r\), precisely
\[
\boxed{4^{j-1}\binom rj}
\]
shifts have \(C(h)=4^{-j}\), with exactly the same number having \(C(h)=-4^{-j}\). No other values occur on that interval.

The sharp all-positive-shift extremal law is
\[
\boxed{-\frac14\leq C(h)\leq\frac14\qquad(h\geq1),}
\]
with equality on the left **if and only if** \(h=2\cdot5^m\) and on the right **if and only if** \(h=4\cdot5^m\), for integers \(m\geq0\). The basic correlation identities
\[
S_r(1)=-1,\quad S_r(2)=-4^{r-1},\quad
S_r(3)=1,\quad S_r(4)=4^{r-1}\qquad(r\geq1)
\]
illustrate the cancellation and sharp scale.

## Assumptions and scope

All indices and shifts are nonnegative integers; \(r\) is a nonnegative integer. A character value of zero means exactly that the Franel number is divisible by five. The scale \(4^r\), rather than \(5^r\), counts the active indices: \(\sum_{0\leq n<5^r}g(n)^2=4^r\). This theorem concerns a *fixed* shift in the correlation limit, although the subsequent finite-shift spectrum ranges over \(h<5^r\) after \(C(h)\) has been defined. It does not assert uniformity of the constant remainder as \(h\) grows. Nothing here asserts that \(g\) has nonzero ordinary natural-density autocorrelation; its correlations divided by \(5^r\) vanish at fixed shifts.

## Proof

**1. The digit character.** Lucas's binomial congruence says that, when \(n=\sum_i n_i5^i\) and \(j=\sum_i j_i5^i\) are written with base-five digits, then
\[
\binom nj\equiv\prod_i\binom{n_i}{j_i}\pmod5.
\]
Summing the cubes over all digit choices \(j_i\) independently gives
\[
F_n\equiv\prod_i F_{n_i}\pmod5.
\]
A direct evaluation at the five one-digit indices gives
\[
(F_0,F_1,F_2,F_3,F_4)\equiv(1,2,0,1,1)\pmod5.
\]
Since \(2\) is a quadratic nonresidue modulo five, the digit-character weights are
\[
(w_0,w_1,w_2,w_3,w_4)=(1,-1,0,1,1),
\qquad g(n)=\prod_iw_{n_i}.
\]
Leading zero digits do not change this product. Hence the active count is exactly \(4^r\), and the unshifted correlation is \(S_r(0)=4^r\).

**2. Exact shifted recurrence.** Write \(h=5q+a\), with \(0\leq a\leq4\), and split \(n=5m+d\), with \(0\leq d\leq4\). The addition \(d+a\) has outgoing carry either zero or one, so
\[
S_r(5q+a)=A_aS_{r-1}(q)+B_aS_{r-1}(q+1)
\qquad(r\geq1),
\]
where
\[
A_a=\sum_{0\leq d<5-a}w_dw_{d+a},\qquad
B_a=\sum_{5-a\leq d\leq4}w_dw_{d+a-5}.
\]
The five exact ordered pairs \((A_a,B_a)\), for \(a=0,1,2,3,4\), are
\[
(4,0),\quad(0,1),\quad(-1,0),\quad(0,-1),\quad(1,0).
\]
The boundary is \(S_0(h)=g(h)\), since the sum contains only \(n=0\). In particular, \(S_r(1)=S_{r-1}(1)=-1\).

**3. Existence and stabilized remainder.** For each fixed \(h\geq2\), the above recurrence expresses \(S_r(h)\) as one signed term equal to \(4S_{r-1}(q)\), \(S_{r-1}(q)\), or \(S_{r-1}(q+1)\), up to sign, with the new shift strictly smaller than \(h\). Induction on \(h\), starting with \(S_r(0)=4^r\) and \(S_r(1)=-1\), therefore shows that
\[
S_r(h)=a_h4^r+b_h
\]
for all sufficiently large \(r\), with rational \(a_h\) and integral \(b_h\). The same recurrence forces \(a_h\) to satisfy the displayed five rules for \(C\), with \(a_0=1\) and \(a_1=0\). This proves existence, uniqueness and the eventual constant remainder. All nonzero coefficients arise by multiplying finitely many factors \(\pm1/4\), apart from steps with factor one.

**4. Complete shift spectrum.** To evaluate \(C(h)\) for the \(r\)-digit base-five words \(0\leq h<5^r\), read digits from least to most significant while tracking a state \(c\in\{0,1\}\). At each digit \(d\), the equation for \(C(5q+d+c)\) changes the state to \(c'\), multiplies by a sign, and multiplies by \(4^{-j}\), where \(j=0\) or \(1\). The ten possible transitions are explicitly:

| Incoming state | Digit | Next state | Multiplier |
|---|---|---|---|
| \(0\) | \(0,1,2,3,4\) | \(0,1,0,1,0\) | \(1,+1/4,-1/4,-1/4,+1/4\) |
| \(1\) | \(0,1,2,3,4\) | \(1,0,1,0,1\) | \(+1/4,-1/4,-1/4,+1/4,1\) |

The initial state is zero; terminal state zero has value \(C(0)=1\) and terminal state one has value \(C(1)=0\). Ignoring the signs but weighting a factor \(4^{-1}\) by a formal variable \(t\) gives the state transition matrix
\[
M(t)=\begin{pmatrix}1+2t&2t\\2t&1+2t\end{pmatrix}.
\]
Including the signs makes the signed transition matrix exactly the identity \(I_2\), because the two opposite-signed off-diagonal choices and two opposite-signed nonconstant diagonal choices cancel. Therefore the unsigned nonzero-magnitude polynomial and its signed version are respectively
\[
\begin{aligned}
P_r(t)&=(M(t)^r)_{00}=\frac{(1+4t)^r+1}{2},\\
Q_r(t)&=(I_2^r)_{00}=1.
\end{aligned}
\]
For \(j\geq1\), the coefficient of \(t^j\) in \(P_r\) is \(4^j\binom rj/2\) and the corresponding coefficient in \(Q_r\) is zero. Positive and negative counts are thus each one-half of the unsigned coefficient, or \(4^{j-1}\binom rj\). The constant coefficient corresponds only to \(h=0\), and \(P_r(1)=(5^r+1)/2\); all remaining \((5^r-1)/2\) shifts have zero correlation. This proves the complete spectrum.

**5. Sharp extreme shifts.** First remove all factors of five from a positive shift, since \(C(5q)=C(q)\). For the remaining shift \(5q+a\), with \(a\in\{1,2,3,4\}\), the relevant coefficient is \(\pm C(q)/4\) or \(\pm C(q+1)/4\). The recursion starts at \(C(0)=1\) and \(C(1)=0\), hence \(|C(h)|\leq1/4\) for all \(h>0\). To have magnitude \(1/4\), its predecessor must be zero, which is possible only for \(a=2\) or \(4\) with \(q=0\); the other cases have predecessor at least one and strictly smaller magnitude. Thus the reduced shifts must be \(2\) and \(4\), with values \(-1/4\) and \(+1/4\). Reinstating the removed factors of five yields precisely the claimed equality families.

## Verification

A standalone standard-library Python checker is supplied as `verify_franel5.py`. It evaluates 450 Franel numbers using the original binomial-cube sum, independently checks their Legendre symbols against the digit rule, compares direct shifted block sums for 151 shifts at each of five depths \(r=1,2,3,4,5\), checks eventual remainder stabilization and extremal classifications for the first 1999 positive shifts, and verifies every entry in the signed-magnitude spectrum for all shifts below \(5^r\), \(1\leq r\leq5\). All these checks passed. Finite checks are illustrations and error traps; the infinite theorem is proved by the preceding digit and matrix identities.

## Relationship to prior work

Classical Lucas congruences supply the digit factorization for binomial coefficients. Sun's *Congruences for Franel Numbers* (first publicly posted 2011-12-05) and Guo's *Proof of two conjectures of Z.-W. Sun on congruences for Franel numbers* (first publicly posted 2012-01-03) study Franel sums and congruences; their main theorems concern weighted sums of Franel terms modulo prime powers. Rowland and Yassawi's *Automatic congruences for diagonals of rational functions* (first publicly posted 2013-10-31) gives a general automata method and Lucas-product context, not the present evaluated signed shift spectrum. The exact Franel quadratic character at base five, the \(4^r\)-normalized all-lag correlation values, the complete binomial shift-spectrum and its sharp equality cases are the assertions here, not the pointwise digit property itself.

## Limitations

The result treats quadratic characters modulo exactly five and unwrapped complete base-five blocks. It does not give a uniform-in-shift bound on the stabilized remainders, a corresponding result for other primes, or a classification of every finite-window non-power-of-five correlation. A previously unlocated theorem on general strongly digit-multiplicative correlations might encode the same special case under a change of notation; this is a historical-priority limitation, not a gap in the proof. No independent mathematical validation is claimed.

## References

1. Z.-W. Sun, *Congruences for Franel Numbers*, arXiv:1112.1034 (first public version 2011-12-05), https://arxiv.org/abs/1112.1034 .
2. V. J. W. Guo, *Proof of two conjectures of Z.-W. Sun on congruences for Franel numbers*, arXiv:1201.0617 (first public version 2012-01-03), https://arxiv.org/abs/1201.0617 .
3. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635 (first public version 2013-10-31), https://arxiv.org/abs/1310.8635 .
4. É. Lucas, classical binomial congruence modulo a prime (1878); a historical survey is R. Meštrović, *Lucas' theorem: its generalizations, extensions and applications (1878–2014)*, arXiv:1409.3820, https://arxiv.org/abs/1409.3820 .
