# Prime-power Franel residues and the Wolstenholme-prime criterion

## Finding
Let \(f_n=\sum_{k=0}^{n}\binom nk^3\) be the Franel numbers, and let \(p\) be a prime and \(a\ge1\) be an integer. For \(p\ge5\), write \(B_j\) for the Bernoulli number with generating function \(x/(e^x-1)=\sum_{j\ge0}B_jx^j/j!\). Then
\[
 f_{p^a}\equiv2+\frac{p^3}{2}B_{p-3}\pmod{p^4}\qquad(p\ge5,\ a\ge1).
\]
The Bernoulli quotient is interpreted in the localization of the integers at \(p\); its denominator is prime to \(p\). In particular, the first nonzero possible \(p\)-adic digit of \(f_{p^a}-2\), after dividing by \(p^3\), is independent of \(a\). For every \(a\ge1\), the following statements are equivalent for primes \(p\ge5\):
\[
 p^4\mid f_{p^a}-2,\qquad p\mid\operatorname{num}(B_{p-3}),\qquad
 \binom{2p-1}{p-1}\equiv1\pmod{p^4}.
\]
The last condition defines a *Wolstenholme prime*. Hence \(\nu_p(f_{p^a}-2)=3\) for every non-Wolstenholme prime \(p\ge5\) and every \(a\ge1\), while the valuation is at least four when \(p\) is a Wolstenholme prime. At the two smaller primes there are unconditional exact values:
\[
 \nu_2(f_{2^a}-2)=\nu_3(f_{3^a}-2)=3\qquad(a\ge1).
\]
Consequently the conjectured criterion \(f_n\equiv2\pmod{n^3}\) for primality has **no composite prime-power solutions** \(n=p^a\) with \(a\ge2\) when \(p=2\), \(p=3\), or \(p\ge5\) is not a Wolstenholme prime. Nothing here rules out the as-yet unresolved Wolstenholme-prime powers, nor arbitrary composite indices.

## Assumptions and scope
Here \(p\) ranges over all rational primes and \(a\) over positive integers; \(\nu_p\) is the usual integer \(p\)-adic valuation. The congruence containing \(B_{p-3}\) concerns primes \(p\ge5\), so the denominator of that Bernoulli number is \(p\)-integral (von Staudt–Clausen or the standard elementary prime-integrality of \(B_j\) for \(0\le j<p-1\)). The assertion for \(p=3\) is separate. The equivalence with Wolstenholme primes uses the classical Glaisher congruence and does not claim priority for that classical result.

## Proof
**1. Uniform prime-power reduction.** Fix \(p\) and \(a\ge1\) and put \(N=p^a\). For every interior index \(1\le k<N\), the binomial identity
\[
 \binom Nk=\frac{p^a}{k}\binom{p^a-1}{k-1}
\]
shows, by Lucas's theorem (all base-\(p\) digits of \(p^a-1\) are \(p-1\)), that \(\binom{p^a-1}{k-1}\not\equiv0\pmod p\). Hence
\[
 \nu_p\!\binom Nk=a-\nu_p(k).
\]
Terms with \(p^{a-1}\nmid k\) have binomial valuation at least \(2\), so their cubes vanish modulo \(p^4\). The remaining interior indices are \(k=jp^{a-1}\) for \(1\le j<p\). Again by Lucas's theorem,
\[
 \frac1p\binom{p^a}{jp^{a-1}}=\frac1j\binom{p^a-1}{jp^{a-1}-1}
 \equiv\frac{(-1)^{j-1}}j\pmod p.
\]
The endpoint terms contribute \(2\), and therefore, **for every prime**,
\[
 f_{p^a}-2\equiv p^3\sum_{j=1}^{p-1}\frac{(-1)^{j-1}}{j^3}\pmod{p^4}.\tag{1}
\]
All displayed inverses exist modulo \(p\), and equation (1) proves independence from the prime-power exponent \(a\) without taking limits.

**2. The Bernoulli coefficient for odd primes.** Let \(p\ge5\). The full reciprocal-cube sum vanishes modulo \(p\), since \(j^{-3}\equiv j^{p-4}\pmod p\) and \(p-1\nmid p-4\). Subtracting twice the even-indexed terms yields
\[
 S_p:=\sum_{j=1}^{p-1}\frac{(-1)^{j-1}}{j^3}
 \equiv-\frac14\sum_{j=1}^{(p-1)/2}j^{-3}\pmod p.
\]
With \(m=p-3\), Faulhaber's Bernoulli-polynomial identity gives
\[
 \sum_{j=1}^{(p-1)/2}j^{-3}
 \equiv\frac{B_m((p+1)/2)-B_m(0)}m\pmod p.
\]
Here \(m\not\equiv0\pmod p\), and \(B_m(1/2)=(2^{1-m}-1)B_m\). By Fermat's theorem \(2^{1-m}=2^{4-p}\equiv8\pmod p\), so the right-hand side is \(6B_m/(-3)=-2B_m\pmod p\). Thus \(S_p\equiv B_{p-3}/2\pmod p\). Substitution in (1) proves the main congruence.

**3. Wolstenholme-prime equivalence.** Glaisher's classical congruence reads
\[
 \binom{2p-1}{p-1}\equiv1-\frac{2p^3}{3}B_{p-3}\pmod{p^4}\qquad(p\ge5).
\]
Since \(2\) and \(3\) are units modulo \(p\), its exceptional divisibility condition is equivalent to \(B_{p-3}\equiv0\pmod p\), exactly as in the Franel congruence. If the coefficient is nonzero then \(\nu_p(f_{p^a}-2)=3\); when it vanishes only the lower bound \(\nu_p\ge4\) follows.

**4. Small primes and the primality-test consequence.** For \(p=3\), the sum in (1) is \(1-2^{-3}\equiv2\pmod3\), so \(f_{3^a}-2\equiv54\pmod{81}\) and its valuation is exactly \(3\). For \(p=2\), the sum in (1) consists of the single unit \(1\), giving \(f_{2^a}-2\equiv8\pmod{16}\), again exact valuation \(3\). Finally, when \(n=p^a\) with \(a\ge2\), the condition \(n^3\mid f_n-2\) requires \(\nu_p(f_n-2)\ge3a\ge6\), contradicting the proven valuation \(3\) in all the stated cases.

## Verification
Run `python3 verify.py` with Python 3 and the standard library. It calculates direct exact binomial sums modulo \(p^4\) for prime powers up to index \(1800\), independently constructs Bernoulli numbers using rational arithmetic, checks the exceptional cases \(p=2,3\), verifies the unit-binomial Lucas reduction, and checks the first known Wolstenholme prime \(16843\) using modular sums and products. The recorded replay result was: `VERIFY_OK prime_power_Franel_mod_p4=PASS Bernoulli_reduction=PASS primitive_binomial_units=PASS p2_p3_exact_valuations=PASS Wolstenholme_16843=PASS checks= 581`. The proof, not the numerical range, establishes the assertions for all primes and prime-power exponents.

## Relationship to prior work
Franel numbers and their recurrence are classical. Sun's *Congruences for Franel numbers*, arXiv:1112.1034 (first submitted December 5, 2011; primary classifications 11A07 and 11B65), studies sums and related congruences and gives the standard \(p^3\)-divisibility at prime indices, but the inspected theorem statements and arguments do not state the uniform prime-power \(p^4\)-coefficient above. Meštrović's *Congruences for Wolstenholme primes*, arXiv:1108.4178 (first submitted August 21, 2011), analyzes the classical central-binomial and harmonic formulations and provides the relevant benchmark, but not a Franel prime-power correspondence. The OEIS A000172 comment dated March 22, 2013 proposes the prime-detection congruence; its forward prime implication is classical. Straub, *Multivariate Apéry numbers and supercongruences of rational functions*, arXiv:1401.0854 (first submitted January 5, 2014), proves a **stronger prime-power height-stability congruence** \(f_{p^a}\equiv f_{p^{a-1}}\pmod{p^{3a}}\) for \(p\ge5\), \(a\ge2\), including Franel numbers (Example 3.6). The height-stability portion of the present claim is therefore **covered prior work**, not an independent novelty assertion. What that theorem does not identify is the explicit Bernoulli coefficient at the initial prime index and the equivalence to Wolstenholme primes. The new contribution claimed here is that exact arithmetic identification, with an elementary self-contained derivation across all heights.

## Limitations
The congruence determines only the first possible nonzero \(p\)-adic digit beyond \(p^3\). It does **not** determine the exact valuation for Wolstenholme primes (where it is at least four), and it does not settle the proposed primality characterization for arbitrary composites. The historical literature search was not exhaustive; other earlier or later formulations may exist. No independent audit has been performed, and the finite verification does not certify the infinite argument.

## References
1. Z.-W. Sun, *Congruences for Franel numbers*, arXiv:1112.1034 (initial submission December 5, 2011), https://arxiv.org/pdf/1112.1034.
2. R. Meštrović, *Congruences for Wolstenholme primes*, arXiv:1108.4178 (initial submission August 21, 2011), https://arxiv.org/pdf/1108.4178.
3. OEIS A000172, *The Franel number*, including Gary Detlefs's March 22, 2013 conjecture, https://oeis.org/A000172.
4. A. Straub, *Multivariate Apéry numbers and supercongruences of rational functions*, arXiv:1401.0854, Section 3, Example 3.6, https://arxiv.org/pdf/1401.0854.
5. J. W. L. Glaisher, classical Bernoulli refinement of Wolstenholme's binomial congruence, as recorded in Meštrović's introduction and standard references.
