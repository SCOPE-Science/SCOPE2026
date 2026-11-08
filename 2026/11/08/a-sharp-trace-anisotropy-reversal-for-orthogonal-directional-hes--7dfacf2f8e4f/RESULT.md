# A sharp trace–anisotropy reversal for orthogonal directional Hessian estimates

## Finding

Orthogonal curvature probes do not uniformly reduce the mean-squared error of a natural, exactly unbiased single-direction zeroth-order Hessian estimator. In dimensions two and three, there is a **sharp trace-to-anisotropy boundary** where the variance ordering reverses. Starting in dimension four, orthogonal probes strictly reduce Frobenius risk for every nonzero symmetric Hessian; positive-semidefinite Hessians also always benefit in every dimension.

For a symmetric matrix \(H\in\mathbb R^{d\times d}\), put \(s=\|H\|_F^2\) and \(t=\operatorname{tr}H\). The risk difference of a \(k\)-column Haar frame versus \(k\) independent uniform directions is, for \(d\ge2\) and \(2\le k\le d\),
\[
\boxed{R_{\mathrm{orth}}-R_{\mathrm{iid}}=\frac{k-1}{k}\left[\frac{-d^2+2d+4}{2(d-1)(d+2)}s-\frac{d(d+1)(d+4)}{4(d-1)(d+2)}t^2\right].}
\]

For nonzero \(H\), the frame has strictly **greater** risk exactly if either
\[
d=2,\quad t^2<\tfrac29s,\qquad\text{or}\qquad d=3,\quad t^2<\tfrac1{42}s.
\]
At either equality boundary the risks match. Otherwise the orthogonal frame strictly improves risk. In particular, every nonzero positive-semidefinite \(H\) benefits from orthogonal directions. At fixed \((d,k)\) in dimensions two or three, the maximum ratio \(R_{\mathrm{orth}}/R_{\mathrm{iid}}\) among all nonzero symmetric \(H\) occurs precisely for traceless matrices; it is \(4/3\) in dimension two with two probes, and \(89/88\) or \(45/44\) in dimension three with two or three probes.

The concrete saddle Hessian \(H=\operatorname{diag}(1,-1)\) has \(R_{\mathrm{iid}}=3/2\) and \(R_{\mathrm{orth}}=2\) for two probes. This is an exact \(33\tfrac13\%\) increase with the same number of black-box evaluations.

## Assumptions and scope

Fix integers \(d\ge2\) and \(2\le k\le d\). Let \(f(x)=\frac12x^\top Hx+b^\top x+c\), where \(H=H^\top\in\mathbb R^{d\times d}\), and fix any evaluation point \(x\in\mathbb R^d\) and any radius \(h>0\). Every unit direction \(u\) yields the *exact* directional curvature
\[
q(u)=\frac{f(x+hu)-2f(x)+f(x-hu)}{h^2}=u^\top Hu.
\]
Define the matrix-valued, one-direction estimate
\[
M(u)=\frac d2q(u)\big((d+2)uu^\top-I_d\big).
\]
In the independent design, \(u_1,\dots,u_k\) are iid uniform on \(S^{d-1}\). In the frame design, they are the first \(k\) columns of a Haar-distributed orthogonal matrix in \(O(d)\). Let \(\widehat H=k^{-1}\sum_{j=1}^kM(u_j)\) and \(R=\mathbb E\|\widehat H-H\|_F^2\) for the respective designs. Both use \(2k+1\) distinct point evaluations when the center evaluation is shared (and fewer only in special coincidences).

The claim concerns the finite-sample Frobenius risk of this *specific calibrated estimator*, not the (different) two-frame mixed-direction Hessian estimator, a recursive rank-one Hessian iteration, gradients, or arbitrary noisy/nonquadratic functions.

## Proof

Write \(P_u=uu^\top\), \(t=\operatorname{tr}H\), and \(s=\operatorname{tr}H^2\). Spherical second and fourth moments give
\[
\mathbb EP_u=I_d/d,\qquad\mathbb E[q(u)P_u]=\frac{tI_d+2H}{d(d+2)}.
\]
Consequently
\[
\mathbb EM(u)=\frac d2\left[\frac{tI_d+2H}{d}-\frac{tI_d}{d}\right]=H.
\]
The same fourth moments yield
\[
\mathbb E q(u)^2=\frac{t^2+2s}{d(d+2)}.
\]
Since \(P_u^2=P_u\) and \(\operatorname{tr}P_u=1\),
\[
\|M(u)\|_F^2=\frac{d^3(d+3)}4q(u)^2.
\]
The one-probe mean-squared error is therefore
\[
S=\mathbb E\|M(u)-H\|_F^2=\frac{d^2(d+3)}{4(d+2)}(t^2+2s)-s.
\]
Thus \(R_{\mathrm{iid}}=S/k\).

Now take two *different columns* \(u\perp v\) of the same Haar frame. Conditional on \(u\), the vector \(v\) is uniform on its orthogonal complement, so
\[
\mathbb E[q(v)\mid u]=\frac{t-q(u)}{d-1}.
\]
Combining this with the one-direction moments proves the exact cross moment
\[
\mathbb E[q(u)q(v)] =\frac{(d+1)t^2-2s}{d(d-1)(d+2)}.
\]
Orthogonality also gives \(\operatorname{tr}(P_uP_v)=0\) and hence
\[
\operatorname{tr}\bigl[((d+2)P_u-I_d)((d+2)P_v-I_d)\bigr]=-(d+4).
\]
The centered Frobenius cross covariance is therefore
\[
\begin{aligned}
C&=\mathbb E\langle M(u)-H,M(v)-H\rangle_F\\
&=-\frac{d^2(d+4)}4\mathbb E[q(u)q(v)]-s\\
&=\frac{-d^2+2d+4}{2(d-1)(d+2)}s-\frac{d(d+1)(d+4)}{4(d-1)(d+2)}t^2.
\end{aligned}
\]
Every ordered distinct frame pair has the same covariance, which proves
\[
R_{\mathrm{orth}}=\frac{S}{k}+\frac{k-1}{k}C.
\]
This establishes the boxed equality, including all quantifiers and finite-sample normalization.

For dimension two, \(C=s/2-9t^2/4\), yielding the boundary \(t^2=2s/9\); for dimension three, \(C=s/20-21t^2/10\), yielding \(t^2=s/42\). When \(d\ge4\), the coefficient \(-d^2+2d+4\) is strictly negative, and the coefficient of \(t^2\) is strictly negative; hence \(C<0\) for all nonzero \(H\). For nonzero positive-semidefinite \(H\), \(t^2\ge s\), so \(C<0\) in dimensions two and three as well.

Finally, \(S\) is positive whenever \(H\ne0\), and the ratio \(R_{\mathrm{orth}}/R_{\mathrm{iid}}=1+(k-1)C/S\) is strictly decreasing in the normalized invariant \(t^2/s\) whenever \(C>0\), with its largest value at \(t=0\). Every \(d\ge2\) admits a nonzero traceless symmetric matrix, so the upper bound is attained, and direct substitution gives the three stated exact ratios. The example is obtained by substituting \(d=k=2\), \(t=0\), \(s=2\).

## Verification

The included `verification/check.py` is a standalone Python 3 checker requiring NumPy and SymPy. Running `python verification/check.py` from the extracted record checks the unbiasedness-related matrix identities, the closed forms for \(S\) and \(C\), the boundaries and sharp risk ratios symbolically. It then checks the planar cases with a deterministic angular quadrature and checks dimensions three and four using a reproducible seeded Haar-frame simulation. Its contemporaneous output is included in `verification/output.txt`. The algebraic proof above, rather than numerical sampling, covers all integer dimensions and every symmetric Hessian.

## Relationship to prior work

Wang's 2022 Riemannian zeroth-order Hessian construction [1] uses two independently sampled tangent directions and mixed directional products, rather than the single calibrated projector \(M(u)\) above. Feng and Wang [2] study orthogonal random directions and give sharp variance/bias bounds for a two-frame finite-difference Hessian scheme; that distinct scheme involves mixed-direction queries and does not logically imply the stated trace-dependent reversal for \(M(u)\). Maritan, Schenato and Dey [3] analyze an *incremental* rank-one residual-curvature Hessian recursion, and discuss orthonormal sampling and alternative estimators, without asserting this finite \(k\) unconditional trace–anisotropy comparison for the calibrated one-step full-matrix estimate. The basic sphere moments and use of Haar frames are standard, not claimed new.

The contribution is the exact comparison law, the dimension-two/three reversal boundaries, the dimension-four universal cutoff, and the sharp worst-case inflation factors for this particular estimator. These are not consequences of a generic bound that merely favors Stiefel-frame sampling for another Hessian estimator.

## Limitations

The objective is exactly quadratic; the identities are not claimed for nonlinear objectives at nonzero radius, noisy evaluations, or estimators with different calibration. Exact equality at the two thresholds is only the exact quadratic finite-probe equality and not a perturbation-stability statement. The proof has not undergone independent validation; older specialized sources might have an equivalent unlocated statement. The one-direction estimator is a useful benchmark rather than an optimal estimator among all possible designs.

## References

[1] Tianyu Wang, *On Sharp Stochastic Zeroth Order Hessian Estimators over Riemannian Manifolds* (first public arXiv version 2022-01-26), https://arxiv.org/abs/2201.10780 .

[2] Yasong Feng and Tianyu Wang, *Stochastic Zeroth Order Gradient and Hessian Estimators: Variance Reduction and Refined Bias Bounds* (first public arXiv version 2022-05-29), https://arxiv.org/abs/2205.14737 .

[3] Alessio Maritan, Luca Schenato and Subhrakanti Dey, *Novel Bounds for Incremental Hessian Estimation With Application to Zeroth-Order Federated Learning*, IEEE Open Journal of Control Systems (2024), DOI https://doi.org/10.1109/OJCSYS.2024.3388374; open full-text rendering https://www.researchgate.net/publication/379845109_Novel_Bounds_for_Incremental_Hessian_Estimation_With_Application_to_Zeroth-Order_Federated_Learning .
