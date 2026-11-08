# Coprimality densities for split integer polynomials and equidistributed integer parts

## Finding

**Theorem (split-polynomial coprimality density).** Fix an integer \(s\ge2\), a nonempty finite set \(H\subset\mathbb Z\) of distinct shifts, and real-valued functions \(f_1,\ldots,f_{s-1}\) on the positive integers. Assume the vector \(\mathbf f=(f_1,\ldots,f_{s-1})\) is *totally homogeneously equidistributed modulo one*: for every positive integer \(D\) and every integer \(0\le u<D\), the sequence \(\mathbf f(Dm+u)/D\) is equidistributed modulo one in the \((s-1)\)-torus. Assume at least one \(f_j\) is a real polynomial having an irrational nonconstant coefficient. Define
\[
P_H(n)=\prod_{h\in H}(n+h),\qquad \rho_H(p)=\#\{-h\pmod p:h\in H\}.
\]
Then the following natural density exists and equals the indicated absolutely convergent, strictly positive product:
\[
\operatorname{dens}\{n\ge1:\gcd(P_H(n),\lfloor f_1(n)\rfloor,\ldots,\lfloor f_{s-1}(n)\rfloor)=1\}
=\prod_{p\ \mathrm{prime}}\left(1-\frac{\rho_H(p)}{p^s}\right).
\]
In particular, for every irrational real \(\alpha\) and every real \(\beta\),
\[
\operatorname{dens}\{n\ge1:\gcd(n(n+1),\lfloor\alpha n+\beta\rfloor)=1\}
=\prod_p(1-2/p^2)\approx0.32263.
\]
No Diophantine-type restriction is imposed on the irrational coefficients.

## Assumptions and scope

The gcd is the nonnegative gcd of the displayed integers (negative or zero floors are allowed). Finitely many \(n\) may make \(P_H(n)=0\) and do not affect density. The equidistribution hypothesis is exactly that used by Holdridge; when each coordinate is a real polynomial, it is equivalent to every nonzero integral linear combination of the coordinates having at least one irrational nonconstant coefficient. The theorem requires at least one coordinate to be a polynomial with an irrational nonconstant coefficient; the remaining coordinates may be nonpolynomial as long as total homogeneous equidistribution holds. \(H\) is fixed, not growing with \(n\).

## Proof

**1. Local probabilities and finite prime truncation.** Fix a finite set of primes \(\mathcal P\) and let \(D=\prod_{p\in\mathcal P}p\). For each integer residue \(0\le u<D\), total homogeneous equidistribution on the progression \(n=Dm+u\) makes the vector of residues \((\lfloor f_1(n)\rfloor,\ldots,\lfloor f_{s-1}(n)\rfloor)\pmod D\) uniformly distributed over \((\mathbb Z/D\mathbb Z)^{s-1}\). Indeed, for an integer \(a\pmod D\), the condition \(\lfloor f_j(n)\rfloor\equiv a\pmod D\) is equivalent to \(\{f_j(n)/D\}\in[a/D,(a+1)/D)\). The boundary has zero limiting mass. Since \(P_H(n)\bmod D\) depends only on \(u\), the joint distribution is uniform on the \(s\)-tuple of the first residue \(u\) and the \(s-1\) floor residues modulo \(D\). By the Chinese remainder theorem, the local event that \(p\) divides all \(s\) integers has probability \(\rho_H(p)/p^s\), independently across primes in \(\mathcal P\). The density excluding all such primes is therefore
\[
\prod_{p\in\mathcal P}(1-\rho_H(p)/p^s).
\]

**2. Eliminate large prime divisors.** Choose one coordinate \(f_j\) that is a polynomial with an irrational nonconstant coefficient, and fix any \(h\in H\). Define \(g_h(m)=f_j(m-h)\). Polynomial translation preserves the property of having an irrational nonconstant coefficient: the highest-degree coefficient that is irrational remains irrational after translation if all higher-degree coefficients are rational (higher-degree contributions to that coefficient are rational). Holdridge's large-prime theorem (Theorem 1.3 of the cited 2026 paper, for degree at least two; the established linear case of Champagne for degree one) therefore gives
\[
\lim_{R\to\infty}\limsup_{N\to\infty}\frac1N\#\{1\le m\le N:\exists p>R,\ p\mid m,\ p\mid\lfloor g_h(m)\rfloor\}=0.
\]
The equality of the two floor values \(\lfloor g_h(n+h)\rfloor=\lfloor f_j(n)\rfloor\) is exact, with no approximation. Translating a fixed interval by \(h\) changes its count by at most \(O_H(1)\); hence the same tail estimate holds for \(n\) with \(p\mid n+h\) and \(p\mid\lfloor f_j(n)\rfloor\). If \(p\mid P_H(n)\), then \(p\mid n+h\) for at least one \(h\in H\). A finite union bound thus shows that the upper density of \(n\) for which a prime larger than \(R\) divides the gcd in the theorem tends to zero as \(R\to\infty\).

**3. Complete the density limit.** The density of the set excluding prime divisors up to \(R\) is the finite product from step 1. The difference between that set and the desired coprime set has upper density tending to zero by step 2. Consequently the natural density exists and equals the infinite product. For every prime, \(1\le\rho_H(p)\le\min\{|H|,p\}\). Since \(s\ge2\), each factor is positive, and \(\sum_p\rho_H(p)p^{-s}\le |H|\sum_p p^{-2}<\infty\), so the product converges to a positive number. In the adjacent case \(H=\{0,1\}\), the residues \(0,-1\) are distinct modulo every prime; hence \(\rho_H(p)=2\). The vector with the single coordinate \(f_1(n)=\alpha n+\beta\) is totally homogeneously equidistributed for irrational \(\alpha\), proving the example.

## Verification

The accompanying `verify.py` uses exact integer square roots to compute \(\lfloor n\sqrt2\rfloor\), checks the adjacent coprimality proportion for increasing finite ranges, calculates the prime-truncated Euler product by an exact sieve of primes and integer root-counting, and independently checks the finite-CRT local count for several shift configurations. These are finite consistency tests, **not** a proof of convergence or of the large-prime tail estimate. The theorem's infinite conclusion uses the cited published large-prime theorem and the preceding reduction, not numerical extrapolation.

## Relationship to prior work

Holdridge, *On the probability that the integer parts of polynomials are coprime* (arXiv:2611.02223v1, first public 2026-11-01), proves density \(1/\zeta(s)\) with the distinguished first coordinate \(n\) and, crucially, a large-prime elimination theorem for \(\gcd(n,\lfloor f(n)\rfloor)\) when \(f\) has an irrational nonconstant coefficient. Its introduction describes rational-coefficient first polynomials as a broader open direction. The case \(H=\{0\}\) here is covered by that paper and is not claimed as new. The present result takes the finitely split, higher-degree *integer-valued first coordinate* \(P_H(n)\), derives its nonuniform local root factors and proves the global density using an exact shift reduction. Champagne's arXiv:2607.27533 gives the linear large-prime case; Banks and Shparlinski's arXiv:2205.00253 concerns gcds with the distinguished coordinate \(n\) under stronger Diophantine hypotheses. No claim is made to originate the necessary published tail theorem or standard CRT equidistribution mechanism.

## Limitations

This does not settle the corresponding question for irreducible integer polynomials or nonsplit factors, because the translation reduction for large primes need not apply. The density is generally not \(1/\zeta(s)\) for \(|H|>1\). A finite truncation is not an error bound at finite \(N\); no effective convergence rate is claimed. Bibliographic priority remains subject to equivalent formulations in literature not indexed by the checked searches; independent review is not performed.

## References

1. Philippa Holdridge, *On the probability that the integer parts of polynomials are coprime*, arXiv:2611.02223v1 (first posted 2026-11-01), https://arxiv.org/html/2611.02223v1. Introduction, Theorems 1.2–1.3, and Section 6.
2. Jérémy Champagne, *On the greatest common divisor of \(n\) and integer parts of polynomial expressions*, arXiv:2607.27533v1 (2026-07-30), https://arxiv.org/abs/2607.27533.
3. William Banks and Igor E. Shparlinski, *On the greatest common divisor of integer parts of polynomials*, arXiv:2205.00253, https://arxiv.org/abs/2205.00253.
4. Carlo Sanna and Márton Szikszai, *A coprimality condition on consecutive values of polynomials*, arXiv:1704.01738, https://arxiv.org/abs/1704.01738 (a different consecutive-polynomial coprimality problem).
