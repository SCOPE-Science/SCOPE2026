# Gaussian logarithmic fluctuations of inverse-partner degrees at proportional rank

## Finding

Let \(\mathcal O_n\) be the semigroup of all weakly increasing total maps of the chain \([n]\) to itself. Two elements \(f,g\in\mathcal O_n\) are mutual semigroup inverses when \(fgf=f\) and \(gfg=g\). Let \(\nu(f)\) be the number of such inverse partners of \(f\). Fix \(0<\alpha<1\), put \(r_n=\lfloor\alpha n\rfloor\), and draw \(F_n\) uniformly among rank-\(r_n\) maps. Set
\[
Z\sim\operatorname{Geom}(\alpha),\quad
\Pr(Z=j)=\alpha(1-\alpha)^{j-1},\ j\ge1,
\quad \mu_\alpha=\mathbb E\log Z,
\]
\[
v_\alpha=\operatorname{Var}(\log Z)
-\frac{\operatorname{Cov}(Z,\log Z)^2}{\operatorname{Var}(Z)}.
\]
Then \(v_\alpha>0\) and
\[
\boxed{\frac{\log\nu(F_n)-(2r_n-1)\mu_\alpha}
{\sqrt{2r_n v_\alpha}}\ \xrightarrow{\ d\ }\ \mathcal N(0,1).}
\]
This is a central limit theorem for the **logarithm of the number of inverse partners of a uniform single map with prescribed proportional rank**, not the rank distribution of a uniformly chosen inverse pair. The degree factorization and all finite power moments used below were established previously; their rederivation is included solely to make the limit proof self-contained.

## Definitions and boundaries

The image rank is the number of distinct values of a full order-preserving map, and the inverse relation is semigroup inversion, not functional inversion. Both constraints \(fgf=f\) and \(gfg=g\) are required. The two independent rank-\(r\) parameters are the composition \((a_1,\dots,a_r)\) of kernel-block lengths (positive, sum \(n\)) and the ordered image \(1\le b_1<\cdots<b_r\le n\). The limit requires \(r_n\sim\alpha n\) with strictly interior fixed \(\alpha\); it does not claim fixed-rank, bounded-rank-defect, or growing-rank-at-the-boundary limits. Empty products are one, and the asymptotic is taken only once \(1\le r_n\le n\).

## Proof

**1. Degree product and independence of parameters (known input, recalled).** The inverse-transversal criterion says that the image of a partner \(g\) must choose one element of each kernel interval of \(f\), and the cuts between consecutive kernel intervals of \(g\) must lie between the corresponding consecutive image values of \(f\). These choices are independent. Hence the previously known exact identity is
\[
\nu(f)=\prod_{i=1}^r a_i\prod_{i=1}^{r-1}(b_{i+1}-b_i).
\tag{1}
\]
A uniform rank-\(r\) isotone map has independent uniform positive kernel-length composition and uniform size-\(r\) image subset. Consequently, \(\log\nu(F_n)\) is the sum of two independent log-product statistics.

**2. Conditional geometric-composition CLT.** Let \(p_n=r_n/n\to\alpha\), and let \(Z_1,\ldots,Z_r\) be i.i.d. positive geometric random variables with parameter \(p_n\). Conditional on \(\sum_i Z_i=n\), every positive composition of \(n\) into \(r\) parts is equiprobable, so these conditioned variables have exactly the kernel-length law.

For \(p\) in a compact subinterval of \((0,1)\), set
\[
\mu_p=\mathbb E_p\log Z,\quad
\beta_p=\frac{\operatorname{Cov}_p(Z,\log Z)}{\operatorname{Var}_p(Z)},\quad
W_p=\log Z-\mu_p-\beta_p(Z-1/p).
\]
Then \(\mathbb E_pW_p=0\), \(\operatorname{Cov}_p(W_p,Z)=0\), and
\[\operatorname{Var}_p(W_p)=v_p>0.\]
Indeed \(\log j\) is not affine in \(j\) on the positive integers, so the strict Cauchy–Schwarz inequality gives \(v_p>0\).

Condition on \(\sum Z_i=n=r/p_n\). Fourier inversion in the lattice sum gives the characteristic function of \(\sum W_{p_n}(Z_i)/\sqrt r\) under that condition as
\[
\frac{\int_{-\pi}^{\pi}\left[\mathbb E_{p_n}
 e^{\,i\theta(Z-1/p_n)+itW_{p_n}/\sqrt r}\right]^r\,d\theta}
{\int_{-\pi}^{\pi}\left[\mathbb E_{p_n}e^{i\theta(Z-1/p_n)}\right]^r\,d\theta}.
\tag{2}
\]
Uniform geometric tails give uniformly bounded moments of the polynomially growing centered log statistic, while the geometric lattice distribution has span one and characteristic-function modulus strictly below one outside any neighborhood of zero. Thus the parts of both integrals away from a shrinking \(O(r^{-1/2})\) central window are negligible. On \(\theta=x/\sqrt r\), the joint Taylor expansion has quadratic term
\(-\tfrac12[x^2\operatorname{Var}_p(Z)+t^2v_p]\): the mixed term vanishes by \(\operatorname{Cov}(W_p,Z)=0\). Local domination and Gaussian integration in \(x\) therefore make the ratio tend to \(e^{-t^2v_\alpha/2}\). On the conditioning event, \(\sum_i(Z_i-1/p_n)=0\), so the projection term in \(\sum W_{p_n}\) vanishes identically. This proves
\[
\frac{\sum_{i=1}^r\log Z_i-r\mu_{p_n}}{\sqrt{r v_{p_n}}}
\;\Bigm|\;\sum_iZ_i=n\ \Longrightarrow\ \mathcal N(0,1).
\tag{3}
\]
Since \(r_n=\lfloor\alpha n\rfloor\), the smooth dependence of geometric logarithmic moments on \(p\) gives \(r_n(\mu_{p_n}-\mu_\alpha)=O(1)\), and \(v_{p_n}\to v_\alpha\).

**3. Image-gap CLT and endpoint slacks.** For the uniformly selected image \(b_1<\cdots<b_r\), write positive gaps \(h_i=b_{i+1}-b_i\), \(1\le i<r\), and nonnegative slacks \(L=b_1-1\), \(U=n-b_r\). Then \(L+U+\sum_i h_i=n-1\). With \(S=L+U\), for \(r\ge2\)
\[
\Pr(S=s)=\frac{(s+1)\binom{n-s-2}{r-2}}{\binom nr},\quad 0\le s\le n-r.
\tag{4}
\]
For each fixed \(s\), this converges to \((s+1)\alpha^2(1-\alpha)^s\). These limits sum to one, hence \(S\) is tight. Conditional on \(S=s\), the \(r-1\) image gaps are a uniform positive composition of \(n-1-s\); their corresponding geometric parameter is \((r-1)/(n-1-s)=p_n+O(1/n)\) for bounded \(s\). Apply the conditional CLT (3) to each fixed \(s\), uniformly over any finite collection of values. Tightness then removes the conditioning on \(S\). Accordingly,
\[
\frac{\sum_{i=1}^{r-1}\log h_i-(r-1)\mu_\alpha}
{\sqrt{(r-1)v_\alpha}}\Longrightarrow\mathcal N(0,1).
\tag{5}
\]
The kernel composition and image subset are exactly independent for each \(n\). Adding their independent asymptotically normal logarithmic statistics, with variances \(rv_\alpha\) and \((r-1)v_\alpha\), proves the claimed normalization by \(\sqrt{2rv_\alpha}\). Equations (1)–(5) establish the theorem without extrapolating a finite experiment.

## Scientific significance

Higgins' inverse-matching theorem addresses existence of matchings in the nonregular inverse relation. An individual inverse-partner degree can differ greatly across maps of the same rank; its typical **multiplicative** fluctuations are not described by the average degree or by fixed-rank Dirichlet limits. The theorem identifies an exact nondegenerate Gaussian law for this natural log-degree statistic as rank grows proportionally with chain size. The subtraction \(\operatorname{Cov}(Z,\log Z)^2/\operatorname{Var}(Z)\) captures the loss of variance caused by conditioning the composition sum, which is essential to the asymptotic rather than a renaming of an ordinary independent-sum CLT.

## Relationship to prior work and originality boundary

The exact local degree factorization (1), all finite power moments, and sharp fixed-rank maxima were established in *Exact inverse-degree moments and Dirichlet limits for isotone transformation monoids* (published October 25, 2026, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exact-inverse-degree-moments-and-dirichlet-limits-for-isotone-tr--35b0c2d31193). The November 2, 2026 study *Exact extremal inverse neighborhoods in order-preserving transformation monoids* further determines the global maxima. Those contributions are fully credited and **not** repeated as originality claims here. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings* (arXiv:2610.01912v1), gives the structural inverse relation and a permutation matching, but not this specified proportional-rank log-degree central limit theorem. The fixed-rank \(n\to\infty\) Dirichlet product has a different regime from the present \(r\sim\alpha n\) Gaussian limit, so neither its moment identity nor its limit statement alone contains this CLT. General conditioned-composition central limit theory supplies the analytic method; the present specific stochastic law and explicit variance are the mathematical contribution. Best-of-knowledge priority remains qualified: an unindexed general theorem or older semigroup statistics may imply this specialization.

## Verification and limitations

The original finite direct-composition checker through \(n=6\) validates the product statistic and its earlier known moment formulas; it does **not** establish the asymptotic theorem. Its random samples at \(n=120,r=60\) are diagnostics only. The CLT above follows from the stated local Fourier inversion and endpoint-slack tightness, for fixed \(\alpha\in(0,1)\). No quantitative convergence rate, full degree histogram, or boundary-rank version is asserted. No new claim of independent certification, formal verification, or absolute bibliographic priority is made.
