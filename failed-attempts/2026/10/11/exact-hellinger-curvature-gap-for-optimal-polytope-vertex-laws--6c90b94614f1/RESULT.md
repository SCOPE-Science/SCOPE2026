# Exact Hellinger curvature gap for optimal polytope vertex laws

## Finding

Let
\[
K\subset\mathbb R^d,\qquad d\ge2,
\]
be a \(C^2_+\) convex body. Write \(\kappa>0\) for its Gauss curvature and \(dS\) for surface measure, and define
\[
a=\frac1{d+1},
\qquad
b=\frac d{d+1},
\qquad
I_t(K)=\int_{\partial K}\kappa(x)^t\,dS(x).
\]

The unique asymptotically optimal limiting vertex distributions for inscribed volume and mean-width approximation are
\[
d\mu_V
=
\frac{\kappa^a}{I_a}\,dS,
\qquad
d\mu_W
=
\frac{\kappa^b}{I_b}\,dS.
\]

Use the squared Hellinger convention
\[
H^2(\mu_V,\mu_W)
=
\frac12
\int_{\partial K}
\left(
\sqrt{\frac{d\mu_V}{dS}}
-
\sqrt{\frac{d\mu_W}{dS}}
\right)^2
dS.
\]
Then
\[
\boxed{
H^2(\mu_V,\mu_W)
=
1-
\frac{I_{1/2}}
{\sqrt{I_aI_b}}.
}
\]

This mismatch admits an exact curvature-variance representation. Define
\[
F(t)=\log I_t
\]
and the probability measure
\[
d\mu_t
=
\frac{\kappa^t}{I_t}\,dS.
\]
Then
\[
F''(t)
=
\operatorname{Var}_{\mu_t}(\log\kappa),
\]
and
\[
\boxed{
-\log(1-H^2)
=
\frac12
\int_a^b
\min\{t-a,b-t\}\,
\operatorname{Var}_{\mu_t}(\log\kappa)\,dt.
}
\]

In particular,
\[
\boxed{
H(\mu_V,\mu_W)=0
\quad\Longleftrightarrow\quad
K\ \text{is a Euclidean ball}.
}
\]
Thus the rigidity mechanism behind simultaneous optimal volume and mean-width approximation has a canonical quantitative scalar: the Hellinger separation of its two optimal vertex laws.

The quantity is invariant under Euclidean similarities.

## Assumptions and scope

The condition \(C^2_+\) means that \(\partial K\) is \(C^2\) and has strictly positive Gauss curvature. Hence \(\kappa\) is positive and continuous on the compact boundary, so every \(I_t\) used above is finite and positive and \(\log\kappa\) is bounded.

The result concerns the limiting vertex probability laws for the inscribed volume and mean-width problems. It does not claim that Hellinger distance between the limiting laws controls Hausdorff distance, Banach--Mazur distance, or another geometric distance from \(K\) to a ball.

No probabilistic sampling assumption is required for the identity itself; only the two source-proved optimal densities are used.

## Proof

The source gives
\[
\frac{d\mu_V}{dS}
=
\frac{\kappa^a}{I_a},
\qquad
\frac{d\mu_W}{dS}
=
\frac{\kappa^b}{I_b},
\]
with
\[
a+b=1.
\]
For probability densities \(p,q\), the stated Hellinger convention gives
\[
H^2(p,q)
=
1-\int\sqrt{pq}.
\]
Therefore
\[
\begin{aligned}
1-H^2(\mu_V,\mu_W)
&=
\int_{\partial K}
\sqrt{
\frac{\kappa^a}{I_a}
\frac{\kappa^b}{I_b}
}\,dS\\
&=
\frac1{\sqrt{I_aI_b}}
\int_{\partial K}
\kappa^{(a+b)/2}\,dS\\
&=
\frac{I_{1/2}}{\sqrt{I_aI_b}},
\end{aligned}
\]
which proves the first formula.

Cauchy--Schwarz applied to
\[
u=\kappa^{a/2},
\qquad
v=\kappa^{b/2}
\]
gives
\[
I_{1/2}^2
\le
I_aI_b.
\]
Equality holds exactly when \(u\) and \(v\) are proportional almost everywhere. Since
\[
b-a=\frac{d-1}{d+1}>0
\]
and \(\kappa\) is positive and continuous, equality is equivalent to \(\kappa\) being constant on \(\partial K\). A closed strictly convex hypersurface of constant Gauss curvature is a round sphere. Hence \(H=0\) exactly for Euclidean balls.

For the variance formula, differentiation under the integral is legitimate because \(\log\kappa\) is bounded. We obtain
\[
F'(t)
=
\int_{\partial K}
\log\kappa\,d\mu_t
\]
and
\[
F''(t)
=
\int_{\partial K}
(\log\kappa)^2\,d\mu_t
-
\left(
\int_{\partial K}
\log\kappa\,d\mu_t
\right)^2
=
\operatorname{Var}_{\mu_t}(\log\kappa).
\]

Let
\[
c=\frac{a+b}{2}=\frac12.
\]
The exact midpoint second-difference identity
\[
F(a)+F(b)-2F(c)
=
\int_a^b
\min\{t-a,b-t\}\,F''(t)\,dt
\]
follows by integrating by parts separately on \([a,c]\) and \([c,b]\). On the other hand,
\[
-\log(1-H^2)
=
\frac12\bigl(F(a)+F(b)\bigr)-F(c).
\]
Combining the last three displays yields the variance representation.

Finally, under a dilation
\[
K\longmapsto sK,
\]
the curvature and area element scale as
\[
\kappa\longmapsto s^{-(d-1)}\kappa,
\qquad
dS\longmapsto s^{d-1}dS.
\]
Hence
\[
I_t\longmapsto
s^{(d-1)(1-t)}I_t.
\]
Because \(a+b=1\), the scaling factors cancel in
\[
I_{1/2}/\sqrt{I_aI_b}.
\]
Rigid motions plainly preserve the same quantity, proving similarity invariance.

## Verification

The bundled checker verifies the exponent identities
\[
a+b=1,
\qquad
\frac{a+b}{2}=\frac12,
\]
the exact cancellation of all dilation exponents, and the algebra converting the Hellinger affinity into the curvature-moment formula.

It also verifies the midpoint-kernel coefficient by the two integration-by-parts boundary formulas: the derivative terms at the midpoint cancel because
\[
c-a=b-c.
\]
The arbitrary-body variance identity is proved analytically above; no finite sampling or numerical curvature experiment is used as a substitute.

As a normalization check, when \(\kappa\) is constant the two source densities are both the normalized surface measure, and the formula gives \(H=0\).

## Relationship to prior work

Hoehner proves that asymptotically best inscribed volume approximants have the unique limiting density proportional to
\[
\kappa^{1/(d+1)},
\]
whereas asymptotically best mean-width approximants have the unique limiting density proportional to
\[
\kappa^{d/(d+1)}.
\]
The paper compares these curvature biases and proves that equality of the two normalized densities forces constant Gauss curvature and hence a Euclidean ball.

The inspected primary text does not introduce Hellinger or Bhattacharyya distance between these laws and does not state an exact scalar mismatch or an integrated variance formula for their separation.

Besau, Hoehner, and Kur developed the earlier intrinsic-volume approximation framework and optimal random densities that motivate the later rigidity question. The inspected public article does not state the Hellinger curvature-moment identity above.

The present result therefore quantifies the exact incompatibility used qualitatively in the rigidity proof: its Bhattacharyya affinity is
\[
\frac{I_{1/2}}{\sqrt{I_aI_b}},
\]
and its logarithmic deficit is precisely an integrated variance of \(\log\kappa\).

## Limitations

A positive Hellinger gap proves that the two optimal limiting vertex laws differ, but no lower bound in terms of a geometric distance from \(K\) to a ball is asserted.

The identity requires strictly positive continuous curvature. Extensions to nonsmooth convex bodies would require a different formulation of the curvature densities.

The formula concerns the volume-versus-mean-width pair. Other pairs of intrinsic-volume objectives have different optimal curvature weights and would require a separate analysis.

## References

1. Steven Hoehner, *One polytope fits all: Characterization of the Euclidean ball via simultaneous intrinsic volume approximation*, arXiv:2602.18547v1, first submitted 20 February 2026.
2. Florian Besau, Steven Hoehner, and Gil Kur, *Intrinsic and Dual Volume Deviations of Convex Bodies and Polytopes*, International Mathematics Research Notices 2021, no. 22, 17456--17513; arXiv:1905.08862.
