# A sharp angular safety frontier for rank-one spectral preconditioning and Gaussian power sketches

## Finding
Let a linear system have a single exceptional high-curvature direction. For the family of **positive rank-one deflating corrections**, a correction direction can improve the spectral condition number by some amount **exactly when its acute angle to the true spike is smaller than 45 degrees**. Below that accuracy, *every* nontrivial contraction of the proposed direction fails to improve conditioning. An optimal scalar correction, a generally stricter threshold for nominal inverse-eigenvalue correction, and the complete Gaussian power-sketch success probabilities are explicit.

Specifically, let \(n\ge2\), \(\kappa>1\), and \(u,v\in\mathbb R^n\) be unit vectors. Define
\[
H=I+(\kappa-1)uu^\mathsf T,\qquad
P_p=I+(p-1)vv^\mathsf T,\qquad 0<p\le1,
\]
and \(w=(u^\mathsf Tv)^2\). Set \(K(p)=\kappa_2(P_p^{1/2}HP_p^{1/2})\). Then
\[
\boxed{p_* = \min\!\left\{1,\frac{\kappa-(\kappa-1)w}{1+(\kappa-1)w}\right\}},
\qquad \boxed{\exists p<1:\ K(p)<\kappa\iff w>\tfrac12}.
\]
For \(w>1/2\), write \(t=(\kappa-1)^2w(1-w)/\kappa\); then
\[
\boxed{\min_{0<p\le1}K(p)=(\sqrt{1+t}+\sqrt{t})^2},
\]
whereas the minimum is \(\kappa\) if \(w\le1/2\). For the unadjusted inverse-spike coefficient \(p=1/\kappa\), strict improvement requires the stronger angular accuracy
\[
\boxed{w>1-\frac{\sqrt\kappa}{(1+\sqrt\kappa)^2}}.
\]

To quantify the randomness of a single power-sketch direction, let \(g\sim N(0,I_n)\), let \(q\ge0\) be an integer, and set \(v=H^qg/\|H^qg\|_2\). Let \(F_{1,n-1}\) be an \(F\)-distributed random variable with the indicated degrees of freedom. Then
\[
\boxed{\Pr\{\exists p<1:K(p)<\kappa\}
=\Pr\!\left\{F_{1,n-1}>\frac{n-1}{\kappa^{2q}}\right\}},
\]
and
\[
\boxed{\Pr\{K(\kappa^{-1})<\kappa\}
=\Pr\!\left\{F_{1,n-1}>
\frac{(n-1)(\sqrt\kappa+1+\kappa^{-1/2})}{\kappa^{2q}}\right\}}.
\]
If along dimensions \(n\to\infty\) the ratio \(\kappa^{2q}/(n-1)\) tends to \(c\in(0,\infty)\), the first probability tends to \(\operatorname{erfc}(1/\sqrt{2c})\); it tends to zero and one at the respective endpoints \(c=0\) and \(c=\infty\).

## Assumptions and scope
Everything is in real exact arithmetic. \(H\) is the specified one-spike symmetric positive-definite matrix; \(P_p\) is a *particular* spectral low-memory correction that reduces the weight of a unit approximate eigenvector \(v\), with \(p\in(0,1]\). Its matrix square root is well-defined and positive definite. Neither the angle nor \(p_*\) is assumed computationally observable. The Gaussian random vector has independent standard-normal coordinates. The power-sketch model uses \(H^qg\), not a claim of equivalence to every randomized eigensolver. There is no claimed improvement in actual conjugate-gradient iteration counts for every right-hand side.

## Proof
Choose \(z\perp u\) in the span of \(u\) and \(v\), and orient signs so that \(v=\sqrt w\,u+\sqrt{1-w}\,z\). When \(w=1\), take any \(z\perp u\). The nonscalar part of the product \(P_pH\) lies in this two-dimensional space, and \(P_pH\) is similar to \(P_p^{1/2}HP_p^{1/2}\). Its two active eigenvalues have trace
\[
T(p)=\kappa+p+(p-1)(\kappa-1)w
\]
and determinant \(\kappa p\). Every remaining eigenvalue, when present, equals one. Thus
\[
\lambda_\pm(p)=\frac{T(p)\pm\sqrt{T(p)^2-4\kappa p}}2.
\]
The characteristic polynomial at one has value
\[
1-T(p)+\kappa p=(\kappa-1)(p-1)(1-w)\le0,
\]
so \(\lambda_-\le1\le\lambda_+\), including endpoints. Therefore \(K(p)=\lambda_+/\lambda_-\), regardless of ambient dimension. It is increasing in the normalized trace \(T(p)/\sqrt{\kappa p}\ge2\), because the two positive roots have fixed product \(\kappa p\).

Write \(a=\kappa-(\kappa-1)w>0\) and \(b=1+(\kappa-1)w>0\). Direct rearrangement gives
\[
\frac{T(p)}{\sqrt{\kappa p}}=
\frac{a/\sqrt p+b\sqrt p}{\sqrt\kappa}.
\]
The derivative has the sign of \(bp-a\); hence the unconstrained minimizer is \(p=a/b\), and its restriction to \((0,1]\) is the claimed \(p_*\). It is strictly below one precisely when \(a<b\), or \(w>1/2\). When \(w\le1/2\), the unique minimum on the permitted interval is \(p=1\), with \(K(1)=\kappa\); every \(p<1\) is strictly worse. When \(w>1/2\),
\[
\frac{a b}{\kappa}=1+\frac{(\kappa-1)^2}{\kappa}w(1-w)=1+t.
\]
The minimum normalized trace is \(2\sqrt{1+t}\). The corresponding reciprocal eigenvalue ratio is \((\sqrt{1+t}+\sqrt t)^2\), proving the optimum formula, including \(w=1\).

For the nominal \(p=1/\kappa\), the normalized trace equals
\[
T(\kappa^{-1})=\kappa+\kappa^{-1}
-\frac{(\kappa-1)^2}{\kappa}w.
\]
The baseline normalized trace at \(p=1\) equals \((\kappa+1)/\sqrt\kappa\). Their strict comparison rearranges exactly to \(w>1-\sqrt\kappa/(1+\sqrt\kappa)^2\). At equality the condition numbers are equal.

Choose coordinates with \(u=e_1\). If \(X=g_1^2\) and \(Y=\sum_{i=2}^n g_i^2\), independence of Gaussian coordinates gives independent \(X\sim\chi^2_1\) and \(Y\sim\chi^2_{n-1}\). Since \(H^q\) acts by \(\kappa^q\) on \(u\) and by one on its orthogonal complement,
\[
w=\frac{\kappa^{2q}X}{\kappa^{2q}X+Y}.
\]
Consequently \(w>1/2\) is exactly \(F_{1,n-1}:=(n-1)X/Y>(n-1)/\kappa^{2q}\). The inverse-scale threshold has odds \(w_0/(1-w_0)=\sqrt\kappa+1+\kappa^{-1/2}\), yielding the second probability. Finally \(Y/(n-1)\to1\) in probability, so the first event converges in probability threshold to \(X>1/c\). Its probability tends to \(\operatorname{erfc}(1/\sqrt{2c})\) by continuity of the \(\chi^2_1\) law. The endpoint limits follow by the same ratio argument. This completes the proof.

## Verification
The standalone `check.py` verifies the active two-dimensional characteristic polynomial with exact rational traces, compares predicted eigenvalues against direct dense symmetric eigensolves in dimensions two, three, five and ten, numerically checks the unique scalar optimizer and the fixed inverse-scale threshold, compares Gaussian simulation against the exact \(F\)-tail formula in five configurations, and cross-checks the isotropic \(\operatorname{Beta}\) law. It outputs `VERIFY_OK` and `VERIFY_FIXED_SCALE_AND_OPTIMAL_FORMULA_OK` when successful. These finite tests support implementation fidelity, not the infinite quantifiers; the proof above supplies the latter.

## Relationship to prior work
Daužickaitė, Gürol, Destouches, Berre and Weaver (2026) introduce randomized leading-eigenpair construction for a scaled spectral limited-memory preconditioner in variational data assimilation, including a power-sketch strategy and practical concerns about approximate eigenvectors. The present work isolates the analytic one-spike, one-direction conditioning question and answers it exactly, including a Gaussian success probability; it does not analyze their full ensemble-based algorithm. Diouane, Gürol, Mouhtal and Orban (2026) optimize spectral cluster placement **with exact eigenvectors**, and their convergence statements do not imply an angular safety frontier for approximate directions. Gratton, Sartenaer and Tshimanga (2011) establish limited-memory preconditioner identities and scaling results, with different preconditioner parameterizations and no such one-spike Gaussian threshold. Giraud and Gratton (2006) study perturbations of spectral preconditioners through *first-order eigenvalue expansions*, not an exact finite-angle minimization and probability law. These are implication comparisons, not a claim that all historical literature has been exhausted.

## Limitations
This is not an assertion that a typical randomized Ritz procedure returns precisely \(H^qg/\|H^qg\|_2\), nor that its practical scaling is the oracle \(p_*\). The 45-degree barrier concerns positive rank-one *deflation-only* corrections \(0<p\le1\); permitting inflation \(p>1\), additional correction directions, or a general spectrum changes the problem. Spectral condition number is a coarse proxy for CG convergence; initial residuals, clustering and stopping budgets matter. No independent mathematical audit has been performed. Unlocated historically equivalent two-by-two conditioning computations remain a possible priority risk.

## References
- I. Daužickaitė, S. Gürol, M. Destouches, L. Berre and A. T. Weaver, *Accelerating an ensemble of variational data assimilations with randomized preconditioning*, arXiv:2605.23571v1 (first posted 22 May 2026), https://arxiv.org/abs/2605.23571 . Sections 3.1 and 3.2.
- Y. Diouane, S. Gürol, O. Mouhtal and D. Orban, *A Spectral Preconditioner for the Conjugate Gradient Method with Iteration Budget*, arXiv:2603.28969v1 (2026), https://arxiv.org/abs/2603.28969 . Sections 3 and 4.
- S. Gratton, A. Sartenaer and J. Tshimanga Ilunga, *On a Class of Limited Memory Preconditioners for Large Scale Linear Systems with Multiple Right-Hand Sides*, Optimization Online manuscript (2008), https://optimization-online.org/wp-content/uploads/2008/12/2166.pdf . Sections 2.3 and 3.2–3.3.
- L. Giraud and S. Gratton, *On the Sensitivity of Some Spectral Preconditioners*, SIAM J. Matrix Anal. Appl. **27** (2006), 1089–1105, https://doi.org/10.1137/040617546 . Sections 2 and 3.
