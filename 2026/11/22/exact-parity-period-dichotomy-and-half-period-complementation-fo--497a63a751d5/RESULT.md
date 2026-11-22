# Exact parity-period dichotomy and half-period complementation for \(k\)-generalized Pell numbers

## Finding
For each integer \(k\ge2\), define the generalized Pell sequence by
\[
P_{2-k}^{(k)}=\cdots=P_0^{(k)}=0,\qquad P_1^{(k)}=1,
\qquad P_n^{(k)}=2P_{n-1}^{(k)}+\sum_{j=2}^{k}P_{n-j}^{(k)}\quad(n\ge2).
\]
Let \(T_k\) be the *least* positive period of \(P_n^{(k)}\bmod2\), including the zero initial terms. Then
\[
\boxed{
\nu_2(T_k)=\begin{cases}1&k\equiv2\pmod4,\\0&k\not\equiv2\pmod4.\end{cases}}
\]
When \(k\equiv2\pmod4\), write \(T_k=2L_k\), where \(L_k\) is odd. The stronger **exact anti-period law** holds:
\[
\boxed{P_{n+L_k}^{(k)}\equiv P_n^{(k)}+1\pmod2\quad\text{for every integer }n.}
\]
Consequently the binary period is perfectly balanced (equal numbers of odd and even values) **if and only if** \(k\equiv2\pmod4\). For all remaining orders its least period is odd, precluding exact balance.

## Assumptions and scope
Only the displayed impulse initial conditions and recurrence are assumed. The integer \(k\) ranges over every \(k\ge2\); the modulus is exactly \(2\). Extend the periodic binary recurrence to negative indices uniquely, which is legitimate because the oldest coefficient is \(1\) modulo \(2\). The least period \(T_k\) refers to the full infinite binary sequence, not an eventually periodic tail. This theorem determines the complete \(2\)-primary part of \(T_k\), not its generally variable odd part.

## Proof
**Minimal denominator.** Work in \(\mathbb F_2\). The ordinary generating function of the sequence is
\[
F_k(z)=\sum_{n\ge0}(P_n^{(k)}\bmod2)z^n
=\frac{z}{D_k(z)},\qquad D_k(z)=1+z^2+\cdots+z^k.
\]
Its numerator and denominator are coprime since \(D_k(0)=1\). The denominator is therefore the unique monic-unit-normalized minimal recurrence denominator. The coefficient sequence is purely periodic, and its least period \(T_k\) is characterized exactly by
\[
D_k(z)\mid (1+z^{T_k})
\quad\Longleftrightarrow\quad
C_k(x)\mid(x^{T_k}+1),\qquad
C_k(x)=x^k+x^{k-2}+\cdots+x+1.
\]
Indeed, periodicity forces the reduced denominator to divide \(1+z^T\); conversely if it divides, the rational series has a numerator of degree less than \(T\), proving periodicity from index zero. Thus \(T_k\) is the multiplicative order of \(x\) in \(\mathbb F_2[x]/(C_k)\), where \(x\) is invertible because \(C_k(0)=1\).

**Exact repeated-factor analysis.** Put \(N_k(x)=(x+1)C_k(x)=x^{k+1}+x^k+x^{k-1}+1\). For odd \(k\),
\[
N_k'(x)=x^{k-1},\qquad N_k(0)=1,\qquad N_k'(1)=1.
\]
So \(N_k\) is squarefree, has the simple factor \(x+1\), and \(C_k\) is squarefree with \(C_k(1)=1\).

For even \(k\),
\[
N_k'(x)=x^{k-2}(x+1)^2,
\qquad C_k(1)=0,
\qquad C_k'(1)\equiv\frac{k-2}{2}\pmod2.
\]
Since \(N_k(0)=1\), the *only possible* repeated root of \(C_k\) is \(1\). If \(4\mid k\), the displayed derivative makes \(x+1\) a simple factor of \(C_k\), hence \(C_k\) is squarefree. If \(k\equiv2\pmod4\), the factor has multiplicity at least two in \(C_k\), while the derivative of \(N_k\) vanishes to *exactly* order two at \(1\). A root of multiplicity at least four in \(N_k\) would force its derivative to vanish to order at least three; thus \(N_k\) has multiplicity exactly three and \(C_k\) exactly two at \(1\). All remaining roots are simple. In this case
\[
C_k(x)=(x+1)^2Q_k(x),\quad Q_k\text{ squarefree},\quad Q_k(0)Q_k(1)=1.
\]

**Period and complementation.** Every squarefree polynomial over \(\mathbb F_2\) with nonzero constant term has odd \(x\)-order, as its irreducible factors embed into multiplicative groups of finite fields of odd order. This proves \(T_k\) odd whenever \(k\not\equiv2\pmod4\). In the remaining case define \(L_k\) as the order of \(x\) modulo \(Q_k\), with order \(1\) when \(Q_k=1\). It is odd. Modulo \((x+1)^2\), the unit \(x\) has order exactly \(2\); coprimality with \(Q_k\) gives \(T_k=\operatorname{lcm}(2,L_k)=2L_k\).

For the shift operator \(S\) acting on this binary sequence \(a=(a_n)\), write \(b=(S^{L_k}+1)a\). Because
\[
C_k(x)\mid (x+1)(x^{L_k}+1),
\]
we have \((S+1)b=0\). Over \(\mathbb F_2\), this means \(b_n\) is a constant independent of \(n\). It cannot equal zero, for then \(L_k\) would be a period of \(a\), contradicting the least period \(2L_k\). Hence \(b_n=1\) for every \(n\), giving the anti-period law. Each of the \(L_k\) pairs of terms separated by \(L_k\) has opposite parity, proving exact half-balance. When \(T_k\) is odd, half-balance is arithmetically impossible. \(\square\)

## Verification
The supplied independent-of-library script `check_parity.py` performs bitset polynomial arithmetic in \(\mathbb F_2[x]\), verifies the gcd/squarefreeness pattern at every order \(2\le k\le500\), directly enumerates complete binary state cycles for \(2\le k\le18\), and tests exact half-period complementation and parity counts in those complete cycles. Expected sample least periods at \(k=2,6,10,14,18\) are \(2,30,434,1638,114674\); for \(k=3,4,5\) they are \(7,7,31\). These are finite checks; the preceding algebraic proof establishes the theorem for every order.

Run `python3 check_parity.py` with any ordinary Python 3 supporting integer `bit_count`.

## Relationship to prior work
The general \(k\)-Pell recurrence appears in Kaggwa [1] and earlier Pell-sequence literature [2,3]. The 2015 work of Deveci and Karaduman [2] proves general periodicity, describes periods through companion matrices and calculates the usual \(k=2\) binary period; the 2018 paper of Deveci, Avcı and Karaduman [3] uses the general binary period \(hP_k(2)\) as an input to formulas for finite-group Pell sequences. Neither located treatment gives the global order-modulo-four classification of \(\nu_2(hP_k(2))\) or the half-period parity-complement involution. Kaggwa [1] addresses Wagstaff-prime occurrence, not modular periods. The result applies specifically to the recurrence with coefficient \(2\) at the first lag and coefficient \(1\) at every remaining lag; it is not the corresponding \(k\)-step Fibonacci period theorem.

## Limitations
The odd factor \(L_k\) is characterized as a finite-polynomial order, not given by a closed expression in \(k\). No theorem about periods modulo higher powers of two, divisibility by arbitrary odd moduli, or distribution of other residues is asserted. Prior-period work [2,3] is relevant and an equivalent statement not captured by the inspected portions or indices remains possible. The stand-alone finite enumeration is not the source of the general proof.

## References
1. Prosper Kaggwa, *On Wagstaff primes in the \(k\)-Pell number sequence*, arXiv:2611.01170 (first posted 31 October 2026), https://arxiv.org/abs/2611.01170.
2. Ömür Deveci and Erdal Karaduman, *The Pell Sequences in Finite Groups*, Utilitas Mathematica 96 (2015), 263–276, https://www.researchgate.net/publication/295591003_The_Pell_Sequences_in_Finite_Groups.
3. Ömür Deveci, Metin Avcı and Erdal Karaduman, *The periods of the \(k\)-step Fibonacci and \(k\)-step Pell sequences in finite groups*, An. Științ. Univ. Al. I. Cuza Iași. Mat. 64 (2018), 283–294, https://www.math.uaic.ro/~annalsmath/pdf-uri_anale/F2%282018%29/Omur_Deveci.pdf.
