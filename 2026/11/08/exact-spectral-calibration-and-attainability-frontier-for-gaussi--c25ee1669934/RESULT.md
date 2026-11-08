# Exact spectral calibration and attainability frontier for Gaussian posterior approximation error

## Finding
Let \(X\sim\mathcal N(0,I_d)\) and \(Y=AX+\sigma\epsilon\) with independent \(\epsilon\sim\mathcal N(0,I_d)\), \(\sigma>0\). For commuting real symmetric \(A,B\), with \(B\succ0\), consider all Gaussian surrogate likelihoods \(Y|X=x\sim\mathcal N(Bx+\xi,G^{-1})\), \(\xi\in\mathbb R^d\), \(G\succ0\). Their error is the expected forward posterior Kullback–Leibler divergence \(\mathbb E_Y\mathrm{KL}(\pi_A(\cdot|Y)\|\pi_{B,\xi,G}(\cdot|Y))\).

In a common orthogonal eigenbasis write \(A=Q\operatorname{diag}(a_i)Q^\top\), \(B=Q\operatorname{diag}(b_i)Q^\top\), \(b_i>0\), and put
\[
\rho_i=\frac{a_i}{b_i},\qquad h_i=\frac{\sigma^2}{b_i^2},\qquad L_i=(1-\rho_i)^2+h_i.
\]
The unique minimising precision in the *closed* cone \(G\succeq0\), with optimal shift \(\xi=0\), is
\[
G_*=Q\operatorname{diag}\!\left(\frac{z_i^*}{b_i^2}\right)Q^\top,\quad
z_i^*=\begin{cases}0,&\rho_i\le0,\\
\dfrac{1-2L_i+\sqrt{(2L_i-1)^2+8L_i\rho_i}}{2L_i},&\rho_i>0.
\end{cases}
\]
The original optimization over finite positive-definite likelihood covariances \(G^{-1}\) attains its infimum **if and only if** \(A\succ0\). A nonpositive eigenmode instead drives optimal precision to zero, so its limiting surrogate posterior ignores that datum. Relative to enhanced-error approximation (EEA) with \(G_{\rm EEA}=((A-B)^2+\sigma^2I)^{-1}\), every mode has the exact sign law
\[
\operatorname{sign}\!\left(\frac{z_i^*}{b_i^2}-(G_{\rm EEA})_{ii}^{(Q)}\right)=\operatorname{sign}(a_i-b_i).
\]
For mixed-sign differences \(a_i-b_i\), the correction \(G_*-G_{\rm EEA}\) is indefinite. These assertions are global over the full symmetric positive-(semi)definite precision cones, **not** merely restricted to diagonal competitors.

## Assumptions and scope
The integer dimension satisfies \(d\ge1\), the prior and observation noise are centered independent identity-covariance Gaussians, and the observation noise amplitude \(\sigma\) is strictly positive. Matrices \(A,B\in\mathbb R^{d\times d}\) are symmetric and commute; \(B\) is positive definite, while \(A\) may have arbitrary real eigenvalues. The proposed surrogate observation covariance \(\Gamma=G^{-1}\) is any positive-definite matrix, without a commuting constraint. The closed-precision extension \(G\succeq0\) defines posterior limits, not proper finite Gaussian likelihood covariances on the boundary. The assessment concerns the **unregularised** expected posterior KL objective; it does not cover the coercively regularised algorithms or arbitrary noncommuting forward operators.

## Proof
**1. Elimination of the shift.** Set \(C_G=(I+BGB)^{-1}\) and \(H_G=C_GBG\). The surrogate posterior has mean \(H_G(Y-\xi)\) and covariance \(C_G\). Since \(\mathbb EY=0\), its expected Gaussian KL divergence separates a shift-dependent term
\[
\tfrac12\xi^\top GBC_GBG\xi.
\]
For every \(G\succ0\) this matrix is positive definite, so \(\xi=0\) is the unique optimum for fixed \(G\). At the boundary \(G\succeq0\), it remains an optimum (possibly nonunique in ignored directions).

**2. Strict convexity, existence, and diagonal reduction.** Discarding a constant independent of \(G\), the zero-shift objective is
\[
J(G)=\tfrac12\mathbb E_{X,Y}(BX-Y)^\top G(BX-Y)
+\mathbb E_Y\log\mathbb E_{X'\sim\mathcal N(0,I_d)}
\exp\!\bigl[-\tfrac12(BX'-Y)^\top G(BX'-Y)\bigr].
\]
This continuous formula extends to all \(G\succeq0\). For any nonzero symmetric direction \(H\), the second directional derivative is
\[
D^2J(G)[H,H]=\mathbb E_Y\operatorname{Var}_{X'|Y,G}\!\left(\tfrac12(BX'-Y)^\top H(BX'-Y)\right)>0.
\]
The strict inequality holds because the surrogate posterior has everywhere-positive Gaussian density and \(B\) is invertible, so a nonzero quadratic polynomial cannot be almost surely constant. Thus \(J\) is strictly convex on the entire closed cone.

For existence, its first term equals \(\tfrac12\operatorname{tr}(SG)\) with \(S=(A-B)^2+\sigma^2I\succeq\sigma^2I\). Completing the Gaussian integral in the second term gives \(-\tfrac12\log\det(I+BGB)-\tfrac12\mathbb E_Y Y^\top M_GY\), where \(0\preceq M_G\preceq B^{-2}\). Therefore \(J(G)\to\infty\) as \(\operatorname{tr}(G)\to\infty\), since the negative logarithm grows only logarithmically. A unique global minimiser exists on \(G\succeq0\).

Conjugate to a common eigenbasis of \(A\) and \(B\). Every diagonal sign matrix \(D\) leaves the joint law of \((X,Y)\) invariant, and hence \(J(DGD)=J(G)\). Averaging over all such \(D\) gives \(\operatorname{diag}(G)\), and convexity gives \(J(\operatorname{diag}(G))\le J(G)\), strictly for any non-diagonal \(G\). Consequently the global optimiser is diagonal even though all full SPD precision matrices were admissible.

**3. Exact scalar solution.** In a common eigenmode write \(\rho=a/b\), \(h=\sigma^2/b^2>0\), \(L=(1-\rho)^2+h\), and \(z=b^2g\ge0\). Up to an additive constant the objective is
\[
j(z)=\tfrac12\left[-\log(1+z)+\frac{(1+(1-\rho)z)^2+hz^2}{1+z}\right].
\]
Direct differentiation yields the exact rational identity
\[
2(1+z)^2j'(z)=Lz^2+(2L-1)z-2\rho.
\]
If \(\rho>0\), the numerator has one positive and one negative root. It changes sign from negative to positive at the displayed \(z^*>0\), giving the unique minimum. If \(\rho\le0\), then \(L\ge1+h\); every nonconstant coefficient in the numerator is positive and its constant term is nonnegative. Therefore \(j'(z)>0\) for every \(z>0\), and the unique minimum is \(z^*=0\). This covers all real sensitivities, dimensions and noise levels.

**4. Attainability and comparison with EEA.** Uniqueness of the closed-cone optimiser implies that an interior optimum exists exactly when \(z_i^*>0\) for all \(i\), equivalent to \(A\succ0\). Otherwise \(G_*+\varepsilon I\succ0\), \(\varepsilon\downarrow0\), approaches the infimum without attaining it. When \(z_i^*=0\), the limiting posterior marginal equals the prior \(\mathcal N(0,1)\); its expected KL contribution from the true posterior is \(\tfrac12\log(1+a_i^2/\sigma^2)\).

The EEA covariance is the prior residual covariance \(\Gamma_{\rm EEA}=(A-B)^2+\sigma^2I\), so its dimensionless precision is \(z_{\rm EEA}=1/L\). The numerator of \(2(1+z)^2j'(z)\) at \(z=1/L\) is exactly \(2(1-\rho)\). Since the scalar derivative crosses zero once for \(\rho>0\), and the boundary is optimal for \(\rho\le0\), the optimal precision lies strictly below, equals, or lies strictly above EEA precision precisely when \(a<b\), \(a=b\), or \(a>b\). The full matrix ordering follows in the common eigenbasis.

## Verification
The included `verify.py` uses only the Python standard library. It checks the derivative identity by independent complex-step derivatives, reproduces the Gaussian KL objective directly from posterior means and variances, tests the closed-form root against stationary and boundary inequalities, and tests the sharp EEA sign classification on a deterministic numerical grid. An additional independent three-dimensional numerical comparison of 500 randomized spectra against 5,000 arbitrary full SPD competitors found no smaller objective; these finite checks supplement, rather than replace, the strict-convexity proof.

Run `python3 verify.py`; success prints `VERIFY_OK`. The exact global statement is supplied by the preceding analytic argument, not by enumeration.

## Relationship to prior work
Schneider and Helin (arXiv:2610.38434v1), Theorems 2.7 and 3.1 and equation (3.5), already prove the general posterior-KL convexity and derive the Gaussian-linear objective and optimal mean shift. Their Section 4.1 provides a **particular one-dimensional sign-flipped nonattainment example**. Those statements, the Gaussian objective and the example are prior work, not claimed as novel. The contribution here is the explicit all-dimensional, all-eigenvalue **global precision minimiser**, exact necessary-and-sufficient existence boundary, and modewise sign law against EEA, including the proof that nondiagonal competitors cannot improve it.

Spantini and colleagues' low-rank Bayesian Gaussian approximation results (arXiv:1407.3463 and arXiv:1607.01881) optimise posterior covariance/mean approximation under different admissible classes, often fixing the true posterior mean, rather than calibrating a common surrogate likelihood over all SPD noise covariances. Carere and Lie (arXiv:2411.01112) similarly study low-rank covariance approximations with fixed posterior mean. None of these statements directly yields the coupled surrogate-mean/precision optimum in this theorem.

## Limitations
The theorem is exact for finite-dimensional, centered, commuting symmetric forward operators with a positive surrogate; it is not a noncommutative or infinite-dimensional classification. The boundary minimiser is a limit of proper likelihoods, not itself a finite positive-definite noise covariance. Closed-form optimality does not certify any particular numerical solver or the source's regularised objective. The literature comparison cannot exclude unindexed historical results or an unreported equivalent reduction, and independent mathematical verification has not been performed.

## References
- F. Schneider and T. Helin, *Optimal approximation error approach in Bayesian inverse problems*, arXiv:2610.38434v1 (first posted 2026-10-28), https://arxiv.org/abs/2610.38434 .
- A. Spantini, A. Solonen, T. Cui, J. Martin, L. Tenorio and Y. Marzouk, *Optimal low-rank approximations of Bayesian linear inverse problems*, arXiv:1407.3463, https://arxiv.org/abs/1407.3463 .
- A. Spantini, T. Cui, K. Willcox, L. Tenorio and Y. Marzouk, *Goal-oriented optimal approximations of Bayesian linear inverse problems*, arXiv:1607.01881, https://arxiv.org/abs/1607.01881 .
- C. Carere and H. Lie, *Optimal low-rank posterior covariance approximation in linear Gaussian inverse problems on Hilbert spaces*, arXiv:2411.01112, https://arxiv.org/abs/2411.01112 .
