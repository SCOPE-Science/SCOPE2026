# A sharp rank-one stabilization cost after spectral truncation of a Riccati solution

## Finding

Consider continuous-time algebraic Riccati equations (CAREs) with a low-rank observation and a single actuator. For every integer \(n\ge2\) and real \(K\ge3\), let \(e_i\) denote coordinate basis vectors and set
\[
A=\operatorname{diag}(-1,1,-1,\ldots,-1),\quad
B=\sqrt K\,e_2,\quad
C=\begin{pmatrix}\sqrt2\,e_1^\top\\K^{-1/2}e_2^\top\end{pmatrix},\quad
G=BB^\top,\quad Q=C^\top C.
\]
Write
\[
\mathcal R(X)=A^\top X+XA-XGX+Q,\qquad
d=d_K=\frac{1+\sqrt2}{K}.
\]
The unique stabilizing symmetric positive-semidefinite CARE solution is
\[
X_*=\operatorname{diag}(1,d,0,\ldots,0).
\]
Its feedback matrix \(A-GX_*\) is Hurwitz with eigenvalues \(-1\) (multiplicity \(n-1\)) and \(-\sqrt2\). Since \(0<d<1\), the unique Frobenius-optimal positive-semidefinite rank-one spectral approximant is \(Y_{\rm svd}=e_1e_1^\top\), whose error and residual satisfy
\[
\|X_*-Y_{\rm svd}\|_F=d,\qquad
\|\mathcal R(Y_{\rm svd})\|_F=K^{-1}.
\]
Nevertheless, \(A-GY_{\rm svd}\) has an eigenvalue \(+1\), so this low-rank approximation fails to stabilize.

More sharply, the set of all strictly stabilizing positive-semidefinite rank-at-most-one approximants has exact distance
\[
\boxed{\inf_{\substack{Y\succeq0,\ \operatorname{rank}Y\le1\\A-GY\ \mathrm{Hurwitz}}}\|X_*-Y\|_F
=\sqrt{d^2+\frac{2(1-d)}K}.}
\]
The infimum is not attained because the boundary has a zero closed-loop eigenvalue. Dividing by the unrestricted best-rank-one error yields the sharp, unbounded stability price
\[
\boxed{\frac{\inf_{\mathrm{stabilizing}\ Y}\|X_*-Y\|_F}{\min_{Y\succeq0,\ \operatorname{rank}Y\le1}\|X_*-Y\|_F}
=\sqrt{(6-4\sqrt2)K+3-2\sqrt2}
\sim(2-\sqrt2)\sqrt K.}
\]
For every fixed relative positive-eigenvalue pruning tolerance \(\eta>0\), sufficiently large \(K\) makes \(d<\eta\), so pruning the second eigenvalue of the exact solution loses stability. The family therefore separates small matrix/residual errors from closed-loop stability.

## Assumptions and scope

All matrices are real, \(n\ge2\), and \(K\ge3\). The actuator has one column; \(C\) has two rows regardless of ambient dimension. The pair \((A,B)\) is stabilizable because the only unstable mode is actuated; \((C,A)\) is detectable because that mode is observed. Stabilizing means every closed-loop eigenvalue has strictly negative real part. Positive-semidefinite rank-one approximants may have arbitrary orientations, not just diagonal support. All errors use Frobenius norm. The finite-dimensional result is exact arithmetic; no floating-point robustness claim is made.

## Proof

**1. Exact solution and stability.** The CARE is diagonal at \(X_*\), with first equation \(-2(1)+2=0\), second equation
\[
2d-Kd^2+K^{-1}=0,
\]
which is an identity for \(d=(1+\sqrt2)/K\). The remaining equations vanish. Since \(G=Ke_2e_2^\top\),
\[
A-GX_*=\operatorname{diag}(-1,-\sqrt2,-1,\ldots,-1).
\]
To see uniqueness among stabilizing symmetric solutions, if another stabilizing solution \(Z\) existed, its difference \(W=Z-X_*\) would satisfy the Sylvester equation
\[
(A-GX_*)^\top W+W(A-GZ)=0.
\]
Both coefficient matrices are Hurwitz, so the Sylvester equation has only \(W=0\). This also establishes the advertised unique stabilizing positive-semidefinite solution.

**2. Spectral truncation.** The positive eigenvalues of \(X_*\) are \(1>d>0\). Eckart--Young's theorem (or direct diagonalization) makes \(Y_{\rm svd}=e_1e_1^\top\) the unique best symmetric positive-semidefinite rank-at-most-one approximant, at Frobenius distance \(d\). Its CARE residual equals \(K^{-1}e_2e_2^\top\), whereas \(A-GY_{\rm svd}=A\) has eigenvalue \(+1\).

**3. Necessary and sufficient stabilization constraint.** Every nonzero positive-semidefinite rank-one matrix is \(Y=zz^\top\). Put \(x=z_1^2\ge0\), \(y=z_2^2\ge0\), and \(w=\sum_{j=3}^{n}z_j^2\ge0\). Because \(G\) has only its second row nonzero, the eigenvalues of \(A-GY\) are \(-1\) (multiplicity \(n-1\)) and \(1-Ky\). Consequently
\[
A-GY\ \mathrm{Hurwitz}\quad\Longleftrightarrow\quad y>K^{-1}.
\]
In particular, rank zero cannot stabilize.

**4. Exact constrained optimum.** Expanding the Frobenius norm gives
\[
\begin{aligned}
\|X_*-zz^\top\|_F^2
&=(x+y+w)^2+1+d^2-2x-2dy\\
&\ge(x+y-1)^2+d^2+2(1-d)y\\
&>d^2+\frac{2(1-d)}{K},
\end{aligned}
\]
where \(d<1\) and \(y>K^{-1}\). For any \(y\in(K^{-1},1)\), take \(z=\sqrt{1-y}\,e_1+\sqrt y\,e_2\). Then \(w=0\), \(x+y=1\), and its squared error is exactly \(d^2+2(1-d)y\). Letting \(y\downarrow K^{-1}\) proves the lower bound is the unattained infimum, with no diagonal-orientation restriction.

**5. Exact gap.** Divide by the best spectral error \(d\):
\[
1+\frac{2(1-d)}{Kd^2}
=(6-4\sqrt2)K+3-2\sqrt2.
\]
The square root grows as \((2-\sqrt2)\sqrt K\). Meanwhile \(d=O(K^{-1})\), \(\|\mathcal R(Y_{\rm svd})\|_F=K^{-1}\), and the exact closed-loop margin is at least one independently of \(K\).

## Verification

The accompanying pure-Python `verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt2)\) for the scalar Riccati identity and sharp ratio at many integer values of \(K\), and direct matrix calculations for multiple dimensions and candidate orientations. Its finite tests are diagnostics, not substitutes for Steps 1--5. Reproduce with `python3 verify.py` from the directory containing that file; only the Python standard library is required. The executable is embedded alongside this result.

## Relationship to prior work

The 2026 mixed-precision CARE refinement paper of Zhang and Zhou introduces positive-eigenvalue truncation in its factor update and analyzes rounding/truncation contributions to residual accuracy. It does not supply the present exact rank-one stability-preserving approximation distance. The 2026 Massei--Saluzzi work explicitly imposes separate residual and stabilizing conditions when using a different, bandwidth-based truncation strategy, with a hypothesis that the uncorrected coefficient matrix is Hurwitz; that stronger base-stability setting does not cover this family, whose matrix \(A\) has an unstable eigenvalue. Classical RADI studies stabilizing low-rank Riccati iterates but does not give the sharp optimization ratio here. This finding concerns the **price of stability for an unrestricted rank-one PSD approximant**, not merely a generic perturbation counterexample.

## Limitations

The witness is a deliberately structured diagonal CARE family. The coefficient norm \(\|B\|_2=\sqrt K\) is unbounded; no fixed-gain impossibility is asserted. Detectability and stabilizability hold but their quantitative conditioning is not uniform as \(K\to\infty\). The result does not assert that an implementation necessarily prunes the unsafe mode, only that rank-one spectral pruning or an absolute/relative eigenvalue rule can do so. No direct implication is claimed for high-rank or noncommuting CAREs, or for algorithms that explicitly test the closed-loop spectrum and reject unstable truncations.

## References

- J. Zhang and Y. Zhou, *Newton-Based Mixed Precision Iterative Refinement for Large-Scale Sparse Continuous-Time Algebraic Riccati Equations*, arXiv:2607.14742, first version 2026-07-16, https://arxiv.org/abs/2607.14742 .
- S. Massei and L. Saluzzi, *On the data-sparsity of the solution of Riccati equations with applications to feedback control*, Numerische Mathematik (2026), https://doi.org/10.1007/s00211-026-01572-0 .
- P. Benner, Z. Bujanović, P. Kürschner and J. Saak, *RADI: a low-rank ADI-type algorithm for large scale algebraic Riccati equations*, Numerische Mathematik (2018), https://doi.org/10.1007/s00211-017-0907-5 .
- J. Skaf and S. Boyd, *Controller coefficient truncation using Lyapunov performance certificate*, International Journal of Robust and Nonlinear Control (2011), https://doi.org/10.1002/rnc.1577 .
