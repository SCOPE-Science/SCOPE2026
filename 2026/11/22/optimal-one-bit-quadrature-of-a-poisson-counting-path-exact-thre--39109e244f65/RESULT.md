# Optimal one-bit quadrature of a Poisson counting path: exact thresholds and a sharp high-intensity limit

## Finding

Let \(N=(N_t)_{0\le t\le1}\) be a homogeneous Poisson counting process with known rate \(\lambda>0\), and let \(J=\int_0^1N_t\,dt\). Choose one deterministic observation time \(x\in[0,1]\), encode the count \(K=N_x\) as **one bit by any deterministic map** \(g:\mathbb Z_{\ge0}\to\{0,1\}\), and estimate \(J\) using any real-valued function of that bit. The loss is unconditional squared error. Define, for \(m>0\),

\[
p_j(m)=e^{-m}\frac{m^j}{j!},\qquad F_j(m)=\sum_{r=0}^{j}p_r(m).
\]

**Exact finite-rate reduction.** At every \(x>0\), an optimal encoder exists among integer thresholds \(g(k)=\mathbf1_{\{k\ge h\}}\), \(h\in\mathbb Z_{\ge1}\). For threshold \(h\), the optimal explained variance is exactly

\[
I_{\lambda}(x,h)=\left(1-\frac{x}{2}\right)^2
\frac{(\lambda x)^2 p_{h-1}(\lambda x)^2}{F_{h-1}(\lambda x)[1-F_{h-1}(\lambda x)]}.
\]

Consequently, the globally minimum achievable squared error is **attained** and equals

\[
R_\lambda^*=\frac\lambda3-\max_{0\le x\le1,\,h\ge1}I_\lambda(x,h),
\]

where \(I_\lambda(0,h)=0\).

**Sharp high-intensity theorem.** For any choice of globally optimal time \(x_\lambda\) and globally optimal threshold representative \(h_\lambda\), as \(\lambda\to\infty\),

\[
x_\lambda\longrightarrow\frac23,\qquad
\frac{h_\lambda-\lambda x_\lambda}{\sqrt{\lambda x_\lambda}}\longrightarrow0,
\qquad
\frac{R_\lambda^*}{\lambda/3}\longrightarrow1-\frac{16}{9\pi}.
\]

Thus a single optimally encoded count bit retains asymptotically exactly \(16/(9\pi)\approx0.565884\) of the target-integral variance, even though the raw count would retain \(8/9\) at its best observation time. The limiting optimal time for the **one-bit** design equals the full-count optimum \(2/3\); the optimal binary cutoff, unlike a fixed saturation cutoff, tracks the changing mean count.

## Assumptions and scope

The process starts at \(N_0=0\), has independent stationary Poisson increments, and the intensity is known. The single measurement is a noiseless count at one predetermined time. Its message may be any deterministic binary function of that count; the receiver uses a Bayes squared-loss estimator (the conditional expectation of \(J\)). No random/adaptive sampling times, multiple bits, unknown-rate inference, packet delays, or causal path reconstruction are included. Equality at threshold boundaries follows the convention \(N_x\ge h\). All limits are for \(\lambda\to\infty\) with the unit observation horizon fixed.

## Proof

**1. Conditioning and variance.** Conditional on \(K=N_x=k\), the \(k\) arrivals in \([0,x]\) have uniform unordered times. The area before \(x\) has conditional mean \(kx/2\). From \(x\) to \(1\) the known count contributes \(k(1-x)\), while independent future arrivals contribute \(\lambda(1-x)^2/2\). Therefore

\[
\mathbb E[J\mid K=k]=\left(1-\frac x2\right)k+\frac\lambda2(1-x)^2.
\]

The integral representation \(J=\int_0^1(1-s)\,dN_s\) gives \(\mathbb EJ=\lambda/2\) and \(\operatorname{Var}(J)=\lambda/3\). If \(B=g(K)\), conditional expectation and total variance give

\[
\operatorname{Var}(\mathbb E[J\mid B])
=\left(1-\frac x2\right)^2\operatorname{Var}(\mathbb E[K\mid B]),
\quad R=\lambda/3-\operatorname{Var}(\mathbb E[J\mid B]).
\]

**2. Every optimal bit has a threshold representative.** Choose arbitrary decoder levels \(a\le b\) for \(K\). For each integer \(k\), assigning it to the nearer level weakly decreases squared error; the resulting cells are separated at \((a+b)/2\), hence form an integer threshold. For each induced binary cell partition, replacing the two decoder levels by conditional count means further decreases squared error. This nearest-neighbor/centroid argument reduces optimization over *all deterministic encoders and decoders* to integer thresholds. For \(m=\lambda x>0\), let \(B_h=\mathbf1_{\{K\ge h\}}\). A Poisson shift identity yields

\[
\operatorname{Cov}(K,B_h)
=\mathbb E[K\mathbf1_{\{K\ge h\}}]-m\Pr(K\ge h)
=m\Pr(K=h-1)=mp_{h-1}(m).
\]

Since \(B_h\) is Bernoulli with variance \(F_{h-1}(m)[1-F_{h-1}(m)]\), the binary regression variance is the squared covariance divided by that variance, proving the formula.

For any bounded interval \(0\le m\le L\), let \(A_h=\{K_m\ge h\}\). Cauchy–Schwarz bounds

\[
\operatorname{Var}(\mathbb E[K_m\mid\mathbf1_{A_h}])
\le\frac{\mathbb E[(K_m-m)^2\mathbf1_{A_h}]}{1-\Pr(A_h)}.
\]

Couple all \(K_m\) with one rate-one Poisson process so \(K_m\le K_L\). The numerator is uniformly dominated by a square-integrable Poisson tail tending to zero as \(h\to\infty\), while the denominator tends uniformly to one. Thus threshold scores tend uniformly to zero; their maximum over \(h\) is attained and varies continuously with \(m\). Compactness of \(x\in[0,1]\) gives the attained global optimum.

**3. Sharp normal two-level constant.** Let \(Z\sim N(0,1)\). For a threshold \(t\), its explained variance is

\[
H(t)=\frac{\varphi(t)^2}{\Phi(t)\Phi(-t)}.
\]

To prove the *global* sharp bound (not just stationary optimality), write \(\varphi\) and \(\Phi\) for standard normal density and cdf. Direct substitution gives

\[
e^{t^2}\Phi(t)\Phi(-t)=
\frac1{2\pi}\int_0^\infty\!\int_0^\infty
 e^{-(u^2+v^2)/2}\cosh(t(u-v))\,du\,dv
\ge\frac14.
\]

The inequality is strict whenever \(t\ne0\). Hence \(H(t)\le2/\pi\), equality only at \(t=0\). The nearest-neighbor argument from step 2 proves the same value is optimal over *all binary encoders*, not only thresholds.

**4. Poisson-to-normal optimal-quantizer limit.** Set \(Z_m=(K_m-m)/\sqrt m\). The Poisson central limit theorem and convergence of second moments imply \(W_2(\mathcal L(Z_m),N(0,1))\to0\). For any square-integrable scalar \(X\), define its minimum two-level squared distortion

\[
D_2(X)=\inf_{a,b\in\mathbb R}\mathbb E\min\{(X-a)^2,(X-b)^2\}.
\]

The distance to a fixed two-point set is 1-Lipschitz; Minkowski's inequality for any coupling gives

\[
|\sqrt{D_2(X)}-\sqrt{D_2(Y)}|\le W_2(\mathcal L(X),\mathcal L(Y)).
\]

For centered unit-variance variables, the explained variance of the optimal two-level quantizer is \(1-D_2\). Therefore, writing \(Q(m)=\max_{h\ge1}\operatorname{Var}(\mathbb E[K_m\mid B_h])\),

\[
\frac{Q(m)}m\longrightarrow\frac2\pi\qquad(m\to\infty).
\]

The sharpness and location of the normal threshold are essential: any optimal Poisson cutoff \(h_m\) satisfies \((h_m-m)/\sqrt m\to0\). Indeed, standardized Poisson squares are uniformly integrable (their fourth moments are \(3+1/m\)). A diverging standardized cutoff makes one binary cell's probability tend to zero and hence its explained variance tend to zero by Cauchy–Schwarz and uniform integrability. A bounded cutoff subsequence tending to \(t\) has explained fraction converging to \(H(t)\) by the central limit theorem and uniform integrability. Optimality forces \(H(t)=2/\pi\), so \(t=0\). This handles every subsequence and establishes cutoff centering.

**5. Optimization of the observation time.** The optimized explained variance at time \(x\) is \(\bigl(1-x/2\bigr)^2Q(\lambda x)\). On each \([\delta,1]\), for \(\delta>0\), its normalization by \(\lambda\) converges uniformly to \((2/\pi)x(1-x/2)^2\); on \([0,\delta]\), it is bounded above by \(\lambda\delta\), since \(Q(m)\le m\). Therefore the global optimization converges to maximizing \(f(x)=x(1-x/2)^2\) on \([0,1]\). Differentiation gives \(f'(x)=(1-x/2)(1-3x/2)\), with the unique maximizer \(x=2/3\) and \(f(2/3)=8/27\). Every optimal \(x_\lambda\to2/3\), and

\[
\lim_{\lambda\to\infty}\frac{\max I_\lambda}{\lambda/3}
=3\cdot\frac2\pi\cdot\frac8{27}=\frac{16}{9\pi}.
\]

Since \(\lambda x_\lambda\to\infty\), the cutoff-centering conclusion of step 4 applies to each globally optimal threshold. For a fixed saturated-presence cutoff \(h=1\), the exact expression simplifies to \(I_\lambda(x,1)=(1-x/2)^2m^2/(e^m-1)\). Because \(\sup_{m>0}m^2/(e^m-1)<\infty\), even its best choice of observation time captures a vanishing fraction of \(\lambda/3\) as \(\lambda\to\infty\). The full-count observation has explained fraction \(3\max_{x\in[0,1]}f(x)=8/9\). This proves the whole claim.

## Verification

Run the accompanying standard-library script with `python3 verify.py`. It computes independent finite Poisson sums for the conditional-mean and binary-regression formulations, checks the exact covariance identity, and performs bounded numerical searches in both time and threshold at several rates. On the supplied implementation, **1,182 finite checks passed**, and the reported high-rate captured fraction at \(\lambda=250\) was approximately \(0.56633\), approaching \(16/(9\pi)\approx0.56588\). The program is a reproducibility aid; the uniform and infinite-rate claims above rely on the analytic proof, not finite enumeration.

## Relationship to prior work

Wang, Chen, and Ephremides (2019) study real-time reconstruction of Poisson counting processes, with full count packets and expected pathwise area distortion; their Appendix A analyzes packet-width overflow rather than optimizing a single binary encoder for the squared error of the integral. Chan, Elgendy, and Wang (2016) analyze binary-thresholded Poisson observations for quanta-image sensing, but optimize image reconstruction from many observations, not a one-time path-integral posterior mean. Arafa and collaborators (2020) study rate-constrained sampling and quantization of Gauss–Markov signals with channel delay, a different process and design criterion. The classical Gaussian two-level scalar quantizer already has the \(2/\pi\) explained-variance constant; **that constant and the standard nearest-neighbor argument are not claimed as new**. The proposed contribution is the sharp combination of a globally optimal one-bit Poisson-area measurement, exact finite-rate cutoff reduction, all-encoder upper bound, and unique high-rate sampling-time law.

## Limitations

There is no closed-form finite-\(\lambda\) formula for every maximizing integer cutoff or maximizing time. Only the asymptotic global optimum and an exact discrete/continuous objective are established. The binary encoder is a deterministic function of a noiseless count; random encoding, adaptation, unknown intensity, multi-sample protocols, and different loss functions are outside the theorem. Numerical experiments cannot establish global novelty. Historical priority remains subject to independent literature review; in particular, broad earlier papers on continuous-time observation quantization were accessible only in part.

## References

- M. Wang, W. Chen, and A. Ephremides, *Real-Time Reconstruction of Counting Process through Queues*, arXiv:1901.08197 (first posted 2019-01-24), https://arxiv.org/abs/1901.08197 .
- S. H. Chan, O. A. Elgendy, and X. Wang, *Images from Bits: Non-Iterative Image Reconstruction for Quanta Image Sensors*, *Sensors* **16** (2016), 1961, https://doi.org/10.3390/s16111961 .
- A. Arafa, K. Banawan, K. G. Seddik, and H. V. Poor, *Sample, Quantize and Encode: Timely Estimation Over Noisy Channels*, arXiv:2007.10200 (2020), https://arxiv.org/abs/2007.10200 .
- N. J. Newton, *Observation sampling and quantisation for continuous-time estimators*, *Stochastic Processes and their Applications* **87** (2000), 311–337, https://doi.org/10.1016/S0304-4149(99)00117-9 (abstract and selected available text inspected; full paper unavailable).
