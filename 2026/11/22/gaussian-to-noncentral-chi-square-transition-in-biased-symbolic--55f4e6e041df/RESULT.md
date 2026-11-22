# Gaussian-to-noncentral-chi-square transition in biased symbolic cylinder collisions

## Finding
Fix an integer \(k\ge1\). For each \(N\), let \(B_0,\ldots,B_{N+k-2}\) be independent binary digits with probability \(p_N\) of being one. Put \(W_i=(B_i,\ldots,B_{i+k-1})\), \(0\le i<N\), and count unordered repeated cylinders
\[
C_{N,k}=\sum_{0\le i<j<N}{\bf1}\{W_i=W_j\}.
\]
For every finite real \(\theta\), if \(p_N=1/2+\theta/\sqrt N\), then
\[
\frac{C_{N,k}-\binom N2 2^{-k}}N\ \Longrightarrow\
\frac{1}{2^{k+1}}\left[k\big((Z-2\theta)^2-1\big)
+\sum_{d=1}^{k-1}(k-d)\big(Q_d-2^{d-1}\big)\right], \tag{1}
\]
where \(Z\) is standard normal, \(Q_d\sim\chi^2_{2^{d-1}}\), and all these variables are independent. Thus local bias acts on exactly **one** mode, producing the noncentrality \(4\theta^2\). The limiting mean and variance in (1) are respectively
\[
\frac{k\theta^2}{2^{k-1}},\qquad
\frac{3\cdot2^k-3-2k+8k^2\theta^2}{2^{2k+1}}.\tag{2}
\]
For each *fixed* \(p\in(0,1)\setminus\{1/2\}\), let \(A=p^2+(1-p)^2\), \(B=p^3+(1-p)^3\), and
\[
V_{k,p}=B^k-A^{2k}+2\sum_{h=1}^{k-1}\big(A^{2h}B^{k-h}-A^{2k}\big).
\]
Then \(V_{k,p}>0\), and
\[
\frac{C_{N,k}-\mathbb E_pC_{N,k}}{N^{3/2}}\Longrightarrow \mathcal N(0,V_{k,p}).\tag{3}
\]
More sharply, if \(\delta_N=p_N-1/2\to0\) and \(\sqrt N|\delta_N|\to\infty\), then
\[
\frac{C_{N,k}-\mathbb E_{p_N}C_{N,k}}{N^{3/2}|\delta_N|}
\Longrightarrow\mathcal N\left(0,\frac{k^2}{2^{2k-2}}\right).\tag{4}
\]
Equations (1), (3) and (4) characterize the fixed-resolution fluctuation transition from degenerate first-order statistics to Gaussian fluctuations, with the sharp window \(|p_N-1/2|\asymp N^{-1/2}\).

## Assumptions and scope
The block length \(k\) is a fixed positive integer, and the limit \(N\to\infty\) is taken through experiments with independent digits of the same bias within each experiment. Overlapping observation windows are **not** made independent. In (1) a fixed \(\theta\) is allowed only for \(N\) large enough that \(0<p_N<1\). No varying-\(k\) assertion is made. In (3) the centering is the exact finite-sample expectation, including overlapping pairs; in (1) it is the exactly known fair-input expectation.

## Proof
For nonempty \(S\subseteq\{0,\ldots,k-1\}\), define a Walsh character and its sliding sum by
\[
\chi_S(W_i)=(-1)^{\sum_{r\in S}B_{i+r}},\qquad H_{N,S}=\sum_{i=0}^{N-1}\chi_S(W_i).
\]
Fourier orthogonality on the Boolean cube gives the **pointwise identity**, without a probabilistic assumption,
\[
C_{N,k}=\frac{N^2}{2^{k+1}}-\frac N2+
\frac1{2^{k+1}}\sum_{\varnothing\ne S\subseteq[k]}H_{N,S}^2.\tag{5}
\]
At fair bias, two overlapping length-\(k\) words match with probability exactly \(2^{-k}\): for separation \(h<k\), the equality enforces the same letter along each of the \(h\) residue chains and imposes exactly \(k\) independent binary constraints. The disjoint case is immediate. Hence \(\mathbb E_{1/2}C_{N,k}=\binom N2 2^{-k}\), and (5) yields
\[
\frac{C_{N,k}-\binom N2 2^{-k}}N
=2^{-k-1}\left(\sum_{S\ne\varnothing}(H_{N,S}/\sqrt N)^2-(2^k-1)\right).\tag{6}
\]
Each nonempty support has a unique anchored pattern obtained by subtracting its minimum. An anchored pattern of span \(d=0\) has \(k\) placements; each anchored pattern with span \(1\le d<k\) has \(k-d\) placements. There are precisely \(2^{d-1}\) anchored patterns of span \(d\ge1\). Sliding sums at different placements of the *same* anchored pattern differ by a bounded number of terms (at most \(2k\) times a unit bound), so have identical \(\sqrt N\)-limits. For two distinct anchored patterns, the fair-bias covariance summed over all time offsets is zero, because at least one coordinate appears to an odd power in the product of Walsh characters; for a pattern paired with itself the sum equals one. These facts also follow by direct finite enumeration in `checker.py`.

Under \(p_N=1/2+\theta/\sqrt N\), the mean of \(\chi_S\) is \((-2\theta/\sqrt N)^{|S|}\). Consequently \(\mathbb E(H_{N,S}/\sqrt N)\to-2\theta\) exactly for singleton supports, and tends to zero otherwise. The limiting long-run covariance is the preceding fair-bias covariance by continuity in \(p\). The bounded, uniformly \((k-1)\)-dependent triangular array obeys a multivariate central limit theorem, using blocking into independent groups separated by \(k\) omitted coordinates and then a vanishing-block-fraction argument. Therefore the anchored-pattern sums converge jointly to independent standard normals, except for the unique singleton pattern whose Gaussian mean is \(-2\theta\). Substitute in (6) to obtain (1). There is one singleton pattern with coefficient \(k\), and \(2^{d-1}\) span-\(d\) patterns, proving the asserted \(\chi^2\) multiplicities. The elementary finite sum \(k^2+\sum_{d=1}^{k-1}(k-d)^2 2^{d-1}=3\cdot2^k-3-2k\) gives (2) by fourth moments of independent Gaussians. Uniform boundedness of higher normalized moments under finite dependence supplies uniform integrability of fourth powers, validating the limiting variance.

For fixed \(p\ne1/2\), write \(\pi_w=\prod_{r=0}^{k-1}p^{w_r}(1-p)^{1-w_r}\) and \(M_w=\#\{i:W_i=w\}\). Since \(C_{N,k}=\frac12(\sum_w M_w^2-N)\), the centered leading term at scale \(N^{3/2}\) is
\[
\frac1{\sqrt N}\sum_{i=0}^{N-1}\big(\pi_{W_i}-\mathbb E_p\pi_{W_i}\big).
\]
The remaining centered quadratic-histogram term is \(O_p(N)\), since the fixed-dimensional vector \((M_w-N\pi_w)_w\) has fluctuations of order \(\sqrt N\). The summands in the leading term are bounded and \((k-1)\)-dependent. Their mean is \(A^k\), variance \(B^k-A^{2k}\), and their lag-\(h\) covariance for \(1\le h<k\) equals \(A^{2h}B^{k-h}-A^{2k}\); greater lags have covariance zero. The \(m\)-dependent CLT yields (3). Positivity follows because the singleton Walsh projection of the score has nonzero coefficient whenever \(p\ne1/2\); equivalently the disjoint-block conditional variance is positive.

Finally, for \(\delta_N\to0\), the centered score's singleton contribution has coefficient \(-\delta_N\,k/2^{k-1}+O(\delta_N^2)\), while its higher Walsh degrees have coefficients \(O(\delta_N^2)\). The first-order term is a scalar multiple of the centered digit sum. The centered remainder of the quadratic-histogram term is \(O_p(N)\), and its own linear projection has order \(O_p(N^{3/2}\delta_N^2)\); dividing by \(N^{3/2}|\delta_N|\) makes both vanish because \(\sqrt N|\delta_N|\to\infty\) and \(\delta_N\to0\). The ordinary Bernoulli triangular-array CLT for the digit sum proves (4). This also confirms that (3)'s Gaussian variance degenerates quadratically as \(p\to1/2\), with the coefficient in (4).

## Verification
Run `python checker.py` from the extracted artifact directory. The standard-library checker independently enumerates 1,860 binary words to verify (5), checks the fair collision expectation in 20 separate cases, evaluates 284 exact pairwise Walsh long-run covariances directly by summing all possible overlapping input strings, and verifies the formula for \(V_{k,p}\) against independent exhaustive probabilities for eight biased cases. Its recorded output is in `check_results.txt`. The computations are finite spot checks; infinite limits rely on the proof.

## Relationship to prior work
The published result *Exact non-Gaussian fixed-cylinder pair-collision law for full shifts* (2026) proves the central weighted \(\chi^2\) law at **exactly uniform independent digits**. Formula (1) reduces to that result at \(\theta=0\), a known special case, but the sharply tuned noncentral limit and the asymptotic matching to the Gaussian phase in (3)–(4) require a varying input law. Baker–Todd (2026) study almost-sure pair-correlation statistics at shrinking **interval metric** scales, rather than fixed-length symbolic-cylinder fluctuations under contiguous changes in Bernoulli bias. Schnurr–Silbernagel–Ruiz Marín (2024) develop short-range-dependent ordinal-pattern correlation-integral limits using classical \(U\)-statistics; their ordinal patterns and fixed-law inference differ from the literal binary-block local-alternative spectrum here. Classical finite-range CLTs, multinomial local-alternative theory, and the uniform result provide significant ingredients: the evaluated critical-window crossover is the contribution asserted here, not a new CLT methodology.

## Limitations
The bias is homogeneous within each experiment, the alphabet is binary, the cylinder length is fixed, and the coordinates are independent. The result does not extend as stated to varying block length, dependent processes, nonstationary coordinates, or geometric metric shrinking. The full Baker–Todd preprint and the detailed manuscript for the uniform result were compared as far as accessible; the former's full text was inaccessible via attempted public routes, so undiscovered equivalent priority remains possible. A classical general local-alternative theorem might imply the noncentral limit abstractly, although it does not by itself provide the explicit sliding-pattern multiplicities or the matching scale law recorded here.

## References
- S. Baker and M. Todd, *Pair correlation statistics for dynamical systems*, arXiv:2606.17880, first public 2026-06-16. https://arxiv.org/abs/2606.17880
- *Exact non-Gaussian fixed-cylinder pair-collision law for full shifts*, publicly available mathematical result (2026). https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-exact-non-gaussian-fixed-cylinder-pair-collision-law-for-full-sh--0ded5372fff8/RESULT.md
- A. Schnurr, A. Silbernagel, and M. Ruiz Marín, *Limit Theorems for the Symbolic Correlation Integral and the Renyi-2 Entropy under Short-range Dependence*, arXiv:2410.18726, first public 2024-10-24. https://arxiv.org/abs/2410.18726
