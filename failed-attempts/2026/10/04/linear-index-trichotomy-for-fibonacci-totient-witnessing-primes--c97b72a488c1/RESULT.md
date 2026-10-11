# Linear-index trichotomy for Fibonacci-totient witnessing primes
## Finding
Let \(q\ne5\) be an odd prime, let \(p=kq+1\) be prime with \(k\ge2\), and assume that the Fibonacci rank of apparition \(z(p)\) divides the Pisano period \(\pi(q)\). Then \(k\) is even. For \(k\ge4\), writing \(d=z(p)\),
\[
d\mid
\begin{cases}
k,&\left(\frac{5}{p}\right)=+1,\\
k+2,&\left(\frac{5}{p}\right)=-1,\ \left(\frac{5}{q}\right)=+1,\\
2(k-2),&\left(\frac{5}{p}\right)=-1,\ \left(\frac{5}{q}\right)=-1.
\end{cases}
\]
Accordingly, \(p\) divides \(F_k\), \(F_{k+2}\), or \(F_{2(k-2)}\), respectively. In particular, the difficult nonresidue branch needs Fibonacci indices at most \(2k-4\), rather than divisors of \(k^2-4\).

Using the complete factorization table through \(F_{196}\), this makes the published range \(32\le k\le100\), previously stated only as computational evidence, deterministic. Together with the already proved range \(k\le31\), the uniqueness conclusion holds for every \(k\le100\): necessarily \(k=2\) and \(p=2q+1\).

## Assumptions and scope
The Fibonacci sequence is \(F_0=0\), \(F_1=1\), \(F_{n+2}=F_{n+1}+F_n\). For a prime \(r\), \(z(r)\) is the least positive \(m\) with \(r\mid F_m\), and \(\pi(r)\) is the Pisano period modulo \(r\). The result assumes \(q\) is an odd prime distinct from \(5\), \(p=kq+1\) is prime, and \(z(p)\mid\pi(q)\). No assertion is made for \(q=5\), which is a known exceptional discriminant prime.

The finite deterministic consequence uses only even \(k\) with \(4\le k\le100\). Its largest required Fibonacci index is \(2(100-2)=196\).

## Proof
Because \(q\) and \(p=kq+1\) are odd, \(k\) is even. Put \(d=z(p)\). Goel's Lemma 2.1 gives
\[
\left(\frac{5}{p}\right)=+1\Rightarrow d\mid p-1,
\qquad
\left(\frac{5}{p}\right)=-1\Rightarrow d\mid p+1,
\]
and, because \(d\mid\pi(q)\),
\[
\left(\frac{5}{q}\right)=+1\Rightarrow d\mid q-1,
\qquad
\left(\frac{5}{q}\right)=-1\Rightarrow d\mid2(q+1).
\]

If \((5/p)=+1\), then \(d\mid kq\). Also \(d\mid\pi(q)\mid q^2-1\), so \(\gcd(q,q^2-1)=1\) gives \(d\mid k\), exactly as in the published Case 1.

Assume now \((5/p)=-1\). Then \(d\mid kq+2\). If \((5/q)=+1\), then \(d\mid q-1\), so reducing \(kq+2\) modulo \(d\) gives \(d\mid k+2\). If \((5/q)=-1\), then \(d\mid2(q+1)\), and
\[
2(kq+2)-k\,2(q+1)=4-2k=-2(k-2),
\]
so \(d\mid2(k-2)\).

Since \(p\mid F_d\) and \(F_a\mid F_b\) whenever \(a\mid b\), the three divisibility statements for \(d\) imply the three claimed Fibonacci divisibilities for \(p\).

For \(4\le k\le100\), every candidate therefore occurs among the prime factors of one of \(F_k\), \(F_{k+2}\), or \(F_{2(k-2)}\), all with index at most \(196\). The cited factor table is complete there. Exhaustive exact screening leaves six prime pairs after the congruence, primality, and Legendre-symbol filters:
\[
(k,p,q)=(46,139,3),(50,151,3),(54,5779,107),(66,199,3),(70,911,13),(78,859,11).
\]
Their exact \((z(p),\pi(q))\) values are, respectively,
\[
(46,8),(50,8),(54,72),(22,8),(70,28),(78,10),
\]
so in every case \(z(p)\nmid\pi(q)\). Hence no \(k\in[4,100]\) survives.

## Verification
`factor_certificate.json` contains the complete factorizations used at the 74 distinct Fibonacci indices required by the three branches. `candidate_certificate.json` records every factor surviving the initial congruence/Legendre filters, gives a proper divisor for every composite quotient \((p-1)/k\), and records exact ranks and periods for the six prime quotients.

Running `python3 verify.py` from the package directory returns:
`VERIFY_OK k_range=4..100 factor_indices=74 screened=92 prime_candidates=6 survivors=0 max_index=196`.

The script reconstructs every required Fibonacci number exactly from its certified factors, redoes the complete branch screen, verifies the composite witnesses, and computes the six ranks and Pisano periods by exact modular Fibonacci arithmetic.

## Relationship to prior work
Goel's 2026 abstract phrases the witnessing-prime converse as a full conclusion, but the paper's Main Results and Theorem 4.2 explicitly label the uniqueness theorem partial: it is proved algebraically through \(k=12\), deterministically through \(k=31\), and the range \(32\le k\le100\) is reported only as non-deterministic evidence because Case 2 uses \(d\mid k^2-4\), reaching incompletely factored high-index Fibonacci numbers. The body further calls the universal statement conjectural and identifies this quadratic-index growth as the principal obstacle to a general algebraic proof. The comparison here therefore uses the theorem/proof scope rather than the broader abstract sentence.

The present sign-sensitive combination of the same rank and Pisano-period bounds replaces that Case 2 quadratic condition by \(d\mid k+2\) or \(d\mid2(k-2)\). This both removes the stated obstruction at the published \(k\le100\) boundary and supplies a reusable linear-index reduction for larger \(k\).

Targeted searches for the formulas \(z(p)\mid k+2\), \(z(p)\mid2(k-2)\), their equivalent Fibonacci divisibility formulation, and a deterministic upgrade of the \(k\le100\) range found no prior statement implying this result.

## Limitations
The theorem does not prove the conjectured uniqueness for all \(k\). The linear-index trichotomy still leaves a finite factorization problem whose size grows with \(k\). The factor-table argument here is asserted only through the published boundary \(k\le100\), where all required indices are at most \(196\). The proof also excludes \(q=5\), as required by the source theorem.

## References
1. A. Goel, *Sophie Germain Primes and the Totient of Fibonacci Numbers*, arXiv:2604.17847, first submitted 20 April 2026; primary MSC 11B39.
2. D. D. Wall, *Fibonacci Series Modulo m*, Amer. Math. Monthly 67 (1960), 525–532.
3. Brillhart–Montgomery–Silverman factorization tables, current Fibonacci factor table: https://mersennus.net/fibonacci/f1000.txt ; index page: https://mersennus.net/fibonacci/ .
