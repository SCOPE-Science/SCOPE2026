# Finite-probe positivity failure and a square-root conditioning frontier for projected Lanczos covariance completion

## Finding

Consider the Schur-corrected covariance completion that estimates its isotropic unresolved variance from Gaussian projected stochastic Lanczos quadrature (P-SLQ). Even when the quadrature and all boundary moments are **exact**, the finite-probe covariance can be indefinite. Its failure law on a minimal three-dimensional symmetric positive-definite family is exactly

\[
\widehat\omega_N\ \stackrel{d}{=}\ \frac{X_N+\kappa^{-1}Y_N}{N}-1,
\qquad X_N,Y_N\ \overset{\mathrm{ind}}{\sim}\ \chi_N^2,
\]

with actual population bulk variance \(\omega=1/\kappa>0\). Thus the unmodified Gaussian sampler has a real square root only when \(\widehat\omega_N\ge0\). Its negative-variance probability is

\[
p_N(\kappa)=\Pr\bigl(X_N+\kappa^{-1}Y_N<N\bigr)>0.
\]

For \(N=2\),

\[
p_2(\kappa)=\begin{cases}
1-\dfrac{\kappa e^{-1}-e^{-\kappa}}{\kappa-1},&\kappa>1,\\[4pt]
1-2e^{-1},&\kappa=1.
\end{cases}
\]

The probability at two probes rises from \(1-2/e\) when \(\kappa=1\) toward \(1-1/e\) as \(\kappa\to\infty\). More generally, for any \(\kappa_N\ge1\), as \(N\to\infty\),

\[
\frac{\sqrt N}{\kappa_N}\to\tau\in[0,\infty)
\quad\Longrightarrow\quad
p_N(\kappa_N)\to\Phi\!\left(-\frac{\tau}{\sqrt2}\right),
\]

where \(\Phi\) is the standard normal CDF. If the ratio tends to infinity, the limit is zero. It follows that \(p_N(\kappa_N)\to0\) **if and only if** \(N/\kappa_N^2\to\infty\), a sharp square-root conditioning/probe-count frontier.

## Assumptions and scope

All operations are in exact real arithmetic, and the Gaussian probes are independent of the Lanczos reference vector. Fix an integer \(N\ge1\), a real \(\kappa\ge1\), and

\[
A_\kappa=\begin{pmatrix}1&1/2&0\\1/2&1&0\\0&0&\kappa\end{pmatrix},
\qquad q_1=e_1.
\]

The eigenvalues are \(1/2,3/2,\kappa\), so the matrix is strictly positive definite. Run \(m=1\) Lanczos step on \(A_\kappa\), and compute the trace in the two-dimensional Krylov complement using \(l=2\) projected Lanczos nodes, terminating exactly if the Krylov process breaks down. Use the paper's deterministic Schur correction and exact boundary moments; **do not** clip the estimated bulk variance or modify the sampler. The parameter \(\kappa\) is the condition number of the compressed complement, while the full matrix condition number is \(2\kappa\) when \(\kappa\ge3/2\) (and equals \(3\) for \(1\le\kappa\le3/2\)).

The output is the scalar \(\widehat\omega_N\) appearing in the isotropic projector onto the final one-dimensional unresolved direction. The positive-semidefinite property of the fully known deterministic covariance does not imply positivity of this Monte Carlo scalar.

## Proof

**1. Exact Lanczos and Schur data.** One Lanczos step gives \(\alpha_1=1\), \(\beta_1=1/2\), \(q_2=e_2\), and \(T_1=[1]\). In the complement basis \([e_2,e_3]\), the compressed operator, Schur correction, and Schur complement are

\[
T_\perp=\operatorname{diag}(1,\kappa),\quad
\gamma=\beta_1^2(T_1^{-1})_{11}=\frac14,\quad
S_\perp=\operatorname{diag}\!\left(\frac34,\kappa\right).
\]

The normalized boundary direction is \(u=e_2\). With the boundary moments \(p_j=e_1^{\mathsf T}S_\perp^{-j}e_1\) in complement coordinates, we have \(p_j=(4/3)^j\), giving

\[
\sigma_u=\frac{p_3}{p_2}=\frac43,
\qquad
\omega=\operatorname{tr}(S_\perp^{-1})-\sigma_u=\frac1\kappa>0.
\]

The boundary probe starts at the eigenvector \(e_2\) of the compressed operator; its legitimate exact Lanczos termination after one node gives \(a_1=e_1^{\mathsf T}T_\perp^{-1}e_1=1\) and \(a_2=e_1^{\mathsf T}T_\perp^{-2}e_1=1\). Therefore the deterministic Sherman–Morrison trace correction is exactly

\[
\frac{\gamma a_2}{1-\gamma a_1}=\frac13.
\]

**2. Exact projected Gaussian quadrature.** Each projected standard Gaussian probe has coordinates \((Z_{i1},Z_{i2})\), independent standard normals, in the complement. Two-node Lanczos evaluates the inverse quadratic form on the full two-dimensional complement exactly (and handles any exact invariant-subspace termination), so the \(i\)-th estimate is

\[
W_i=Z_{i1}^2+\frac{Z_{i2}^2}{\kappa}.
\]

Combining the paper's trace correction with the boundary variance subtraction yields

\[
\widehat\omega_N=\frac1N\sum_{i=1}^{N}W_i+\frac13-\frac43
=\frac{X_N+\kappa^{-1}Y_N}{N}-1,
\]

where \(X_N=\sum_iZ_{i1}^2\) and \(Y_N=\sum_iZ_{i2}^2\) are independent chi-square variables with \(N\) degrees of freedom. This proves the distribution and the exact negative-variance event. The other covariance terms are confined to \(\operatorname{span}\{e_1,e_2\}\); the quadratic form of the constructed covariance on \(e_3\) is precisely \(\widehat\omega_N\). Consequently a negative scalar makes the full covariance indefinite, not merely an inaccurate trace estimate. Because the weighted chi-square law has a positive density on the positive axis, \(0<p_N(\kappa)<1\) for every finite \(N\) and \(\kappa\).

**3. Finite-probe formula.** When \(N=2\), \(X_2\) and \(Y_2\) are independent exponentials with rate \(1/2\). The weighted second term \(Y_2/\kappa\) has rate \(\kappa/2\). Integrating their convolution below the threshold \(2\) gives the stated formula, with the equal-rate limit \(1-2/e\). The large-\(\kappa\) limit is \(1-1/e\).

**4. Sharp joint limit.** Let \(\tau_N=\sqrt N/\kappa_N\). Then

\[
\sqrt N\,\widehat\omega_N
=\frac{X_N-N}{\sqrt N}+\tau_N\frac{Y_N}{N}.
\]

The central limit theorem gives \((X_N-N)/\sqrt N\Rightarrow\mathcal N(0,2)\), and the law of large numbers gives \(Y_N/N\to1\) in probability. If \(\tau_N\to\tau<\infty\), Slutsky's theorem and continuity of the limiting normal CDF yield \(p_N(\kappa_N)\to\Phi(-\tau/\sqrt2)\). If \(\tau_N\to\infty\), use

\[
\mathbb E\widehat\omega_N=\kappa_N^{-1},
\quad\operatorname{Var}(\widehat\omega_N)=\frac2N(1+\kappa_N^{-2}),
\quad
p_N(\kappa_N)\le\frac{2(\kappa_N^2+1)}{N}\to0
\]

by Chebyshev's inequality. Conversely, if \(N/\kappa_N^2\) does not diverge, extract a subsequence for which \(\tau_N\) has a finite limit; that subsequence has strictly positive limiting failure probability. This proves the if-and-only-if claim.

**5. Irreducible matrices.** For fixed finite \(N,\kappa\), replace the zero entry in positions \((2,3)\) and \((3,2)\) by \(\varepsilon>0\):

\[
A_{\kappa,\varepsilon}=\begin{pmatrix}
1&1/2&0\\1/2&1&\varepsilon\\0&\varepsilon&\kappa
\end{pmatrix},\qquad 0<\varepsilon^2<3\kappa/4.
\]

Sylvester's criterion makes this strictly positive definite and the tridiagonal matrix irreducible. The first Lanczos step is unchanged. For any nonzero \(\varepsilon\), a two-node projected Lanczos calculation is exact on the complement, and the boundary probe spans it in two steps. All Schur moments and sample quadratic forms are continuous as \(\varepsilon\downarrow0\). Thus the random bulk scalar converges almost surely to its diagonal-case counterpart when identical Gaussian probes are used. As that limit has no atom at zero, its negative-event probability converges to \(p_N(\kappa)>0\). Hence positivity failure persists for every sufficiently small strictly positive coupling; it is not a numerical artifact of a reducible block.

## Verification

The standalone Python program `verify.py` checks exact rational Schur identities at multiple condition ratios, two-node Lanczos inverse quadratic forms against direct inversion, the two-probe failure formula against seeded gamma simulation, and the critical-normal limit at selected joint scales. It also independently evaluates the perturbed Schur scalar and tests continuity for irreducible matrices. Run it with `python3 verify.py`. Its finite randomized checks are **not** substitutes for the distributional and asymptotic proofs above.

## Relationship to prior work

Fifen, Karambal and Hennig (2026) construct the Schur-corrected complement covariance, specify Gaussian P-SLQ probes and the trace-correction-minus-boundary-variance formula (their equations (33), (68), (86) and Algorithm 1), and prove trace-estimator consistency. This finding keeps their definition unchanged and isolates its finite-sample positivity probability; their result that the population \(\omega>0\) does not imply that each Monte Carlo realization is nonnegative. Chen, Trogdon and Ubaru (2022) and Saibaba, Alexanderian and Ipsen (2016) analyze stochastic spectral sums and matrix-free trace estimation, respectively. Those bounds cover quadrature and trace-estimation accuracy but do not directly assert the Schur-subtracted covariance sign law or its conditioning/probe-count frontier.

## Limitations

The exact chi-square formula uses the specified three-dimensional family, a single resolved Lanczos step, an exact boundary correction, full two-node complement quadrature, and independent **real Gaussian** probes. The irreducible perturbation result is qualitative for fixed finite parameters; the joint scaling limit is claimed for the explicit unperturbed family. No claim is made for arbitrarily implemented postprocessing, clipping, general covariance estimators, or numerical floating-point behavior. The asymptotic threshold concerns avoiding a negative covariance eigenvalue, not the overall Frobenius or KL accuracy of the estimated matrix. Earlier stochastic-trace literature may contain equivalent tail estimates; the specific algorithmic implication has not been independently audited.

## References

1. H. Fifen, I. Karambal and P. Hennig, *Stochastic Lanczos Quadrature for Computational Uncertainty in Linear Algebra*, arXiv:2609.10080 (first posted 2026-09-09), https://arxiv.org/abs/2609.10080.
2. T. Chen, T. Trogdon and S. Ubaru, *Randomized matrix-free quadrature: unified and uniform bounds for stochastic Lanczos quadrature and the kernel polynomial method*, arXiv:2204.01941, https://arxiv.org/abs/2204.01941.
3. A. K. Saibaba, A. Alexanderian and I. C. F. Ipsen, *Randomized Matrix-free Trace and Log-Determinant Estimators*, arXiv:1605.04893, https://arxiv.org/abs/1605.04893.
