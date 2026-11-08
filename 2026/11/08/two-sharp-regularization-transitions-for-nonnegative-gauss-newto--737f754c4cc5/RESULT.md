# Two sharp regularization transitions for nonnegative Gauss–Newton steps on SPD quadratics

## Finding

Let \(d\ge2\), let \(H\) be a real symmetric positive-definite \(d\times d\) matrix with **actual** extremal eigenvalues \(0<a<b\), and write
\[
f(x)=\tfrac12 x^\top Hx,\qquad
G_\sigma(x)=x-\frac{\sigma}{1+\sigma\|Hx\|_2^2/(x^\top Hx)}Hx
\quad (x\ne0,\ \sigma>0).
\]
This is the deterministic nonnegative Gauss–Newton (NGN) gradient update with a fixed regularization parameter \(\sigma\) for a zero-minimum quadratic, as defined by Orvieto and Xiao [1]. The update is extended by \(G_\sigma(0)=0\).

**Theorem (exact all-state objective envelope).** The sharp ratio
\[
Q_\sigma(a,b)=\sup_{x\ne0}\frac{f(G_\sigma(x))}{f(x)}
\]
is
\[
\boxed{
Q_\sigma(a,b)=
\begin{cases}
(1+a\sigma)^{-2},& (b-a)\sigma(1+a\sigma)\le2,\\[2mm]
\displaystyle\frac{4+\sigma^2(b-a)^2}
{4\sigma(a+b+ab\sigma)},&(b-a)\sigma(1+a\sigma)>2.
\end{cases}}
\]
The branch transition \(\sigma_{\rm mode}\) is the unique positive solution of \((b-a)\sigma(1+a\sigma)=2\). Before this transition a vector in the \(a\)-eigenspace maximizes the ratio; after it the unique optimal **spectral mass distribution** uses only the \(a\)- and \(b\)-eigenspaces. For the latter branch its \(H\)-weighted mean eigenvalue is
\[
\boxed{m_\sigma=
\frac{\sigma(a+b)+2\sigma^2ab-2}
{\sigma(2+\sigma(a+b))}.}
\]
Explicitly the normalized \(H\)-weighted masses of the \(a\) and \(b\) eigenspaces are respectively \((b-m_\sigma)/(b-a)\) and \((m_\sigma-a)/(b-a)\). Thus the envelope is attained for every such \(H\), not just for a freely chosen spectrum.

The envelope has a **unique finite minimizer**
\[
\boxed{\sigma_{\rm opt}=\frac{2(a+b)}{(b-a)^2},\qquad
\min_{\sigma>0}Q_\sigma(a,b)=\left(\frac{b-a}{b+a}\right)^2.}
\]
This sharp objective factor equals the familiar minimax one-step quadratic objective factor for optimally fixed-step gradient descent, but the NGN step is state-dependent and generally differs from that fixed step. At \(\sigma_{\rm opt}\) the extremizing spectral mean is \(2ab/(a+b)\), and the adaptive step at that extremizer is \(2/(a+b)\).

Let \(\kappa=b/a\). Every nonzero state has \(f(G_\sigma(x))\le f(x)\) precisely under either of the following conditions:
\[
\boxed{\kappa\le3+2\sqrt2\quad\text{(all finite \(\sigma>0\))},}
\]
or
\[
\boxed{\kappa>3+2\sqrt2\quad\text{and}\quad
0<\sigma\le\sigma_{\rm safe}:=
\frac2{a+b-2\sqrt{2ab}}.}
\]
For \(\kappa>3+2\sqrt2\), equality at a nonzero state occurs at \(\sigma=\sigma_{\rm safe}\), and a strict objective increase is attainable for every \(\sigma>\sigma_{\rm safe}\). For smaller \(\sigma\), and for all finite \(\sigma\) when \(\kappa\le3+2\sqrt2\), the decrease is strict at every nonzero state.

For an exact witness take \(H=\operatorname{diag}(1,10)\), \(\sigma=2\), and \(x=(\sqrt{950},\sqrt{13})^\top\). The step is \(12/31\), and
\[
\boxed{\frac{f(G_2(x))}{f(x)}=\frac{41}{31}>1.}
\]
The result concerns *one-step objective decrease*, not the broader long-run convergence guarantees in [1].

## Assumptions and scope

All matrices are real symmetric positive definite and all calculations are exact. The objective is a centered zero-minimum quadratic and the parameter \(\sigma\) is a positive scalar held fixed during the step. Euclidean gradients, Euclidean gradient norms, and ordinary (not preconditioned) NGN are used. The extremal eigenvalues are required to occur in the spectrum. The theorem permits arbitrary dimension \(d\ge2\), intermediate eigenvalues and multiplicities. For the scalar-spectrum case \(a=b>0\), the sharp factor is simply \((1+a\sigma)^{-2}\), strictly decreases with \(\sigma\), and has no finite minimizing parameter or mode switch.

## Proof

**1. An exact objective identity.** For \(x\ne0\), put \(S_j=x^\top H^jx\), \(j=1,2,3\), \(m=S_2/S_1\), and \(v=S_3/S_1-m^2\). Let \(\lambda_i\) be the eigenvalues and \(p_i=\lambda_i x_i^2/S_1\) the spectral probabilities in an orthonormal eigenbasis. Then \(m=\sum p_i\lambda_i\), \(v=\sum p_i(\lambda_i-m)^2\ge0\). By definition, the NGN scalar stepsize equals \(\alpha=\sigma/(1+\sigma m)\). Expanding \(f(x-\alpha Hx)\) gives exactly
\[
\frac{f(G_\sigma(x))}{f(x)}
=1-\frac{2\sigma m}{1+\sigma m}
+\frac{\sigma^2(S_3/S_1)}{(1+\sigma m)^2}
=\boxed{\frac{1+\sigma^2v}{(1+\sigma m)^2}}.\tag{1}
\]
No probabilistic sampling is used; the spectral probabilities are a deterministic rewriting of the state.

**2. Endpoint reduction is exact.** For every \(\lambda\in[a,b]\), \((\lambda-a)(b-\lambda)\ge0\). Averaging gives
\[
\sum p_i\lambda_i^2\le(a+b)m-ab,\qquad
v\le(b-m)(m-a).\tag{2}
\]
Equality holds exactly when all positive spectral mass is on eigenvalues \(a,b\). For each \(m\in[a,b]\), the required masses \((b-m)/(b-a)\) and \((m-a)/(b-a)\) can be realized by a nonzero vector supported on extremal eigenspaces. Consequently
\[
Q_\sigma(a,b)=\max_{a\le m\le b}
q_\sigma(m),\qquad
q_\sigma(m)=\frac{1+\sigma^2(b-m)(m-a)}{(1+\sigma m)^2}.\tag{3}
\]
This establishes sharpness on any fixed \(H\) having the stated endpoints.

**3. Exact mode switch and envelope.** Direct differentiation yields
\[
q_\sigma'(m)=\frac{\sigma\{\sigma(a+b)+2\sigma^2ab-2-
\sigma[2+\sigma(a+b)]m\}}{(1+\sigma m)^3}.\tag{4}
\]
The numerator is strictly decreasing in \(m\). Its sole real zero is \(m_\sigma\) displayed in the finding, and \(m_\sigma<b\) for every \(\sigma>0\). The condition \(m_\sigma\le a\) is equivalent to \((b-a)\sigma(1+a\sigma)\le2\). Thus (3) is maximized at \(m=a\) on the first branch and at \(m=m_\sigma\) on the second. Substitution gives the displayed two rational formulas. At the transition they agree; equality cases follow from (2).

**4. Unique optimal regularization.** On the first branch the envelope decreases strictly. On the interior branch its derivative has the sign of
\[
\sigma^2(b-a)^2(a+b)-8ab\sigma-4(a+b).
\]
This quadratic has exactly one positive root, \(\sigma_{\rm opt}=2(a+b)/(b-a)^2\). Moreover
\[
(b-a)\sigma_{\rm opt}(1+a\sigma_{\rm opt})-2
=\frac{8a(a^2+b^2)}{(b-a)^3}>0,
\]
so the root lies strictly inside the interior branch. The envelope decreases before and increases after it; substitution gives \(((b-a)/(b+a))^2\). Inserting \(\sigma_{\rm opt}\) into \(m_\sigma\) gives \(2ab/(a+b)\), proving the extremizer assertion.

**5. Exact universal descent boundary.** From (1), the objective is nonincreasing at a state if and only if
\[
\sigma\left(\frac{S_3}{S_1}-2m^2\right)\le2m.
\]
Using (2) and dividing by \(2m>0\) reduces the all-state condition to
\[
\sigma\phi(m)\le1\quad\text{for all }m\in[a,b],
\quad
\phi(m)=\frac{a+b}{2}-\frac{ab}{2m}-m.\tag{5}
\]
AM–GM gives \(\phi(m)\le(a+b)/2-\sqrt{2ab}\). When \(a+b\le2\sqrt{2ab}\), every finite \(\sigma\) gives strict decrease. When \(a+b>2\sqrt{2ab}\), the maximizing \(m=\sqrt{ab/2}\) lies strictly in \((a,b)\), because then \(b/a>3+2\sqrt2>2\); the AM–GM bound is attained by a two-eigenspace state. Hence \(\sigma\le2/(a+b-2\sqrt{2ab})\) is both necessary and sufficient. Rearranging \(a+b\le2\sqrt{2ab}\) gives \(b/a\le3+2\sqrt2\). This establishes all strictness and equality statements.

**6. Exact example.** For \(H=\operatorname{diag}(1,10)\) and squared coordinates \((950,13)\), \(S_1=1080\) and \(S_2=2250\). At \(\sigma=2\), \(\alpha=2S_1/(S_1+2S_2)=12/31\). Direct substitution yields \(f(G_2(x))/f(x)=41/31\).

## Verification

Run `python artifacts/verify.py` using Python 3's standard library. The program performs exact-rational checks of the objective identity, spectral endpoint envelope, optimal parameter and explicit counterexample; it also checks numerical high-dimensional spectra with independently expanded objective ratios. The saved output in `artifacts/verification.txt` records **37,727** assertions passed. Exact symbolic calculations in this proof, not the sampled experiments, establish the universal quantifiers and uniqueness.

## Relationship to prior work

Orvieto and Xiao [1], publicly available July 5, 2024, define the NGN update and prove convergence in broader stochastic/nonnegative smooth settings. Their primary treatment provides the step formula, scalar quadratic examples and convergence analysis; the quadratic-spectrum all-state envelope, sharp fixed-regularization transition and exact minimax calibration stated here were not located in the inspected passages.

The publicly posted theorem *Sharp one-step objective frontier for scaled Polyak steps on SPD quadratics* [2] proves the **different** fixed-multiplier Polyak envelope \(1-\gamma+\gamma^2(a+b)^2/(16ab)\), and already gives the doubled-Polyak condition-number threshold \(3+2\sqrt2\) and the usual optimal gradient-descent factor. Those constants, the endpoint spectral inequality, and the generic possibility of objective spikes are **not claimed as new**. The NGN multiplier is state dependent: \(\alpha=\sigma/(1+\sigma m)\), coupling step length to the spectral mean \(m\). The fixed-\(\gamma\) envelope does not give (3)'s coupled maximum, the exact finite-\(\sigma\) two-branch formula, its unique optimal \(\sigma\), or its sharp safe-parameter threshold.

Huang and Qi [3] analyze a generalized spectral gradient family, including fixed-scaled Polyak steps, and prove norm contraction and asymptotics. Their fixed-parameter quotient is not the NGN harmonic-mean regularization; the exact envelope above is distinct. Classical optimal fixed-step gradient descent and the Kantorovich spectral inequality provide comparisons and tools, not an originality claim.

## Limitations

No conclusion is asserted for nonquadratic losses, positive objective floors, stochastic gradients, indefinite or singular Hessians, constrained problems, preconditioners, multiple-step trajectories, floating-point error, or a globally optimal regularization for practical training. This result is for one-step *objective* ratios, not a proof of instability or nonconvergence of NGN. Spectral endpoint information is assumed for calibration. A specialized equivalent theorem under adaptive gradient/Polyak nomenclature could exist; independent audit remains unperformed.

## References

1. A. Orvieto and L. Xiao, *An Adaptive Stochastic Gradient Method with Non-negative Gauss-Newton Stepsizes*, arXiv:2407.04358v1, first public July 5, 2024. https://arxiv.org/html/2407.04358v1
2. *Sharp one-step objective frontier for scaled Polyak steps on SPD quadratics*, publicly posted September 2026. https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-polyak-objective-monotonicity-frontier--169a05cdc789/RESULT.md
3. Y.-K. Huang and H.-D. Qi, *Analytic analysis of the worst-case complexity of the gradient method with exact line search and the Polyak stepsize*, arXiv:2407.04914v1, first public July 6, 2024. https://arxiv.org/html/2407.04914v1
