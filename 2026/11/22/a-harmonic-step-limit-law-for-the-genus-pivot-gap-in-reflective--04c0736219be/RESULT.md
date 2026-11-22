# A harmonic-step limit law for the genus-pivot gap in reflective numerical semigroups

## Finding

Let \(S\) be a reflective numerical semigroup of genus \(g\ge1\): its finite set of positive gaps contains exactly one integer from every residue class modulo \(g\). The integer \(g\) itself is always a gap. Let \(R(S)\) be the length of the **maximal contiguous run of gaps containing \(g\)**. Choose \(S_g\) uniformly among all reflective semigroups of genus \(g\), and put \(X_g=R(S_g)/g\).

The admissible multiplicities are precisely \(2\le a\le g+1\) with \(a\nmid g\), one semigroup for each. There are \(M_g=g+1-\tau(g)\) semigroups, where \(\tau\) counts positive divisors. The genus-pivot run has exact length
\[
R(S(g,a))=g-a\left\lfloor\frac ga\right\rfloor.
\]
For each integer \(1\le t<g\), its **exact fixed-genus frequency** is
\[
\boxed{C_g(t)=\#\{d\mid(g-t):d>t\},}\qquad C_g(g)=1,
\]
and all other frequencies vanish. In particular, the exact mean normalized run length is
\[
\boxed{\mathbb E[X_g]=\frac{g(g+1)-\sum_{n=1}^{g}\sigma(n)}{g(g+1-\tau(g))},}
\]
where \(\sigma(n)\) is the sum of all positive divisors of \(n\).

As \(g\to\infty\), the variables \(X_g\) converge in distribution, with **uniform cumulative-distribution error** \(O(g^{-1/2})\), to a random variable \(X=1-U\lfloor 1/U\rfloor\), where \(U\) is uniform on \((0,1)\). Its continuous law is supported on \([0,1/2]\), with cumulative-distribution function
\[
\boxed{F(x)=\begin{cases}
0,&x\le0,\\
\displaystyle\frac1{K+1}+xH_K,&0<x<\tfrac12,\quad K=\left\lfloor\frac1x-1\right\rfloor,\\
1,&x\ge\tfrac12,
\end{cases}}
\]
where \(H_K=\sum_{j=1}^K1/j\). Its density away from the countable jump boundaries is the harmonic-step function \(f(x)=H_{\lfloor1/x-1\rfloor}\) for \(0<x<1/2\), and zero elsewhere. Its limiting moments are
\[
\boxed{\lim_{g\to\infty}\mathbb E[X_g]=1-\frac{\pi^2}{12},\qquad
\lim_{g\to\infty}\operatorname{Var}(X_g)
=1-\frac{\zeta(2)+\zeta(3)}3-\left(1-\frac{\zeta(2)}2\right)^2.}
\]

## Assumptions and scope

A numerical semigroup is a cofinite additive submonoid of the nonnegative integers, with genus the number of missing nonnegative integers (gaps). A reflective semigroup has a gap set containing one representative of each residue modulo its genus, as classified by Shor. All exact identities hold for each integer genus \(g\ge1\); the limit ranges over all positive genera, with the uniform counting measure on the finite population of reflective semigroups at each genus. The **pivot run** is the maximal interval of gaps **containing the numerical value \(g\)**; it is not asserted to be the longest gap run anywhere in the semigroup. The special ordinary semigroup with multiplicity \(a=g+1\) has \(R=g\) and contributes a vanishing exceptional atom in the limiting distribution. Quantities called densities are with respect to this finite-population sampling, not to all semigroups or to integer indices.

## Proof

**1. Exact pivot-run length.** Shor's classification (arXiv:2207.00051, Proposition 3.4 and its proof) gives the unique reflective semigroup \(S(g,a)\) for each \(a\in\{2,\ldots,g+1\}\) not dividing \(g\). Write \(g=qa+r\), with \(q=\lfloor g/a\rfloor\) and \(1\le r<a\). Its gap set is exactly
\[
\{n:1\le n<g,\ a\nmid n\}\ \cup\ \{g+ja:0\le j\le q\}.
\]
The multiples \(qa\) and all positive members of \([g+1,g+a-1]\) are nongaps, so the maximal contiguous run containing the gap \(g\) is \([qa+1,g]\). Its length is \(g-qa=r\). This also covers \(a=g+1\), when \(q=0\) and the pivot run is \([1,g]\).

**2. Exact histogram and mean.** For \(1\le t<g\), an admissible \(a\) produces \(r=t\) precisely when \(g=qa+t\) with \(q\ge1\), \(a>t\); equivalently \(a\mid(g-t)\) and \(a>t\). These conditions imply \(a\ge2\) and \(a\nmid g\). The only \(q=0\) case has \(a=g+1\) and \(t=g\), proving the histogram.

To sum the remainders, include all \(a=1,\ldots,g+1\), noting that terms with \(a\mid g\) vanish and \(a=1\) vanishes. Then
\[
\sum_{S}R(S)=\sum_{a=1}^{g+1}\left(g-a\left\lfloor\frac ga\right\rfloor\right)
=g(g+1)-\sum_{a=1}^{g}a\left\lfloor\frac ga\right\rfloor
=g(g+1)-\sum_{n=1}^g\sigma(n).
\]
The last equality counts a divisor \(a\) once for each of its multiples at most \(g\). Dividing by \(gM_g\) gives the mean identity. The classical elementary estimate \(\sum_{n\le g}\sigma(n)=\tfrac12\zeta(2)g^2+O(g\log g)\) and \(\tau(g)=O(\sqrt g)\) yield \(\mathbb E[X_g]=1-\zeta(2)/2+O(g^{-1/2}+\log(g+1)/g)\).

**3. Uniform limit with rate.** For \(a\le g\), put \(u=a/g\). Outside the divisor-excluded indices, \(X_g=1-u\lfloor1/u\rfloor\). Consider the function \(T(u)=1-u\lfloor1/u\rfloor\) for \(0<u\le1\). On each interval \((1/(k+1),1/k]\), it is affine with slope \(-k\) and ranges from \(0\) to \(1/(k+1)\) (endpoint conventions are immaterial to integrals). For fixed \(x\), the set \(\{u:T(u)\le x\}\), restricted to \(u\ge g^{-1/2}\), is a union of at most \(\lfloor\sqrt g\rfloor+1\) intervals. Each interval's fraction of grid points \(a/g\) differs from its Lebesgue measure by at most \(2/g\). The deleted region \(0<u<g^{-1/2}\) has measure and grid proportion \(O(g^{-1/2})\). Removing the \(\tau(g)\) divisor indices, adding \(a=g+1\), and renormalizing by \(M_g=g+1-\tau(g)\) change the cumulative distribution by \(O(\tau(g)/g+1/g)=O(g^{-1/2})\). These bounds are uniform in \(x\). Thus \(\sup_x|\Pr(X_g\le x)-\Pr(T(U)\le x)|=O(g^{-1/2})\).

**4. The continuous law and moments.** On the \(k\)-th interval, the inverse change of variable \(x=1-ku\) has Jacobian \(1/k\), and its image is \((0,1/(k+1))\). Consequently the density is
\[
f(x)=\sum_{k\ge1}\frac1k\,\mathbf1_{\{0<x<1/(k+1)\}}.
\]
For \(0<x<1/2\), the summation indices are precisely \(1\le k\le\lfloor1/x-1\rfloor\), except at boundary points where the value of a density can be assigned arbitrarily. Integrating gives \(F(x)=1/(K+1)+xH_K\). Direct integral calculations give
\[
\mathbb E[X]=\sum_{k\ge1}\int_{1/(k+1)}^{1/k}(1-ku)\,du
=\sum_{k\ge1}\frac1{2k(k+1)^2}=1-\frac{\zeta(2)}2,
\]
\[
\mathbb E[X^2]=\sum_{k\ge1}\frac1{3k(k+1)^3}=1-\frac{\zeta(2)+\zeta(3)}3.
\]
The partial fractions follow by \(1/[k(k+1)^j]\) decomposition for \(j=2,3\). Since \(0\le X_g\le1\), weak convergence also implies convergence of the first two moments. Subtracting the squared mean proves the displayed variance.

## Verification

The included standard-library script `CHECK.py` constructs reflective semigroups independently from the generating set \(\{a,2g+a-r\}\cup[g+1,g+a-1]\). For every \(1\le g\le90\) and every admissible \(a\), it compares the actual gap set from additive reachability with Shor's classification and checks the maximal run containing \(g\). It also compares all histogram cells with the divisor formula and checks the total semigroup count and exact mean numerator. All assertions pass. The finite tests do not replace the infinite argument. For reference, the predicted asymptotic mean is approximately \(0.1775329666\), and the limiting variance is approximately \(0.0194850558\).

## Relationship to prior work

Shor's 2022 preprint gives the complete genus/multiplicity parametrization and gap decomposition, which directly implies the individual semigroup's pivot-run length \(g\bmod a\); this elementary reduction is **not separately claimed as novel**. Published work on reflective semigroups also gives a different fixed-genus **isolated-gap count** whose distribution has the discrete heavy tail \(1/[k(k+1)]\); the present statistic is a *single contiguous run crossing the genus pivot*, rather than the number of isolated gaps. In particular, its limiting law is continuous on \([0,1/2]\) with a harmonic-step density, not a discrete heavy-tail law. The assessed additional result is the exact divisor histogram for pivot-run lengths together with the continuous limiting distribution, a uniform convergence rate, and explicit zeta-valued moments. It remains possible that these are implicit or recorded in an unindexed source; priority is not independently certified.

## Limitations

The theorem concerns only reflective numerical semigroups, not all semigroups of fixed genus. It counts the gap run containing the genus pivot, not the maximum of all run lengths. The exact arithmetic formula is an extension of Shor's established parametrization and therefore depends on it. The asymptotic theorem does not imply pointwise convergence of individual integer-valued histograms. Computational verification is finite; all-limit claims follow from the proof. Independent mathematical audit has not been performed, and bibliographic incompleteness remains a risk.

## References

1. C. M. Shor, *Reflective Numerical Semigroups*, arXiv:2207.00051v1, first publicly posted 30 June 2022, Proposition 3.4 and proof, Proposition 5.2; *Albanian Journal of Mathematics* 17 (2023), 41–68. https://arxiv.org/abs/2207.00051
2. *An exact isolated-gap distribution and harmonic tail law for reflective numerical semigroups*, public mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-exact-isolated-gap-distribution-and-harmonic-tail-law-for-ref--c016095bed6e .
3. T. M. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976; standard divisor-summatory estimates (used only for the effective mean asymptotic).
