# Exact first-order normal-curvature production in Kunikawa's compact torus

## Finding

Let
\[
F(s,\theta)
=
\bigl((2+\cos\theta)\gamma(s),\sin\theta\bigr)
\subset\mathbb R^4
\]
be the compact torus in Kunikawa's counterexample, where
\[
\gamma:\mathbb S_L^1\to S^2
\]
is smooth, unit speed, embedded, closed, and has nonconstant geodesic curvature \(\kappa\).

Use the oriented orthonormal tangent and normal frames
\[
(e_1,e_2;\nu,\xi)
\]
from the construction and extend them smoothly in spacetime. Define the scalar normal curvature
\[
K^\perp(s,\theta,t)
=
\left\langle
R^\perp(e_1,e_2)\nu,\xi
\right\rangle .
\]
Because the initial normal bundle is flat,
\[
K^\perp(s,\theta,0)=0.
\]
Its exact initial production rate is
\[
\boxed{
\partial_tK^\perp(s,\theta,0)
=
-\frac{4\kappa'(s)\sin\theta}{(2+\cos\theta)^4}.
}
\]

Hence, whenever
\[
\kappa'(s)\ne0,
\]
normal curvature is generated to first order at every point of the corresponding profile circle except
\[
\theta=0,\pi.
\]

The absolute production rate on that profile circle has exactly two maximizers. They are characterized by
\[
\boxed{
\cos\theta
=
\frac{1-\sqrt{13}}{3},
}
\]
and the maximal rate is
\[
\boxed{
\max_\theta
\left|
\partial_tK^\perp(s,\theta,0)
\right|
=
\frac{108\sqrt{2\sqrt{13}-5}}
{(7-\sqrt{13})^4}
|\kappa'(s)|.
}
\]
Numerically, the universal coefficient is
\[
1.2096262067386666\ldots.
\]

There is also an exact global production law. Put
\[
\mathcal E(t)
=
\int_{F_t}(K^\perp)^2\,d\mu_t.
\]
Then
\[
\boxed{
\mathcal E(t)
=
\frac{118\sqrt3\pi}{243}
\left(
\int_0^L(\kappa'(s))^2\,ds
\right)t^2
+
o(t^2).
}
\]
Equivalently,
\[
\boxed{
\mathcal E''(0)
=
\frac{236\sqrt3\pi}{243}
\int_0^L(\kappa'(s))^2\,ds.
}
\]
Since \(\kappa\) is nonconstant, the last quantity is strictly positive.

## Assumptions and scope

The scalar \(K^\perp\) is defined after choosing orientations of the tangent and normal two-planes. Reversing one orientation reverses its sign but leaves
\[
(K^\perp)^2
\]
and the absolute production rate unchanged.

The profile is exactly the one fixed in the compact counterexample:
\[
\rho(\theta)=2+\cos\theta,
\qquad
z(\theta)=\sin\theta.
\]
The initial induced metric is
\[
g=\rho^2\,ds^2+d\theta^2,
\]
so
\[
d\mu_0=\rho\,ds\,d\theta.
\]

The result is a first-order statement for the scalar curvature and a second-order statement for its squared \(L^2\) energy at time zero. It does not determine the later nonlinear evolution of the location of the maximal-curvature points.

## Proof

Kunikawa defines the commutator source term
\[
\mathcal C(\nu,\xi)
=
\sum_k
\bigl[
(\nabla_{e_k}S)^\nu,
(\nabla_{e_k}S)^\xi
\bigr].
\]
For an initially flat normal bundle, the source's evolution identity gives
\[
\left\langle
(\nabla_tR^\perp)(e_1,e_2)\nu,\xi
\right\rangle
=
-2
\left\langle
\mathcal C(\nu,\xi)e_1,e_2
\right\rangle .
\]

For the compact torus with
\[
\rho=2+\cos\theta,
\qquad
z=\sin\theta,
\]
the source computes
\[
\mathcal C(\nu,\xi)
=
\frac{2\kappa'(s)\sin\theta}{\rho^4}
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]
Therefore
\[
\left\langle
\mathcal C(\nu,\xi)e_1,e_2
\right\rangle
=
\frac{2\kappa'(s)\sin\theta}{\rho^4}.
\]
Because \(R^\perp=0\) at time zero, derivatives of the chosen frame extensions make no contribution to the derivative of the scalar component. Thus
\[
\partial_tK^\perp(s,\theta,0)
=
-\frac{4\kappa'(s)\sin\theta}{(2+\cos\theta)^4}.
\]

For fixed \(s\) with \(\kappa'(s)\ne0\), the zero set in the profile variable is therefore exactly
\[
\theta\in\{0,\pi\}.
\]

To maximize the absolute rate, it suffices on
\[
0<\theta<\pi
\]
to maximize
\[
h(\theta)
=
\frac{\sin\theta}{(2+\cos\theta)^4}.
\]
Differentiation gives
\[
h'(\theta)
=
\frac{4+2\cos\theta-3\cos^2\theta}
{(2+\cos\theta)^5}.
\]
The critical equation is
\[
3x^2-2x-4=0,
\qquad
x=\cos\theta.
\]
Only one root lies in \([-1,1]\):
\[
x_*=\frac{1-\sqrt{13}}3.
\]
The derivative changes from positive to negative there, so this is the unique maximizer on \((0,\pi)\). By reflection \(\theta\mapsto2\pi-\theta\), there are exactly two maximizers on the full profile circle.

At \(x=x_*\),
\[
1-x_*^2
=
\frac{2\sqrt{13}-5}{9},
\qquad
2+x_*
=
\frac{7-\sqrt{13}}3.
\]
Hence
\[
\max_\theta h(\theta)
=
\frac{27\sqrt{2\sqrt{13}-5}}
{(7-\sqrt{13})^4},
\]
which gives the displayed maximal production rate after multiplication by \(4|\kappa'(s)|\).

For the global law, smoothness of mean curvature flow on the compact initial torus gives
\[
K^\perp(s,\theta,t)
=
-\frac{4\kappa'(s)\sin\theta}{(2+\cos\theta)^4}t
+
o(t)
\]
uniformly on the torus. Since the initial scalar is zero, the first variation of the area form does not affect the coefficient of \(t^2\) in the squared-curvature energy. Therefore
\[
\mathcal E(t)
=
16t^2
\left(
\int_0^L(\kappa')^2\,ds
\right)
\left(
\int_0^{2\pi}
\frac{\sin^2\theta}{(2+\cos\theta)^7}
\,d\theta
\right)
+
o(t^2).
\]

It remains to evaluate one elementary integral. If
\[
J_n(a)
=
\int_0^{2\pi}
(a+\cos\theta)^{-n}\,d\theta,
\]
then
\[
J_1(a)
=
\frac{2\pi}{\sqrt{a^2-1}},
\qquad
J_{n+1}(a)
=
-\frac1n\frac{dJ_n}{da}.
\]
Because
\[
\sin^2\theta
=
-(2+\cos\theta)^2
+
4(2+\cos\theta)
-
3,
\]
we get
\[
\int_0^{2\pi}
\frac{\sin^2\theta}{(2+\cos\theta)^7}
\,d\theta
=
-J_5(2)+4J_6(2)-3J_7(2)
=
\frac{59\sqrt3\pi}{1944}.
\]
Multiplying by \(16\) gives
\[
\frac{118\sqrt3\pi}{243},
\]
which proves the energy expansion and its second-derivative form.

## Verification

The bundled symbolic checker verifies:

- the derivative formula for the profile rate;
- the critical polynomial
  \[
  3\cos^2\theta-2\cos\theta-4;
  \]
- the unique admissible critical cosine
  \[
  (1-\sqrt{13})/3;
  \]
- the exact maximal-rate coefficient;
- the recurrence values \(J_5(2)\), \(J_6(2)\), and \(J_7(2)\);
- the exact profile integral
  \[
  59\sqrt3\pi/1944;
  \]
- the global energy coefficient
  \[
  118\sqrt3\pi/243.
  \]

The checker also confirms that the point \(\theta=\pi/2\) used in the source has initial scalar production rate
\[
-\kappa'(s)/4,
\]
whereas the true profile maximum is larger by the universal factor
\[
4.8385048269546666\ldots.
\]

No finite sampling is used to establish any infinite or exact statement.

## Relationship to prior work

Kunikawa proves that flatness of the normal bundle need not be preserved by mean curvature flow. For the compact torus, the paper derives the exact commutator source
\[
\mathcal C(\nu,\xi)
=
\frac{2\kappa'\sin\theta}{(2+\cos\theta)^4}
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}
\]
and evaluates it at
\[
\theta=\pi/2
\]
to obtain one nonzero witness. Together with the general evolution criterion, this proves instantaneous loss of flatness.

The inspected source does not extract the full first-time derivative of the scalar normal curvature over the profile circle, locate its maximizing latitude, or compute the quadratic onset of an integrated normal-curvature energy.

Baker and Nguyen derived a general evolution equation involving normal curvature and gradient terms for codimension-two surfaces. Their work predates this compact torus and addresses pinched-flow convergence rather than the exact first-order production profile of Kunikawa's example.

Targeted searches by source identifier, exact rate formula, the \(\sqrt{13}\) critical point, and the global energy coefficient did not locate a covering result.

## Limitations

The result concerns the specific compact torus family with profile
\[
(2+\cos\theta,\sin\theta).
\]
It does not give a corresponding closed formula for arbitrary profiles satisfying Kunikawa's general ansatz.

The maximizing latitude is a statement about the instantaneous derivative at time zero. It need not remain the point of maximal normal curvature at later times.

The global quantity
\[
\mathcal E(t)
\]
uses the scalar normal curvature of an oriented codimension-two surface. The square makes the energy independent of orientation choices.

## References

1. Keita Kunikawa, *Counterexamples to preservation of flat normal bundles under mean curvature flow*, arXiv:2609.34291v1, first submitted 28 September 2026.
2. Charles Baker and Huy The Nguyen, *Codimension two surfaces pinched by normal curvature evolving by mean curvature flow*, Annales de l'Institut Henri Poincaré C, Analyse non linéaire 34 (2017), 1599--1610.
