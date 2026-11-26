# Polynomial multiplicity of prime–Zumkeller representations of odd integers

## Finding

A positive integer is **Zumkeller** if its positive divisors can be split into two sets with equal sum. For a positive integer \(n\), define the ordered additive-representation count
\[
R(n)=\#\{(q,z):q\text{ is prime},\ z\text{ is Zumkeller},\ q+z=n\}.
\]
For every fixed real number \(0<\delta<1/15\),
\[
\boxed{\liminf_{\substack{n\to\infty\\ n\text{ odd}}}
\frac{R(n)\log n}{n^{\delta}}
\ge \frac{1}{\delta\lfloor1/\delta\rfloor}\ge1.}
\]
Consequently \(R(n)\gg_{\delta}n^{\delta}/\log n\) for all sufficiently large odd \(n\). In particular, the exceptional set of odd positive integers that are not a prime plus a Zumkeller number is **finite**. This proves the sufficiently-large-integer portion, but not the exact small-number cutoff, of Somu–Kukla–Tran's Conjecture 4.20.

## Assumptions and scope

The result is unconditional and uses the prime number theorem and an admissible exponent \(L=5\) in Linnik's least-prime-in-a-coprime-residue-class bound. The uniform form is: for every modulus \(m\ge2\) and every residue \(a\) with \(\gcd(a,m)=1\), the least prime \(q\equiv a\pmod m\) obeys \(q\le C m^5\) with an absolute constant \(C\). The established admissibility of exponent \(5\) is recorded in Matomäki–Merikoski–Teräväinen (2024), citing Xylouris. Here \(\log\) means natural logarithm. The range \(0<\delta<1/15\) is open at the upper endpoint; no effective finite cutoff or all-integer representation theorem is asserted.

## Proof

**1. Explicit Zumkeller seeds.** Let \(p\) be an odd prime, and let \(t=t(p)\ge1\) be the least integer with \(2^{t+1}-1>p\). Put \(S=2^{t+1}-1\) and \(K=2^t p\). The divisor sum of \(K\) is \(S(p+1)\). Since \(0\le(S-p)/2<2^t\), its binary expansion gives distinct divisors among \(1,2,\ldots,2^{t-1}\) summing to \((S-p)/2\). Together with the divisor \(2^tp\), their sum is
\[
2^tp+\frac{S-p}{2}=\frac{S(p+1)}{2}.
\]
Hence \(K\) is Zumkeller. Moreover, if \(K\) is Zumkeller and \(\gcd(K,w)=1\), multiplying each of the two equal-sum divisor sets of \(K\) by every divisor of \(w\) constructs an equal-sum partition of the divisors of \(Kw\); this uses the unique product description of divisors under coprimality. Thus \(Kw\) is Zumkeller. Minimality of \(t\) gives \(2^t-1\le p\), so \(K\le p(p+1)\le2p^2\).

**2. A guaranteed representation from each eligible prime parameter.** Let \(n\) be odd and \(p\) an odd prime with \(p\nmid n\). Define \(K\) as above and
\[
M=2pK=2^{t+1}p^2\le4p^3.
\]
Because \(n-K\) is odd and is congruent to nonzero \(n\) modulo \(p\), it is coprime to \(M\). Linnik's theorem supplies a prime \(q\equiv n-K\pmod M\) with
\[
q\le C M^5\le C4^5p^{15}.
\]
Whenever \(n>q+K\), the quotient \(j=(n-q-K)/M\) is a positive integer. Thus
\[
n=q+K(2pj+1).
\]
The factor \(2pj+1\) is odd and coprime to \(p\), hence coprime to \(K=2^tp\), so the second summand is Zumkeller by Step 1.

**3. Uniformly many prime parameters.** Fix \(\delta\) in the stated range and put \(Y=n^\delta\). For every prime \(p\in(Y,2Y]\) not dividing odd \(n\), Step 2 gives \(q\ll Y^{15}=n^{15\delta}=o(n)\) and \(K\ll Y^2=n^{2\delta}=o(n)\), with constants uniform in \(n,p\). Consequently \(n>q+K\) for every such \(p\) when \(n\) is sufficiently large. The prime number theorem gives
\[
P(Y):=\pi(2Y)-\pi(Y)\sim\frac{Y}{\log Y}=\frac{n^\delta}{\delta\log n}.
\]
Let \(B=\lfloor1/\delta\rfloor\). Since each prime in \((Y,2Y]\) is larger than \(n^\delta\), a positive integer smaller than \(n\) has at most \(B\) distinct prime factors from this interval. This applies to \(n\), so at least \(P(Y)-B\) prime parameters are eligible. It also applies to each Zumkeller summand \(z<n\), so a single representation \(n=q+z\) can have arisen from **at most \(B\)** eligible parameters (each such parameter divides \(z\)). Therefore
\[
R(n)\ge\frac{P(Y)-B}{B}
=\left(\frac{1}{\delta B}+o(1)\right)\frac{n^\delta}{\log n}.
\]
Taking the inferior limit over odd \(n\) proves the boxed inequality. Since this bound grows without limit, all sufficiently large odd \(n\) have a representation. \(\square\)

## Verification

The proof's key dependencies have been reconstructed explicitly: the seed's half-divisor-sum subset; the coprime product lemma; the residue-class coprimality modulo \(2^{t+1}p^2\); uniform Linnik and seed-size bounds; and the independent upper bounds on the number of parameter primes dividing either \(n\) or a fixed \(z<n\). The argument applies to infinitely many \(n\); it does not rely on finite searches or numerical certificates. The admissible exponent \(5\) is an established unconditional input, not proved here.

## Relationship to prior work

Somu–Kukla–Tran (2023), Proposition 4.12, handles ten residue classes modulo \(18\) and Conjecture 4.20 predicts that every odd integer above \(8\), except \(21\), is a prime–Zumkeller sum. Their paper does not claim this conjecture is proved. Li (2026), Theorem 1.2, obtains density zero for the overall exceptional set; its Lemma 3.1 supplies one representation for odd \(n\) avoiding an individual odd prime parameter, with uniform threshold \(O(p^{3L})\). That lemma is the motivating starting point and is **not claimed as new**. The present contribution is the dyadic family of \(\asymp n^\delta/\log n\) simultaneous parameter primes, together with the bounded-multiplicity prime-factor argument proving a **pointwise polynomial representation count for every large odd integer**. Neither cited main theorem provides such a count, nor the finiteness of odd exceptions. Related counts of equal-sum divisor partitions of Zumkeller numbers address a different multiplicity.

## Limitations

The result does not determine the exact finite odd exceptional set, an explicit threshold, asymptotic equivalents for \(R(n)\), or an analogous result for even integers; the latter are known to contain infinitely many exceptions. The exponent \(1/15\) is only a strict upper endpoint for the proven family of lower exponents and is not claimed optimal. The proof depends on classical Linnik and prime-number theorems. Exhaustive historical originality is not claimed: an equivalent inference may occur in unindexed additive-number-theory literature.

## References

1. T. H. S. Li, *The Density and Quantitative Upper Bound of Integers Not Expressible as the Sum of a Prime and a Zumkeller Number*, arXiv:2610.19574v1 (first public 14 October 2026), especially Lemma 3.1 and Theorem 1.2. https://arxiv.org/html/2610.19574v1
2. S. T. Somu, A. Kukla, D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v2 (2023), especially Proposition 4.12 and Conjecture 4.20. https://arxiv.org/html/2310.14149v2
3. K. Matomäki, J. Merikoski, J. Teräväinen, *Primes in arithmetic progressions and short intervals without \(L\)-functions*, arXiv:2401.17570 (2024), Introduction, admissible Linnik exponent \(5\). https://arxiv.org/abs/2401.17570
4. T. Xylouris, *On the least prime in an arithmetic progression and estimates for the zeros of Dirichlet \(L\)-functions*, Acta Arithmetica 150 (2011), 65–91, as background for least-prime bounds.
