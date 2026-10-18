# FAMO re-normalization has an exact harmonic-mean loss-scale law
## Finding

FAMO derives its balancing direction from gradients of log losses. Those log gradients are exactly invariant under positive rescaling of individual task losses. The practical algorithm then adds a scalar re-normalization so that the returned direction is a convex combination of the raw task gradients. That additional scalar reintroduces a precise loss-unit dependence.

Fix one FAMO state with positive task objectives
\[
\ell_i>0,
\]
task gradients
\[
g_i=\nabla\ell_i,
\]
and simplex coefficients
\[
z_i>0,
\qquad
\sum_i z_i=1.
\]
The source log-gradient direction is
\[
d^{\log}
=
\sum_i z_i\frac{g_i}{\ell_i}.
\]
The practical re-normalization is
\[
c
=
\left(
\sum_i\frac{z_i}{\ell_i}
\right)^{-1},
\]
so the model direction is
\[
d=c\,d^{\log}.
\]

Now independently change the units of the task objectives by fixed constants
\[
s_i>0,
\qquad
\ell_i'=s_i\ell_i,
\qquad
g_i'=s_i g_i.
\]
At the same parameter and logit state,
\[
\frac{g_i'}{\ell_i'}
=
\frac{g_i}{\ell_i},
\]
so
\[
\boxed{
(d^{\log})'=d^{\log}.
}
\]
Likewise, for any two matched parameter states,
\[
\log(s_i\ell_i(\theta))
-
\log(s_i\ell_i(\theta'))
=
\log\ell_i(\theta)
-
\log\ell_i(\theta'),
\]
so the loss-difference signal used by FAMO's logit update is also invariant.

The practical model direction is not invariant. Define the current practical task weights
\[
w_i
=
\frac{z_i/\ell_i}
{\sum_j z_j/\ell_j}.
\]
Then
\[
\boxed{
d'
=
H_w(s)\,d,
\qquad
H_w(s)
=
\left(
\sum_i\frac{w_i}{s_i}
\right)^{-1}.
}
\]
Thus independent task rescaling preserves the update orientation exactly but changes its magnitude by the weighted harmonic mean of the task-unit scale factors.

In particular,
\[
\boxed{
\min_i s_i
\le
H_w(s)
\le
\max_i s_i.
}
\]

For a common rescaling
\[
s_i=s
\]
for every task,
\[
\boxed{
d'=s\,d.
}
\]
Consequently, paper-form FAMO run on the commonly rescaled losses with model learning rate
\[
\alpha'=\frac{\alpha}{s}
\]
has exactly the same full discrete parameter-and-logit trajectory as FAMO on the original losses with learning rate \(\alpha\), provided the initial states and all other hyperparameters agree.

The two-task equal-weight case makes the loss-unit sensitivity transparent. If
\[
w_1=w_2=\frac12
\]
and the scale factors are
\[
(s_1,s_2)=(s,1),
\]
then
\[
\boxed{
H_w(s,1)
=
\frac{2s}{1+s}.
}
\]
Therefore
\[
s\downarrow0
\quad\Longrightarrow\quad
H_w(s,1)\downarrow0.
\]
One task's loss unit can make the practical FAMO step arbitrarily small while the underlying log-gradient direction remains unchanged.

## Assumptions and scope

The theorem concerns the positive objectives that enter the paper-form FAMO equations. If an implementation constructs those objectives by subtracting task lower bounds and adding a fixed numerical floor, the stated rescaling law applies when that positive objective is rescaled as a whole. Rescaling only the raw loss while keeping an additive floor numerically fixed introduces an additional, separate unit dependence.

The result is pointwise for arbitrary independent scale factors. The exact full-trajectory equivalence is claimed only for common scaling, where one fixed reciprocal learning-rate adjustment compensates the re-normalization at every state.

No claim is made that this scalar sensitivity harms empirical performance. The result separates directional task balancing from the effective step length.

## Proof

Under
\[
\ell_i'=s_i\ell_i,
\qquad
g_i'=s_i g_i,
\]
the log-gradient term satisfies
\[
\frac{g_i'}{\ell_i'}
=
\frac{s_i g_i}{s_i\ell_i}
=
\frac{g_i}{\ell_i}.
\]
Hence the unnormalized log-gradient direction is unchanged.

The new re-normalization scalar is
\[
c'
=
\left(
\sum_i
\frac{z_i}{s_i\ell_i}
\right)^{-1}.
\]
Because
\[
w_i
=
c\frac{z_i}{\ell_i},
\]
we have
\[
\frac{c'}{c}
=
\frac{
\sum_i z_i/\ell_i
}{
\sum_i z_i/(s_i\ell_i)
}
=
\left(
\sum_i\frac{w_i}{s_i}
\right)^{-1}
=
H_w(s).
\]
Since the log-gradient direction itself is unchanged,
\[
d'=c'd^{\log}
=
\frac{c'}{c}d
=
H_w(s)d.
\]

The harmonic-mean bounds follow from
\[
\frac1{\max_i s_i}
\le
\sum_i\frac{w_i}{s_i}
\le
\frac1{\min_i s_i},
\]
using
\[
w_i\ge0,
\qquad
\sum_iw_i=1.
\]

For common scale \(s\),
\[
H_w(s,\ldots,s)=s.
\]
The model step on scaled losses with learning rate \(\alpha/s\) is therefore
\[
-\frac{\alpha}{s}d'
=
-\alpha d.
\]
If the two runs start from identical parameter and logit states, their next parameter states agree. The corresponding log-loss differences agree because the common additive constant \(\log s\) cancels. Their logit updates therefore agree as well. Induction proves equality of the complete discrete trajectories.

For two equal practical weights,
\[
H_w(s,1)
=
\left(
\frac1{2s}+\frac12
\right)^{-1}
=
\frac{2s}{1+s}.
\]

## Verification

The accompanying `verify.py` randomly generates positive losses, simplex coefficients, task gradients, and independent scale factors. It reconstructs the paper-form FAMO direction before and after rescaling and checks the exact harmonic-mean multiplier.

It separately checks the common-scale trajectory equivalence for a small deterministic multi-task quadratic system, including the logit update driven by consecutive log-loss differences.

The computations are transcription guards. The theorem itself is the algebraic identity proved above.

## Relationship to prior work

Liu, Feng, Stone, and Liu derive FAMO from gradients of log task losses, formulate balanced improvement through those log gradients, and then introduce a practical scalar re-normalization so that the returned model direction becomes a convex combination of the raw task gradients. They motivate this re-normalization as protection against very large coefficients when a task loss becomes small.

The defining paper also uses a scale-invariant log-loss baseline in its experiments and reports that FAMO remains balanced on a toy problem with improperly scaled task losses. The inspected full text does not state how independent task rescaling transforms the practical re-normalized FAMO step, nor that the entire loss-unit dependence collapses to a weighted harmonic-mean scalar.

The official implementation realizes the same mechanism: it forms positive adjusted task objectives, computes softmax task coefficients, sums coefficient-over-objective terms into a detached normalization factor, and divides the weighted log-objective aggregate by that factor.

Related multi-task work on loss-scale balancing emphasizes logarithmic transformations as a way to remove objective-scale disparities. That general principle explains why FAMO's log-gradient direction is scale invariant, but does not imply the harmonic-mean magnitude law introduced by the practical convex-combination re-normalization.

Focused published-record searches for FAMO loss scaling, re-normalization, scale invariance, and harmonic-mean step dependence did not identify an implication-equivalent result.

## Limitations

The independent-rescaling statement compares the same parameter and logit state. With a fixed common model learning rate, differently scaled runs generally follow different subsequent parameter paths because their step magnitudes differ.

A fixed learning-rate compensation gives exact trajectory equivalence for common scaling only. For independently scaled tasks, the harmonic-mean multiplier generally changes with the current losses and coefficients.

Fixed additive numerical floors can add a second source of scale dependence if they are not transformed together with the positive task objectives.

The theorem concerns update geometry and does not establish a convergence-rate or generalization consequence.

## References

1. Bo Liu, Yihao Feng, Peter Stone, and Qiang Liu, “FAMO: Fast Adaptive Multitask Optimization,” arXiv:2306.03792v1, first submitted 2023-06-06; NeurIPS 2023.
2. Official FAMO implementation, Cranial-XIX/FAMO, `methods/weight_methods.py`, inspected repository revision `26ecb954dceb25d68dbfdf93a209e5c9ad13967a`.
