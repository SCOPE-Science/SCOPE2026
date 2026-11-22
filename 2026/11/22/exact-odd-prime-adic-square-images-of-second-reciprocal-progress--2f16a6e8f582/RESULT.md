# Exact odd-prime-adic square images of second reciprocal-progression symmetric sums

## Finding

Let \(p\) be any odd prime, and let \(c,d\) be positive integers with \(p\nmid c\) and \(p\mid d\). For every integer \(n\ge0\), define
\[
E_n(c,d)=\sum_{0\le i<j<n}\frac{1}{(c+di)(c+dj)},\qquad E_0=E_1=0.
\]
There is a uniquely determined \(p\)-adic analytic interpolation \(F_{c,d}:\mathbb Z_p\to\mathbb Z_p\) constructed below, a unique critical point \(\alpha\in\mathbb Z_p\) of this interpolation, and its critical value \(A=F_{c,d}(\alpha)\in\mathbb Z_p^\times\). There is a bijective isometry \(\Psi:\mathbb Z_p\to\mathbb Z_p\) for which
\[
F_{c,d}(x)=A+\frac{\Psi(x)^2}{2c^2}\quad\text{for all }x\in\mathbb Z_p.
\]
Here \(\alpha\equiv 2^{-1}\pmod p\) and \(A\equiv-(8c^2)^{-1}\pmod p\). Consequently the exact closure of the rational sequence in \(\mathbb Z_p\) is
\[
\overline{\{E_n(c,d):n\ge0\}}=A+(2c^2)^{-1}\{z^2:z\in\mathbb Z_p\}.
\]
For every \(k\ge1\), the number of represented residues modulo \(p^k\) is
\[
N_{p,k}=1+\sum_{j=0}^{\lfloor(k-1)/2\rfloor}\frac{p-1}{2}p^{k-2j-1}.
\]
The exact number of input indices \(n\bmod p^k\) representing a target \(y\bmod p^k\) is \(p^{\lfloor k/2\rfloor}\) if \(y\equiv A\pmod{p^k}\); is \(2p^j\) if \(\nu_p(y-A)=2j<k\) and \((y-A)/(p^{2j}(2c^2)^{-1})\) is a square unit modulo \(p\); and is zero otherwise. In the second case the square-unit criterion is independent of the lift of \(y\) and \(A\). The index period modulo \(p^k\) is exactly \(p^k\). Each fiber therefore has natural density equal to its stated count divided by \(p^k\). The value closure has normalized Haar measure
\[
\boxed{\frac{p}{2(p+1)}}.
\]

## Assumptions and scope

All arithmetic congruences of the rational \(E_n\) use inverses of denominators, which are units because \(p\nmid c\) and \(p\mid d\). The theorem applies to every odd prime and every such positive arithmetic progression. The set of square values includes zero. The existence of a global isometry and the full all-depth assertion are proved algebraically and \(p\)-adically; checking finitely many indices alone would not imply them. The critical value \(A\) depends on the progression; it is specified without assuming a closed rational expression.

## Proof

**1. Analytic interpolation and coefficient bound.** Define \(P_0(x)=x\). For every integer \(m\ge1\), the power-sum polynomial has the Stirling expansion
\[
P_m(x)=\sum_{j=0}^{m}\left\{\!\begin{matrix}m\\j\end{matrix}\!\right\}\frac{x(x-1)\cdots(x-j)}{j+1}.
\]
Thus \(P_m(n)=\sum_{i=0}^{n-1}i^m\) for all nonnegative integers \(n\), and every monomial coefficient of \(P_m\) has \(p\)-adic valuation at least \(-\lfloor\log_p(m+1)\rfloor\). (The Stirling numbers and the numerator polynomials have integral coefficients.) For \(s\in\{1,2\}\), define the restricted \(p\)-adic power series
\[
H_s(x)=c^{-s}\sum_{m\ge0}(-1)^m\binom{s+m-1}{m}(d/c)^m P_m(x).
\]
The term with \(m=0\) is \(x/c^s\). Since \(\nu_p(d)\ge1\), the coefficients of each term with \(m\ge1\) have valuation at least \(m-\lfloor\log_p(m+1)\rfloor\), which is at least one for all odd \(p\) and tends to infinity with \(m\). Hence \(H_s\in\mathbb Z_p\langle x\rangle\) and
\[
H_s(x)-x/c^s\in p\mathbb Z_p\langle x\rangle.
\]
For integer \(n\ge0\), the uniformly convergent geometric expansion of \((c+di)^{-s}\) permits interchanging the two sums and proves \(H_s(n)=\sum_{i=0}^{n-1}(c+di)^{-s}\).

**2. The quadratic reduction.** Newton's identity gives
\[
F(x)=\frac{H_1(x)^2-H_2(x)}2
=\frac{x(x-1)}{2c^2}+pR(x),\qquad R\in\mathbb Z_p\langle x\rangle.
\]
It interpolates precisely \(E_n(c,d)\). Differentiation preserves the restricted integral power-series algebra. Since
\[
F'(x)=\frac{x-1/2}{c^2}+pR'(x),\qquad
F''(x)=c^{-2}+pR''(x),
\]
the map \(T(x)=x-c^2F'(x)=1/2-pc^2R'(x)\) is a strict contraction of \(\mathbb Z_p\). The derivative \(R'\) is \(1\)-Lipschitz there. The contraction has exactly one fixed point \(\alpha\), so \(F'(\alpha)=0\), \(\alpha\equiv1/2\pmod p\), and \(B:=F''(\alpha)/2\equiv(2c^2)^{-1}\pmod p\). Also \(A=F(\alpha)\equiv-(8c^2)^{-1}\pmod p\), so \(A\) and \(B\) are units.

**3. Global square normal form.** Translating the restricted power series to \(\alpha\) and using the vanishing linear term gives, for every \(z\in\mathbb Z_p\),
\[
F(\alpha+z)-A=Bz^2(1+pU(z)),\qquad U\in\mathbb Z_p\langle z\rangle.
\]
All coefficients beyond degree two are divisible by \(p\), because the reference polynomial is quadratic. Since \(p\) is odd, both \(1+pU(z)\) and \(2c^2B\in1+p\mathbb Z_p\) have unique square roots congruent to one modulo \(p\). Therefore
\[
\Psi(\alpha+z)=z\sqrt{2c^2B}\sqrt{1+pU(z)}=z+pV(z),\quad V\in\mathbb Z_p\langle z\rangle,
\]
is an isometry: the difference \(V(z)-V(w)\) is divisible by \(z-w\) in \(\mathbb Z_p\). It is also onto, because \(z\mapsto y-pV(z)\) is a strict contraction for each target \(y\in\mathbb Z_p\). Substitution gives the asserted exact normal form on all of \(\mathbb Z_p\), not just in a small neighborhood of the critical point.

**4. Closures, fibers, periods, and measure.** The nonnegative integers are dense in \(\mathbb Z_p\), while \(F\) is continuous. Its sequence-value closure is therefore its full image. The isometry \(\Psi\) induces a permutation of \(\mathbb Z/p^k\mathbb Z\). For an odd prime, a nonzero square with valuation \(2j<k\) has exactly \(2p^j\) square roots modulo \(p^k\); zero has exactly \(p^{\lfloor k/2\rfloor}\). Summing the square-value counts gives \(N_{p,k}\) and the fiber distribution. For any \(t=p^ju\) with \(0\le j<k\), the difference \(\Psi(x+t)-\Psi(x)\) has valuation \(j\). Choosing \(x\) so the sum \(\Psi(x+t)+\Psi(x)\) is a unit (possible because \(p\ge3\)) shows that \(F(x+t)-F(x)\) has valuation \(j\); by density the same witness can be taken at nonnegative integer \(x\). Thus no positive period with valuation below \(k\) exists, whereas \(p^k\) is a period by \(1\)-Lipschitz continuity. Finally, the squares form disjoint valuation shells of measures \((p-1)/(2p^{2j+1})\); their total measure is \(p/(2(p+1))\). Translation and unit scaling preserve Haar measure.

## Verification

The standalone `check_reciprocal_e2.py` needs only Python 3. It computes \(E_n\) modulo prime powers by its exact two-variable recurrence, independently recovers the critical index through finite differences, and compares the *complete* fiber histogram against the translated square histogram. It also checks the predicted counts, critical residue, and minimal periods. Nine independently enumerated parameter/depth instances cover \(2087\) input indices: \((p,c,d,k)=(3,1,3,4),(3,1,3,5),(3,2,6,4),(5,1,5,3),(5,1,5,4),(5,2,10,3),(7,1,7,3),(7,2,14,3),(11,3,11,2)\). This is corroborating finite computation, not proof of the infinite theorem.

## Relationship to prior work

Wang and Hong (first public arXiv version November 6, 2013) study precisely the elementary symmetric functions of the reciprocals in arithmetic progressions and prove nonintegrality, using prime divisors outside the step. The present theorem instead studies the opposite local regime \(p\mid d\), where all denominators are units, and determines an exact global \(p\)-adic value image and all modular fiber counts. Boyd (1994) investigates ordinary harmonic sums and their \(p\)-adic valuations, not this second symmetric function's regular-prime value distribution. Jiang and Hong (2022) treat the arithmetic-progression integrality problem, not an identified complete \(p\)-adic square image; only its abstract was accessible. A nonarchimedean Morse-type normal form is a known general method; the central mathematical calculation here is the uniform restricted-series coefficient estimate for the concrete reciprocal symmetric sums, followed by a *global* isometric coordinate reduction. No claim of inventing \(p\)-adic Morse theory is made.

## Limitations

Only odd primes dividing the progression step are covered. The critical value \(A\) is characterized as the value at the unique \(p\)-adic derivative zero and is computable modulo any fixed power via the convergent series; no simple rational closed form is claimed. The theorem concerns prime-power residue images, not real asymptotic magnitudes or integrality. Historical priority remains uncertain where literature is inaccessible or a general normal-form argument has been previously specialized to the same sequence. This is a self-contained proof and computational corroboration, not independent mathematical validation.

## References

- C. Wang and S. Hong, *The elementary symmetric functions of reciprocals of the elements of arithmetic progressions*, first posted November 6, 2013, https://arxiv.org/abs/1311.1389 . Full HTML text (including theorem, proofs, and appendix) was inspected.
- D. W. Boyd, *A p-adic Study of the Partial Sums of the Harmonic Series*, Experimental Mathematics 3 (1994), 287–302, https://doi.org/10.1080/10586458.1994.10504298 . Relevant accessible HTML transcription was inspected.
- X. Jiang and S. Hong, *A Generalisation of a Theorem of Erdős and Niven*, Bulletin of the Australian Mathematical Society 106 (2022), 215–223, https://doi.org/10.1017/S0004972721001234 . Abstract only; potential overlap risk noted above.
