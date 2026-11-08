# Exact two- and three-primary fourth-power sliding GCDs for the Pell companion pair

## Finding

Let the Pell numbers and associated Pell numbers be specified by
\[
P_0=0,\quad P_1=1,\qquad Q_0=Q_1=1,\qquad X_{n+2}=2X_{n+1}+X_n
\]
for either sequence \(X\). For each integer \(k\ge 1\), define the positive integer
\[
H_X(k)=\gcd_{n\ge0}\left(\sum_{j=1}^{k}X_{n+j}^{4}\right).
\]
Then for all \(k\ge1\), the following valuations are exact:
\[
\boxed{\nu_3(H_P(k))=\nu_3(H_Q(k))=
\begin{cases}
1+\nu_3(k),&4\mid k,\\
0,&4\nmid k;
\end{cases}}
\]
\[
\boxed{\nu_2(H_P(k))=
\begin{cases}
\nu_2(k)-1,&4\mid k,\\
0,&4\nmid k;
\end{cases}
\qquad \nu_2(H_Q(k))=\nu_2(k).}
\]
Equivalently, these formulas determine the exact largest divisors of \(H_P(k)\) and \(H_Q(k)\) supported on the primes \(2,3\), for every length \(k\).

## Assumptions and scope

The symbol \(\nu_p(a)\) is the exponent of the prime \(p\) in a nonzero integer \(a\). A GCD of the infinitely many positive window sums means their unique positive common gcd; it exists by the well-ordering of positive integers and is determined by some finite subcollection. Every starting index \(n\) is a nonnegative integer, and the windows begin at \(n+1\), not \(n\). We make no assertion about prime factors other than \(2\) and \(3\). The sequences are the standard Pell and *associated Pell* sequences with \(Q_0=Q_1=1\), not the differently normalized Pell-Lucas sequence with initial term \(2\).

## Proof

**1. A four-term polynomial and its step map.** Put \(v_n=(X_n,X_{n+1})^{\mathsf T}\). For an arbitrary integer vector \(v=(x,y)^{\mathsf T}\), the four following sequence terms are
\[
y,\quad x+2y,\quad 2x+5y,\quad 5x+12y.
\]
Consequently one four-term fourth-power sum is
\[
F(x,y)=y^4+(x+2y)^4+(2x+5y)^4+(5x+12y)^4
\]
\[
=642x^4+6168x^3y+22224x^2y^2+35592xy^3+21378y^4.
\]
Every coefficient is divisible by \(6\), so \(F\in6\mathbb Z[x,y]\). Four recurrence steps give
\[
v_{n+4}=Mv_n,\qquad
M=\begin{pmatrix}5&12\\12&29\end{pmatrix}.
\]
Note that \(M\equiv I\pmod4\) and \(-M\equiv I\pmod3\). Since \(F\) is homogeneous of even degree, \(F(-v)=F(v)\).

**2. Lifting a block sum.** Set \((U,p)=(M,2)\) or \((U,p)=(-M,3)\), and define the linear operator \(R\) on integral two-variable polynomials by \((RG)(v)=G(Uv)\), with \(\Delta=R-I\). Because \(U\equiv I\pmod{p}\), each application of \(\Delta\) to an integral polynomial introduces a factor of \(p\). Therefore, from \(F\in3\mathbb Z[x,y]\),
\[
\Delta^\ell F\in 3^{\ell+1}\mathbb Z[x,y]\quad(\ell\ge0)
\]
when \(U=-M\). For \(U=M\), every linear form \(L\) obeys \(L(Mv)=L(v)+4L(Av)\) with integral \(A=(M-I)/4\). Expanding the fourth power shows
\[
(L(Mv))^4-(L(v))^4\in16\mathbb Z[x,y].
\]
Summing over the four linear forms in \(F\) gives \(\Delta F\in16\mathbb Z[x,y]\), and further applications of \(\Delta\) contribute factors of \(4\):
\[
\Delta^\ell F\in 2^{2\ell+2}\mathbb Z[x,y]\quad(\ell\ge1).
\]

For each integer \(m\ge1\), the binomial theorem for commuting operators and the hockey-stick identity give the exact finite identity
\[
\sum_{j=0}^{m-1}R^jF
=\sum_{\ell=0}^{m-1}\binom m{\ell+1}\Delta^\ell F.
\]
The elementary bound
\[
\nu_p\!\left(\binom m{\ell+1}\right)
\ge \nu_p(m)-\nu_p(\ell+1)
\]
follows from \((\ell+1)\binom m{\ell+1}=m\binom{m-1}{\ell}\). For every \(\ell\ge1\),
\[
\ell+1-\nu_3(\ell+1)\ge2,\qquad
2\ell+2-\nu_2(\ell+1)\ge3.
\]
It follows that for every integral vector \(v\),
\[
\sum_{j=0}^{m-1}F(M^jv)\equiv mF(v)
\pmod{3^{\nu_3(m)+2}},
\]
\[
\sum_{j=0}^{m-1}F(M^jv)\equiv mF(v)
\pmod{2^{\nu_2(m)+3}}.
\]
Here the first congruence may use \(U=-M\), because \(F((-M)^jv)=F(M^jv)\).

**3. Exact valuations when \(4\mid k\).** Write \(k=4m\). The sum of the \(4m\) consecutive fourth powers starting at \(n+1\) is \(\sum_{j=0}^{m-1}F(M^jv_n)\). Since \(F\) is divisible by \(6\), the previous congruences show universal divisibility by \(3^{\nu_3(m)+1}\) and \(2^{\nu_2(m)+1}\). For the Pell sequence use \(n=0\):
\[
F(P_0,P_1)=F(0,1)=21378,
\qquad \nu_2(21378)=\nu_3(21378)=1.
\]
The errors have at least two further powers of \(2\) and one further power of \(3\), respectively. Therefore this single Pell window has exact valuations \(\nu_2(m)+1\) and \(\nu_3(m)+1\), proving both claimed minima for \(P\).

For the associated Pell sequence, every term \(Q_n\) is odd, so each fourth power is \(1\pmod{16}\). In particular \(F(v_n)\equiv4\pmod{16}\) for every \(n\), giving \(\nu_2(F(v_n))=2\). The two-adic lifting congruence then implies \(\nu_2\bigl(\sum_{j=1}^{4m}Q_{n+j}^4\bigr)=\nu_2(m)+2\) for every \(n\). For the three-adic upper bound choose \(n=1\), for which
\[
F(Q_1,Q_2)=F(1,3)=2911764,
\qquad \nu_3(2911764)=1.
\]
The lifting congruence gives exact three-adic valuation \(\nu_3(m)+1\) for this window. Since \(\nu_2(k)=\nu_2(m)+2\) and \(\nu_3(k)=\nu_3(m)\), the asserted formulas follow for all multiples of four.

**4. The other window lengths.** Modulo \(3\), any integer fourth power is \(0\) if its base is divisible by \(3\), and \(1\) otherwise. The zero positions for the Pell fourth-power sequence are precisely indices \(0\pmod4\); for the associated Pell fourth-power sequence they are indices \(2\pmod4\). Thus each four-term block sums to \(0\pmod3\), but for each length remainder \(1\), \(2\), or \(3\pmod4\) there is a starting index whose incomplete block sums to a nonzero residue. For \(P\), choose starts at index \(1\), \(1\), and \(2\) respectively (an index here is the first term in the window); for \(Q\), choose index \(1\) in all three cases. Hence \(3\nmid H_X(k)\) when \(4\nmid k\).

Modulo \(2\), \(P_n\equiv n\pmod2\). For \(k\equiv2\pmod4\), every length-\(k\) interval has an odd number of odd-indexed terms, so every Pell window is odd. For odd \(k\), one of the two possible index parities gives an odd number of odd-indexed terms. Hence \(2\nmid H_P(k)\) whenever \(4\nmid k\). Since all associated Pell terms are odd, their fourth powers are \(1\pmod{16}\): for odd \(k\) their sums are odd; for \(k\equiv2\pmod4\) every sum is \(2\pmod4\). Thus \(\nu_2(H_Q(k))\) is respectively \(0\) and \(1\), completing the proof.

## Verification

Run `python3 verify.py` using only the Python standard library. It checks the exact quartic coefficient certificate, 600 length-and-sequence combinations with lengths \(1\le k\le300\) using a gcd of twelve independently computed window sums, and 2100 block-lifting congruences for lengths \(4m\), \(1\le m\le150\), in seven starting positions for each of two sequences. Expected output is in `verification_output.txt`. These checks supplement rather than establish the infinite claim. The polynomial identity, operator divisibility bounds, and explicit sharp windows are the proof.

## Relationship to prior work

Mbirika, Schrader, and Spilker (first public version 2023-01-13, arXiv:2301.05758; Journal of Integer Sequences 26 (2023), article 23.6.4) define sliding GCDs of powers of Pell and associated Pell numbers in their Convention 1. Their sections 4–5 treat first powers; section 6.1 gives explicit squared-power results and asks further questions. The present statement concerns **fourth** powers and gives the complete \(2\)- and \(3\)-primary portions, rather than claiming a formula for the full gcd. Mbirika and Spilker (arXiv:2204.12626) study square powers for generalized Fibonacci sequences, not this fourth-power Pell pair. Frontczak (2018) studies fourth-power Fibonacci and Lucas sums for a different recurrence, with no sliding-GCD valuation classification; Anand et al. (arXiv:2407.12868) treat first-power Pell sums. Searching for direct forms, divisibility reformulations, broader Lucas-power GCD statements, and prior records did not identify a covering result. This literature comparison is not a proof of global novelty.

## Limitations

The values of \(\nu_p(H_X(k))\) at primes \(p\ge5\), and therefore generally the complete integer gcds, are **not determined**. This theorem is local at exactly two primes and exponent exactly four; it is not asserted for arbitrary Lucas sequences or other exponents. No independent external audit has been performed. An unindexed broader Lucas-sequence congruence theorem might imply these special formulas.

## References

1. aBa Mbirika, Janee Schrader, Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences 26 (2023), article 23.6.4. arXiv:2301.05758. https://arxiv.org/abs/2301.05758 ; full publisher PDF: https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.pdf . First public version: 2023-01-13.
2. aBa Mbirika, Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly 60 (2022), 255–269. arXiv:2204.12626. https://arxiv.org/abs/2204.12626 .
3. Robert Frontczak, *Sums of powers of Fibonacci and Lucas numbers: A new bottom-up approach*, Notes on Number Theory and Discrete Mathematics 24 (2018), 94–103. https://nntdm.net/papers/nntdm-24/NNTDM-24-2-094-103.pdf .
4. Navvye Anand, Amit Kumar Basistha, Kenny B. Davenport, Alexander Gong, Florian Luca, Steven J. Miller, Alexander Zhu, *Sum of Consecutive Terms of Pell and Related Sequences*, arXiv:2407.12868 (first posted 2024-07-13); first-power consecutive sums, different invariant. https://arxiv.org/abs/2407.12868 .
