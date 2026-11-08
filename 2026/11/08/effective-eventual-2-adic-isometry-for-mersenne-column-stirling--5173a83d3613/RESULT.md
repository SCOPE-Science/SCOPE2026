# Effective eventual 2-adic isometry for Mersenne-column Stirling differences

## Finding
For the Stirling numbers of the second kind \(S(N,k)\), fix any integer \(m\ge4\) and put \(k=2^m-1\), \(h=\nu_2(k!)=2^m-m-1\). Let \(a>b\ge1\), and let \(w=\nu_2(a-b)\). For every integer \(n\) satisfying
\[n\ge\max\{m,h+1\},\qquad 2^n\ge n+2+h+w,\]
the exact difference valuation is
\[\boxed{\nu_2(S(a2^n,k)-S(b2^n,k))=n+1+w.}\]
In fact, the stronger normalized congruence holds in the ring of \(2\)-adic integers:
\[\frac{S(a2^n,k)-S(b2^n,k)}{a-b}\equiv S(2^{n+1},k)-S(2^n,k)\pmod{2^{n+2}}.\]
Thus for each fixed \(m\ge4\), all distinct positive integer multiplier pairs eventually obey Lengyel's two-parameter Stirling-difference law; the threshold is fully effective. The normalization and comparison in this statement are part of the claim, not empirical approximations.

## Assumptions and scope
The Stirling number \(S(N,k)\) counts partitions of an \(N\)-element set into exactly \(k\) nonempty blocks; it is zero for \(N<k\). Here \(m,n,a,b\) are integers with the displayed restrictions, \(\nu_2(t)\) is the exponent of two in a nonzero integer \(t\), and \(h=k-m\) follows from Legendre's factorial formula because \(k=2^m-1\) has \(m\) binary ones. Congruences involving quotients are in \(\mathbb Q_2\); the proof shows the normalized quotient is actually in \(\mathbb Z_2\). The bound depends on the difference valuation \(w\), not on the magnitudes of \(a\) and \(b\).

## Proof
**1. Exact finite exponential representation.** The inclusion-exclusion formula, valid for every positive \(N\), is
\[S(N,k)=\frac1{k!}\sum_{j=1}^k(-1)^{k-j}\binom kj j^N.\]
Put \(q_j=j^{2^n}\), and write \(F(t)=S(t2^n,k)\) for positive integers \(t\). In each term, the coefficient \((-1)^{k-j}\binom kj/k!\) has \(2\)-adic valuation at least \(-h\).

**2. Uniform odd-base divided-difference estimate.** If \(j\) is odd, the lifting-the-exponent identity (or direct repeated squaring) shows \(q_j=1+z_j\) with \(\nu_2(z_j)\ge n+2\); this also covers \(j=1\), where \(z_j=0\). For \(d=a-b>0\), the binomial identity
\[\frac{q_j^a-q_j^b}d=q_j^b\left(z_j+\sum_{t=2}^d\frac{\binom dt}d z_j^t\right)\]
gives the estimate. Since \(\binom dt/d=\binom{d-1}{t-1}/t\), every summand with \(t\ge2\) has valuation at least \(t(n+2)-\nu_2(t)\ge2n+3\). Also \(q_j^b\equiv1\pmod{2^{n+2}}\); therefore
\[\frac{q_j^a-q_j^b}d\equiv z_j\equiv q_j^2-q_j\pmod{2^{2n+3}}.\]
Both congruences hold for all positive \(a>b\), even when \(d\) is highly divisible by two. After multiplying the rational coefficients and summing over odd \(j\), the odd-base contribution to
\[\frac{F(a)-F(b)}d-(F(2)-F(1))\]
has valuation at least \(2n+3-h\), which is at least \(n+2\) when \(n\ge h+1\).

**3. Uniform even-base bound.** For even \(j\), \(q_j\) is divisible by \(2^{2^n}\). The factor \(q_j^d-1\) is odd, so
\[\nu_2\left(\frac{q_j^a-q_j^b}d\right)\ge b2^n-w\ge2^n-w.\]
The coefficient \((-1)^{k-j}\binom kj/k!\) reduces the valuation by at most \(h\). Thus every even-base term in the normalized difference has valuation at least \(2^n-h-w\ge n+2\) by the explicit second hypothesis. The even-base terms in \(F(2)-F(1)\) also vanish modulo \(2^{n+2}\). Combining both groups proves the normalized congruence.

**4. Exact leading valuation and all quantifiers.** Zhao, Zhao and Hong, Theorem 1.3 in arXiv:1407.8443v1 (2014), prove
\[\nu_2\bigl(S(2^{n+1},2^m-1)-S(2^n,2^m-1)\bigr)=n+1\]
for all \(m\ge2\) and \(n\ge m\), with a single exception at \(m=n=2\). Our \(m\ge4\) range avoids this exception. The normalized quotient is congruent to an element of exact valuation \(n+1\) modulo \(2^{n+2}\), so it has exact valuation \(n+1\). Multiplying by \(d\) adds \(w=\nu_2(d)\), proving the stated identity for every permitted \(m,n,a,b\). The proof is infinite and does not depend on an enumerated cutoff.

## Verification
The standalone standard-library Python script `verify_stirling.py` computes Stirling differences by modular inclusion-exclusion, independently checks a bounded range against the integer Stirling recurrence, and tests the theorem through \(m=7\) including multiplier gaps divisible by \(2^{25}\). The verification run printed:

`VERIFY_OK direct_independent_cases=25 eventual_cases=48 m_range=4..7 big_gap_bits=25 counterexample_at_small_n=11`

The small-\(n\) counterexample is a boundary test: \(m=4\), \(n=4\), \(a=257\), \(b=1\) gives valuation \(11\), while the eventual right side would be \(13\). The verified computational cases are finite; the proof above supplies the unrestricted conclusion.

## Relationship to prior work
Lengyel (2009) proposed a two-parameter exact \(2\)-adic valuation law for Stirling differences. Zhao, Hong and Zhao (arXiv:1209.6284, 2012) proved the law when the column is not one less than a power of two. Zhao, Zhao and Hong (arXiv:1407.8443, 2014) proved the Mersenne-column multiplier-doubling law but explicitly left its unrestricted two-parameter analogue open for columns at least \(15\) (their discussion following Theorem 1.3, page 3). That multiplier-doubling theorem is used here as a premise, not claimed as new. The new ingredient is the uniform \(2\)-adic normalized divided-difference congruence, which transfers the known valuation from one multiplier pair to all positive multiplier pairs at a quantitative precision threshold. The 2019 Adelberg study of higher-order Bernoulli bounds concerns valuations of individual Stirling numbers and supplies useful context but does not state this difference-isometry result. Priority beyond the inspected published material remains subject to independent historical review.

## Limitations
The exponent cutoff is sufficient and may be much larger than the minimal valid exponent. It depends on \(\nu_2(a-b)\); it cannot be dropped uniformly for arbitrarily divisible multiplier differences. We do not classify the exceptional low-precision fibers, claim a sharp threshold, or establish analogous formulas for odd primes.

## References
1. T. Lengyel, “On the 2-adic order of Stirling numbers of the second kind and their differences,” *Discrete Mathematics & Theoretical Computer Science* (2009), DOI: 10.46298/dmtcs.2694.
2. J. Zhao, S. Hong, and W. Zhao, “Divisibility by 2 of Stirling numbers of the second kind and their differences,” arXiv:1209.6284 (first posted 2012-09-27; subsequent revision 2014), *Journal of Number Theory* 140 (2014), 324–348.
3. W. Zhao, J. Zhao, and S. Hong, “The 2-adic valuations of differences of Stirling numbers of the second kind,” arXiv:1407.8443v1 (2014-07-31), *Journal of Number Theory* 153 (2015), 309–320.
4. A. Adelberg, “The 2-Adic Analysis of Stirling Numbers of the Second Kind via Higher Order Bernoulli Numbers and Polynomials,” arXiv:1912.01090v1 (2019-12-02).
