# An exact Gaussian-null MMD covariance kernel and its sharp high-dimensional bandwidth trichotomy

## Finding
Let \(d\ge1\) and \(n\ge2\) be integers, \(P_d=N_d(0,I_d)\), and \(X_1,\ldots,X_n\) be independent with law \(P_d\). For \(a>0\), put \(k_a(x,y)=\exp(-a\|x-y\|^2)\), \(m_a(x)=\mathbb E_{Y\sim P_d}k_a(x,Y)\), \(c_a=\mathbb E_{X,Y\sim P_d}k_a(X,Y)\), and \(h_a(x,y)=k_a(x,y)-m_a(x)-m_a(y)+c_a\). Define the unbiased, centered one-sample MMD-square statistic
\[
 U_{n,d}(a)=\frac{2}{n(n-1)}\sum_{1\le i<j\le n}h_a(X_i,X_j).
\]
For all \(a,b>0\), define
\[
 K_d(a,b)=[1+4(a+b)]^{-d/2}-2[1+4(a+b)+12ab]^{-d/2}+[1+4(a+b)+16ab]^{-d/2}.
\]
**Exact finite-sample result:**
\[
\mathbb EU_{n,d}(a)=0,\qquad\operatorname{Cov}(U_{n,d}(a),U_{n,d}(b))=\frac{2K_d(a,b)}{n(n-1)}.
\]
For each \(d\), \(K_d(a,b)>0\); its normalized correlation \(\rho_d(a,b)=K_d(a,b)/\sqrt{K_d(a,a)K_d(b,b)}\) belongs to \((0,1)\) if \(a\ne b\), equals one if \(a=b\), and is independent of \(n\).

**Sharp high-dimensional trichotomy:** Fix distinct \(u,v>0\), \(\alpha>0\), and set \(a_d=u d^{-\alpha}\), \(b_d=v d^{-\alpha}\). Then
\[
\begin{array}{lll}
0<\alpha<\tfrac12:&\displaystyle \log\rho_d(a_d,b_d)=-4(u-v)^2d^{1-2\alpha}(1+o(1)),&\rho_d\longrightarrow0;\\[3pt]
\alpha=\tfrac12:&\displaystyle \rho_d\longrightarrow e^{-4(u-v)^2}\frac{g(uv)}{\sqrt{g(u^2)g(v^2)}},&0<\lim\rho_d<1;\\[6pt]
\alpha>\tfrac12:&\displaystyle \rho_d\longrightarrow1,&
\end{array}
\]
where \(g(t)=1-2e^{-6t}+e^{-8t}>0\) for \(t>0\). The critical limit is strictly between zero and one for distinct positive \(u,v\). The regime \(\alpha=0\) (fixed unequal inverse-square bandwidths) also decorrelates exponentially, with the exact base given in the proof.

## Assumptions and scope
The Gaussian reference distribution is fully specified: its mean and covariance are **known**, not estimated. The sample size \(n\) can be any integer at least two, fixed or varying with dimension. Bandwidth \(a\) is the inverse-square scale of the kernel itself, not its usual standard-deviation parameter. Correlation refers to the null distribution of the unbiased one-sample MMD-square \(U_{n,d}\), which may take negative values. This is neither the two-sample MMD statistic nor a theorem about the distribution of a maximum over bandwidths.

## Proof
**1. Exact Gaussian integrals.** Completing the square gives
\[
m_a(x)=(1+2a)^{-d/2}\exp\!\left(-\frac{a\|x\|^2}{1+2a}\right),\qquad c_a=(1+4a)^{-d/2}.
\]
For independent \(X,Y,Z\sim P_d\), with \(A=1+4(a+b)\), \(B=A+12ab\), \(C=A+16ab\), independence and the Gaussian quadratic-form integral give
\[
\mathbb E[k_a(X,Y)k_b(X,Y)]=A^{-d/2},\quad
\mathbb E[k_a(X,Y)k_b(X,Z)]=B^{-d/2},\quad
\mathbb E[k_a(X,Y)]\mathbb E[k_b(X,Z)]=C^{-d/2}.
\]
For example, the middle expectation equals \(\mathbb E[m_a(X)m_b(X)]\), whose denominator after integrating \(X\) is
\[
(1+2a)(1+2b)+2a(1+2b)+2b(1+2a)=1+4(a+b)+12ab.
\]
Expanding the centered product therefore yields \(\mathbb E[h_a(X,Y)h_b(X,Y)]=K_d(a,b)\). Because \(\mathbb E[h_a(X,Y)\mid X]=\mathbb E[h_a(X,Y)\mid Y]=0\), pairs of summands with disjoint sample indices or with exactly one shared index have covariance zero. Only identical unordered index pairs survive. This proves the stated mean and finite-sample covariance for every \(d,n,a,b\).

**2. Strict correlation bounds.** Let \(f(t)=t^{-d/2}\). Since \(A<B<C\), \(B-A=12ab\), \(C-B=4ab\), and \(f\) is strictly convex and decreasing,
\[
f(A)-f(B)>3(f(B)-f(C)),\qquad K_d(a,b)>2(f(B)-f(C))>0.
\]
Cauchy-Schwarz gives \(\rho_d\le1\). Equality would force the continuous kernels \(h_a\) and \(h_b\) to be proportional everywhere because the Gaussian density is strictly positive. Their mixed four-point increments at \(x=y=0\), \(x'=y'=te_1\) are \(2(1-e^{-at^2})\) and \(2(1-e^{-bt^2})\). Proportionality for every \(t>0\) forces \(a=b\); hence \(0<\rho_d(a,b)<1\) for distinct bandwidths.

**3. Dimension-dependent covariance.** Write \(p=d/2\) and
\[
H_d(a,b)=1-2\left(1+\frac{12ab}{1+4(a+b)}\right)^{-p}
+\left(1+\frac{16ab}{1+4(a+b)}\right)^{-p}.
\]
Then \(K_d(a,b)=[1+4(a+b)]^{-p}H_d(a,b)\), so
\[
\rho_d(a,b)=\left(\frac{\sqrt{(1+8a)(1+8b)}}{1+4(a+b)}\right)^{d/2}
\frac{H_d(a,b)}{\sqrt{H_d(a,a)H_d(b,b)}}.
\]
For \(a_d=u d^{-\alpha}\), \(b_d=v d^{-\alpha}\), the logarithm of the first factor has expansion
\[
-4(u-v)^2d^{1-2\alpha}+O(d^{1-3\alpha})
\]
when \(\alpha>0\), with the remainder negligible relative to its leading scale if \(\alpha<1/2\).

If \(0<\alpha<1/2\), then \(d a_db_d\to\infty\) and \(H_d(a_d,b_d)\to1\), also for the diagonal pairs; thus the logarithmic law follows. If \(\alpha=1/2\), then \(H_d(a_d,b_d)\to g(uv)\) and the first factor tends to \(e^{-4(u-v)^2}\), which yields the critical formula. For \(\alpha>1/2\), \(d a_db_d\to0\), and expansion to first order gives
\[
H_d(a_d,b_d)=\frac{4d a_db_d}{1+4(a_d+b_d)}(1+o(1));
\]
the same holds with equal parameters on the diagonal. Both factors in \(\rho_d\) therefore approach one.

To see that the critical limit is strictly below one for \(u\ne v\), let \(S,T\sim N(0,2)\), \(V\sim N(0,1)\) independent and set
\[
F_u=e^{-u(S+T-2V)}-e^{3u^2-uS}-e^{3u^2-uT}+e^{4u^2}.
\]
Direct Gaussian moment evaluation gives \(\mathbb E F_u=0\) and \(\mathbb E[F_uF_v]=e^{4(u+v)^2}g(uv)\). The critical formula is therefore \(\operatorname{Corr}(F_u,F_v)\). Conditional on \(S,T\), a linear dependence between \(F_u\) and \(F_v\) would imply proportionality of \(e^{2uV}\) and \(e^{2vV}\) up to constants for every real \(V\), impossible for \(u\ne v\). This proves strictness. For fixed distinct \(a,b>0\), the same factorization with \(d\to\infty\) gives
\[
\rho_d(a,b)=\left(\frac{\sqrt{(1+8a)(1+8b)}}{1+4(a+b)}\right)^{d/2}(1+o(1))\to0.
\]

## Verification
The standalone file `proof_check.py` uses only Python's standard library and tests positivity, strict correlations, finite-dimensional quadrature of the centered kernel, finite-sample direct simulation, and the three high-dimensional numerical regimes. Run `python3 proof_check.py` from the directory containing the file. The run reported 91 checks passed, including independent one-dimensional Simpson quadrature and a seeded 40,000-replicate direct \(n=4,d=3\) sample experiment (formula \(0.0055762051103\), empirical \(0.0055497138064\)). Numerical experiments are sanity checks; the proofs of exactness and infinite-dimensional regimes are the preceding identities and asymptotics.

## Relationship to prior work
Li and Yuan (2019), Section 2 and Equation (1), introduce the centered Gaussian-kernel goodness-of-fit U-statistic and its **same-bandwidth** null variance under a general prescribed null. In particular, the case \(a=b\) of the exact formula here specializes their variance identity under \(N_d(0,I_d)\); the Gaussian kernel, degeneracy, and same-bandwidth variance are not novel. The present claim is the complete exact **cross-bandwidth** covariance and its \(d^{-1/2}\) phase boundary for all fixed distinct scales and arbitrary sample sizes.

Schrab et al. (2021/2023) and Biggs, Schrab and Gretton (2023) develop adaptive multikernel **two-sample** tests and their calibration/power theory, without the present known-Gaussian-null one-sample cross-bandwidth covariance formula. Yan and Zhang (2022/2023) analyze high-dimensional two-sample MMD and linearization in regimes controlling bandwidth relative to dimension; their theorems do not state the three-way correlation law for the present one-sample centered Gaussian kernel. Ramdas et al. (2015) obtain bandwidth-independent high-dimensional **power** under mean-shift alternatives, a different assertion from exact joint null correlation. These distinctions do not rule out earlier equivalent results under other terminology.

## Limitations
The result assumes iid observations and exactly known Gaussian null \(N_d(0,I_d)\). It does not cover estimated mean/covariance, non-Gaussian alternatives, two-sample MMD, or finite-sample rejection thresholds. The dimension asymptotics are for fixed positive \(u,v\); they give no uniform relative-error bounds over bandwidth grids whose size increases. For \(\alpha<1/2\), the raw variances themselves can be extremely small even though their normalized correlation tends to zero; decorrelation does not imply high power. A historical-priority risk remains from general multikernel covariance methods and high-dimensional kernel-test asymptotics.

## References
- Tong Li and Ming Yuan (2019), *On the Optimality of Gaussian Kernel Based Nonparametric Tests against Smooth Alternatives*, arXiv:1909.03302, first public September 7, 2019, especially Section 2 and Equation (1). https://arxiv.org/pdf/1909.03302
- Antonin Schrab et al. (2021/2023), *MMD Aggregated Two-Sample Test*, arXiv:2110.15073, especially Sections 2–3. https://arxiv.org/pdf/2110.15073
- Felix Biggs, Antonin Schrab and Arthur Gretton (2023), *MMD-FUSE: Learning and Combining Kernels for Two-Sample Testing Without Data Splitting*, arXiv:2306.08777, Sections 3–5. https://arxiv.org/pdf/2306.08777
- Jian Yan and Xianyang Zhang (2022/2023), *Kernel two-sample tests in high dimensions: interplay between moment discrepancy and dimension-and-sample orders*, Biometrika 110, 411–430, DOI 10.1093/biomet/asac049. https://doi.org/10.1093/biomet/asac049
- Aaditya Ramdas et al. (2015), *Adaptivity and Computation-Statistics Tradeoffs for Kernel and Distance based High Dimensional Two Sample Testing*, arXiv:1508.00655. https://arxiv.org/abs/1508.00655
