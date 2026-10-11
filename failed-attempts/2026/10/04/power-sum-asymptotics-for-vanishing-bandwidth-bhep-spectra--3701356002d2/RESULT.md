# Power-sum asymptotics for vanishing-bandwidth BHEP spectra
## Finding
Fix \(d\in\mathbb{N}\). Let \(A_{\beta,d}\) be the covariance operator of the BHEP limiting null law, and let \((\lambda_j(\beta,d))_{j\ge1}\) be its positive eigenvalues, repeated with multiplicity. Put
\[
q=\frac{\sqrt{1+4\beta^2}-1}{\sqrt{1+4\beta^2}+1}.
\]
For every fixed integer \(r\ge2\), as \(\beta\to\infty\),
\[
\sum_{j\ge1}\lambda_j(\beta,d)^r
=\left\{\frac{(1-q)^r}{1-q^r}\right\}^{d}+O_{d,r}(\beta^{-dr})
\sim r^{-d}\beta^{-d(r-1)}.
\]

The limiting quadratic form has the representation
\[
T_\beta(d)=\sum_{j\ge1}\lambda_j(\beta,d)N_j^2,
\]
with independent \(N_j\sim N(0,1)\). Therefore, for
\[
W_{\beta,d}=\frac{T_\beta(d)-\mathbb E T_\beta(d)}{\sqrt{\operatorname{Var}(T_\beta(d))}},
\]
every fixed cumulant order \(r\ge3\) obeys
\[
\kappa_r(W_{\beta,d})
\sim
2^{(d+1)r/2-1}(r-1)!\,r^{-d}\,\beta^{-d(r-2)/2}.
\]
In particular,
\[
\kappa_3(W_{\beta,d})
\sim \frac{2^{3(d+1)/2}}{3^d}\beta^{-d/2},
\qquad
\kappa_4(W_{\beta,d})
\sim 12\beta^{-d}.
\]
Here \(\kappa_4(W_{\beta,d})\) is the excess kurtosis. The leading excess-kurtosis coefficient \(12\) is independent of dimension.

A quantitative companion to the known Gaussian limit is
\[
d_K(W_{\beta,d},N(0,1))=O_d(\beta^{-d/2}),
\]
obtained from the classical Berry--Esseen inequality for independent centered summands.

## Assumptions and scope
The dimension \(d\) and cumulant order \(r\) are fixed while \(\beta\to\infty\). The operator \(A_{\beta,d}\) and the limiting law \(T_\beta(d)\) are those of the BHEP normality test after taking the sample-size limit at fixed \(\beta\). The result does not justify replacing \(\beta\) by a diverging sequence in the original finite-sample statistic without a separate joint-limit argument.

The motivating spectral paper lists \(62\mathrm{H}15\) as a primary MSC2020 classification. Its first public version is arXiv:2609.28464v1, posted 2026-09-23.

## Proof
Let \(B_{\beta,d}\) denote the Gaussian integral operator in the Henze--Wagner decomposition. The complete spectral analysis gives the exact eigenvalues
\[
c_\beta q^{|\nu|},\qquad \nu\in\mathbb N_0^d,
\qquad c_\beta=(1-q)^d,
\]
for \(B_{\beta,d}\). Hence for every integer \(r\ge2\),
\[
\operatorname{tr}(B_{\beta,d}^r)
=c_\beta^r\sum_{\nu\in\mathbb N_0^d}q^{r|\nu|}
=\frac{(1-q)^{dr}}{(1-q^r)^d}
=\left\{\frac{(1-q)^r}{1-q^r}\right\}^{d}.
\]
Since \(1-q\sim\beta^{-1}\) and \((1-q^r)/(1-q)\to r\),
\[
\operatorname{tr}(B_{\beta,d}^r)
\sim r^{-d}\beta^{-d(r-1)}.
\]

The same paper gives an exact finite-rank decomposition
\[
A_{\beta,d}=B_{\beta,d}-R_{\beta,d},
\]
where \(R_{\beta,d}\) is a finite sum of positive rank-one operators. Thus \(R_{\beta,d}\ge0\), \(0\le A_{\beta,d}\le B_{\beta,d}\), and
\[
\|R_{\beta,d}\|_1
=\operatorname{tr}(R_{\beta,d})
=1-\operatorname{tr}(A_{\beta,d})
=O_d(\beta^{-d}).
\]
Also
\[
\|A_{\beta,d}\|\le\|B_{\beta,d}\|=c_\beta=O_d(\beta^{-d}).
\]
The noncommutative telescoping identity gives
\[
B_{\beta,d}^r-A_{\beta,d}^r
=\sum_{k=0}^{r-1}B_{\beta,d}^{r-1-k}R_{\beta,d}A_{\beta,d}^{k}.
\]
Using \(|\operatorname{tr}(XYZ)|\le\|X\|\,\|Z\|\,\|Y\|_1\) when \(Y\) is trace class,
\[
\left|\operatorname{tr}(B_{\beta,d}^r)-\operatorname{tr}(A_{\beta,d}^r)\right|
\le r\|B_{\beta,d}\|^{r-1}\|R_{\beta,d}\|_1
=O_{d,r}(\beta^{-dr}).
\]
Since \(A_{\beta,d}\) is nonnegative and trace class,
\[
\operatorname{tr}(A_{\beta,d}^r)=\sum_{j\ge1}\lambda_j(\beta,d)^r,
\]
which proves the power-sum expansion.

For the quadratic form, independence of the standard normals gives
\[
\kappa_r\{T_\beta(d)\}=2^{r-1}(r-1)!\sum_{j\ge1}\lambda_j(\beta,d)^r.
\]
At \(r=2\), the power-sum result gives
\[
\operatorname{Var}\{T_\beta(d)\}=2\sum_j\lambda_j^2
\sim 2^{1-d}\beta^{-d},
\]
in agreement with the variance asymptotic already established in the motivating paper. Dividing the general cumulant asymptotic by the \(r/2\)-th power of this variance yields
\[
\kappa_r(W_{\beta,d})
\sim
2^{(d+1)r/2-1}(r-1)!\,r^{-d}\beta^{-d(r-2)/2}.
\]

Finally write \(X_j=\lambda_j(\beta,d)(N_j^2-1)\). For a finite truncation, Berry--Esseen gives
\[
d_K\le C_{\mathrm{BE}}\,
\frac{\mathbb E|N_1^2-1|^3\sum_j\lambda_j^3}
{\{2\sum_j\lambda_j^2\}^{3/2}}.
\]
Passing to the infinite series by \(L^2\) truncation is valid because the variance tails vanish. The power-sum laws for orders two and three make the ratio \(O_d(\beta^{-d/2})\), proving the stated rate.

## Verification
The proof was checked at the operator level rather than by finite spectral truncation. The two critical source identities are the Gaussian Mercer spectrum of \(B_{\beta,d}\) and the positive finite-rank decomposition \(A_{\beta,d}=B_{\beta,d}-R_{\beta,d}\). The source trace formula independently gives \(\operatorname{tr}(R_{\beta,d})=O_d(\beta^{-d})\), and the \(r=2\) specialization reproduces the published variance asymptotic \(\operatorname{tr}(A_{\beta,d}^2)\sim2^{-d}\beta^{-d}\).

The constants were algebraically cross-checked from
\[
\kappa_r(W_{\beta,d})
\sim
2^{(d+1)r/2-1}(r-1)!\,r^{-d}\beta^{-d(r-2)/2}.
\]
At \(r=4\) this simplifies exactly to \(12\beta^{-d}\), independent of \(d\).

## Relationship to prior work
Ebner, Edelmann, Henze, Ouimet and Richards determine the complete BHEP spectrum and prove the vanishing-bandwidth Gaussian limit. Their argument gives the exact mean, the variance asymptotic
\[
\operatorname{tr}(A_{\beta,d}^{2})\sim2^{-d}\beta^{-d},
\]
and a Lyapunov condition based on the largest eigenvalue. The paper does not state the fixed-order power-sum law above, the resulting all-order standardized cumulant hierarchy, or a Berry--Esseen rate.

Henze and Wagner give closed forms for the first three cumulants at arbitrary fixed \(d\) and \(\beta\). A later preprint by Ebner and Henze, first posted 2026-09-28, gives a closed form for the fourth cumulant and four-moment approximations. That later work states the general identity between cumulants and spectral power sums but does not state the \(\beta\to\infty\) all-fixed-order power-sum asymptotic or the Berry--Esseen rate derived here. In particular, the individual skewness and kurtosis asymptotics can be recovered by asymptotically expanding known low-order formulas, so the originality claim is the unified fixed-order spectral law and its quantitative Gaussianization consequence, not ownership of the low-order cumulant formulas themselves.

## Limitations
The result is asymptotic for each fixed \(d\) and fixed \(r\); it is not uniform in growing dimension or growing cumulant order. The Berry--Esseen statement is an upper rate only and is not claimed sharp. No finite-sample statement for \(T_{n,\beta_n}\) is proved. A more general trace-ideal perturbation theorem could subsume the operator comparison abstractly, although the BHEP constants and the resulting cumulant hierarchy would still require the specific Gaussian Mercer spectrum.

## References
1. B. Ebner, D. Edelmann, N. Henze, F. Ouimet and D. Richards, *The Spectra of the Henze--Zirkler and Henze--Wagner Operators for BHEP Tests*, arXiv:2609.28464v1, first public 2026-09-23.
2. N. Henze and T. Wagner, *A New Approach to the BHEP Tests for Multivariate Normality*, Journal of Multivariate Analysis 62 (1997), 1--23, DOI 10.1006/jmva.1997.1684.
3. B. Ebner and N. Henze, *Four-Moment Approximations and Fast p-Values for BHEP Tests of Multivariate Normality*, arXiv:2609.35037v1, first public 2026-09-28.
