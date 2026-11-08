# Exact mean advantage and a common non-Gaussian limit for circular facility lotteries

## Finding

Let \(n\ge3\) agents have independent, Haar-uniform locations \(X_1,\ldots,X_n\) on the circle \(\mathbb T=\mathbb R/\mathbb Z\), with geodesic distance \(d(x,y)=\min\{|x-y|,1-|x-y|\}\) for representatives in \([0,1)\). Consider the single-facility lotteries Random Dictator (RD), Proportional Circle Distance (PCD, odd \(n\)), its random-deletion extension (EPCD, even \(n\)), and the half-and-half mixture MRP of RD with PCD/EPCD. For each lottery \(M\), let \(C_n^M\) be its expected social cost **conditional on the observed agent locations** and let \(O_n=\min_{t\in\mathbb T}\sum_i d(X_i,t)\). Put \(R_n^M=C_n^M/O_n\), a.s. well defined.

**Exact unconditional gain.** Define \(s_n=n\) for odd \(n\), and \(s_n=n-1\) for even \(n\); then \(s_n\) is odd. For every \(n\ge3\),
\[
\mathbb E C_n^{\mathrm{RD}}=\frac{n-1}{4},\qquad
\mathbb E(C_n^{\mathrm{RD}}-C_n^{\mathrm{PCD/EPCD}})
=\Delta_n:=\frac14-\frac{1}{2^{s_n+1}}\binom{s_n}{(s_n-1)/2}>0,
\]
\[
\mathbb E(C_n^{\mathrm{RD}}-C_n^{\mathrm{MRP}})=\frac{\Delta_n}{2},\qquad
\Delta_n\longrightarrow\frac14.
\]
In particular, the odd-size gains at \(n=3,5,7\) equal \(1/16,3/32,29/256\), respectively. The even-size gain matches the preceding odd size.

**Joint, non-Gaussian typical approximation law.** Define a centered continuous Gaussian process \(G\) on \(\mathbb T\) with covariance, writing \(h=d(s,t)\in[0,1/2]\),
\[
\mathbb E[G(s)G(t)]=\frac1{48}-\frac{h^2}{2}+\frac{2h^3}{3}.
\]
An explicit version uses independent standard normal variables \(A_j,B_j\), with odd positive integers \(j\):
\[
G(t)=\frac{\sqrt2}{\pi^2}\sum_{\substack{j\ge1\\j\ \mathrm{odd}}}
\frac{A_j\cos(2\pi jt)+B_j\sin(2\pi jt)}{j^2}.
\]
The series converges absolutely and uniformly almost surely. On one probability space, compute all three conditional ratios from the **same** sample. As \(n\to\infty\), without restriction to odd or even subsequences,
\[
\boxed{\sqrt n\bigl(R_n^{\mathrm{RD}}-1,\ R_n^{\mathrm{PCD/EPCD}}-1,\ R_n^{\mathrm{MRP}}-1\bigr)
\ \Longrightarrow\ (Z,Z,Z),\qquad Z=4\sup_{t\in\mathbb T}G(t).}
\]
Here \(Z\) is finite, strictly positive almost surely, nondegenerate, and non-Gaussian. In particular all three approximation ratios tend to one in probability, but their common first nonzero \(n^{-1/2}\)-scale excess has a nonconstant law. Moreover \(\sqrt n(R_n^{\mathrm{RD}}-R_n^{\mathrm{PCD/EPCD}})\to0\) in probability.

## Assumptions and scope

Locations are independent and continuously uniform on a circle of circumference one. The assertion concerns conditional-on-reports *expected* mechanism cost, not a single realized facility draw. The optimum permits any point of the circle, rather than only reports. For odd \(n=2k+1\), write the clockwise reports as \(z_1,\ldots,z_n\) and the intervening clockwise gaps as \(g_i\), indices cyclic; PCD selects \(z_i\) with probability \(g_{i+k}\). For even \(n=2k\), EPCD selects \(z_i\) with probability \((g_{i+k-1}+g_{i+k})/2\), equivalently deleting one agent uniformly and then applying PCD to the remaining odd-sized profile. MRP chooses RD with probability \(1/2\) and the relevant PCD/EPCD rule otherwise. These mechanism definitions and their strategyproofness are prior results, not claimed anew here.

## Proof

**1. Exact mean for odd samples.** Fix \(n=2k+1\). RD independently chooses an observed location uniformly. Because the circle distance between two independent uniform locations has mean \(1/4\), the diagonal terms vanish and \(\mathbb E C_n^{\mathrm{RD}}=(n-1)/4=k/2\).

For the PCD mean, rotate the sample so that a uniformly chosen agent is the cyclic starting report. The other \(n-1\) relative points are independent uniform points, and the \(n\) circular gaps have the exchangeable \(\mathrm{Dirichlet}(1,\ldots,1)\) law. This random cyclic anchor is essential: anchoring at the smallest numerical report would not give exchangeable gaps. Let \(S_r\) be the clockwise displacement over \(r\) successive gaps from a fixed report, so \(S_r\sim\mathrm{Beta}(r,n-r)\). For \(1\le r\le k\), the opposing gap used to select that report is disjoint from the \(r\) gaps in \(S_r\). Conditional on \(S_r\), its mean is \((1-S_r)/(n-r)\). For \(k+1\le r\le 2k\), the opposing gap lies in the \(r\)-gap block, and, upon replacing \(r\) by \(n-r\) and \(S_r\) by \(1-S_r\), its expected contribution equals the matching first-half contribution. Thus by summing over cyclic reports and distances to other agents,
\[
\mathbb E C_n^{\mathrm{PCD}}
=2n\sum_{r=1}^k\frac{\mathbb E[(1-S_r)\min(S_r,1-S_r)]}{n-r}
=2\sum_{r=1}^k\mathbb E\min(V_{(r)},1-V_{(r)}),
\]
where \(V_{(r)}\) is the \(r\)-th order statistic of \(n\) independent uniforms on \([0,1]\). The second equality uses the elementary beta density tilt \((1-s)\mathrm{Beta}(r,n-r)/(n-r)=\mathrm{Beta}(r,n-r+1)/n\). Also \(2\sum_{r=1}^k \mathbb E V_{(r)}=k/2\). As \(v-\min(v,1-v)=2(v-1/2)_+\), the RD minus PCD mean is
\[
\Delta_n=4\sum_{r=1}^k\mathbb E(V_{(r)}-1/2)_+.
\]
Let \(B\sim\mathrm{Binomial}(n,1/2)\) count the observations not exceeding \(1/2\). Given \(B=b<k\), the first \(k-b\) order statistics above \(1/2\) are the first \(k-b\) of \(n-b\) independent uniforms on \((1/2,1)\); their expected total excess is \((k-b)(k-b+1)/(4(n-b+1))\). Therefore
\[
\Delta_n=2^{-n}\sum_{b=0}^{k-1}\binom nb\frac{(k-b)(k-b+1)}{n-b+1}.
\]
Using \(\binom nb/(n-b+1)=\binom{n+1}b/(n+1)\), let \(T\sim\mathrm{Binomial}(2k+2,1/2)\). The last display equals
\[
\frac1{k+1}\mathbb E\bigl[(k-T)_+(k-T+1)_+\bigr].
\]
Set \(H=|T-(k+1)|\). Binomial symmetry turns the preceding expression into \(\mathbb E[H(H-1)]/[2(k+1)]\), since \(H(H-1)=0\) for \(H=0,1\). Now \(\mathbb E H^2=\operatorname{Var}(T)=(k+1)/2\). The centered absolute first moment obeys
\[
\mathbb E H=(k+1)\binom{2k+2}{k+1}2^{-(2k+2)}.
\]
Indeed \((s-b)\binom{2s}b=s[\binom{2s-1}b-\binom{2s-1}{b-1}]\), whose sum over \(b<s\) telescopes; symmetry doubles the result. Consequently
\[
\Delta_n=\frac14-\frac12\binom{2k+2}{k+1}2^{-(2k+2)}
=\frac14-\binom{2k+1}k2^{-(2k+2)}.
\]
The central binomial probability is strictly less than \(1/2\) for \(n\ge3\), so the gain is positive. The central binomial estimate gives \(\Delta_n=1/4-(2\pi n)^{-1/2}+O(n^{-3/2})\).

**2. Even samples and mixtures.** For even \(n\), uniformly delete one agent, independently of its position, and apply PCD to the \(n-1\) remaining locations. The deletion leaves an independent uniform location, whose expected distance to whatever facility is selected from the survivors equals \(1/4\). Thus \(\mathbb E C_n^{\mathrm{EPCD}}=\mathbb E C_{n-1}^{\mathrm{PCD}}+1/4\), whereas \(\mathbb E C_n^{\mathrm{RD}}=\mathbb E C_{n-1}^{\mathrm{RD}}+1/4\). The exact gain is therefore \(\Delta_{n-1}\); linearity yields the half-gain for MRP.

**3. Uniform empirical-cost process.** Put \(F_n=n^{-1}\sum_i\delta_{X_i}\) and define
\[
H_n(t)=\sqrt n\left[\int d(x,t)\,dF_n(x)-\frac14\right].
\]
The finite-dimensional central limit theorem applies because the summands are bounded. For any arc coordinates \(s,t\) separated by \(\delta\), their centered single-observation increment has magnitude at most \(\delta\). The fourth-moment expansion of a sum of independent centered increments gives \(\mathbb E|H_n(t)-H_n(s)|^4\le4\delta^4\), uniformly in \(n\). Together with bounded pointwise fourth moments, the Kolmogorov tightness criterion gives \(H_n\Rightarrow G\) in \(C(\mathbb T)\). Direct circular integration of the centered triangular distance function gives the displayed covariance: for \(0\le h\le1/2\), \(\operatorname{Cov}(G(0),G(h))=1/48-h^2/2+2h^3/3\). Equivalently, its nonzero Fourier coefficients are \(-2/(\pi^2 j^2)\) at odd harmonics, yielding the stated Gaussian series.

The samplewise identities \(\int_\mathbb T H_n(t)\,dt=0\) and \(H_n(t+1/2)=-H_n(t)\) follow from \(\int d(x,t)\,dt=1/4\) and \(d(x,t+1/2)=1/2-d(x,t)\). They pass to \(G\). In particular \(\sup G=-\inf G\) and \(\sup G\ge|G(0)|>0\) almost surely, because \(\operatorname{Var}(G(0))=1/48\).

**4. Asymptotic uniformity of the facility lotteries.** Write \(\mu_n^M\) for the conditional distribution of the location chosen by mechanism \(M\). For RD, \(\mu_n^{\mathrm{RD}}=F_n\Rightarrow\mathrm{Haar}\) almost surely. To treat PCD/EPCD, let \(z_i\) be the sorted reports and \(g_i\) the gaps. Uniform empirical-quantile convergence implies \(\max_i g_i\to0\) and, for either parity, the points \(z_{i+\lfloor n/2\rfloor}\) are uniformly within vanishing circle distance of \(z_i+1/2\), almost surely. Reindexing the PCD formula yields for every continuous periodic test function \(h\)
\[
\int h\,d\mu_n^{\mathrm{PCD}}
=\sum_i g_{i+\lfloor n/2\rfloor}h(z_i)\longrightarrow
\int_\mathbb T h(t-1/2)\,dt=\int_\mathbb T h(t)\,dt.
\]
The RHS is the limit of Riemann sums based on the opposite gaps. For EPCD the average of two adjacent opposite-gap Riemann sums has the same limit. Therefore all three selection measures converge weakly to Haar almost surely, and MRP does as well.

Because \(H_n\) is tight in \(C(\mathbb T)\), asymptotic uniformity of these possibly sample-dependent measures implies
\[
\int H_n(t)\,d\mu_n^M(t)-\int H_n(t)\,dt=o_{\mathbb P}(1).
\]
To justify this use a compact equicontinuous set containing \(H_n\) with arbitrarily high probability; weak convergence of probability measures is uniform over that compact set by a finite uniform approximation. The Haar integral is zero. Hence jointly for the four lotteries,
\[
C_n^M=\frac n4+o_{\mathbb P}(\sqrt n),\qquad
O_n=\frac n4+\sqrt n\min_tH_n(t).
\]
Continuous mapping and expansion of the positive denominator imply \(\sqrt n(R_n^M-1)\Rightarrow-4\min G=4\sup G\), jointly, as claimed. The Gaussian supremum is finite by continuity and is non-Gaussian because it is nonconstant and supported on the positive half-line.

## Verification

The accompanying standalone standard-library checker `check.py` evaluates the exact binomial-absolute-moment and mean-gain identities with rational arithmetic for many odd sizes, verifies the explicit covariance by numerical integration, and independently samples both odd PCD and even EPCD cost profiles using the original opposing-gap formulas. Run `python3 check.py`. The analytic proof above establishes the infinite-sample result; finite simulations and numerical quadrature do not establish distributional convergence or novelty.

## Relationship to prior work

Meir (2019) introduced PCD and proved its strategic properties, primarily studying worst-case approximation guarantees. Rogowski and Dziubiński (2025) analyzed the half-and-half RD/PCD mechanism for odd populations and its worst-case bound. Chan, Lin, and Wang (2026) defined the even-population random-deletion extension and proved the \(3/2\) worst-case guarantee for the parity-dependent mixture. Those definitions and guarantees are assumed here, not newly derived. The present statement instead fixes Haar-uniform random agent positions and supplies a closed finite-population **unconditional cost advantage**, together with a **joint, non-Gaussian limit for conditional approximation ratios**. The distinct exact mean and fluctuation laws are not consequences of the cited worst-case bounds alone. Standard empirical-process convergence underlies one proof step; the mechanism-specific gap-law, mean identity, and convergence of PCD/EPCD selection measures provide the additional argument.

## Limitations

The location model is Haar-uniform on the circle; no theorem is asserted for nonuniform populations or discrete circles. The Gaussian-supremum law concerns conditional expected mechanism cost and is not the law of the cost of a randomly realized facility. The central-binomial improvement is an unconditional **difference in social-cost expectations**, not an exact expectation of the random approximation ratio. The Gaussian-supremum distribution is described by a convergent Fourier series rather than a closed elementary distribution function. No independent scientific validation has been performed. Although targeted literature comparisons did not identify equivalent exact laws, that search cannot establish absolute publication priority.

## References

1. R. Meir, *Strategyproof Facility Location for Three Agents on a Circle*, arXiv:1902.08070 (2019), https://arxiv.org/abs/1902.08070. Mechanism PCD, original strategyproofness and worst-case analysis.
2. K. Rogowski and M. Dziubiński, *Improved Approximation Ratio for Strategyproof Facility Location on a Cycle*, arXiv:2505.12943 (2025), https://arxiv.org/abs/2505.12943. Mixed RD/PCD and odd-population worst-case analysis.
3. H. Chan, J. Lin, and C. Wang, *A Randomized \(3/2\)-Approximation for Strategic Facility Location on a Circle*, arXiv:2609.12792v1 (first public September 11, 2026), https://arxiv.org/html/2609.12792v1. Definition of EPCD/MRP and general worst-case theorem.
