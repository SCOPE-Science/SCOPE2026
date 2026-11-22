# Critical Poisson shot-noise calibration of high-concentration spherical uniformity tests

## Finding

For each fixed integer \(q\geq1\), the Poisson-kernel uniformity test on the unit sphere \(\mathbb S^q\) has a non-Gaussian, jointly coupled null limit when its smoothing parameter approaches one on the close-pair scale \(n^{-2/q}\). This limit has an exact covariance and universal log-bandwidth correlation, and it interpolates between a rare-collision boundary and a Gaussian limit. The claim is about a *triangular* tuning regime; it does not replace fixed-parameter asymptotics.

Let \(X_1,\ldots,X_n\) be independent area-uniform points on \(\mathbb S^q\), \(n\geq2\), and let \(\theta_{ij}=\arccos(X_i\cdot X_j)\). For \(0<\rho<1\), set
\[
P_\rho(\theta)=\frac{1-\rho^2}{(1-2\rho\cos\theta+\rho^2)^{(q+1)/2}},\qquad
T_n(\rho)=\frac2n\sum_{i<j}\big(P_\rho(\theta_{ij})-1\big).
\]
For every fixed \(c>0\), take \(\rho_n(c)=1-cn^{-2/q}\) (with \(n\) large enough that \(0<\rho_n(c)<1\)) and \(Y_n(c)=T_n(\rho_n(c))/n\).

Define \(a_q=\Gamma((q+1)/2)/(\sqrt\pi\,\Gamma(q/2))\), and let \(\Pi_q\) be a Poisson random measure on \((0,\infty)\) with intensity \(\mu_q(ds)=\tfrac12a_qs^{q-1}\,ds\). The random variables
\[
Z_q(c)=4c\int_0^\infty\frac{\Pi_q(ds)}{(c^2+s^2)^{(q+1)/2}}-1
\]
are defined simultaneously from the same random measure; the integral is finite almost surely. For any fixed finite collection \(c_1,\ldots,c_m>0\),
\[
\big(Y_n(c_1),\ldots,Y_n(c_m)\big)
\ \xrightarrow{\ d\ }\
\big(Z_q(c_1),\ldots,Z_q(c_m)\big).
\]

The exact finite-sample and limiting covariance formulas are
\[
\operatorname{Cov}(T_n(\rho),T_n(\sigma))
=\frac{2(n-1)}n\left(\frac{1+\rho\sigma}{(1-\rho\sigma)^q}-1\right),
\qquad
\operatorname{Cov}(Z_q(c),Z_q(d))=\frac4{(c+d)^q}.
\]
Consequently,
\[
\operatorname{Var}(Z_q(c))=\frac4{(2c)^q},\qquad
\operatorname{Corr}(Z_q(c),Z_q(d))
=\left(\frac{2\sqrt{cd}}{c+d}\right)^q
=\operatorname{sech}^{q}\!\left(\frac{\log(c/d)}2\right).
\]
In particular the standardized covariance depends only on the ratio of the two tuning scales, not their absolute levels.

Every marginal is centered, has all finite exponential moments, and is strictly non-Gaussian. For each integer \(k\geq2\) its cumulant is
\[
\kappa_k(Z_q(c))=
4^{k-1}a_q
B\!\left(\frac q2,\frac{k(q+1)-q}2\right)c^{-q(k-1)}.
\]
Its third cumulant is strictly positive. Coupling over all \(c>0\) using the same \(\Pi_q\) yields \(Z_q(c)\to-1\) almost surely as \(c\downarrow0\), whereas
\[
\frac{Z_q(c)}{2^{1-q/2}c^{-q/2}}\xrightarrow[c\to\infty]{\ d\ }N(0,1).
\]
These last two conclusions are *iterated* bandwidth limits of the displayed shot-noise process, not simultaneous joint-\(n\)-bandwidth assertions.

## Assumptions and scope

The null is exactly area-uniform iid sampling; the sphere dimension \(q\) is a fixed positive integer. The statistic is the centered off-diagonal U-statistic normalization displayed above (equivalently the Poisson-kernel statistic of Fernández-de-Marcos and García-Portugués). The parameter \(c\) is fixed and positive during sample-size convergence, with finitely many \(c\)'s for joint convergence. All statements concern the null and are not test-power statements. The primary mathematical subject is goodness-of-fit testing (MSC2020 \(62G10\)). The motivating source was first publicly available on 2023-04-10 as arXiv:2304.04519; publication or revision dates are not substituted for that date.

## Proof

**1. Rare distances form a Poisson point process.** Put \(b_n=n^{-2/q}\) and \(\Xi_n=\sum_{i<j}\delta_{\theta_{ij}/b_n}\). A pairwise angle has density \(a_q\sin^{q-1}\theta\) on \((0,\pi)\), hence for bounded \(0<u<v\) the expected number of atoms in \((u,v]\) tends to \(\tfrac12a_q\int_u^v s^{q-1}ds\). To establish joint factorial moments of atom counts in disjoint bounded intervals, expand them over ordered lists of distinct sample edges. Lists consisting of disjoint edges contribute the products of those limiting means, because distinct pairs use disjoint independent sample points. For an edge pattern with \(v\) vertices and \(r\) connected components, all edges being at most \(Lb_n\) forces each new vertex in a spanning forest into a cap of probability \(O(b_n^q)=O(n^{-2})\); the pattern contributes at most \(O(n^{v-2(v-r)})=O(n^{2r-v})\). If any component has more than two vertices then \(v>2r\) and the contribution vanishes. This proves joint Poisson convergence on bounded sets, and hence \(\Xi_n\Rightarrow\Pi_q\) vaguely.

**2. Pass from a point process to its unbounded-support shot noise.** Since \(\rho_n(c)=1-cb_n\), for every fixed \(s\geq0\),
\[
\frac2{n^2}P_{\rho_n(c)}(b_ns)
\longrightarrow\frac{4c}{(c^2+s^2)^{(q+1)/2}},
\]
uniformly for \(s\) in compact intervals. For \(\theta\in[0,\pi]\), \(1-\cos\theta\geq2\theta^2/\pi^2\) implies the uniform bound
\[
P_{\rho_n(c)}(\theta)\leq C_{q,c}\frac{b_n}{(b_n^2+\theta^2)^{(q+1)/2}}
\]
for large \(n\). The expected contribution to \((2/n^2)\sum_{i<j}P_{\rho_n(c)}\) of distances larger than \(Lb_n\) is at most
\[
C'_{q,c}\int_L^\infty \frac{s^{q-1}}{(1+s^2)^{(q+1)/2}}ds=O_{q,c}(L^{-1}).
\]
The limiting Poisson integral has the same integrable tail bound. Truncation at \(L\), the continuous mapping theorem for the atom integrals, and then \(L\to\infty\) establish joint convergence, using a common \(\Xi_n\) for every tuning scale. Finally, \(Y_n(c)=(2/n^2)\sum_{i<j}P_{\rho_n(c)}-(n-1)/n\), giving the stated shift by minus one.

**3. Means, covariances and cumulants.** The convolution semigroup identity for the spherical Poisson kernel implies
\[
\mathbb E P_\rho(\theta_{12})=1,\qquad
\mathbb E[P_\rho(\theta_{12})P_\sigma(\theta_{12})]
=P_{\rho\sigma}(0)=\frac{1+\rho\sigma}{(1-\rho\sigma)^q}.
\]
Different unordered edges are uncorrelated even if they share one endpoint, by conditional centering and rotation invariance. Summing diagonal covariance terms gives the finite-sample formula. Divide that formula by \(n^2\), set \(\rho=1-cn^{-2/q}\), \(\sigma=1-dn^{-2/q}\), and pass to the limit to obtain \(4/(c+d)^q\). Independently, the Poisson integral has covariance \(\int h_c(s)h_d(s)\mu_q(ds)\), with \(h_c(s)=4c(c^2+s^2)^{-(q+1)/2}\). Its mean equals \(\int h_c\,d\mu_q=1\) by the beta integral. The Poisson Laplace functional gives, for real \(t\),
\[
\log\mathbb E\exp(tZ_q(c))=-t+\int_0^\infty\big(e^{t h_c(s)}-1\big)\mu_q(ds).
\]
This is finite for every real \(t\). Differentiation yields the asserted beta-function cumulants, and strict positivity of the third cumulant excludes Gaussianity.

**4. Two bandwidth endpoints.** A Poisson realization has an almost surely positive smallest atom and \(\sum_{s\in\Pi_q,\,s>\varepsilon}s^{-(q+1)}<\infty\) for each \(\varepsilon>0\); dominated convergence on that realization gives \(\int h_c\,d\Pi_q\to0\) as \(c\downarrow0\). For \(c\to\infty\), the maximal jump of \(Z_q(c)\) is \(4c^{-q}\), while its standard deviation is \(2^{1-q/2}c^{-q/2}\). Their ratio goes to zero. Expanding the Poisson characteristic exponent to order two gives a standard normal limit, since the Taylor remainder is bounded by the maximum normalized jump times the unit normalized variance.

## Verification

The standalone `check.py` verifies the spherical Poisson-kernel semigroup integral, kernel normalization, the shot-noise cross-covariance, beta-function cumulants, convergence of finite-sample covariance, and the Poisson intensity and void probability of short pair distances. The supplied checker passed 202 numerical or algebraic assertions on dimensions \(1\leq q\leq6\) and several bandwidths, including direct angular quadratures and Monte Carlo for the rare-pair counts on \(\mathbb S^1\) and \(\mathbb S^2\). These finite checks are auxiliary: Steps 1–4 give the proof for all fixed positive integer dimensions and tuning parameters.

Run from the extracted directory with `python check.py` (requires Python, NumPy and SciPy); all random trials use a fixed seed. The entire analytic proof does not rely on simulations.

## Relationship to prior work

Fernández-de-Marcos and García-Portugués (2023), arXiv:2304.04519, define the Poisson-kernel statistic, prove its fixed-tuning-parameter null asymptotic chi-squared series, and provide its exact null variance. Their displayed regime holds the kernel parameter fixed when \(n\to\infty\). Ding, Markatou and Saraceno (Statistica Sinica, 2025; 2022-numbered preprint) give the spherical Poisson kernel's eigendecomposition and fixed-parameter calibration using U- and V-statistics. Both provide useful kernel identities but neither inspected analysis establishes the joint \(n^{-2/q}\) critical-window shot-noise limit. Their finite-\(n\) covariance machinery is consistent with the variance obtained here.

Poisson limits for close interpoint distances are classical (e.g. Silverman and Brown 1978; Brown and Silverman 1979). The rare-distance point-process ingredient is thus not claimed as independently new. The contribution is its all-dimension singular Poisson-kernel U-statistic consequence, including control of the noncompact kernel tail, exact joint dependence in the critical window, an explicit non-Gaussian calibration law and the two sequential bandwidth transitions. The 2010 Pycke paper treats a related circular Poisson-kernel uniformity test at fixed tuning and provides historical context; its complete paywalled text was not independently available in this inspection.

## Limitations

The proof fixes \(q\) as the sample size grows. It does not cover growing dimension, arbitrary simultaneous regimes \(c=c_n\to0\) or \(\infty\), nonuniform alternatives, parameter estimation, optimal power, or finite-sample error bounds. The limit has a non-Gaussian distribution for each fixed positive \(c\), so fixed-parameter Gaussian or weighted-chi-squared calibration should not be transferred to this critical window without justification. General geometric U-statistic theorems may subsume the distance point-process ingredient, and additional uninspected historical work could cover an equivalent singular-kernel application.

## References

1. A. Fernández-de-Marcos and E. García-Portugués, *On new omnibus tests of uniformity on the hypersphere*, arXiv:2304.04519 (first posted 2023-04-10), https://arxiv.org/abs/2304.04519; *TEST* 32 (2023), 1508–1529, DOI:10.1007/s11749-023-00882-x.
2. Y. Ding, M. Markatou and G. Saraceno, *Poisson kernel-based tests for uniformity on the d-dimensional sphere*, *Statistica Sinica* 35 (2025), 1947–1969, DOI:10.5705/ss.202022.0347, publicly accessible preprint https://www3.stat.sinica.edu.tw/preprint/SS-2022-0347_Preprint.pdf.
3. J.-R. Pycke, *Some tests for uniformity of circular distributions powerful against multimodal alternatives*, *Canadian Journal of Statistics* 38 (2010), 80–96, DOI:10.1002/cjs.10048.
4. B. W. Silverman and T. C. Brown, *Short distances, flat triangles and Poisson limits*, *Journal of Applied Probability* 15 (1978), 815–825, DOI:10.2307/3213436.
5. T. C. Brown and B. W. Silverman, *Rates of Poisson convergence for U-statistics*, *Journal of Applied Probability* 16 (1979), 428–432, DOI:10.2307/3212911.
