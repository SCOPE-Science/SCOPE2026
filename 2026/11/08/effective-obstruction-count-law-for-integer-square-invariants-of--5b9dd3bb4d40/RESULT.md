# Effective obstruction-count law for integer-square invariants of reciprocal-sum sequences

## Finding

For an integer \(k\ge1\), a positive integer \(x_0\), and \(n\ge0\), let
\[
x_{n+1}=\frac{k}{x_0+\cdots+x_n},\qquad x_n=\frac{a_n}{b_n},\quad \gcd(a_n,b_n)=1,\quad a_n,b_n>0.
\]
The integer-square question concerns \(J_n=b_n^2-4a_n^2/k\), for all \(n\ge2\) and all integer starts. This paper counts, as the parameter \(k\) varies, its failing prime-local tests.

Define the finite *obstruction set* \(\mathcal B(k)\) by the following exact rules. For an odd prime \(p\), put \(p\in\mathcal B(k)\) if \(v_p(k)=2j\ge2\) and \(-k/p^{2j}\) is a nonzero square modulo \(p\). Put \(2\in\mathcal B(k)\) if \(v_2(k)=2j\ge4\) and \(k/2^{2j}\equiv3\pmod4\). Write \(B(k)=|\mathcal B(k)|\).

The published integer-square criterion [1, Theorem C] identifies \(B(k)=0\) with the property that \(J_n\) is an integer perfect square for **every** integer start and every \(n\ge2\).

**Theorem (exact local distribution and effective convergence).** Let \(K_X\) be uniform on \(\{1,\ldots,\lfloor X\rfloor}\), for \(X\ge1\). Let \(Z_p\) be independent Bernoulli variables with
\[
q_2:=\Pr(Z_2=1)=\frac1{48},\qquad q_p:=\Pr(Z_p=1)=\frac1{2p(p+1)}\quad(p\ge3\text{ prime}),
\]
and set \(B_\infty=\sum_p Z_p\), which is finite almost surely. For all sufficiently large \(X\),
\[
\boxed{d_{\rm TV}\!\left(\mathcal L(B(K_X)),\mathcal L(B_\infty)\right)
\ll \frac{\log\log X}{\log X}.}
\]
The implied constant is absolute. Consequently, for each \(r\in\mathbb Z_{\ge0}\),
\[
\lim_{X\to\infty}\frac1{\lfloor X\rfloor}\#\{1\le k\le\lfloor X\rfloor:B(k)=r\}
=[z^r]\prod_{p}\bigl(1+q_p(z-1)\bigr).
\]
In particular, the exact density of parameters having the universal integer-square property is
\[
\boxed{\delta=\frac{47}{48}\prod_{p\ge3\text{ prime}}\left(1-\frac1{2p(p+1)}\right).}
\]
A product through primes at most \(10^6\) gives \(\delta\approx0.901295\), with absolute truncation error below \(5\cdot10^{-7}\). The full probability law has mean \(\sum_p q_p\) and variance \(\sum_pq_p(1-q_p)\).

## Assumptions and scope

The square criterion in [1] is a published premise; no new proof of that theorem is claimed here. The sampling is uniform among *positive integer parameters* \(k\le X\), not among starts \(x_0\). The defect count is a **number of distinct obstructing primes**, not a number of failing recurrence indices. The total-variation bound concerns the law of this defect count; it is not a convergence bound for the individual rational sequences.

## Proof

**1. Local masses.** For an odd prime \(p\), the event \(v_p(k)=2j\) has \(p\)-adic Haar measure \((p-1)/p^{2j+1}\). Conditional on that event, the unit \(k/p^{2j}\) is uniformly distributed in \(\mathbb F_p^\times\). Exactly half of the nonzero residues make its negative a square. Thus the Haar probability of a local obstruction is
\[
q_p=\frac12\sum_{j\ge1}\frac{p-1}{p^{2j+1}}=\frac1{2p(p+1)}.
\]
For \(p=2\), the condition begins at \(v_2(k)=4\) and only even valuations are allowed; conditional on an exact even valuation, one of the two odd classes modulo \(4\) is obstructing. Therefore
\[
q_2=\sum_{j\ge2}\frac1{2^{2j+2}}=\frac1{48}.
\]
In particular \(\sum_pq_p<\infty\), so the claimed independent sum is almost surely finite and its generating product converges absolutely for every fixed complex \(z\).

**2. Finite congruence approximation.** Fix integers \(Y\ge2\), \(L\ge2\). Define \(B_{Y,L}(k)\) by restricting to obstructing primes \(p\le Y\) whose exact positive even valuation does not exceed \(2L\). The event at an odd prime \(p\) is determined by the residue modulo \(p^{2L+1}\); the event at \(2\) is determined modulo \(2^{2L+2}\). Hence \(B_{Y,L}(k)\) is periodic modulo
\[
M_{Y,L}:=2^{2L+2}\prod_{3\le p\le Y\atop p\text{ prime}}p^{2L+1}.
\]
The Chinese remainder theorem identifies its law for a uniformly random residue modulo \(M_{Y,L}\) with that of a sum of independent finite-level Bernoulli variables, with parameters the appropriate truncated local measures.

**3. Finite-sample error.** If \(K_X\) is uniform on \(\{1,\ldots,\lfloor X\rfloor}\), its reduction modulo \(M_{Y,L}\) is at total-variation distance at most \(M_{Y,L}/\lfloor X\rfloor\) from a uniform residue. On the other hand, if \(B(k)\ne B_{Y,L}(k)\), either a prime \(p>Y\) satisfies \(p^2\mid k\), or some \(p\le Y\) has valuation greater than \(2L\). The union bound gives
\[
\Pr\bigl(B(K_X)\ne B_{Y,L}(K_X)\bigr)
\le\sum_{p>Y}\frac{\lfloor X/p^2\rfloor}{\lfloor X\rfloor}
+\sum_{p\le Y}\frac{\lfloor X/p^{2L+1}\rfloor}{\lfloor X\rfloor}
\ll\frac1Y+2^{-2L}.
\]
The second sum is bounded by the convergent series over *all* integers \(n\ge2\) of \(n^{-(2L+1)}\); the first is dominated by \(\sum_{n>Y}n^{-2}\). These estimates are uniform in \(X\).

**4. Infinite-model error.** Couple the full independent Bernoulli sum \(B_\infty\) to the CRT-truncated sum prime by prime, using the same independent \(p\)-adic random integers. Their probability of disagreement is at most
\[
\sum_{p>Y}q_p+\sum_{p\le Y}\Pr\bigl(v_p(k)>2L\bigr)
\ll\frac1Y+2^{-2L}.
\]
Combining the three couplings yields the uniform estimate
\[
d_{\rm TV}\bigl(\mathcal L(B(K_X)),\mathcal L(B_\infty)\bigr)
\ll \frac{M_{Y,L}}{X}+\frac1Y+2^{-2L}.
\]

**5. Effective parameters.** For sufficiently large \(X\), choose
\[
L=\lceil\log\log X\rceil,\qquad
Y=\left\lfloor\frac{\log X}{100\log\log X}\right\rfloor.
\]
The elementary Chebyshev estimate \(\sum_{p\le Y}\log p\ll Y\) implies
\(\log M_{Y,L}\ll L Y\), and, using any elementary uniform Chebyshev constant, the explicit factor \(100\) ensures \(M_{Y,L}\le X^{1/2}\) for all sufficiently large \(X\). Also \(2^{-2L}\ll1/\log X\) and \(1/Y\ll(\log\log X)/\log X\). Substitution proves the claimed effective total-variation bound.

**6. Density and generating function.** A total-variation bound controls all singleton probabilities uniformly, so each \(r\)-defect density exists and equals the corresponding independent Bernoulli sum probability. For \(r=0\), multiply the non-obstruction factors, using \(1-q_2=47/48\). By the integer-square criterion of [1], this is exactly the desired density of universally square-valued parameters. Standard finite-sum expectation formulas, justified by \(\sum_pq_p<\infty\), give the stated mean and variance. This completes the proof.

## Verification

The standalone file `verify_density.py` checks the odd-prime and dyadic local probabilities with exact rational counts; computes all obstruction multiplicities for \(1\le k\le10^5\); and compares the published criterion to direct divisibility conditions in the second recurrence iterate for \(1\le k\le1000\). It finds exactly \(98\) non-universal parameters among the first \(1000\), agreeing with [1]. It also evaluates the probability generating product to primes at most \(10^6\) and bounds each omitted probability by \(1/[2(10^6+1)]<5\cdot10^{-7}\). The exact finite tests support but do not prove the infinite statements, whose proof is given above.

## Relationship to prior work

[1, Theorem C] supplies the parameterwise necessary-and-sufficient criterion but does not give a parameter-counting distribution, its exact Euler factors, or an effective convergence rate. The Poonen–Stoll local-global geometric sieve, reproduced in [2, Theorem 2.2], supplies **general qualitative independence/density machinery**: when its hypotheses hold, the product-form limiting law follows abstractly. Accordingly this note does **not** claim the Bernoulli principle itself to be new. Its specific contribution is the fully computed distribution for the recurrence's precise local criterion, together with a concrete uniform \(O((\log\log X)/\log X)\) total-variation rate for the entire count law. A previous specialized investigation of [1] counted failing *indices* as the start varies for a fixed square parameter; it neither entails nor is entailed by this parameter distribution.

## Limitations

The proof relies on the published parameterwise integer-square criterion of [1]. It does not establish an optimal total-variation rate or an exact secondary term. The numerical decimal given above is not certified beyond the explicit \(5\cdot10^{-7}\) truncation error. An earlier unindexed specialization of a general effective sieve may imply a comparable rate; an independent historical-priority review remains outstanding. No independent mathematical audit is claimed.

## References

1. Matijasevick, Rodríguez and Salazar, Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields, arXiv:2610.00765v1 (first posted 2026-09-30), especially Theorem C. https://arxiv.org/abs/2610.00765
2. Micheli, Schraven, Tinani and Weger, Geometric sieve over number fields for higher moments, Research in Number Theory 9 (2023), Article 62, DOI 10.1007/s40993-023-00466-6, especially Theorem 2.2. https://doi.org/10.1007/s40993-023-00466-6
