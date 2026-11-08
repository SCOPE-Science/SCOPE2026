# A sharp local prime-sieve lower bound for Zumkeller complements

## Finding
Call a positive integer *Zumkeller* if its positive divisors admit an equal-sum bipartition. For any odd integer \(N\), let \(R(N)\) count primes \(p\le N/2\) such that \(N-p\) is Zumkeller. Let \(q=q(N)\) be the least **odd prime** not dividing \(N\). Choose the least \(a\ge1\) satisfying \(q\le2^{a+1}-1\), and put \(B=2^a q\). Then, uniformly as odd \(N\to\infty\),
\[
\boxed{R(N)\ \ge\ \bigl(1-1/q+o(1)\bigr)
\frac{\operatorname{Li}(N/2)}{\varphi(B)}.}
\]
The \(o(1)\) is uniform in odd \(N\). Consequently, there are absolute constants \(c>0\) and \(N_0\) such that every odd \(N\ge N_0\) has **at least**
\[
\boxed{cN/(\log N)^3}
\]
representations \(N=p+z\) with \(p\le N/2\) prime and \(z\) Zumkeller. The threshold may be ineffective. This strengthens the previously established \(N/(100(\log N)^5)\) lower bound, and determines the asymptotic fraction of admissible prime residues within a natural moving modulus. No assertion is made about all small odd targets or about even targets.

## Assumptions and scope
All logarithms are natural, and \(\operatorname{Li}\) denotes the logarithmic integral. We use the classical prime number theorem \(\vartheta(y)=\sum_{p\le y}\log p\sim y\), and the uniform Siegel–Walfisz estimate: for each fixed \(A>0\), whenever \(Q\le(\log X)^A\) and \(\gcd(r,Q)=1\),
\[
\pi(X;Q,r)=\frac{\operatorname{Li}(X)}{\varphi(Q)}+O_A\left(Xe^{-c_A\sqrt{\log X}}\right),
\]
where \(c_A>0\) may be ineffective and the error is uniform in \(Q,r\). The result is an **unconditional asymptotic** lower bound for every odd target, not an exact representation-count formula.

## Proof
**1. Selecting a small coprime Zumkeller base.** Fix an odd \(N\) sufficiently large and let \(q\) be its least missing odd prime divisor. If \(q>2\log N\), every odd prime up to \(2\log N\) divides \(N\), implying
\[
\log N\ge \vartheta(2\log N)-\log2
=(2+o(1))\log N,
\]
a contradiction. Thus \(q\le2\log N\). Choose \(a\ge1\) minimal with \(q\le2^{a+1}-1\), put \(B=2^a q\), and note
\[
2^a<q,\quad B<q^2\le4(\log N)^2,\quad
Bq=2^a q^2<q^3\le8(\log N)^3,
\quad \gcd(N,Bq)=1.
\]
The integer \(2^b q\) is Zumkeller for **every** \(b\ge a\): write \(M_b=2^{b+1}-1\) and \(H=(q+1)M_b/2\); choose \(v=\lfloor H/q\rfloor\), \(u=H-qv\). Then \(0\le u<q\le M_b\) and \(0\le v\le M_b\). Their binary expansions select divisors from \(\{2^i\}\) and \(\{q2^i\}\) respectively, with combined sum \(u+qv=H\), half the total divisor sum of \(2^b q\). This is the classical two-prime Zumkeller criterion, here supplied with a direct certificate.

**2. A dense admissible subfamily modulo \(B\).** Consider primes \(p\le X=N/2\) satisfying
\[
p\equiv N\pmod B,\qquad p\not\equiv N\pmod{Bq}.
\]
These conditions say that \(N-p=Bm\) for an integer \(m\ge1\) with \(q\nmid m\). Write \(m=2^t m_0\), where \(t\ge0\) and \(m_0\) is odd. Then \(\gcd(m_0,2^{a+t}q)=1\), while \(2^{a+t}q\) is Zumkeller by step 1. A coprime multiple of a Zumkeller number is Zumkeller: multiply both classes of an equal-divisor-sum partition by each divisor of the coprime multiplier. Hence
\[
N-p=2^{a+t}q\,m_0
\]
is Zumkeller. Distinct admissible primes give distinct representations.

The rejected primes inside the single class \(p\equiv N\pmod B\) are precisely those in the unique refinement \(p\equiv N\pmod{Bq}\). Both residue classes are reduced because \(N\) is coprime to \(Bq\). The number of admissible primes is therefore **exactly**
\[
T(N)=\pi(X;B,N)-\pi(X;Bq,N).
\]
Euler's totient obeys \(\varphi(Bq)=q\varphi(B)\), since \(B=2^a q\). Thus, by Siegel–Walfisz, as both moduli are \(O((\log N)^3)\),
\[
T(N)=\frac{\operatorname{Li}(X)}{\varphi(B)}\left(1-\frac1q\right)
+O\!\left( X e^{-c_4\sqrt{\log X}}\right).
\]
The remainder is uniform over odd \(N\), and dividing it by \(\operatorname{Li}(X)/\varphi(B)\) gives \(o(1)\), uniformly: \(\varphi(B)\le B<4(\log N)^2\). Since \(R(N)\ge T(N)\), this proves the boxed local lower bound.

**3. The cubic logarithmic exponent.** Since \(q\ge3\), we have \(1-1/q\ge2/3\). Also \(\varphi(B)\le4(\log N)^2\) and \(\operatorname{Li}(N/2)\gg N/\log N\). For all sufficiently large odd \(N\), the uniform relative error above is smaller than a fixed positive fraction of the main term. Consequently \(R(N)\gg N/(\log N)^3\) with absolute implied constant, proving the second assertion. \(\square\)

## Verification
The standalone exact-integer file `verify.py` tests binary equal-sum divisor partitions for prime bases, checks coprime-multiplier stability, and checks the new refined-congruence characterization and corresponding explicit divisor partitions for a finite collection of odd targets. The finite verification is only a sanity check: the uniform infinite statement relies on the standard prime number theorem and Siegel–Walfisz estimate. A positive numerical cutoff is not obtained from the proof.

## Relationship to prior work
Somu–Kukla–Tran (2023) state the all-odd prime-plus-Zumkeller conjecture, prove most odd residue classes, and establish the coprime-multiple construction. Mahanta–Saikia–Yaqubi (2020) characterize the family \(2^a q\). An earlier quantitative result gives, for all sufficiently large odd \(N\), at least \(N/(100(\log N)^5)\) prime-plus-Zumkeller representations. The present theorem is **strictly stronger**: using the full reduced prime class modulo \(B\), and excluding only its index-\(q\) refinement to prevent a second \(q\)-factor, replaces the square modulus \(B^2=O((\log N)^4)\) by the pair \(B,Bq\) and improves the lower bound by two full logarithmic powers. Moreover it gives a uniform explicit local main term with proportion \(1-1/q\) of primes in the moving reduced class. Neither the two-prime Zumkeller criterion alone nor a finite interval census implies this count.

## Limitations
The claimed local estimate is a **lower bound** for all Zumkeller complements, not an exact global asymptotic. It neither proves an optimal exponent nor provides an explicit least threshold; the analytic uniformity can be ineffective. The method uses a special family of even Zumkeller numbers and leaves open stronger counts from other families. No claim is made for even targets, and the full conjecture for finitely many potentially exceptional odd integers below the unspecified threshold is not settled. Bibliographic uniqueness beyond inspected sources is not certified.

## References
1. S. T. Somu, A. Kukla, D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149 (first posted 2023-10-22), especially Lemma 2.1, Proposition 4.10, Proposition 4.12, Conjecture 4.20. https://arxiv.org/html/2310.14149v2
2. P. J. Mahanta, M. P. Saikia, D. Yaqubi, *Some properties of Zumkeller numbers and k-layered numbers*, Journal of Number Theory, DOI 10.1016/j.jnt.2020.05.003, especially Theorem 2.6. https://doi.org/10.1016/j.jnt.2020.05.003
3. J. Thorner, A. Zaman, *Refinements to the prime number theorem for arithmetic progressions*, arXiv:2108.10878 (2021), for a modern implication of the classical Siegel–Walfisz theorem. https://arxiv.org/abs/2108.10878
4. *Siegel–Walfisz theorem*, uniform prime-counting estimate for reduced classes of polylogarithmic modulus.
5. OEIS A368082, positive integers expressible as a Zumkeller number plus a prime. https://oeis.org/A368082
