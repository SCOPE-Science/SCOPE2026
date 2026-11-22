# An exact all-shift correlation law and prime-lag sign reversal for signed two-block odd partitions

## Finding
For the signed two-block odd partition function \(a(n)\) of Merca, set \(G(n)=a(n)/n\). The full fixed-shift pair correlation has an explicit arithmetic kernel. Given \(h\ge1\), put \(t=\nu_2(h)\) and
\[
R(h)=\prod_{\substack{p^v\parallel h\\p\text{ odd}}}\left(1+p^{-3}+\cdots+p^{-3v}\right),\quad
D(t)=\begin{cases}1,&t=0,\\\frac87-\frac{15}{7\cdot8^t},&t\ge1.\end{cases}
\]
The empty product is one. For each fixed \(h\ge1\) and every \(\varepsilon>0\), as \(X\to\infty\),
\[
\frac1X\sum_{1\le n\le X}G(n)=\frac{\pi^2}{32}+O_\varepsilon(X^{-1+\varepsilon}),\qquad
\frac1X\sum_{1\le n\le X}G(n)G(n+h)=\frac3{32}D(t)R(h)+O_{h,\varepsilon}(X^{-1+\varepsilon}).
\]
Thus the limiting centered covariance at lag \(h\) is
\[K(h)=\frac3{32}D(\nu_2(h))R(h)-\frac{\pi^4}{1024}.\]
Among prime shifts, the covariance is strictly positive exactly at \(h=3\) and strictly negative at every other prime. The unnormalized nearest-neighbor correlation obeys
\[\sum_{1\le n\le X}a(n)a(n+1)=\frac{X^3}{32}+O_\varepsilon(X^{2+\varepsilon}).\]

## Assumptions and scope
For \(n\ge1\), \(a(n)\) is the coefficient of \(q^n\) in
\[\sum_{1\le x<y}\frac{q^x}{1+q^{2x}}\frac{q^y}{1+q^{2y}},\]
so the coefficient for the representation \(n=(2r+1)x+(2s+1)y\), \(1\le x<y\), \(r,s\ge0\), carries the sign \((-1)^{r+s}\). The symbols \(\sigma(n)\) and \(\tau(n)\) are the ordinary divisor-sum and divisor-count functions, respectively; \(\sigma(z)=0\) when \(z\) is not a positive integer. The symbol \(\lambda(n)=\sum_{d\mid n}\chi_4(d)\) uses the nonprincipal character modulo four. The shift \(h\) is fixed while \(X\) grows; the error constant is not claimed uniform for growing shifts. Summation endpoints mean positive integers at most the real cutoff \(X\).

## Proof
Merca's coefficient identity is
\[4a(n)=\sigma(n)-\lambda(n)-2\sigma(n/2)+4\sigma(n/4).\]
Write \(b(n)=\sigma(n)-2\sigma(n/2)+4\sigma(n/4)\), and define the multiplicative weight
\[u(d)=1-2\mathbf1_{2\mid d}+4\mathbf1_{4\mid d}=\begin{cases}1,&d\text{ odd},\\-1,&\nu_2(d)=1,\\3,&\nu_2(d)\ge2.\end{cases}\]
Divisor rearrangement gives \(b(n)/n=\sum_{d\mid n}u(d)/d\). Because \(\lambda(n)=O(\tau(n))\), the divisor bound \(\tau(n)=O_\varepsilon(n^\varepsilon)\) implies that replacing \(G(n)\) by \(b(n)/(4n)\) in either of the displayed averages costs \(O_{h,\varepsilon}(X^{-1+\varepsilon})\). Specifically, \(|b(n)|/n\le3\sum_{d\mid n}1/d\le3\tau(n)\), so the pairwise replacement error is bounded by a constant times \(X^{-1}\sum_{n\le X+h}n^{-1+2\delta}\), with \(\delta>0\) arbitrarily small.

For the mean, divisor rearrangement and the elementary progression count show
\[\frac1X\sum_{n\le X}\frac{b(n)}n=\sum_{d\ge1}\frac{u(d)}{d^2}+O\!\left(\frac{\log X}{X}\right).\]
The Euler product's factor at two is \(1-1/4+3\sum_{j\ge2}4^{-j}=1\), while the odd-prime product is \((1-2^{-2})\zeta(2)=\pi^2/8\). Division by four proves the first formula.

For the pair mean, expand the two divisor sums. The congruences \(d\mid n\), \(e\mid n+h\) have a solution precisely if \(\gcd(d,e)\mid h\), with one residue class modulo \(\operatorname{lcm}(d,e)\). Hence
\[\frac1X\sum_{n\le X}\frac{b(n)}n\frac{b(n+h)}{n+h}
=\sum_{\gcd(d,e)\mid h}\frac{u(d)u(e)}{de\,\operatorname{lcm}(d,e)}
+O_{h,\varepsilon}(X^{-1+\varepsilon}).\]
The double series converges absolutely, since \(|u|\le3\) and
\[\sum_{d,e\ge1}\frac1{de\operatorname{lcm}(d,e)}<\infty.\]
Indeed, for the truncated sums \(d\le X\), \(e\le X+h\), the progression-count error is \(O(\log^2(X+h)/X)\). The omitted infinite tails satisfy \(O_h(\log(X+h)/X)\), by separating \(e\le d\) and \(e>d\), and bounding the denominator using \(\operatorname{lcm}(d,e)\ge\max(d,e)\). These estimates prove the stated power-saving error without asserting any stronger uniformity in \(h\).

The absolutely convergent double sum factors into prime-power local factors. For an odd prime \(p\), writing \(v=\nu_p(h)\), the local terms with \(\min(i,j)=0\) contribute \(L_p(0)=1+2\sum_{k\ge1}p^{-2k}=(p^2+1)/(p^2-1)\). Each new permitted minimum \(m\ge1\) contributes precisely \(p^{-3m}L_p(0)\). Consequently
\[L_p(v)=\frac{p^2+1}{p^2-1}\sum_{m=0}^vp^{-3m}.\]
For \(p=2\), the minimum-zero local terms sum to \(L_2(0)=1+2\sum_{j\ge1}u(2^j)4^{-j}=1\). The minimum-one increment equals \(-1/8\); for every minimum \(m\ge2\), the increment equals \(15\cdot8^{-m}\). Summing the finite geometric series gives exactly \(L_2(t)=D(t)\).

Finally,
\[\prod_{p\text{ odd}}\frac{p^2+1}{p^2-1}=\frac{\zeta(2)^2/\zeta(4)}{5/3}=\frac32.\]
Dividing the total product by sixteen proves the pair-correlation formula. The mean-square centering produces \(K(h)\). For primes \(p\ge3\), \(D(0)=1\) and \(R(p)=1+p^{-3}\); at two, \(D(1)=7/8\). As \(\pi^4/1024\) lies strictly between \((3/32)(1+5^{-3})\) and \((3/32)(1+3^{-3})\), and exceeds \((3/32)(7/8)\), the only positive prime-lag covariance is the lag three. These inequalities follow, for instance, from the elementary bounds \(3.14<\pi<22/7\). Partial summation applied to the lag-one mean, using \(n(n+1)G(n)G(n+1)=a(n)a(n+1)\), yields the cubic unnormalized asymptotic.

## Verification
The accompanying standalone Python checker constructs the coefficients from the exact divisor identity, independently enumerates the signed two-part-size definition through degree \(120\), and checks limiting pair constants for thirteen shifts with a cutoff of \(120000\). It also checks the strict prime-lag signs. The checker is finite evidence only; the infinite statements follow from the divisor-series argument above. To run: `python3 verify.py` (Python standard library only).

## Relationship to prior work
Merca's September 2026 preprint establishes the defining signed partition model and the divisor identity, positivity, and modular congruences; it does not state fixed-shift correlations. Merca's October 2026 dyadic follow-up studies pointwise dyadic decompositions and congruences. His broader signed-enumeration paper treats generating functions for arbitrary numbers of part sizes, rather than arithmetic lag kernels. The present evaluation uses classical divisor-function and Chinese-remainder averaging, so that general method is not claimed as novel; the explicit all-shift kernel, its nontrivial dyadic local factor, and the prime-lag sign reversal are the distinct findings. A reported marginal law for \(a(n)/n\) does not imply the pair correlation at any fixed positive shift.

## Limitations
The error constants may depend on the fixed shift and on \(\varepsilon\). No effective error uniform for shifts growing with \(X\), no limiting joint distribution, and no claim about higher-point correlations is asserted. The arithmetic calculation is not an independent peer review. It does not establish that the derived theorem is absent from every unindexed source.

## References
1. M. Merca, *The two-block odd partition function*, arXiv:2609.33770v1, posted 27 September 2026, published in *The Ramanujan Journal* 71, article 23 (2026), https://doi.org/10.1007/s11139-026-01426-1 .
2. M. Merca, *Dyadic Structure of the Two-Block Odd Partition Function and Theta-Weighted Congruences for pod(n)*, arXiv:2610.05020v1, 4 October 2026, https://arxiv.org/abs/2610.05020 .
3. M. Merca, *Signed Enumeration of Partitions with Exactly k Distinct Magnitudes of Odd Multiplicity*, *Mediterranean Journal of Mathematics* 23, 212 (2026), https://doi.org/10.1007/s00009-026-03168-2 .
4. L. Tóth, *Multiplicative Arithmetic Functions of Several Variables: A Survey*, arXiv:1310.7053, https://arxiv.org/abs/1310.7053 .
