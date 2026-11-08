# The inverse-partner degree law and Gaussian logarithmic fluctuations for isotone transformations

## Finding
Let \(\mathcal O_n\) be the semigroup of all weakly increasing full transformations of the ordered chain \([n]=\{1,\dots,n\}\). Two elements are mutual semigroup inverses if \(fgf=f\) and \(gfg=g\). For \(f\in\mathcal O_n\), put
\[
\nu(f)=|\{g\in\mathcal O_n:fgf=f,\ gfg=g\}|.
\]
The new result determines every integer moment of this **individual inverse-partner degree**, its sharp extrema in each rank, and its logarithmic limiting distribution for a uniformly sampled fixed-rank transformation.

**Exact degree.** Suppose \(f\) has rank \(r\), with its \(r\) consecutive nonempty kernel blocks of respective sizes \(a_1,\ldots,a_r\), and its image is \(\{b_1<\cdots<b_r\}\). Then
\[
\boxed{\nu(f)=\left(\prod_{i=1}^r a_i\right)\left(\prod_{i=1}^{r-1}(b_{i+1}-b_i)\right).}
\]
Empty products equal one.

**All-moment factorization.** For every integer \(k\ge0\), let \(G_k(z)=\sum_{j\ge1}j^kz^j\). If \(D_{n,r}\) is the set of rank-\(r\) members of \(\mathcal O_n\), then
\[
\boxed{\sum_{f\in D_{n,r}}\nu(f)^k
= [z^n]G_k(z)^r\;\cdot\;[z^{n-1}]\frac{G_k(z)^{r-1}}{(1-z)^2}.}
\]
Thus the full sequence of power moments, and hence the complete finite distribution of inverse-partner degrees, is explicitly computable by finite integer convolution. In particular \(|D_{n,r}|=\binom{n-1}{r-1}\binom nr\), and the first moment agrees with the previously known ordered inverse-pair count \(\binom{n+r-1}{2r-1}^2\); this first moment is *not* claimed as new.

**Sharp degree range.** Define, for \(N\ge k\ge1\),
\[
P_k(N)=\lfloor N/k\rfloor^{k-s}(\lfloor N/k\rfloor+1)^s,
\qquad s=N\bmod k,
\]
and put \(P_0(0)=1\). Then
\[
\boxed{\min_{f\in D_{n,r}}\nu(f)=n-r+1,\qquad
\max_{f\in D_{n,r}}\nu(f)=P_r(n)P_{r-1}(n-1)}
\]
for \(r\ge2\), while for \(r=1\) both the minimum and maximum equal \(n\). The upper bound is attained precisely when the kernel block sizes are as balanced as possible and, for \(r\ge2\), the image includes both endpoints and has gaps as balanced as possible. The lower bound is attained when all but at most one kernel block have size one and the image consists of consecutive points (with the obvious degeneracies when all blocks have size one).

**Conditional logarithmic central limit theorem.** Fix \(0<\alpha<1\), set \(r_n=\lfloor\alpha n\rfloor\), and choose \(F_n\) uniformly from \(D_{n,r_n}\). Let \(Z\) have the geometric law \(\Pr(Z=j)=\alpha(1-\alpha)^{j-1}\), \(j\ge1\), and define
\[
\mu_\alpha=\mathbb E\log Z,\qquad
v_\alpha=\operatorname{Var}(\log Z)
-\frac{\operatorname{Cov}(Z,\log Z)^2}{\operatorname{Var}(Z)}>0.
\]
Then
\[
\boxed{\frac{\log\nu(F_n)-(2r_n-1)\mu_\alpha}
{\sqrt{2r_n v_\alpha}}\ \xrightarrow{\mathrm d}\ \mathcal N(0,1).}
\]
Hence the typical inverse-partner count has a logarithmic Gaussian fluctuation of order \(\sqrt n\), although the rank is fixed. This is different from the previously known Gaussian limit for the **rank of a random mutual-inverse pair**.

## Assumptions and scope
All transformations are total, order-preserving maps of the labeled linearly ordered \(n\)-set, not partial transformations or non-monotone transformations. The inverse relation is the pair of semigroup sandwich identities, not group inversion. Fixed-rank sampling is uniform over \(D_{n,r}\). The exact finite moment identity applies for every \(n\ge1\), \(1\le r\le n\) and integer \(k\ge0\). The probabilistic limit assumes fixed \(\alpha\in(0,1)\), not a rank tending to zero or a rank with bounded defect.

## Proof
**1. Inverse relation.** A rank-\(r\) weakly increasing map \(f\) is uniquely described by its consecutive kernel blocks \(A_1<\cdots<A_r\) and its increasing image \(B=\{b_1<\cdots<b_r\}\). A second rank-\(r\) map \(g\), with blocks \(C_i\) and image \(D=\{d_1<\cdots<d_r\}\), is a mutual inverse precisely when \(d_i\in A_i\) and \(b_i\in C_i\) for all \(i\). Necessity follows since the sandwich identities restrict \(f\) and \(g\) to mutually inverse order-preserving bijections between their images. Conversely, these two sets of inclusions give \(f(d_i)=b_i\), \(g(b_i)=d_i\), and both sandwich identities. The ranks must agree because each sandwich identity bounds one rank by the other. The transversality characterization is also given by Higgins (2026), Section 3.

For fixed \(f\), the choice of \(D\) is a transversal of the kernel blocks \(A_i\), yielding \(\prod_i a_i\) possibilities. Independently, choose the \(r-1\) cut points of the kernel of \(g\): the cut between \(C_i\) and \(C_{i+1}\) can be any integer from \(b_i\) through \(b_{i+1}-1\), yielding \(\prod_{i<r}(b_{i+1}-b_i)\) choices. This proves the degree formula.

**2. Every moment.** Uniform rank-\(r\) maps are in bijection with the Cartesian product of (i) positive compositions \(a_1+\cdots+a_r=n\) and (ii) increasing \(r\)-subsets \(B\) of \([n]\). Therefore the sum of powers of \(\nu\) factors. The first factor is exactly \([z^n]G_k(z)^r\). For \(r\ge2\), set \(h_i=b_{i+1}-b_i\ge1\), with total \(H=\sum h_i\le n-1\). Given these gaps there are exactly \(n-H\) possible starting image points \(b_1\). The coefficient of \(z^{n-1-H}\) in \((1-z)^{-2}\) is \(n-H\), proving the second factor. The same identity for \(r=1\) follows from \(G_k^0=1\) and \([z^{n-1}](1-z)^{-2}=n\). At \(k=0\), the identity recovers \(|D_{n,r}|\); at \(k=1\), \(G_1(z)=z/(1-z)^2\), and both factors equal \(\binom{n+r-1}{2r-1}\). A finite nonnegative integer-valued distribution is determined by all its moments; moreover all \(\nu(f)\) lie in the displayed finite sharp interval, so finitely many moments already suffice by Vandermonde inversion.

**3. Extremes.** For positive integers \(a,b\), \(ab\ge a+b-1\), and repeated merging yields \(\prod a_i\ge n-r+1\), with equality when all but at most one part equal one. Each image gap is at least one, and choosing consecutive image points gives gap-product one. Thus the lower bound is sharp. Conversely, replacing unequal positive parts \(a,b\) with \(a+1,b-1\) when \(b\ge a+2\) raises their product. Consequently the maximum product among positive \(r\)-compositions of \(n\) equals \(P_r(n)\), attained exactly by balanced parts. For image gaps, the total cannot exceed \(n-1\) and the maximum increases with total, so choose \(b_1=1\), \(b_r=n\) and distribute the \(n-1\) gap units as evenly as possible, giving \(P_{r-1}(n-1)\). The kernel and image choices are independent, proving sharpness and the equality conditions.

**4. Conditional central limit theorem for compositions.** Write \(r=r_n\) and \(p_n=r/n\), so \(p_n\to\alpha\). If \(Z_1,\dots,Z_r\) are independent positive geometric random variables of parameter \(p_n\), conditioned on \(\sum_i Z_i=n\), then every positive composition of \(n\) into \(r\) parts has equal conditional probability, since its unconditioned probability equals \(p_n^r(1-p_n)^{n-r}\). Put \(\mu_p=\mathbb E_p\log Z\), \(\beta_p=\operatorname{Cov}_p(Z,\log Z)/\operatorname{Var}_p(Z)\), and \(W=\log Z-\mu_p-\beta_p(Z-1/p)\). Then \(\operatorname{Cov}_p(W,Z)=0\) and \(\operatorname{Var}_p(W)=v_p\). A standard local Fourier proof yields the conditional CLT
\[
\frac{\sum_{i=1}^{r}\log Z_i-r\mu_{p_n}}{\sqrt{r v_{p_n}}}\ \Bigm|\ \sum_i Z_i=n
\quad\xrightarrow{\mathrm d}\quad\mathcal N(0,1).
\]
For clarity, Fourier inversion in the lattice coordinate gives the conditional characteristic function as the ratio of integrals
\[
\frac{\int_{-\pi}^{\pi}\bigl[\mathbb E_{p_n}e^{i\theta(Z-1/p_n)+itW/\sqrt r}\bigr]^r\,d\theta}
{\int_{-\pi}^{\pi}\bigl[\mathbb E_{p_n}e^{i\theta(Z-1/p_n)}\bigr]^r\,d\theta}.
\]
Aperiodicity of the geometric distribution makes the contributions outside \(|\theta|=O(r^{-1/2})\) negligible; inside this window Taylor expansion of the joint characteristic function, with zero mixed covariance, gives the ratio \(e^{-t^2v_\alpha/2}\) after rescaling. The geometric variables have uniformly finite exponential moments for \(p_n\) near \(\alpha\); this justifies uniform domination and the Taylor remainder. The linear subtraction of \(\beta_p(\sum Z_i-r/p_n)\) vanishes exactly under the conditioning. Since \(\log j\) is not affine in \(j\) on \(\{1,2,3\}\), \(v_\alpha>0\).

**5. Image gaps.** A uniformly random image \(r\)-subset is described by \(r-1\) positive gaps \(h_i\) and two nonnegative endpoint slacks \(L=b_1-1\), \(U=n-b_r\), with \(L+U+\sum h_i=n-1\). Put \(S=L+U\). Then
\[
\Pr(S=s)=\frac{(s+1)\binom{n-s-2}{r-2}}{\binom nr}
\quad(0\le s\le n-r),
\]
which converges for each fixed \(s\) to \((s+1)\alpha^2(1-\alpha)^s\). This limiting probability law has total mass one, so \(S=O_{\Pr}(1)\). Conditional on \(S=s\), the \(r-1\) gaps are a uniform positive composition of \(n-1-s\); their geometric parameter \((r-1)/(n-1-s)\) differs from \(p_n\) by \(O(1/n)\) for bounded \(s\). The preceding conditional Fourier argument applies uniformly on every bounded collection of \(s\), and the tightness of \(S\) transfers the CLT to the image gap log product, centered at \((r-1)\mu_\alpha\), with variance asymptotic to \((r-1)v_\alpha\). For the kernel part, replacing \(\mu_{p_n},v_{p_n}\) by \(\mu_\alpha,v_\alpha\) changes its centering by \(O(1)\), since \(r_n=\lfloor\alpha n\rfloor\). The kernel composition and image subset are independent under uniform rank-\(r\) sampling. Adding their independent asymptotically Gaussian log products proves the displayed central limit theorem with scaling \(\sqrt{2rv_\alpha}\).

## Verification
The file `CHECK_DEGREE.py` uses exhaustive direct composition of every pair of isotone transformations through \(n=6\), verifies the individual degree formula for every element, checks all exact rank-stratified power moments for \(k=0,1,2,3\), and independently checks the sharp rank extrema. It also includes a reproducible large-sample diagnostic for the log-degree limit at \(n=120,r=60\), which is a finite empirical check, not a proof. The recorded output `CHECK_DEGREE_OUTPUT.txt` concludes with `DEGREE_VERIFY_OK` and `ASYMPTOTIC_DIAGNOSTIC_OK`. The unbounded all-moment theorem and the CLT follow from the proofs above, not from finite experiments.

## Relationship to prior work
Higgins (2026), arXiv:2610.01912v1, Theorems A and B and Sections 2–3, establishes permutation matchings for \(\mathcal O_n\) and states the crossed-square inverse relation. It already supplies the incidence/transversality foundation. Higgins (2024), *Finite regular semigroups with permutations that map elements to inverses*, studies inverse matchings and poses the existence question for isotone maps. Higgins (2026) explains why the isotone inverse neighborhoods are not regular in the manner exploited for the full transformation monoid. The earlier 1993 paper *Combinatorial results for semigroups of order-preserving mappings* treats rank, components, and other enumerative random-map statistics; its available full-text material does not expose the conditional log-degree limit. The exact ordered inverse-pair rank count, its maximizing ranks, Pell ties, and a Gaussian law for the **rank when a mutual-inverse pair is selected** have been derived previously and are not claimed here. These results amount to the **first** partner-degree moment and a different conditional distribution; they do not determine the second and higher partner-degree moments nor the logarithmic degree CLT for a **uniform single map of prescribed rank**. The new contribution is exactly that higher-moment factorization, sharp degree profile, and conditional Gaussian fluctuation law, not the transversality criterion or first moment. Search-based historical priority is not absolute; a more general conditioned-composition limit theorem could imply the fluctuation part as a specialization.

## Limitations
The theorem does not give a closed expression for the complete discrete degree histogram with every possible degree explicitly listed, although the moment identities determine it. The conditional CLT is only for proportional ranks \(r_n\sim\alpha n\) with fixed interior \(\alpha\), and does not claim quantitative error bounds or an analogous statement for partial maps. The geometric conditional-CLT argument invokes a standard Fourier/local-limit step, for which a detailed integrand and nondegeneracy argument are provided. No independent review or formal proof verification has been performed.

## References
1. P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1, 1 October 2026, especially Sections 2 and 3. https://arxiv.org/abs/2610.01912.
2. P. M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, Semigroup Forum 109 (2024), 141–147. https://doi.org/10.1007/s00233-024-10430-0.
3. P. M. Higgins, *Combinatorial results for semigroups of order-preserving mappings*, Math. Proc. Cambridge Philos. Soc. 113 (1993), 281–296. https://doi.org/10.1017/S0305004100075964.
