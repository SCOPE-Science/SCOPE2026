# An exact quartic grid-phase law for oblique half-plane jittered quadrature

## Finding

Let \(a,b\) be coprime positive integers with \(1\le a\le b\), and let \(0<c<a\) be real. Independently draw one uniformly distributed point inside each of the \(n^2\) cells of the standard \(n\times n\) square partition. Evaluate the half-plane indicator \(f(x,y)=\mathbf 1_{\{ax+by>c\}}\) at those points and average, obtaining \(Q_n\). This unbiased randomized quadrature has the following **exact finite-sample variance** and **sharp leading grid-phase law**.

Write \(m_n=\lfloor nc\rfloor\), \(\theta_n=nc-m_n\), and
\[
N_{a,b}(s)=\#\{(i,j)\in\mathbb Z_{\ge0}^2:ai+bj=s\},\qquad N_{a,b}(s)=0\quad(s<0).
\]
For independent uniforms \(U,V\) on \([0,1]\), put \(F_{a,b}(z)=\Pr(aU+bV\le z)\), and \(v_{a,b}(z)=F_{a,b}(z)(1-F_{a,b}(z))\). For every integer \(n\ge1\),
\[
\boxed{\operatorname{Var}(Q_n)=\frac1{n^4}\sum_{k=0}^{a+b-1}N_{a,b}(m_n-k)\,v_{a,b}(k+\theta_n).}
\]
Define
\[
C_{a,b}=\frac{-a^4+5a^3b+10ab^3+1}{60ab^2}.
\]
Then, with an error bounded by a constant depending only on \(a,b,c\),
\[
\boxed{n^3\operatorname{Var}(Q_n)=\frac{c}{ab}\left[C_{a,b}-\frac{\theta_n^2(1-\theta_n)^2}{2ab^2}\right]+O_{a,b,c}(n^{-1}).}
\]
The complete leading dependence on the lattice alignment is always the same quartic waveform. If \(c\) is irrational, the set of subsequential limits of \(n^3\operatorname{Var}(Q_n)\) is precisely
\[
\boxed{\left[\frac{c}{ab}\left(C_{a,b}-\frac1{32ab^2}\right),\ \frac{c}{ab}C_{a,b}\right].}
\]
If \(c=p/q\) is rational in lowest terms, the finite cluster set is exactly
\[
\left\{\frac{c}{ab}\left[C_{a,b}-\frac{(k/q)^2(1-k/q)^2}{2ab^2}\right]:k=0,\ldots,q-1\right\}.
\]
For odd \(q\) the minimum is \(\frac{c}{ab}[C_{a,b}-(q^2-1)^2/(32ab^2q^4)]\), and for even \(q\) it is \(\frac{c}{ab}[C_{a,b}-1/(32ab^2)]\); the maximum is always \(cC_{a,b}/(ab)\). In the primitive diagonal case \(a=b=1\), the irrational-height limiting interval is exactly \([7c/32,c/4]\).

## Assumptions and scope

The draws are independent *between* all cells, and each is uniform inside its own cell; there is precisely one function evaluation per cell and equal weights \(n^{-2}\). The integers \(a,b\) are fixed and coprime, \(1\le a\le b\), and \(c\in(0,a)\) is fixed as \(n\to\infty\). The half-plane is measured within the unit square. The strict inequality at the boundary is immaterial because the sampling distribution is continuous. The exact integral and expected quadrature value are \(1-c^2/(2ab)\). The equal-slope primitive case is \(a=b=1\); multiples \(a=b>1\) are not within the coprime hypothesis. The formulas make no claim about other partition geometries, correlated sampling, changing slopes, or smooth-function integration.

The distribution function used above is explicitly
\[
F_{a,b}(z)=\begin{cases}
0,&z\le0,\\
z^2/(2ab),&0<z\le a,\\
(z-a/2)/b,&a<z\le b,\\
1-(a+b-z)^2/(2ab),&b<z<a+b,\\
1,&z\ge a+b.
\end{cases}
\]
The adjacent branches agree at every boundary, including when \(a=b\).

## Proof

**1. Exact cell reduction.** The cell indexed by \((i,j)\), \(0\le i,j<n\), contains the random point \(((i+U_{ij})/n,(j+V_{ij})/n)\). Its Bernoulli success probability is \(1-F_{a,b}(nc-ai-bj)\), so independence yields
\[
n^4\operatorname{Var}(Q_n)=\sum_{i,j=0}^{n-1}v_{a,b}(nc-ai-bj).
\]
Write \(nc=m_n+\theta_n\). Since \(v_{a,b}(z)=0\) outside \((0,a+b)\), only \(ai+bj=m_n-k\) for \(0\le k\le a+b-1\) can contribute. Every nonnegative solution of such an equation lies in the finite sample grid: \(ai+bj\le m_n<na\) implies \(i<n\), and \(bj\le m_n<na\le nb\) implies \(j<n\). Grouping by \(k\) proves the exact formula, including \(n=1\) and alignment endpoints.

**2. The quartic sum.** Put \(t\in[0,1]\). The continuous formula for \(F_{a,b}\) gives
\[
W_{a,b}(t):=\sum_{k=0}^{a+b-1}v_{a,b}(k+t)
=\frac{S_2}{2ab}-\frac{S_4}{4a^2b^2}+M,
\]
where the lower and reflected upper triangular branches and the middle linear branch respectively give
\[
S_2=\sum_{k=0}^{a-1}(k+t)^2+\sum_{j=1}^{a}(j-t)^2
=\frac a3(2a^2+6t^2-6t+1),
\]
\[
S_4=\sum_{k=0}^{a-1}(k+t)^4+\sum_{j=1}^{a}(j-t)^4
=\frac a{15}(6a^4+60a^2t^2-60a^2t+10a^2+30t^4-60t^3+30t^2-1),
\]
and
\[
M=\sum_{k=a}^{b-1}\left(\frac{k+t-a/2}{b}-\frac{(k+t-a/2)^2}{b^2}\right)
=\frac{(a-b)(a^2-2ab-2b^2+12t^2-12t+2)}{12b^2}.
\]
The middle sum is empty when \(a=b\), and the closed expression for \(M\) then vanishes. Substitution and cancellation give the exact finite identity
\[
\boxed{W_{a,b}(t)=C_{a,b}-\frac{t^2(1-t)^2}{2ab^2}.}
\]
This is an algebraic identity for all integer \(1\le a\le b\); coprimality is needed in the next step.

**3. Primitive lattice counting.** Since \(\gcd(a,b)=1\), for each nonnegative integer \(s\), the allowable nonnegative \(j\) solving \(bj\equiv s\pmod a\) form one residue class modulo \(a\). If \(j_0\in\{0,\ldots,a-1\}\) represents it, the count is \(\max(0,1+\lfloor(s/b-j_0)/a\rfloor)\). Thus \(N_{a,b}(s)=s/(ab)+O_{a,b}(1)\) uniformly over \(s\ge0\). In the exact variance formula each \(s=m_n-k=nc+O_{a,b}(1)\), and the number of summands is fixed. Consequently
\[
n^3\operatorname{Var}(Q_n)=\frac c{ab}W_{a,b}(\theta_n)+O_{a,b,c}(n^{-1}),
\]
which proves the displayed leading law.

**4. Complete limit sets.** The polynomial \(t^2(1-t)^2\) ranges over \([0,1/16]\) on \([0,1]\), with its unique maximum at \(t=1/2\) and minima at the endpoints. If \(c\) is irrational, \(\{nc\}\) is dense in \([0,1]\); continuity and the vanishing error establish the entire closed interval as the cluster set. If \(c=p/q\) is reduced, its phases cycle through precisely the residues \(k/q\). Their closest point to \(1/2\) yields the asserted parity-specific minima. This proves every claimed endpoint and the absence of other cluster values.

## Verification

A standalone exact-rational verifier, `verify.py`, independently computes all cell probabilities and compares the direct variance with the lattice-count formula for multiple primitive slopes, heights and grid sizes. It also checks the universal quartic identity against independent convolution-CDF evaluations for many slopes and rational phases, tests the diagonal endpoints, and checks the elementary lattice-count discrepancy over finite ranges. Its recorded result is `PASS: 1742 independent exact-rational assertions`. The analytical sums, coprime lattice-count estimate and irrational-rotation argument—not finite testing—prove the unrestricted theorem. To replay, run `python verify.py` with Python 3 and the standard library.

## Relationship to prior work

Kiderlen–Pausinger (first posted 2020) prove general partition/discrepancy principles for stratified samples and analyze diagonal-line *partition geometries*. They do not directly state the fixed oblique-indicator variance coefficient under the ordinary axis-aligned square grid. Kirk–Pausinger (first posted 2022) compute the *integrated* expected squared discrepancy of jittered sampling, rather than the variance for one rational-slope oblique half-plane. Kunsch (first posted 2023) studies randomized integration bounds and stratified control variates on Sobolev classes, including low regularity; that setting does not supply the arithmetic quartic alignment law. The basic independent-stratum variance sum is standard, so novelty is claimed only for its full primitive-integer-direction exact reduction, quartic cancellation and arithmetic classification of all possible leading constants. The literature comparisons do not amount to publication-priority certification.

## Limitations

The law requires a fixed primitive integer normal, a threshold strictly below the smaller coefficient, independent per-cell jitter and the square grid. It does not assert an error constant for irrational normal directions, thresholds whose line crosses other edges of the square, nonuniform cells, or estimators with common random shifts. The variance limit need not exist when \(c\) is irrational: its cluster interval is the correct statement. A same-scope result in older specialized sampling literature could change the novelty assessment. Independent scientific review has not occurred.

## References

1. M. Kiderlen and F. Pausinger, *Discrepancy of stratified samples from partitions of the unit cube*, arXiv:2008.12026, first submitted 2020-08-27; journal version: https://link.springer.com/article/10.1007/s00605-021-01538-4 .
2. N. Kirk and F. Pausinger, *On the expected L2-discrepancy of jittered sampling*, arXiv:2208.08924, first submitted 2022-08-18; https://arxiv.org/abs/2208.08924 .
3. R. J. Kunsch, *Linear Monte Carlo quadrature with optimal confidence intervals*, arXiv:2309.09059, first submitted 2023-09-16; https://arxiv.org/abs/2309.09059 .
4. K. Basu and A. B. Owen, *Quasi-Monte Carlo for an integrand with a singularity along a diagonal in the square*, arXiv:1609.07444, first submitted 2016-09-23; https://arxiv.org/abs/1609.07444 .
