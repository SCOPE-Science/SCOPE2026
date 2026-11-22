# Mertens lower-tail law for Erdős's prime-power quotient sum

## Finding

Let \(w(1)=0\), and, for every integer \(n\ge2\) with prime-power factorization \(n=\prod_{p^a\parallel n}p^a\), set
\[
w(n)=\sum_{p^a\parallel n}\frac{n}{p^a},\qquad f(n)=\frac{w(n)}n=\sum_{p^a\parallel n}p^{-a}.
\]
The empirical distribution of \(f(n)\) has a continuous, atomless limit with full topological support \([0,\infty)\). Write
\[
F(t)=\lim_{X\to\infty}\frac1{\lfloor X\rfloor}\#\{1\le n\le \lfloor X\rfloor:f(n)\le t\},\qquad t\in\mathbb R.
\]
Then \(F(t)=0\) for \(t\le0\), and the lower endpoint has the *sharp* asymptotic
\[
\boxed{\displaystyle F(t)\sim\frac{e^{-\gamma}}{\log(1/t)}\quad(t\downarrow0),}
\]
where \(\gamma\) is the Euler–Mascheroni constant. Hence, for every fixed \(\alpha\ge1\),
\[
\boxed{\displaystyle\lim_{t\downarrow0}\frac{F(t^\alpha)}{F(t)}=\frac1\alpha.}
\]
Equivalently, with \(S\) distributed according to \(F\), the conditional variable \(\log(1/S)/\log(1/t)\), given \(0<S\le t\), converges in distribution to the Pareto law on \([1,\infty)\) having survival function \(\Pr(Y\ge\alpha)=1/\alpha\) for \(\alpha\ge1\).

## Assumptions and scope

All indices are positive integers. The notation \(p^a\parallel n\) means that \(a\ge1\) is the *exact* exponent of the prime \(p\) in \(n\); distinct prime powers are counted once each. We put \(f(1)=0\). Natural densities are over the initial interval \(1\le n\le\lfloor X\rfloor\), followed by \(X\to\infty\). The endpoint limit \(t\downarrow0\) is taken *after* that density limit, not jointly with \(X\). The theorem does not assert an effective two-variable bound in \(X\) and \(t\).

Define mutually independent prime-indexed random variables \(Z_p\) with
\[
\Pr(Z_p=0)=1-\frac1p,\qquad
\Pr(Z_p=p^{-a})=\frac{1-1/p}{p^a}\quad(a\ge1).
\]
These probabilities sum to one. The random series \(S=\sum_pZ_p\) converges almost surely since it is nonnegative and
\[
\mathbb ES=\sum_p\frac1{p(p+1)}<\infty.
\]
In fact the limiting distribution is the law of \(S\), with Laplace transform, for \(s\ge0\),
\[
\mathbb Ee^{-sS}=\prod_p\left(1-\frac1p\right)
\left(1+\sum_{a\ge1}\frac{e^{-s/p^a}}{p^a}\right).
\]

## Proof

### 1. The limiting distribution

For each fixed finite collection of primes, the Chinese remainder theorem gives independent exact-valuation densities
\[
\lim_{X\to\infty}\frac{\#\{n\le X:v_p(n)=a\}}{\lfloor X\rfloor}
=\left(1-\frac1p\right)p^{-a}\quad(a\ge0).
\]
For the untruncated arithmetic sum, uniformly in \(X\ge1\), the contribution from primes greater than \(P\) is bounded in mean by
\[
\frac1{\lfloor X\rfloor}\sum_{n\le X}\sum_{\substack{p>P\\p^a\parallel n}}p^{-a}
\le\sum_{p>P}\frac1p\frac{\lfloor X/p\rfloor}{\lfloor X\rfloor}
\le\sum_{p>P}\frac1{p^2}\longrightarrow0.
\]
The same tail bound holds for \(S\), by \(\mathbb EZ_p=1/[p(p+1)]\). Finite-prime cylinder convergence plus these uniform \(L^1\) tail estimates proves weak convergence of the empirical laws to the law of \(S\).

The function \(f\) is additive on coprime factors and \(f(p)=1/p\). Its Erdős–Wintner series converge: the linear and quadratic prime sums are bounded by \(\sum_p p^{-2}\) and \(\sum_p p^{-3}\), respectively, and the large-value series is empty. The classical continuity criterion applies since \(\sum_{p:f(p)\ne0}1/p=\sum_p1/p\) diverges. Thus the limiting law has no atoms, and the displayed density limit holds for every real \(t\), including \(t=0\). Since \(S\ge0\), necessarily \(F(t)=0\) for \(t\le0\).

To verify full support, fix \(u\ge0\) and \(\varepsilon>0\). Choose a sufficiently large prime cutoff \(P\) such that \(1/P<\varepsilon/8\) and the expected tail beyond \(P\) is smaller than \(\varepsilon/8\). By divergence of \(\sum_p1/p\) and the vanishing individual terms, select a finite subset of primes larger than \(P\), all at exponent one, whose reciprocal sum differs from \(u\) by less than \(\varepsilon/4\) (for \(u=0\), use the empty set). Take \(Q\) larger than every selected prime and sufficiently large that the expected remaining tail beyond \(Q\) is smaller than \(\varepsilon/8\). The event setting \(Z_p\) to the chosen value for each \(p\le Q\), and zero for every other \(p\le Q\), has strictly positive probability. Independently, Markov's inequality gives positive probability that the tail beyond \(Q\) is less than \(\varepsilon/4\). The resulting \(S\) lies within \(\varepsilon\) of \(u\). Thus every relative neighborhood in \([0,\infty)\) has positive probability, proving the full support claim.

### 2. Two-sided prime-cylinder bounds near zero

Let \(y\to\infty\), and abbreviate
\[
M(y)=\prod_{p\le y}\left(1-\frac1p\right).
\]
On the event \(Z_p=0\) for every \(p\le y\), of probability exactly \(M(y)\), only primes larger than \(y\) contribute. Their conditional mean is
\[
\mathbb E\sum_{p>y}Z_p
=\sum_{p>y}\frac1{p(p+1)}
\ll\frac1{y\log y},
\]
by the standard upper bound \(\pi(v)\ll v/\log v\) and partial summation. Markov's inequality and independence consequently yield
\[
F(1/y)\ge M(y)\left(1-O\left(\frac1{\log y}\right)\right).
\tag{1}
\]

For an upper bound, \(S\le1/y\) forces each nonnegative summand \(Z_p\le1/y\). For \(p\le y\) define
\[
h_p=\min\{a\ge1:p^a\ge y\}.
\]
Thus the allowable values of \(Z_p\) are zero and \(p^{-a}\) with \(a\ge h_p\), and, by the geometric valuation distribution, their total probability is \(1-1/p+p^{-h_p}\). Independence implies
\[
F(1/y)\le\prod_{p\le y}\left(1-\frac1p+p^{-h_p}\right).
\tag{2}
\]
For \(p\le\sqrt y\), \(p^{-h_p}\le1/y\), so their sum is at most \(\pi(\sqrt y)/y\). For \(\sqrt y<p<y\), \(h_p=2\) and \(\sum_{p>\sqrt y}p^{-2}\ll y^{-1/2}\). If \(y\) itself is prime, the remaining single term \(p=y\) contributes \(1/y\). Therefore
\[
\sum_{p\le y}p^{-h_p}\ll y^{-1/2}.
\]
Since \(1-1/p\ge1/2\), dividing the right-hand side of (2) by \(M(y)\), taking logarithms, and using \(\log(1+x)\le x\) gives
\[
F(1/y)\le M(y)\bigl(1+O(y^{-1/2})\bigr).
\tag{3}
\]
Equations (1) and (3) yield \(F(1/y)\sim M(y)\). Mertens' product theorem states \(M(y)\sim e^{-\gamma}/\log y\), proving the asserted sharp small-value law.

### 3. Conditional logarithmic scaling

For fixed \(\alpha\ge1\), continuity at positive thresholds and \(F(0)=0\) give
\[
\Pr\!\left(\frac{\log(1/S)}{\log(1/t)}\ge\alpha\ \middle|\ 0<S\le t\right)
=\frac{F(t^\alpha)}{F(t)}\longrightarrow\frac1\alpha.
\]
This is the survival function of the stated Pareto law; at \(\alpha=1\) the ratio equals one. All three parts concern the same limiting law, completing the theorem.

## Verification

The standalone `CHECK.py` (Python standard library only) verifies the defining identity \(w(n)=nf(n)\) in exact rational arithmetic for \(1\le n\le4500\), enumerates exact prime-valuation cylinder probabilities for \(p\in\{2,3,5,7\}\) through depth five, and verifies the finite-prime necessary-condition upper products for several \(y\). It also measures the ratio of the upper cylinder product to \(M(1000)\). Execute `python CHECK.py` beside this document. The expected completion marker is `PRIME_POWER_RECIPROCAL_ENDPOINT_OK`. These finite checks verify arithmetic and formulas only; the infinite assertions use the preceding proof and named classical theorems.

## Relationship to prior work

Campbell, *On a problem due to Erdős concerning* \(w_1(n)\) (first public version 2026-11-05), introduced the same \(w(n)\) notation from Erdős and proved positive lower linear growth for the image-set counting function \(V(x)=\#\{w(n):n\le x\}\). The present result concerns a different statistic: the natural-density distribution of the normalized values \(w(n)/n\), especially the sharp lower-endpoint law and its conditional scaling. No image-set growth assertion is claimed here.

The existence and atomlessness of the limiting additive-function distribution are applications of the classical Erdős–Wintner theorem; these aspects are explicitly not claimed as independent novel machinery. Mertens' classical prime product is also an ingredient. The contribution is their combination with the exact-valuation cylinder squeeze that determines the endpoint constant for this specific natural arithmetic statistic. General related results about reciprocal prime-divisor sums and unrelated Pareto laws do not by themselves imply the displayed formula for \(w(n)/n\).

## Limitations

The result is an *iterated* density-then-endpoint limit, not a uniform estimate for growing thresholds as a function of the integer cutoff. It gives no density formula at general positive arguments beyond the convergent random-prime product and no upper-tail asymptotic. The Pareto limit is a direct consequence of the sharp endpoint law rather than a separate independent theorem. An equivalent endpoint statement hidden in general small-deviation theory for additive functions or a nonindexed source is a residual literature risk. No independent mathematical validation is asserted.

## References

1. J. M. Campbell, *On a problem due to Erdős concerning* \(w_1(n)\), arXiv:2611.07617v1 (2026-11-05), https://arxiv.org/abs/2611.07617 ; full text https://arxiv.org/html/2611.07617 . Primary MSC2020: 11N64.
2. P. Erdős and A. Wintner, *Additive arithmetical functions and statistical independence*, American Journal of Mathematics 61 (1939), 713–721. The limiting-distribution and continuity criteria are classical.
3. P. D. T. A. Elliott, *Probabilistic Number Theory I: Mean-Value Theorems*, Springer (1979), chapter on the Erdős–Wintner theorem.
4. F. Mertens, *Ein Beitrag zur analytischen Zahlentheorie*, Journal für die reine und angewandte Mathematik 78 (1874), 46–62. The prime-product asymptotic is classical.
5. V. Bergelson, J. Kułaga-Przymus, M. Lemańczyk and F. K. Richter, *A generalization of Kátai's orthogonality criterion with applications*, arXiv:1705.07322v2 (2017), §2.3, Theorem 2.11 (a restatement of Erdős–Wintner).
