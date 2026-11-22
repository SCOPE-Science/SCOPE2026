# Exact mixed-composite rational quadratic-floor coprimality densities

## Finding

Let \(a,b\) be coprime positive integers, and suppose \(b\ge6\) has at least two distinct prime factors. Define
\[
F_{a,b}(n)={\bf1}_{\gcd(n,\lfloor an^2/b\rfloor)=1}\qquad(n\ge1).
\]
For each \(1\le r<b\), uniquely write \(ar^2=bc_r+t_r\) with \(0\le t_r<b\). Call a residue \(r\) *admissible* when \(t_r>0\) and \(\gcd(b,r,c_r)=1\), and for admissible \(r\) define
\[
Q_r=\prod_{\substack{\ell\text{ prime},\ \ell\mid t_r\\\ell\nmid b}}\ell,\qquad w_r=\prod_{\substack{\ell\text{ prime},\ \ell\mid t_r\\\ell\nmid b}}\left(1-\frac1\ell\right).
\]
Empty products equal one; for inadmissible residues put \(w_r=0\). Set \(Q=\operatorname{lcm}_{r\text{ admissible}}Q_r\), using \(Q=1\) if the set is empty, and \(P=bQ\).

**Complete periodic-plus-spike classification.** Define the periodic indicator \(H_{a,b}(n)\) by writing \(n=bq+r\), \(0\le r<b\), and setting
\[
H_{a,b}(n)=\begin{cases}
1,&r\text{ admissible and }\gcd(n,Q_r)=1,\\
0,&\text{otherwise}.
\end{cases}
\]
Then \(H_{a,b}\) has period \(P\), and for **every** \(n\ge1\),
\[
\boxed{F_{a,b}(n)=H_{a,b}(n)+{\bf1}_{\{b\text{ a square},\ n=\sqrt b\}}.}
\]
In particular, \(F_{a,b}\) is periodic starting at its first positive index when \(b\) is nonsquare. If \(b\) is square, the smallest index after which it is periodic is exactly \(\sqrt b+1\) (the periodicity may have a smaller period than \(P\)).

**Exact density and effective fixed-parameter count.** The density exists and is the rational number
\[
\boxed{\delta_{a,b}=\lim_{X\to\infty}\frac1X\sum_{1\le n\le X}F_{a,b}(n)
=\frac1b\sum_{r=1}^{b-1}w_r.}
\]
For all real \(X\ge1\), the discrepancy from \(\delta_{a,b}X\) has absolute value at most \(P+1\).

**Quadratic numerator symmetry.** If \(a'\) is another positive integer coprime to \(b\), and \(a'\equiv au^2\pmod b\) for some \(u\) coprime to \(b\), then \(\delta_{a',b}=\delta_{a,b}\). Consequently the density depends only on the square class of the numerator modulo \(b\), and is unchanged by adding a multiple of \(b\) to the numerator.

For instance, at the first mixed-composite denominator \(b=6\), the two unit classes yield \(\delta_{1,6}=1/2\) and \(\delta_{5,6}=23/30\). The square denominator \(b=36\) exhibits the single nonperiodic success \(n=6\) preceding its periodic tail.

## Assumptions and scope

All floor functions are ordinary real floors, all gcds are positive gcds, and prime products are taken over **distinct** primes. The principal statement is restricted to denominators with at least two different prime divisors; its elementary reduction also applies to prime and prime-power denominators, for which related work was already available. \(P\) is an explicit period, **not** asserted to be least. The starting index of eventual periodicity is least when \(b\) is a square. No assertion is made for irrational coefficients or for different polynomial degrees.

## Proof

**1. Exact reduction in a residue class.** For \(n=bq+r\), \(0\le r<b\), elementary division gives
\[
\left\lfloor\frac{an^2}{b}\right\rfloor=aqn+arq+c_r.
\]
Thus \(\gcd(n,\lfloor an^2/b\rfloor)=\gcd(bq+r,arq+c_r)\). Every common prime divisor \(\ell\) must divide
\[
b(arq+c_r)-ar(bq+r)=bc_r-ar^2=-t_r.
\]
If \(r=0\), the floor is divisible by \(n\), and the indicator vanishes because \(b\ge6\). In the remaining argument first suppose \(t_r>0\).

**2. The local obstructions.** For any prime \(\ell\mid b\), if \(\ell\nmid r\) it cannot divide \(n\). If \(\ell\mid r\), then \(\ell\mid n\) for every \(q\), and \(arq+c_r\equiv c_r\pmod\ell\). Consequently the entire residue class is disqualified precisely when \(\gcd(b,r,c_r)>1\). Suppose instead that \(\gcd(b,r,c_r)=1\). Each prime \(\ell\mid t_r\) that does not divide \(b\) creates exactly one forbidden class \(q\equiv-rb^{-1}\pmod\ell\); at that class both arguments are divisible by \(\ell\), and outside it neither is simultaneously divisible. No other primes can divide the gcd. Therefore the indicator in this residue class is exactly \({\bf1}_{\gcd(n,Q_r)=1}\). Its period in \(q\) divides \(Q_r\), and by the Chinese remainder theorem its mean over \(Q_r\) consecutive \(q\)'s is \(\varphi(Q_r)/Q_r=w_r\).

**3. The zero-remainder fiber is an isolated spike.** Assume \(t_r=0\), so \(b\mid ar^2\), whence \(b\mid r^2\) since \(\gcd(a,b)=1\). For every \(n\equiv r\pmod b\), also \(b\mid n^2\). Write \(g=\gcd(n,b)\), \(n=gm\), \(b=gh\), with \(\gcd(m,h)=1\). The divisibility \(b\mid n^2\) forces \(h\mid g\), say \(g=hj\). Consequently \(n=hjm\), \(b=h^2j\), and
\[
\left\lfloor\frac{an^2}{b}\right\rfloor=ajm^2,\qquad
\gcd(hjm,ajm^2)=jm=\frac{n}{h},
\]
using \(\gcd(h,am)=1\). Thus this gcd equals one iff \(n=h=b/g\). Since \(0<r<b\) and \(n\equiv r\pmod b\), this forces \(n=r=h\); then \(g=\gcd(b,r)=r\), so \(b=r^2\). Conversely, if \(b=d^2\), then \(n=d\) satisfies \(\lfloor ad^2/b\rfloor=a\), and \(\gcd(d,a)=1\). Hence there is exactly the asserted extra occurrence and no other zero-remainder occurrence.

**4. Periodicity, counting, and exact onset.** The nonzero fibers in Step 2 depend on \(n\pmod{bQ}\), so \(H_{a,b}\) is \(P\)-periodic from the first index. Each fiber occupies one of the \(b\) residue classes, and the CRT mean is \(w_r\); this proves the density formula. A periodic binary indicator has counting error bounded by the length of one period, and the spike adds at most one. If \(b=d^2\), \(H_{a,b}(d)=0\) but \(F_{a,b}(d)=1\). Suppose an eventual period \(T\) for \(F\) began at or before \(d\). Since \(F=H\) beyond \(d\), \(T\) would be an eventual, hence actual, period of the already-periodic \(H\); then \(F(d+T)=H(d+T)=H(d)=0\), contradicting \(F(d)=1\). The least possible eventual-onset index is therefore \(d+1\).

**5. Square-class symmetry.** It is enough to consider reduced positive residues \(a,a'\) modulo \(b\). Suppose \(a'\equiv au^2\pmod b\) with \(\gcd(u,b)=1\), and match \(r\) with \(r'\equiv u^{-1}r\pmod b\). Then the canonical residues \(t_r\) and \(t'_{r'}\) coincide. To compare the obstruction from primes dividing \(b\), write \(a'=au^2+bm\) and \(r=ur'+bk\). The difference of the corresponding quotients is
\[
c'_{r'}-c_r=mr'^2-2aukr'-abk^2.
\]
For every prime \(\ell\mid b\) and \(\ell\mid r\), one has \(\ell\mid r'\), so the displayed difference is zero modulo \(\ell\). Thus the condition \(\gcd(b,r,c_r)=1\) is carried bijectively to the analogous condition for \(r'\). Since the \(t\)'s match, the permitted prime products and weights also match. Summation proves the asserted density invariance.

## Verification

The standalone script `verify.py`, using Python's standard library and exact rational arithmetic, independently constructs the residue model, compares it with the original gcd-of-floor definition, checks fiber means by direct enumeration, checks periodic shifts, and tests numerator square-class invariance. It runs over all reduced positive numerator classes for denominators up to \(60\), including every mixed-composite denominator in that range, and includes the exceptional square case. Run `python3 verify.py` from the directory containing this file. These finite diagnostics support but do not replace the unrestricted proof.

## Relationship to prior work

Chatterjee's November 3, 2026 quadratic-floor coprimality theorem assumes an irrational coefficient; it does not apply to positive rational \(a/b\). Holdridge's November 1, 2026 theorem also requires irrational-polynomial equidistribution. An existing published published-finding corpus theorem *Exact periods and a prime-denominator transition law for rational floor-polynomial coprimality* covers **prime** denominators, and a separate earlier prime-square-denominator result covers a specific prime-power case; neither statement implies the mixed-composite local obstruction formula. Another published-finding corpus theorem *Numerator-independent gcd histograms for rational floor dilations* treats the **linear** floor, whose numerator symmetry is different. These source comparisons motivate treating mixed-composite denominators as a distinct boundary, rather than relabeling an existing prime-case result. Classical Chinese-remainder arithmetic is used without methodological novelty claims.

## Limitations

The displayed \(P\) may not be the least period of \(H\). The fixed-parameter error is not uniform as \(b\to\infty\), and no prime-denominator convergence rate is asserted. The result does not determine higher joint correlations or classify irrational coefficients. An unindexed equivalent analysis of mixed-composite rational floors remains a residual originality risk; independent mathematical validation has not been performed.

## References

1. A. Chatterjee, *On integers n relatively prime to floor αn²*, arXiv:2611.04345v1, first public November 3, 2026, https://arxiv.org/abs/2611.04345.
2. P. Holdridge, *On the probability that the integer parts of polynomials are coprime*, arXiv:2611.02223v1, first public November 1, 2026, https://arxiv.org/abs/2611.02223.
3. *Exact periods and a prime-denominator transition law for rational floor-polynomial coprimality*, published-finding corpus research record, November 8, 2026, https://github.com/published-finding corpus/2026.
4. *Numerator-independent gcd histograms for rational floor dilations*, published-finding corpus research record, November 8, 2026, https://github.com/published-finding corpus/2026.
