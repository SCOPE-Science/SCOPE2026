# Complete eightfold binomial saturation profiles and sharp exceptional counts

## Finding
For every positive integer \(m\), define the number of eightfold-divisible interior entries in its proportional binomial row by
\[
E(m)=\#\left\{j\in\{1,2,3,4,5,6,7\}:8\mid\binom{8m}{jm}\right\}.
\]
Write \(o=m/2^{\nu_2(m)}\), the odd part of \(m\), and let \(s_2(t)\) be the number of ones in the binary expansion of a nonnegative integer \(t\). Then the exact universal formula is
\[
E(m)=7-2\mathbf1_{s_2(3o)\le2}-\mathbf1_{s_2(o)\le2}.
\tag{1}
\]
In particular, the only attainable values are \(4,5,6,7\), with a complete, disjoint classification:

- \(E(m)=4\) precisely when \(o\in\{1,3\}\).
- \(E(m)=5\) precisely when \(o=(2^b+1)/3\) for an **odd** integer \(b\ge5\), the corresponding Jacobsthal-number family.
- \(E(m)=6\) precisely when \(o=2^a+1\) for an integer \(a\ge2\).
- \(E(m)=7\) for every other positive integer \(m\).

For real \(X\ge0\), let \(H(X)=\#\{1\le m\le X:E(m)<7\}\). Define \(H_{\rm odd}(Y)\) to count the exceptional odd positive integers up to real \(Y\); it is zero for \(Y<1\), one for \(1\le Y<3\), and for \(Y\ge3\) equals
\[
H_{\rm odd}(Y)=\left\lfloor\log_2(\lfloor Y\rfloor-1)\right\rfloor
 +\left\lceil\frac12\left\lfloor\log_2(3\lfloor Y\rfloor-1)\right\rfloor\right\rceil-1.
\tag{2}
\]
The exact unrestricted count and its asymptotic are
\[
H(X)=\sum_{t\ge0}H_{\rm odd}(\lfloor X/2^t\rfloor)
=\frac34(\log_2 X)^2+O(\log X)\qquad(X\to\infty).
\tag{3}
\]
The sum terminates automatically when its argument becomes zero.

Finally, let \(A_8(n)=\#\{0\le k\le n:\gcd(n,\binom nk)=8\}\). For **every prime \(p>8\)**,
\[
A_8(8p)=E(p).
\tag{4}
\]
Hence \(A_8(8p)=5\) exactly for Jacobsthal primes \(p=(2^b+1)/3\) with odd \(b\ge5\); it equals \(6\) exactly for primes \(p=2^a+1\) with \(a\ge2\) (necessarily the familiar Fermat-prime exponents), and equals \(7\) for all remaining primes \(p>8\). There are **at most \(O(\log X)\)** exceptional primes \(p\le X\).

## Assumptions and scope
All assertions about \(E(m)\), including the binary formula, the disjoint exceptional families, and the quadratic-logarithmic counting law, hold for every positive integer \(m\), composite or prime. In (2), floors in the logarithm arguments ensure the count is well-defined for real cutoffs. The assertion about \(A_8(8p)\) requires \(p\) prime and \(p>8\); it does not assert the same identity for composite odd \(m\), where primes dividing \(m\) can affect the greatest common divisor. As usual, \(\nu_2(m)\) is the exponent of two in \(m\).

## Proof
**Step 1: reduce to odd multipliers.** Legendre's formula \(\nu_2(N!)=N-s_2(N)\) gives, for each \(1\le j\le7\),
\[
\nu_2\binom{8m}{jm}=s_2(jm)+s_2((8-j)m)-s_2(8m).
\tag{5}
\]
Multiplication of every argument by the same power of two does not change its binary digit sum. Consequently every valuation in (5), and therefore \(E(m)\), depends only on \(o\), the odd part of \(m\).

**Step 2: all seven valuations.** Assume that \(o\) is odd. For odd \(j\), both \(jo\) and \((8-j)o\) are odd, while their sum is \(8o\). The latter is divisible by eight. Binary addition of two odd integers whose sum is divisible by eight has a carry in each of positions zero, one, and two. Kummer's theorem therefore yields
\[
\nu_2\binom{8o}{jo}\ge3\quad (j=1,3,5,7).
\tag{6}
\]
For the other columns, (5) and \(s_2(2^t z)=s_2(z)\) give the **exact** valuations
\[
\nu_2\binom{8o}{2o}=\nu_2\binom{8o}{6o}=s_2(3o),
\qquad\nu_2\binom{8o}{4o}=s_2(o).
\tag{7}
\]
Thus four columns always satisfy the three-power threshold; the remaining two equal-valued columns fail precisely when \(s_2(3o)\le2\), and the center column fails precisely when \(s_2(o)\le2\). This proves (1).

**Step 3: solve the digit constraints.** An odd positive integer has binary digit sum at most two exactly when it is one or a sum of a positive power of two and one. Thus
\[
s_2(o)\le2\iff o=1\text{ or }o=2^a+1\ (a\ge1).
\tag{8}
\]
Likewise \(3o\) is odd; it cannot be a single power of two, so \(s_2(3o)\le2\) means \(3o=2^b+1\). Reduction modulo three forces \(b\) odd. For \(b=1,3\) this yields \(o=1,3\); for \(b\ge5\) it yields the stated Jacobsthal family. These two digit conditions overlap only at \(o=1,3\): if \(o=2^a+1\) with \(a\ge2\), then \(3o-1=2(3\cdot2^{a-1}+1)\) has exact two-adic valuation one and cannot equal \(2^b\) for \(b\ge3\). Substituting into (1) proves the disjoint four-value classification.

**Step 4: count the exceptions.** For odd \(o\le Y\), the value four occurs exactly twice once \(Y\ge3\). The value six occurs for \(a=2,3,\ldots,\lfloor\log_2(Y-1)\rfloor\), giving \(\lfloor\log_2(Y-1)\rfloor-1\) choices. The value five occurs for odd \(b=5,7,\ldots,\lfloor\log_2(3Y-1)\rfloor\), giving \(\lceil\lfloor\log_2(3Y-1)\rfloor/2\rceil-2\) choices. Their sum is (2); its two small cases are immediate. Each positive \(m\) has a unique representation \(m=2^t o\) with \(o\) odd, proving the exact sum in (3). From (2), uniformly for \(Y\ge1\), \(H_{\rm odd}(Y)=\tfrac32\log_2Y+O(1)\); summing over \(0\le t\le\lfloor\log_2X\rfloor\) yields \(\tfrac34(\log_2X)^2+O(\log X)\).

**Step 5: recover the prime-row GCD statistic.** Suppose \(p>8\) is prime. If \(\gcd(8p,\binom{8p}{k})=8\), then \(p\nmid\binom{8p}{k}\). The identity \(k\binom{8p}{k}=8p\binom{8p-1}{k-1}\) implies \(p\mid k\). Excluding the endpoints, write \(k=jp\), \(1\le j\le7\). Lucas's congruence gives
\[
\binom{8p}{jp}\equiv\binom8j\not\equiv0\pmod p,
\]
since all prime factors of \(\binom8j\) are at most seven. Hence its GCD with \(8p\) is exactly eight if and only if \(8\mid\binom{8p}{jp}\). Counting such \(j\) proves (4). The two exceptional families have \(O(\log X)\) members at most \(X\), so the prime restriction has the same bound. This proves all assertions.

## Verification
The standalone file `check.py` uses Python 3's exact integer arithmetic and needs no third-party package. Run `python3 check.py` after extraction. It checks the formula and complete classification against direct binomial-coefficient residues for all \(1\le m\le180\), independently tests the prime-row greatest-common-divisor identity for every prime \(8<p\le251\), verifies the exact odd and unrestricted exceptional counts at 15 cutoffs up to one million, and tests the closed-form classification at all \(1\le m\le100000\). The recorded successful output is reproducible; the infinite statements follow from the proof, not from finite tests.

## Relationship to prior work
Chai Wah Wu's *Computing the Greatest Common Divisor of Binomial Coefficients* (publicly posted June 18, 2026, arXiv:2606.20940v1) studies the GCD across **all** coefficients of a proportional row. That invariant does not determine the number of individual columns attaining a prescribed valuation threshold. Cui and Yang's *The distribution of greatest common divisors of binomial coefficients and their upper indices* (arXiv:2611.25794v1, November 19, 2026), whose Lemma 2.1 and Corollary 6.3 address the corresponding GCD statistic, show that \(A_d(dp)=d-1\) for all but a power-saving exceptional set of primes. Their result does not state this **exact** special-value classification at \(d=8\), nor the complete all-multiplier two-adic count. The present result uses the classical Legendre–Kummer and Lucas identities, so priority for an unindexed or implicit specialization cannot be ruled out by search alone.

## Limitations
The theorem is specific to the \(2^3\) threshold in proportional rows with factor eight; it neither classifies the full GCD for every composite multiplier nor proves that the Jacobsthal or Fermat prime-exception families contain infinitely many primes. The sequence names and binary-arithmetic lemmas are classical; the claimed contribution is their specific exact **column-count classification** and exceptional count. The supplied checker is only finite corroboration. Any independent literature or mathematical assessment remains outstanding.

## References
1. Chai Wah Wu, *Computing the Greatest Common Divisor of Binomial Coefficients* \(\binom{mn}{mk}\), arXiv:2606.20940v1 (first public June 18, 2026); revised August 4, 2026. https://arxiv.org/abs/2606.20940
2. Zhoulin Cui and Zhishan Yang, *The distribution of greatest common divisors of binomial coefficients and their upper indices*, arXiv:2611.25794v1 (November 19, 2026), especially Lemma 2.1 and Corollary 6.3. https://arxiv.org/html/2611.25794v1
3. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, J. Reine Angew. Math. 44 (1852), 93–146 (carry criterion).
4. É. Lucas, *Théorie des fonctions numériques simplement périodiques*, Amer. J. Math. 1 (1878), 184–240, 289–321 (congruence).
5. The OEIS Foundation, sequence A001045, Jacobsthal numbers. https://oeis.org/A001045
