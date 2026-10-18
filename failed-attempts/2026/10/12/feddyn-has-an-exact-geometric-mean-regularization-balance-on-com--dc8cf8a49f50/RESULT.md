# FedDyn has an exact geometric-mean regularization balance on common-Hessian quadratics
## Finding

Consider exact-minimization FedDyn with full client participation and equal client weights. Let
\[
L_k(x)
=
\frac12(x-b_k)^\top H(x-b_k),
\qquad
k\in\{1,\ldots,m\},
\]
where the clients share a symmetric positive-definite Hessian
\[
\mu I\preceq H\preceq LI,
\qquad
0<\mu\le L.
\]
Let the source-stored client-gradient states be initialized to zero, as in the defining algorithm, and let the FedDyn regularization parameter satisfy
\[
\alpha>0.
\]

The global objective has minimizer
\[
x_\star
=
\frac1m\sum_{k=1}^m b_k.
\]
Write
\[
\gamma^t
=
\frac1m\sum_{k=1}^m x_k^t
\]
for the mean client model after round \(t\). Define the commuting positive operators
\[
R_\alpha
=
\alpha(H+\alpha I)^{-1},
\qquad
S_\alpha
=
H(H+\alpha I)^{-1}.
\]
They satisfy
\[
R_\alpha+S_\alpha=I.
\]

For every integer
\[
t\ge1,
\]
the FedDyn trajectory has the exact decomposition
\[
\boxed{
\gamma^t-x_\star
=
R_\alpha^t(x^0-x_\star),
}
\]
and
\[
\boxed{
x_k^t-\gamma^t
=
S_\alpha^t(b_k-x_\star).
}
\]
The server model itself satisfies
\[
\boxed{
x^t-x_\star
=
\left(I-\frac{H}{\alpha}\right)
R_\alpha^t(x^0-x_\star).
}
\]

Thus FedDyn separates, on this family, into two complementary spectral channels. The global-average residual contracts with sharp operator factor
\[
r(\alpha)
=
\left\|R_\alpha\right\|_2
=
\frac{\alpha}{\alpha+\mu},
\]
whereas client disagreement contracts with sharp operator factor
\[
s(\alpha)
=
\left\|S_\alpha\right\|_2
=
\frac{L}{L+\alpha}.
\]

The first factor increases with \(\alpha\), while the second decreases. Therefore the joint worst-channel factor
\[
\rho(\alpha)
=
\max\left\{
\frac{\alpha}{\alpha+\mu},
\frac{L}{L+\alpha}
\right\}
\]
has the unique minimizer
\[
\boxed{
\alpha_\star=\sqrt{\mu L}.
}
\]
Writing
\[
\kappa=\frac{L}{\mu},
\]
the exact minimax factor is
\[
\boxed{
\rho(\alpha_\star)
=
\frac{\sqrt{\kappa}}{1+\sqrt{\kappa}}.
}
\]

There is an additional exact cancellation in the isotropic case
\[
H=aI.
\]
At the balanced choice
\[
\alpha=a,
\]
the server satisfies
\[
\boxed{
x^t=x_\star
\qquad
\text{for every }t\ge1,
}
\]
while
\[
\gamma^t-x_\star
=
2^{-t}(x^0-x_\star),
\]
and
\[
x_k^t-\gamma^t
=
2^{-t}(b_k-x_\star).
\]
So the server reaches the exact global minimizer after one communication round even though the client models continue to approach consensus geometrically.

## Assumptions and scope

The result uses the defining exact-minimization FedDyn update, full participation, equal client weights, and the source initialization in which the stored client-gradient states begin at zero.

All client objectives are deterministic strongly convex quadratics with a common Hessian. Their minimizers \(b_k\) may be arbitrary, so statistical heterogeneity remains present through shifted local optima.

The common-Hessian assumption is essential to the closed decomposition. The theorem does not claim the same formulas for client-dependent Hessians, stochastic local solvers, partial participation, unequal aggregation weights, or inexact local minimization.

The factor
\[
\rho(\alpha)
\]
is a deliberately joint metric: it balances the mean-client residual against client disagreement. It is not asserted to be the only meaningful tuning objective for FedDyn.

## Proof

The defining FedDyn local subproblem in round \(t\) is
\[
x_k^t
=
\mathop{\arg\min}_x
\left[
L_k(x)
-
\langle g_k^{t-1},x\rangle
+
\frac{\alpha}{2}\|x-x^{t-1}\|^2
\right],
\]
where the stored client-gradient state begins at
\[
g_k^0=0
\]
and is updated so that, after the first exact local minimization,
\[
g_k^t=\nabla L_k(x_k^t).
\]

At the first round, the optimality condition gives
\[
(H+\alpha I)x_k^1
=
Hb_k+\alpha x^0.
\]
Hence
\[
x_k^1
=
R_\alpha x^0+S_\alpha b_k.
\]
Averaging over clients gives
\[
\gamma^1-x_\star
=
R_\alpha(x^0-x_\star),
\]
and subtraction of the mean gives
\[
x_k^1-\gamma^1
=
S_\alpha(b_k-x_\star).
\]

For every later round, the stored gradient is the true gradient at the preceding client model:
\[
g_k^{t-1}
=
H(x_k^{t-1}-b_k).
\]
The local optimality condition therefore simplifies to
\[
(H+\alpha I)x_k^t
=
Hx_k^{t-1}+\alpha x^{t-1},
\]
or
\[
x_k^t
=
S_\alpha x_k^{t-1}
+
R_\alpha x^{t-1}.
\]

Under full participation the defining server identity is
\[
x^t
=
\gamma^t-\frac{1}{\alpha}h^t,
\]
with
\[
h^t
=
\frac1m\sum_{k=1}^m \nabla L_k(x_k^t).
\]
For the common Hessian family,
\[
h^t
=
H(\gamma^t-x_\star).
\]
Thus
\[
x^t-x_\star
=
\left(I-\frac{H}{\alpha}\right)(\gamma^t-x_\star).
\]

Averaging the later-round client recurrence yields
\[
\gamma^t-x_\star
=
S_\alpha(\gamma^{t-1}-x_\star)
+
R_\alpha(x^{t-1}-x_\star).
\]
Substituting the server identity and using
\[
S_\alpha
+
R_\alpha\left(I-\frac{H}{\alpha}\right)
=
R_\alpha
\]
gives
\[
\gamma^t-x_\star
=
R_\alpha(\gamma^{t-1}-x_\star).
\]
Together with the first-round formula, this proves
\[
\gamma^t-x_\star
=
R_\alpha^t(x^0-x_\star).
\]

Subtracting the mean recurrence from the client recurrence gives
\[
x_k^t-\gamma^t
=
S_\alpha(x_k^{t-1}-\gamma^{t-1}),
\]
and the first-round identity gives
\[
x_k^t-\gamma^t
=
S_\alpha^t(b_k-x_\star).
\]

Because \(H\) is symmetric positive definite, \(R_\alpha\) and \(S_\alpha\) diagonalize in the eigenbasis of \(H\). Their eigenvalues at curvature \(\lambda\in[\mu,L]\) are
\[
\frac{\alpha}{\alpha+\lambda}
\]
and
\[
\frac{\lambda}{\alpha+\lambda},
\]
respectively. The first decreases in \(\lambda\) and the second increases, proving the sharp endpoint factors
\[
r(\alpha)=\frac{\alpha}{\alpha+\mu},
\qquad
s(\alpha)=\frac{L}{L+\alpha}.
\]

The unique minimizer of their maximum occurs where they are equal:
\[
\frac{\alpha}{\alpha+\mu}
=
\frac{L}{L+\alpha}.
\]
This reduces to
\[
\alpha^2=\mu L,
\]
which proves the geometric-mean tuning and its factor.

If
\[
H=aI
\quad\text{and}\quad
\alpha=a,
\]
then
\[
R_\alpha=S_\alpha=\frac12 I
\]
and
\[
I-\frac{H}{\alpha}=0.
\]
The one-round server cancellation and the exact halving laws follow immediately.

## Verification

The accompanying `verify.py` reconstructs the defining exact FedDyn local subproblem and server state directly for randomly rotated positive-definite common Hessians.

It compares direct client and server iterates with the closed formulas for the mean residual, client disagreement, and server state over multiple rounds. It also checks the endpoint operator factors, the unique geometric-mean minimizer, and the isotropic one-round server cancellation.

The numerical checks are transcription guards. The identities and minimax tuning are proved analytically above.

## Relationship to prior work

Acar and coauthors introduce FedDyn by dynamically adding linear and quadratic terms to each client objective. Their exact-minimization algorithm, stored-gradient recursion, and server correction are precisely the ingredients used here. Their convergence theory gives general convex, strongly convex, and nonconvex rates, while their sensitivity discussion states that \(\alpha\) balances problem-dependent constants and is the only FedDyn hyperparameter when clients have an optimization solver.

The inspected defining paper does not diagonalize the exact common-Hessian quadratic dynamics into mean-residual and disagreement channels. It does not state the factors
\[
\frac{\alpha}{\alpha+\mu}
\quad\text{and}\quad
\frac{L}{L+\alpha},
\]
the geometric-mean balance
\[
\alpha=\sqrt{\mu L},
\]
or the isotropic one-round server cancellation.

Focused searches for FedDyn with common or shared Hessians, exact quadratic spectral dynamics, geometric-mean regularization, one-round exact server minimization, and condition-number tuning did not identify an implication-equivalent published result. Broader spectral and federated-optimization records returned other recurrences or empirical comparisons rather than this exact FedDyn decomposition.

## Limitations

The theorem exploits common curvature across clients. Heterogeneity enters through different local minimizers, not different Hessians.

The geometric-mean parameter minimizes the maximum of two specific exact channels. Other objectives, such as server-only error at a prescribed finite horizon, can favor a different \(\alpha\), especially because the server has the extra cancellation factor
\[
I-\frac{H}{\alpha}.
\]

The isotropic one-round cancellation is exact for the server state, not for all client states. The client models still require further rounds to reach consensus.

The result does not compare practical wall-clock cost or stochastic generalization performance.

## References

1. Durmus Alp Emre Acar, Yue Zhao, Ramon Matas Navarro, Matthew Mattina, Paul N. Whatmough, and Venkatesh Saligrama, “Federated Learning Based on Dynamic Regularization,” ICLR 2021, OpenReview `B7v4QMR6Z9w`.
2. Durmus Alp Emre Acar, Yue Zhao, Ramon Matas Navarro, Matthew Mattina, Paul N. Whatmough, and Venkatesh Saligrama, “Federated Learning Based on Dynamic Regularization,” arXiv:2111.04263v2, 2021.
