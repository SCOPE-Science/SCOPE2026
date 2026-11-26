# Exact probe-depth allocation frontier for two-mode projected Gaussian Lanczos quadrature

## Finding

For projected stochastic Lanczos quadrature (P-SLQ) on a real positive-definite compressed operator of dimension two, the one-node rule has strictly smaller *single-probe variance* than the exact two-node rule, despite having strictly negative bias. At a fixed even budget of matrix-vector products, the optimal choice between these two uncorrected rules changes at one explicit spectral threshold.

Let the compressed matrix \(B\) have eigenvalues \(a>b>0\). For independent standard real Gaussian probes \(g\in\mathbb R^2\), let \(S_1\) be the one-node inverse Gauss-Lanczos bilinear estimate, \(S_2\) the two-node estimate, and \(T=\operatorname{tr}(B^{-1})\). Their exact moments are
\[
\mathbb E S_1=\frac{2}{\sqrt{ab}},\qquad \mathbb E S_2=T=\frac1a+\frac1b,
\]
\[
T-\mathbb E S_1=\frac{(\sqrt a-\sqrt b)^2}{ab}>0,
\]
\[
\operatorname{Var}(S_1)=\frac{4(a+b-\sqrt{ab})}{(ab)^{3/2}},\qquad
\operatorname{Var}(S_2)=2\left(\frac1{a^2}+\frac1{b^2}\right).
\]
In particular,
\[
\operatorname{Var}(S_2)-\operatorname{Var}(S_1)
=\frac{2(a+b)(\sqrt a-\sqrt b)^2}{a^2b^2}>0.
\]
For any integer \(N\ge1\), the averages of \(N\) independent probes satisfy
\[
\operatorname{MSE}(\widehat T_{1,N})=\frac{(\sqrt a-\sqrt b)^4}{a^2b^2}
+\frac{4(a+b-\sqrt{ab})}{N(ab)^{3/2}},\qquad
\operatorname{MSE}(\widehat T_{2,N})=\frac2N\left(\frac1{a^2}+\frac1{b^2}\right).
\]
At an even integer budget \(M\ge2\) of **projected matrix-vector products**, use \(M\) one-node probes or \(M/2\) two-node probes. Put
\[
M_*(a,b)=\frac{4\bigl(a^2-a\sqrt{ab}+ab-b\sqrt{ab}+b^2\bigr)}{(\sqrt a-\sqrt b)^4}.
\]
The one-node estimator has smaller mean-squared error **if and only if** \(M<M_*(a,b)\); the two estimators tie at equality and the two-node estimator has smaller mean-squared error **if and only if** \(M>M_*(a,b)\). This is a complete allocation classification among the two available exact P-SLQ depths on a two-dimensional complement, with no approximation to the Gaussian moments.

For example, \((a,b)=(4,1)\) gives \(M_*=44\), one-node mean-squared error \(0.1375\) at \(M=20\), and two-node error \(0.2125\) at that budget. At \(M=60\) the respective errors are \(0.0875\) and \(0.0708333\ldots\). At equal **probe** counts, rather than matched products, the threshold is \(N_*=2(a+b)/(\sqrt a-\sqrt b)^2\) (equal to \(10\) in this example).

## Assumptions and scope

Take any real symmetric positive-definite \(A\in\mathbb R^{d\times d}\), \(d\ge2\), and any prescribed resolved orthonormal subspace of codimension two with matrix \(Q\). Restrict the reprojected matrix \(P^\perp A P^\perp\) to the complement to obtain the \(2\times2\) symmetric positive-definite compression \(B=Q_\perp^\top A Q_\perp\). Assume its two eigenvalues are \(a>b>0\). Draw independent \(\xi\sim N(0,I_d)\), set \(u=P^\perp\xi\), and perform reprojected Lanczos from \(u/\|u\|\). When the complement is all of \(\mathbb R^2\), this reduces to \(g\sim N(0,I_2)\).

The \(l\)-node estimator per probe is \(S_l=\|u\|^2 e_1^\top \Theta_l^{-1}e_1\) for \(l=1,2\). Count one projected \(A\)-product for each Lanczos node; assume identical orthogonalization and sampling overhead are excluded from the budget and that the already constructed resolved Krylov basis is reused. The two-node rule exactly evaluates \(u^\top (P^\perp A P^\perp)^+u\) because the complement has dimension two. For \(a>b\) Gaussian probes almost surely have nonzero components in both eigenspaces, so the second Lanczos node exists. The equal-eigenvalue case is excluded since one node is already exact on every probe and the crossover formula is singular.

## Proof

By orthogonal invariance, work in an eigenbasis with \(B=\operatorname{diag}(a,b)\). For \(g=(g_1,g_2)\) standard Gaussian, the one-node Ritz scalar is \(\alpha=(g^\top B g)/(g^\top g)\). Hence
\[
S_1=\frac{\|g\|^4}{g^\top B g},\qquad S_2=g^\top B^{-1}g=\frac{g_1^2}{a}+\frac{g_2^2}{b}.
\]
The two-node identity is exact Lanczos/Gauss quadrature on a two-point spectrum; equivalently, the two Lanczos unit vectors form an orthogonal basis and the tridiagonal is orthogonally similar to \(B\).

Use Gaussian polar coordinates \(g=R(\cos\theta,\sin\theta)\), where \(\theta\) is uniform on \([0,2\pi)\), independent of \(R\), and \(R^2\sim\chi^2_2\). Therefore \(\mathbb E R^2=2\), \(\mathbb E R^4=8\), and \(S_1=R^2/(a\cos^2\theta+b\sin^2\theta)\). The exact angular integral, obtained by the substitution \(t=\tan\theta\) on the four quadrants, is
\[
I_1=\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{a\cos^2\theta+b\sin^2\theta}=\frac1{\sqrt{ab}}.
\]
Differentiate with respect to \(a\) and \(b\) and add, using \(\cos^2\theta+\sin^2\theta=1\), to obtain
\[
I_2=\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{(a\cos^2\theta+b\sin^2\theta)^2}
=-\partial_a I_1-\partial_b I_1=\frac{a+b}{2(ab)^{3/2}}.
\]
Thus \(\mathbb E S_1=2I_1\) and \(\mathbb E S_1^2=8I_2\), proving the one-node mean and variance formulas. For the two-node rule, independence and \(\operatorname{Var}(g_i^2)=2\) give the exact mean and variance. Direct factorization gives the strictly positive variance difference. Subtracting the mean of \(S_1\) from \(T\) gives the squared-root spectral bias.

Averaging \(N\) independent probes divides variance by \(N\) without changing bias; hence the two exact mean-squared errors. For an even product budget \(M\), the difference of the one-node and two-node errors is exactly
\[
\operatorname{MSE}(\widehat T_{1,M})-\operatorname{MSE}(\widehat T_{2,M/2})
=\frac{(\sqrt a-\sqrt b)^4}{a^2b^2}
-\frac{2\operatorname{Var}(S_2)-\operatorname{Var}(S_1)}{M}.
\]
The numerator \(2\operatorname{Var}(S_2)-\operatorname{Var}(S_1)>0\). Solving for its sole zero in positive \(M\) and simplifying yields \(M_*(a,b)\). The difference is strictly increasing in \(M\); the claimed strict inequalities and equality follow. An identical calculation at fixed \(N\) gives \(N_*(a,b)\). All formulas depend only on \(a,b\), so orthogonal changes of complement basis or nonzero coupling between resolved and unresolved subspaces do not alter the result.

## Verification

The standalone `verify.py` reproduces the two elementary angular integrals by independent deterministic quadrature, checks both crossover identities across a seeded family of positive eigenvalue pairs, tests direct two-step reprojected Lanczos with a nonzero resolved/complement matrix coupling, and checks empirical moments using 260,000 seeded Gaussian samples. It reports 1,694 passing assertions. These finite checks supplement but do not replace the exact polar-coordinate proof above.

## Relationship to prior work

Fifen, Karambal and Hennig [1], Theorem 20 and Algorithm 1, introduce P-SLQ for the compressed inverse trace, describe quadrature bias and Monte Carlo variance bounds, and count the quadrature cost as \(N l\) matrix-vector products. The present theorem isolates their trace component at complement dimension two and compares **exact squared errors at equal matvec budget**, rather than asserting a new algorithm, a new Gauss-Lanczos representation, or a general error bound. Chen, Trogdon and Ubaru [2] give general stochastic matrix-free quadrature and simultaneous approximation bounds, but not this two-node finite-budget variance reversal and threshold. Classical Gaussian trace identities and two-node quadrature exactness are acknowledged ingredients, not novelty claims.

## Limitations

The classification is restricted to a real Gaussian probe law, the unmodified one- and two-node P-SLQ rules, a positive-definite **two-dimensional** compression, independent probe averages, and exact arithmetic. It does not cover adaptive stopping, probe reuse with dependence, arbitrary high-dimensional spectra, or the coupling-corrected covariance constructed elsewhere in [1]. The fixed budget excludes construction of the resolved Krylov basis, projector application costs, orthogonalization, and other algorithm overhead. The result compares MSE rather than all loss functions or high-probability error. Older specialized exact-distribution research may contain overlapping identities and requires independent historical-priority review.

## References

[1] H. Fifen, I. Karambal and P. Hennig, *Stochastic Lanczos Quadrature for Computational Uncertainty in Linear Algebra*, arXiv:2609.10080v1, first posted 2026-09-09, especially Theorem 20, Algorithm 1 and Section 6.1. https://arxiv.org/pdf/2609.10080

[2] T. Chen, T. Trogdon and S. Ubaru, *Randomized matrix-free quadrature: unified and uniform bounds for stochastic Lanczos quadrature and the kernel polynomial method*, arXiv:2204.01941v3; SIAM Journal on Scientific Computing 47 (2025), A1733–A1757. https://arxiv.org/pdf/2204.01941
