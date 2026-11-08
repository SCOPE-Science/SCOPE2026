# Exact dyadic contact orders of central Delannoy numbers with their alternating signs

## Finding
For \(n\ge1\), define the central Delannoy number \(D_n=\sum_{j=0}^{n}2^j\binom nj^2\) and put \(t=\nu_2(n(n+1))\). Then
\[
\nu_2(D_n-(-1)^n)=\begin{cases}2,&t=1,\\3t,&t\ge2.\end{cases}
\]
This proves Lengyel's 2021 Conjectures 2 and 3 simultaneously, and consequently both parts of his Conjecture 1. A structural strengthening is the following cubic-contact identity. Put
\[
H(X)=1+\sum_{j\ge1}\frac{(-2)^j}{(j!)^2}\prod_{i=0}^{j-1}(X-i(i+1)).
\]
This series converges for every \(X\in4\mathbb Z_2\), and there exists a restricted 2-adic power series \(U(Y)\in1+2\mathbb Z_2\langle Y\rangle\) with
\[H(4Y)=1+64Y^3U(Y)\quad(Y\in\mathbb Z_2).\]
Here \(\mathbb Z_2\langle Y\rangle\) denotes power series whose coefficients tend 2-adically to zero. This is an exact order-three zero, not just a congruence at finitely many indices.

## Assumptions and scope
All valuations are normalized by \(\nu_2(2)=1\); \(\nu_2(0)=+\infty\). The integer theorem concerns every positive index, including odd indices. The interpolation is on the entire closed 2-adic disk \(4\mathbb Z_2\). The formula does not concern ordinary valuations of \(D_n\) itself (all central Delannoy numbers are odd), nor any odd-prime analogue.

## Proof
**Step 1: the symmetric interpolation.** Let \(N=n(n+1)\). The Legendre polynomial identity \(P_n(3)=D_n\), the parity law \(P_n(-3)=(-1)^nP_n(3)\), and
\[
P_n(-3)=\sum_{j=0}^{n}(-2)^j\binom nj\binom{n+j}{j}
\]
show that \(H(N)=(-1)^nD_n\), since \((n-i)(n+i+1)=N-i(i+1)\). Every term after index \(n\) vanishes at this \(N\).

**Step 2: two exact 2-adic cancellations.** Write the positive-index summand as
\[
a_j(X)=-\frac{2^jX}{j}\prod_{i=1}^{j-1}\left(1-\frac{X}{i(i+1)}\right).
\]
The linear coefficient of \(\sum_{j\ge1}a_j(X)\) is \(-\sum_{j\ge1}2^j/j=\log(1-2)=\log(-1)=0\). Since \(\sum_{i=1}^{j-1}1/(i(i+1))=1-1/j\), the quadratic coefficient is
\[
\sum_{j\ge1}\frac{2^j}{j}-\sum_{j\ge1}\frac{2^j}{j^2}=0.
\]
For completeness, the formal dilogarithm identity
\[
\operatorname{Li}_2(z)+\operatorname{Li}_2\!\left(\frac{z}{z-1}\right)=-\tfrac12\log^2(1-z)
\]
follows by differentiating both sides and comparing their zero constant terms. At \(z=2\), all series converge in \(\mathbb Q_2\), the substitution \(z/(z-1)\) again equals \(2\), and \(\log(-1)=0\). Hence \(2\operatorname{Li}_2(2)=0\), proving the second cancellation. Each individual coefficient series here converges 2-adically, because \(\nu_2(2^j/j^2)\to\infty\).

**Step 3: a uniform bound on the tail.** Substitute \(X=4Y\). Then
\[
\frac{a_j(4Y)}{64}=-\frac{2^{j-4}}jY\prod_{i=1}^{j-1}\left(1-\frac{4Y}{i(i+1)}\right).
\]
For every coefficient of this polynomial, its 2-adic valuation is at least \(j-4-\nu_2(j)-S_j\), where
\[
S_j=\sum_{i=1}^{j-1}\max(0,\nu_2(i(i+1))-2)
=\sum_{r\ge3}\left(\left\lfloor\frac{j-1}{2^r}\right\rfloor+\left\lfloor\frac{j}{2^r}\right\rfloor\right)\le\frac j2.
\]
The equality uses the fact that precisely one of \(i,i+1\) is even. For \(17\le j\le31\), \(\nu_2(j)\le3\); for \(j\ge32\), \(\nu_2(j)\le j/4\). Consequently the lower bound is at least \(1\) for every \(j\ge17\), and it tends to infinity with \(j\). Thus all coefficients in the normalized tail \(\sum_{j\ge17}a_j(4Y)/64\) are even 2-adic integers, and its coefficients tend to zero.

**Step 4: a finite exact coefficient certificate.** For \(1\le j\le16\), define \(a_1(X)=-2X\) and iterate
\[
a_{j+1}(X)=\frac{-2(X-j(j+1))}{(j+1)^2}a_j(X).
\]
Expand the rational polynomial \(64^{-1}\sum_{j=1}^{16}a_j(4Y)\). For degrees \(3,4,\ldots,16\), the exact 2-adic valuations of its coefficients are, respectively,
\[
0,1,7,3,5,5,10,8,10,9,13,12,14,12.
\]
These are finite rational calculations using the displayed recurrence; the included verifier checks them independently using elementary symmetric sums. In particular, the cubic coefficient is odd and every coefficient of degree at least four is even. Step 2 cancels the *total* linear and quadratic coefficients exactly; Step 3 shows the remaining infinite tail cannot change the just-established coefficient parities. Therefore
\[
H(4Y)-1=64Y^3(1+2V(Y)),\qquad V(Y)\in\mathbb Z_2\langle Y\rangle.
\]
For any positive integer \(n\) with \(t=\nu_2(n(n+1))\ge2\), set \(Y=n(n+1)/4\). Because \(1+2V(Y)\) is a unit,
\[
\nu_2(D_n-(-1)^n)=\nu_2(H(n(n+1))-1)=6+3(t-2)=3t.
\]

**Step 5: the first 2-adic stratum.** From the other Delannoy expression \(D_n=\sum 2^j\binom nj^2\),
\[D_n\equiv1+2n^2+4\binom n2^2\pmod8.\]
For \(n\equiv0,1,2,3\pmod4\), these residues are respectively \(1,3,5,7\pmod8\). The cases \(t=1\) are exactly \(n\equiv1,2\pmod4\), and there \(D_n-(-1)^n\equiv4\pmod8\), establishing valuation \(2\). This completes the proof.

## Verification
Run `python3 verify_delannoy.py` (Python standard library only). It reconstructs the fourteen rational coefficient valuations twice, independently via the recurrence and elementary symmetric sums; directly evaluates the Delannoy binomial sum at indices \(1\le n\le600\); and checks the stated tail bound at \(17\le j\le512\). The finite calculation supplies a small exact rational certificate for Step 4. The unrestricted conclusion uses Steps 1–5 and does not follow from the finite index search alone.

## Relationship to prior work
Central Delannoy numbers and their congruences were studied by Z.-W. Sun (arXiv:1009.2486, first posted 2010-09-13, especially its introduction and principal theorems) and Sun (arXiv:1602.00574, first posted 2016-02-01, particularly polynomial identities and congruences). Those sources concern weighted sums, polynomial integrality, and largely odd-prime congruences; the inspected theorem statements do not give this exact valuation of the difference with the parity sign. Crucially, T. Lengyel, *On Some p-adic Properties and Supercongruences of Delannoy and Schröder Numbers* (INTEGERS 21 (2021), A86), explicitly posed Conjectures 2 and 3 in Section 2: the sharp dyadic valuations of \(D_{4m+3}+1\) and \(D_{2m}-1\) for indices divisible by four. Those precisely match the previously unproved portions proved here, and imply his Conjecture 1. His Theorem 3 and Corollary 1 give weaker lower bounds. Reading the main result statements in Section 2 and relevant proofs in Section 3 confirmed that these were stated as conjectures, not established theorems. J. Mikić (arXiv:2311.14623) determines the 3-adic valuation of the central Delannoy numbers themselves using their Legendre representation; this is a different prime and a different integer being valued. The 2026 paper on valuations of \(P_n(p)\) treats Legendre polynomial values at primes; its advertised result does not directly determine \(\nu_2(P_n(3)-(-1)^n)\). An older identity with the same implications is not ruled out solely by search results.

## Limitations
The proof establishes the stated dyadic valuation and interpolation contact, not a classification at odd primes or a distribution of the unit quotients. The comparison with older literature is limited by indexing and not an independent priority certification. All computations are reproducible finite exact arithmetic; they do not replace the analytic tail argument.

## References
- Z.-W. Sun, *On Delannoy numbers and Schröder numbers*, arXiv:1009.2486 (2010), J. Number Theory 131 (2011), 2387–2397. https://arxiv.org/abs/1009.2486
- Z.-W. Sun, *Arithmetic properties of Delannoy numbers and Schröder numbers*, arXiv:1602.00574 (2016), J. Number Theory 183 (2018), 146–171. https://arxiv.org/abs/1602.00574
- T. Lengyel, *On Some p-adic Properties and Supercongruences of Delannoy and Schröder Numbers*, INTEGERS 21 (2021), A86, 1–20. https://sites.oxy.edu/lengyel/morepapers.html
- J. Mikić, *On new divisibility properties of generalized central trinomial coefficients and Legendre polynomials*, arXiv:2311.14623 (2023). https://arxiv.org/abs/2311.14623
- M. Alekseyev, T. Amdeberhan, J. Shallit and I. Vukusic, *On the p-adic valuations of values of Legendre polynomials*, arXiv:2505.08935 (2025). https://arxiv.org/abs/2505.08935
- OEIS A001850, central Delannoy numbers, https://oeis.org/A001850
