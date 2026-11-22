# A universal interior variance optimum for paired stochastic Neumann inverses

## Finding

**Theorem (exact risk and strictly partial optimal mirroring).** Consider the paired stochastic Neumann inverse-vector estimator defined below. In the infinite-depth limit it is unbiased, has an explicit variance depending only on the factor-noise variances, and has a **unique variance-minimizing mirror strength strictly between zero and one** whenever at least one stochastic mode affects the right-hand side. Consequently the exactly reflected construction, although it removes all odd noise degrees, is never variance-optimal within this equal-weight paired family at positive noise. The same conclusion holds for every finite-dimensional jointly diagonal model, without requiring independence of noise coordinates.

For one active mode write \(B=1-a^2\), \(s=\operatorname{Var}(\epsilon)>0\), and \(\nu=s/B\in(0,1)\). The optimal strength is the square of the unique root \(u\in(0,1)\) of
\[
\nu u^4+\nu u^3+u-1=0,\qquad \tau_*=u^2.
\]
It satisfies \(\tau_*=1-4\nu+O(\nu^2)\) as \(\nu\downarrow0\), and the sharp high-noise boundary
\[
\lim_{\nu\uparrow1}\tau_* = \frac{3-\sqrt5}{2}.
\]
With the variance of the single-branch ordinary Neumann estimator as reference, the optimal paired-to-single risk ratio tends to \(1/4\) at this boundary, whereas the full-mirror paired-to-single ratio tends to \(1/2\). These are comparisons of estimator variances, not equal-computational-cost claims.

## Assumptions and scope

Fix a positive integer \(d\), a scalar \(\eta>0\), a diagonal positive-definite Hessian \(H=\eta\operatorname{diag}(1-a_1,\ldots,1-a_d)\) with \(0<a_i<1\), and a deterministic vector \(b\in\mathbb R^d\). Let \((\epsilon_j)_{j\ge1}\) be independent and identically distributed random vectors. Assume \(\mathbb E\epsilon_{j,i}=0\), \(s_i=\mathbb E\epsilon_{j,i}^2\in[0,1-a_i^2)\). Coordinates inside one vector may be arbitrarily dependent. Put \(A=I-H/\eta\), \(E_j=\operatorname{diag}(\epsilon_j)\), and let \(\tau\in[0,1]\).

For every integer \(m\ge1\), with empty products equal to the identity, set
\[
V_{m,\tau}=\frac1{2\eta}\sum_{k=0}^{m-1}\left[\prod_{j=1}^k(A+E_j)+\prod_{j=1}^k(A-\tau E_j)\right]b.
\]
This is a normalized exact-reference mirrored Neumann construction. Changing \(E_j\) to its negative recovers the factor-sign convention sometimes used in the literature. All products in this result commute because the factor matrices are diagonal. The reference \(H\) is exact, and the averaging weights of the two branches are fixed at one half. Require \(\sum_i b_i^2s_i>0\) for strict uniqueness.

Put \(B_i=1-a_i^2\). The limit \(V_{\infty,\tau}=\lim_{m\to\infty}V_{m,\tau}\) exists in \(L^2\), uniformly in \(\tau\in[0,1]\); it has mean \(H^{-1}b\). Its exact squared Euclidean risk is
\[
\mathcal R(\tau)=\mathbb E\|V_{\infty,\tau}-H^{-1}b\|_2^2
=\sum_{i=1}^d\frac{b_i^2s_i}{4\eta^2(1-a_i)^2}
\left[\frac1{B_i-s_i}+\frac{\tau^2}{B_i-s_i\tau^2}-\frac{2\tau}{B_i+s_i\tau}\right],
\]
where a mode with \(s_i=0\) contributes zero. This function is strictly convex on \([0,1]\), decreases at zero and increases at one, and therefore has a unique minimizer \(\tau_*\in(0,1)\). The scalar quartic formula above applies when precisely one weighted noisy mode is active. In the general diagonal case the unique root of \(\mathcal R'(\tau)=0\) is an exact one-dimensional characterization.

For any sequence of finite-depth variance minimizers \(\tau_m\in\operatorname*{argmin}_{\tau\in[0,1]}\operatorname{Var}(V_{m,\tau})\), interpreted componentwise via expected squared norm when \(d>1\), one has \(\tau_m\to\tau_*\). More precisely, the finite-depth mean-squared error differs from that finite-depth total variance only by a deterministic, mirror-strength-independent squared truncation bias.

## Proof

**Convergence and mean.** For each coordinate the \(L^2\) norm of a length-\(k\) product of factors \(a_i+c\epsilon_{j,i}\), with \(|c|\le1\), is \((a_i^2+c^2s_i)^{k/2}\), bounded by \(q_i^k\) for \(q_i=\sqrt{a_i^2+s_i}<1\). Minkowski's inequality gives uniformly convergent \(L^2\) Neumann sums. Independence across \(j\) and centering give the finite-depth mean
\[
\mathbb E V_{m,\tau}=\eta^{-1}\sum_{k=0}^{m-1}A^kb
=H^{-1}(I-A^m)b.
\]
Thus \(\mathbb E V_{\infty,\tau}=H^{-1}b\), independently of \(\tau\).

**Exact scalar covariance.** Fix a coordinate; suppress its index. Let \(S_+=\sum_{k\ge0}\prod_{j=1}^k(a+\epsilon_j)\) and \(S_-=\sum_{k\ge0}\prod_{j=1}^k(a-\tau\epsilon_j)\), with the same underlying perturbations in the two branches. Let \(\mu=1/(1-a)\). Removing the first perturbation yields the distributional recursions \(S_+=1+(a+\epsilon_1)S_+'\) and \(S_-=1+(a-\tau\epsilon_1)S_-'\), where the primed pair is independent of \(\epsilon_1\) and has the same joint law. Subtracting \(\mu\) and taking second moments gives
\[
\operatorname{Var}(S_+)=\frac{s\mu^2}{B-s},\qquad
\operatorname{Var}(S_-)=\frac{\tau^2s\mu^2}{B-\tau^2s},\qquad
\operatorname{Cov}(S_+,S_-)=-\frac{\tau s\mu^2}{B+\tau s}.
\]
In particular no third, fourth, or symmetry assumptions on the noise are needed. The variance of \((S_++S_-)/2\) is the stated summand before scaling by \(b^2/\eta^2\). For diagonal \(H\), squared Euclidean error is the sum of coordinate squares, so arbitrary cross-coordinate dependencies do not enter the result.

**Interior optimum.** For fixed \(0<s<B\), define the bracket in the risk formula as \(F_{B,s}(\tau)\). Direct differentiation gives
\[
F_{B,s}'(\tau)=2B\left[\frac{\tau}{(B-s\tau^2)^2}-\frac1{(B+s\tau)^2}\right],
\]
\[
F_{B,s}''(\tau)=2B\left[\frac{B+3s\tau^2}{(B-s\tau^2)^3}+\frac{2s}{(B+s\tau)^3}\right]>0.
\]
Furthermore \(F_{B,s}'(0)=-2/B<0\), and \(F_{B,s}'(1)=8B^2s/((B-s)^2(B+s)^2)>0\). Positive weighted sums therefore remain strictly convex with the same endpoint-derivative signs whenever at least one \(b_i^2s_i\) is positive. Existence, interiority, and uniqueness follow by continuity and the intermediate-value theorem.

**Scalar optimum and sharp noise limits.** With \(u=\sqrt\tau\), equality in \(F_{B,s}'(\tau)=0\) is equivalent, since all denominators are positive, to \(u(B+s\tau)=B-s\tau^2\). Dividing by \(B\) yields \(\nu u^4+\nu u^3+u-1=0\). The left side has strictly positive derivative in \(u\ge0\), and changes sign from negative at zero to positive at one. Implicit differentiation at \(\nu=0\) gives \(u=1-2\nu+O(\nu^2)\), hence \(\tau_*=1-4\nu+O(\nu^2)\). At \(\nu=1\), the quartic factors as \((u^2+1)(u^2+u-1)\), yielding \(u=(\sqrt5-1)/2\).

The ordinary single-branch estimator has variance \(s/(\eta^2(1-a)^2(B-s))\) when \(b=1\). Dividing the paired variance by this amount gives
\[
\frac{\operatorname{Var}(V_{\infty,\tau})}{\operatorname{Var}(V_{\infty,\mathrm{single}})}
=\frac14\left[1+\frac{\tau^2(B-s)}{B-s\tau^2}-\frac{2\tau(B-s)}{B+s\tau}\right].
\]
For \(\tau=1\), this simplifies to \(s/(B+s)\), tending to \(1/2\) as \(s\uparrow B\). Along \(\tau_*(s)\to(3-\sqrt5)/2<1\), the last two bracketed contributions tend to zero, yielding \(1/4\).

**Finite depths.** For any coordinate and either branch, the \(L^2\) norm of the tail after depth \(m\) is at most \(q_i^m/(1-q_i)\), uniformly in \(\tau\). Uniform \(L^2\) convergence implies uniform convergence of the finite-depth second moments and hence uniform convergence of the variance risk functions. Compactness of \([0,1]\) and uniqueness of the limiting minimizer force every sequence of finite-depth minimizers to converge to \(\tau_*\). The finite-depth bias is \(-H^{-1}A^mb\) and does not depend on \(\tau\), so the same claim applies to finite-depth mean-squared error.

## Verification

A standalone Python checker, `verify.py`, uses rational arithmetic for exact enumeration of centered two-point noises, exact finite-depth second-moment recursions, and a two-coordinate case with perfectly correlated perturbations. It also tests limiting moments, the unique quartic optimizer, and the golden-ratio boundary. The checker passed all 109 diagnostics. These finite computations are checks on the explicit calculations, not proofs of the infinite-depth or uniqueness statements; those statements follow from the arguments above.

For an admissible strongly convex scalar example take \(\eta=b=1\), \(a=1/2\), and independent perturbations \(\epsilon_j\in\{-1/4,1/4\}\) with equal probabilities. Then \(H=1/2\) and \(s=1/16\), so the sampled Hessians are positive. The exact optimal strength is \(\tau_*=0.790817468534710\ldots\), with limiting variance \(0.022236590071761\ldots\). Full mirroring has limiting variance \(4/143=0.027972027972028\ldots\), a roughly \(20.5\%\) larger variance than the unique partial optimum. The ordinary single-branch variance is \(4/11\). The target inverse-Hessian-vector value equals \(2\).

## Relationship to prior work

Bohne, Polak, Kazantsev, and Rosenberg (arXiv:2611.15895, first public version November 11, 2026) introduced antithetic Neumann factors, the mirror-strength parameter, and exact cancellation of odd perturbation degrees at full reflection; they also reported experimental variance and skewness changes under partial mirroring. These estimator definitions and motivations are prior art, **not** claimed here. Their Proposition 3.4 and Appendix A.3 analyze cancellation, while Appendix C.4–C.6 reports numerical mirror-strength ablations; those material sections do not provide this distribution-free infinite-depth covariance identity, unique variance optimum, quartic law, or commuting-mode extension. Their experimental choice of \(\tau=1\) favors exact odd-degree cancellation, a different objective from minimal variance.

Ghadimi and Wang (arXiv:1802.02246) supplied foundational stochastic bilevel inverse-Hessian approximation and convergence analysis, without this paired mirror-strength variance optimization. Related partial-antithetic Gaussian sampling and other noise-coupling results concern different estimands and do not imply this Neumann-product optimum. Priority of equivalent results outside the inspected sources is not independently certified.

## Limitations

The exact formula assumes diagonal commuting Hessian samples with an exact reference, independent perturbation vectors across Neumann factors, and their finite second moments; noncommuting matrices, approximate references, temporal dependence, and optimally weighted or differently coupled estimators are not covered. The optimum minimizes squared Euclidean variance within the fixed equal-weight two-branch estimator family, **not** skewness, third-moment error, execution cost, or any downstream bilevel-training performance measure. In the scalar model the exact Hessian is known, so the result is a theoretically calibrated benchmark rather than a claim of cheaper scalar inversion. For finite depth the optimal strength converges to the stated limit but is not asserted to equal it. There has been no independent audit of this proof or historical-priority assessment.

## References

1. J. Bohne, P. Polak, G. Kazantsev, D. Rosenberg, *Your Hypergradient is Skewed: Antithetic Neumann Estimation for Bilevel Optimization*, arXiv:2611.15895v1 (first posted November 11, 2026). https://arxiv.org/abs/2611.15895
2. S. Ghadimi, M. Wang, *Approximation Methods for Bilevel Programming*, arXiv:1802.02246 (2018). https://arxiv.org/abs/1802.02246
