# Hypergeometric short excursions and a Rayleigh–Gaussian two-scale limit for random-walk bridges

## Finding

Let \(S\) be a simple symmetric nearest-neighbor walk with \(S_0=S_{2n}=0\), sampled uniformly from all length-\(2n\) bridges. Write \(K_n\) for the number of complete excursions between successive visits to zero, and \(J_n\) for the number of excursions of length exactly two. For every integer \(n\ge2\) and \(1\le k<n\),

\[
J_n\mid\{K_n=k\}\sim\operatorname{Hypergeom}(2n-k-1,k-1,n),
\]

where the parameters are population size, number marked and sample size. Explicitly, for every integer \(j\),

\[
\Pr(J_n=j\mid K_n=k)=\frac{\binom{k-1}{j}\binom{2(n-k)}{n-j}}{\binom{2n-k-1}{n}},
\]

with out-of-range binomial coefficients interpreted as zero. The exceptional case \(k=n\) has \(J_n=n\) almost surely (and also \(K_1=J_1=1\)). In particular, when \(1\le k<n\),

\[
\mathbb E[J_n\mid K_n=k]=\frac{n(k-1)}{2n-k-1},\quad
\operatorname{Var}(J_n\mid K_n=k)=\frac{2n(k-1)(n-k)(n-k-1)}{(2n-k-1)^2(2n-k-2)}.
\]

This finite-population identity leads to an unusual simultaneous two-scale limit. Let \(X\) have the Rayleigh distribution with density \(f_X(x)=\frac{x}{2}e^{-x^2/4}\) on \(x>0\), and let \(Z\sim N(0,1)\) be independent of \(X\). Then

\[
\left(\frac{K_n}{\sqrt n},\frac{J_n-K_n/2}{n^{1/4}}\right)
\ \xrightarrow{d}\ \left(X,\frac{\sqrt X}{2}Z\right).
\]

Consequently \(J_n/K_n\to1/2\) in probability, \(\operatorname{Corr}(K_n,J_n)\to1\), and the rate is

\[
\sqrt n\bigl(1-\operatorname{Corr}(K_n,J_n)\bigr)
\longrightarrow\frac{\sqrt\pi}{2(4-\pi)}.
\]

## Assumptions and scope

All paths have independent fair \(+1,-1\) increments before conditioning on \(S_{2n}=0\); after conditioning they are uniform among the \(\binom{2n}{n}\) bridges. Every excursion is a maximal zero-free segment between consecutive visits to zero; a length-two excursion is \(0,1,0\) or \(0,-1,0\). \(K_n\) counts the terminal return but not time zero. There are \(1\le K_n\le n\) excursions. Hypergeometric samples are drawn without replacement. Statements for \(k<n\) are separated from the degenerate \(k=n\) boundary because the former sample population would otherwise be smaller than the sample. The Gaussian mixture is convergence in distribution, not a pathwise identity or an independence claim for \(K_n,J_n\).

## Proof

**Exact conditional distribution.** Let \(C(z)=\sum_{m\ge0}\frac1{m+1}\binom{2m}{m}z^m\) be the Catalan series, satisfying \(C=1+zC^2\). An unsigned positive primitive excursion of half-length \(m\ge1\) has \(C_{m-1}\) shapes, while a signed primitive excursion has \(2C_{m-1}\) shapes. Thus its generating series is \(E(z)=2zC(z)=1-\sqrt{1-4z}\). Conditioning on exactly \(k\) excursions gives the bivariate coefficient

\[
\mathbb E[v^{J_n}\mid K_n=k]
=\frac{[z^n]\bigl(zC(z)+z(v-1)\bigr)^k}{[z^n](zC(z))^k},
\]

since each choice of signs supplies the same factor \(2^k\). For integers \(0\le r<k\), differentiate \(r\) times at \(v=1\), giving

\[
\mathbb E[(J_n)_{\underline r}\mid K_n=k]
=(k)_{\underline r}\frac{[z^{n-k}]C(z)^{k-r}}{[z^{n-k}]C(z)^k}.
\]

For \(n>k\), the standard Lagrange-inversion identity

\[
[z^m]C(z)^a=\frac{a}{2m+a}\binom{2m+a}{m}\quad(a\ge1)
\]

therefore reduces the ratio to

\[
\mathbb E[(J_n)_{\underline r}\mid K_n=k]
=\frac{(n)_{\underline r}(k-1)_{\underline r}}{(2n-k-1)_{\underline r}}.
\]

When \(r=k\) the left side vanishes, since at least one excursion must exceed two steps if \(n>k\), and the right side vanishes too. These are precisely all factorial moments of a hypergeometric variable with population \(2n-k-1\), marked count \(k-1\), and draw size \(n\). Finite support makes factorial moments determining. If \(n=k\), all excursions must have half-length one, hence \(J_n=k=n\). Standard hypergeometric mean and variance yield the stated conditional formulas.

**Marginal returns and Rayleigh limit.** The same decomposition and Catalan coefficient identity give

\[
\Pr(K_n=k)=\frac{2^k k}{(2n-k)\binom{2n}{n}}\binom{2n-k}{n-k}
=\frac{k}{2n-k}\prod_{i=0}^{k-1}\frac{2(n-i)}{2n-i}.
\]

For \(k=\lfloor x\sqrt n\rfloor\), uniformly with \(x\) in compact subsets of \((0,\infty)\), the logarithm of the product is \(-k(k-1)/(4n)+o(1)\). Therefore \(\sqrt n\Pr(K_n=k)\to (x/2)e^{-x^2/4}\). The product is at most \(\exp[-k(k-1)/(4n)]\), giving a summable Gaussian tail bound and tightness. The limiting density integrates to one. Thus \(K_n/\sqrt n\Rightarrow X\), with convergence of all fixed polynomial moments; in particular \(\mathbb EX=\sqrt\pi\) and \(\operatorname{Var}(X)=4-\pi\).

**Microscopic fluctuations.** For \(k\asymp\sqrt n\), the conditional hypergeometric law has marked population \(k-1\to\infty\), success fraction in the drawn \(n\) positions approaching \(1/2\), and finite-population correction approaching \(1/2\). Its variance is \(k/4+O(1)\) uniformly for \(k/\sqrt n\) in compact subsets of \((0,\infty)\). The elementary hypergeometric central limit theorem, obtained by Stirling expansion of the displayed exact mass function around its mean, yields

\[
\frac{J_n-\mathbb E(J_n\mid K_n=k)}{\sqrt{k}/2}\Rightarrow N(0,1)
\]

uniformly on such compact subsets. Moreover

\[
\mathbb E(J_n\mid K_n=k)-k/2
=\frac{k^2+k-2n}{2(2n-k-1)}=O(1)
\]

for \(k=O(\sqrt n)\). Conditioning on \(K_n\), integrating characteristic functions over compact sets, and using the preceding Rayleigh tails proves the joint two-scale convergence with an independent standard normal \(Z\). Since \(X>0\) almost surely, this also proves \(J_n/K_n\to1/2\).

**Correlation rate.** Write \(J_n=K_n/2+\delta_n(K_n)+\varepsilon_n\), where \(\varepsilon_n\) has conditional mean zero and \(\delta_n(k)=(k^2+k-2n)/(2(2n-k-1))\) for \(k<n\), with \(\delta_n(n)=n/2\). The exponential product tail makes \(\delta_n(K_n)\) bounded in every fixed \(L^p\) as \(n\to\infty\). The exact conditional variance and moment convergence yield \(\mathbb E\varepsilon_n^2/\sqrt n\to\sqrt\pi/4\), while \(\operatorname{Var}(K_n)/n\to4-\pi\). In the correlation identity, the \(\operatorname{Cov}(K_n,\delta_n(K_n))\) terms cancel at first relative order; the remaining leading departure from one equals \(2\mathbb E\varepsilon_n^2/\operatorname{Var}(K_n)\). Consequently the claimed constant follows.

## Verification

The standalone `verify_bridge.py` enumerates every balanced signed walk up to 18 steps, computes \((K_n,J_n)\) directly, and compares every conditional mass to the hypergeometric formula using exact rational arithmetic. It separately checks Catalan convolution coefficients, the marginal \(K_n\) mass and conditional factorial moments at larger finite sizes. The asymptotic proof is analytic; numerical checks do not substitute for the infinite-limit argument. The checks were rerun after extracting this script from the final ledger.

## Relationship to prior work

Csáki and Hu (2003) studied ranked random-walk excursion lengths and heights, without stating the conditional short-excursion hypergeometric law or the microscopic joint fluctuation scale. Lindell and Holst (2007), Proposition 3.1, give a general joint generating function for excursion counts in macroscopic length intervals; their formula and iid excursion decomposition are important antecedents, but their stated macroscopic bin regime and ranked-length limits do not identify the present shrinking-bin conditional law or the \(n^{1/4}\) Gaussian mixture. Serlet (2014), equation (6), gives the exact product-Catalan joint probability for ordered excursion lengths and studies bridges with \(K_n=o(\sqrt n)\), a different scaling regime. This exact joint-length formula is a genuine stronger *input* from which the finite hypergeometric identity can be recovered by a nontrivial sum, so priority for the finite law is qualified; the two-scale limit and correlation rate are the assessed conclusions. Cameron and McLeod (2016) investigate returns and hills of nonnegative Dyck paths, primarily as separate marginal statistics; their root-level hill statistic corresponds to the short components when conditioned on the number of returns, but the conditional law and tied-down-bridge mixed scaling are not among the inspected claims.

## Limitations

The finite conditional law uses a bridge with fair symmetric steps and a fixed exact terminal return. It does not assert analogous hypergeometric behavior for drifted walks, general increments, or other excursion lengths. The \(n^{1/4}\) fluctuations are of the short-excursion count **after subtracting one-half the realized return count**; centering by its unconditional mean instead gives a different, dominant \(\sqrt n\) scale. Both a general ordered-excursion formula (Serlet) and an excursion-count generating-function framework (Lindell–Holst) significantly overlap the combinatorial input; historical priority for the explicit reductions cannot be ruled out. There has been no independent audit.

## References

- Endre Csáki and Yueyun Hu, *Lengths and heights of random walk excursions*, Discrete Mathematics and Theoretical Computer Science AC (2003), 45–52, DOI: https://doi.org/10.46298/dmtcs.3337 (open text: https://dmtcs.episciences.org/en/articles/3337/download).
- Andreas Lindell and Lars Holst, *Distributions of the longest excursions in a tied down simple random walk and in a Brownian bridge*, Journal of Applied Probability **44** (2007), 1056–1067, DOI: https://doi.org/10.1239/jap/1197908824.
- Laurent Serlet, *Invariance principle for the random walk conditioned to have few zeros*, Séminaire de Probabilités XLVI (2014), 461–472, https://lmbp.uca.fr/~serlet/rwfew.pdf.
- Naiomi T. Cameron and Jillian E. McLeod, *Returns and hills on generalized Dyck paths*, Journal of Integer Sequences **19** (2016), Article 16.6.1, https://www2.math.ethz.ch/EMIS/journals/JIS/VOL19/McLeod/mcleod3.pdf.
- Jochen Voss, *Random walk bridges*, October 17, 2007, https://www.seehuhn.de/blog/6.html.
