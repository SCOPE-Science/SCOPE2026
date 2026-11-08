# Exact periods and a prime-denominator transition law for rational floor-polynomial coprimality

## Finding

For a prime \(p\), an integer \(a\geq1\) with \(p\nmid a\), and an integer \(k\geq2\), put
\[
F_{a,p,k}(n)=\mathbf 1_{\gcd(n,\lfloor an^k/p\rfloor)=1}\qquad(n\geq1).
\]
For \(1\leq r<p\), let \(t_r\) be the unique integer in \(\{1,\ldots,p-1\}\) congruent to \(ar^k\pmod p\), and write
\[
Q=\operatorname{rad}\!\left(\operatorname{lcm}(t_1,\ldots,t_{p-1})\right).
\]
Use \(\operatorname{rad}(1)=1\). The following assertions hold simultaneously.

**Exact fundamental period.** The binary sequence \(F_{a,p,k}\) is periodic from its first positive index, and its *least* positive period is
\[
P_{a,p,k}=pQ.
\]

**Exact rational natural density.** For every real \(X\geq1\),
\[
\#\{1\leq n\leq X:F_{a,p,k}(n)=1\}=
\delta_{a,p,k}X+O(P_{a,p,k}),\qquad
\delta_{a,p,k}=\frac1p\sum_{r=1}^{p-1}\frac{\varphi(t_r)}{t_r}.
\]

**Power-residue cosets and averaging.** Write \(g=\gcd(k,p-1)\), and \(H=(\mathbb F_p^\times)^k\). The pair \((P_{a,p,k},\delta_{a,p,k})\) depends only on the coset \(aH\). Consequently, among nonzero coefficient classes modulo \(p\), there are at most \(g\) distinct such pairs, and
\[
\frac1{p-1}\sum_{a=1}^{p-1}\delta_{a,p,k}
=\frac1p\sum_{t=1}^{p-1}\frac{\varphi(t)}t.
\]

**Uniform limit as the denominator prime grows.** For each fixed integer \(k\geq2\), uniformly over primes \(p\geq3\) and integers \(a\) coprime to \(p\),
\[
\delta_{a,p,k}=\zeta(2)^{-1}+O_k\!\left(\frac{(\log p)^2}{\sqrt p}\right).
\]
Thus the rational densities need not equal \(\zeta(2)^{-1}\) at a fixed denominator, but converge to that value uniformly across all rational numerators as the prime denominator increases.

For example, at \(p=5,k=2\), coefficients \(a=1\) and \(a=2\) give densities \(3/5\) and \(7/15\), with least periods \(10\) and \(30\), respectively. At \(p=2\), every odd \(a\) and every \(k\ge2\) give period \(2\) and density \(1/2\).

## Assumptions and scope

All parameters are integers in the ranges just stated; \(n\) ranges over positive integers. The least-period statement is about the full sequence from \(n=1\), not eventual periodicity. The totient convention is \(\varphi(1)=1\), and the lcm over the one-element set for \(p=2\) is \(1\). No irrational coefficient, composite denominator, negative numerator, or non-monomial polynomial is asserted. The implied constant in \(O_k\) may depend on \(k\), but not on \(a\) or \(p\).

## Proof

**1. Integer-part reduction.** For \(n\) divisible by \(p\), since \(k\ge2\) we have \(\lfloor an^k/p\rfloor=an^k/p\), a multiple of \(n\), so \(F_{a,p,k}(n)=0\) (for \(n\ge p\ge2\)). For \(p\nmid n\), write \(r\equiv n\pmod p\) with \(1\le r<p\). Division with remainder gives
\[
p\left\lfloor\frac{an^k}{p}\right\rfloor=an^k-t_r.
\]
As \(p\) is invertible modulo \(n\),
\[
\gcd\!\left(n,\left\lfloor\frac{an^k}{p}\right\rfloor\right)
=\gcd(n,an^k-t_r)=\gcd(n,t_r).
\]
Therefore
\[
F_{a,p,k}(n)=1\iff p\nmid n\ \text{and}\ \gcd(n,t_{n\bmod p})=1.
\tag{1}
\]

**2. A period and the density.** Every prime factor of any \(t_r\) divides \(Q\), and none equals \(p\). Formula (1) depends only on \(n\bmod pQ\); hence \(pQ\) is a period. By the Chinese remainder theorem, in the fiber \(n\equiv r\pmod p\), the proportion avoiding all primes dividing \(t_r\) is exactly \(\varphi(t_r)/t_r\). Summing over fibers proves the density formula. Any periodic zero-one sequence of period \(P\) has summatory error bounded by \(P\).

**3. Minimality of the period.** Let \(T\ge1\) be any period. If \(p\nmid T\), select \(r\equiv-T\pmod p\), \(r\ne0\), and use the Chinese remainder theorem to choose arbitrarily large positive \(n\equiv r\pmod p\) that are coprime to \(t_r\). Then \(F(n)=1\) but \(p\mid(n+T)\) and \(F(n+T)=0\), contradicting periodicity. Thus \(p\mid T\).

Now let \(\ell\mid Q\) be prime. Some \(r\) has \(\ell\mid t_r\). Suppose \(\ell\nmid T\). Choose positive \(n\equiv r\pmod p\) satisfying \(n\equiv0\pmod\ell\) and \(n\not\equiv-T\pmod u\) for every other distinct prime \(u\mid t_r\). CRT applies since these moduli are distinct and coprime to \(p\); for \(u=\ell\), \(n+T\not\equiv0\pmod\ell\) follows from \(\ell\nmid T\). Then \(F(n)=0\), but \(F(n+T)=1\) by (1), again a contradiction. Consequently every \(\ell\mid Q\) divides \(T\), so \(pQ\mid T\). This proves the least positive period is exactly \(pQ\).

**4. Coset invariance and coefficient average.** The map \(r\mapsto r^k\) on \(\mathbb F_p^\times\) has image \(H\) and each fiber has cardinality \(g\). Therefore the multiset of representatives \(t_r\) is determined by the coset \(aH\). Both density and \(Q\) use only this multiset. For every fixed \(r\), as \(a\) runs through \(1,\ldots,p-1\), the representative \(ar^k\bmod p\) runs once through all \(1,\ldots,p-1\). Averaging the density formula over \(a\) yields the asserted mean.

**5. Uniform prime-denominator bound.** Here \(p\ge3\). Set \(w(t)=\varphi(t)/t\). Let \(\mathcal X\) be the group of the \(g\) multiplicative characters modulo \(p\) that are trivial on \(H\). Orthogonality gives, for \(1\le t<p\),
\[
\#\{1\le r<p:ar^k\equiv t\pmod p\}
=\sum_{\chi\in\mathcal X}\chi(t)\overline{\chi(a)}.
\]
Therefore
\[
p\delta_{a,p,k}=\sum_{\chi\in\mathcal X}
\overline{\chi(a)}\sum_{t=1}^{p-1}\chi(t)w(t).
\tag{2}
\]
The principal-character inner sum satisfies
\[
\sum_{t<p}w(t)
=\sum_{d<p}\frac{\mu(d)}d\left\lfloor\frac{p-1}{d}\right\rfloor
=\frac p{\zeta(2)}+O(\log p),
\]
using \(w(t)=\sum_{d\mid t}\mu(d)/d\), absolute convergence of \(\sum\mu(d)/d^2\), and the harmonic sum bound.

For a nonprincipal \(\chi\in\mathcal X\), the same convolution gives
\[
\sum_{t<p}\chi(t)w(t)
=\sum_{d<p}\frac{\mu(d)\chi(d)}d
\sum_{m\le(p-1)/d}\chi(m).
\]
The Pólya–Vinogradov inequality bounds every character partial sum on the right by \(O(\sqrt p\log p)\), uniformly in \(d\). Hence its total is \(O(\sqrt p(\log p)^2)\). In (2) there are at most \(g-1\le k-1\) nonprincipal terms, each with an outer factor of modulus one. Dividing by \(p\) proves the stated \(O_k((\log p)^2/\sqrt p)\) bound and completes the proof.

## Verification

The standalone script `verify.py` uses exact integer arithmetic and rational fractions. It directly checks the floor-based gcd predicate against the residue criterion, the least-period prediction, and the exact rational density for representative small primes and powers. For higher primes it checks the coset and mean identities symbolically over finite fields without iterating enormous periods. Finite computations corroborate but do not establish the infinite theorem or its uniform analytic limit; the arguments in the proof are required.

Run `python3 verify.py` from the same directory as this file. No external Python dependencies are required.

## Relationship to prior work

Jérémy Champagne (2026, arXiv:2607.27533v1) studies gcds involving floors of polynomial powers with **irrational** coefficients, and explicitly poses a higher-degree irrational problem. This theorem studies the complementary rational prime-denominator regime and proves an exact least period together with a quantitative uniform transition to the irrational density. William Banks and Igor Shparlinski (arXiv:2205.00253v1, subsequently Michigan Mathematical Journal 75) obtain asymptotics subject to irrational coefficient/Diophantine hypotheses, not an exact least-period classification for rational monomials. Rational coefficients in the **linear** case go back to Watson (1953), also reflected in Sykora's 2014 rational density tabulations; the present claim assumes \(k\ge2\). The later Aahan Chatterjee preprint (arXiv:2611.04345v1, first posted November 3, 2026) proves the quadratic statement for **irrational** \(\alpha\), not the rational statement here. Classical character estimates underlie the uniform-error step and are not claimed to be new.

## Limitations

The exact-period formula does not extend without new analysis to composite denominators or arbitrary rational polynomial coefficients. The prime-denominator convergence is uniform only when \(k\) is fixed; no claim of a uniform bound for \(k\) growing with \(p\) is made. The error in \(X\) is a fixed-parameter periodic error, not uniform in \(p\) as \(p\to\infty\) jointly with \(X\). The originality assessment is qualified by possible unindexed earlier equivalent results and incomplete access to a 2014 rational-linear reference.

## References

1. J. Champagne, *On the greatest common divisor of n, floor α1 n, ..., floor αk n^k*, first public July 30, 2026, arXiv:2607.27533v1, https://arxiv.org/abs/2607.27533.
2. W. Banks and I. E. Shparlinski, *On the greatest common divisor of integer parts of polynomials*, arXiv:2205.00253v1, https://arxiv.org/abs/2205.00253; Michigan Mathematical Journal 75 (2025), 451–469.
3. G. L. Watson, *On integers n relatively prime to the integer part of αn*, Canadian Journal of Mathematics 5 (1953), 451–455, https://doi.org/10.4153/CJM-1953-050-9.
4. S. Sykora, *On some number densities related to coprimes* (2014), DOI:10.3247/SL5Math14.005; OEIS A250031, https://oeis.org/A250031.
5. A. Chatterjee, *On integers n relatively prime to floor αn²*, first public November 3, 2026, arXiv:2611.04345v1, https://arxiv.org/abs/2611.04345.
6. Classical Pólya–Vinogradov inequality for nonprincipal Dirichlet characters; standard analytic number theory.
