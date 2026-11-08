# Exact universal congruence modulus for hook-length and core-partition coefficients

## Finding
Let \(E(q)=\prod_{r\ge1}(1-q^r)\), interpreted in \(\mathbb Z[[q]]\). For every integer \(t\ge2\), define integer sequences by
\[
\sum_{n\ge0}a_t(n)q^n=E(q)^{t^2-1},\qquad
\sum_{n\ge0}b_t(n)q^n=\frac{E(q^t)^t}{E(q)}.
\]
The first is the Nekrasov--Okounkov hook-length series at parameter \(t^2\); the second enumerates \(t\)-core partitions. Let \(G(t)\) be the positive gcd of the integers \(a_t(n)-b_t(n)\) as \(n\ge0\) varies. Then
\[
G(t)=\begin{cases}
p^{a+1},&t=p^a\text{ for a prime }p\text{ and }a\ge1,\\
1,&t\text{ has at least two distinct prime factors}.
\end{cases}
\]
The optimality has explicit first witnesses. For \(t=p^a\), put \(k=p^{a-1}\). Then
\[
a_t(n)-b_t(n)\equiv0\pmod{p^{a+2}}\quad(0\le n<k),\qquad
a_t(k)-b_t(k)\equiv-p^{a+1}\pmod{p^{a+2}}.
\]
For non-prime-power \(t\), if \(p^a\) exactly divides \(t\) and \(m=t/p^a>1\), then
\[
a_t(n)-b_t(n)\equiv0\pmod p\quad(0\le n<p^{2a}),\qquad
a_t(p^{2a})-b_t(p^{2a})\equiv-m^2\pmod p.
\]
The second witness is a sharpened explicit form of the composite obstruction in Sharma's motivating paper; the new prime-power optimal modulus and first sharp witness complete the global gcd classification.

## Assumptions and scope
All products are formal power series over the integers, with coefficientwise congruences. No analytic convergence or modular-form assumptions are required. All primes include \(p=2\), and all exponents \(a\ge1\). The gcd is well-defined because the coefficient at degree one of the difference is \(-t^2\), hence some difference is nonzero. The theorem concerns the greatest common divisor across **all** coefficient indices, not the valuation of each individual difference.

## Proof
Set \(D_t(q)=\sum_{n\ge0}(a_t(n)-b_t(n))q^n\). The defining identities give the exact factorization
\[
D_t(q)=E(q)^{-1}\bigl(E(q)^{t^2}-E(q^t)^t\bigr).
\tag{1}
\]
Because \(E(q)\) has constant coefficient one, multiplying or dividing by \(E(q)\) preserves any coefficientwise congruence modulus, and preserves the first nonzero coefficient modulo that modulus.

**A power-lifting lemma.** For every \(H(q)\in1+q\mathbb Z[[q]]\) and prime \(p\), the freshman's-dream congruence gives \(H(q)^p\equiv H(q^p)\pmod p\). Also, if \(U\equiv V\pmod{p^r}\), where \(r\ge1\), then \(U^p\equiv V^p\pmod{p^{r+1}}\): expand \((V+p^rW)^p\), observing that the linear term has factor \(p^{r+1}\) and every higher term has at least that valuation (also for \(p=2\)). Raising the freshman's-dream congruence to \(p^{s-1}\) therefore yields
\[
H(q)^{p^s}\equiv H(q^p)^{p^{s-1}}\pmod{p^s}\qquad(s\ge1).
\tag{2}
\]
Apply (2) successively to \(H(q)=E(q^{p^j})\), for \(j=0,1,\ldots,a-1\), with \(s=2a-j\). The successive moduli are \(p^{2a},p^{2a-1},\ldots,p^{a+1}\), and the resulting telescoping chain proves
\[
E(q)^{p^{2a}}\equiv E(q^{p^a})^{p^a}\pmod{p^{a+1}}.
\tag{3}
\]
Equation (1) proves the divisibility of every difference by \(p^{a+1}\) for \(t=p^a\).

**First sharp coefficient.** Put \(N=p^{2a}\) and \(k=p^{a-1}\). Since \(k<p^a\), the second term of the parentheses in (1) is congruent to one modulo \(q^{k+1}\). For \(1\le j<N\), the exact binomial valuation is
\[
\nu_p\binom Nj=2a-\nu_p(j).
\tag{4}
\]
Indeed, \(\binom Nj=(N/j)\binom{N-1}{j-1}\), while \(\binom{N-1}{j-1}\equiv(-1)^{j-1}\pmod p\), since \(N\) is a power of \(p\). If \(j<k\), equation (4) gives valuation at least \(a+2\) (the range is empty for \(a=1\)). In the product
\[
E(q)^N=\prod_{r\ge1}(1-q^r)^N,
\]
every contribution in a positive degree at most \(k\) uses a choice \(j\le k/r\) from some factor. Except for the single choice \(r=1,j=k\), its coefficient is divisible by \(p^{a+2}\). The exceptional contribution satisfies
\[
(-1)^k\binom Nk\equiv-p^{a+1}\pmod{p^{a+2}},
\]
because \(N/k=p^{a+1}\) and \(\binom{N-1}{k-1}\equiv(-1)^{k-1}\pmod p\). Consequently
\[
E(q)^N-E(q^{p^a})^{p^a}\equiv-p^{a+1}q^k
\pmod{(p^{a+2},q^{k+1})}.
\tag{5}
\]
Dividing by \(E(q)\) in (1) preserves the first nonzero coefficient modulo \(p^{a+2}\), proving the two stated first-witness congruences. Thus \(\nu_p(G(p^a))=a+1\) exactly, and no other prime divides the gcd because its degree-one difference is \(-p^{2a}\).

**Parameters with multiple prime divisors.** Fix \(p^a\parallel t\) and put \(m=t/p^a>1\), with \(p\nmid m\). Frobenius in \(\mathbb F_p[[q]]\) gives
\[
E(q)^{t^2}\equiv E(q^{p^{2a}})^{m^2},\qquad
E(q^t)^t\equiv E(q^{p^{2a}m})^m\pmod p.
\tag{6}
\]
Write \(y=q^{p^{2a}}\). The first power series on the right of (6) has coefficient \(-m^2\) at \(y\), whereas the second has no nonconstant term before \(y^m\). Hence the parenthesized difference in (1) has no coefficient below degree \(p^{2a}\) modulo \(p\), and its coefficient there is \(-m^2\not\equiv0\pmod p\). Division by \(E(q)\) preserves that first coefficient. Thus \(p\nmid G(t)\) for every prime \(p\mid t\). Finally \([q]D_t=-t^2\), so no other prime can divide \(G(t)\). Therefore \(G(t)=1\), completing the proof.

## Verification
The standalone script `verify.py` uses two independently implemented exact-integer coefficient methods: (i) logarithmic-derivative recurrences using divisor sums and (ii) truncated Euler-product multiplication together with the unrestricted partition recurrence. It compares all coefficients through the selected bounds for 21 values of \(t\), including prime powers and parameters with two or more prime factors. The script checks the predicted gcd, the sharp first prime-power witness, and each composite local first failure. Expected successful terminal line:

```text
VERIFY_OK parameter_cases=21 coefficients_cross_checked=1611 exact_integer=yes
```

The exact formal-power-series proof, not the finite tests, establishes the result for all parameters and degrees.

## Relationship to prior work
Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and t-Core Partitions*, arXiv:2610.01422v1 (October 1, 2026), proves the congruence modulo \(t=p^a\), strengthens it to \(p^2\) for \(a=1\), and exhibits an obstruction when \(t\) has multiple prime factors. Its Section 5 explicitly raises the possibility of further lifts in the prime-power case. The present result gives the exact **optimal** modulus \(p^{a+1}\) for every \(a\ge1\), including \(a>1\), and the first coefficient where an additional lift fails; it also packages the composite obstructions as the complete gcd-of-differences invariant. The general power-lifting mechanism is classical, and the composite nondivisibility is substantively already contained in Sharma's argument; neither is claimed as an independent novelty.

Earlier articles by Han (2010) provide the hook-length and core identities, Cotron--Michaelsen--Stamm--Zhu (2019 arXiv version) study lacunarity of eta-quotient coefficients modulo powers of primes, and Du--Liu--Zhao (2018) study congruences for Euler-product coefficients in specific progressions. Their investigated statements do not identify the exact global coefficient-difference content here. This is a best-knowledge priority assessment, not proof that no equivalent older result exists.

## Limitations
No claim is made concerning exact valuations of all individual coefficients beyond the first sharp witness, nor regarding arbitrary generalized hook-length exponents. The answer uses classical formal-series and binomial congruences; an equivalent formulation might exist in the older eta-quotient or Witt-vector literature. The 2010 Han source was assessed from accessible bibliographic material rather than fully inspected, and the two 2017/2018 comparison papers were inspected in their stated introductions, principal results, and relevant sections rather than exhaustively. The mathematical result has not undergone independent review.

## References
- M. Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and t-Core Partitions*, arXiv:2610.01422v1, October 1, 2026. https://arxiv.org/html/2610.01422v1
- G.-N. Han, *The Nekrasov--Okounkov hook length formula: refinement, elementary proof, extension and applications*, Ann. Inst. Fourier 60 (2010), 1--29. https://www.numdam.org/articles/10.5802/aif.2515/
- T. Cotron, A. Michaelsen, E. Stamm, W. Zhu, *Lacunary Eta-quotients Modulo Powers of Primes*, arXiv:1707.04627v2 (2019). https://arxiv.org/pdf/1707.04627
- J. Q. D. Du, E. Y. S. Liu, J. C. D. Zhao, *Congruences for the Coefficients of the Powers of the Euler Product*, arXiv:1802.01374v2 (2018). https://arxiv.org/pdf/1802.01374
