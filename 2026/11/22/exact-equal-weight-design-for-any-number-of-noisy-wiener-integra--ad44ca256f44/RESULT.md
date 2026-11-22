# Exact equal-weight design for any number of noisy Wiener integral samples

## Finding
For every integer \(n\ge1\) and any finite, strictly positive observation noise variance \(\eta>0\), the unique optimal deterministic design for Gaussian estimation of the Wiener path integral is
\[
 t_i^*=1-\bigl(n-i+\tfrac12\bigr)w,\quad
 w=\frac{2}{2(n+\eta)+\sqrt{4(n+\eta)^2-(4n^2-1)}},\quad i=1,\ldots,n.
\]
The conditional-mean estimator has **all weights equal**:
\[
 \widehat J=w\sum_{i=1}^nY_i,\qquad
 R_{n,\eta}^*=\frac13-\frac{nw}2+\frac{n(4n^2-1)w^3}{24}.
\]
All nodes are distinct and interior at every finite positive noise variance; replication is strictly inferior. The displayed closed-form formula requires no nonlinear numerical optimization.

## Assumptions and scope
Let \(B(0)=0\) be a standard real Brownian motion, \(J=\int_0^1 B(t)\,dt\), and \(Y_i=B(t_i)+\epsilon_i\), with independent centered Gaussian noises of variance \(\eta>0\), independent of the process. The sample count \(n\) is an arbitrary positive integer. Locations are fixed deterministically before observing data and may a priori coincide or include endpoints. For each design the estimator is the conditional mean; it minimizes unconditional mean-square loss among all measurable functions of the observations by Gaussian conditioning.

The covariance is \(K(s,t)=\min(s,t)\); hence \(\operatorname{Var}(J)=1/3\) and \(\operatorname{Cov}(J,B(t))=k(t)=t-t^2/2\). The optimality assertion is over all ordered designs in \([0,1]^n\), not just equally spaced configurations.

## Proof
**1. A deterministic regression functional.** Itô isometry represents the target as \(J=\int_0^1(1-s)\,dB_s\). For any real coefficients \(v_1,\ldots,v_n\) and ordered sampling locations, the unconditional risk is exactly
\[
 E(t,v)=\int_0^1\left(1-s-\sum_{i:s\le t_i}v_i\right)^2ds+\eta\sum_{i=1}^nv_i^2.
\]
The unique minimizing coefficient vector solves \((K_t+\eta I)v=k_t\); the positive noise guarantees strict positive definiteness, even with repeated sites. The minimized risk is continuous on the compact ordered design simplex and therefore has a minimizer.

**2. Positive optimal coefficients for distinct positive sites.** If \(0<t_1<\cdots<t_m\le1\), set \(t_0=0\), \(h_i=t_i-t_{i-1}>0\). The inverse of the Brownian covariance matrix \(K=(\min(t_i,t_j))\) is the tridiagonal matrix with off-diagonal entries \(-1/h_{i+1}\), first-to-penultimate diagonal entries \(1/h_i+1/h_{i+1}\), and final diagonal \(1/h_m\). The vector \(z=K^{-1}k\) has strictly positive entries
\[
 z_i=\frac{t_{i+1}-t_{i-1}}2\quad(i<m),\qquad z_m=1-\frac{t_m+t_{m-1}}2>0.
\]
Here the last formula includes \(m=1\) with \(t_0=0\). With independent noise variances \(d_i>0\) after merging identical sites, \((K^{-1}+D^{-1})(Dv)=z\). Its coefficient matrix is a symmetric positive definite, strictly diagonally dominant M-matrix with an entrywise nonnegative inverse. Thus each aggregate coefficient is strictly positive; repeated channels at the same time share that positive aggregate coefficient equally.

**3. Exclude all boundary and repeated configurations.** A site at zero has coefficient zero. Because the residual Itô kernel \(h(s)=1-s-\sum_i v_i\mathbf{1}_{s\le t_i}\) has derivative \(-1\) between finitely many knots, \(\int_0^u h(s)ds\) is not identically zero. Replacing a zero-time site with a time \(u\) where this integral is nonzero strictly reduces the conditional variance, by the Gaussian partial-covariance formula; hence no optimum uses zero. If \(m\ge2\) observations coincide at a positive \(c<1\), their common optimal coefficient \(v>0\) permits moving one to \(c-\delta\) and one to \(c+\delta\) while retaining coefficients. Directly integrating the two affected intervals in \(E\) gives the first-order change \(-2(m-1)v^2\delta+o(\delta)<0\). At \(c=1\), moving one observation left gives a negative first-order change. Finally if the largest distinct site is \(t_n=1\), differentiating \(E\) while holding coefficients fixed gives \(\partial_{t_n}E=v_n^2>0\), so moving that site left improves risk. Thus every global minimizer has \(0<t_1<\cdots<t_n<1\) and all its conditional-mean weights are positive.

**4. All optimal weights must coincide.** At an interior optimum, the location derivatives of \(E\) vanish. Positivity of each \(v_i\) gives
\[
 1-t_i=\sum_{j>i}v_j+\frac{v_i}2,\qquad
 t_{i+1}-t_i=\frac{v_i+v_{i+1}}2.
\]
The normal equations in \(v_i\) read \(\int_0^{t_i}(g(s)-(1-s))ds+\eta v_i=0\), with \(g(s)=\sum_{j:s\le t_j}v_j\). Subtracting consecutive equations and using the just-derived midpoint conditions yields
\[
 (v_i-v_{i+1})\left(\eta+\frac{v_i+v_{i+1}}8\right)=0.
\]
Since the bracket is strictly positive, \(v_i=v_{i+1}\). Therefore all \(n\) weights equal a single \(w>0\), and the location equations force \(t_i=1-(n-i+1/2)w\).

**5. Solve and prove uniqueness.** The final weight normal equation is \(w(\sum_i t_i+\eta)=k(t_n)\). With \(\sum_i t_i=n-n^2w/2\) and \(k(t_n)=1/2-w^2/8\), it becomes
\[
 (4n^2-1)w^2-8(n+\eta)w+4=0.
\]
The quadratic is positive at zero and negative at \(2/(2n+1)\); its larger root exceeds \(2/(2n-1)\). Only the smaller root is compatible with strictly interior ordered sites. Rationalizing it gives the displayed closed form. Existence of an interior global minimizer and uniqueness of the feasible stationary point imply unique **global** optimality. With \(k(t_i)=1/2-(n-i+1/2)^2w^2/2\) and \(\sum_{r=0}^{n-1}(r+1/2)^2=n(4n^2-1)/12\), the Gaussian projection identity \(R^*=1/3-w\sum_i k(t_i)\) proves the stated exact risk.

## Verification
All claims above are analytic. A companion verifier independently constructs Brownian covariance matrices for rational-noise examples, solves their linear normal equations with exact rational arithmetic, verifies the quadratic and the equal-weight prediction, and performs nonexhaustive rational-grid comparisons for \(1\le n\le5\). Its experiments check implementation consistency but do **not** constitute a proof of global optimality for all \(n\).

## Relationship to prior work
Cai, Lam and Scarlett (arXiv:2202.10615, publicly available 22 February 2022) establish general noisy kernel quadrature bounds and give GP conditioning formulas; their relevant full-text sections concern kernel-class rates, not an exact all-\(n\) Wiener design. Benhenni and Cambanis (1992) develop stochastic-integral sampling designs and asymptotic methods. Mukherjee (2003) explicitly studies exact optimal designs for product-covariance process integrals, so it is the closest historical source. Its accessible abstract does not indicate independent observation noise; the full text could not be examined, leaving a publication-priority risk. The noiseless configuration \(t_i=2i/(2n+1)\) is **not** claimed new. The present mathematical claim is the strictly positive-noise, all-sample-count closed form, including universal equal weights and strict nonreplication.

## Limitations
The result needs independent noises of identical *known* positive variance, fixed deterministic observation times, a zero-start standard Wiener prior, and an unweighted path integral. It does not prove optimality under adaptive observation, colored or heteroscedastic errors, nonlinear observation channels, or alternative Gaussian processes. An earlier exact formulation under noisy product-covariance sampling terminology could still exist; independent publication-priority verification is pending.

## References
1. Xu Cai, Chi Thanh Lam, Jonathan Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615, version 1 dated 2022-02-22, https://arxiv.org/abs/2202.10615.
2. Karim Benhenni, Stamatis Cambanis, *Sampling Designs for Estimating Integrals of Stochastic Processes*, Annals of Statistics 20(1), 1992, DOI:10.1214/aos/1176348517.
3. Bhramar Mukherjee, *On Sampling Designs for Integral Estimation of a Random Process*, Communications in Statistics—Theory and Methods 32(8), 2003, DOI:10.1081/STA-120022249. Full text not available in this assessment.
