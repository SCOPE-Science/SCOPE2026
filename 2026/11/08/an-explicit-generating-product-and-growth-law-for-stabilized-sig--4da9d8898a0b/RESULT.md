# An explicit generating product and growth law for stabilized signed Fibonacci forcing

## Finding
Let \(F_1=F_2=1\) and \(F_{j+2}=F_{j+1}+F_j\). For an integer \(n\) and \(k\ge1\), let \(B(n;k)\) count the vectors \((\varepsilon_1,\ldots,\varepsilon_k)\in\{-1,0,1\}^k\) for which \(\sum_{j=1}^k\varepsilon_jF_j=n\). For \(k\ge4\), define the signed-representation recurrence's forcing term
\[
f(n;k)=B(n;k)-B(n;k-1)-B(n;k-2)-B(n;k-3).
\]

**Exact coefficient and effective stabilization.** For every \(k\ge5\) and integer \(n\) with \(0<|n|\le F_{k-4}\),
\[
 f(n;k)=[z^{|n|-1}]\prod_{j=1}^{k-3}(1+z^{F_j}+z^{2F_j})
 =[z^{|n|-1}]\prod_{j\ge1}(1+z^{F_j}+z^{2F_j}).
\]
Also \(f(0;k)=0\) for every \(k\ge4\). In particular, the stable function \(f(n)=\lim_{k\to\infty}f(n;k)\) exists and satisfies
\[
 f(0)=0,\qquad
 \sum_{n\ge1}f(n)z^n=z\prod_{j\ge1}(1+z^{F_j}+z^{2F_j}),
 \qquad f(-n)=f(n).
\]
In the product, the two positions with \(F_1=F_2=1\) are **distinct labelled positions**; each digit may be used zero, one, or two times.

**Sharp summatory order of growth.** With \(\varphi=(1+\sqrt5)/2\) and \(\beta=\log 3/\log\varphi\), there exist absolute constants \(0<c<C<\infty\) such that, for all sufficiently large integers \(X\),
\[
 cX^\beta\le\sum_{n=1}^{X}f(n)\le CX^\beta.
\]
Thus the stabilized correction has an exact summatory power exponent, \(\beta\approx2.2830\), though no leading asymptotic constant is claimed.

## Assumptions and scope
All digit vectors are indexed: the two equal Fibonacci weights in positions one and two count as different choices. A vector may have leading zero digits, so \(B(n;k)\) counts all signed strings of exactly \(k\) slots. The forcing term is the same correction in the length recurrence of Anders, Dawsey and Vandehey (2026). Only finite signed strings and formal power-series coefficients are involved; no analytic convergence of the infinite product is needed. The coefficient \([z^m]\) is understood in the ring \(\mathbb Z[[z]]\), in which each coefficient stabilizes because \(F_j\to\infty\).

## Proof
**Step 1: Isolating the only possible high-order patterns.** The published decomposition of signed representations into leading-prefix classes identifies \(f(n;k)\) with the number of strings beginning with one of \((1,0)\), \((1,1)\), \((-1,0)\), \((-1,-1)\), \((1,-1,1)\), and \((-1,1,-1)\). The identity \(\sum_{j=1}^{r}F_j=F_{r+2}-1\) implies that a length-\(k\) string beginning with \((1,1)\) has value at least \(F_{k-1}+1\). A string beginning with \((1,0,0)\), \((1,0,1)\), or \((1,-1,1)\) has value at least \(F_{k-4}+1\). Negating all digits gives the matching negative bounds. These inequalities hold for \(k\ge5\). Consequently, for \(|n|\le F_{k-4}\), every counted string must begin with \((1,0,-1)\) or \((-1,0,1)\). The first type has value at least \(1\), and the second at most \(-1\); hence the first can contribute only when \(n>0\), the second only when \(n<0\), and neither contributes when \(n=0\).

**Step 2: The coefficient identity.** A string starting with \((1,0,-1)\) has the form
\[
 n=F_k-F_{k-2}+\sum_{j=1}^{k-3}\varepsilon_jF_j
   =F_{k-1}+\sum_{j=1}^{k-3}\varepsilon_jF_j.
\]
Using \(\sum_{j=1}^{k-3}F_j=F_{k-1}-1\) and putting \(d_j=1+\varepsilon_j\in\{0,1,2\}\), this is exactly
\[
 n=1+\sum_{j=1}^{k-3}d_jF_j.
\]
This is a bijection: every admissible digit vector determines exactly one signed string with that prefix. Sign reversal handles negative \(n\). If \(0<|n|\le F_{k-4}\), all additional product factors with index \(j\ge k-2\) have weights \(F_j\ge F_{k-2}>|n|-1\). Their nonconstant terms cannot affect the indicated coefficient. This proves the finite and infinite product equalities and the stated effective stabilization threshold.

**Step 3: The summatory exponent.** Write \(P(m)=[z^m]\prod_{j\ge1}(1+z^{F_j}+z^{2F_j})\). For an integer \(X\ge2\),
\[
 T(X)=\sum_{n=1}^{X}f(n)=\sum_{m=0}^{X-1}P(m)
\]
counts all finite digit vectors \((d_j)\in\{0,1,2\}^{(\mathbb N)}\) with \(\sum_jd_jF_j\le X-1\). Choose the largest \(J\) with \(F_J\le X-1\). No digit after position \(J\) can be nonzero, so \(T(X)\le3^J\). For \(J\ge5\), every choice of digits at positions \(1,\ldots,J-4\), with all others zero, is admissible, because
\[
 2\sum_{j=1}^{J-4}F_j=2(F_{J-2}-1)<F_J\le X-1.
\]
Thus \(3^{J-4}\le T(X)\le3^J\). By Binet's formula, \(F_J\asymp\varphi^J\); also \(F_J\le X-1<F_{J+1}\). It follows that \(3^J\asymp X^{\log3/\log\varphi}\), proving the two-sided power law.

## Verification
The accompanying dependency-free script `verify.py` uses exact integer dynamic programming in two distinct ways. One path counts all signed Fibonacci strings and obtains the correction from the four-term difference of \(B(n;k)\). A second path counts explicitly the six forbidden prefixes. Both are compared against a separate bounded-digit coefficient DP over all tested integer arguments. It also checks the published initial values, explicit stabilization bounds, and the summatory inequalities over a finite range. Execute `python3 verify.py`. The code is finite corroboration, not a substitute for the unrestricted proof above.

## Relationship to prior work
Anders, Dawsey and Vandehey, *Non-standard Zeckendorf decompositions; or, Tribonacci within Fibonacci* (arXiv:2604.15446v1, April 16, 2026), establish the modified Tribonacci recurrence, define the correction \(f(n;k)\), and prove eventual stabilization for each fixed integer. Their Section 4 gives the leading-prefix inequalities used in Step 1 but does **not** identify the stable function with the explicit bounded-digit partition product, give a uniform effective stabilization threshold in terms of \(F_{k-4}\), or determine its summatory order.

Chow and Slattery, *On Fibonacci partitions* (arXiv:2009.08222v1), treat the classical distinct-part function in OEIS A000119; that function has **one** type of Fibonacci unit and digits only zero or one. OEIS A007000 counts unbounded multiplicities at every indexed Fibonacci part; OEIS A103577 counts unbounded two-colour Fibonacci partitions. These conventions differ substantially from the finite digit set \(\{0,1,2\}\) at each indexed Fibonacci weight. Anders and collaborators' earlier *Non-standard quaternary representations and the Fibonacci numbers* (arXiv:2505.04589v1) concerns positional powers of fixed integer bases, rather than the present signed Fibonacci correction. None of these inspected statements implies this exact all-integer product and effective bound.

## Limitations
The theorem does not give a pointwise asymptotic for \(f(n)\), an asymptotic constant for \(T(X)\), or a formula for the behavior of \(B(n;k)\) when \(n\) grows comparably with the largest Fibonacci weights. The elementary exponent is a two-sided order estimate, not a limit for \(T(X)/X^\beta\). The comparison with accessible literature cannot exclude unknown or unindexed equivalent formulations.

## References
- K. Anders, M. L. Dawsey and J. Vandehey, *Non-standard Zeckendorf decompositions; or, Tribonacci within Fibonacci*, arXiv:2604.15446v1 (first public version April 16, 2026), Theorem 1.2 and Section 4. https://arxiv.org/pdf/2604.15446
- K. Anders, M. L. Dawsey, R. Gupta, N. Lebowitz-Lockard and J. Vandehey, *Non-standard quaternary representations and the Fibonacci numbers*, arXiv:2505.04589v1 (2025), Sections 1–2. https://arxiv.org/pdf/2505.04589
- S. Chow and T. Slattery, *On Fibonacci partitions*, arXiv:2009.08222v1 (2020), Theorems 1.1–1.3. https://arxiv.org/pdf/2009.08222
- OEIS A000119, A007000 and A103577, sequence definitions and generating functions. https://oeis.org/A000119 ; https://oeis.org/A007000 ; https://oeis.org/A103577
