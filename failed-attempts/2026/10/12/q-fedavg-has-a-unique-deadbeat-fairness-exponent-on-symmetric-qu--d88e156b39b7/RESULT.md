# q-FedAvg has a unique deadbeat fairness exponent on symmetric quadratics
## Finding

The q-Fair Federated Learning objective introduces a positive parameter \(q\) that continuously changes how strongly high-loss clients are emphasized. The associated q-FedAvg method also changes its server denominator with \(q\). Even in the simplest symmetric quadratic problem, this parameter has a sharp and nonmonotone effect on communication-round dynamics.

Consider two equally weighted scalar clients
\[
F_1(x)=\frac a2(x-b)^2,
\qquad
F_2(x)=\frac a2(x+b)^2,
\qquad
a,b>0.
\]
The q-FFL objective is
\[
\Phi_q(x)
=
\frac12\sum_{i=1}^2
\frac{F_i(x)^{q+1}}{q+1},
\qquad
q>0.
\]
By symmetry its unique minimizer is
\[
x^\star=0.
\]

Run deterministic, full-participation q-FedAvg. Let each client take exactly one local gradient step with
\[
\eta=\frac1a,
\]
and use the source smoothness constant
\[
L=a.
\]
Each client then reaches its own local minimizer exactly after that one step.

At every broadcast point
\[
x\ne\pm b,
\]
the q-FedAvg communication round is exactly one Newton step on
\[
\Phi_q.
\]
Its exact map is
\[
\boxed{
T_q(x)
=
x-
\frac{
(x-b)|x-b|^{2q}
+
(x+b)|x+b|^{2q}
}{
(2q+1)
\left(
|x-b|^{2q}
+
|x+b|^{2q}
\right)
}.
}
\]

Inside the open interval between the two client minimizers,
\[
|x|<b,
\]
the fairness exponent
\[
\boxed{q=\frac12}
\]
is uniquely deadbeat:
\[
\boxed{
T_{1/2}(x)=0
\qquad
\text{for every }|x|<b.
}
\]
Thus every point in that entire interval reaches the exact q-FFL minimizer in one communication round.

For every other positive exponent,
\[
q\ne\frac12,
\]
the local map has the expansion
\[
\boxed{
T_q(x)
=
\frac{2q(2q-1)}{3b^2}x^3
+
O(x^5)
\qquad
(x\to0).
}
\]
Hence the local convergence order is exactly three. The leading coefficient is negative for
\[
0<q<\frac12,
\]
so sufficiently small errors reverse sign, and it is positive for
\[
q>\frac12,
\]
so sufficiently small errors preserve sign.

The deadbeat exponent is therefore isolated: among all positive \(q\), only
\[
q=\frac12
\]
annihilates a whole neighborhood in one q-FedAvg round.

For the practically common value
\[
q=1,
\]
the exact map simplifies globally to
\[
\boxed{
T_1(x)
=
\frac{2x^3}{3(x^2+b^2)}.
}
\]
It obeys
\[
0<|T_1(x)|<\frac23|x|
\qquad
(x\ne0),
\]
so it converges globally and cubically to zero but never reaches zero in finitely many rounds from a nonzero initialization.

For comparison, the source method reduces to ordinary FedAvg at
\[
q=0.
\]
Under the same exact local solves, FedAvg averages the two returned models \(b\) and \(-b\), and therefore reaches zero in one round from every initialization.

## Assumptions and scope

The result uses source-form q-FedAvg with two equally weighted clients, deterministic full participation, and exactly one local gradient step.

The local learning rate is
\[
\eta=\frac1a,
\]
which is the reciprocal of the exact scalar smoothness constant and sends each quadratic client exactly to its local minimizer.

The exact Newton equivalence is stated at points
\[
x\ne\pm b,
\]
so every client loss is positive. This avoids the raw source expression
\[
F_i^{q-1}
\]
at a zero client loss when
\[
0<q<1.
\]
The deadbeat interval itself is open and therefore has no such singular point.

No claim is made for stochastic local gradients, client subsampling, unequal client weights, multiple local steps, unequal curvatures, or vector-valued noncommuting Hessians.

The finding is about optimization dynamics, not about whether
\[
q=\frac12
\]
is the statistically preferable fairness choice on a given application.

## Proof

With one local gradient step,
\[
\bar x_i
=
x-\eta\nabla F_i(x).
\]
Because
\[
\eta=\frac1a
\]
and
\[
\nabla F_1(x)=a(x-b),
\qquad
\nabla F_2(x)=a(x+b),
\]
the local models are exactly
\[
\bar x_1=b,
\qquad
\bar x_2=-b.
\]

The source q-FedAvg scaled local difference is
\[
\Delta x_i
=
L(x-\bar x_i).
\]
Since
\[
L=a,
\]
we have
\[
\Delta x_i=\nabla F_i(x).
\]
Therefore q-FedAvg's transmitted numerator contribution is
\[
\Delta_i
=
F_i(x)^q\nabla F_i(x).
\]

Its denominator contribution is
\[
h_i
=
qF_i(x)^{q-1}\|\nabla F_i(x)\|^2
+
aF_i(x)^q.
\]
For a scalar quadratic,
\[
F_i''(x)=a,
\]
so
\[
h_i
=
\frac{d^2}{dx^2}
\left(
\frac{F_i(x)^{q+1}}{q+1}
\right),
\]
while
\[
\Delta_i
=
\frac{d}{dx}
\left(
\frac{F_i(x)^{q+1}}{q+1}
\right).
\]
Summing the two client contributions shows that the server ratio is exactly
\[
\frac{\Phi_q'(x)}{\Phi_q''(x)}.
\]
Hence q-FedAvg is an exact Newton step on this family.

Writing
\[
d_1=x-b,
\qquad
d_2=x+b,
\]
the common positive constants in numerator and denominator cancel, yielding
\[
T_q(x)
=
x-
\frac{
d_1|d_1|^{2q}
+
d_2|d_2|^{2q}
}{
(2q+1)
\left(
|d_1|^{2q}
+
|d_2|^{2q}
\right)
}.
\]

Now assume
\[
|x|<b
\]
and put
\[
u=\frac xb.
\]
Then
\[
|u-1|=1-u,
\qquad
|u+1|=1+u.
\]
At
\[
q=\frac12,
\]
the numerator of the Newton ratio becomes
\[
(u-1)(1-u)+(u+1)(1+u)
=
4u,
\]
and its denominator becomes
\[
2\bigl((1-u)+(1+u)\bigr)
=
4.
\]
The ratio is exactly \(u\), so
\[
T_{1/2}(x)=0.
\]

For general positive \(q\), the functions
\[
(1-u)^{2q}
\quad\text{and}\quad
(1+u)^{2q}
\]
are analytic for
\[
|u|<1.
\]
Expanding the exact map at
\[
u=0
\]
gives
\[
\frac{T_q(bu)}b
=
\frac{2q(2q-1)}3u^3
-
\frac{2q(2q-1)(8q^2-3)}{15}u^5
+
O(u^7).
\]
Returning to \(x\) gives the stated cubic coefficient.

If the map vanished on an open neighborhood of zero for some positive \(q\), every Taylor coefficient would vanish. In particular the cubic coefficient would satisfy
\[
2q(2q-1)=0.
\]
Under
\[
q>0,
\]
this forces
\[
q=\frac12.
\]
Thus the positive deadbeat exponent is unique.

Finally, setting
\[
q=1
\]
in the exact map gives
\[
T_1(x)
=
x-
\frac{(x-b)^3+(x+b)^3}
{3\bigl((x-b)^2+(x+b)^2\bigr)}
=
\frac{2x^3}{3(x^2+b^2)}.
\]
For every nonzero \(x\), the multiplicative factor
\[
\frac{2x^2}{3(x^2+b^2)}
\]
lies strictly between zero and
\[
\frac23.
\]
This proves global convergence and the absence of finite termination away from zero.

## Verification

The accompanying `verify.py` reconstructs Algorithm 2's scaled client differences, numerator terms, denominator terms, and server update directly.

It checks random positive curvatures and shifts, verifies the closed q-FedAvg map, confirms one-round annihilation for
\[
q=\frac12
\]
throughout the open client-minimizer interval, checks the general cubic coefficient numerically for several positive \(q\), and verifies the exact
\[
q=1
\]
global map.

The computations are transcription guards. The exact Newton identity, deadbeat interval, uniqueness, and convergence-order statements are proved algebraically above.

## Relationship to prior work

Li, Sanjabi, Beirami, and Smith introduced q-FFL and q-FedAvg. Their method uses a \(q\)-dependent local smoothness bound to construct a dynamic server denominator, and q-FedAvg replaces each client gradient in the q-FedSGD construction by a scaled local model difference. The source describes this local-update replacement as a heuristic and evaluates communication efficiency empirically.

The defining paper derives the q-FFL Hessian expression that underlies the server denominator, but it does not state that this bound becomes exact on equal-curvature scalar quadratics, that one local exact solve makes q-FedAvg identical to Newton's method, or that
\[
q=\frac12
\]
is a unique deadbeat exponent on the interval between symmetric client minimizers. Its discussion of \(q\) emphasizes fairness tuning and empirical convergence rather than an exact dynamical phase transition.

A 2024 analysis of a FedAvg-like q-FFL method studies local stochastic gradients of the transformed q-FFL loss with a fixed learning rate and derives standard convergence bounds. That update is different from the original q-FedAvg dynamic-denominator rule, so those results do not imply the exact Newton map or the deadbeat exponent here.

Focused searches for q-FedAvg quadratic dynamics, Newton equivalence, finite termination, and the exponent
\[
q=\frac12
\]
did not identify an implication-equivalent published statement.

## Limitations

The exact phenomenon uses a symmetric two-client scalar family and a one-step exact local solve.

The unique-deadbeat classification is among positive q-FFL exponents and concerns an open neighborhood of the minimizer. The separate
\[
q=0
\]
FedAvg baseline is also one-round exact here.

At client minimizers and
\[
0<q<1,
\]
the unsimplified source denominator contains a negative power of a zero loss. No statement here assigns a value to that raw expression; the deadbeat theorem avoids those endpoints.

The result does not show that
\[
q=\frac12
\]
optimizes statistical fairness, test accuracy, or communication complexity outside this exact quadratic family.

## References

1. Tian Li, Maziar Sanjabi, Ahmad Beirami, and Virginia Smith, “Fair Resource Allocation in Federated Learning,” arXiv:1905.10497v1, first submitted 2019-05-25; ICLR 2020.
2. Amirreza Talebi, “Fair Federated Learning,” Preprints 2024, DOI:10.20944/preprints202409.0544.v1, posted 2024-09-06.
