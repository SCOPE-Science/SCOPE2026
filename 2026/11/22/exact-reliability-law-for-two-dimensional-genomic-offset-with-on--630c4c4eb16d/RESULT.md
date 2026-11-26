# Mean and median genomic-offset reliability separate at large anisotropy

## Finding

In the two-dimensional Gaussian, single-trait model specified below, let \(X_\kappa\) be the squared population correlation of genomic offset with conditional mean negative log-relative fitness. The spectral ratio \(\kappa\) is the ratio of the larger and smaller eigenvalues of the environment-whitened genomic-offset metric. The mean over Gaussian allelic effects and the unique median both rise strictly for \(\kappa>1\), but their deficits from perfect correlation have different rates:

\[
\begin{aligned}
\mathbb E_a X_\kappa
 &=\frac{(\kappa+1)^2-\tfrac32(\kappa+1)\sqrt\kappa}{\kappa^2+1},
& 1-\mathbb E_a X_\kappa &\sim \frac{3}{2\sqrt\kappa},\\
\operatorname{median}_a X_\kappa
 &=\frac{\kappa^2+1}{(\kappa+1)^2},
& 1-\operatorname{median}_a X_\kappa &\sim \frac2\kappa.
\end{aligned}
\]

At each fixed quantile level in \((0,1)\) the reliability deficit is of order \(\kappa^{-1}\), but the fraction of architectures with reliability below a fixed \(x\in(0,1)\) decays more slowly:
\[
\sqrt\kappa\,\Pr_a(X_\kappa\le x)\longrightarrow
\frac{2x^{1/4}}{\pi\sqrt{1-\sqrt x}}.
\]
These rare architectures contribute to the slower convergence of the ensemble mean. The distinct result is the quantitative separation of the mean and typical reliability scales in this model, not the exact distribution of a ratio of normal quadratic forms or its median by itself.

## Assumptions and scope

Let \(L\ge2\), fix vectors \(b_1,\ldots,b_L\in\mathbb R^2\), and suppose \(C_b=L^{-1}\sum_{\ell=1}^L b_\ell b_\ell^\top\) is positive definite. Independently of the architecture draw, take \(h\sim N(0,\Sigma_x)\) with \(\Sigma_x\) positive definite. The squared genomic-offset score is \(g(h)=h^\top C_bh\). For one adaptive trait with no direct environmental mismatch effect, take independent \(a_\ell\sim N(0,\sigma_a^2)\), \(\sigma_a>0\), and \(\beta=L^{-1/2}\sum_{\ell=1}^L b_\ell a_\ell\). Assume the conditional mean negative log-relative fitness is a constant plus a positive multiple of \((\beta^\top h)^2\). For fixed \(\beta\ne0\), set
\[
X_\kappa=\operatorname{Corr}_h^2\!\left(g(h),\,\mathbb E[-\log\omega(h)\mid h,\beta]\right),
\qquad A=\Sigma_x^{1/2}C_b\Sigma_x^{1/2},\qquad \kappa=\lambda_{\max}(A)/\lambda_{\min}(A).
\]
Probabilities and averages indexed by \(a\) are over allelic effects conditional on the fixed GEA vectors. This is not a law for realized relative fitness or empirical out-of-sample \(R^2\).

## Proof

**Gaussian quotient and known distributional input.** For a standard normal vector \(z\) and symmetric matrices \(M,N\), \(\operatorname{Cov}(z^\top Mz,z^\top Nz)=2\operatorname{tr}(MN)\). Whiten the environment and use \(w=\Sigma_x^{1/2}\beta\sim N(0,\sigma_a^2 A)\). With \(Q=(w^\top Aw)/(w^\top w)\), the covariance identity gives \(X_\kappa=Q^2/\operatorname{tr}(A^2)\); the event \(w=0\) is null. After a rotation and common rescaling take \(A=\operatorname{diag}(\kappa,1)\) and \(w=\sigma_a(\sqrt\kappa U,V)^\top\) for independent standard normals \(U,V\). Thus with \(T=(V/U)^2\),
\[
X_\kappa=\frac{1}{1+\kappa^2}\left(\frac{\kappa^2+T}{\kappa+T}\right)^2,
\qquad \Pr(T\le t)=\frac2\pi\arctan\sqrt t\quad(t\ge0).
\tag{1}
\]
The distribution of \(Q\) is a direct specialization of the known exact law for a ratio of normal quadratic forms: use the numerator matrix \(\operatorname{diag}(\kappa^2,1)\) and denominator matrix \(\operatorname{diag}(\kappa,1)\) on \((U,V)\). For \(\kappa>1\), the quotient decreases strictly from \(\kappa\) to \(1\) over \(0<T<\infty\), so \(X_\kappa\) lies strictly between \(1/(1+\kappa^2)\) and \(\kappa^2/(1+\kappa^2)\) almost surely. For thresholds strictly between these bounds, writing \(r=\sqrt{(1+\kappa^2)x}\), the event \(X_\kappa\le x\) is \(T\ge\kappa(\kappa-r)/(r-1)\). Its probability is \((2/\pi)\arctan\sqrt{(r-1)/(\kappa(\kappa-r))}\). The CDF is zero at and below the lower bound and one at and above the upper bound. At \(\kappa=1\), \(X_1=1/2\) deterministically.

**Exact ensemble mean and monotonicity.** The median of \(T\) is 1 and its distribution is strictly increasing on \((0,\infty)\), so the unique median of \(X_\kappa\) is obtained by setting \(T=1\) in (1). Its derivative in \(\kappa\) is \(2(\kappa-1)/(\kappa+1)^3\). To compute the mean, reduce the angle of \((U,V)\) to the first quadrant, where \(\theta\) is uniform on \([0,\pi/2]\). Set \(D_\theta=\kappa\cos^2\theta+\sin^2\theta\). The quotient in (1) is \(\kappa+1-\kappa/D_\theta\). For positive \(u,v\), the angle average of \((u\cos^2\theta+v\sin^2\theta)^{-1}\) is \((uv)^{-1/2}\) by the tangent substitution. Differentiating in \(u,v\) and adding the negatives of the two derivatives gives the average of the squared inverse. Setting \(u=\kappa,v=1\) yields \(\mathbb E(D_\theta^{-1})=\kappa^{-1/2}\) and \(\mathbb E(D_\theta^{-2})=(\kappa+1)/(2\kappa^{3/2})\). Expanding the squared quotient then gives the stated mean. Its derivative with \(t=\sqrt\kappa\) is
\[
\frac{(t^2-1)(3t^4-8t^3+12t^2-8t+3)}{4t(t^4+1)^2}.
\]
The quartic equals \(t^2[3(t+t^{-1})^2-8(t+t^{-1})+6]\), strictly positive since the polynomial in brackets is positive and increasing at arguments at least 2. The derivative is therefore positive for \(\kappa>1\).

**Deficit scales.** For each fixed \(T\in(0,\infty)\), (1) gives \(\kappa(1-X_\kappa)\to2T\), establishing the fixed-quantile scale, including the median. But \(\mathbb E T=\infty\), so pointwise expansion does not produce the mean deficit. Put \(u=|V/U|/\sqrt\kappa\); its density on \(u>0\) is \(2\sqrt\kappa/[\pi(1+\kappa u^2)]\). By (1),
\[
X_\kappa=\frac{(1+u^2/\kappa)^2}{(1+\kappa^{-2})(1+u^2)^2}
=(1+u^2)^{-2}+O(\kappa^{-1})
\]
uniformly in \(u\ge0\). For fixed \(x\in(0,1)\), the threshold for \(u\) tends to \(\sqrt{x^{-1/2}-1}>0\). The Cauchy tail at this threshold times \(\sqrt\kappa\) tends to \(2/(\pi\sqrt{x^{-1/2}-1})\), giving the stated rare-low probability. For the mean, the uniform error contributes \(o(1)\) after multiplication by \(\sqrt\kappa\). For the deficit \(1-(1+u^2)^{-2}\), dominated convergence under the rescaled densities gives
\[
\lim_{\kappa\to\infty}\sqrt\kappa\,\mathbb E_a(1-X_\kappa)
=\frac2\pi\int_0^\infty\frac{1-(1+u^2)^{-2}}{u^2}\,du
=\frac2\pi\int_0^\infty\frac{2+u^2}{(1+u^2)^2}\,du=\frac32.
\]
Indeed, \(\kappa/(1+\kappa u^2)\le1/u^2\) for \(u>0\) and the resulting bound is integrable at zero and infinity. The same limit follows by expanding the exact mean. This calculation identifies the orientations with \(|V/U|\) on the order of \(\sqrt\kappa\) as the source of the slower mean scale.

## Verification

The exact expressions give mean \(10/17\), median \(17/25\), and probability \(\Pr_a(X_4<1/2)=0.37337399348\ldots\) at \(\kappa=4\). The accompanying `verification/check.py` provides numerical consistency checks for the quotient representation, CDF, angular mean integral and median. The different scales and the monotonicity claims follow from the proof, not from simulated architectures.

## Relationship to prior work and limitations

François gives the underlying genomic-offset model, conditional quadratic-form reliability and spectral bounds [1, §§3.3 and 4.4]. Forchini's equations (3)–(6) and Theorem 3 [2] cover the exact finite-\(\kappa\) probability law by substitution; the arctangent form above is its elementary two-dimensional specialization. Neither the general Gaussian quotient law nor a deterministic spectral bound is claimed here as new. The precise anisotropy comparison is between the integrated ensemble deficit and a typical deficit, with the rare-orientation scaling explaining why a pointwise approximation cannot give that comparison. It is specific to two environmental dimensions, one adaptive trait, and the stated conditional Gaussian uncertainty model. It does not establish validity of genomic-offset estimation under empirical confounding, or reliability for realized fitness, direct environmental effects, or non-Gaussian ensembles. Priority of the anisotropy comparison beyond the available sources is not certified.

1. O. François, *Predicting fitness from genomic offset: a multivariate latent-trait framework*, arXiv:2611.09748v1, https://arxiv.org/html/2611.09748v1.
2. G. Forchini, *The Exact Cumulative Distribution Function of a Ratio of Quadratic Forms in Normal Variables, with Application to the AR(1) Model*, *Econometric Theory* 18(4), 823–852 (2002); working paper https://www.york.ac.uk/media/economics/documents/discussionpapers/2001/0102.pdf.
