# Arithmetic density of positive lag covariance in prime-power Pascal columns

## Finding

Fix a prime \(p\) and an integer \(a\ge1\), and put \(r=p^a\). For integers \(n\ge r\), let
\[
V(n)=\nu_p\!\left(\binom n r\right).
\]
For every positive integer lag \(h\), the Cesàro covariance
\[
C(h)=\lim_{N\to\infty}\left[\frac1N\sum_{n=r}^{r+N-1}V(n)V(n+h)
-\left(\frac1N\sum_{n=r}^{r+N-1}V(n)\right)
\left(\frac1N\sum_{n=r}^{r+N-1}V(n+h)\right)\right]
\]
exists and never vanishes. Define \(\mathcal P_{p,a}=\{h\ge1:C(h)>0\}\). The **natural density** of this set exists, and admits the following finite rational formula. Set
\[
c_d=\left\lfloor\frac{p^{a+d}}{(p+1)(p^d-1)}\right\rfloor\quad(1\le d\le a),
\qquad c_\infty=\left\lfloor\frac{p^a}{p+1}\right\rfloor.
\]
Then
\[
\boxed{\displaystyle
\delta_{p,a}=\lim_{H\to\infty}\frac{\#(\mathcal P_{p,a}\cap[1,H])}{H}
=\sum_{d=1}^a\frac{(p-1)(2p^a-1-2c_d)}{p^{a+d+1}}
+\frac{2p^a-1-2c_\infty}{p^{2a+1}}.}
\]
For example, \(\delta_{2,1}=1/2\), \(\delta_{3,1}=11/27\), \(\delta_{3,2}=35/81\), and \(\delta_{5,2}=197/625\). At fixed \(p\), these rational numbers have the limit
\[
\boxed{\displaystyle
\delta_{p,\infty}=\frac2p-\frac{2(p-1)}{p(p+1)}\sum_{d=1}^{\infty}\frac1{p^d-1},
\qquad |\delta_{p,a}-\delta_{p,\infty}|\le p^{-a-1}.}
\]
The convergent Lambert-type series encodes the accumulation of prime-power resonances. In particular, for a fixed column the covariance does not eventually have a constant sign: positive and negative lags each have positive natural density.

## Assumptions and scope

The prime \(p\) includes \(2\); the exponent \(a\) is any positive integer; \(h\) is any positive integer. The valuation \(\nu_p(m)\) is the exponent of \(p\) dividing a nonzero integer \(m\). The limiting mean and covariance are over the index \(n\), while \(\delta_{p,a}\) is a **second, different limit** over the lag \(h\). The convention \(\alpha_p(0)=0\) is used below, without assigning a finite valuation to zero. No claims are made for non-prime-power lower binomial columns or non-Cesàro sampling of the index.

## Proof

**1. Reduction to one valuation sequence.** By Kummer's theorem, the \(p\)-adic order of \(\binom n{p^a}\) is the number of borrows when subtracting the base-\(p\) number \(p^a\) from \(n\). The borrow begins precisely when the base-\(p\) digit of \(n\) at position \(a\) is zero and runs through consecutive zero digits. Thus, for every \(n\ge p^a\),
\[
V(n)=\nu_p\left(\left\lfloor\frac n{p^a}\right\rfloor\right).
\]
The exceptional \(n\) for which the right-hand argument is zero are excluded by \(n\ge r\).

**2. Two-point valuation moments.** Let \(U\) be Haar-uniform in \(\mathbb Z_p\), and write \(W=\nu_p(U)\), with the measure-zero infinite case ignored. Summing valuation thresholds gives
\[
\mathbb E W=\frac1{p-1},\qquad \mathbb EW^2=\frac{p+1}{(p-1)^2}.
\]
For a nonzero integer \(c\) with \(d=\nu_p(c)\), expand \(W\nu_p(U+c)\) into indicators of simultaneous congruences \(U\equiv0\pmod{p^j}\), \(U\equiv-c\pmod{p^k}\). The congruences are compatible exactly when \(\min(j,k)\le d\), in which case their probability is \(p^{-\max(j,k)}\). Summing gives
\[
\mathbb E[\nu_p(U)\nu_p(U+c)]
=\frac{p+1}{(p-1)^2}(1-p^{-d}).
\]
For \(c=0\), the moment is \((p+1)/(p-1)^2\). Introduce the abbreviation
\[
\alpha_p(c)=\begin{cases}0,&c=0,\\p^{-\nu_p(|c|)},&c\ne0.\end{cases}
\]
The joint moment is therefore \(\frac{p+1}{(p-1)^2}(1-\alpha_p(c))\) for every integer \(c\).

**3. Exact lag covariance.** Divide \(h=rt+u\), where \(t\ge0\), \(0\le u<r\). For a uniformly sampled residue \(s\in\{0,\ldots,r-1\}\), the pair of integer quotients at lag \(h\) is \((q,q+t)\) for \(r-u\) choices of \(s\), and \((q,q+t+1)\) for the remaining \(u\) choices. Each \(q\) becomes equidistributed modulo arbitrary powers of \(p\) as the index interval grows. Truncation by \(\min\{\nu_p(q),M\}\), followed by the geometric second-moment bound, justifies passage from residue averages to the full unbounded covariance. Substituting the preceding moment formula and the common mean \(1/(p-1)\) yields
\[
\boxed{\displaystyle
C(h)=\frac{p-(p+1)\left(\frac{r-u}{r}\alpha_p(t)+\frac{u}{r}\alpha_p(t+1)\right)}{(p-1)^2}.}
\]
This explicit local two-point covariance is an auxiliary consequence of standard prime-adic valuation intersection methods; the new claimed invariant is the **distribution of its sign across all lags**, including its fixed-prime column-depth limit.

**4. Sharp sign and nonvanishing.** If both \(t\) and \(t+1\) are prime-to-\(p\), then \(C(h)=-1/(p-1)^2\). Otherwise exactly one is divisible by \(p\). If \(t\equiv0\pmod p\), let \(d=\nu_p(t)\ge1\), permitting \(d=\infty\) for \(t=0\); then \(C(h)>0\) precisely when
\[
\frac{r-u}{r}>g_d:=\frac{p^d}{(p+1)(p^d-1)},\qquad g_\infty:=\frac1{p+1}.
\]
If \(t+1\equiv0\pmod p\), the corresponding condition is \(u/r>g_d\), with \(d=\nu_p(t+1)\ge1\). In either finite-\(d\) case, equality would imply
\[
\nu_p(u)=a+d\quad\text{or}\quad\nu_p(r-u)=a+d,
\]
respectively, because \((p+1)(p^d-1)\) is a \(p\)-adic unit; both are impossible for \(0<u<r\). In the \(d=\infty\) case equality would require \(p+1\) to divide \(p^a\), also impossible. Therefore \(C(h)\ne0\) for all positive \(h\).

For a finite \(d\ge1\), \(rg_d\) is not an integer, so among \(u\in\{0,\ldots,r-1\}\) the first type has \(r-c_d\) positive choices and the second has \(r-1-c_d\), with \(c_d=\lfloor rg_d\rfloor\). Thus \(2r-1-2c_d\) of the combined \(2r\) remainder opportunities are positive, taking one residue class of \(t\) for each type.

**5. Density over all positive shifts.** For \(d\ge1\), the integers \(t\) with \(\nu_p(t)=d\) have natural density \((p-1)/p^{d+1}\); the same is true of \(\nu_p(t+1)=d\). These two types are disjoint. As \(h\) varies, each \(t\) supplies exactly \(r\) consecutive possible remainder values. The tail of the valuation-depth partition at \(d>D\) has density bounded by \(2/p^{D+1}\); hence finite-layer counts converge to a natural density, without assuming a periodicity that is not present. We obtain the absolutely convergent expression
\[
\delta_{p,a}=\sum_{d=1}^{\infty}\frac{p-1}{p^{d+1}}\frac{2r-1-2c_d}{r}.
\]
For \(d\ge a+1\), one has \(c_d=c_\infty\): indeed
\[
rg_d=\frac r{p+1}+\frac r{(p+1)(p^d-1)},
\]
and the second term is smaller than \(1/(p+1)\). The fractional part of \(p^a/(p+1)\) is either \(1/(p+1)\) or \(p/(p+1)\), so no integer boundary is crossed. Consequently the tail \(\sum_{d\ge a+1}(p-1)p^{-d-1}=p^{-a-1}\) can be summed exactly. This proves the displayed **finite rational formula**.

**6. High-column-depth limit and error.** Replace each \(c_d\) in the infinite expression by \(rg_d\). Since \(0\le rg_d-c_d<1\), its change in the density has absolute value at most
\[
\frac1r\sum_{d\ge1}\frac{p-1}{p^{d+1}}=\frac1{pr}=p^{-a-1}.
\]
The resulting expression simplifies by a geometric cancellation:
\[
\sum_{d\ge1}\frac{p-1}{p^{d+1}}\,(2-2g_d)
=\frac2p-\frac{2(p-1)}{p(p+1)}\sum_{d\ge1}\frac1{p^d-1}.
\]
The series converges absolutely since \(1/(p^d-1)=O(p^{-d})\). This proves the claimed limiting law and its error. Moreover, \(0<\delta_{p,a}<1\), since each of the positive and negative sign conditions occurs on a set of lags of positive density: for positive signs take \(t\equiv0\pmod p\) with \(\nu_p(t)=1\) and \(u=0\), and for negative signs take \(u=0\), \(t\equiv1\pmod p\) for odd \(p\), or \(t\equiv1\pmod2\) for \(p=2\).

## Verification

A standalone Python checker (`check.py`) uses exact rational arithmetic for all covariance and density comparisons. Its test suite independently computes actual integer binomial coefficients at 2,992 indices; verifies the sign characterization and absence of zero covariances in 68,988 parameter-lag cases; checks finite positive-lag frequencies against their exact natural densities; and compares 569,978 finite-depth cyclic valuation-pair moment tuples with the analytic covariance. All checks pass. These finite checks corroborate but do **not** establish the infinite theorems; Steps 1–6 above supply the proofs. Run with `python3 check.py`; no third-party modules or external data are required.

## Relationship to prior work

Kummer's classical theorem supplies the prime-power binomial reduction. Dillon Snyder, *Products of \(p\)-Adic Valuation Trees* (first publicly posted 2023-08-22), develops linear and product valuation trees, giving the relevant general mathematical framework. Spiegelhofer and Wallner (2016) develop generating functions for **within-row** prime-power divisibility counts, rather than autocovariances along a fixed column. Existing general joint-valuation/root-collision methods cover the local two-point moment in Step 3, which is **not claimed as new**. The asserted distinction is the exact **arithmetic density of lags with positive covariance**, its finite depth formula, and the Lambert-series high-depth limit with an explicit error bound. Literature searches did not identify these conclusions, but a nonindexed or unstated prior derivation remains possible.

## Limitations

The source comparison is not an exhaustive proof of priority. Stronger general digital-correlation formulas, if discovered, might imply the result; the original 2001 Barat–Grabner paper was not inspected in full. The limit uses index Cesàro averaging, then separate lag counting, and must not be mistaken for the covariance of a finite random sample without boundary corrections. No result is asserted for varying primes jointly, or arbitrary fixed lower binomial indices.

## References

- E. E. Kummer, prime-power divisibility and base-prime carry theorem (1852), used in the standard form for binomial coefficients.
- Dillon Snyder, *Products of \(p\)-Adic Valuation Trees*, arXiv:2308.11718, first posted 2023-08-22. https://arxiv.org/abs/2308.11718
- Lukas Spiegelhofer and Michael Wallner, *An explicit generating function arising in counting binomial coefficients divisible by powers of primes*, arXiv:1604.07089, first posted 2016-04-24. https://arxiv.org/abs/1604.07089
- V. Barat and P. J. Grabner, *Distribution of binomial coefficients and digital functions*, Journal of the London Mathematical Society 64 (2001), DOI 10.1112/S0024610701002630. https://doi.org/10.1112/S0024610701002630
