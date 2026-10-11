# Exact Nyquist-gain stability law for Grokfast-EMA gradient descent
## Finding

Grokfast-EMA amplifies a low-pass-filtered copy of the gradient before an underlying optimizer acts. For plain gradient descent on a positive-definite quadratic, the resulting closed-loop stability boundary has an exact frequency-domain interpretation.

Let
\[
f(x)=\frac12x^\top Hx,
\qquad
H=H^\top\succ0,
\]
and write
\[
L=\lambda_{\max}(H).
\]
Take Grokfast-EMA parameters
\[
0\le\alpha<1,
\qquad
\lambda\ge0,
\]
and a gradient-descent learning rate
\[
\eta>0.
\]
The filtered gradient recurrence is
\[
\mu_t
=
\alpha\mu_{t-1}
+
(1-\alpha)Hx_t,
\]
followed by
\[
x_{t+1}
=
x_t-
\eta\left(Hx_t+\lambda\mu_t\right).
\]

The complete linear state is Schur stable for every initial condition if and only if
\[
0<\eta L
<
q_\star,
\]
where
\[
q_\star
=
\frac{2(1+\alpha)}{(1+\alpha)+\lambda(1-\alpha)}
=
\frac{2}{1+\lambda(1-\alpha)/(1+\alpha)}.
\]

The boundary is sharp. At
\[
\eta L=q_\star,
\]
the top-curvature mode has an eigenvalue exactly equal to
\[
-1,
\]
and for
\[
\eta L>q_\star
\]
that mode has an eigenvalue of modulus larger than one.

The same formula has a direct signal-processing meaning. Grokfast-EMA has total gradient transfer factor
\[
A(z)
=
1+
\frac{\lambda(1-\alpha)}{1-\alpha z^{-1}}.
\]
Its DC gain is
\[
A(1)=1+\lambda,
\]
whereas its Nyquist gain is
\[
A(-1)
=
1+
\lambda\frac{1-\alpha}{1+\alpha}.
\]
The exact quadratic stability ceiling is therefore
\[
q_\star
=
\frac{2}{A(-1)}.
\]

Thus the learning-rate margin is controlled by how much the filter amplifies the alternating, highest-frequency mode that appears at the gradient-descent stability boundary, not by the much larger low-frequency amplification that Grokfast is designed to create.

For the implementation defaults
\[
\alpha=0.98,
\qquad
\lambda=2,
\]
the DC gain is
\[
A(1)=3,
\]
while the Nyquist gain is only
\[
A(-1)
=
1+
2\frac{0.02}{1.98}
=
\frac{101}{99}.
\]
Hence
\[
q_\star
=
\frac{198}{101}
\approx
1.9603960396.
\]
So a threefold amplification of perfectly slow gradients reduces the scalar quadratic learning-rate ceiling by only about
\[
1.98\%.
\]

The paper recommends roughly
\[
\lambda\in[0.1,5],
\qquad
\alpha\in[0.8,0.99].
\]
At the most aggressive low-momentum corner
\[
\alpha=0.8,
\qquad
\lambda=5,
\]
the exact ceiling becomes
\[
q_\star
=
\frac97
\approx
1.2857142857.
\]
This is a substantially smaller margin than ordinary gradient descent. The formula therefore isolates a concrete tradeoff: increasing \(\alpha\) makes the amplifier more selective for slow components and simultaneously protects the high-frequency stability boundary.

## Assumptions and scope

The result analyzes Grokfast-EMA placed in front of plain gradient descent, exactly following the paper's gradient-filtering architecture. It uses a deterministic SPD quadratic and a constant learning rate.

The EMA may have any finite initial state. Initialization changes only the transient coefficients, not the Schur-stability criterion.

There is no weight decay, stochastic gradient noise, or additional base-optimizer momentum in the theorem. Adam, AdamW, and momentum SGD introduce extra state and have different closed-loop characteristic polynomials.

The result concerns asymptotic linear stability, not monotonic decrease of the objective at every individual step.

## Proof

Diagonalize the Hessian as
\[
H=U\operatorname{diag}(h_1,\ldots,h_d)U^\top,
\qquad
0<h_i\le L.
\]
Because the EMA coefficient and amplification factor are scalar, the orthogonal change of coordinates simultaneously decouples the parameter and EMA recurrences into independent Hessian modes.

Fix one mode with curvature
\[
h>0
\]
and define
\[
q=\eta h.
\]
Scale the previous EMA coordinate by \(h\), writing
\[
w_{t-1}=\frac{\mu_{t-1}}{h}.
\]
Then
\[
w_t
=
\alpha w_{t-1}
+
(1-\alpha)x_t,
\]
and
\[
x_{t+1}
=
\left[1-q\left(1+\lambda(1-\alpha)\right)\right]x_t
-
q\lambda\alpha w_{t-1}.
\]
Therefore the modal state matrix is
\[
M(q)
=
\begin{bmatrix}
1-q\left(1+\lambda(1-\alpha)\right)&-q\lambda\alpha\\
1-\alpha&\alpha
\end{bmatrix}.
\]
Its trace and determinant are
\[
T
=
1+\alpha
-q\left(1+\lambda(1-\alpha)\right),
\]
and
\[
D
=
\alpha(1-q).
\]
The characteristic polynomial is
\[
r^2-Tr+D.
\]

For a real monic quadratic, both roots are strictly inside the unit disk exactly when
\[
1-T+D>0,
\]
\[
1+T+D>0,
\]
and
\[
1-D>0.
\]
Here these three expressions simplify to
\[
1-T+D
=
q(1-\alpha)(1+\lambda),
\]
\[
1+T+D
=
2(1+\alpha)
-q\left[(1+\alpha)+\lambda(1-\alpha)\right],
\]
and
\[
1-D
=
1-\alpha+\alpha q.
\]
For
\[
q>0,
\qquad
0\le\alpha<1,
\qquad
\lambda\ge0,
\]
the first and third inequalities are automatic. The second is therefore the unique stability restriction, giving
\[
q<q_\star.
\]

Because the restriction is monotone in \(h\), all Hessian modes are stable exactly when the top mode satisfies
\[
\eta L<q_\star.
\]
At equality,
\[
1+T+D=0,
\]
which is precisely the condition that
\[
r=-1
\]
is a root. Above equality, the corresponding real root crosses outside the unit disk.

Finally, the EMA impulse response used by Grokfast is
\[
\lambda(1-\alpha)\alpha^t,
\]
so the total input-gradient transfer factor is
\[
A(z)
=
1+
\frac{\lambda(1-\alpha)}{1-\alpha z^{-1}}.
\]
Evaluating at
\[
z=-1
\]
gives
\[
A(-1)
=
1+
\lambda\frac{1-\alpha}{1+\alpha},
\]
and substitution proves
\[
q_\star=2/A(-1).
\]

## Verification

The accompanying `verify.py` reconstructs the modal state matrix, checks the exact trace and determinant identities, tests the Schur inequalities on randomized parameters on both sides of the boundary, verifies the \(-1\) root at equality, and reproduces the two numerical parameter examples.

Those computations are transcription guards. The stability theorem follows analytically from the modal decomposition and the exact quadratic Schur criterion.

## Relationship to prior work

Lee, Kang, Kim, and Lee introduced Grokfast by viewing gradient trajectories as time signals and amplifying low-frequency components. Their EMA variant uses
\[
\mu_t
=
\alpha\mu_{t-1}+(1-\alpha)g_t
\]
and replaces the current gradient by
\[
g_t+\lambda\mu_t.
\]
The paper explicitly analyzes the filter in the frequency domain, gives its impulse response, distinguishes it from ordinary optimizer momentum, and proves that filtering gradients is equivalent to filtering updates for linear optimizers.

The paper's experiments and ablations motivate \(\lambda\) and \(\alpha\) through generalization speed and cutoff frequency. Its inspected full text does not state a quadratic Schur-stability region, a learning-rate ceiling, or the Nyquist-gain identity derived here.

Later work comparing grokking accelerators has reported empirical stability differences between Grokfast variants, which makes an exact baseline stability calculation useful, but those empirical observations do not imply the closed-form boundary above.

The result is also not a generic momentum stability formula in disguise: the relevant source architecture adds a low-pass residual to the current gradient before the base optimizer. The resulting boundary is naturally expressed by the source filter's Nyquist gain.

## Limitations

The exact formula applies to Grokfast-EMA with plain gradient descent on SPD quadratics.

Additional optimizer state, stochasticity, nonlinear curvature, weight decay, or time-varying learning rates change the closed-loop system.

Schur stability does not guarantee per-step objective monotonicity or say whether grokking occurs.

The numerical examples use hyperparameters documented in the source paper; they are illustrations of the theorem rather than universal tuning recommendations.

## References

1. Jaerin Lee, Bong Gyun Kang, Kihoon Kim, and Kyoung Mu Lee, “Grokfast: Accelerated Grokking by Amplifying Slow Gradients,” arXiv:2405.20233v1, 2024.
2. Xinyu Zhou, Simin Fan, Martin Jaggi, and Jie Fu, “NeuralGrok: Accelerate Grokking by Neural Gradient Transformation,” arXiv:2504.17243, 2025.
