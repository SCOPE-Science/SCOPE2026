# Asymptotically independent shadow-volume and central-section face fluctuations of a regular simplex

## Finding
Let \(N\ge3\) and let \(\Delta_{N-1}=\operatorname{conv}(e_1,\ldots,e_N)\) be the regular \((N-1)\)-simplex of side length \(\sqrt2\), in its affine span \(H=\{x\in\mathbb R^N:\sum_i x_i=1\}\). Select a unit vector \(a\) Haar-uniformly from \(H_0=\{x:\sum_i x_i=0\}\). Let \(P_N\) be the \((N-2)\)-volume of the orthogonal projection of \(\Delta_{N-1}\) to the hyperplane in \(H\) normal to \(a\). Let \(f_{N,k}\) be the number of \(k\)-faces of the central section \(\Delta_{N-1}\cap\{x\in H:a\cdot x=0\}\), for each fixed \(k\ge0\) and \(N\ge k+3\). Define
\[
 R_N=\frac{2(N-2)!}{N}P_N,\qquad
 D_{N,k}=\frac{\binom N{k+2}-2\binom{N/2}{k+2}-f_{N,k}}{N^{k+1}},
\]
where \(\binom{x}{j}=x(x-1)\cdots(x-j+1)/j!\) for real \(x\).

For every fixed \(m\ge0\), as \(N\to\infty\),
\[
 \left(\sqrt N\left(R_N-\sqrt{\frac2\pi}\right),D_{N,0},\ldots,D_{N,m}\right)
 \ \Longrightarrow\ 
 \left(X,\frac{Y^2}{4},\frac{Y^2}{2^3 1!},\ldots,\frac{Y^2}{2^{m+2}m!}\right),
\]
where \(X\sim N(0,1-3/\pi)\), \(Y\sim N(0,1-2/\pi)\), and **\(X\) and \(Y\) are independent**. Consequently, the Gaussian fluctuation of the shadow volume is asymptotically independent of the entire finite collection of central-section face deficits, whose limit is driven by one chi-square variable. The variance \(1-3/\pi\) is strictly positive.

The normalized shadow also has exact finite-dimensional first and second moments. With \(\rho_N=-1/(N-1)\),
\[
 \mathbb E R_N=\frac{\sqrt{N-1}\,\Gamma((N-1)/2)}{\sqrt\pi\,\Gamma(N/2)},
\qquad
 \mathbb E R_N^2=\frac1N+\frac{2(N-1)}{\pi N}
 \left(\sqrt{1-\rho_N^2}+\rho_N\arcsin\rho_N\right).
\]

## Assumptions and scope
Haar-uniform refers to the rotation-invariant probability on the unit sphere of \(H_0\). All sections and projections use the **same** random normal. Almost surely no coordinate of \(a\) vanishes and the section is in combinatorial general position. Dimensions and factorial normalizations are those displayed above; \(k\) and \(m\) stay fixed as \(N\to\infty\). This result concerns hyperplane shadows and central face counts of a simplex, not random points uniformly drawn inside it.

## Proof
**1. Exact geometric reductions.** The hyperplane-projection formula (Pandis, Theorem 1.2, reference [1]) gives
\[
 P_N=\frac{\sqrt N}{2(N-2)!}\sum_{i=1}^N|a_i|,
\qquad R_N=\frac1{\sqrt N}\sum_{i=1}^N|a_i|.
\]
Let \(K_N=\#\{i:a_i>0\}\) and \(S_N=2K_N-N\). A \(k\)-face of the section corresponds uniquely to a \((k+1)\)-face of the simplex with vertices on both sides of the cutting hyperplane. Thus, for \(j=k+2\),
\[
 f_{N,k}=\binom Nj-\binom{K_N}j-\binom{N-K_N}j.
\]
These identities hold almost surely, with ordinary integer binomials for integer arguments.

**2. Gaussian representation and the shadow influence function.** Let \(G_1,\ldots,G_N\) be independent standard normal variables, \(\bar G=N^{-1}\sum_iG_i\), and \(B_N=N^{-1}\sum_i(G_i-\bar G)^2\). Rotational invariance gives
\[
 a\ \overset d=\ \frac{(G_i-\bar G)_{i=1}^N}{\sqrt{NB_N}},
\qquad R_N\ \overset d=\ \frac{N^{-1}\sum_i|G_i-\bar G|}{\sqrt{B_N}}.
\]
Put \(\mu=\sqrt{2/\pi}\). Since \(|\bar G|=O_{\mathbb P}(N^{-1/2})\), the elementary inequality
\[
 \big||x-t|-|x|+t\operatorname{sgn}x\big|\le2|t|\,\mathbf1_{\{|x|\le|t|\}}
\]
implies
\[
 N^{-1}\sum_i|G_i-\bar G|=N^{-1}\sum_i|G_i|+o_{\mathbb P}(N^{-1/2}).
\]
Indeed the linear term is \(-\bar G\,N^{-1}\sum_i\operatorname{sgn}G_i=O_{\mathbb P}(N^{-1})\), and the remainder is bounded by \(2|\bar G|\) times the empirical fraction within \(|\bar G|\) of zero, which is \(O_{\mathbb P}(N^{-1/2})\). Also \(B_N=N^{-1}\sum_iG_i^2+o_{\mathbb P}(N^{-1/2})\). Taylor expansion of the reciprocal square root yields
\[
 \sqrt N(R_N-\mu)=\frac1{\sqrt N}\sum_{i=1}^N U(G_i)+o_{\mathbb P}(1),
\quad U(g)=|g|-\mu-\frac\mu2(g^2-1).
\]

**3. The section-sign influence function.** Almost surely \(S_N=\sum_i\operatorname{sgn}(G_i-\bar G)\). For the empirical normal distribution function \(F_N\), its centered stochastic increments over intervals of width \(O(N^{-1/2})\) are \(o_{\mathbb P}(N^{-1/2})\) uniformly. This follows, for example, by the standard empirical-CDF stochastic-equicontinuity lemma; it also follows directly by bounding the maximal centered count in a shrinking interval using binomial variance and a maximal inequality. Since \(\bar G=O_{\mathbb P}(N^{-1/2})\) and the normal density at zero equals \(1/\sqrt{2\pi}\),
\[
 \frac{S_N}{\sqrt N}=\frac1{\sqrt N}\sum_{i=1}^N W(G_i)+o_{\mathbb P}(1),
\quad W(g)=\operatorname{sgn}(g)-\mu g.
\]
The functions \(U\) and \(W\) are centered, respectively even and odd. Direct standard-normal moments give
\[
 \operatorname{Var}U=1-3/\pi,\qquad
 \operatorname{Var}W=1-2/\pi,\qquad
 \operatorname{Cov}(U,W)=0.
\]
The bivariate classical central limit theorem therefore yields independent Gaussian limits \((X,Y)\) for \((\sqrt N(R_N-\mu),S_N/\sqrt N)\).

**4. All fixed face dimensions simultaneously.** Write \(j=k+2\), \(x=N/2\), and \(\delta=S_N/2\). The exact face identity gives
\[
 N^{k+1}D_{N,k}=\binom{x+\delta}j+\binom{x-\delta}j-2\binom xj.
\]
As a polynomial in \(x\), \(\binom xj\) has leading coefficient \(1/j!\). Since \(S_N=O_{\mathbb P}(\sqrt N)\), Taylor's even-term expansion, for each fixed \(k\), gives
\[
 D_{N,k}=\frac1{2^{k+2}k!}\left(\frac{S_N}{\sqrt N}\right)^2+o_{\mathbb P}(1).
\]
For \(k=0\) the identity is exact. Joint convergence and the continuous mapping theorem prove the displayed limit for any fixed \(m\).

**5. Finite-dimensional moments.** The Gaussian direction \(a\) is independent of its radial norm. Since each coordinate of its unnormalized centered Gaussian vector has variance \((N-1)/N\), the spherical-coordinate formula yields \(\mathbb E|a_i|=\sqrt{(N-1)/N}\,\Gamma((N-1)/2)/(\sqrt\pi\Gamma(N/2))\), giving \(\mathbb E R_N\). For distinct indices, the centered Gaussian coordinates have correlation \(\rho_N\), and the bivariate normal identity
\[
 \mathbb E|Z_1Z_2|=\frac2\pi\bigl(\sqrt{1-\rho^2}+\rho\arcsin\rho\bigr)
\]
for unit marginal variances gives \(\mathbb E|a_i a_j|=(2/(\pi N))(\sqrt{1-\rho_N^2}+\rho_N\arcsin\rho_N)\), because the squared Gaussian radius has mean \(N-1\). Expanding \(R_N^2=N^{-1}(\sum_i|a_i|)^2\) gives the second moment.

## Verification
The supplementary `verify.py` independently computes projected-simplex volumes by direct convex-hull geometry for small dimensions and enumerates crossed faces. It compares exact moment formulas against Monte Carlo and tests the predicted asymptotic covariance matrix in dimensions 200 and 1000 with a fixed random seed. The executable script makes 387 explicit assertions; it is supplementary numerical evidence only. The limits are established by the preceding analytic argument.

## Relationship to prior work
Pandis [1] supplies the exact hyperplane-projection formula and characterizes extrema, but does not establish the Gaussian projection-volume fluctuations or their **joint decoupling** from section face counts. Earlier central-simplex-section results determine the section marginal and its chi-square scaling; these do not determine its joint law with the *same direction's* shadow volume. Prochno, Thäle, and Tuchel [2] prove projection-volume limit theorems for fixed-dimensional projections of \(\ell_p\)-balls, not codimension-one projections of simplices. Baci et al. [3] investigate norms of points sampled uniformly inside the simplex, not Haar normals. Dirksen [4] studies geometric volumes of simplex sections, rather than this joint shadow/face law. The new assertion is the **joint independent product law** and its exact shadow normalization and variance; it is not a claim that the two existing marginal theories are new.

## Limitations
The face-vector statement holds for finitely many fixed ranks as dimension increases, not simultaneously for ranks growing with \(N\). The finite-dimensional moment formulas concern only shadow volume and not arbitrary mixed shadow/section moments. Classical empirical-process and central limit theorems are invoked, with the critical influence functions and coefficients explicitly derived. No quantitative convergence rate or independent audit is claimed. Historical priority is provisional pending broader expert review.

## References
[1] C. Pandis, *On Extremal Volume Projections of the Simplex and the Cube*, arXiv:2601.18436v1 (first public 2026-01-26), Theorem 1.2. https://arxiv.org/html/2601.18436

[2] J. Prochno, C. Thäle, P. Tuchel, *Limit Theorems for the Volume of Random Projections and Sections of ℓp-balls*, arXiv:2412.16054v1 (2024), Theorem A. https://arxiv.org/pdf/2412.16054

[3] A. Baci, Z. Kabluchko, J. Prochno, M. Sonnleitner, C. Thäle, *Limit theorems for random points in a simplex*, arXiv:2005.04911v1 (2020). https://arxiv.org/pdf/2005.04911

[4] H. Dirksen, *Sections of the regular simplex — Volume formulas and estimates*, arXiv:1509.06408 (2015/2016). https://arxiv.org/abs/1509.06408
