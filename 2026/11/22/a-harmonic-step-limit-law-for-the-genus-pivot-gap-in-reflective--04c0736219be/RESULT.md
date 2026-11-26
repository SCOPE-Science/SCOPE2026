# A harmonic-step limit law for the genus-pivot gap in reflective numerical semigroups

## Finding

A reflective numerical semigroup of genus \(g\ge1\) is a cofinite additive submonoid of the nonnegative integers whose \(g\) gaps contain one representative of each residue class modulo \(g\). Choose \(S_g\) uniformly among the reflective numerical semigroups of genus \(g\). Let \(R(S_g)\) be the length of the maximal contiguous gap run containing the integer \(g\), and put \(X_g=R(S_g)/g\).

Then \(X_g\) converges in distribution to \(X=1-U\lfloor1/U\rfloor\), where \(U\) is uniform on \((0,1)\), with
\[
\sup_x\left|\Pr(X_g\le x)-\Pr(X\le x)\right|=O(g^{-1/2}).
\]
The limiting CDF is zero on \(({-\infty},0]\), one on \([1/2,\infty)\), and
\[
\Pr(X\le x)=\frac{1}{K+1}+xH_K,\qquad K=\left\lfloor\frac1x-1\right\rfloor,\quad 0<x<1/2,
\]
where \(H_K=\sum_{j=1}^K1/j\). The density on \((0,1/2)\) is \(H_K\) away from its jump points. The limiting second moment is \(1-(\zeta(2)+\zeta(3))/3\). The limiting mean is the classical remainder-sum constant \(1-\zeta(2)/2\), so the limiting variance is
\[
1-\frac{\zeta(2)+\zeta(3)}{3}-\left(1-\frac{\zeta(2)}2\right)^2.
\]
The contribution is the explicit continuous law and uniform finite-genus error for this sampling scheme, with its second moment and variance. The finite remainder table, its translation from the genus/Frobenius classification, and its first-moment numerator are prior inputs or immediate consequences, not novelty claims.

## Proof

**Reduction to the classical remainder array.** Shor's Proposition 3.4 and Corollary 5.1 give exactly one semigroup per multiplicity \(2\le a\le g+1\) with \(a\nmid g\). Write \(g=qa+r\), with \(1\le r<a\). Shor's gap decomposition is the union of the nonmultiples of \(a\) in \([1,g-1]\) and the progression \(g,g+a,\ldots,g+qa\). The gap run at \(g\) is therefore \([qa+1,g]\), since both \(qa\) (including 0 if \(q=0\)) and \(g+1\) are nongaps. Its length is \(r\), and Shor's Corollary 3.6 gives \(r=2g-F(S_g)\), with \(F\) the Frobenius number. Thus at fixed genus the pivot-run law is the Frobenius law in an affine coordinate.

There are \(M_g=g+1-\tau(g)\) admissible multiplicities. For \(1\le t<g\), the condition \(r=t\) is exactly \(a\mid(g-t)\) and \(a>t\); the only case \(t=g\) is \(a=g+1\), the ordinary semigroup. In particular, the multiset is the nonzero portion of row \(g\) of OEIS A372727: its entry at modulus 0 stands for the remainder \(g\) at \(a=g+1\). These finite identities are included for normalization and replay, not claimed as new.

The sum of all entries is A111490 at \(g\), namely \(g+\mathrm{A004125}(g)\). Counting divisors by multiples writes it as \(g(g+1)-\sum_{n=1}^g\sigma(n)\), with \(\sigma(n)\) the sum of the divisors of \(n\). Division by \(g M_g\) gives \(\mathbb E[X_g]\). The classical remainder-sum asymptotic gives the limiting mean \(1-\pi^2/12\).

**Uniform error.** For the grid \(u=a/g\), \(1\le a\le g\), put \(T(u)=1-u\lfloor1/u\rfloor\). Removing the \(\tau(g)\) divisor indices and adding the single observation 1 reproduces the finite law of \(X_g\). This changes any cumulative probability by \(O((1+\tau(g))/g)=O(g^{-1/2})\), by counting divisor pairs. To compare the unconditioned grid with uniform \(U\), first discard the region \(0<u<g^{-1/2}\), whose grid proportion and Lebesgue measure are \(O(g^{-1/2})\). On the rest, the level set \(\{T(u)\le x\}\) is a union of at most \(\lfloor\sqrt g\rfloor+1\) intervals, since on \((1/(k+1),1/k]\) the map is \(1-ku\). For each interval the normalized grid count differs from its length by at most \(2/g\), including endpoint conventions. The total error is uniform in \(x\).

**Law and moments.** On the \(k\)-th branch, the range is \([0,1/(k+1))\) and the inverse Jacobian is \(1/k\). The branch contributes \(\min(x,1/(k+1))/k\) to \(\Pr(T(U)\le x)\) for \(x>0\); it contributes the density \(1/k\) for \(0<x<1/(k+1)\). For \(0<x<1/2\) the CDF sum splits into \(xH_K\) and the telescoping tail \(\sum_{k>K}1/[k(k+1)]=1/(K+1)\). The CDF is continuous; endpoint choices inside the density do not affect it. Integrating each branch to compute the first and second moments gives, respectively,
\[
\sum_{k\ge1}\frac{1}{2k(k+1)^2}=1-\frac{\zeta(2)}2,\qquad
\sum_{k\ge1}\frac{1}{3k(k+1)^3}=1-\frac{\zeta(2)+\zeta(3)}3.
\]
For partial fractions, use \(1/[k(k+1)^j]=1/[k(k+1)]+\sum_{\ell=2}^j(-1)/(k+1)^\ell\). The second moment and variance of \(X_g\) tend to those of \(X\), since all these laws are supported on \([0,1]\).

## Comparison and limits

Shor's fixed-Frobenius enumeration uses a different conditioning; the exact genus/multiplicity data and the Frobenius identity already determine the joint law. OEIS A372727 tabulates the underlying remainder data and A111490 gives the first-moment numerator, including the leading constant. None of those inspected sources states the explicit harmonic-step CDF with uniform discrepancy and second moment for this law. A fixed-genus isolated-gap count has a discrete law and a divergent limiting mean, unlike this statistic. A fixed-genus Wilf-surplus limit uses a different transform of the multiplicity; a marginal law for that transform does not yield the remainder law. The limit here is not a statement about all numerical semigroups or their longest gap run. The uniform upper bound on the CDF error is not asserted to be optimal. Bibliographic comparisons are limited to the sources inspected.

## References

- C. M. Shor, *Reflective Numerical Semigroups*, Albanian Journal of Mathematics **17** (2023), 41–68; [arXiv:2207.00051v1](https://arxiv.org/html/2207.00051v1), Proposition 3.4, Corollaries 3.6 and 5.1, and §5.
- OEIS [A372727](https://oeis.org/A372727), [A111490](https://oeis.org/A111490), and [A004125](https://oeis.org/A004125).
- *An exact isolated-gap distribution and harmonic tail law for reflective numerical semigroups* and *A zeta-moment limit law for Wilf surplus in reflective numerical semigroups* (indexed mathematical statements).
