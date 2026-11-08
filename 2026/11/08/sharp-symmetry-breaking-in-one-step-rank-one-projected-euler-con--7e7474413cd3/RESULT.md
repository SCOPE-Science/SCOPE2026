# Sharp symmetry breaking in one-step rank-one projected Euler control

## Finding

A one-step, best-rank-one projected Euler scheme for a linear matrix equation can change a uniquely solvable linear-quadratic terminal-control problem into one with **exactly two distinct global control minimizers**. The transition has a sharp target-amplitude threshold despite a uniform gap between the first and second singular values of every matrix being truncated.

Let \(e_1,e_2\) be the canonical basis of \(\mathbb R^2\), and put
\[
Y_0=e_1e_1^\top=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
E=e_1e_2^\top+e_2e_1^\top=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
For a constant real control \(u\), apply one unit-length projected Euler step with the **exact best rank-one Frobenius retraction** \(\Pi_1\) to the linear state equation \(\dot X=uE\). The resulting terminal state is
\[
Y_1(u)=\Pi_1(Y_0+uE).
\]
For any target amplitude \(q\in\mathbb R\) and quadratic control weight \(\gamma\ge0\), consider the terminal objective
\[
J_{q,\gamma}(u)=\frac12\|Y_1(u)-qe_2e_2^\top\|_F^2+\frac\gamma2 u^2.
\]
Define the exact threshold \(q_{\mathrm c}=1+\gamma/2\). Then the set of **all** global minimizers is
\[
\operatorname*{argmin}_{u\in\mathbb R}J_{q,\gamma}(u)
=\begin{cases}
\{0\},&q\le q_{\mathrm c},\\
\{-u_*,u_*\},&q>q_{\mathrm c},
\end{cases}
\]
where \(u_*=(\delta_*^2-1)^{1/2}/2>0\), and \(\delta_*>1\) is the **unique** solution of
\[
(1+\gamma)\delta_*^3+(1-q)\delta_*^2-q=0
\qquad(\delta_*>1).
\]
When \(q>q_{\mathrm c}\), the zero control is a strict local maximum. At equality, it remains the unique global minimizer but has quartic (rather than quadratic) local growth:
\[
J_{q_{\mathrm c},\gamma}(u)-J_{q_{\mathrm c},\gamma}(0)
=\left(\gamma+\frac32\right)u^4+O(u^6).
\]
As \(h=q-q_{\mathrm c}\downarrow0\), the two optimal controls satisfy
\[
u_\pm=\pm\sqrt{\frac{h}{3+2\gamma}}\bigl(1+O(h)\bigr),
\quad
J_{q,\gamma}(u_\pm)-J_{q,\gamma}(0)
=-\frac{h^2}{2(3+2\gamma)}+O(h^3).
\]
Moreover, their **matrix retraction error tends to zero**:
\[
\|Y_1(u_\pm)-(Y_0+u_\pm E)\|_F
=\frac{h}{3+2\gamma}+O(h^2).
\]
Nevertheless, for **every** real \(u\), the two singular values of \(Y_0+uE\) are separated by exactly \(1\); the truncation has no singular-value crossing or ambiguity.

## Assumptions and scope

All matrices and controls are real. The time interval has length one. The state equation is \(\dot X=uE\), with constant scalar control \(u\in\mathbb R\) and initial state \(Y_0\) as defined above. The full state has terminal value \(X(1)=Y_0+uE\). The one-step projected Euler scheme uses the tangent projector onto the rank-one manifold at \(Y_0\), followed by the **unique** Frobenius-nearest rank-one matrix. Tracking is imposed only at the terminal time; \(q\) is any real number and \(\gamma\ge0\). Results concern exact arithmetic, one step and the global scalar control objective, not a multi-step or continuous-time optimizer.

The corresponding **unreduced** objective is
\[
J^{\mathrm{full}}_{q,\gamma}(u)
=\frac12\|Y_0+uE-qe_2e_2^\top\|_F^2+\frac\gamma2u^2
=\frac{1+q^2}{2}+\left(1+\frac\gamma2\right)u^2,
\]
which has the unique global minimizer \(u=0\) for every \(q\) and \(\gamma\) in the stated domain.

## Proof

**1. The scheme is a projected Euler step.** Write \(P_0=e_1e_1^\top\). The orthogonal tangent-space projector at the rank-one state \(Y_0=P_0\) is
\[
\mathcal P_{Y_0}(Z)=P_0Z+ZP_0-P_0ZP_0.
\]
Direct substitution gives \(\mathcal P_{Y_0}(E)=E\), hence a length-one projected Euler update, retracted by \(\Pi_1\), is exactly \(Y_1(u)=\Pi_1(Y_0+uE)\).

**2. Exact singular-value decomposition.** Put \(A(u)=Y_0+uE\) and \(\delta=\sqrt{1+4u^2}\). Its two eigenvalues are \(\lambda_+=(1+\delta)/2\) and \(\lambda_-=(1-\delta)/2\). Because \(\lambda_+>|\lambda_-|\) and \(\lambda_+-|\lambda_-|=1\), the leading singular component is unique for all real controls, including \(u=0\). Let
\[
P_+(u)=\frac{A(u)-\lambda_-I}{\delta}.
\]
This is the rank-one positive spectral projector, so \(Y_1(u)=\lambda_+P_+(u)\), and direct calculation gives
\[
\|Y_1(u)\|_F^2=\lambda_+^2
=\frac{1+\delta}{2}+u^2,
\qquad
[Y_1(u)]_{22}=\frac{u^2}{\delta},
\qquad
\|A(u)-Y_1(u)\|_F=|\lambda_-|=\frac{\delta-1}{2}.
\]

**3. Global scalar classification.** Substituting the identities into the objective yields the exact even function
\[
J_{q,\gamma}(u)
=\frac{q^2}{2}+\frac{1+\delta}{4}
+\frac{1+\gamma}{2}u^2
-\frac{qu^2}{\delta}.
\]
Set \(s=u^2\ge0\), \(\delta=\sqrt{1+4s}\), and \(a=1+\gamma\). Its derivative with respect to \(s\) is
\[
\frac{\mathrm dJ}{\mathrm ds}
=\frac12\left(a+\frac1\delta-q\frac{\delta^2+1}{\delta^3}\right)
=\frac{\delta^2+1}{2\delta^3}\bigl(T_\gamma(\delta)-q\bigr),
\qquad
T_\gamma(\delta)=\frac{a\delta^3+\delta^2}{\delta^2+1}.
\]
For all \(\delta\ge1\),
\[
T_\gamma'(\delta)
=\frac{a(\delta^4+3\delta^2)+2\delta}{(\delta^2+1)^2}>0,
\qquad T_\gamma(1)=\frac{a+1}{2}=q_{\mathrm c},
\quad \lim_{\delta\to\infty}T_\gamma(\delta)=\infty.
\]
Thus if \(q\le q_{\mathrm c}\), the objective is strictly increasing in \(s>0\) and has only the minimizer \(u=0\). If \(q>q_{\mathrm c}\), there is exactly one \(\delta_*>1\) satisfying \(T_\gamma(\delta_*)=q\), with negative derivative before this point and positive derivative after it. Hence it is the unique global minimum in \(s\), corresponding to exactly two global minimizers in \(u\). The zero control is then a strict local maximum since the coefficient of \(u^2\) is \(q_{\mathrm c}-q<0\). Clearing denominators gives the displayed cubic. This proves the classification over the entire parameter domain.

**4. Critical boundary and precision of truncation.** Taylor expansion in \(s\) at zero gives
\[
J_{q,\gamma}(u)-J_{q,\gamma}(0)
=(q_{\mathrm c}-q)s+\left(2q-\frac12\right)s^2+O(s^3).
\]
At \(q=q_{\mathrm c}\), the leading coefficient is \(\gamma+3/2\), establishing quartic growth. The implicit equation \(T_\gamma(\delta_*)=q_{\mathrm c}+h\), together with \(T_\gamma'(1)=(3+2\gamma)/2>0\), gives
\[
\delta_*-1=\frac{2h}{3+2\gamma}+O(h^2),
\quad
u_*^2=\frac{h}{3+2\gamma}+O(h^2).
\]
Substitution into the objective and into the exact residual norm \((\delta_*-1)/2\) gives the claimed cost-gap, control and retraction-error expansions. The singular gap remains exactly one by Step 2. The full-rank minimizer claim follows from the explicit strictly convex quadratic above. \(\square\)

## Verification

Run `python verify.py` using Python 3.9 or later with only its standard library. The checker constructs exact rational matrix decompositions from a Pythagorean parametrization, verifies the algebraic cost identity, and checks randomized global-phase and near-critical cases. It reports `REPRODUCIBILITY_OK: 1728 exact rational cost identities; 2500 numerical phase cases; 8 critical asymptotics`. The analytic monotonicity and global claims are proved above; finite checks are only supplementary.

## Relationship to prior work

Carrel and Vanzan (2026, Section 4.2, Remark 4.10 and Section 6.3) show why low-rank project-then-optimize control can be nonconvex and present numerical evidence of local-minimum behavior. Their continuous-time dynamical low-rank model is **not** the one-step Euler-retraction model considered here. Kieri and Vandereycken (2017 preprint, Section 4, equation (21); published 2018/2019) analyze projected Euler updates and general rank retractions but do not classify this target-dependent optimal-control objective. The present theorem combines these two ingredients in the minimum matrix size, gives an exact all-parameter global classification, and exhibits symmetry breaking with an entirely nondegenerate singular gap. A general warning about low-rank nonconvexity does not determine the threshold, the two global controls or their critical scaling.

## Limitations

This is a fully specified **one-step, terminal-cost** result with exact best-rank-one retraction, not a theorem about the continuous projected ODE, BUG integration, multiple steps, arbitrary target matrices, or an implemented large-scale solver. The two controls are globally optimal for the reduced cost but not the full cost. The chosen model is deliberately minimal; no universal threshold for other data is claimed. Equivalence to an unindexed historical algebraic example cannot be excluded by literature search alone. Numerical tests do not replace the proof, and no independent mathematical validation is asserted.

## References

1. B. Carrel and T. Vanzan, *Dynamical low-rank approximations for the optimal control of matrix ODEs*, arXiv:2610.29554v1, 21 October 2026, especially Remark 4.10, Sections 5 and 6. https://arxiv.org/html/2610.29554v1
2. E. Kieri and B. Vandereycken, *Projection methods for dynamical low-rank approximation of high-dimensional problems*, 2017 author preprint; published online 21 July 2018, *Computational Methods in Applied Mathematics* 19 (2019), 73–92, DOI: 10.1515/cmam-2018-0029. https://www.unige.ch/math/vandereycken/papers/preprint_Kieri_V_2017.pdf
