# Two exact dyadic residue sections of the Perrin numbers

## Finding

Let the classical Perrin numbers be defined by \(P_0=3\), \(P_1=0\), \(P_2=2\) and \(P_{n+3}=P_{n+1}+P_n\) for all integers \(n\ge0\). Then, for each \(j\in\{1,3\}\) and all distinct nonnegative integers \(u,v\),

\[
\nu_2(P_{7u+j}-P_{7v+j})=1+\nu_2(u-v).
\]

Consequently, for every integer \(k\ge1\), the \(2^{k-1}\) numbers \(P_{7t+1}\) with \(0\le t<2^{k-1}\) represent **each even residue modulo \(2^k\) exactly once**, while the corresponding numbers \(P_{7t+3}\) represent **each odd residue exactly once**. Every residue modulo every power of two is therefore represented infinitely many times somewhere in the Perrin sequence, and

\[
\overline{\{P_n:n\ge0\}}^{\,(2)}=\mathbb Z_2.
\]

The entire Perrin sequence has least period \(7\cdot2^{k-1}\) modulo \(2^k\). This period is recorded numerically for initial moduli in OEIS A104217; the new assertion here is the exact all-depth collision law and its two canonical residue sections, not the period data alone.

## Assumptions and scope

All indices and residue computations are integers, with \(k\ge1\) and \(u,v,t\ge0\) wherever defined. The convention is \(\nu_2(m)\) for a nonzero integer \(m\); no valuation is assigned to zero in the displayed collision law. The closure is in the ring of \(2\)-adic integers, and is not a statement that every \(2\)-adic element is a term at an ordinary integer index. Index congruences are taken modulo \(2^{k-1}\) separately in each of the two arithmetic progressions.

## Proof

Define the integral matrix

\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix}.
\]

Its characteristic polynomial is \(X^3-X-1\), and \(P_n=\operatorname{tr}(M^n)\) for every \(n\ge0\): the trace has the same order-three recurrence and initial values \(3,0,2\). Exact integer matrix multiplication gives

\[
A=M^7=\begin{pmatrix}1&2&2\\2&3&2\\2&4&3\end{pmatrix}=I+2B,
\qquad
B=\begin{pmatrix}0&1&1\\1&1&1\\1&2&1\end{pmatrix},
\]

and

\[
A^2=I+4C,
\qquad C=\begin{pmatrix}2&4&3\\3&5&4\\4&7&5\end{pmatrix}.
\]

The four decisive exact trace computations are

\[
\begin{array}{c|cc}
j&\operatorname{tr}(M^jB)&\operatorname{tr}(M^jC)\\\hline
1&5&17\\3&7&29
\end{array},
\]

all of which are odd. Fix \(j\in\{1,3\}\) and write \(u=v+h\) with \(h>0\). The difference of Perrin terms is

\[
P_{7u+j}-P_{7v+j}=\operatorname{tr}\bigl(M^j A^v(A^h-I)\bigr).
\]

If \(h\) is odd, then \(A^h-I\equiv2B\pmod4\), while \(A^v\equiv I\pmod2\). Dividing the trace difference by two and reducing modulo two gives \(\operatorname{tr}(M^jB)\equiv1\pmod2\). Hence its valuation is precisely one.

If \(h=2^r w\) with \(r\ge1\) and \(w\) odd, repeated squaring of \(A^2=I+4C\) proves

\[
A^{2^r}=I+2^{r+1}C_r,
\qquad C_r\in M_3(\mathbb Z),\qquad C_r\equiv C\pmod2.
\]

Indeed, the squaring induction has \(C_{r+1}=C_r+2^r C_r^2\). Raising to an odd power then yields \((A^h-I)/2^{r+1}\equiv C\pmod2\). Since \(A^v\equiv I\pmod2\), the normalized trace difference is odd by \(\operatorname{tr}(M^jC)\equiv1\pmod2\). Its exact valuation is \(r+1=1+\nu_2(h)\). Interchanging \(u,v\) handles the opposite order. This establishes the collision law for all distinct pairs, not merely adjacent or experimentally sampled indices.

Because \(A\equiv I\pmod2\), all terms in the progression \(P_{7t+1}\) are even, and all those in \(P_{7t+3}\) are odd. For \(0\le t,s<2^{k-1}\), the collision law implies that two terms in the same progression are equal modulo \(2^k\) precisely if \(t\equiv s\pmod{2^{k-1}}\). Thus each progression contains \(2^{k-1}\) distinct residues of its fixed parity, hence exactly that entire parity class. The same argument shows each target has a unique index parameter modulo \(2^{k-1}\) in its prescribed progression.

To establish the stated least period, \(M\pmod2\) has order seven since \(M^7\equiv I\pmod2\), \(M\not\equiv I\pmod2\), and seven is prime. The odd entry in \(B\) makes \(A\) have order two modulo four; the odd entries in \(C\) and the same squaring induction show that \(A\) has order \(2^{k-1}\) modulo \(2^k\) for all \(k\ge2\). Therefore the order of \(M\) modulo \(2^k\) is \(7\cdot2^{k-1}\), also for \(k=1\). The vectors \((P_0,P_1,P_2)^T\), \((P_1,P_2,P_3)^T\) and \((P_2,P_3,P_4)^T\) have determinant \(-23\), a unit modulo every power of two. Any period of the scalar sequence fixes these three spanning state vectors under the companion matrix, hence forces the corresponding matrix power to be the identity. Consequently the scalar period is exactly the matrix order.

## Verification

The accompanying standalone script `check_perrin.py` checks all displayed integer matrices and odd trace certificates; the first twenty traces; all valuation comparisons for pairs of parameters below one hundred on the two distinguished progressions; exact least periods and both complete residue sections through modulus \(2^{10}\). It makes 11,956 grouped finite checks and reports PASS. These computations corroborate, but do not replace, the matrix argument for all indices and all powers of two.

## Relationship to prior work

The Perrin recurrence and its general history are recorded in OEIS A001608, while OEIS A104217 tabulates initial modular periods. Periodicity does not determine the exact pairwise collision law or the existence of parity-separated bijective residue sections. Herendi's general constructions concern *uniformly distributed entire linear recurrences* modulo powers of two; the present Perrin sequence is not uniformly distributed even modulo two (four odd values and three even values per seven-term period), and the theorem proved here concerns two subsequences. Bravo and Irmak (2024) classify valuations of the shifted Perrin numbers \(P_n+1\), which do not by themselves specify every target residue or every pairwise collision valuation. A later published study of Perrin residues modulo powers of three addresses a different local prime, not the dyadic sections. Earlier implicit coverage cannot be excluded without complete historical inspection.

## Limitations

The result does not classify every fiber of the *full* Perrin period; other index classes can produce additional representations, so overall residue frequencies need not be equal. The full historical priority of the specific two-section isometry has not been independently established, and not every relevant published work was available in complete full text. There has been no independent mathematical audit.

## References

1. OEIS A001608, *Perrin sequence*, https://oeis.org/A001608/internal.
2. OEIS A104217, *Period of Perrin sequence modulo \(n\)*, https://oeis.org/A104217/internal (initial contribution dated 2005-03-14; published initial period values).
3. E. Bravo and N. Irmak, *The 2-adic valuation of shifted Padovan and Perrin numbers and applications*, Turkish Journal of Mathematics 48 (2024), 1183–1196, https://doi.org/10.55730/1300-0098.3568.
4. T. Herendi, *Construction of uniformly distributed linear recurring sequences modulo powers of 2*, Uniform Distribution Theory 13 (2018), 109–129, https://doi.org/10.1515/udt-2018-0006.
5. *Complete ternary residue coverage and sharp minimum fibers of the Perrin sequence*, publicly indexed mathematical research record (2026-11-08), concerning residues modulo powers of three.
