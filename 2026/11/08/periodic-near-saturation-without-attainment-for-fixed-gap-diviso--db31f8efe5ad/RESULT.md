# Periodic near-saturation without attainment for fixed-gap divisor sums

## Finding

Let \(\tau(n)\) denote the number of positive divisors of \(n\). For a fixed positive integer \(h\), call \(A\subset\mathbb N\) \(h\)-separated if distinct elements differ by more than \(h\). Call \(A\) periodic if membership depends only on the residue class modulo some positive integer \(M\). For each periodic \(A\), its divisor-weight coefficient is
\[
\mathcal D(A)=\lim_{X\to\infty}\frac1{X\log X}\sum_{\substack{n\le X\\n\in A}}\tau(n).
\]

**Theorem.** For every fixed \(h\ge1\),
\[
\sup_{\substack{A\text{ periodic}\\A\text{ is }h\text{-separated}}}\mathcal D(A)=1,
\qquad \mathcal D(A)<1\quad\text{for every individual such }A.
\]
More precisely, set \(c=3-2\sqrt2\), let \(Y\ge2\) be large enough that \(M_Y=\prod_{p\le Y}p>2h\), and define for each residue \(a\bmod M_Y\)
\[
W_Y(a)=\prod_{p\le Y}\frac{p-1+p\,\mathbf 1_{p\mid a}}{p^2}.
\]
There is an explicitly constructible \(h\)-separated periodic set \(A_{h,Y}\), with period \(M_Y\), satisfying
\[
1-\mathcal D(A_{h,Y})\le
\sum_{d=1}^{h}\prod_{\substack{p\le Y\\p\nmid d}}
\frac{(p-2)(p-1)+2\sqrt{(2p-1)(p-1)}}{p^2}
\ll_h(\log Y)^{-c}.
\]
In particular, for any prescribed \(\varepsilon>0\) one can choose a fixed period, independent of \(X\), and a single periodic spacing pattern that captures at least \(1-\varepsilon\) of the leading divisor-sum mass.

## Assumptions and scope

All logarithms are natural. The spacing \(h\) is a fixed positive integer; \(Y\to\infty\) only after the limit \(X\to\infty\) for each fixed period. The notation \(\ll_h\) allows a constant depending on \(h\), not on \(Y\). The result does **not** provide uniform estimates if the primorial period is permitted to grow with \(X\), and it does not improve the already established unrestricted asymptotic for \(S(X,h)\).

## Proof

**1. Local divisor-mass coefficients.** For every fixed positive modulus \(M\), and every residue \(a\bmod M\), let
\[
W_M(a)=\frac1{M^2}\sum_{u\bmod M}\gcd(u,M)\,\mathbf1_{\gcd(u,M)\mid a}.
\]
Write \(\tau(n)=\sum_{uv=n}1\). For fixed \(u\) put \(g=\gcd(u,M)\). The congruence \(uv\equiv a\pmod M\) has solutions in \(v\) precisely when \(g\mid a\), and then exactly one class modulo \(M/g\). Thus
\[
\sum_{\substack{n\le X\\n\equiv a\ (\mathrm{mod}\ M)}}\tau(n)
=\frac X M\sum_{u\le X}\frac{\gcd(u,M)}u\mathbf1_{\gcd(u,M)\mid a}+O(X).
\]
Since the integer-valued numerator is periodic modulo \(M\), summation by residue classes gives \(\sum_{u\le X}f(u)/u=(M^{-1}\sum_{u\bmod M}f(u))\log X+O_M(1)\). Therefore
\[
\sum_{\substack{n\le X\\n\equiv a\ (\mathrm{mod}\ M)}}\tau(n)
=W_M(a)X\log X+O_M(X).
\]
Chinese remaindering factors the finite sum for squarefree \(M\). Its prime factor is \((p-1)/p^2\) if \(p\nmid a\), and \((2p-1)/p^2\) if \(p\mid a\), giving the displayed product \(W_Y\). Every \(W_M(a)>0\) for arbitrary \(M\), because the coprime summands contribute at least \(\varphi(M)/M^2\); also \(\sum_{a\bmod M}W_M(a)=1\).

**2. Weighted residue graph and deterministic construction.** On the cycle \(\mathbb Z/M_Y\mathbb Z\), connect \(a\) to \(a+d\) for every \(1\le d\le h\). For every such edge choose an endpoint whose weight \(W_Y\) is no greater than that of the other (break ties arbitrarily). Let \(D\) be the union of all chosen endpoints, and \(B=(\mathbb Z/M_Y\mathbb Z)\setminus D\). Each forbidden edge meets \(D\); hence \(B\) is independent and \(A_{h,Y}=\{n\ge1:n\bmod M_Y\in B\}\) is \(h\)-separated since \(M_Y>2h\). Removing duplicate vertices can only decrease weight, so
\[
1-\mathcal D(A_{h,Y})=\sum_{a\in D}W_Y(a)
\le\sum_{d=1}^{h}\sum_{a\bmod M_Y}\min\{W_Y(a),W_Y(a+d)\}.
\]
Use \(\min(s,t)\le\sqrt{st}\) for nonnegative \(s,t\).

**3. Exact local affinity.** For a prime \(p\mid M_Y\), write \(w_p(0)=(2p-1)/p^2\) and \(w_p(u)=(p-1)/p^2\) otherwise. By the Chinese remainder theorem,
\[
\sum_{a\bmod M_Y}\sqrt{W_Y(a)W_Y(a+d)}
=\prod_{p\le Y}\sum_{u\bmod p}\sqrt{w_p(u)w_p(u+d)}.
\]
If \(p\mid d\), the local sum is \(1\). Otherwise \(u=0\) and \(u=-d\) are two distinct exceptional residues and the remaining \(p-2\) residues are ordinary. Their local sum is
\[
H_p=\frac{(p-2)(p-1)+2\sqrt{(2p-1)(p-1)}}{p^2}.
\]
This proves the displayed finite-product upper bound, with no probabilistic approximation.

**4. Prime-product decay.** As \(p\to\infty\) through primes,
\[
H_p=1-\frac{3-2\sqrt2}{p}+O(p^{-2}),
\qquad \log H_p=-\frac{3-2\sqrt2}{p}+O(p^{-2}).
\]
The convergent sum of reciprocal prime squares and Mertens' prime-reciprocal estimate \(\sum_{p\le Y}p^{-1}=\log\log Y+O(1)\) imply
\[
\prod_{\substack{p\le Y\\p\nmid d}}H_p
\ll_d(\log Y)^{-(3-2\sqrt2)}.
\]
Only finitely many prime factors of each fixed \(d\) are removed. Summing over \(d\le h\) completes the quantitative construction. Finally, any nonempty periodic \(h\)-separated set omits at least one residue class (indeed at least one for any period), and all residue weights are positive; hence \(\mathcal D(A)<1\). The empty set has coefficient zero. This proves strict nonattainment and the supremum statement.

## Verification

The standalone `verify.py` checks the squarefree-modulus finite-sum formula against the local product at every residue of primorial moduli \(6,30,210,2310\). It constructs the vertex covers for multiple small spacings and checks independence and the exact rational weight inequality, using integer arithmetic and `fractions.Fraction`. As an independent finite benchmark, a maximum-weight independent-set dynamic program finds \(927/1225\) for the \(210\)-periodic unit-spacing problem. These finite checks do not prove the infinite prime-product decay; that step is the analytic argument in the proof.

Run `python3 verify.py` with a standard Python installation. The expected final marker is `VERIFY_OK`.

## Relationship to prior work

Aahan Chatterjee, *Divisor Sums with Spacing Constraints* (first public version 2026-10-22, arXiv:2610.31832), proves that the **unrestricted** maximum \(S(X,y)\) is asymptotic to \(X\log X\) for a range of spacings \(y\) growing as a positive power of \(\log X\). In particular, monotonicity already implies \(S(X,h)\sim X\log X\) for fixed \(h\); this is **not claimed as new**. The additional statement proved here is that, for any fixed accuracy, the same leading mass can be captured by one prescribed finite periodic arithmetic pattern, repeated unchanged at every scale, together with an explicit prime-product convergence rate and nonattainment for every single period. The inspected source constructs cutoff-dependent independent sets by sieve and graph methods and does not state this periodic approximation theorem. Classical divisor sums in fixed residue classes provide an ingredient but do not themselves construct separated periodic sets.

## Limitations

The rate \((\log Y)^{-(3-2\sqrt2)}\) is an upper bound on the missing divisor mass, not an asserted optimal exponent. The period \(M_Y\) grows rapidly with \(Y\), so this is an existence-and-structure result rather than a practical uniformly effective construction at moderate cutoffs. The source's more difficult growing-spacing regime is not extended. Historical priority beyond the inspected relevant primary literature and searchable records remains subject to independent review.

## References

1. A. Chatterjee, *Divisor Sums with Spacing Constraints*, arXiv:2610.31832v1 (first posted 2026-10-22), Theorem 1.1 and Section 8. https://arxiv.org/abs/2610.31832 . Lawful full text: https://borowiecki.dev/pdf/2610.31832 .
2. E. Fouvry, H. Iwaniec, N. Katz, *The divisor function over arithmetic progressions*, Acta Arithmetica 61 (1992), 271–287. The argument here needs only the elementary fixed-modulus residue calculation proved above.
3. Classical Mertens prime-reciprocal estimate, used in the proof of the prime-product exponent.
