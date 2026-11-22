# Exact ternary denominator and leading-digit law for generalized Jacobsthal reciprocal powers

## Finding
For every integer \(a\ge2\) with \(a\equiv-1\pmod3\), every integer power \(h\ge1\), and every prefix length \(N\ge1\), define
\[
U_n(a)=\frac{a^n-(-1)^n}{a+1}\quad(n\ge0),
\qquad S_{a,h}(N)=\sum_{n=1}^{N}\frac{1}{U_n(a)^h}.
\]
These are positive rational sums: \(U_0(a)=0\), \(U_1(a)=1\), and \(U_{n+2}(a)=(a-1)U_{n+1}(a)+aU_n(a)\). The case \(a=2\) is the standard Jacobsthal sequence.

There are unique integers \(r\ge0\) and \(d\in\{1,2\}\) satisfying \(3^r\le N<3^{r+1}\) and \(d=\lfloor N/3^r\rfloor\). Then
\[
\boxed{\nu_3(S_{a,h}(N))=-hr,\qquad 3^{hr}S_{a,h}(N)\equiv d\pmod3.}
\]
The second congruence is between rationals integral at \(3\). Equivalently, the exact power of \(3\) in the denominator after rational reduction is \(3^{hr}\), and the first nonzero ternary digit of the normalized sum equals the leading ternary digit of \(N\). The denominator exponent jumps by precisely \(h\) when \(N\) crosses a positive power of \(3\).

## Assumptions and scope
Write \(\nu_3(x)\) for the exponent of \(3\) in a nonzero rational number \(x\), and \(\mathbb Z_{(3)}=\{u/v:u,v\in\mathbb Z,\,3\nmid v\}\). Congruence modulo \(3\) applies only to elements of this local ring. The generator \(a\) is a positive integer congruent to \(2\) modulo \(3\), without a primality assumption. The exponent \(h\) is any positive integer. All sums are finite from index \(1\) to \(N\); no limiting operation is used in the theorem.

## Proof
**1. An exact valuation and unit lemma.** For each \(n\ge1\), the integer \(U_n(a)\) has
\[
\boxed{\nu_3(U_n(a))=\nu_3(n),\qquad
\frac{U_n(a)}n\equiv(-1)^{n-1}\pmod3.}
\]
To prove both assertions simultaneously, first suppose \(3\nmid n\). The identity
\[
U_n(a)=\sum_{j=0}^{n-1}a^{n-1-j}(-1)^j
\]
reduces modulo \(3\) to \(n(-1)^{n-1}\), because \(a\equiv-1\pmod3\). This is a unit, and dividing by the unit \(n\) gives the assertion in this case.

For the inductive step \(n=3m\), factor the difference of cubes:
\[
U_{3m}(a)=U_m(a)\bigl(a^{2m}+(-1)^ma^m+1\bigr).
\]
Write \(a^m=(-1)^m(1+3t)\) with \(t\in\mathbb Z\). The parenthesis becomes \(3(1+3t+3t^2)\). Therefore
\[
\nu_3(U_{3m}(a))=\nu_3(U_m(a))+1,
\qquad \frac{U_{3m}(a)}{3m}\equiv\frac{U_m(a)}m\pmod3.
\]
Iteration strips all factors of \(3\) from \(n\); since \((-1)^{3m-1}=(-1)^{m-1}\), it preserves the asserted sign. This proves the lemma for every \(n\). No invocation of a prime-power congruence beyond the displayed exact factorization is needed.

**2. Locate the lowest ternary layers.** Fix \(r\) with \(3^r\le N<3^{r+1}\). Every \(1\le n\le N\) has \(\nu_3(n)\le r\). Exactly \(d\) indices attain equality: \(n=3^r\), and also \(n=2\cdot3^r\) if \(d=2\). By the lemma, the terms of \(S_{a,h}(N)\) have valuations \(-h\nu_3(n)\). Multiplication by \(3^{hr}\) thus makes every summand integral at \(3\), and those with \(\nu_3(n)<r\) vanish modulo \(3\).

For a maximal-depth index \(n=t3^r\), where \(t\in\{1,2\}\), the lemma gives
\[
\frac{U_n(a)}{3^r}\equiv t(-1)^{n-1}\equiv1\pmod3.
\]
The second congruence holds because \(t=1\) gives odd \(n\), while \(t=2\) gives even \(n\) and \(-2\equiv1\pmod3\). Consequently each maximal-depth summand satisfies
\[
\frac{3^{hr}}{U_n(a)^h}\equiv1\pmod3.
\]
Adding these \(d\) surviving contributions yields
\[
3^{hr}S_{a,h}(N)\equiv d\pmod3.
\]
Since \(d\) equals \(1\) or \(2\), it is nonzero modulo \(3\), proving \(\nu_3(S_{a,h}(N))=-hr\) as well.

**3. Denominators and sharp domain boundary.** For a nonzero rational with valuation \(-hr\), its reduced denominator contains exactly \(3^{hr}\). The congruence also describes the first ternary unit. The hypothesis \(a\equiv-1\pmod3\) is substantive: for \(a=4\) and \(N=3\), the sequence begins \(1,3,13\), so \(S_{4,1}(3)=55/39\). This example illustrates that agreement of one reduced denominator with a projected exponent would not establish the full conclusion. Already \(N=2\) gives \(S_{4,1}(2)=4/3\), so the putative normalized leading digit \(2\) is incorrect: \(3S_{4,1}(2)\equiv1\pmod3\). Thus the congruence is not being claimed for all bases.

## Verification
The self-contained Python 3 checker `checker.py` uses independent exact rational addition and direct recurrence generation for the families \(a\in\{2,5,8,11,14\}\), \(1\le h\le7\), \(1\le N\le50\): \(1750\) complete exact-rational cases. A second, modular calculation uses the closed-form sequence rather than the recurrence and checks \(1024\) selected higher-index states through \(N=1500\). It also checks the explicitly computed boundary \(S_{4,1}(3)=55/39\). Invoke `python3 checker.py`, with expected output `VERIFY_OK exact_rational_cases=1750 modular_cases=1024 base_boundary_sum=55/39`. These computations independently corroborate finite instances; the displayed unit-factorization and lowest-layer argument prove the result for all parameters.

## Relationship to prior work
Ahmed Gaber's *On the reciprocal sum of Jacobsthal numbers*, publicly submitted 19 July 2022, studies inverses of **infinite** ordinary and alternating Jacobsthal reciprocal tails (first and second powers). Its introduction explicitly confines the paper to such infinite tails. It does not determine exact reduced denominators or ternary leading units of **finite prefixes** across arbitrary powers and bases. The later published-finding corpus paper *Exact inverse-tail floors for reciprocal squares of Jacobsthal numbers* gives precise real-valued floor and error formulas for the inverse of the infinite square tail. The same object is related, but that real-tail theorem neither states nor logically forces the prefix-denominator result here. General literature on lifting valuations of Lucas sequences supplies part of the context for the unit lemma, whereas the resulting no-cancellation law for the entire finite reciprocal sum is the point of the finding.

## Limitations
The congruence is asserted only at the prime \(3\), for \(a\equiv-1\pmod3\), positive reciprocal power \(h\), and full prefixes starting at \(1\). It does not classify denominators at other primes, shifted sums, or alternating finite sums. The \(3\)-adic valuation of the reduced numerator may be positive when the sum is \(3\)-adically integral, but the normalized claim gives precisely its first nonzero digit after scaling. The overlap review inspects the named literature and indexed records rather than proving universal bibliographic uniqueness; a latent general theorem covering these sums remains a residual novelty risk. Independent scientific validation has not been performed.

## References
- Ahmed Gaber, *On the reciprocal sum of Jacobsthal numbers*, arXiv:2207.12857v1, publicly submitted 19 July 2022, https://arxiv.org/abs/2207.12857 . See introduction, Theorems 2.1–2.2, and Section 3.
- *Exact inverse-tail floors for reciprocal squares of Jacobsthal numbers*, published-finding corpus, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-inverse-tail-floors-for-reciprocal-squares-of-jacobsthal-n--62b53b6d7002 . See RESULT.md for its complete real-tail floor theorem.
