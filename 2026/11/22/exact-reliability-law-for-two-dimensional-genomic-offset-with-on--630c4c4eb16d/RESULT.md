# Exact reliability law for two-dimensional genomic offset with one latent trait

## Finding

Consider squared genomic offset and realized mean log-fitness loss from a single latent adaptive trait under Gaussian environmental displacement and Gaussian allelic effects. The entire probability law, over possible genetic architectures, of the squared across-environment predictive correlation is determined by one spectral ratio. If the two eigenvalues of the environmentally whitened genotype–environment-association (GEA) metric have ratio \(\kappa>1\), then the squared correlation \(X\) has strict-support endpoints

\[
 x_-(\kappa)=\frac{1}{1+\kappa^2},\qquad x_+(\kappa)=\frac{\kappa^2}{1+\kappa^2}.
\]

For \(x_-<x<x_+\), put \(r=\sqrt{(1+\kappa^2)x}\). Its cumulative distribution is exactly

\[
 \Pr_{a}\{X\leq x\}=
 \frac{2}{\pi}\arctan\sqrt{\frac{r-1}{\kappa(\kappa-r)}}.
 \tag{1}
\]

The CDF is zero at and below \(x_-\) and one at and above \(x_+\). The architecture-averaged mean and unique median are

\[
 \mathbb E_a X=\frac{(\kappa+1)^2-\tfrac32(\kappa+1)\sqrt\kappa}{\kappa^2+1},
 \qquad \operatorname{median}_a(X)=\frac{\kappa^2+1}{(\kappa+1)^2}.
 \tag{2}
\]

Both are strictly increasing in \(\kappa>1\). Their deficits have different asymptotic orders:

\[
 1-\mathbb E_a X\sim \frac{3}{2\sqrt\kappa},\qquad
 1-\operatorname{median}_a(X)\sim\frac2\kappa.
 \tag{3}
\]

More sharply, for each fixed \(x\in(0,1)\),

\[
 \lim_{\kappa\to\infty}\sqrt\kappa\Pr_a(X\le x)
 =\frac{2x^{1/4}}{\pi\sqrt{1-\sqrt x}}.
 \tag{4}
\]

At \(\kappa=1\), the distribution degenerates exactly to \(X=1/2\). For \(\kappa=4\), \(\mathbb E_aX=10/17\), \(\operatorname{median}_a(X)=17/25\), and \(\Pr_a(X<1/2)=0.3733739934\ldots\).

## Assumptions and scope

Fix any integer \(L\ge2\), and deterministic GEA vectors \(b_1,\ldots,b_L\in\mathbb R^2\) such that \(C_b=L^{-1}\sum_{\ell=1}^L b_\ell b_\ell^{\top}\) is positive definite. Environmental displacements \(h\sim N(0,\Sigma_x)\) have a fixed, positive-definite \(2\times2\) covariance \(\Sigma_x\), independently of genetic-architecture uncertainty. The squared genomic-offset score is \(g(h)=h^\top C_bh\).

There is one latent adaptive trait, with independent conditional Gaussian allelic effects \(a_\ell\sim N(0,\sigma_a^2)\), \(\sigma_a>0\), and genetic-effect vector

\[
 \beta=L^{-1/2}\sum_{\ell=1}^L b_\ell a_\ell.
\]

There are no direct environmental mismatch effects. Under a strictly positive scalar selection strength, the *quenched mean negative log-relative fitness* is an affine positive rescaling of \((\beta^\top h)^2\); environmental-independent residual noise, if present, only contributes a constant in this conditional mean. The across-environment predictive reliability for a fixed realization \(\beta\ne0\) is

\[
 X=\operatorname{Corr}_{h}^{2}\bigl(g(h),\mathbb E[ -\log\omega(h)\mid h,\beta]\bigr).
\]

The probability and expectation in the theorem are over allelic effects, conditional on the GEA vectors. Write \(A=\Sigma_x^{1/2}C_b\Sigma_x^{1/2}\); its positive eigenvalues \(\lambda_1\ge\lambda_2\) determine \(\kappa=\lambda_1/\lambda_2\). The theorem does not assume all genetically possible architectures are biologically equally likely; the stated Gaussian uncertainty model is essential. It does not describe realized relative fitness, with its residual biological noise, or empirical out-of-sample \(R^2\).

## Proof

**1. Matrix covariance reduction.** Put \(z=\Sigma_x^{-1/2}h\sim N(0,I_2)\) and \(w=\Sigma_x^{1/2}\beta\). Then \(g(h)=z^\top A z\) and the nonconstant part of the quenched loss is a positive multiple of \((w^\top z)^2\). For any symmetric matrices \(M,N\) and standard normal \(z\), Isserlis' formula gives \(\operatorname{Cov}(z^\top Mz,z^\top Nz)=2\operatorname{tr}(MN)\), with corresponding variances \(2\operatorname{tr}(M^2)\) and \(2\operatorname{tr}(N^2)\). Therefore, outside the probability-zero event \(w=0\),

\[
 X=\frac{(w^\top Aw)^2}{\operatorname{tr}(A^2)(w^\top w)^2}.
 \tag{5}
\]

The Gaussian allelic-effect model gives \(\beta\sim N(0,\sigma_a^2C_b)\) exactly, hence \(w\sim N(0,\sigma_a^2A)\). Orthogonal diagonalization and cancellation of common scales allow \(A=\operatorname{diag}(\kappa,1)\), \(w=\sigma_a(\sqrt\kappa U,V)^\top\), where \(U,V\) are independent standard normals. Thus, with \(T=V^2/U^2\),

\[
 X=\frac1{\kappa^2+1}
 \left(\frac{\kappa^2+T}{\kappa+T}\right)^2.
 \tag{6}
\]

**2. Distribution and boundaries.** The ratio \(V/U\) is standard Cauchy, so for \(t\ge0\), \(\Pr(T\le t)=(2/\pi)\arctan\sqrt t\). For \(\kappa>1\), \(R(T)=(\kappa^2+T)/(\kappa+T)\) strictly decreases from \(\kappa\) to \(1\), with \(R'(T)=\kappa(1-\kappa)/(\kappa+T)^2<0\). Solving \(R(T)=r\) gives \(T=\kappa(\kappa-r)/(r-1)\). Hence, for \(1<r<\kappa\),

\[
 \Pr(R\le r)=\Pr\left(T\ge\frac{\kappa(\kappa-r)}{r-1}\right)
 =\frac2\pi\arctan\sqrt{\frac{r-1}{\kappa(\kappa-r)}}.
\]

This proves (1), including the endpoint values and continuity. At \(\kappa=1\), (6) equals \(1/2\) identically.

**3. Median and mean.** The strictly increasing CDF of \(T\) has median \(1\), and the map \(T\mapsto X\) is strictly decreasing for \(\kappa>1\); thus the unique median is \(X(1)=(\kappa^2+1)/(\kappa+1)^2\). For the mean let \(U/\sqrt{U^2+V^2}=\cos\theta\), \(V/\sqrt{U^2+V^2}=\sin\theta\). The ratio is unaffected by radial magnitude or signs, and \(\theta\) is uniform on \([0,\pi/2]\) after reduction to the first quadrant. Set \(D=\kappa\cos^2\theta+\sin^2\theta\). Direct algebra yields

\[
 \frac{\kappa^2\cos^2\theta+\sin^2\theta}{D}
 =\kappa+1-\frac\kappa D.
\]

The elementary definite integrals

\[
 \frac2\pi\int_0^{\pi/2}\frac{d\theta}{D}=\frac1{\sqrt\kappa},\qquad
 \frac2\pi\int_0^{\pi/2}\frac{d\theta}{D^2}=
 \frac{\kappa+1}{2\kappa^{3/2}}
\]

follow from \(u=\tan\theta\) and differentiating the rational integral, respectively. Expanding \((\kappa+1-\kappa/D)^2\) and dividing by \(\kappa^2+1\) proves the mean identity (2).

**4. Monotonicity and tails.** The median derivative is \(2(\kappa-1)/(\kappa+1)^3>0\). For the mean derivative, put \(t=\sqrt\kappa>1\). It factors as

\[
 \frac{d\mathbb E_a X}{d\kappa}=
 \frac{(t-1)(t+1)(3t^4-8t^3+12t^2-8t+3)}{4t(t^4+1)^2}>0.
\]

Indeed, the quartic factor is \(t^2[3(t+t^{-1})^2-8(t+t^{-1})+6]\), positive because \(t+t^{-1}\ge2\) and the bracket is strictly positive and increasing on \([2,\infty)\). Expanding (2) for large \(\kappa\) proves (3). At fixed \(x\in(0,1)\), in (1) one has \(r\sim\kappa\sqrt x\) and the square-root argument is asymptotic to \(x^{1/4}/[\sqrt\kappa\sqrt{1-\sqrt x}]\). Since \(\arctan y\sim y\) as \(y\downarrow0\), (4) follows.

No infinite-sample claim relies on numerical computation.

## Verification

The standalone standard-library checker at `verification/check.py` independently evaluates the original matrix/normal representation, the closed CDF, the exact cases at \(\kappa=1,4\), numerical quadrature for the mean, and seeded Gaussian empirical distributions for multiple anisotropies. Execute `python verification/check.py` from the directory containing this document. Finite numerical tests are only consistency checks; the derivation above proves the quantified statements.

## Relationship to prior work

François (2026) supplies the underlying genomic-offset framework, Gaussian allelic effects, and the formula for squared quenched correlation in its Equations (3.7) and (4.19), as well as eigenvalue bounds in (4.20). Those are pre-existing results. The present result fixes a biologically interpretable uncertainty ensemble and computes the *entire* architecture-to-architecture distribution, its mean, median, and an exact rare-low-reliability asymptotic in two environmental dimensions. In particular, the different \(\kappa^{-1/2}\) and \(\kappa^{-1}\) rates cannot be read off from a deterministic spectral bound. Gain et al. (2023) introduced the geometric GO relationship and compared predictive correlations in simulations and data, not this conditional analytical distribution. Capblancq et al. (2026) study generalized selection gradients; their available abstract does not provide the present distribution, although their complete article was not inspected.

The ratio-of-normals/Cauchy identity and Gaussian quadratic-form identities are classical mathematical tools, not claimed as new. An equivalent abstract angular-Gaussian ratio calculation could exist outside the inspected ecological-genomics literature.

## Limitations

This is a two-dimensional, single-trait theorem with positive-definite \(C_b\) and \(\Sigma_x\), independent centered Gaussian allelic effects, and no direct environmental effects. It concerns population *conditional mean negative log-relative fitness*, not measured survival, actual finite-environment training statistics, or absolute population fitness. Non-Gaussian genetic architectures, correlated genetic effects, direct environment-to-trait effects, and more than two environmental variables require new calculations. The exact law is conditional on fixed GEA coefficients. The proof establishes no new validity claim for genomic-offset inference under empirical confounding, and its novel application to predictive-reliability calibration should not be conflated with novelty of its elementary probability identities.

## References

1. O. François, *Predicting fitness from genomic offset: a multivariate latent-trait framework*, arXiv:2611.09748v1, first publicly released 2026-11-06. https://arxiv.org/html/2611.09748v1 (Sections 2, 3.3, 4.4, and Equations (3.7), (4.19), (4.20)).
2. C. Gain et al., *A Quantitative Theory for Genomic Offset Statistics*, Molecular Biology and Evolution 40(6), msad140 (2023). https://doi.org/10.1093/molbev/msad140.
3. T. Capblancq et al., *Linking Genomic Offset Statistics to the Shape of Selection Gradients*, The American Naturalist 207(3), 356–367 (2026). https://doi.org/10.1086/739079 (abstract and metadata inspected; full article inaccessible at assessment).
