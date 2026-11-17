# Sharp global forty-five-degree robustness of inexact high-index saddle flows

## Finding

For a smooth, uniformly strongly concave--convex *separable* energy, the classical high-index saddle flow tolerates arbitrary time- and state-dependent errors in its unstable-subspace projector with a **sharp universal angular boundary of forty-five degrees**, independent of the energy's spectral condition number.

Precisely, the condition \(\|P(t,x)-P_0\|_2\leq\delta<1/\sqrt{2}\) guarantees, from *every* initial state, exponential convergence of
\[
\dot x=-\beta\bigl(I-2P(t,x)\bigr)\nabla E(x)
\]
to the unique index-\(k\) saddle. The exact uniform energy-decay bound is
\[
F(x(t))-F(x_*)\leq \bigl(F(x(0))-F(x_*)\bigr)
\exp\!\bigl[-2\beta\mu(1-2\delta^2)t\bigr],
\]
where \(F\) is the positive-definite energy obtained by reversing the concave part. The coefficient \(1-2\delta^2\) cannot be improved as a bound uniform over this class.

The bound \(\delta<1/\sqrt{2}\) is also best possible for a universal global-attraction assertion: at equality a quadratic two-coordinate example has a continuum of periodic orbits, and above equality that example is exponentially repelling. Both constructions extend to every prescribed index strictly between zero and the ambient dimension by leaving the other directions exactly aligned.

## Assumptions and scope

Fix integers \(n\geq2\) and \(1\leq k<n\). Split the Euclidean state space orthogonally as \(\mathbb R^n=U\oplus V\), with \(\dim U=k\), and denote by \(P_0\) the orthogonal projector onto \(U\). Let \(f:U\to\mathbb R\) and \(g:V\to\mathbb R\) be twice continuously differentiable and \(\mu\)-strongly convex for a common \(\mu>0\), meaning
\[
\nabla^2 f(u)\succeq \mu I_U,\qquad
\nabla^2 g(v)\succeq \mu I_V
\]
at every point. The *saddle energy* and its positive companion are
\[
E(u,v)=-f(u)+g(v),\qquad F(u,v)=f(u)+g(v).
\]
They have the same unique stationary point \(x_*=(u_*,v_*)\); the Hessian of \(E\) has exactly \(k\) negative eigenvalues at every point, and \(x_*\) has Morse index \(k\).

Let \(\beta>0\). Let \(P:[0,\infty)\times\mathbb R^n\to\mathbb R^{n\times n}\) be continuous in time and locally Lipschitz in the state, locally uniformly in time, with \(P(t,x)^\top=P(t,x)\), \(P(t,x)^2=P(t,x)\), \(\operatorname{rank}P(t,x)=k\), and \(\sup_{t,x}\|P(t,x)-P_0\|_2\leq\delta\). Existence and uniqueness are understood in the usual classical ordinary-differential-equation sense. The same energy inequality holds for any absolutely continuous solution for which the projector is merely measurable.

The operator-norm difference of equal-rank orthogonal projectors equals the sine of their largest principal angle, so the strict condition is precisely largest angle less than \(\pi/4\). No upper Hessian bound, spectral gap between different *positive* eigenvalues, or convergence of \(P(t,x)\) to \(P_0\) is required.

## Proof

**Step 1 (exact reflection identity).** Set \(J=I-2P_0\) and \(R=I-2P\) at an arbitrary point and time. Since \(J\nabla F=\nabla E\), the perturbed saddle flow is
\[
\dot x=-\beta RJ\nabla F.
\]
Both projectors are symmetric and idempotent. Expanding the product and averaging with its transpose gives the *exact matrix identity*
\[
\frac{RJ+JR}{2}
=I-2(P-P_0)^2.
\]
Consequently, without any derivative of \(P\),
\[
\begin{aligned}
\frac{d}{dt}F(x(t))
&=-\beta\nabla F(x(t))^\top RJ\nabla F(x(t))\\
&=-\beta\bigl(\|\nabla F(x(t))\|^2
-2\|(P-P_0)\nabla F(x(t))\|^2\bigr)\\
&\leq-\beta(1-2\delta^2)\|\nabla F(x(t))\|^2.
\end{aligned}
\]
The equality in the first two lines is exact for every admissible state-dependent projector.

**Step 2 (global attraction).** By assumption \(F\) is globally \(\mu\)-strongly convex. Its unique minimizer \(x_*\) satisfies the gradient-dominance inequality
\[
\|\nabla F(x)\|^2\geq2\mu\bigl(F(x)-F(x_*)\bigr).
\]
For completeness, strong convexity at \(x\) with comparison point \(x_*\) implies
\[
F(x)-F(x_*)\leq
\nabla F(x)\cdot(x-x_*)-\frac\mu2\|x-x_*\|^2
\leq\frac{\|\nabla F(x)\|^2}{2\mu},
\]
which is the claimed inequality. Combining with Step 1 and integrating proves
\[
F(x(t))-F(x_*)\leq
\bigl(F(x(0))-F(x_*)\bigr)e^{-2\beta\mu(1-2\delta^2)t}.
\]
The strong-convexity lower bound then yields
\[
\|x(t)-x_*\|
\leq\sqrt{\frac{2(F(x(0))-F(x_*))}{\mu}}
\,e^{-\beta\mu(1-2\delta^2)t}.
\]
All sublevel sets of \(F\) are compact, so a locally defined classical solution cannot escape to infinity in finite time. Local Lipschitz regularity of the vector field therefore extends it uniquely for all positive times. The result holds for every initial state and for arbitrarily varying projectors subject only to the stated norm bound.

**Step 3 (optimal energy exponent and failure at the boundary).** Take \(n=2\), \(k=1\), \(E(u,v)=\mu(-u^2+v^2)/2\), and \(P_0\) the projector onto the first axis. For a constant projector \(P\) onto the line at angle \(\phi\in[0,\pi/2]\) to that axis, let \(\delta=\sin\phi\). The linear state equation is exactly
\[
\dot x=-\beta\mu
\begin{pmatrix}
\cos(2\phi)&-\sin(2\phi)\\
\sin(2\phi)&\cos(2\phi)
\end{pmatrix}x.
\]
Thus every nonzero trajectory has radius
\[
\|x(t)\|=e^{-\beta\mu\cos(2\phi)t}\|x(0)\|,
\qquad\cos(2\phi)=1-2\delta^2.
\]
Since \(F(x)=\mu\|x\|^2/2\), equality holds in the energy bound of Step 2 for every \(\delta<1/\sqrt2\); the exponential coefficient is sharp. When \(\delta=1/\sqrt2\), the linear flow is pure rotation with angular velocity \(\beta\mu\), so all nonzero solutions are periodic, precluding global attraction. When \(\delta>1/\sqrt2\), the radius grows exponentially, so the saddle is unstable. For any \(1\leq k<n\), rotate just one pair consisting of a vector in \(U\) and one in \(V\), leaving all other basis vectors fixed. This embeds the same optimality and nonattraction examples in every allowed dimension and index.

## Verification

The accompanying `verification.py` uses exact rational arithmetic to check the projector idempotence and the identity \(\operatorname{sym}(RJ)=I-2(P-P_0)^2\) in planar and higher-index examples. It separately checks the pure-rotation boundary and a strict-expansion example at projector distance \(4/5\), whose radial exponential growth coefficient is \(7\beta\mu/25\). Run `python verification.py` with Python's standard library. These finite checks verify concrete algebraic instances; universal quantifiers, infinite-time conclusions, and the nonlinear result are proved in the preceding argument.

## Relationship to prior work

Shi, Zhang, Zheng and Zhu study continuous perturbed high-index saddle dynamics, including a local exponential-stability guarantee when their projector-error parameter \(\alpha\) obeys \(\mu-2\alpha L>0\) (Theorem 3, arXiv:2611.09049v1, Section 3.2). Here the energy class is more restricted—its negative eigenspace is fixed globally and its positive/negative blocks are completely uncoupled—but within that class the angle threshold is necessary and sufficient for a **uniform all-initial-state, arbitrary-projector-variation** guarantee, and it is independent of the upper curvature bound \(L\). Neither the nonlinear global estimate nor the sharp boundary orbit follows as stated from that local sufficient bound.

Chu and Lin discuss an angle \(\pi/4\) between the *instantaneous gradient* and an approximate ascent direction as a criterion for whether the original saddle energy increases or decreases. This is not a bound on the principal angle between exact and inexact negative eigenspaces, and it does not give the above uniform global stability theorem or the critical periodic counterexample. Huang, Su, Zhang and Zhao's metric-preconditioned HiSD results also provide local convergence estimates, including a condition-number-dependent error bound for discrete inexact eigenframes; they do not imply the present sharp continuous-time result without a different, split-energy argument.

The exact reflection identity is elementary linear algebra. The scientific contribution is the sharp **dynamical** tolerance and condition-number-free global certificate for a natural nonlinear saddle-search class, together with its matching failure at equality, not a claim of novelty for elementary projector algebra or the number \(\pi/4\) in isolation.

## Limitations

The fixed eigenspace and separability hypotheses are essential to the Lyapunov construction \(J\nabla E=\nabla F\); the theorem does **not** assert the same angle bound for Hessians whose positive and negative eigenspaces rotate with the state, or for coupled nonseparable saddle energies. It concerns continuous-time position dynamics, not explicit Euler steps, momentum variants, or the separate evolution/accuracy of eigenvectors. The arbitrary projector may vary with time or state but must satisfy the bound uniformly. The theorem establishes a sharp universal guarantee, not that every particular system is unstable outside the guaranteed range. Historical priority is not independently certified.

## References

1. B. Shi, L. Zhang, X. Zheng and S. Zhu, *Asymptotic stability of high-index saddle dynamics*, arXiv:2611.09049v1 (first public 2026-11-06), https://arxiv.org/html/2611.09049v1, especially (2) and Theorem 3.
2. M. T. Chu and M. M. Lin, *Generalized Gentlest Ascent Dynamics Methods for High-Index Saddle Points*, SIAM Journal on Numerical Analysis (2025), DOI:10.1137/24M1710905, https://epubs.siam.org/eprint/6RBKIUEVWEEPYCJZVVBK/full, especially Sections 2 and 3.
3. B. Huang, H. Su, L. Zhang and J. Zhao, *Preconditioned High-index Saddle Dynamics for Computing Saddle Points*, arXiv:2603.25390v1 (2026), https://arxiv.org/html/2603.25390v1, especially Theorems 5 and 8.
4. Y. Luo, X. Zheng, X. Cheng and L. Zhang, *Convergence Analysis of Discrete High-Index Saddle Dynamics*, arXiv:2204.00171 (2022), https://arxiv.org/abs/2204.00171; abstract and bibliographic record consulted.
