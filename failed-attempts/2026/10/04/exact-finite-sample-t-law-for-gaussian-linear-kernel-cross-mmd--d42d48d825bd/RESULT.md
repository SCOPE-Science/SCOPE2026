# Exact finite-sample \(t\)-law for Gaussian linear-kernel cross-MMD
## Finding
Consider the cross-MMD construction with one-dimensional observations, linear kernel \(k(x,y)=xy\), balanced sample splitting, and equal group sizes. Let each of the two original samples have size \(2s\), with \(s\ge2\) observations from each group in each half. Under the Gaussian null \(X_i,Y_j\stackrel{{\mathrm{{iid}}}}{{\sim}}N(\mu,\sigma^2)\), let \(T_s\) denote the studentized cross-MMD statistic defined by the cross-MMD variance estimator.

Then
\[
T_s\overset{{d}}=\sqrt{{\frac{{s}}{{s-1}}}}\,t_{{2s-2}}.
\]
Therefore the one-sided test that uses the standard-normal cutoff \(z_{{1-\alpha}}\) has exact null rejection probability
\[
\alpha_s
=1-F_{{t_{{2s-2}}}}\!\left(z_{{1-\alpha}}\sqrt{{\frac{{s-1}}{{s}}}}\right),
\]
and \(\alpha_s>\alpha\) for every \(0<\alpha<1/2\). An exact finite-sample level-\(\alpha\) cutoff is
\[
c_{{s,\alpha}}=\sqrt{{\frac{{s}}{{s-1}}}}\,t_{{2s-2,1-\alpha}}.
\]
For fixed \(\alpha\), writing \(z=z_{{1-\alpha}}\),
\[
\alpha_s
=\alpha+\frac{{\phi(z)(z^3+5z)}}{{8s}}+O(s^{{-2}}).
\]
At \(\alpha=0.05\), the exact normal-cutoff sizes are \(0.0680319448704\) for \(s=10\) and \(0.0516503578015\) for \(s=100\). Thus the asymptotic Gaussian calibration is measurably anti-conservative at moderate sample sizes even in this elementary null model.

## Assumptions and scope
The result assumes two independent samples, equal Gaussian variance, balanced halves of size \(s\) within each group, and the linear kernel. The statistic and its variance estimator are exactly the cross-MMD definitions of Shekhar, Kim, and Ramdas. The statement concerns the one-sided null calibration used for the nonnegative population MMD target. No claim is made for nonlinear characteristic kernels, unequal split sizes, heteroscedastic Gaussian samples, or non-Gaussian distributions.

The linear kernel makes cross-MMD a mean-difference benchmark rather than a fully distribution-sensitive test. Its value here is that it gives an exact finite-sample diagnostic for the sample-splitting and studentization mechanism that is otherwise calibrated through a limiting Gaussian law.

## Proof
Write the first-half mean difference as
\[
A=\overline X_1-\overline Y_1
\]
and the second-half mean difference as
\[
B=\overline X_2-\overline Y_2.
\]
For the linear kernel, the empirical kernel mean difference from the second half is the scalar \(B\), so the cross inner product is
\[
\widehat{\mathrm{{xMMD}}}^2=AB.
\]
For a first-half observation, the source paper's projected variables become \(U_{{X,i}}=X_iB\) and \(U_{{Y,j}}=Y_jB\). Hence, with
\[
S=\sum_{{i=1}}^s(X_i-\overline X_1)^2+\sum_{{j=1}}^s(Y_j-\overline Y_1)^2,
\]
the published variance estimator reduces exactly to
\[
\widehat\sigma^2=\frac{{B^2S}}{{s^2}}.
\]
Because \(B\neq0\) almost surely,
\[
T_s=\frac{{AB}}{{|B|\sqrt S/s}}
=\operatorname{{sgn}}(B)\frac{{sA}}{{\sqrt S}}.
\]
Under the equal-variance Gaussian null, the usual pooled two-sample statistic based only on the first half is
\[
U=A\sqrt{{\frac{{s(s-1)}}{{S}}}}\sim t_{{2s-2}}.
\]
The second half is independent of the first, so \(\operatorname{{sgn}}(B)\) is an independent fair sign. Since the Student law is symmetric,
\[
T_s\overset{{d}}=\sqrt{{\frac{{s}}{{s-1}}}}\,U,
\]
which proves the exact distribution and the exact cutoff formula.

To prove strict anti-conservatism of the normal cutoff, let \(f_\nu\) and \(\phi\) be the Student and standard-normal densities. For \(x>0\), direct differentiation gives
\[
\frac{{d}}{{dx}}\log\frac{{f_\nu(x)}}{{\phi(x)}}
=\frac{{x(x^2-1)}}{{\nu+x^2}}.
\]
The density ratio begins below one at zero, decreases on \((0,1)\), then increases to infinity. Therefore the positive Student tail strictly exceeds the Gaussian tail at every positive threshold. Since \(z_{{1-\alpha}}\sqrt{{(s-1)/s}}<z_{{1-\alpha}}\) for \(\alpha<1/2\), the displayed size is strictly larger than \(\alpha\).

For the expansion, uniformly for fixed \(x\),
\[
F_\nu(x)=\Phi(x)-\frac{{(x^3+x)\phi(x)}}{{4\nu}}+O(\nu^{{-2}}).
\]
Substitute \(\nu=2s-2\) and \(x=z\sqrt{{1-1/s}}=z-z/(2s)+O(s^{{-2}})\), then expand the Gaussian tail. This yields
\[
\alpha_s=\alpha+\frac{{\phi(z)(z^3+5z)}}{{8s}}+O(s^{{-2}}).
\]

## Verification
The accompanying `verify.py` uses only the Python standard library. It implements Student-\(t\) survival probabilities through the regularized incomplete beta function, checks the exact algebraic reduction on rational sample values, reproduces the quoted \(5\%\) sizes, verifies the exact calibrated cutoffs, and checks convergence to the stated first-order coefficient at increasing \(s\). The packaged script returns `VERIFY_OK`.

The computational checks confirm numerical evaluations and the algebraic identity on a concrete exact-arithmetic instance; the distributional theorem itself follows from the analytic reduction above and the classical Gaussian pooled-\(t\) law.

## Relationship to prior work
Kim and Ramdas introduced cross U-statistics based on sample splitting and self-normalization, with a Gaussian limiting distribution designed to be dimension-agnostic. Shekhar, Kim, and Ramdas then defined cross-MMD, its studentizer, and the one-sided standard-normal calibration, and proved asymptotic standard-normality under the null. The relevant full text of the cross-MMD paper was inspected at the statistic, variance-estimator, and null-limit statements, together with targeted full-text searches for an exact Student law and finite-sample calibration. No statement equivalent to the scaled \(t\) law above was located.

The classical two-sample Student theorem is used as an ingredient rather than claimed as new. The new content is the exact reduction of the published cross-MMD statistic and studentizer to that law in the Gaussian linear-kernel benchmark, together with the resulting exact size, strict direction of finite-sample distortion, exact repair, and first-order calibration error. Targeted searches of the published-finding database and primary-literature metadata did not locate an equivalent cross-MMD statement.

## Limitations
This result is intentionally a sharply delimited benchmark. The linear kernel detects mean differences only, and Gaussian equal-variance structure is essential to the exact Student law. The theorem does not establish an exact null distribution for Gaussian/RBF kernels or for the general high-dimensional regimes that motivate cross-MMD. It also does not compare finite-sample power after replacing the normal cutoff by the exact cutoff.

A residual literature risk remains: the full body of the foundational cross-U-statistics article was not available through the attempted lawful access route during this check, so an equivalent elementary Gaussian special case could in principle appear there under different notation. Its accessible abstract and metadata describe Gaussian limiting calibration rather than this exact two-sample cross-MMD law, and the directly relevant cross-MMD paper's inspected full text did not contain the formula.

## References
1. Ilmun Kim and Aaditya Ramdas, *Dimension-agnostic inference using cross U-statistics*, arXiv:2011.05068, first posted 2020-11-10; Bernoulli 30(1), 2024.
2. Shubhanshu Shekhar, Ilmun Kim, and Aaditya Ramdas, *A Permutation-free Kernel Two-Sample Test*, arXiv:2211.14908, first posted 2022-11-27.
