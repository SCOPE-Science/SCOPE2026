# A three-regime Gaussian sketch risk law for one-spike matrices

## Finding

Let \(d\ge2\), \(1\le k<d\), and \(q\in\mathbb Z_{\ge0}\). On the one-spike positive-definite matrix \(A_\kappa=\operatorname{diag}(\kappa,1,\ldots,1)\) with \(\kappa\ge1\), a Gaussian randomized range finder with exactly \(k\) columns and \(q\) subspace-power steps has an **exact distribution** for its excess squared Frobenius residual over the optimal rank-\(k\) residual. Its strong-spike expected excess has three sharply distinct regimes, depending on whether \(k=1\), \(k=2\), or \(k\ge3\).

Specifically, draw \(\Omega\in\mathbb R^{d\times k}\) with independent standard-normal entries, set \(Y=(A_\kappa A_\kappa^\top)^qA_\kappa\Omega\), and let \(P\) be the orthogonal projection onto \(\operatorname{range}(Y)\). With independent \(U\sim\chi^2_k\) and \(V\sim\chi^2_{d-k}\), one has the following equality in distribution:

\[
\|A_\kappa-PA_\kappa\|_F^2
\ \stackrel{\mathrm d}{=}\ d-k+(\kappa^2-1)\frac{V}{V+\kappa^{4q+2}U}.
\]

Thus, writing \(\Delta_{d,k,q}(\kappa)=\mathbb E\|A_\kappa-PA_\kappa\|_F^2-(d-k)\), \(a=k/2\), \(b=(d-k)/2\), and \(t=\kappa^{4q+2}\),

\[
\Delta_{d,k,q}(\kappa)=\frac{\kappa^2-1}{B(a,b)}\int_0^1\frac{x^{a-1}(1-x)^b}{1+(t-1)x}\,dx
=\frac{(\kappa^2-1)(d-k)}d\,{}_2F_1\!\left(1,\frac{k}{2};\frac d2+1;1-t\right).
\]

For every fixed admissible \((d,k,q)\), the following *equivalences* hold as \(\kappa\to\infty\):

\[
\Delta_{d,k,q}(\kappa)\sim
\begin{cases}
\displaystyle\sqrt\pi\frac{\Gamma(d/2)}{\Gamma((d-1)/2)}\,\kappa^{1-2q},&k=1,\\[4pt]
\displaystyle(d-2)(2q+1)\,\kappa^{-4q}\log\kappa,&k=2,\\[4pt]
\displaystyle\frac{d-k}{k-2}\,\kappa^{-4q},&3\le k<d.
\end{cases}
\]

In particular, without power iteration (\(q=0\)), the expected excess diverges linearly for one sketch column, diverges logarithmically for two, and converges to a finite strictly positive constant for three or more. For every integer \(q\ge1\), the expected excess tends to zero in all three regimes, with the displayed sharp rate. For \(d=2\), \(k=1\), the exact formula simplifies to \(\Delta_{2,1,q}(\kappa)=(\kappa^2-1)/(1+\kappa^{2q+1})\), so the zero-power expected squared residual equals \(\kappa\) exactly.

## Assumptions and scope

The statement concerns a real, square, symmetric positive-definite **one-spike matrix**, standard real Gaussian independent test columns, exact arithmetic, and the unrecompressed rank-\(k\) orthogonal range-projection approximation \(PA_\kappa\). This is not a theorem about optimally truncating a larger sketch, about non-Gaussian sketches, or about the spectral norm or the unsquared Frobenius error. A \(q\)-step power sketch means exactly \(Y=(A_\kappa A_\kappa^\top)^q A_\kappa\Omega\); no normalization or finite-precision roundoff is modeled. Since \(A_\kappa\) has \(d-1\) unit singular values, the minimum squared Frobenius error of any rank-at-most-\(k\) approximation is exactly \(d-k\), including the case \(\kappa=1\).

## Proof

**1. Deterministic reduction.** Write \(s=2q+1\). Partition \(\Omega\) into its first row \(g\in\mathbb R^{1\times k}\) and remaining \(H\in\mathbb R^{(d-1)\times k}\). Then \(Y=[\kappa^s g;H]\). Almost surely \(H\) has full column rank because \(d-1\ge k\); put \(W=H^\top H\) and \(\gamma=gW^{-1}g^\top\). The Sherman--Morrison formula yields

\[
P_{11}=\kappa^{2s}g(W+\kappa^{2s}g^\top g)^{-1}g^\top
=\frac{\kappa^{2s}\gamma}{1+\kappa^{2s}\gamma}.
\]

As \(\operatorname{tr}P=k\), and \(A_\kappa^2=I+(\kappa^2-1)e_1e_1^\top\), orthogonality gives

\[
\|A_\kappa-PA_\kappa\|_F^2
=\operatorname{tr}[(I-P)A_\kappa^2]
=d-k+(\kappa^2-1)(1-P_{11})
=d-k+\frac{\kappa^2-1}{1+\kappa^{4q+2}\gamma}.
\]

**2. Exact Gaussian ratio.** By right-orthogonal invariance of \(H\), one may rotate coordinates so that \(g/\|g\|=e_1^\top\), without changing the distribution of \(H\). Denote the columns of this rotated \(H\) by \(h_1,\ldots,h_k\). The inverse Gram diagonal entry obeys the exact regression identity

\[
(W^{-1})_{11}
=\bigl\|(I-\Pi_{\operatorname{span}(h_2,\ldots,h_k)})h_1\bigr\|^{-2}.
\]

Conditionally on \(h_2,\ldots,h_k\), the orthocomplement has dimension \((d-1)-(k-1)=d-k\); hence its squared Gaussian residual norm \(V\) has the \(\chi^2_{d-k}\) law, independently of \(U=\|g\|^2\sim\chi^2_k\). Thus \(\gamma\stackrel{\mathrm d}{=}U/V\). Substituting into the deterministic identity proves the full distribution statement. The independence is genuine because \(g\) and \(H\) are independent, and the conditional residual law does not depend on the other columns.

**3. Exact expectation.** The ratio \(X=U/(U+V)\) has the \(\mathrm{Beta}(a,b)\) distribution, with \(a=k/2>0\) and \(b=(d-k)/2>0\). Then \(V/(V+tU)=(1-X)/(1+(t-1)X)\). Integrating against the beta density proves the integral formula; Euler's beta representation of \({}_2F_1\) yields the hypergeometric expression. For \(d=2\), \(k=1\), direct beta integration gives \(\mathbb E[V/(V+tU)]=1/(1+\sqrt t)\).

**4. Sharp large-spike asymptotics.** Define \(F_{a,b}(t)=\mathbb E[(1-X)/(1+(t-1)X)]\). For \(0<a<1\), the substitution \(y=tx\) and dominated convergence give

\[
\lim_{t\to\infty} t^aF_{a,b}(t)
=\frac1{B(a,b)}\int_0^\infty\frac{y^{a-1}}{1+y}\,dy
=\frac\pi{B(a,b)\sin(\pi a)}.
\]

Only the admissible value \(a=1/2\) is relevant, and elementary gamma simplification yields \(\sqrt\pi\,\Gamma(d/2)/\Gamma((d-1)/2)\). For \(a=1\), split the beta integral at a fixed small positive number, and compare the singular part with \(\int_0^1(1+(t-1)x)^{-1}\,dx\), obtaining \(F_{1,b}(t)\sim b\log(t)/t\). For \(a>1\), dominated convergence in the original beta expectation yields

\[
\lim_{t\to\infty}tF_{a,b}(t)
=\mathbb E[(1-X)/X]=b/(a-1)=(d-k)/(k-2).
\]

Finally multiply by \(\kappa^2-1\), use \(t=\kappa^{4q+2}\), and note \(\log t=(4q+2)\log\kappa\). These arguments are limits over the continuous parameter \(\kappa\to\infty\), not extrapolations from sampled matrices. They establish all three claimed sharp equivalences.

## Verification

A standalone numerical verifier in `verifier.py` reconstructs \(P\) from Gaussian sketches using QR factorization and checks the exact deterministic error reduction against direct squared Frobenius norms. It separately evaluates the beta integral and the hypergeometric formula, checks exact two-dimensional simplifications and the identity-matrix endpoint, and numerically checks the predicted sharp large-spike leading constants. With its recorded seed and dependencies (`numpy`, `mpmath`), the supplied run passed 460 assertions. The finite tests corroborate, but do not prove, the arbitrary-dimensional chi-square law or any asymptotic equivalence; those are established above.

## Relationship to prior work

The Gaussian range finder and power-sketch algorithm are established. Halko, Martinsson and Tropp, *Finding structure with randomness* (2011), Theorem 10.5, give expected Frobenius error bounds with oversampling; their theorem does not state this exact one-spike, all-sketch-size distribution and its sharp three-way large-spike risk constants. Witten and Candès, *Randomized algorithms for low-rank matrix factorizations: sharp performance bounds* (2013/2014), explicitly demonstrate a two-dimensional, single-column strong-spike blow-up and prove sharp worst-case spectral and Frobenius inequalities (including Theorem 1.5). Thus the qualitative one-column obstruction and the existence of bounded oversampled errors are **not new**; the present contribution is the exact all-\((d,k,q)\) spike-risk distribution and sharp phase classification, including the critical two-column logarithm and each power-iteration coefficient. Diouane and collaborators (2022) analyze related expected Frobenius bounds for nonstandard Gaussian sketches, not this exact beta law. Saibaba (2018) proves canonical-angle and subspace-iteration bounds subject to a target-rank spectral gap, which fails for this one-spike family when \(k\ge2\). Saibaba and Międlar (first circulated 2023) provide general distributional-class bounds for randomized subspace iteration with unspecified constants; their baseline Gaussian and subspace-power framework motivates isolating the exact minimal-column effect. The results do not imply a stronger general-matrix performance guarantee, nor do they improve the already available worst-case theorems. Relevant specialist prior work might contain an equivalent one-spike beta calculation and remains a precedence risk.

## Limitations

The model fixes one nonunit singular value, all other singular values exactly one, and fixed dimension/sketch size/power count while the spike diverges. This does not characterize arbitrary anisotropic spectra, high-dimensional simultaneous limits, nonsymmetric matrices, floating-point stability, or compressed rank-one truncation after a wider sketch. The power count changes the number of matrix multiplications; the three regimes are not equal-cost algorithm comparisons. No almost-sure asymptotic rate is claimed. The beta and gamma special functions describe exact expected squared error, not unsquared error. Originality is conditional on the inspected literature and mathematical record searches and is not an independent bibliographic certification.

## References

- A. K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814 (first public version August 10, 2023), https://arxiv.org/abs/2308.05814; SIAM Journal on Mathematics of Data Science 7 (2025), 136--162.
- N. Halko, P.-G. Martinsson and J. A. Tropp, *Finding structure with randomness: probabilistic algorithms for constructing approximate matrix decompositions*, SIAM Review 53 (2011), 217--288, https://arxiv.org/abs/0909.4061.
- R. Witten and E. J. Candès, *Randomized algorithms for low-rank matrix factorizations: sharp performance bounds*, 2013 preprint revised 2014, https://candes.su.domains/publications/downloads/RandomizedNLA.pdf.
- A. K. Saibaba, *Randomized subspace iteration: Analysis of canonical angles and unitarily invariant norms*, arXiv:1804.02614 (2018), https://arxiv.org/abs/1804.02614.
- Y. Diouane, S. Gürol, A. Scotto di Perrotolo and X. Vasseur, *A general error analysis for randomized low-rank approximation methods*, arXiv:2206.08793 (2022), https://arxiv.org/abs/2206.08793.
