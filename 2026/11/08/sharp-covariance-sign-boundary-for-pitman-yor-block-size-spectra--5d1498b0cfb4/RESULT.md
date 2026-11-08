# Sharp covariance sign boundary for Pitman–Yor block-size spectra

## Finding

Let \(\Pi_n\) be the exchangeable partition of \([n]\) from the two-parameter Poisson–Dirichlet (Pitman–Yor) sampling law. Write \(K_n\) for its total block count and \(M_{r,n}\) for its number of blocks of size exactly \(r\). For every \(n\ge2\), the covariance \(\operatorname{Cov}(M_{r,n},K_n)\), as \(r\) runs through \(1,\ldots,n\), changes sign **exactly once** from positive to negative, allowing at most one zero at an intermediate integer frequency.

More precisely, put \(g_j(\alpha,\theta)=\mathbb E_{\alpha,\theta}K_j\) for \(j\ge1\), and \(g_0=0\). Then

\[
\operatorname{Cov}(M_{r,n},K_n)=\binom nr\frac{(1-\alpha)_{r-1}(\theta+\alpha)_{n-r}}{(\theta+1)_{n-1}}\bigl[1+g_{n-r}(\alpha,\theta+\alpha)-g_n(\alpha,\theta)\bigr].\tag{1}
\]

Here \((x)_j=\prod_{i=0}^{j-1}(x+i)\), with \((x)_0=1\). The expression in square brackets is strictly decreasing in the integer \(r\), positive at \(r=1\), and negative at \(r=n\). The covariance has the same sign because its prefactor is strictly positive.

For \(0<\alpha<1\), define

\[
A_{\alpha,\theta}=\frac{\Gamma(\theta+1)}{\alpha\Gamma(\theta+\alpha)},\qquad
\rho_{\alpha,\theta}=1-\left(\frac{A_{\alpha,\theta}}{A_{\alpha,\theta+\alpha}}\right)^{1/\alpha}.
\]

This critical fraction is strictly between zero and one. If \(r_n^+\) is the largest integer frequency with positive covariance, then

\[
\lim_{n\to\infty}\frac{r_n^+}{n}=\rho_{\alpha,\theta}.\tag{2}
\]

For the Ewens case \(\alpha=0,\theta>0\), the same limit holds with \(\rho_{0,\theta}=1-e^{-1/\theta}\). In two Brownian excursion-sampling models the respective limits are

\[
\rho_{1/2,0}=1-\frac4{\pi^2}\quad\text{(unconditioned Brownian motion)},\qquad
\rho_{1/2,1/2}=1-\frac{\pi^2}{16}\quad\text{(Brownian bridge)}.\tag{3}
\]

## Assumptions and scope

The parameters range over \(0<\alpha<1\) with \(\theta>-\alpha\), and also \(\alpha=0\) with \(\theta>0\). The random partition has the standard exchangeable partition probability function

\[
p_{\alpha,\theta}(n_1,\ldots,n_k)=\frac{\prod_{j=1}^{k-1}(\theta+j\alpha)}{(\theta+1)_{n-1}}\prod_{i=1}^{k}(1-\alpha)_{n_i-1},\qquad \sum_{i=1}^k n_i=n.
\]

All claims concern the unconditional law of this random partition, not the law conditional on its diversity or its total block count. For (2), the parameters are held fixed as \(n\) grows. In (3), sample points are independent uniforms on \([0,1]\); labels are in the same block when their sample points belong to the same excursion interval, with the final meander interval included in the unconditioned Brownian case.

## Proof

**Marking a block.** Fix a particular set \(B\subseteq[n]\) of size \(r\). Canceling the factors for a block \(B\) in the displayed EPPF against those for the remaining partition under the shifted parameter \(\theta+\alpha\) gives, for each partition \(\pi\) of \([n]\setminus B\),

\[
\Pr_{\alpha,\theta}(B\text{ is a block},\ \Pi_{[n]\setminus B}=\pi)
= q_{n,r}\,\Pr_{\alpha,\theta+\alpha}(\Pi_{n-r}=\pi),
\quad q_{n,r}=\frac{(1-\alpha)_{r-1}(\theta+\alpha)_{n-r}}{(\theta+1)_{n-1}}.
\]

For \(r=n\), the remaining empty partition has probability one. Summing over the \(\binom nr\) choices of \(B\) gives \(\mathbb EM_{r,n}=\binom nr q_{n,r}\). On the event that \(B\) is a block, total block count is one plus the block count of its shifted-parameter remainder. Consequently

\[
\mathbb E(M_{r,n}K_n)=\mathbb EM_{r,n}\,[1+g_{n-r}(\alpha,\theta+\alpha)],
\]

which proves (1).

**Strict finite-size sign switch.** The Chinese restaurant recurrence is

\[
g_0=0,\qquad g_1=1,\qquad
g_{j+1}(\alpha,\theta)=g_j(\alpha,\theta)
+\frac{\theta+\alpha g_j(\alpha,\theta)}{\theta+j}\quad(j\ge1).
\]

Every increment is strictly positive since \(\theta+\alpha g_j\ge\theta+\alpha>0\). Therefore \(h_n(r):=1+g_{n-r}(\alpha,\theta+\alpha)-g_n(\alpha,\theta)\) strictly decreases with \(r\). Since \(g_n>1\) for \(n\ge2\), \(h_n(n)=1-g_n<0\). For \(r=1\), the transition probability of a new table after \(j\) customers and \(k\) tables is \((\theta+\alpha k)/(\theta+j)\). This probability is nondecreasing in both \(\theta\) and \(k\): its derivative in \(\theta\) has numerator \(j-\alpha k>0\) for \(1\le k\le j\). The standard common-uniform coupling thus gives \(g_{n-1}(\alpha,\theta+\alpha)\ge g_{n-1}(\alpha,\theta)\). Every one-step increase of \(g_j\) is strictly less than one for \(j\ge1\), so

\[
h_n(1)\ge1+g_{n-1}(\alpha,\theta)-g_n(\alpha,\theta)>0.
\]

This proves a single positive-to-negative sign boundary, with at most one zero. No generic nonzero assertion is made about the exceptional integer at the boundary.

**Macroscopic location.** Solving the expectation recurrence gives, for \(\alpha>0\),

\[
g_j(\alpha,\theta)=\frac1\alpha\left[\frac{(\theta+\alpha)_j}{(\theta+1)_{j-1}}-\theta\right]
= A_{\alpha,\theta}\frac{\Gamma(\theta+j+\alpha)}{\Gamma(\theta+j)}-\frac\theta\alpha
\quad(j\ge1).
\]

The standard gamma-ratio limit implies \(g_j(\alpha,\theta)\sim A_{\alpha,\theta}j^\alpha\). For \(r/n\to x\in(0,1)\),

\[
n^{-\alpha}h_n(r)\longrightarrow A_{\alpha,\theta+\alpha}(1-x)^\alpha-A_{\alpha,\theta}.
\]

This limiting function is strictly decreasing, with a unique zero \(\rho_{\alpha,\theta}\). Indeed \(\theta\mapsto A_{\alpha,\theta}\) is strictly increasing because the digamma function is increasing and \(\psi(\theta+1)-\psi(\theta+\alpha)>0\). Monotonicity of \(h_n\) and the signs at fixed fractions on either side of the zero imply (2).

For \(\alpha=0\), \(g_j(0,\theta)=\sum_{i=0}^{j-1}\theta/(\theta+i)\), so exactly

\[
h_n(r)=1-\theta\sum_{i=n-r}^{n-1}\frac1{\theta+i}.
\]

If \(r/n\to x\in(0,1)\), the sum tends to \(-\log(1-x)\), giving the root \(1-e^{-1/\theta}\). Finally the Brownian models have \((\alpha,\theta)=(1/2,0)\) and \((1/2,1/2)\), respectively, by the excursion partition construction in Pitman's *Poisson–Kingman partitions*, Sections 7–8. Substitution and \(\Gamma(1/2)=\sqrt\pi\) give (3).

## Verification

The standalone \(\texttt{check.py}\) uses only the Python standard library. It independently enumerates every restricted-growth set partition by Chinese restaurant transitions, calculates exact rational \(\mathbb E M_{r,n}\), \(\mathbb E K_n\), and \(\mathbb E(M_{r,n}K_n)\), and compares them with (1) for five rational parameter choices and \(2\le n\le8\). It also numerically checks the critical-fraction limit for four parameter choices at a sample size of 12000. Running \(\texttt{python3 check.py}\) produced **706 passing assertions**. Exact enumeration is a finite cross-check; the all-parameter results follow from the preceding analytic proof, not from the checks.

## Relationship to prior work

The EPPF, deletion of classes and Brownian excursion representation are standard results described by Pitman (2002), especially Proposition 12 and Sections 7–8. Those underlying laws, expected block counts and the algebraic possibility of obtaining the mixed moment are not claimed as new. Maller and Shemehsavar (2024, 2026) study frequency-spectrum and diversity distributions jointly; in particular, their 2026 paper contains a general finite-sample transform and macroscopic-frequency limit results. The contribution assessed here is the **strict all-parameter sign ordering and its explicit macroscopic critical fraction**, including different Brownian motion/bridge thresholds, rather than a general joint generating function. A published result for uniform set partitions has a distinct one-switch law at a logarithmic scale; it is not the two-parameter Poisson–Dirichlet sampling model.

## Limitations

There may be historical derivations of the same sign theorem from known joint formulas; an inaccessible closely related 2024 full text leaves residual priority risk. This is not an independence assertion or external certification. For a finite \(n\), a single integer size can have exactly zero covariance. The result gives a *limit* for the last positive size, not an explicit closed formula for that integer at every \(n\). It does not give conditional-on-diversity covariance signs, multivariate covariance matrices, or extensions to arbitrary Gibbs partitions.

## References

1. Jim Pitman, *Poisson–Kingman partitions*, arXiv:math/0210396v1, first posted October 24, 2002, https://arxiv.org/abs/math/0210396. Sections 6–8, Proposition 12.
2. Ross A. Maller and Soudabeh Shemehsavar, *Asymptotics of the allele frequency spectrum and the number of alleles*, published online November 22, 2024, https://doi.org/10.1017/jpr.2024.84. Abstract inspected; full text unavailable for this comparison.
3. Ross A. Maller and Soudabeh Shemehsavar, *Limit Theorems for the Pitman–Yor Frequency Spectrum*, arXiv:2607.23401v1, first posted July 26, 2026, https://arxiv.org/abs/2607.23401. Full text inspected, especially Theorem 2.1 and Section 3.
4. *Block-size counts switch covariance sign at the Lambert-W scale*, published 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-block-size-counts-switch-covariance-sign-at-the-lambert-w-scale--8198e77842ad. Published summary inspected for distinction of partition laws.
