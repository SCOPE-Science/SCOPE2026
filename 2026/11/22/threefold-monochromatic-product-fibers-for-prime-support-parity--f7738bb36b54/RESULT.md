# Threefold monochromatic product fibers for prime-support parity

## Finding

Color every positive integer according to the parity of its number of distinct prime divisors: \(\chi(n)=(-1)^{\omega(n)}\), with \(\omega(1)=0\). Let \(R(n)\) be the number of **ordered** triples \((a,b,c)\) of integers strictly greater than one satisfying \(abc=n\) and \(\chi(a)=\chi(b)=\chi(c)\).

For every positive integer \(n\), write its distinct-prime factorization as \(n=\prod_{i=1}^{r}p_i^{e_i}\) with \(e_i\ge1\), and interpret products over the empty set as one. Define

\[
\begin{aligned}
A(n)&=\prod_{i=1}^{r}\binom{e_i+2}{2},\\
B(n)&=\prod_{i=1}^{r}\frac{e_i^2-5e_i+2}{2},\\
C(n)&=\prod_{i=1}^{r}(e_i+1),\\
D(n)&=\prod_{i=1}^{r}(1-e_i),\\
E(n)&=\prod_{i=1}^{r}(e_i-3).
\end{aligned}
\]

Then the **exact threefold fiber count** is

\[
\boxed{R(n)=\frac{A(n)+3B(n)-3C(n)-6D(n)-3E(n)}4
+\frac32\bigl(1+(-1)^r\bigr)-\mathbf1_{n=1}.}
\]

As a squarefree specialization, when \(n\) is a product of \(r\ge1\) distinct primes,

\[
\boxed{R(n)=\begin{cases}
(3^r-3)/4,&r\text{ odd},\\
(3^r-6\cdot2^r+15)/4,&r\text{ even}.
\end{cases}}
\]

It follows that \(R(n)=0\) **if and only if** \(n\) is one of the following: \(1\), a prime, a square of a prime, a product of two distinct primes, or a squarefree product of four distinct primes. Consequently, writing \(Z(X)=\#\{1\le n\le X:R(n)=0\}\),

\[
\boxed{Z(X)\sim\frac{X(\log\log X)^3}{6\log X}\quad(X\to\infty).}
\]

All claims use the same nonunit-factor convention, which is essential.

## Assumptions and scope

The domain is all positive integers \(n\), with repetitions of primes in the factorization allowed. The three factors are **ordered**, each is strictly greater than one, and their parity colors must coincide; the color of their *product* is unrestricted. There are no coprimality requirements among the factors. Empty prime products are one, and \(\mathbf1_{n=1}\) denotes the indicator of \(n=1\). The notation \(\sim\) denotes ratio tending to one as \(X\to\infty\).

## Proof

**1. Character projector.** Put \(f(n)=(-1)^{\omega(n)}\) and let \(\mathbf1(n)=1\). The function \(f\) is multiplicative, although not completely multiplicative. For three signs \(u,v,w\in\{-1,1\}\), their equality indicator is

\[
\mathbf1_{u=v=w}=\frac{1+uv+uw+vw}{4}.
\]

Let \(*\) denote Dirichlet convolution and \(d_j=\mathbf1^{*j}\). Summing this identity over all positive ordered factor triples of product \(n\), including factors equal to one, gives

\[
T(n)=\frac{d_3(n)+3(f*f*\mathbf1)(n)}4.
\]

The number of equal-color triples with a specified coordinate equal to one is

\[
U(n)=\frac{d_2(n)+2(f*\mathbf1)(n)+(f*f)(n)}4,
\]

because the remaining two colors must both equal \(f(1)=1\). The number with two specified coordinates equal to one is \((1+f(n))/2\), and the number with all three equal to one is \(\mathbf1_{n=1}\). Inclusion–exclusion therefore yields, **for every \(n\ge1\)**,

\[
R(n)=\frac{d_3(n)+3(f*f*\mathbf1)(n)-3d_2(n)-6(f*\mathbf1)(n)-3(f*f)(n)}4
+\frac32(1+f(n))-\mathbf1_{n=1}.
\]

**2. Exact prime-power factors.** For any prime \(p\) and exponent \(e\ge1\), one has \(f(p^e)=-1\) and \(f(1)=1\). Direct convolution therefore gives

\[
\begin{aligned}
d_3(p^e)&=\binom{e+2}{2},&d_2(p^e)&=e+1,\\
(f*\mathbf1)(p^e)&=1-e,&(f*f)(p^e)&=e-3,\\
(f*f*\mathbf1)(p^e)&=1+\sum_{j=1}^e(j-3)=\frac{e^2-5e+2}{2}.
\end{aligned}
\]

Each displayed convolution is multiplicative, and \(f(n)=(-1)^r\). Multiplying the prime-power evaluations yields the stated fiber formula. The convention at \(n=1\) follows from the preceding inclusion–exclusion, not from an exceptional extension of the prime-power formulas.

**3. Complete support classification.** If \(n\) has at least three distinct prime factors, write \(n=\prod_{i=1}^{r}p_i^{e_i}\). When \(r\ge3\) is odd, the explicit factorization

\[
(p_1^{e_1},\ p_2^{e_2},\ \prod_{i=3}^r p_i^{e_i})
\]

has prime-support cardinalities \(1,1,r-2\), all odd. When \(r\ge6\) is even, use the disjoint prime-support blocks of sizes \(2,2,r-4\), all even, assigning each prime power wholly to its block. When \(r=4\) and at least one exponent, say \(e_1\), is at least two, the three factors

\[
(p_1,\ p_1^{e_1-1},\ \prod_{i=2}^{4}p_i^{e_i})
\]

have support cardinalities \(1,1,3\). For \(r=2\) with a repeated prime \(p_1\), the factors \((p_1,p_1^{e_1-1},p_2^{e_2})\) have one distinct prime each. For \(r=1\) and exponent at least three, \((p_1,p_1,p_1^{e_1-2})\) works.

The remaining numbers are exactly \(1\), primes, prime squares, squarefree semiprimes and squarefree products of four distinct primes. In the first four cases there are fewer than three prime factors counted with multiplicity, so no triple of nonunits exists. For squarefree products of four distinct primes, the three support sets of a nonunit factorization form a partition of four elements into three positive cardinalities. If all three cardinalities are odd, their sum is odd; if all are even, their sum is at least six. Both contradict a sum of four. Thus no unlisted exceptions exist.

**4. Count of exceptions.** The standard fixed-order Landau asymptotic for squarefree integers with exactly four distinct prime factors is \(X(\log\log X)^3/(6\log X)\). The other exceptional families contain only one, primes, prime squares and squarefree semiprimes, jointly \(O(X\log\log X/\log X)\), with prime squares negligible. Consequently the four-prime family supplies the displayed leading term.

## Verification

The standalone standard-library script `verify.py` independently enumerates all positive ordered nonunit triples for \(1\le n\le2500\), compares their actual colors to the exact formula and the complete zero-set characterization, and tests eight additional structured larger instances. Execute `python3 verify.py` in the directory containing this result and script. It prints `PASS: 2508 independently enumerated integers; support and counts agree`. The proof above applies to every positive integer independently of these finite experiments.

## Relationship to prior work

The November 1, 2026 preprint by J. M. Campbell formulates monochromatic **two-factor** products for arbitrary two-colorings, and proves that the infimum of their lower densities is zero. The present claim is a different, fixed arithmetic coloring and demands **three nonunit factors**; it determines every ordered fiber and the complete exceptional set, not a worst-case two-factor density. The general monochromatic equation \(xy=z\) is studied by Aragão, Chapman, Ortega and Souza (2025), but their color constraint includes the output \(z\), unlike the present threefactor product. The classical Landau theorem supplies the asymptotic consequence once the exact exceptions are known; it does not establish the fiber count or classification. Prior number-theory work on unconstrained ordered factorization counts supplies a useful comparison, but counting by parity color is an additional constraint.

## Limitations

The result is restricted to the particular two-coloring \((-1)^{\omega(n)}\), exactly three factors, and nonunit factors. It gives no universal-density theorem for arbitrary colorings and no optimal bound for other numbers of factors. Standard published Landau asymptotics are used as known input, not independently reproved. Historical database and open-web searches cannot guarantee uniqueness; an older unindexed special case may exist. Independent mathematical validation has not been performed.

## References

1. J. M. Campbell, *A solution to the Erdős–Sárközy product-density problem*, arXiv:2611.01480v1 (November 1, 2026), https://arxiv.org/abs/2611.01480.
2. L. Aragão, J. Chapman, M. Ortega and V. Souza, *On the number of monochromatic solutions to multiplicative equations*, *Combinatorica* 45 (2025), article 64, https://doi.org/10.1007/s00493-025-00183-x.
3. E. Landau, classical fixed-order asymptotic for integers with a prescribed number of prime factors; see also M. Belton, *Asymptotic density of k-almost primes*, arXiv:1401.2694, https://arxiv.org/abs/1401.2694.
