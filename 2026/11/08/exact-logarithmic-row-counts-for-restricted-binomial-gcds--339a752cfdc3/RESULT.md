# Exact logarithmic row counts for restricted binomial gcds

## Finding

For integers \(m\ge2\) and \(q\ge2\), put
\[
G(mq;m)=\gcd\left\{\binom{mq}{mj}:1\le j<q\right\}.
\]
Fix a prime \(p\nmid m\) and write \(h=\operatorname{ord}_m(p)\). For integer \(L\ge0\), let
\[
C_{m,p}(L)=\#\{q\ge2:mq<p^L,\ p\mid G(mq;m)\}.
\]
For all sufficiently large \(L\), \(C_{m,p}(L)\) is an exact rational-coefficient quasipolynomial of degree \(m\), of period dividing \(h\), whose leading coefficient in every residue class is
\[
\boxed{\frac1{m!h^{m-1}}}.
\]

The following formula is exact for **every** \(L\ge0\). Write \(n_r(L)=\#\{0\le i<L:i\equiv r\pmod h\}\), and let \(\mathcal M\) be the finite collection of matrices \(e=(e_{r,d})\), \(0\le r<h\), \(1\le d<p\), of nonnegative integers for which the multiset consisting of \(d e_{r,d}\) copies of \(p^r\bmod m\) is a nonempty minimal zero-sum sequence in \(\mathbb Z/m\mathbb Z\). Let \(E_r=\sum_d e_{r,d}\) and \((n)_k=n(n-1)\cdots(n-k+1)\), with \((n)_0=1\). Then
\[
\boxed{C_{m,p}(L)=\sum_{e\in\mathcal M}\prod_{r=0}^{h-1}
\frac{(n_r(L))_{E_r}}{\prod_{d=1}^{p-1}e_{r,d}!}
-\mathbf1_{\{p^L>m\}}.}
\]
The sum is finite because every admissible profile has \(1\le\sum_{r,d} d e_{r,d}\le m\). For ordinary multiplier cutoffs,
\[
\boxed{\#\{2\le q\le X:p\mid G(mq;m)\}
=\frac{(\log_p X)^m}{m!h^{m-1}}+O_{m,p}((\log X)^{m-1})\quad(X\to\infty).}
\]

At \((m,p)=(5,2)\), \(h=4\), and the eventual polynomial branches at \(L\equiv0\pmod4\) and \(L\equiv2\pmod4\) are respectively
\[
C_{5,2}(L)=\frac{L^5+40L^4+560L^3-640L^2+6144L-30720}{30720},
\]
\[
C_{5,2}(L)=\frac{L^5+40L^4+600L^3-640L^2+12944L-59520}{30720}.
\]
These branches differ, proving that the least eventual quasipolynomial period is **exactly four**.

## Assumptions and scope

Throughout \(m\ge2\) is fixed and \(p\) is prime with \(\gcd(m,p)=1\); \(m\) and \(p\) are fixed before \(L\) or \(X\) tends to infinity. The *digit cutoff* defining \(C_{m,p}(L)\) is \(mq<p^L\). By contrast, the *multiplier cutoff* in the last asymptotic is \(q\le X\). These are different exact finite counts, though they share the same leading logarithmic asymptotic. The event is \(v_p(G(mq;m))\ge1\); no distribution of higher valuations, growing primes, or cases \(p\mid m\) is asserted.

## Proof

**1. Lucas's theorem and minimal zero sums.** Write \(N=mq=\sum_i a_i p^i\) in base \(p\). Form the multiset \(W(N)\) with \(a_i\) copies of \(p^i\bmod m\). Its total sum is zero modulo \(m\). By Lucas's theorem, a coefficient \(\binom Nk\) is nonzero modulo \(p\) precisely when every digit of \(k\) is at most the corresponding digit of \(N\). Hence a proper admissible multiple \(k=mj\), \(0<k<N\), with a nonzero binomial coefficient exists exactly when \(W(N)\) has a nonempty proper zero-sum submultiset. Therefore
\[
p\mid G(N;m)\quad\Longleftrightarrow\quad W(N)
\text{ is a minimal zero-sum sequence in }\mathbb Z/m\mathbb Z.
\]
This translation includes repeated digits and repeated residue weights.

**2. Maximum length and equality case.** A nonempty minimal zero-sum sequence in a cyclic group of order \(m\) has length at most \(m\). For a putative longer sequence, consider the first \(m\) terms: a zero prefix or a repeated partial sum gives a nonempty proper zero-sum subblock. If the length is exactly \(m\), then for every ordering its first \(m\) prefix sums, including the initial zero and excluding the final complete sum, are distinct and exhaust the group. Swapping adjacent terms changes just one such partial sum, which must therefore remain unchanged, so any two adjacent terms coincide. Consequently all \(m\) terms equal an additive generator of \(\mathbb Z/m\mathbb Z\). Conversely, \(m\) copies of any generator form a minimal zero-sum sequence.

**3. Exact profile count.** Because \(p\) is invertible modulo \(m\), the weight \(p^i\) depends only on \(i\pmod h\). A digit \(d\) at a position \(i\equiv r\pmod h\) contributes \(d\) identical weights \(p^r\). For any prescribed minimal-zero-sum profile \(e\), the \(n_r(L)\) possible positions with residue \(r\) can receive the specified nonzero digits in exactly
\[
\frac{(n_r(L))_{E_r}}{\prod_{d=1}^{p-1}e_{r,d}!}
\]
ways, zero if \(E_r>n_r(L)\). Multiplication and summation count precisely positive multiples \(N=mq<p^L\) with the required gcd divisibility. The term \(q=1\) is included whenever \(m<p^L\) and always has minimal-zero-sum digit multiset, since no proper positive subnumber less than \(m\) can be divisible by \(m\). Removing it gives the displayed formula.

**4. Quasipolynomial and leading coefficient.** Every minimal-zero-sum profile uses at most \(m\) tokens and hence at most \(m\) occupied digit positions. Each summand is polynomial of degree at most \(m\) in the counts \(n_r(L)\), and these are affine in \(L\) on each residue class modulo \(h\). Degree \(m\) requires exactly \(m\) occupied positions, all digits equal to one, and, by Step 2, all \(m\) weights equal one generator. This forces all positions into a single class \(r\pmod h\). Such choices contribute
\[
\sum_{r=0}^{h-1}\binom{n_r(L)}m
=\frac{L^m}{m!h^{m-1}}+O_{m,p}(L^{m-1}).
\]
Every other profile uses at most \(m-1\) occupied positions and contributes at most \(O_{m,p}(L^{m-1})\). For large \(L\), the subtraction of \(q=1\) is constant. This proves the stated degree and leading coefficient.

**5. General multiplier cutoffs.** Sandwich \(\#\{2\le q\le X:p\mid G(mq;m)\}\) between the digit-cutoff counts at neighboring powers of \(p\) around \(mX\). Neighboring values differ by \(O_{m,p}((\log X)^{m-1})\) by the proved quasipolynomial, and \(\log_p(mX)=\log_p X+O_m(1)\). The ordinary-cutoff asymptotic follows.

**6. Exact-period example.** At \(m=5,p=2\), the nonempty minimal-zero-sum profiles consist of 14 four-component residue-count vectors, each of total multiplicity at most five. Inserting \(n_r(L)\) into the finite formula produces the two displayed branches. Exact rational evaluations at six consecutive arguments on each residue class determine the degree-five polynomials, and the general degree bound in Step 4 makes the interpolation conclusive for the eventual branches. Since the \(L\equiv0\) and \(L\equiv2\) polynomials differ, period one or two is impossible, whereas period four was proved in Step 4. Hence the least eventual period is four.

## Verification

The package's `verify.py` independently tests Lucas's digit criterion against the minimal-zero-sum criterion, enumerates maximal-length cyclic zero-sum words in small groups, and compares the exact profile formula with direct digit-cutoff row counts. Its finite tests are corroboration rather than an infinite proof. Independent review additionally enumerated all 14 minimal-zero-sum residue profiles for \((m,p)=(5,2)\), checked the digit-cutoff formula directly at \(L=8,12,16,20\), and checked the two degree-five polynomial branches.

**Cutoff clarification.** For the exact *digit cutoff* \(mq<2^L\), the values of \(C_{5,2}(L)\) at \(L=8,12,16,20\) are **15, 65, 191, 453**, respectively. The package's independent sparse-count experiment instead computes the *multiplier cutoff* \(2\le q\le2^L\); at the same four exponents its correctly enumerated counts are **46, 147, 367, 784**. The two finite sequences must not be conflated. Both agree with the asymptotic leading coefficient after the corresponding logarithmic cutoff is correctly interpreted. The original verifier's sparse-count routine used `bound=m*(p**L)` but limited digit positions to `L+2`, omitting valid leading digits whenever `m` requires more base-`p` positions. The corrected `verify.py` enumerates all positions up to that bound. It now gives the correct multiplier-cutoff counts; its exact-profile routine independently gives the correct digit-cutoff counts.

## Relationship to prior work

Fairfax-Ball, *Sharp p-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs* (arXiv:2610.01328, October 1, 2026) determines maximal valuations and least extremal rows, not the general frequency of positive valuations. McTague (arXiv:1510.06696, 2015) gives a rowwise criterion when \(p\equiv1\pmod m\); the \(h=1\) frequency formula follows from it and is not claimed to be new. Fairfax-Ball, *Restricted Binomial GCDs at Primes Congruent to -1* (arXiv:2609.37754, September 29, 2026), gives the complete \(h=2\) valuation criterion; counting those digits may recover this subfamily. Wu (arXiv:2606.20940) treats restricted-gcd formulas under other special hypotheses, notably prime-power restrictions. The contribution surviving those comparisons is the uniform order-\(h\) profile formula and leading constant for unrestricted coprime \((m,p)\), especially orders \(h\ge3\).

## Limitations

The error term is allowed to depend on fixed \((m,p)\). Higher powers \(p^j\) and prime-averaged counts are not addressed. The classification is not a general distribution law over all integers \(m\). The literature comparison establishes best-of-knowledge novelty, not absolute historical priority; an unindexed cyclic-zero-sum enumeration might yield an equivalent formula.

## References

1. John Fairfax-Ball, *Sharp p-adic Extrema and Least Extremal Rows for Restricted Binomial GCDs*, arXiv:2610.01328v1 (2026-10-01), https://arxiv.org/abs/2610.01328.
2. Carl McTague, *On the Greatest Common Divisor of Binomial Coefficients*, arXiv:1510.06696 (2015-10-22), https://arxiv.org/abs/1510.06696.
3. Chai Wah Wu, *Computing the Greatest Common Divisor of Binomial Coefficients*, arXiv:2606.20940 (2026-06-18), https://arxiv.org/abs/2606.20940.
4. John Fairfax-Ball, *Restricted Binomial GCDs at Primes Congruent to -1*, arXiv:2609.37754 (2026-09-29), https://arxiv.org/abs/2609.37754.
5. Édouard Lucas, *Théorie des Fonctions Numériques Simplement Périodiques*, American Journal of Mathematics 1 (1878).
