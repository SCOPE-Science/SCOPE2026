# Prime-index irreducibility for two generalized-totient Lambert numerators

## Finding
For an integer \(a\ge 1\), let \(\tau\) be the divisor-counting function, and define the polynomial
\[
P_a(X)=\sum_{j=1}^{2a-1}\tau(\gcd(a,j))\min(j,2a-j)X^{j-1}.
\]
Define its companion polynomial by
\[
Q_a(X)=P_a(X)(1+X^a)^2-2X P_a(X^2).
\]
These are the two explicit Lambert-series numerators associated with the generalized totient in van der Kamp's 2012 work.

**Theorem.** For every prime \(p\), the polynomial \(P_p(X)\) is irreducible in \(\mathbb Q[X]\). For every prime \(p\equiv3\pmod4\), the quotient \(Q_p(X)/(1+X^2)\) is also irreducible in \(\mathbb Q[X]\). Both statements hold for unbounded degrees, and the first holds also at \(p=2\). For every odd prime \(p\), the related degree-\(2p-2\) polynomial
\[
H_p(Y)=\left(1+Y+\cdots+Y^{p-1}\right)^2+pY^{(p-1)/2}\left(1-Y+\cdots+Y^{p-1}\right)
\]
is irreducible in \(\mathbb Q[Y]\), with \(Q_p(X)=(1+X^2)H_p(X^2)\).

## Assumptions and scope
A prime means a positive rational prime. Polynomial irreducibility always means irreducibility over \(\mathbb Q\), not over \(\mathbb R\) or a finite field. For \(p\equiv3\pmod4\), the quotient is monic of degree \(4p-4\), including the case \(p=3\). No claim is made that this quotient is irreducible when \(p\equiv1\pmod4\), nor that either generalized polynomial is irreducible for all composite indices.

For \(p\) prime, write \(S_p(X)=\sum_{j=0}^{p-1}X^j\). The coefficient definition yields
\[
P_p(X)=S_p(X)^2+pX^{p-1}.
\]
Indeed, \(S_p(X)^2\) has triangular coefficients \(\min(j,2p-j)\) in degree \(j-1\), and the only changed coefficient is the central one, where \(\tau(\gcd(p,p))=2\).

## Proof
**1. First numerator.** The polynomial \(P_p\) is monic of degree \(2p-2\), and
\[
P_p(1)=p^2+p=p(p+1).
\]
Over \(\mathbb F_p\), the freshman's-dream identity gives
\[
S_p(X)=\frac{X^p-1}{X-1}\equiv (X-1)^{p-1}\pmod p.
\]
Consequently \(P_p(X)\equiv(X-1)^{2p-2}\pmod p\), so \(P_p(1+Y)\equiv Y^{2p-2}\pmod p\). Every nonleading coefficient of the translate is divisible by \(p\), its leading coefficient is \(1\), and its constant coefficient \(p(p+1)\) is divisible by \(p\) but not by \(p^2\). Eisenstein's criterion at \(p\), followed by the invertible translation \(X=Y+1\), proves \(P_p\) irreducible for every prime \(p\).

**2. Second numerator and its folded quotient.** Suppose \(p\) is odd and put
\[
T_p(Y)=\sum_{j=0}^{p-1}(-Y)^j=\frac{1+Y^p}{1+Y}.
\]
Using \(S_p(X)(1+X^p)=S_{2p}(X)=(1+X)S_p(X^2)\), direct substitution in the definition of \(Q_p\) gives
\[
\begin{aligned}
Q_p(X)&=S_{2p}(X)^2-2X S_p(X^2)^2+pX^{p-1}(1+X^{2p})\\
&=(1+X^2)\left(S_p(X^2)^2+p(X^2)^{(p-1)/2}T_p(X^2)\right)\\
&=(1+X^2)H_p(X^2).
\end{aligned}
\]
The polynomial \(H_p\) is monic of degree \(2p-2\) and satisfies \(H_p(1)=p^2+p\), because \(T_p(1)=1\). Its reduction modulo \(p\) is \(S_p(Y)^2\equiv(Y-1)^{2p-2}\). Thus \(H_p(1+Y)\) is Eisenstein at \(p\), and \(H_p\) is irreducible over \(\mathbb Q\) for every odd prime.

**3. Irreducibility after the quadratic substitution.** If \(p\equiv3\pmod4\), then \((p-1)/2\) is odd and \(T_p(-1)=p\). Therefore
\[
H_p(0)=1>0,\qquad H_p(-1)=1-p^2<0.
\]
There exists a root \(\alpha\in(-1,0)\) of \(H_p\). Because \(H_p\) is irreducible, \([\mathbb Q(\alpha):\mathbb Q]=2p-2\). Choose \(\beta\in\mathbb C\) with \(\beta^2=\alpha\). The field \(\mathbb Q(\alpha)\) is a subfield of \(\mathbb R\), so a negative \(\alpha\) cannot be a square there. Hence \([\mathbb Q(\beta):\mathbb Q(\alpha)]=2\), and the tower formula gives
\[
[\mathbb Q(\beta):\mathbb Q]=4p-4.
\]
But \(\beta\) is a zero of the monic polynomial \(H_p(X^2)\) of degree \(4p-4\). Its minimal polynomial therefore has the same degree, and \(H_p(X^2)=Q_p(X)/(1+X^2)\) is irreducible. This proves the theorem.

## Verification
The accompanying `verify.py` uses only Python's standard library. It compares both numerator identities coefficient-by-coefficient for the 15 primes at most 47, computes the coefficient lists of \(P_p(1+Y)\) and \(H_p(1+Y)\), verifies the complete Eisenstein divisibility tests, and evaluates the real-sign test for all sampled primes in the specified congruence class. Run with `python verify.py`; expected output begins `VERIFY_OK`. Separate symbolic factorization checks were performed for the primes \(3,5,7,11,13\), and agreed with the theorem. These are finite checks; the infinite results follow from the proof.

## Relationship to prior work
P. H. van der Kamp, *On the Fourier transform of the greatest common divisor* (public preprint, 16 January 2012, arXiv:1201.3139v1), derives these Lambert numerators in Sections 4.10 and 4.11 and remarks that the first appears irreducible and that the second appears irreducible apart from its \(1+X^2\) factor when the index is odd. Those polynomial identities and the proposed irreducibility questions are prior work; the prime-index Eisenstein arguments and the negative-real-root composition argument above are the claimed contribution.

L. J. Holleboom, *Prime number decomposition of the Fourier transform of a function of the greatest common divisor* (arXiv:1410.2054v1, 2014), studies prime-factor representations of the Fourier transform rather than polynomial irreducibility of the Lambert numerators. K. Dilcher and S. Robins, *Zeros and irreducibility of polynomials with gcd powers as coefficients* (Ramanujan J. 36, 2015), studies polynomials with coefficients \(\gcd(n,j)^k\), unlike the triangular, divisor-weighted coefficients here. Full text of the latter work was not obtained, so that comparison has a residual historical-priority risk.

## Limitations
The first conclusion does not settle the composite-index case, and the second does not settle odd primes congruent to \(1\pmod4\). The irreducibility of the folded polynomial \(H_p(Y)\) is established for every odd prime, but this fact alone does not imply irreducibility of \(H_p(X^2)\) when \(p\equiv1\pmod4\). Targeted literature and mathematical-record comparisons did not locate a covering proof, but absence of a search hit cannot certify historical uniqueness. No independent audit has been performed.

## References
1. P. H. van der Kamp, *On the Fourier transform of the greatest common divisor*, arXiv:1201.3139v1, submitted 2012-01-16, Sections 4.10–4.11. https://arxiv.org/abs/1201.3139
2. L. J. Holleboom, *Prime number decomposition of the Fourier transform of a function of the greatest common divisor*, arXiv:1410.2054v1, submitted 2014-10-08. https://arxiv.org/abs/1410.2054
3. K. Dilcher and S. Robins, *Zeros and irreducibility of polynomials with gcd powers as coefficients*, Ramanujan J. 36 (2015), 227–236. https://doi.org/10.1007/s11139-014-9579-2
4. Eisenstein's irreducibility criterion and the field-degree tower formula (classical standard results).
