# An exact excitation-budget transition for the two-step scalar input-design oracle

## Finding

**Theorem (complete two-step oracle phase diagram).** Let a scalar state satisfy \(x_0=0\) and \(x_1=u_0+w\), where \(w\) is centered, has variance \(\sigma^2>0\), and is independent of the choice of \(u_0\). Set \(z_t=(x_t,u_t)^{\mathsf T}\) for \(t=0,1\). Take
\[
 Q=\begin{pmatrix}h&g\\g&j\end{pmatrix}\succ0,\qquad g\ne0,
\]
and allow any causal, possibly randomized controls with finite second moments. For a given \(\beta>\sigma^2\), maximize
\[
 J=\mathbb E\sum_{t=0}^1 z_t^{\mathsf T}Qz_t
 \quad\text{subject to}\quad
 \mathbb E\sum_{t=0}^1\|z_t\|_2^2\le\beta.
\]
Define
\[
 a=h-j,\quad b=|g|,\quad d=\sqrt{a^2+8b^2},\quad c=a/d\in(-1,1),\quad
 \beta_{\rm crit}=\sigma^2\frac{3-c}{1+c}.
\]
Then \(\beta_{\rm crit}>\sigma^2\). The optimal initial excitation energy is **uniquely** determined by
\[
 s_*=\mathbb E[u_0^2]
 =\max\left\{0,\frac{1+c}{4}(\beta-\beta_{\rm crit})\right\}.
\]
The complete optimal-policy characterization is that \(u_0\) may be any random variable independent of \(w\) with this second moment and that \(u_1=K_*x_1\) almost surely, where
\[
 K_*=\operatorname{sgn}(g)
 \begin{cases}
 \sqrt{\beta/\sigma^2-1},&\sigma^2<\beta\le\beta_{\rm crit},\\[3pt]
 \dfrac{4b}{a+d},&\beta\ge\beta_{\rm crit}.
 \end{cases}
\]
At the common endpoint the two formulas agree. Thus the feedback gain freezes at the critical budget, while additional optimal budget above it must enter through nonzero time-zero excitation. Such excitation may be deterministic or randomized; randomness is **not** necessary.

Writing \(q=\beta-\sigma^2\), the exact optimal value is
\[
 J_*(\beta)=h\sigma^2+jq+
 \begin{cases}
 2b\sigma\sqrt q,&\sigma^2<\beta\le\beta_{\rm crit},\\[3pt]
 \dfrac{a(q-2\sigma^2)+d(q+2\sigma^2)}4,&\beta\ge\beta_{\rm crit}.
 \end{cases}
\]
Among all policies with \(u_0=0\), the best value equals
\(J_{\rm no\,exc}=h\sigma^2+jq+2b\sigma\sqrt q\).
Therefore \(J_*>J_{\rm no\,exc}\) if and only if \(\beta>\beta_{\rm crit}\). This is also a strict optimality gap against all homogeneous linear state-feedback policies, since \(x_0=0\). The optimized value is continuously differentiable at the threshold. Below it, its derivative is \(j+b\sigma/\sqrt{\beta-\sigma^2}\) and its second derivative is negative; above it, the derivative freezes at \(j+(a+d)/4\) and the value is exactly affine in budget.

## Assumptions and scope

The horizon has precisely two scored state-input observations. The first state is zero, the scalar input coefficient is one, and the only state equation needed for the objective is \(x_1=u_0+w\); a general state-transition coefficient would have no effect at this horizon. The disturbance need not be Gaussian. Its future independence from the first control and its finite positive variance are essential. The weight \(Q\) is real symmetric positive definite with nonzero off-diagonal entry; the trace-budget weight is the identity. Controls are causal, can use internal randomization, and have finite second moments. The result is exact-arithmetic and finite-horizon. The linear objective is the negative of the linear minimization oracle for \(M=-Q\prec0\), not the outer nonlinear information-design objective.

## Proof

**1. Exact moment reduction.** Put \(s=\mathbb E u_0^2\), \(r=\mathbb E u_1^2\), and \(t=\mathbb E[x_1u_1]\). Since \(u_0\) is independent of the centered disturbance,
\[
 v:=\mathbb E x_1^2=\sigma^2+s,\quad
 \mathbb E\sum\|z_t\|_2^2=\sigma^2+2s+r,
\quad
 J=h(\sigma^2+s)+j(s+r)+2gt.
\]
The budget is active: if it had slack, adding to \(u_1\) an independent centered perturbation of sufficiently small positive variance would increase \(J\) by \(j\) times that variance, since \(j>0\). Hence \(r=q-2s\), with \(q=\beta-\sigma^2>0\) and \(0\le s\le q/2\). Cauchy–Schwarz gives \(|t|\le\sqrt{vr}\). Because \(g\ne0\), the maximally favorable correlation is \(t=\operatorname{sgn}(g)\sqrt{vr}\); it is attainable exactly by \(u_1=Kx_1\) with \(K=\operatorname{sgn}(g)\sqrt{r/v}\). Equality in Cauchy–Schwarz forces this proportionality almost surely at every maximizer. Thus the entire causal-control problem reduces **without relaxation** to
\[
 \max_{0\le s\le q/2}
 F(s),\qquad
 F(s)=h\sigma^2+jq+as+2b\sqrt{(\sigma^2+s)(q-2s)}.
\]
Every feasible \(s\) is realizable by an independent centered \(u_0\) with \(\mathbb E u_0^2=s\) and the displayed linear second-step control.

**2. Sharp constrained ellipse maximum.** Define
\[
 R=(q+2\sigma^2)/4,\qquad s_c=(q-2\sigma^2)/4.
\]
An exact completion of the square gives
\[
 (\sigma^2+s)(q-2s)=2\bigl(R^2-(s-s_c)^2\bigr).
\]
For \(0<s<q/2\), the second derivative of its square root is strictly negative: if \(v(s)=(\sigma^2+s)(q-2s)\), then
\[
 \frac{\mathrm d^2}{\mathrm ds^2}\sqrt{v(s)}
 =-\frac{2}{\sqrt{v(s)}}-\frac{(v'(s))^2}{4v(s)^{3/2}}<0.
\]
The derivative of \(F\) tends to \(-\infty\) at \(s=q/2\), so the upper endpoint is never optimal. The *unconstrained* maximizer of the ellipse support function is
\[
 s_{\rm ell}=s_c+R\frac{a}{\sqrt{a^2+8b^2}}
 =\frac{q(1+c)-2\sigma^2(1-c)}4.
\]
Strict concavity implies that the constrained maximizer is \(s_*=\max\{0,s_{\rm ell}\}\). The inequality \(s_{\rm ell}>0\) is equivalent to
\[
 \beta>\sigma^2\frac{3-c}{1+c}=\beta_{\rm crit};
\]
this proves the threshold and unique optimal initial second moment.

**3. Feedback and value formulas.** At \(s=0\), the equality case in Cauchy–Schwarz yields \(K=\operatorname{sgn}(g)\sqrt{q/\sigma^2}\). In the interior regime, \(s_*=s_{\rm ell}\), hence
\[
 \sigma^2+s_*=(q+2\sigma^2)(1+c)/4,\qquad
 q-2s_*=(q+2\sigma^2)(1-c)/2.
\]
Their ratio gives \(|K_*|=\sqrt{2(1-c)/(1+c)}=4b/(a+d)\). The unconstrained ellipse support is \(Rd\), yielding the second branch of \(J_*\), while the boundary \(s=0\) yields its first branch. Both value and gain branches agree at the threshold. Finally \(F\) is strictly concave, so for \(\beta>\beta_{\rm crit}\) its unique maximizer has \(s_*>0\), proving the strict gap against every \(s=0\) policy.

**4. Singular Riccati boundary (an explicit dual calculation).** For the minimization with stage weight \(\lambda I-Q\), the last-step scalar control curvature is \(S_1=\lambda-j\). When positive, its minimizing gain is \(K_1=g/(\lambda-j)\), in the sign convention \(u_1=K_1x_1\). The first-step control curvature, because \(x_0=0\), is
\[
 S_0=2\lambda-h-j-\frac{b^2}{\lambda-j}.
\]
Both are strictly positive precisely when
\[
 \lambda>\lambda_{\rm crit}
 :=j+\frac{a+d}{4}.
\]
Within this regular domain the first control vanishes and its budget is
\[
 b(\lambda)=\sigma^2\left[1+\frac{b^2}{(\lambda-j)^2}\right]
 <\sigma^2\frac{3-c}{1+c}=\beta_{\rm crit}.
\]
The right-hand side is approached as \(\lambda\downarrow\lambda_{\rm crit}\). In particular, the dual threshold multiplier equals the above-threshold derivative of the optimal value. Thus exactly when \(\beta>\beta_{\rm crit}\) the regular Riccati family cannot saturate the budget. The singular first-step direction at \(\lambda_{\rm crit}\) allows the excitation described above. This last step relates the explicit classification to the general singular-case mechanism already recognized in the source literature; it is not claimed as a new generic duality theorem.

## Verification

An exact witness takes \(\sigma^2=1\), \(Q=\begin{psmallmatrix}3&1\\1&1\end{psmallmatrix}\) and \(\beta=3\). It has
\[
 \beta_{\rm crit}=5-2\sqrt3,\quad
 \mathbb E u_0^2=1/\sqrt3,\quad
 u_1=(\sqrt3-1)x_1,
\]
with the optimal aggregated matrix
\[
 \Sigma_*=\begin{pmatrix}
 1+1/\sqrt3&2/\sqrt3\\
 2/\sqrt3&2-1/\sqrt3
 \end{pmatrix},\qquad
 \operatorname{tr}\Sigma_*=3.
\]
Its objective is \(5+2\sqrt3\); with \(u_0=0\), even the best arbitrary causal second-step policy is limited to \(5+2\sqrt2\). The strictly positive gap is \(2(\sqrt3-\sqrt2)\).

Run `python3 verify.py` alongside this document. The self-contained verifier uses exact rational quadratic-surd arithmetic to check the witness identities, and deterministic finite parameter trials to cross-check both branches and the scalar global inequality. Such finite checks corroborate but do not prove the universal result, which is established above.

## Relationship to prior work

Bencherki, Lee, Matni, and Rantzer [1] formulate the finite-horizon causal-covariance linear minimization oracle and solve regular cases by a Riccati recursion plus scalar bisection; their Section 4, Remark 2 already recognizes singular-boundary directions that permit extra input excitation. Their Appendix, Lemma 4 gives a general covariance-feasibility characterization. The present result does **not** claim discovery of the singular-boundary mechanism, convex moment feasibility, or ordinary Riccati theory. It supplies instead an exact, parameter-uniform **two-step scalar phase diagram**: the critical budget, uniquely optimal initial excitation second moment, frozen optimal gain, both optimal-value branches, and a strict quantified feedback-only gap. Those formulas are not stated in the inspected theorem, remark, or appendix of [1].

Wagenmaker, Simchowitz, and Jamieson [2] study task-optimal exploration and cost-sensitive system identification with broader systems but different performance criteria; Mutný, Janik, and Krause [3] study conditional-gradient exploration over Markov chain occupancy measures. The material examined does not establish the above exact two-step covariance-oracle formula. Any equivalent earlier special-case classification would supersede the originality assessment; no uniqueness conclusion follows from bibliographic searches alone.

## Limitations

This is a two-observation scalar control problem, not a multidimensional or arbitrary-horizon phase law. It optimizes a **linearized** covariance objective; it does not by itself solve the outer A-optimal inverse-information criterion. Gaussian noise is unnecessary; only independence, zero mean, and finite positive variance are used. The optimal nonzero initial input may be deterministic, so no necessity of randomized excitation is asserted. Strictness depends on \(g\ne0\) and \(Q\succ0\); diagonal or indefinite weights are not covered. There is no finite-precision or online system-identification guarantee. General singular-boundary optimality was previously known [1]; the original contribution asserted here is its explicit sharp scalar classification, still awaiting independent literature review.

## References

[1] F. Bencherki, B. Lee, N. Matni, and A. Rantzer, *Optimal input design via Frank–Wolfe*, arXiv:2609.08751, first submitted 2026-09-08, Sections 2–4 and Appendix 8.1, 8.4. https://arxiv.org/abs/2609.08751 . Lawful full-text rendering: https://documents.live/documents/display/Optimal-input-design-via-Frank-Wolfe .

[2] A. Wagenmaker, M. Simchowitz, and K. Jamieson, *Task-Optimal Exploration in Linear Dynamical Systems*, Proceedings of Machine Learning Research 139 (2021), 10641–10652. https://proceedings.mlr.press/v139/wagenmaker21a.html .

[3] M. Mutný, T. Janik, and A. Krause, *Active Exploration via Experiment Design in Markov Chains*, Proceedings of Machine Learning Research 206 (2023), 7349–7374. https://proceedings.mlr.press/v206/mutny23a.html .
