# A sharp rank-budget barrier for first-step original-energy descent in relaxed SAV optimization

## Finding

Consider a coherently initialized relaxed scalar auxiliary variable (RSAV) optimization step with a positive-semidefinite curvature operator. On every strictly convex quadratic, **universal descent of the original objective in the first state update** has the exact if-and-only-if condition

\[
 h(H-2L)\preceq2I.
\]

In particular, for every rank budget \(0\le r<d\), the largest possible universally safe time step is the exact spectral-tail cutoff

\[
 \sup_{L\succeq0,\ \operatorname{rank}L\le r} h_{\max}(H,L)=\frac{2}{\lambda_{r+1}(H)}.
\]

The best cutoff is attained by retaining half of each of the first \(r\) eigenvalues in the leading eigenspace. The necessity proof constructs an objective-increasing initial state of arbitrarily small norm whenever the cutoff is exceeded. This establishes a precise rank-versus-step-size limitation that is not captured by unconditional dissipation of the auxiliary modified energy.

## Assumptions and scope

Let \(d\ge1\), and let \(H\in\mathbb R^{d\times d}\) be symmetric positive definite with eigenvalues \(\lambda_1(H)\ge\cdots\ge\lambda_d(H)>0\). Let \(L\in\mathbb R^{d\times d}\) be an arbitrary symmetric positive-semidefinite operator, not assumed to commute with \(H\), and let \(C>0\) and \(h>0\). Set

\[
 f(x)=\frac12x^{\mathsf T}Hx,\quad g=Hx_0,\quad A=I+hL,\quad r_0=\sqrt{f(x_0)+C}.
\]

The first state update in the first-order SAV scheme, or in its relaxed variant prior to the scalar-only relaxation, is

\[
 x_1=x_0-\frac{h}{1+\frac{h}{2(f(x_0)+C)}g^{\mathsf T}A^{-1}g}\,A^{-1}g.
\tag{1}
\]

The scalar relaxation performed after (1) affects the auxiliary variable but not \(x_1\). The statement quantifies over **every** \(x_0\in\mathbb R^d\), keeping \(H,L,C,h\) fixed, and concerns only this first coherently initialized update. If \(r<d\), the rank budget applies to the curvature operator \(L\), not to the scalar correction induced by the SAV elimination.

## Proof

**1. Symmetric normalized form.** Define \(z=H^{1/2}x_0\) and the positive-definite matrix

\[
 B=hH^{1/2}(I+hL)^{-1}H^{1/2}.
\]

Since \(2f(x_0)=z^{\mathsf T}z\), the nonnegative scalar attenuation in (1) is

\[
 \eta=\frac{z^{\mathsf T}Bz}{\|z\|^2+2C},\qquad
 z_1=H^{1/2}x_1=\left(I-\frac{B}{1+\eta}\right)z.
\tag{2}
\]

For \(z\ne0\), positive definiteness of \(B\) and \(C>0\) imply \(\eta>0\). Thus \(\alpha=(1+\eta)^{-1}\) satisfies \(0<\alpha<1\).

**2. Exact universal descent criterion.** If \(B\preceq2I\), each eigenvalue \(\beta\) of \(B\) lies in \((0,2]\). Therefore \(0<\alpha\beta<2\) for every nonzero input, so every eigenvalue of \(I-\alpha B\) has modulus strictly below one. Consequently (2) gives \(\|z_1\|^2<\|z\|^2\), equivalently \(f(x_1)<f(x_0)\), whenever \(x_0\ne0\). The zero input remains fixed.

Conversely, suppose \(\lambda_{\max}(B)=\beta>2\), and take a unit eigenvector \(v\) for that eigenvalue. Let \(z=t v\), \(t>0\), so that \(\eta=t^2\beta/(t^2+2C)\to0\) as \(t\downarrow0\). Then

\[
 \frac{\|z_1\|^2}{\|z\|^2}
 =\left(1-\frac{\beta}{1+\eta}\right)^2
 \longrightarrow (1-\beta)^2>1.
\]

Therefore all sufficiently small positive \(t\) produce an increase in the original objective. This also shows why dissipation of the scalar modified energy alone cannot imply original-energy descent.

**3. Equivalent Loewner inequality.** Since \(H\) and \(I+hL\) are positive definite, congruence and inversion order imply

\[
 B\preceq2I
 \ \Longleftrightarrow\ 
 h(I+hL)^{-1}\preceq2H^{-1}
 \ \Longleftrightarrow\ 
 hH\preceq2(I+hL)
 \ \Longleftrightarrow\ 
 h(H-2L)\preceq2I.
\]

Writing \(\mu=\lambda_{\max}(H-2L)\), all positive \(h\) satisfy this inequality if \(\mu\le0\), whereas precisely \(0<h\le2/\mu\) satisfy it if \(\mu>0\). The threshold includes equality because \(C>0\) makes \(\alpha<1\) for nonzero inputs.

**4. Sharp rank cutoff.** Suppose \(\operatorname{rank}L\le r<d\). The nullspace of \(L\) has dimension at least \(d-r\). By the Courant–Fischer min–max principle, some unit vector \(v\in\ker L\) has \(v^{\mathsf T}Hv\ge\lambda_{r+1}(H)\). Since \(Lv=0\),

\[
 \lambda_{\max}(H-2L)\ge v^{\mathsf T}(H-2L)v
 =v^{\mathsf T}Hv\ge\lambda_{r+1}(H).
\]

For an orthonormal eigenbasis \(u_i\) of \(H\), take

\[
 L_*=\frac12\sum_{i=1}^{r}\lambda_i(H)u_iu_i^{\mathsf T}.
\]

It has rank \(r\) and \(H-2L_*\) has eigenvalues \(0\) (\(r\) copies) and \(\lambda_{r+1}(H),\ldots,\lambda_d(H)\). Thus the lower bound is attained, establishing the spectral-tail optimum. For \(r=0\), the empty sum means \(L_*=0\). If full rank is allowed, taking \(L=H/2\) makes the first state step strictly descending for every finite \(h>0\).

## Verification

The self-contained `verify.py` executes randomized symmetric positive-definite, **noncommuting** curvature-operator tests, checks both sides of the Loewner criterion, constructs small-amplitude counterexamples beyond the frontier, and verifies optimal rank truncations. A run with NumPy completed **17,663 recorded numerical checks**. These finite tests are diagnostic, not substitutes for the analytic argument in the preceding section.

An exact small example is \(H=\operatorname{diag}(9,4,1)\). With rank one, \(L_*=\operatorname{diag}(9/2,0,0)\) and the sharp time-step ceiling is \(h=1/2\). With rank two, \(L_*=\operatorname{diag}(9/2,2,0)\) and the ceiling becomes \(h=2\). Whenever the respective threshold is exceeded, a sufficiently small initial state aligned with an uncovered extremal direction has strictly increasing objective after the first step.

## Relationship to prior work

Sagawa, Furihata and Miyatake [1] define the relevant SAV and N-RSAV state updates (their equations (5)–(6)), use a positive-semidefinite low-rank approximation as a curvature operator, and prove original-objective decrease under a conservative smoothness-dependent step restriction (their Theorem 4.6). Their algorithm dissipates the modified energy unconditionally. The result here instead gives the **exact necessary and sufficient first-step original-objective condition** for every strictly convex quadratic, including noncommuting curvature operators, and the sharp optimizer over all positive-semidefinite rank-constrained operators. It does not replace the source's all-iteration analysis.

Shen and Zhao [2] study original-energy dissipation for a different relaxed SAV gradient-flow formulation, without this first-step spectral rank bound. Zhang and Shen [3] develop pullback-corrected SAV schemes with variable-rank corrections induced by component decompositions; those corrections are not the fixed auxiliary curvature operator in (1), and their modified-energy results do not imply the present rank-constrained threshold. The established SAV optimization formulation of Zhang et al. [4] explains the modified-versus-original-energy distinction but supplies no sharp spectral-tail rank-budget classification identified here.

## Limitations

The result is a first-step theorem with coherent scalar initialization, not a claim about later relaxed iterations when the auxiliary scalar need not match the original objective. It assumes a fixed positive-definite quadratic, exact linear solves, real arithmetic, and a positive-semidefinite curvature operator; it does not analyze random-sample quality of a Nyström approximation or finite-precision effects. The rank result is a worst-case best-achievable step-size guarantee, not an optimization of computational cost or iteration complexity. As in any literature comparison, unidentified equivalent classical matrix-scaling or SAV identities remain possible.

## References

[1] R. Sagawa, D. Furihata, Y. Miyatake, *Accelerating SAV-based optimization via randomized low-rank Hessian approximation*, arXiv:2606.10562v1 (first public 2026-06-09). https://arxiv.org/abs/2606.10562

[2] J. Shen, C. Zhao, *The original energy dissipation law of the R-SAV approach for gradient flows*, Applied Mathematics Letters 177 (2026), 109905, DOI 10.1016/j.aml.2026.109905. https://www.math.purdue.edu/~shen7/pub/SZ_AML26.pdf

[3] S. Zhang, J. Shen, *Scalar-Tracking SAV Schemes with Pullback Corrections for Gradient Flows*, arXiv:2606.18551v1 (first public 2026-06-17). https://arxiv.org/abs/2606.18551

[4] *An efficient and robust SAV based algorithm for discrete gradient systems arising from optimizations*, arXiv:2301.02942. https://arxiv.org/abs/2301.02942
