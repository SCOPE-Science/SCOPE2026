# Exact prime-square period-stable lifts of generalized Fibonacci recurrences

## Finding
For any odd prime \(p\), put \(F_0=0\), \(F_1=1\), and \(F_{n+2}=aF_{n+1}+bF_n\), where \(a,b\) are integers and \(p\nmid b\). Let \(\pi_{a,b}(p^e)\) be the least positive period of this recurrence modulo \(p^e\). For each \((a_0,b_0)\in\mathbb F_p\times\mathbb F_p^\times\), consider the \(p^2\) coefficient pairs modulo \(p^2\) reducing to \((a_0,b_0)\).

The precise number of lifts satisfying \(\pi_{a,b}(p^2)=\pi_{a,b}(p)\) is
\[
\begin{cases}
1,&a_0^2+4b_0\ne0,\\
0,&a_0^2+4b_0=0\text{ and }p\ge5,\\
3,&a_0^2+4b_0=0\text{ and }p=3.
\end{cases}
\]
When \(p=3\), the three exceptional lifts are precisely those for which \(a^2+4b\equiv6\pmod9\). Summing over all \(p(p-1)\) base coefficient pairs gives exactly \((p-1)^2\) stable pairs modulo \(p^2\) for every \(p\ge5\) and exactly \(10\) stable pairs for \(p=3\). Every other lift has its period multiplied by \(p\) on passing from \(p\) to \(p^2\).

## Assumptions and scope
The prime \(p\) is odd, with no restriction on \(a\) and with \(p\nmid b\). All coefficient pairs are considered modulo \(p^2\), not up to scaling or conjugation. The discriminant is \(\Delta=a^2+4b\). The period is the period of the normalized sequence with initial values \(0,1\), not merely the rank of apparition or a projective period. The finite-field scalar \(2^{-1}\) exists because \(p\) is odd.

## Proof
**1. From sequence periods to matrix orders.** Put
\[
M=\begin{pmatrix}a&b\\1&0\end{pmatrix}.
\]
Its determinant is \(-b\), a unit modulo \(p^2\). The identity \(M^n(1,0)^T=(F_{n+1},F_n)^T\) shows that a return of the sequence state to \((1,0)^T\) forces \(M^n=I\): the two vectors \((1,0)^T\) and \(M(1,0)^T=(a,1)^T\) form a basis, and any power of \(M\) fixing the first also fixes the second. Thus \(\pi_{a,b}(p^e)\) is the matrix order modulo \(p^e\). Let \(h\) be that order modulo \(p\). If \(M^h=I+pX\pmod{p^2}\), then \((M^h)^p=I\pmod{p^2}\). Hence the matrix order modulo \(p^2\) is exactly \(h\) or \(ph\).

**2. Separable characteristic polynomials.** Suppose \(\Delta_0=a_0^2+4b_0\ne0\pmod p\). The polynomial \(T^2-a_0T-b_0\) has distinct nonzero roots \(\alpha,\beta\) in \(\mathbb F_{p^2}\), either both in \(\mathbb F_p\) or exchanged by Frobenius. Consequently \(h\) is their least common multiple of multiplicative orders and \(p\nmid h\). In the unramified degree-two extension of \(\mathbb Z/p^2\mathbb Z\), each root has exactly one lift \(\widehat\alpha\), respectively \(\widehat\beta\), satisfying \(z^h=1\): the derivative \(hz^{h-1}\) is invertible modulo \(p\). Their sum and product are invariant under Frobenius, so
\[
a=\widehat\alpha+\widehat\beta,\qquad
b=-\widehat\alpha\widehat\beta
\]
lie in \(\mathbb Z/p^2\mathbb Z\). This pair reduces to \((a_0,b_0)\). Its companion matrix is diagonalizable in the splitting ring (the difference of the roots is a unit) and satisfies \(M^h=I\). Conversely, for any period-stable pair, the characteristic roots lift \(\alpha,\beta\) and satisfy \(z^h=1\); the uniqueness of those lifts forces the same \(a,b\). Thus exactly one stable coefficient lift exists in the separable case.

**3. Repeated-root characteristic polynomials.** Suppose \(\Delta_0=0\). Then \(a_0\ne0\), because \(b_0\ne0\). In \(R=\mathbb Z/p^2\mathbb Z\), set \(\lambda=a/2\), \(N=M-\lambda I\), and \(\delta=\Delta/4\). Direct multiplication gives \(N^2=\delta I\), with \(p\mid\delta\), and the lower-left entry of \(N\) equals \(1\). Modulo \(p\), \(M\) is a nontrivial Jordan block with eigenvalue \(\lambda_0=a_0/2\). Let \(t=\operatorname{ord}_{\mathbb F_p^\times}(\lambda_0)\), which divides \(p-1\). The order of this Jordan block is \(h=pt\).

For \(p\ge5\), expanding \((\lambda I+N)^p\), using \(N^2=\delta I\) and \(p\mid\delta\), gives
\[
M^p\equiv\lambda^pI+p\lambda^{p-1}N\pmod{p^2}.
\]
All terms with exponent at least two vanish modulo \(p^2\): the interior binomial coefficients contribute one \(p\), while \(N^j\) contributes an additional \(p\); the last term \(N^p=\delta^{(p-1)/2}N\) vanishes because \((p-1)/2\ge2\). Raising to \(t\) gives
\[
M^{pt}\equiv \lambda^{pt}I+pt\lambda^{pt-1}N\pmod{p^2}.
\]
The lower-left entry of this matrix is \(pt\lambda^{pt-1}\not\equiv0\pmod{p^2}\), hence \(M^h\ne I\) for every lift: none is stable.

For \(p=3\), instead the exact cubic expansion is
\[
M^3=(\lambda^3+3\lambda\delta)I+(3\lambda^2+\delta)N
\equiv\lambda^3 I+(3\lambda^2+\delta)N\pmod9.
\]
Here \(t=1\) or \(2\). Since \(\lambda^{3t}=1\pmod9\) for every unit \(\lambda\) reducing to order \(t\) modulo three, and \(3\mid(3\lambda^2+\delta)\), the lower-left entry of \(M^{3t}-I\) vanishes modulo nine exactly when \(3\lambda^2+\delta=0\pmod9\). Since \(\lambda^2=1\pmod3\), this is equivalent to \(\delta=6\pmod9\), hence to \(\Delta=6\pmod9\). Under this condition the scalar part is also \(I\); otherwise the offdiagonal obstruction remains. For each of the three choices of \(a\) above \(a_0\), the condition \(a^2+4b=6\pmod9\) specifies exactly one of the three choices of \(b\), so there are exactly three stable lifts.

**4. Count base parameter pairs.** For each \(a_0\in\mathbb F_p^\times\), the equation \(a_0^2+4b_0=0\) specifies one nonzero \(b_0\). It has no admissible solution when \(a_0=0\). Hence there are \(p-1\) repeated-root pairs and \(p(p-1)-(p-1)=(p-1)^2\) separable pairs. The preceding counts yield the stated global totals. Step 1 proves that every nonstable lift has period exactly \(ph\), completing the proof.

## Verification
A standalone exact-integer script, `artifacts/verify.py`, enumerates all admissible coefficient pairs modulo \(p^2\) for \(p\in\{3,5,7,11,13,17\}\), computes each base matrix period, checks the lifted period using modular matrix powers, and checks the predicted stable-lift count for each base pair. For \(p\in\{3,5,7\}\), it independently computes every lifted period by iterating the recurrence state. Output: `VERIFY_OK matrix_lifts=120894 recurrence_checks=2612`. The proof, not the finite checks, establishes the conclusion for all odd primes.

## Relationship to prior work
Renault's Theorems 2–3 give general prime-power period growth alternatives and base-field discriminant cases; his example \((a,b,p)=(76,56,3)\) exhibits stability, but no classification of all parameter lifts modulo \(p^2\) is given. Li investigates related rank and period growth and explicitly raises the problem of finding coefficient parameters for exceptional equality. Pal–Venkatesan study prime-power divisibility and matrix identities for related recurrences, not the number or precise locus of coefficient lifts preserving the period. The result here treats the coefficient space at a **fixed prime** rather than proving anything about the set of primes exceptional for a **fixed integer recurrence**.

## Limitations
The result excludes \(p=2\), nonunit constant coefficients, and lifts beyond \(p^2\). It is not a solution to the classical Wall–Sun–Sun problem for the fixed Fibonacci recurrence. The originality assessment is literature-based, not an exhaustive historical-priority guarantee; a more general unpublished or older matrix-lifting classification could subsume it. The source work appeared in a 2013 journal issue; the verified public author-upload date used for source eligibility is February 20, 2015, not an asserted date of the original journal's first availability.

## References
1. Marc Renault, *The Period, Rank, and Order of the (a,b)-Fibonacci Sequence Mod m*, Mathematics Magazine **86** (2013), 372–380, DOI: 10.4169/math.mag.86.5.372. Full text: https://webspace.ship.edu/msrenault/fibonacci/RenaultPeriodRankOrderMathMag.pdf.
2. Hua-Chieh Li, *On Second-Order Linear Recurrence Sequences: Wall and Wyler Revisited*, Fibonacci Quarterly **37** (1999), 342–349, DOI: 10.1080/00150517.1999.12428841. Scanned full text: https://www.fq.math.ca/Scanned/37-4/li.pdf.
3. Soumyabrata Pal and Shankar M. Venkatesan, *Prime Power Divisibility, Periodicity, and Other Properties of Some Second Order Recurrences*, arXiv:1509.03794 (first submitted September 13, 2015), https://arxiv.org/abs/1509.03794.
