# Two finite-perturbation phase boundaries for recycled spectral scaling

## Finding

Let \(m\ge 1\), \(a>b>c>0\), and \(0<\tau<\sqrt{ab}\). Consider the positive-definite matrix
\[
A_\tau=\begin{pmatrix}
a&\tau&0\\
\tau&b&0\\
0&0&cI_m
\end{pmatrix}
\]
with reference matrix \(A_0=\operatorname{diag}(a,b,cI_m)\). Recycle the reference top eigenvector \(e_1\) using the one-parameter symmetric spectral preconditioner
\[
U_\theta=\operatorname{diag}(\sqrt{\theta/a},1,I_m),\qquad
B_\theta=U_\theta A_\tau U_\theta,\qquad\theta>0.
\]
Set \(v=\tau^2/a\), \(d=b-c\), and \(v_1=d^2/b\), so \(0<v<b\) and \(0<v_1<d\). The **unique** minimizer of the spectral condition number \(\kappa_2(B_\theta)\) is
\[
\theta_*=\begin{cases}
\dfrac{cd}{d-v},&0<v\le v_1,\\[3pt]
b,&v_1\le v<b,
\end{cases}
\]
where the two expressions agree at \(v=v_1\). The sharp minimum equals
\[
\kappa_* = \begin{cases}
\dfrac bc+\dfrac{v}{d-v},&0<v\le v_1,\\[4pt]
\dfrac{b+\sqrt{bv}}{b-\sqrt{bv}},&v_1\le v<b.
\end{cases}
\]

There is a **second**, different threshold for exact-arithmetic preconditioned conjugate gradients (PCG). Some finite \(\theta>0\) makes PCG terminate within two iterations for **every right-hand side and every initial guess** if and only if \(v<d\). In this case the unique such parameter is
\[
\theta_{\mathrm{coll}}=\frac{cd}{d-v}.
\]
For \(v>v_1\), the condition-number minimizer \(\theta_*=b\) has three distinct eigenvalues, and generic right-hand sides require three PCG iterations; when \(v_1<v<d\), the two-step choice \(\theta_{\mathrm{coll}}>b\) exists but has strictly worse condition number. Moreover,
\[
\kappa_2(B_{\theta_{\mathrm{coll}}})
=\frac bc+\frac{v}{d-v}\longrightarrow+\infty
\qquad(v\uparrow d),
\]
while the optimal condition number remains finite at \(v=d\). Thus exact two-step termination and best spectral conditioning become incompatible above \(v_1\), and two-step termination becomes impossible at and above \(d\). Equivalently the perturbation-amplitude transitions occur at \(\tau=\sqrt{a}\,(b-c)/\sqrt b\) and \(\tau=\sqrt{a(b-c)}\).

## Assumptions and scope

All matrices, vectors, and arithmetic are real, and CG/PCG mean the usual symmetric positive-definite Krylov procedure in exact arithmetic. The reference top eigenvector is known exactly, but it is generally not an eigenvector of the perturbed system. The perturbation changes only the coupling between the two isolated reference modes; the \(m\)-dimensional low-frequency bulk stays at \(c\). The conjugate-gradient iteration count refers to applying ordinary CG to the split system \(B_\theta y=U_\theta f\), then mapping back to \(x=U_\theta y\). Consequently the statements hold for arbitrary right-hand side \(f\) and arbitrary starting guess \(y_0\). The parameter \(\tau\) may be any value in the complete SPD range, not only an asymptotically small perturbation.

## Proof

**Step 1: spectral reduction.** Since \(\tau^2<ab\), the leading two-by-two principal block of \(A_\tau\) is SPD, hence so is \(A_\tau\). By direct congruence,
\[
B_\theta=\begin{pmatrix}
\theta&\sqrt{\theta v}&0\\
\sqrt{\theta v}&b&0\\
0&0&cI_m
\end{pmatrix}.
\]
Write \(\ell_\pm(\theta)=(\theta+b\pm\sqrt{(\theta-b)^2+4\theta v})/2\) for the two eigenvalues of its leading block. Its determinant is \(\theta(b-v)>0\), so \(0<\ell_-<\ell_+\), and \(\ell_+>b>c\) because \(v>0\). Therefore
\[
\kappa_2(B_\theta)=\frac{\ell_+(\theta)}{\min\{c,\ell_-(\theta)\}}.
\]
The flat-bulk multiplicity does not enter this formula.

**Step 2: exact collision criterion.** Since \(\ell_+(\theta)>c\), the sign of \(\ell_-(\theta)-c\) is the sign of the characteristic polynomial at \(c\), which is
\[
(\theta-c)(b-c)-\theta v=\theta(d-v)-cd.
\]
If \(v<d\), this changes sign once, at \(\theta_{\mathrm{coll}}=cd/(d-v)\). If \(v\ge d\), it is always negative. Thus precisely when \(v<d\), and at precisely one positive scale, the spectrum collapses to the two distinct values \(c\) and \(\ell_+(\theta_{\mathrm{coll}})=\theta_{\mathrm{coll}}+b-c\). For an SPD matrix, CG terminates in at most the number of its distinct eigenvalues, for all initial residuals. When three distinct eigenvalues occur, a residual having nonzero projections onto each of their eigenspaces has minimal polynomial of degree three and cannot terminate at step two. This proves both directions of the universal two-step assertion, including its uniqueness.

**Step 3: global condition-number optimum.** On the region \(\ell_-\le c\), the full condition number is the condition number of the leading two-by-two block. Its trace is \(\theta+b\) and determinant \(\theta(b-v)\). For a fixed positive determinant-to-trace-squared ratio, the two-by-two eigenvalue condition number decreases strictly as that ratio increases. Here
\[
\frac{\det}{\operatorname{tr}^2}=
\frac{\theta(b-v)}{(\theta+b)^2},
\]
whose unique maximizer on \(\theta>0\) is \(\theta=b\), increasing strictly before \(b\) and decreasing strictly afterward. On the region \(\ell_-\ge c\), by contrast, \(\kappa_2(B_\theta)=\ell_+(\theta)/c\). The function \(\ell_+(\theta)\) is strictly increasing in \(\theta\): indeed, differentiating the positive simple generalized eigenvalue under the congruence \(\operatorname{diag}(\sqrt\theta,1)\), the derivative with respect to \(\log\theta\) is \(\ell_+(\theta)\) times the squared first coordinate of its normalized eigenvector, which is positive as \(v>0\). Alternatively this follows directly from the displayed quadratic formula.

If \(v<d\), the collision occurs at \(\theta_{\mathrm{coll}}\), with \(\ell_-<c\) below it and \(\ell_->c\) above it. As a result the full condition number decreases up to \(\min\{b,\theta_{\mathrm{coll}}\}\) and increases thereafter. If \(v\ge d\), the smaller block eigenvalue remains below \(c\), and the global minimizer is \(b\). Finally
\[
\theta_{\mathrm{coll}}\le b
\quad\Longleftrightarrow\quad
v\le\frac{(b-c)^2}{b}=v_1.
\]
This proves uniqueness and the two cases for \(\theta_*\). At collision, \(\ell_+ = \theta_{\mathrm{coll}}+b-c\); substitution yields \(\kappa_*=b/c+v/(d-v)\). At \(\theta=b\), the leading block eigenvalues are \(b\pm\sqrt{bv}\); for \(v\ge v_1\), the smaller one does not exceed \(c\), yielding \(\kappa_*=(b+\sqrt{bv})/(b-\sqrt{bv})\). The expressions coincide at the boundary. In the incompatible regime \(v_1<v<d\), strict uniqueness of the minimizer gives the strict conditioning penalty for the collision scale. Letting \(v\uparrow d\) proves its divergence, while \(\kappa_*(d)=(b+\sqrt{bd})/(b-\sqrt{bd})<\infty\) because \(d<b\). All claimed boundaries follow.

## Verification

The standalone `check_preconditioner.py` executes exact-rational collision and branch identities, 4,000 deterministic randomized parameter tests in various bulk dimensions, one-dimensional scans around each predicted global optimum, and actual CG recurrences on explicit weak, incompatible, and impossible-resonance cases. It passed 44,183 checks. This code is supplementary validation of formulas; the proof above establishes the assertions for all admissible real parameters and dimensions.

For a reproducible rational example, take \(a=9\), \(b=4\), \(c=1\). At \(v=1\), \(\theta_*=\theta_{\mathrm{coll}}=3/2\), with spectrum \(\{1,9/2\}\) and condition number \(9/2\), whereas \(\theta=4\) has condition number \(6\). At \(v=5/2\), the unique condition minimizer is \(\theta_*=4\), with condition number \((4+\sqrt{10})/(4-\sqrt{10})<9\), but the two-step scale is \(\theta_{\mathrm{coll}}=6\), with spectrum \(\{1,9\}\) and condition number \(9\). At \(v=3\), no finite two-step tuning is possible.

## Relationship to prior work

Diouane, Gürol, Mouhtal, and Orban (2026, arXiv:2610.28808) study the exact same *recycled reference eigenvector* spectral-preconditioner mechanism for perturbed SPD systems, giving perturbative PCG-versus-deflated-CG estimates; they do not supply this nonasymptotic condition-number minimizer or its two iteration-count boundaries in a flat-bulk rank-two coupling. The preceding paper (arXiv:2603.28969) studies optimal spectral cluster placement for a fixed iteration budget when the spectral information belongs to the system itself; it does not furnish the perturbation-dependent collision law. Giraud and Gratton (2006) provide first-order sensitivity analysis for approximate spectral preconditioners. Braatz and Morari (1994) provide a general convex optimization procedure for Euclidean matrix scaling, which is broader computational coverage of scaling optimization but does not state the two closed-form thresholds or the PCG minimal-polynomial implications. The source methods and classical eigenvalue/CG facts are credited; the new claim is their sharp joint characterization for this specified perturbation model.

## Limitations

This theorem is confined to a flat-bulk, two-isolated-mode reference spectrum with a single off-diagonal coupling, one selected reference eigenvector, exact arithmetic and a one-parameter symmetric preconditioner. It is **not** an assertion that condition-number minimization predicts the optimal finite-step CG energy error for arbitrary right-hand sides, or that floating-point Krylov methods terminate exactly. There is no claimed result for general perturbations coupling all bulk coordinates. As with specialized explicit matrix scaling formulas, unindexed earlier treatments may exist; originality remains subject to external expert priority assessment.

## References

1. Y. Diouane, S. Gürol, O. Mouhtal, D. Orban, *Deflation-Based Spectral Preconditioning for the Conjugate Gradient Method on Perturbed Systems*, arXiv:2610.28808 (first version 2026-10-20), https://arxiv.org/abs/2610.28808.
2. Y. Diouane, S. Gürol, O. Mouhtal, D. Orban, *A Spectral Preconditioner for the Conjugate Gradient Method with Iteration Budget*, arXiv:2603.28969 (2026-03-30), https://arxiv.org/abs/2603.28969.
3. L. Giraud, S. Gratton, *On the Sensitivity of Some Spectral Preconditioners*, SIAM J. Matrix Anal. Appl. 27 (2006), 1089–1105, https://doi.org/10.1137/040617546.
4. R. D. Braatz, M. Morari, *Minimizing the Euclidean Condition Number*, SIAM J. Control Optim. 32 (1994), 1763–1768, https://doi.org/10.1137/S0363012992238680.
