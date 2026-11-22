# A birthday-scale Poisson law and an energy threshold for sparse histogram evidence

## Finding

Consider the histogram likelihood-ratio statistic associated with a symmetric Dirichlet prior of one pseudo-count in each cell. Let \(Z_1,\ldots,Z_n\) be independent observations from a **fixed, bounded, continuous** probability density \(f\) on \([0,1]^2\). For integer \(d=d_n\ge2\), divide the square into \(K=d^2\) equal cells, with counts \(B_1,\ldots,B_K\), and define
\[
M_{n,d}=\frac{K^n\,(K-1)!}{(K+n-1)!}\prod_{j=1}^K B_j!,\qquad
\lambda_n=\frac{n(n-1)}{2K},\qquad
J(f)=\int_{[0,1]^2}f(u,v)^2\,du\,dv.
\]
The density \(f\) is nonnegative, integrates to one, and need not have uniform marginals for the general theorem. Assume throughout that \(d_n^2/n\to\infty\), equivalently \(n/K\to0\). Then the following are the **complete non-boundary sparse-grid limits**:

1. If \(\lambda_n\to0\), then \(M_{n,d_n}\to1\) in probability.
2. If \(\lambda_n\to\tau\in(0,\infty)\), then
\[
M_{n,d_n}\ \Rightarrow\ e^{-\tau}2^Z,\qquad Z\sim\operatorname{Poisson}(\tau J(f)).
\]
Thus, for every \(t>0\) outside the countable support \(\{e^{-\tau}2^k:k\ge0\}\), the exceedance probability converges to \(\Pr\{e^{-\tau}2^Z>t\}\).
3. If \(\lambda_n\to\infty\), then
\[
\frac{\log M_{n,d_n}}{\lambda_n}\ \xrightarrow{\mathbb P}\ J(f)\log 2-1.
\]
In particular, \(M_{n,d_n}\to0\) in probability if \(J(f)<1/\log 2\), whereas \(M_{n,d_n}\to\infty\) in probability if \(J(f)>1/\log 2\). No conclusion about the unscaled statistic is asserted at equality.

Consequently, when \(d_n/n\to c\in(0,\infty)\), the critical Poisson parameter is \(\tau=1/(2c^2)\). If \(\sqrt n\ll d_n\ll n\), the energy cutoff \(1/\log2\) separates vanishing and exploding evidence even for fixed smooth alternatives.

A concrete, strictly positive, real-analytic copula family is
\[
f_a(u,v)=1+a\cos\{2\pi(u-v)\},\qquad 0<|a|<1.
\]
It has both marginals uniform, is nonindependent whenever \(a\ne0\), and has \(J(f_a)=1+a^2/2\). For independent observations drawn **directly from this copula** and \(\sqrt n\ll d_n\ll n\), the same histogram evidence converges to zero if \(0<|a|<a_*\) and diverges if \(a_*<|a|<1\), where
\[
a_*=\sqrt{2\left(\frac1{\log2}-1\right)}=0.9409516893963934\ldots.
\]
These alternatives are fixed, smooth, and bounded away from zero for each \(a\in(-1,1)\).

## Assumptions and scope

The observations in the theorem are independent identically distributed pairs drawn directly from \(f\). The calculation applies to the **uncorrected, randomized, fixed-grid** rank martingale of Henzi and Law (2023), equation (9), **under its independence null**, because their randomized sequential-rank pairs are then exactly independent uniform pairs by their Proposition 1(iii). For that application, \(f\equiv1\), hence \(J(f)=1\) and the growing-grid null limits above apply without any continuity assumption on the original observed marginals.

The non-null copula statements are for independent draws from the **oracle copula distribution**, not for the empirical *sequential ranks* under dependence; those ranks do not generally form an iid copula sample. No power or detection threshold for the actual sequential-rank test under those alternatives is claimed. Each sample size \(n\) may use a different fixed grid \(d_n\); this triangular array does **not** define a single anytime-valid test martingale obtained by changing the grid during observation.

## Proof

**Step 1 (deterministic likelihood-ratio identity).** Let \(p_{j,d}\) be the cell probabilities and let \(s_{r,d}=\sum_j p_{j,d}^r\). Since \(\max_j p_{j,d}\le\|f\|_\infty/K\) and equal-cell averages of a continuous density converge uniformly, the squared-mass relation is
\[
Ks_{2,d}=\frac1K\sum_{j=1}^K(Kp_{j,d})^2\longrightarrow J(f),\qquad
s_{r,d}=O_f(K^{1-r})\quad(r\ge2\ \text{fixed}).
\]
Set \(C_n=\sum_j\binom{B_j}{2}\), the number of equal-label pairs, and \(T_n=\sum_j\binom{B_j}{3}\). The exact identity is
\[
\log M_{n,d}=\sum_j\log(B_j!)-H_{n,K},\qquad
H_{n,K}=\sum_{i=0}^{n-1}\log(1+i/K).
\]
Under \(n/K\to0\), Taylor's inequality yields
\[
H_{n,K}=\lambda_n+O(n^3/K^2)=\lambda_n\{1+O(n/K)\}.
\]
For each integer \(b\ge0\), the terms with \(b=0,1,2\) satisfy \(\log(b!)=(\log2)\binom b2\). For \(b\ge3\), elementary factorial bounds imply
\[
\left|\log(b!)-(\log2)\binom b2\right|
\le3(1+\log2)\binom b3.
\]
Therefore
\[
\left|\log M_{n,d}-\{(\log2)C_n-\lambda_n\}\right|
\le3(1+\log2)T_n+O(n^3/K^2).
\tag{1}
\]
As \(\mathbb E T_n=\binom n3s_{3,d}=O_f(n^3/K^2)=O_f(\lambda_n n/K)\), the right side is \(o_{\mathbb P}(\lambda_n)\) when \(\lambda_n\to\infty\), and \(o_{\mathbb P}(1)\) when \(\lambda_n\) remains bounded.

**Step 2 (collision law at the critical scale).** If \(\lambda_n\to\tau\in(0,\infty)\), write \(C_n=\sum_{1\le i<j\le n}\mathbf1\{Z_i,Z_j\text{ fall in the same cell}\}\). In its fixed factorial moment of order \(r\), ordered collections of \(r\) distinct pairs correspond to finite simple graphs with \(v\) vertices and \(c\) connected components. For a connected component involving \(h\) vertices, the event that all its observations share a cell has probability \(s_{h,d}=O(K^{1-h})\). Thus a graph type contributes \(O(n^v/K^{v-c})=O(n^{2c-v})\). All graph types containing a component with at least three vertices vanish because \(v\ge2c+1\). The disjoint-pair graphs contribute
\[
\frac{(n)_{2r}}{2^r}s_{2,d}^{\,r}\longrightarrow\{\tau J(f)\}^{r}.
\]
Hence every fixed factorial moment converges to that of \(\operatorname{Poisson}(\tau J(f))\), proving \(C_n\Rightarrow Z\). Combine this with (1), the continuous mapping theorem, and exponential continuity to obtain the critical law. If \(\lambda_n\to0\), \(\mathbb E C_n=\lambda_n K s_{2,d}=O_f(\lambda_n)\to0\), so \(C_n=0\) with probability tending to one, and (1) shows \(M_{n,d}\to1\).

**Step 3 (many collisions at low mean occupancy).** In general,
\[
\mathbb E C_n=\binom n2s_{2,d}=\lambda_n(Ks_{2,d}),
\]
\[
\operatorname{Var}(C_n)=\binom n2(s_{2,d}-s_{2,d}^2)+6\binom n3(s_{3,d}-s_{2,d}^2).
\]
Disjoint pair indicators are independent; overlapping pair indicators have joint probability \(s_{3,d}\), which gives this exact variance. For \(\lambda_n\to\infty\) and \(n/K\to0\), this variance is \(O_f(\lambda_n+n^3/K^2)=o(\lambda_n^2)\). As \(Ks_{2,d}\to J(f)\), Chebyshev's inequality gives \(C_n/\lambda_n\to J(f)\) in probability. Divide (1) by \(\lambda_n\) to obtain the claimed logarithmic limit.

**Step 4 (analytic copula example).** The cosine term integrates to zero along either coordinate, establishing both uniform marginals. Orthogonality gives \(\int_{[0,1]^2}\cos^2\{2\pi(u-v)\}\,du\,dv=1/2\), hence \(J(f_a)=1+a^2/2\). This crosses \(1/\log2\) once on \(0<a<1\), at the stated \(a_*\). More explicitly, the exact cell probabilities are
\[
p_{ij,d}=d^{-2}+a\left\{\frac{\sin(\pi/d)}{\pi}\right\}^2
\cos\left\{\frac{2\pi(i-j)}d\right\},\quad 0\le i,j<d.
\]
For \(d\ge3\), this gives the exact finite-grid value
\[
Ks_{2,d}=1+\frac{a^2}{2}\left\{\frac{d\sin(\pi/d)}\pi\right\}^4,
\]
which converges to \(1+a^2/2\).

## Verification

The standalone Python checker `checker.py` uses only the standard library. It exactly enumerates short categorical sequences and verifies the predictive-versus-factorial identity and the unit-null-expectation identity using rational arithmetic. It independently checks the exact nonuniform pair-collision variance, the triple-collision error bound, and the cosine copula's exact finite-grid \(L^2\) mass. Seeded simulation at sample size \(n=450\), \(d=450\) checks the predicted critical collision intensity and logarithmic evidence approximation for three analytic-copula parameters. On the reviewed run it completed **2,011 assertions**. This numerical evidence supplements, but does not replace, the all-size arguments above.

## Relationship to prior work

Henzi and Law introduced the **exact** statistic \(M_{n,d}\) and its sequential rank construction; these are not claimed as new. Their analysis emphasizes fixed discretizations, power bounds, and mixtures of grids, rather than a square-grid birthday scaling with dimension proportional to sample size. The classical birthday-collision Poisson law is prior knowledge (including Arratia, Garibaldi and Kilian, 2016). Symmetric Dirichlet-multinomial marginal likelihood and the Bayesian birthday problem are also established. The present claim concerns the synthesis of the **statistic's three sparse-grid evidence limits**, the nonuniform intensity \(\tau J(f)\), and the sharp smooth-copula energy threshold \(J(f)=1/\log2\).

## Limitations

The boundary \(J(f)=1/\log2\) is not classified at the unscaled level. The many-collision theorem requires \(n/d_n^2\to0\), and says nothing about dense occupancy grids. The critical law concerns the terminal statistic, not the running maximum or stopping time. The non-null result only applies to iid input pairs drawn directly from a density and is **not** asserted for dependent sequential empirical ranks or corrected/derandomized variants of the published test. Claims of literature priority remain subject to further independent review.

## References

- A. Henzi and M. Law, *A Rank-Based Sequential Test of Independence*, preprint first public 23 May 2023, arXiv:2305.13818; published *Biometrika* 111 (2024), 1169–1186. https://arxiv.org/abs/2305.13818 ; https://doi.org/10.1093/biomet/asae023.
- R. Arratia, S. Garibaldi and J. Kilian, *Asymptotic distribution for the birthday problem with multiple coincidences, via an embedding of the collision process*, *Random Structures & Algorithms* 48 (2016), 480–502. https://doi.org/10.1002/rsa.20591.
- *Modelling Mixtures: the Dirichlet distribution*, Stanford Stats 366 course notes, discussion of Dirichlet birthday probabilities and uniform-simplex priors. https://web.stanford.edu/class/stats366/Mixt.html.
