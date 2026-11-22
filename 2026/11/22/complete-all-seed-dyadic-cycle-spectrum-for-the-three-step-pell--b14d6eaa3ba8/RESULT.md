# Complete all-seed dyadic cycle spectrum for the three-step Pell recurrence

## Finding
For every integer \(k\geq1\), consider the recurrence-state permutation
\[
T_k(a,b,c)=(2a+b+c,a,b)\pmod{2^k}
\]
on \((\mathbb Z/2^k\mathbb Z)^3\). The zero state is the unique fixed point. For every \(0\le j<k\), there are exactly \(4^j\) distinct directed cycles of least period \(7\cdot2^j\), and there are no other cycles. In particular, the total number of cycles is
\[
1+\sum_{j=0}^{k-1}4^j=\frac{4^k+2}{3}.
\]
More precisely, every nonzero state \(\mathbf v=(a,b,c)\), with truncated coordinate valuation
\[
t=\min\{\nu_2(a),\nu_2(b),\nu_2(c),k\}\in\{0,\ldots,k-1\},
\]
has least period exactly \(7\cdot2^{k-t-1}\). Here \(\nu_2(0)=+\infty\), and the minimum is independent of the choice of integer representatives after truncation at \(k\).

## Assumptions and scope
The parameter \(k\) is any positive integer, with arbitrary ordered initial triple modulo \(2^k\). This is the order-three specialization of the generalized Pell recurrence \(u_{n+3}=2u_{n+2}+u_{n+1}+u_n\). We count directed cycles under the state update, not occurrences of a single scalar residue or cyclic rotations as different cycles. The claim concerns powers of two, not arbitrary moduli or general recurrence order.

## Proof
Set
\[
M=\begin{pmatrix}2&1&1\\1&0&0\\0&1&0\end{pmatrix},\qquad \det M=1.
\]
Thus \(M\) is invertible modulo every \(2^k\) and all states are periodic. The characteristic polynomial of its reduction modulo two is \(X^3+X+1\), irreducible over \(\mathbb F_2\) (neither \(0\) nor \(1\) is a root). Hence \(M\) identifies with multiplication by a nonidentity element of \(\mathbb F_8^\times\), a group of prime order seven. Its action on the seven nonzero states modulo two is one seven-cycle, and the zero state is fixed.

The following exact integral computation is the lifting certificate:
\[
M^7=\begin{pmatrix}545&298&214\\214&117&84\\84&46&33\end{pmatrix}
=I+2B,\qquad
B=\begin{pmatrix}272&149&107\\107&58&42\\42&23&16\end{pmatrix},\qquad \det B=87.
\]
In particular, \(B\) is invertible over \(\mathbb Z_2\). Squaring gives
\[
M^{14}=I+4C,\quad C=B+B^2,\quad
C\equiv\begin{pmatrix}1&0&1\\1&1&1\\1&1&0\end{pmatrix}\pmod2,
\quad \det C=7569.
\]
Therefore \(C\) is invertible over \(\mathbb Z_2\). For every \(j\geq1\), repeated squaring yields
\[
M^{7\cdot2^j}=I+2^{j+1}C_j,\qquad C_j\equiv C\pmod2.
\]
Indeed, if this holds at \(j\), its square has the same form with \(C_{j+1}=C_j+2^jC_j^2\), which is congruent to \(C_j\) modulo two. With \(C_0=B\), every \(C_j\) is thus invertible modulo two (the base \(j=0\) is checked separately).

For nonzero \(\mathbf v\) of truncated coordinate valuation \(t\), multiplication by any such \(C_j\) preserves the minimal coordinate valuation. Consequently,
\[
\min_i\nu_2\big((M^{7\cdot2^j}-I)\mathbf v\big)_i=t+j+1
\]
as an identity in \(\mathbb Z_2\) for any lift of \(\mathbf v\) whose minimum valuation is \(t\). Reduction modulo \(2^k\) therefore fixes \(\mathbf v\) at this iterate if and only if \(t+j+1\geq k\). Because every nonzero reduced state has period seven modulo two, and the displayed iterate \(7\cdot2^{k-t-1}\) fixes \(\mathbf v\), the exact period is \(7\cdot2^{k-t-1}\); its only possible proper divisors consistent with the mod-two period are ruled out by the valuation formula.

There are exactly \(2^{3(j+1)}-2^{3j}=7\cdot8^j\) states of coordinate valuation \(t=k-j-1\). Each of their cycles has length \(7\cdot2^j\), so they form \(8^j/2^j=4^j\) cycles. Only the zero state lies in all three zero residue classes modulo \(2^k\), and it is fixed. This proves every assertion, including the absence of other periods.

## Verification
The standalone `CHECK.py` recomputes the integral matrix powers, \(\det B=87\), \(\det C=7569\), and the odd determinants of all fourteen tested normalized dyadic lifts. It independently enumerates the complete finite state-space orbits for \(1\le k\le5\), checking \(37{,}448\) states and \(458\) cycles against the stated valuation formula and cycle multiplicities. Run `python3 CHECK.py` in the directory containing this file. Finite checks corroborate the exact algebra; the unlimited range \(k\ge1\) is established by the repeated-squaring proof, not by enumeration.

## Relationship to prior work
Şiar, Keskin and Öztaş (published online September 29, 2022) define the generalized Pell recurrence with primary classification 11B39, but study perfect powers rather than modular all-seed orbits. Deveci, Avcı and Karaduman (2018) investigate generalized Pell periods for particular generating sets in finite nonabelian groups and refer to the ordinary period of the distinguished order-three Pell sequence. Their period information concerns a distinguished seed or specified group generators; it does not state the full least-period distribution over all triples in \((\mathbb Z/2^k\mathbb Z)^3\). The maximal period alone is not asserted to be new. Related results for ordinary two-step Pell and the generalized Narayana recurrence address different companion matrices; similarity of some possible periods does not identify their all-seed state sets with this recurrence.

## Limitations
The result is a self-reviewed mathematical claim without independent audit. An earlier general integral matrix-lifting theorem may subsume this specialization, or an unnoticed all-seed three-step Pell calculation may exist; a literature search cannot establish absolute novelty. The proof does not address odd prime powers, scalar image multiplicities, or generalized Pell orders other than three.

## References
1. Z. Şiar, R. Keskin, E. S. Öztaş, “On perfect powers in \(k\)-generalized Pell sequence,” *Mathematica Bohemica* 148 (2023), 507–518, published online September 29, 2022. https://doi.org/10.21136/MB.2022.0033-22 ; lawful full text: https://dml.cz/bitstream/handle/10338.dmlcz/151971/MathBohem_148-2023-4_6.pdf
2. Ö. Deveci, M. Avcı, E. Karaduman, “The periods of the \(k\)-step Fibonacci and \(k\)-step Pell sequences in finite-group products,” *An. Ştiinţ. Univ. Al. I. Cuza Iaşi. Mat.* 64 (2018), 283–292. https://www.math.uaic.ro/~annalsmath/pdf-uri_anale/F2%282018%29/Omur_Deveci.pdf
