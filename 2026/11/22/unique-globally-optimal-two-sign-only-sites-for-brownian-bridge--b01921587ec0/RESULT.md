# Unique globally optimal two sign-only sites for Brownian-bridge integral quadrature

## Finding
Let \(B\) be the standard centered Brownian bridge on \([0,1]\), with covariance \(K(s,t)=\min(s,t)-st\), and let \(J=\int_0^1 B_u\,du\). Fix two observation times \(0\le s\le t\le1\) before observing the path. The only reported values are the one-bit signs \(S_s=\operatorname{sgn}(B_s)\) and \(S_t=\operatorname{sgn}(B_t)\); no sample magnitudes are reported. Estimate \(J\) by its conditional mean given these two bits, and measure unconditional squared-error Bayes risk \(R(s,t)=\mathbb E[(J-\mathbb E[J\mid S_s,S_t])^2]\).

Among **all deterministic, nonadaptive two-site choices** in the closed square, the unique optimum up to exchanging the two sites is
\[
(s_*,t_*)=\left(\frac{\rho_*}{1+\rho_*},\frac{1}{1+\rho_*}\right)
=(0.35038006274637545569\ldots,\;0.64961993725362454431\ldots),
\]
where \(\rho_*\in(0,1)\) is the unique solution of
\[
\left(\frac\pi2+\arcsin\rho\right)(1-\rho)^{3/2}
=\rho\sqrt{1+\rho},
\qquad \rho_*=0.53936162154700019653\ldots.
\]
The exact maximum explained variance, its complement Bayes risk, and the fraction of integral variance recovered are
\[
V_* =\frac{\rho_*}{\pi(1+\rho_*)^2[1+\tfrac2\pi\arcsin\rho_*]}
=0.05316900652043648255\ldots,
\]
\[
R_* =\frac1{12}-V_*=0.03016432681289685079\ldots,
\qquad \frac{V_*}{\operatorname{Var}J}=12V_*=0.63802807824523779056\ldots.
\]
A single optimal sign reports only \(3/(2\pi)=0.4774648292\ldots\) of integral variance, whereas optimally placed full-precision two-site observations report \(8/9\) of the variance. The two-sign placement is **not** an assertion of optimality among arbitrary binary encoders, adjustable threshold queries, adaptive policies, or full-valued samples.

## Assumptions and scope
The bridge is a centered Gaussian process with zero endpoints and the displayed covariance normalization; hence \(\operatorname{Var}J=1/12\). Both sensors are chosen deterministically before measuring the path. A sensor reports only the sign at its prescribed time. At a deterministic pinned endpoint the report is uninformative, and two coincident sites report only one nontrivial bit. The decision loss is the mean square error of the exact Bayes conditional-mean decoder, averaged over the bridge. Observation bits are neither flipped nor contaminated with noise. Times are compared on the entire closed domain, including duplicated sites and endpoints.

## Proof
**1. Exact two-bit risk.** For interior distinct times \(0<s<t<1\), set
\[
\rho=\sqrt{\frac{s(1-t)}{t(1-s)}}\in(0,1),\quad
c=\frac2\pi\arcsin\rho,\quad
 a=\frac{\sqrt{s(1-s)}}2,\quad b=\frac{\sqrt{t(1-t)}}2.
\]
Direct covariance integration gives \(\operatorname{Cov}(J,B_s)=s(1-s)/2\), so Gaussian regression yields \(\mathbb E[J S_s]=\sqrt{2/\pi}\,a\), and likewise at \(t\). The exact bivariate Gaussian sign identity gives \(\mathbb E[S_s S_t]=c\) and \(\mathbb E[S_s]=\mathbb E[S_t]=0\). Global sign reversal leaves the joint Gaussian law invariant and sends \((J,S_s,S_t)\) to \((-J,-S_s,-S_t)\). Since all four sign pairs have strictly positive probabilities, the conditional mean \(\mathbb E[J\mid S_s,S_t]\), an odd function on the four-element sign square, **must be of the form** \(\alpha S_s+\beta S_t\). Thus regression on both signs is the *exact* Bayes decoder, not merely a linear surrogate. Inverting the \(2\times2\) sign covariance gives
\[
\operatorname{Var}(\mathbb E[J\mid S_s,S_t])
=V(s,t)=\frac2\pi\frac{a^2+b^2-2cab}{1-c^2},\quad R(s,t)=\frac1{12}-V(s,t).\tag{1}
\]

**2. Separate correlation from midpoint asymmetry.** Introduce logit coordinates \(u=\log(s/(1-s))\), \(v=\log(t/(1-t))\); write \(\delta=(v-u)/2=-\log\rho>0\) and \(z=(u+v)/2\). Put
\[
h=\sinh^2(\delta/2)=\frac{(1-\rho)^2}{4\rho},\qquad
w=\cosh^2(z/2)\ge1.
\]
Equality \(w=1\) holds if and only if \(u+v=0\), equivalently \(s+t=1\). Substituting \(a=[4\cosh(u/2)]^{-1}\) and \(b=[4\cosh(v/2)]^{-1}\) into (1) gives the elementary rational identity
\[
V(\rho,w)=\frac{Lw-M}{4\pi(w+h)^2},\quad
L=\frac{1+2h-c}{1-c^2}>0,\qquad M=\frac{h(1+c)}{1-c^2}>0.\tag{2}
\]
Its derivative with respect to \(w\) has the sign of \(Lh+2M-Lw\). Consequently, at each fixed \(\rho\), the best unconstrained midpoint parameter is
\[
w_{\rm crit}=h\frac{3+2h+c}{1+2h-c},\tag{3}
\]
and the maximum over all \(w>0\) equals
\[
V(\rho,w)\le\frac{L^2}{16\pi(Lh+M)}.\tag{4}
\]

**3. For correlations at least one-third, only symmetric sites maximize.** For \(0<\rho<1\), strict convexity of the arcsine function between its endpoints gives \(c=(2/\pi)\arcsin\rho<\rho\). Formula (3) increases strictly with \(c\). Moreover the exact factorization
\[
1+2h-\rho-h(3+2h+\rho)
=\frac{(1-\rho)(1+\rho)^2(3\rho-1)}{8\rho^2}\ge0
\qquad(1/3\le\rho<1)
\]
implies \(w_{\rm crit}(c)<w_{\rm crit}(\rho)\le1\). Formula (2) is therefore strictly decreasing on \(w\ge1\). Thus, for every fixed \(\rho\ge1/3\), the unique best time pair is the reflected pair \(s=\rho/(1+\rho)\), \(t=1/(1+\rho)\).

**4. Correlations below one-third cannot be globally best.** The function \(q\mapsto\log\cosh(q)\) has derivative bounded in absolute value by one. Hence \(\min(a/b,b/a)\ge e^{-\delta}=\rho\). For fixed \(a,b>0\), differentiation in the sign correlation shows
\[
\frac{\partial}{\partial c}\left[\frac2\pi\frac{a^2+b^2-2cab}{1-c^2}\right]
=-\frac4\pi\frac{(a-cb)(b-ca)}{(1-c^2)^2}\le0
\qquad(0\le c\le\rho).
\]
Since \(c=(2/\pi)\arcsin\rho>(3/5)\rho\), replacing \(c\) in (2) by \(c_0=3\rho/5\) provides a strict upper bound on its value. Write \(L_0,M_0\) for (2)'s coefficients with \(c_0\) in place of \(c\). Applying (4), we obtain
\[
V(\rho,w)<\frac{L_0^2}{16\pi(L_0h+M_0)}<\frac1{6\pi}\qquad(0<\rho\le1/3),\tag{5}
\]
where the last strict inequality follows from the **exact identity**
\[
8(L_0h+M_0)-3L_0^2
=-\frac{25(6\rho^3-\rho^2-14\rho+5)(6\rho^3+\rho^2-14\rho-5)}{4\rho^2(3\rho-5)^2(3\rho+5)^2}>0.
\]
Indeed on \(0<\rho\le1/3\), the first cubic is at least \(2/9>0\) (using \(-\rho^2\ge-1/9\) and \(-14\rho\ge-14/3\)); the second cubic is negative because \(6\rho^3+\rho^2<1\) while \(-14\rho-5\le-5\). A symmetric pair with \(\rho=1/2\) attains \(V=1/(6\pi)\), so no design with correlation at most one-third can be globally optimal.

**5. Unique scalar optimum.** For reflected pairs the explained variance reduces to
\[
V_{\rm sym}(\rho)=\frac{\rho}{\pi(1+\rho)^2(1+\tfrac2\pi\arcsin\rho)}.\tag{6}
\]
Logarithmic differentiation shows that the sign of its derivative is the sign of \(Q(\rho)-1\), with
\[
Q(\rho)=\frac{(\frac\pi2+\arcsin\rho)(1-\rho)^{3/2}}{\rho\sqrt{1+\rho}}.
\]
This function decreases strictly from \(+\infty\) to zero on \((0,1)\). Indeed
\[
\frac{Q'(\rho)}{Q(\rho)}=
\frac{1}{\sqrt{1-\rho^2}(\pi/2+\arcsin\rho)}-
\frac{3}{2(1-\rho)}-\frac1\rho-\frac{1}{2(1+\rho)}<0,
\]
since \(\sqrt{1-\rho^2}(\pi/2+\arcsin\rho)>(1-\rho)\) (already \((\pi/2)\sqrt{1-\rho^2}\ge1-\rho\)). There is thus one critical point \(\rho_*\), necessarily the unique maximum of (6). Since (6) at \(\rho=1/2\) equals \(1/(6\pi)\), steps 3–4 prove this critical point is the **unique global** optimum among distinct interior placements.

**6. All remaining boundaries.** If sites coincide, one sign is repeated; an optimal single sign at \(s=1/2\) explains at most \(\max_s s(1-s)/(2\pi)=1/(8\pi)\). If one sensor is a pinned endpoint, only the other nontrivial sign remains, with the same bound; if both are pinned there is no information. This is strictly less than \(V_{\rm sym}(1/2)=1/(6\pi)\), so boundaries do not introduce additional optimizers. This completes the all-site proof.

## Verification
Run `python verify.py` with Python 3, NumPy, SciPy, SymPy, and mpmath from the directory containing the verifier; requirements are listed in `requirements.txt`. It establishes exact symbolic identities for the correlation-to-logit conversion, the derivative and both polynomial certificates. It independently rederives the explained variance through numerical Gaussian-quadrant integrals for six nonsymmetric and near-collision pairs. A deterministic 1,500-pair randomized check tests global comparisons, and 599 parameter values test inequalities; a 65-digit root solve verifies the stated decimal constants. The verifier's actual output is included as `verification_output.txt`.

The analytic Gaussian sign representation, inequalities, factorizations, monotonicity and boundary arguments—not any finite experiment—prove the infinite-domain optimizer statement. The numerical checks alone would not establish global uniqueness or historical originality.

## Relationship to prior work
Pronzato and Zhigljavsky (2018) treat Gaussian-process/kernel quadrature through energy minimization and real-valued sample evaluations; their framework does not determine an optimal **fixed pair of binary Gaussian sign measurements** for a bridge's integrated value. Foster, Lyons and Oberhauser (2019) study Brownian path approximations with polynomial information and integral-related Gaussian structure, not the stipulated sign-only two-site design. Guo and Kostina (2019) study causal rate-constrained *Wiener path reconstruction*, with a different target, sampling policy and loss. Fesl, Koller and Utschick (2022) analyze the exact conditional mean, Bussgang covariance formulas, and pilot design for one-bit-quantized Gaussian channel estimation: their general sign-estimation methodology encompasses ingredients of equation (1), but their pilot configuration and channel MSE objective do not specify or optimize two time locations in a pinned Brownian-bridge integral. A public result entitled *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature* optimizes a distribution of randomly selected **full-precision** bridge sites and the ensuing expected conditional variance, not two deterministic sign-only observations; its theorem and assumptions were compared directly. Another public result, *Noise-calibrated thresholds for two parallel binary location queries*, optimizes two noisy comparisons of one uniformly distributed unknown location, not a Gaussian bridge integral. The Gaussian quadrant and arcsine identities used here are established classical tools and are not new contributions.

The novel candidate is the explicit global binary-site optimizer with its proof excluding every asymmetric placement and the exact information fraction. Its novelty comparison is limited to the identifiable inspected literature, and no comprehensive historical-priority or independent mathematical review is claimed.

## Limitations
The result assumes exact sign reporting, a standard Brownian bridge with known Gaussian covariance, two fixed predetermined point observations, and the scalar signed integral with squared loss. Alternative binary thresholds, arbitrary one-bit encoders of site values, additive noise, bit flips, adaptively selected sites, non-Gaussian processes, nonlinear integral targets, and more than two bits are outside the proof. The numerical site coordinates are approximations to an analytically specified unique root. An overlooked earlier treatment of quantized Gaussian experimental design may affect historical priority; the presented statement is not independently validated.

## References
1. L. Pronzato and A. Zhigljavsky, *Bayesian quadrature and energy minimization for space-filling design*, arXiv:1808.10722v1, first public 2018-08-31; https://arxiv.org/abs/1808.10722.
2. J. Foster, T. Lyons and H. Oberhauser, *An optimal polynomial approximation of Brownian motion*, arXiv:1904.06998v1, first public 2019-04-15; https://arxiv.org/abs/1904.06998.
3. N. Guo and V. Kostina, *Optimal Causal Rate-Constrained Sampling of the Wiener Process*, arXiv:1909.01317v1, first public 2019-09-03; https://arxiv.org/abs/1909.01317.
4. *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature*, public result, 2026; https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-unique-optimal-i-i-d-two-node-design-for-brownian-bridge-kernel--1c7b05ec88c4/RESULT.md.
5. B. Fesl, M. Koller and W. Utschick, *On the Mean Square Error Optimal Estimator in One-Bit Quantized Systems*, arXiv:2212.04470v1, first public 2022-12-08; https://arxiv.org/abs/2212.04470.
6. *Noise-calibrated thresholds for two parallel binary location queries*, public result, 2026; https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-noise-calibrated-thresholds-for-two-parallel-binary-location-que--dedce94eaa8e/RESULT.md.
