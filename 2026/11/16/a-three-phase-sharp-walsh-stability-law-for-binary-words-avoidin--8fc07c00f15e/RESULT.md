# A three-phase sharp Walsh stability law for binary words avoiding \(001\)

## Finding
For each integer \(n\ge3\), let \(A_n\subseteq G_n=\mathbb F_2^n\) consist of the length-\(n\) binary strings containing no consecutive factor \(001\). For each frequency \(s\in G_n\), define the **unnormalized** Walsh multiplier
\[
W_n(s)=\sum_{x\in A_n}(-1)^{\langle s,x\rangle}.
\]
Write \(\delta_0=1\), \(\delta_1=2\), and \(\delta_2=4\). Then for **every** \(n\ge3\),
\[
\gcd\{W_n(s):s\in G_n\}
=\min\{|W_n(s)|: W_n(s)\ne0\}=\delta_{n\bmod3}.
\]
Moreover, \(W_n\) has no zero multiplier if and only if \(3\mid n\). Hence counting convolution \(T_nf=\mathbf1_{A_n}*f\), on \(\ell^2(G_n)\) with counting measure, is invertible precisely when \(3\mid n\). For every length, its Moore–Penrose inverse on its range and its positive-spectrum condition number obey
\[
\|T_n^\dagger\|_{2\to2}=\delta_{n\bmod3}^{-1},\qquad
\kappa_+(T_n)=\frac{F_{n+3}-1}{\delta_{n\bmod3}},
\]
where \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\).

## Assumptions and scope
All strings are linearly ordered, not cyclic, and the forbidden factor is the **contiguous** three-symbol word \(001\). The group law is coordinatewise binary addition, not concatenation. All Fourier transforms and convolutions are unnormalized; the scalar product in \(\ell^2\) uses counting measure. The identity is asserted for each integer \(n\ge3\) and every frequency \(s\in\mathbb F_2^n\), including the zero frequency. The multiplicity of positive spectral values and the total nullity in singular cases are not asserted.

## Proof
Let the three automaton states mean that the currently scanned permitted prefix ends with the longest prefix of \(001\) of length \(0,1,2\), respectively. A bit \(0\) has weight \(1\), and a bit \(1\) has weight \(\varepsilon\in\{+1,-1\}\). The transfer matrix, acting on row-state counts, is
\[
M(\varepsilon)=\begin{pmatrix}\varepsilon&1&0\\\varepsilon&0&1\\0&0&1\end{pmatrix}.
\]
The final transition that would complete \(001\) is absent. Thus, with \(e=(1,0,0)\) and \(\mathbf1=(1,1,1)^{\mathsf T}\),
\[
W_n(s)=eM(\varepsilon_1)\cdots M(\varepsilon_n)\mathbf1,
\qquad \varepsilon_i=(-1)^{s_i}.
\]
Put \(P=M(+1)\), \(N=M(-1)\). Direct integer multiplication gives
\[
N^3=I_3,\quad eN\mathbf1=eN^2\mathbf1=0,\quad
B=P^2N=\begin{pmatrix}-3&2&2\\-2&1&2\\0&0&1\end{pmatrix},\quad B\mathbf1=\mathbf1.
\]
It follows already that the all-negative sign choice has coefficient \(0\) for \(n\equiv1,2\pmod3\) and coefficient \(1\) for \(n\equiv0\pmod3\).

The unsigned count is \(a_n=eP^n\mathbf1=F_{n+3}-1\). One way to verify this for all \(n\ge0\) is to use \(P^3-2P^2+I_3=0\) and the three initial values \(a_0=1\), \(a_1=2\), \(a_2=4\). Consequently, when \(n\equiv0\pmod3\), the Fibonacci number \(F_{n+3}\) is even, so \(a_n\) is odd. Every signed coefficient is congruent to \(a_n\pmod2\), hence is odd and therefore nonzero. When \(n\equiv1\pmod3\), \(a_n\) is even, so **every** coefficient is even.

For \(n\equiv2\pmod3\) we establish the stronger divisibility by four. The Fibonacci sequence modulo four has period six, yielding \(a_n=F_{n+3}-1\equiv0\pmod4\). Let \(b_{n,i}\) count permitted strings with bit \(i\) equal to one. Writing
\[
J=\begin{pmatrix}1&0&0\\1&0&0\\0&0&0\end{pmatrix},
\qquad b_{n,i}=eP^{i-1}JP^{n-i}\mathbf1,
\]
we see that \(P^3\equiv I_3\pmod2\). Since \((i-1)+(n-i)=n-1\equiv1\pmod3\), the possible residue pairs of exponents are \((0,1)\), \((1,0)\), and \((2,2)\). The corresponding integer values of \(eP^rJP^t\mathbf1\) are \(2,2,12\), all even. Thus every \(b_{n,i}\) is even. For any mask \(s\), the number of permitted strings satisfying \(\langle s,x\rangle=1\) is congruent modulo two to \(\sum_{i:s_i=1}b_{n,i}=0\). Therefore
\[
W_n(s)=a_n-2\#\{x\in A_n:\langle s,x\rangle=1\}\equiv0\pmod4.
\]
This proves the three universal lower bounds \(1,2,4\) on the absolute value of every nonzero multiplier.

All three bounds are attained. For \(r\in\{0,1,2\}\), put \(m_r=3+r\). Direct multiplication gives
\[
eP^{m_0-1}N\mathbf1=1,\qquad
eP^{m_1-1}N\mathbf1=2,\qquad
eP^{m_2-1}N\mathbf1=4.
\]
For \(n=m_r+3k\) with any integer \(k\ge0\), take a frequency whose sign sequence consists of \(m_r-1\) positive signs, one negative sign, and then \(k\) copies of \((+1,+1,-1)\). Its signed sum is
\[
eP^{m_r-1}N B^k\mathbf1=eP^{m_r-1}N\mathbf1=\delta_r
\]
because \(B\mathbf1=\mathbf1\). The attained positive values establish both the exact minimum and the exact greatest common divisor.

Finally, the Walsh characters diagonalize counting convolution with eigenvalues \(W_n(s)\). The maximum absolute multiplier is \(W_n(0)=a_n\) by the triangle inequality. The smallest positive absolute multiplier is \(\delta_r\), hence the stated inverse-on-range norm and positive-spectrum condition number follow. The zero-existence criterion above gives the invertibility equivalence. \(\square\)

## Verification
The accompanying `checker.py` uses two separate exact-integer constructions: it generates every forbidden-factor-free word directly and performs a full in-place fast Walsh transform; it also computes a signed sum by the independent three-state dynamic-programming recurrence. All masks are cross-checked through \(n=10\), with deterministic additional masks through \(n=17\). The checker independently verifies \(N^3=I\), \(P^3\equiv I\pmod2\), the three marginal parities, all sharp witnesses, and the exact counts \(F_{n+3}-1\). Running `python3 checker.py` prints the marker `FORBIDDEN_001_SHARP_WALSH_PASS`; `certificate.json` records the complete small-dimension zero counts and sharp gap measurements. These finite experiments corroborate, but do not substitute for, the displayed all-length proof.

## Relationship to prior work
The forbidden-word graphs \(Q_n(f)\), and their combinatorial enumerators and isomorphism properties, precede this result. Azarija–Klavžar–Lee–Pantone–Rho (2014) treats forbidden factors, autocorrelation counting, and equivalence under reversal and bit-complementation; Wei–Zhang (2015) treats isometric embeddability and critical words. Neither inspected manuscript supplies an all-character Walsh multiplier bound or the exact nonzero spectral gap for \(f=001\). Known Fourier results for avoiding \(111\) and \(101\) concern different reversal-and-complement orbits of length-three factors: neither orbit contains \(001\). The general automaton and Fourier-transform techniques themselves are not claimed as new. The asserted contribution is the precise all-length spectral and stability statement above.

## Limitations
No formula for the entire zero-locus, the singular-case convolution rank, or the smallest *support size* of a zero-frequency character is proved. The theorem concerns only the linearly scanned forbidden factor \(001\), equivalently its reversed or complemented forms; cyclic avoidance and longer patterns are not included. Historic priority has been checked only against identified accessible sources and indexed search records. This report has not undergone independent mathematical validation.

## References
- J. Azarija, S. Klavžar, J. Lee, J. Pantone, and Y. Rho, *On Isomorphism Classes of Generalized Fibonacci Cubes*, first public arXiv version 2014-02-25, https://arxiv.org/abs/1402.6377.
- J. Wei and H. Zhang, *Proofs of Two Conjectures on Generalized Fibonacci Cubes*, first public arXiv version 2015-01-02, https://arxiv.org/abs/1501.00378.
- A. Ilić, S. Klavžar, and Y. Rho, *Generalized Fibonacci Cubes*, Discrete Mathematics 312 (2012), 2–11, https://doi.org/10.1016/j.disc.2011.02.015 (background definition and graph-theoretic context).
