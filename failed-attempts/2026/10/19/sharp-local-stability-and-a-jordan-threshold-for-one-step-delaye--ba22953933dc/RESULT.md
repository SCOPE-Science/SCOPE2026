# Sharp local stability and a Jordan threshold for one-step delayed polar eigensolvers

## Finding

Let \(A=A^{\mathsf T}\in\mathbb R^{d\times d}\), \(d\geq2\), have ordered eigenvalues \(\lambda_1>\lambda_2\geq\cdots\geq\lambda_d\), and let \(v_1\) be a unit principal eigenvector. Define \(L=\lambda_1-\lambda_d>0\), the sphere gradient \(g(w)=-(I-ww^{\mathsf T})Aw\), and the normalized delayed-gradient map, for \(p\in[0,1]\) and \(\eta>0\),

\[
 w_{t+1}=\frac{w_t-\eta[(1-p)g(w_t)+p g(w_{t-1})]}{\|w_t-\eta[(1-p)g(w_t)+p g(w_{t-1})\|_2}.
\]

The fixed pair \((v_1,v_1)\) is **locally exponentially attracting for all sufficiently close independent initial pairs** exactly on the strict open stepsize range \(0<\eta<\eta_{\max}(p)\), where

\[
\eta_{\max}(p)=\frac{1}{L}\begin{cases}
\dfrac{2}{1-2p},&0\leq p\leq\tfrac14,\\[3pt]
\dfrac{1}{p},&\tfrac14\leq p\leq1.
\end{cases}
\]

For every \(\eta>\eta_{\max}(p)\), the fixed pair has a transverse multiplier of modulus strictly larger than one and is linearly unstable. At equality local **exponential** attraction fails because a multiplier has modulus one; no assertion of mere asymptotic attraction or repulsion is made there. Among all convex fresh/stale mixtures, the **unique** maximizer of the strict stability-step ceiling is \(p=1/4\), yielding \(\eta_{\max}=4/L\); the all-fresh choice has ceiling \(2/L\).

At the ceiling, the largest-gap transverse mode has exactly three spectral types: for \(0\leq p<1/4\) there is a simple multiplier \(-1\) and a second multiplier \(-2p/(1-2p)\); for \(p=1/4\) there is a defective double multiplier \(-1\); for \(1/4<p\leq1\) there is a nonreal conjugate unit-modulus pair. At the unique optimal mixture, the critical-mode companion matrix \(M=\left(\begin{smallmatrix}-2&-1\\1&0\end{smallmatrix}\right)\) has the **exact** amplification law

\[
\|M^k\|_2=k+\sqrt{k^2+1}\qquad(k=0,1,2,\ldots).
\]

Thus the doubled stability ceiling has an intrinsic linearly growing perturbation response exactly at the boundary.

## Assumptions and scope

The gradient is the Riemannian gradient of \(F(w)=-\tfrac12w^{\mathsf T}Aw\) on the real unit sphere. The update **aggregates an extrinsic fresh gradient and a one-iteration-old tangent gradient without parallel transport**, then normalizes the aggregate to the sphere. This is a deliberately specified two-component delayed polar model, not an assertion about every arrival schedule of an asynchronous implementation. Its proportions can be represented by two proportional quadratic components, one evaluated at the current vector and the other at the previous vector. The denominator is nonzero throughout some neighborhood of the equilibrium because both gradients vanish there.

Local exponential attraction means there are a neighborhood \(U\) of \((v_1,v_1)\), constants \(C<\infty\) and \(r\in(0,1)\), such that every pair initialized in \(U\) follows the well-defined normalized map and satisfies \(\|(w_t,w_{t-1})-(v_1,v_1)\|\leq Cr^t\|(w_0,w_{-1})-(v_1,v_1)\|\). Equivalently, the linearized two-state map has spectral radius strictly below one. The strict converse above concerns multipliers larger than one, not all possible nonlinear dynamics at unit-modulus boundary points. Other nonprincipal eigenvector equilibria are outside the claim.

## Proof

**(1) Exact transverse Jacobian.** Choose an orthonormal eigenbasis with \(v_1=e_1\) and local hemisphere coordinates \(w(\xi)=(\sqrt{1-\|\xi\|_2^2},\xi)\). The map is smooth near \((e_1,e_1)\). At \(\xi=0\), the differential of the sphere gradient is \(Dg(e_1)[e_j]=(\lambda_1-\lambda_j)e_j\) for each \(j=2,\ldots,d\); normalization at \(e_1\) has differential the orthogonal projection onto its tangent space. Writing \(\Delta_j=\lambda_1-\lambda_j\in(0,L]\), the local two-state Jacobian splits into companion blocks

\[
 M_j=\begin{pmatrix}1-\eta(1-p)\Delta_j&-\eta p\Delta_j\\1&0\end{pmatrix},
\quad
 P_j(z)=z^2-[1-\eta(1-p)\Delta_j]z+\eta p\Delta_j.
\]

The formulas hold in every dimension and allow multiplicities below the simple leading eigenvalue.

**(2) Exact Schur inequalities.** For a real monic quadratic \(z^2-az+b\), both roots are strictly inside the unit disk exactly when \(1-b>0\), \(1-a+b>0\), and \(1+a+b>0\). In this case \(a=1-\eta(1-p)\Delta_j\) and \(b=\eta p\Delta_j\), so the three conditions reduce to

\[
 \eta p\Delta_j<1,\qquad \eta\Delta_j>0,\qquad
 2-\eta(1-2p)\Delta_j>0.
\]

For nonnegative mixture weights, these are simultaneously valid for every \(j\geq2\) if and only if they hold at the maximal gap \(\Delta_j=L\). Indeed, all relevant upper bounds are monotone in \(\Delta_j\) and a lowest-eigenvalue direction realizes \(L\). When \(p=0\), the first inequality imposes no restriction; when \(p\geq1/2\), the third inequality is automatic. Thus the allowable normalized stepsize \(\alpha=\eta L\) is

\[
 0<\alpha<\min\left\{\frac1p,\frac{2}{1-2p}\right\},
\]

with a term omitted when its denominator is nonpositive or zero. The two finite ceilings cross only at \(p=1/4\). One ceiling strictly rises up to that value; the other strictly decreases afterward. This proves the unique maximum \(\alpha=4\). By the standard discrete fixed-point linearization theorem, strict Schur stability of the smooth map yields local exponential attraction. Above the stated ceiling the lowest-eigenvalue block has a root strictly outside the unit disk (from either \(1-b<0\) or \(1+a+b<0\)), establishing linear instability.

**(3) Boundary types.** For \(p<1/4\), substitute \(\alpha=2/(1-2p)\) in \(P_d\); the two roots are \(-1\) and \(-2p/(1-2p)\), with the second strictly between \(-1\) and zero, including zero at \(p=0\). At \(p=1/4\), \(\alpha=4\) gives \(P_d(z)=(z+1)^2\), with nontrivial Jordan block \(M=\left(\begin{smallmatrix}-2&-1\\1&0\end{smallmatrix}\right)\). For \(p>1/4\), the boundary is \(\alpha=1/p\), so the quadratic has constant coefficient one and linear coefficient of magnitude strictly less than two. Its roots are therefore distinct, nonreal and unit-modulus.

**(4) Exact critical growth.** Let \(N=M+I=\left(\begin{smallmatrix}-1&-1\\1&1\end{smallmatrix}\right)\); then \(N^2=0\) and \(M^k=(-1)^k(I-kN)\). The determinant of \(I-kN\) is one and the squared Frobenius norm is \(2+4k^2\). Consequently the larger singular value equals \(k+\sqrt{k^2+1}\), giving the displayed operator norm for every integer \(k\geq0\). These equalities are exact, not asymptotic numerical observations.

## Verification

The standalone standard-library program `verify_stale_polar.py` checks 288 companion-root configurations (three transverse eigenmodes, twelve mixture weights and eight step multipliers); evaluates 144 finite-difference partial derivatives of the **actual normalized nonlinear update** against the analytic Jacobian; and checks 100 exact integer powers and corresponding singular-value formulas at the Jordan threshold. Execute from the artifact directory using `python3 verify_stale_polar.py`. All checks passed. They corroborate, but do not replace, the algebraic proof for arbitrary dimension and continuous parameters.

## Relationship to prior work

Wang, Hu and Wai (2026) introduced asynchronous Grassmannian incremental aggregation with extrinsic polar updates and established sufficient broad-basin and local convergence restrictions involving eigengaps, component spectral spreads and delay. Their Theorem 2, proof and algorithm describe no sharp **necessary-and-sufficient** two-component local stability frontier, no uniquely optimal cached-gradient fraction, and no boundary Jordan-growth law. Wang, Jiao, Wai and Gu (2023) analyzed related asynchronous Riemannian aggregation for distributed PCA and gave sufficient convergence bounds; their algorithm and theorem do not specify the above full parameter classification. Generic Schur stability tests and classical linear-multistep absolute-stability theory already supply the underlying scalar polynomial techniques and are not claimed as new. The present assertion is the exact eigensolver-specific combination of the differential reduction, sharp optimization of the mixing fraction, and the boundary spectral-growth classification.

## Limitations

This theorem is local, deterministic, real-symmetric, rank-one, and assumes a fixed one-step latency with two proportional components. It gives no global basin, no finite-precision guarantee, no all-schedules asynchronous guarantee, and no assertion of a better asymptotic **rate** or lower computational cost from introducing a stale gradient. At the exact step ceiling a multiplier lies on the unit circle, precluding local exponential attraction; more general nonlinear boundary stability is not classified. The use of standard Schur theory means that novelty is application-specific rather than a new general root criterion. Broader multistep stability literature and uninspected sections of related asynchronous PCA research remain plausible bibliographic risks; a comprehensive independent literature audit has not occurred.

## References

1. Xiaolu Wang, Jiang Hu, Hoi-To Wai (2026), *Incremental Aggregation on the Grassmannian for Asynchronous Eigenspace Computation*, arXiv:2608.04406v1 (public 2026-08-05), https://arxiv.org/abs/2608.04406; publicly accessible complete manuscript: https://www.researchgate.net/publication/411716720_Incremental_Aggregation_on_the_Grassmannian_for_Asynchronous_Eigenspace_Computation .
2. Xiaolu Wang, Yuchen Jiao, Hoi-To Wai, Yuantao Gu (2023), *Incremental Aggregated Riemannian Gradient Method for Distributed PCA*, Proceedings of Machine Learning Research 206, 7492–7510, https://proceedings.mlr.press/v206/wang23j.html .
3. Lajos Lóczi (2019), *Optimal subsets in the stability regions of multistep methods*, Numerical Algorithms (2019), DOI 10.1007/s11075-019-00775-x, https://link.springer.com/article/10.1007/s11075-019-00775-x .
4. J. C. Butcher (2003), *Numerical Methods for Ordinary Differential Equations*, Chapter 4, Linear Multistep Methods, DOI 10.1002/0470868279.ch4 (classical background on multistep stability).
