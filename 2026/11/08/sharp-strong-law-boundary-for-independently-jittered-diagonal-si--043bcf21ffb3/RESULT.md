# Sharp strong-law boundary for independently jittered diagonal-singular quadrature

## Finding

The strong law for a fresh one-point-per-square sampling of a diagonal power-log singularity has an exact integrability boundary. For \(0<\alpha<1\), \(\beta\in\mathbb R\), let
\[
f_{\alpha,\beta}(x,y)=|x-y|^{-\alpha}\bigl[\log(e/|x-y|)\bigr]^{-\beta}.
\]
For each integer \(n\ge1\), divide the unit square into \(n^2\) equal square cells, take one independent uniform draw per cell, redraw the entire array independently across different \(n\), and define \(Q_n\) as the average of the \(n^2\) function values. Let
\[
I_{\alpha,\beta}=2\int_0^1(1-t)t^{-\alpha}[\log(e/t)]^{-\beta}\,dt.
\]
Then \(Q_n\to I_{\alpha,\beta}\) in probability for all parameters. Moreover,
\[
Q_n\longrightarrow I_{\alpha,\beta}\quad\text{almost surely}
\quad\Longleftrightarrow\quad
\alpha<\frac23\ \text{or}\ \left(\alpha=\frac23,\ \beta>\frac23\right).
\]
Equivalently, the strong law holds in this family precisely when \(f_{\alpha,\beta}\in L^{3/2}([0,1]^2)\). Otherwise,
\[
\liminf_{n\to\infty}Q_n=I_{\alpha,\beta},\qquad
\limsup_{n\to\infty}Q_n=+\infty\qquad\text{almost surely}.
\]
The two strict statements are simultaneous on one probability-one event. In particular, the logarithmic endpoint \(\alpha=2/3\) is included, with a sharp strict condition on \(\beta\).

## Assumptions and scope

Let the cells be \(C_{ij}= [i/n,(i+1)/n]\times[j/n,(j+1)/n]\), \(0\le i,j<n\). In each cell choose \((X_{ij}^{(n)},Y_{ij}^{(n)})\) uniformly, independently for different cells and different sample sizes. Let \(Q_n=n^{-2}\sum_{i,j=0}^{n-1} f_{\alpha,\beta}(X_{ij}^{(n)},Y_{ij}^{(n)})\). The integrand may be assigned any finite value on the measure-zero diagonal; this changes no statement. All logarithms are natural. Parameter \(\beta\) can be any real number. The overall integration dimension is two, and the singular set is a line, not a boundary or isolated point.

## Proof

**1. Split the grid into a small singular band and its complement.** Write \(Q_n=B_n+D_n\), where \(B_n\) collects \(|i-j|\le1\) and \(D_n\) collects \(|i-j|\ge2\), including the weights \(n^{-2}\). For diagonal cells, the distance to the diagonal is \(T/n\) with \(T=|U-V|\) for independent uniform \(U,V\in(0,1)\), whose density is \(2(1-t)\) for \(0<t<1\). The adjacent-cell distance is \((1+U-V)/n\), whose density vanishes linearly at zero. Thus every singular-band variable has the form \(n^\alpha Z_n\), with \(Z_n=t^{-\alpha}[\log(en/t)]^{-\beta}\) for a gap variable with a density bounded near zero (diagonal) or vanishing at zero (adjacent). Since \(\alpha<1\), direct integration gives
\[
0\le\mathbb E B_n\le C_{\alpha,\beta}\,n^{\alpha-1}(1+\log n)^{|\beta|}\longrightarrow0.
\]
Unbiasedness holds for each \(n\) because a uniform draw over each cell represents that cell's integral; hence \(\mathbb E D_n=I_{\alpha,\beta}-\mathbb E B_n\to I_{\alpha,\beta}\).

**2. The complement converges almost surely without moment restrictions on the full integrand.** On a cell with \(|i-j|=k\ge2\), its distance to the diagonal is at least \((k-1)/n\). Using \(\log(e/t)\ge1\) and \(\log(e/t)\le1+\log n\) on this region, we have the deterministic bound
\[
|f_{\alpha,\beta}(X_{ij}^{(n)},Y_{ij}^{(n)})|
\le C n^\alpha(k-1)^{-\alpha}(1+\log n)^{|\beta|}.
\]
Independence of the cell draws therefore yields
\[
\operatorname{Var}(D_n)\le C n^{2\alpha-3}(1+\log n)^{2|\beta|}
\sum_{k=1}^{n}k^{-2\alpha}.
\]
The sum of these variance bounds over all \(n\) is finite: for \(\alpha<1/2\) the bound is \(O(n^{-2}(\log n)^{2|\beta|})\), for \(\alpha=1/2\) it has an additional logarithm, and for \(\alpha>1/2\) it is \(O(n^{2\alpha-3}(\log n)^{2|\beta|})\), whose exponent is strictly less than \(-1\). Chebyshev and the first Borel–Cantelli lemma give \(D_n-\mathbb E D_n\to0\) almost surely. Hence \(D_n\to I_{\alpha,\beta}\) almost surely for **every** permitted parameter pair. Markov's inequality and the expectation estimate in Step 1 also imply \(B_n\to0\) in probability, so \(Q_n\to I_{\alpha,\beta}\) in probability for every pair.

**3. Below the critical power the band also converges almost surely.** If \(\alpha<2/3\), choose \(p\) with
\[
\frac{2}{2-\alpha}<p<\min\left\{2,\frac1\alpha\right\}.
\]
Such a \(p>1\) exists exactly because \(\alpha<2/3\). From the triangular gap densities and \(\alpha p<1\), each unscaled near-band variable \(Z_n\) satisfies \(\mathbb E|Z_n|^p\le C(1+\log n)^{p|\beta|}\). Apply the von Bahr–Esseen inequality to the at most \(3n\) independent centered band variables (it applies for \(1\le p\le2\)) and use their total expectation from Step 1. For any \(\varepsilon>0\),
\[
\Pr\bigl(|B_n-\mathbb E B_n|>\varepsilon\bigr)
\le C_\varepsilon n^{1-p(2-\alpha)}(1+\log n)^{p|\beta|}.
\]
This is summable since \(p(2-\alpha)>2\). First Borel–Cantelli shows \(B_n\to0\) almost surely.

**4. The logarithmic critical endpoint.** Put \(\alpha=2/3\) and suppose \(\beta>2/3\). The adjacent cells contribute an independent sub-sum \(B_n^{\mathrm{adj}}\). Their gap density vanishes linearly at zero, so their second moments are bounded by \(Cn^{4/3}(1+\log n)^{2|\beta|}\). Summing at most \(2n\) independent cells and dividing by \(n^4\) gives \(\sum_n\operatorname{Var}(B_n^{\mathrm{adj}})<\infty\). Its expectation tends to zero by Step 1, so \(B_n^{\mathrm{adj}}\to0\) almost surely.

The \(n\) diagonal cells have independent contributions
\[
W_{n,j}=n^{2/3}T_{n,j}^{-2/3}[\log(en/T_{n,j})]^{-\beta},
\qquad 0<T_{n,j}<1,
\]
with triangular gap density \(2(1-t)\). Fix any \(c>0\), and let \(s_n\) solve \(n^{2/3}s_n^{-2/3}[\log(en/s_n)]^{-\beta}=cn^2\). The function on the left is decreasing in \(s_n\) for all sufficiently large \(n\). Taking logarithms yields
\[
s_n\sim c^{-3/2}3^{-3\beta/2}\,n^{-2}(\log n)^{-3\beta/2}.
\]
In particular \(s_n\asymp n^{-2}(\log n)^{-3\beta/2}\), and
\[
\Pr\left(\max_{1\le j\le n}W_{n,j}>cn^2\right)
\le 2ns_n\le\frac C{n(\log n)^{3\beta/2}}.
\]
After truncation at \(cn^2\), the same density and \(\log(en/t)\ge\log n\) give
\[
\mathbb E\left[W_{n,j}^2\mathbf1_{\{W_{n,j}\le cn^2\}}\right]
\le Cn^{4/3}(\log n)^{-2\beta}
\int_{s_n}^{1}t^{-4/3}\,dt
\le Cn^2(\log n)^{-3\beta/2}.
\]
The expectation of the whole untruncated diagonal sum is \(o(n^2)\). Union bound for large entries and Chebyshev for the independent truncated centered entries now yield
\[
\Pr\left(n^{-2}\sum_{j=1}^nW_{n,j}>\varepsilon\right)
\le \frac{C_\varepsilon}{n(\log n)^{3\beta/2}}
\]
for all large \(n\). The right-hand side is summable exactly when \(\beta>2/3\). First Borel–Cantelli proves the critical strong law.

**5. Sharp failure, infinite upper limsup, and exact lower liminf.** Fix \(c>0\). For any \(\alpha,\beta\) in the claimed failure region, the equation
\[
n^\alpha s_n^{-\alpha}[\log(en/s_n)]^{-\beta}=cn^2
\]
has a small positive solution with
\[
s_n\sim c^{-1/\alpha}(2/\alpha)^{-\beta/\alpha}
 n^{1-2/\alpha}(\log n)^{-\beta/\alpha}.
\]
Thus the probability that at least one of the \(n\) independent diagonal cells alone makes \(Q_n>c\) is
\[
1-\bigl(1-(2s_n-s_n^2)\bigr)^n
\sim 2c^{-1/\alpha}(2/\alpha)^{-\beta/\alpha}
 n^{2-2/\alpha}(\log n)^{-\beta/\alpha}.
\]
These probabilities have divergent series if and only if \(\alpha>2/3\), or \(\alpha=2/3\) and \(\beta\le2/3\). The events for different \(n\) are independent by the **whole-array redraw assumption**. Second Borel–Cantelli, applied at all positive integer thresholds \(c\), gives \(\limsup_n Q_n=+\infty\) almost surely. On the other hand, \(Q_n\ge D_n\to I_{\alpha,\beta}\) almost surely, and \(\sum_{k\ge1}\mathbb E B_{2^k}<\infty\) by Step 1. First Borel–Cantelli implies \(B_{2^k}\to0\) almost surely, so \(\liminf_nQ_n=I_{\alpha,\beta}\) almost surely.

**6. The integrability formulation.** A unit-square diagonal strip of transverse width \(dt\) has area density \(2(1-t)\,dt\). Consequently, \(f_{\alpha,\beta}\in L^{3/2}\) exactly when \(\int_0^1t^{-3\alpha/2}[\log(e/t)]^{-3\beta/2}\,dt\) is finite, giving precisely the same strict threshold. This completes the proof.

## Verification

The standalone `checker.py` tests exact power-only cell moments and their unbiased decomposition, the exact triangular gap tail, algebraic threshold exponents, and numerically stable logarithmic tail-root asymptotics at critical and off-critical parameters. It has no reliance on random simulations. Reproduction: `python checker.py` with the Python standard library. Finite checks serve as diagnostics; the proof of the almost-sure statements is Steps 1–6, not finite sampling or numerical evidence.

## Relationship to prior work

Owen and Rudolf, *A strong law of large numbers for scrambled net integration* (first version 2020-02-18), prove strong laws for a **nested scrambled digital-net** integration procedure under \(L^p\), \(p>1\), assumptions; this sampling law and its dependence across sample sizes differ from the independently redrawn square-grid stratifications here. Basu and Owen, *Quasi-Monte Carlo for an Integrand with a Singularity along a Diagonal in the Square* (first version 2016-09-23), study exactly the motivating geometric singularity but analyze triangular truncation, extensions, and coordinate transforms, not this square-cell strong-law threshold. Pruss, *Randomly sampled Riemann sums and complete convergence in the law of large numbers for a case without identical distribution* (1996), establishes a sharp \(L^2\) threshold for **one-dimensional** equal-length stratification, whereas the current proof uses a two-dimensional grid, a line singularity, and a critical logarithmic border. Grahl's thesis on random Riemann sums discusses one-dimensional independently stratified convergence, including higher-moment sufficient conditions. The present \(L^{3/2}\) equivalence and especially the critical logarithmic threshold do not follow from those cited statements without a new geometric and probability-tail argument.

## Limitations

The theorem is for this explicit power-log family, not for every \(L^1\) integrand or every \(L^{3/2}\) integrand. Exact independence of the entire sequence of sampling grids is essential to the converse; nested or shared-randomness grids could behave differently. The infinite-excursion assertion is asymptotic and does not quantify realistic finite-precision hazards or exact crossover probabilities at modest \(n\). Related stronger convergence theorems under other terminology or inaccessible historical literature may affect publication priority. No independent audit has yet been performed.

## References

1. A. B. Owen and D. Rudolf, *A strong law of large numbers for scrambled net integration*, arXiv:2002.07859, first public 2020-02-18, https://arxiv.org/html/2002.07859v3.
2. K. Basu and A. B. Owen, *Quasi-Monte Carlo for an Integrand with a Singularity along a Diagonal in the Square*, arXiv:1609.07444, first public 2016-09-23, https://arxiv.org/html/1609.07444v3.
3. A. Pruss, *Randomly sampled Riemann sums and complete convergence in the law of large numbers for a case without identical distribution*, Proceedings of the AMS 124 (1996), 919–929, DOI:10.1090/S0002-9939-96-03100-0.
4. J. Grahl, *Exceptional Lebesgue densities and random Riemann sums*, doctoral thesis, University College London (2011/2012), https://discovery.ucl.ac.uk/id/eprint/1346450/1/1346450.pdf.
5. B. von Bahr and C.-G. Esseen, *Inequalities for the rth absolute moment of a sum of random variables*, The Annals of Mathematical Statistics 36 (1965), 299–303.
