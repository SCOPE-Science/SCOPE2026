# A unique minimum in the stretched-exponential Fock Korenblum radius

## Finding

For
\[
m>0,
\]
consider the Hilbert Fock space of entire functions with radial weight
\[
e^{-|z|^m}.
\]
The recent sharp Korenblum theorem gives its exact Korenblum radius as
\[
K(m)
=
\left(
\frac{\Gamma(4/m)}{\Gamma(2/m)}
\right)^{1/2}.
\]

This radius is not monotone in the decay exponent. It has a unique global minimum.

Let
\[
x_*>0
\]
be the unique solution of
\[
\psi\!\left(x_*+\frac12\right)
=
-2\log2,
\]
where \(\psi\) is the digamma function, and define
\[
m_*=\frac2{x_*}.
\]
Then
\[
K'(m)<0
\qquad(0<m<m_*),
\]
and
\[
K'(m)>0
\qquad(m>m_*).
\]
Consequently \(m_*\) is the unique global minimizer.

Numerically,
\[
x_*=0.145034743166672\ldots,
\]
\[
m_*=13.7897993014103\ldots,
\]
and
\[
K(m_*)=0.693483574639660\ldots.
\]

At the two ends of the family,
\[
K(m)\longrightarrow\infty
\qquad(m\downarrow0),
\]
whereas
\[
K(m)\longrightarrow\frac1{\sqrt2}
\qquad(m\to\infty).
\]
The latter limit is approached from below, with
\[
K(m)
=
\frac1{\sqrt2}
\left(
1-\frac{\gamma}{m}
+
\frac{\gamma^2+\pi^2}{2m^2}
+
O(m^{-3})
\right),
\]
where \(\gamma\) is Euler's constant.

Thus increasing the stretched-exponential decay exponent first lowers the exact Korenblum radius, but only up to one distinguished exponent; beyond it the radius reverses direction and rises toward \(1/\sqrt2\).

## Assumptions and scope

For a nonnegative radial weight \(W\) on \([0,\infty)\), the source writes the Hilbert Fock-type norm in the form
\[
\|f\|_W^2
=
\frac1\pi
\int_{\mathbb C}
|f(z)|^2W(|z|^2)\,dA(z).
\]
For a non-increasing radial weight with finite moments
\[
m_k=\int_0^\infty t^kW(t)\,dt,
\]
its sharp Korenblum radius is
\[
\sqrt{m_1/m_0}.
\]

For the stretched-exponential weight
\[
e^{-|z|^m},
\]
one has
\[
W(t)=e^{-t^{m/2}},
\]
and direct integration gives the exact radius
\[
K(m)
=
\left(
\frac{\Gamma(4/m)}{\Gamma(2/m)}
\right)^{1/2}.
\]
The source proves this formula for every \(m>0\); the present result analyzes its complete dependence on \(m\).

No assertion is made here for non-Hilbert Fock exponents, where the source records that the optimal Korenblum radius remains open in general. No assertion is made for weights outside this stretched-exponential family.

## Proof

Set
\[
x=\frac2m.
\]
Then
\[
K(m)^2
=
\frac{\Gamma(2x)}{\Gamma(x)}.
\]
The duplication formula
\[
\Gamma(2x)
=
\frac{2^{2x-1}}{\sqrt\pi}
\Gamma(x)\Gamma\!\left(x+\frac12\right)
\]
gives the simpler exact representation
\[
K(m)^2
=
\frac{2^{2x-1}}{\sqrt\pi}
\Gamma\!\left(x+\frac12\right).
\]
Define
\[
H(x)=\log K(2/x)^2.
\]
Then
\[
H'(x)
=
2\log2
+
\psi\!\left(x+\frac12\right),
\]
and
\[
H''(x)
=
\psi_1\!\left(x+\frac12\right)>0,
\]
where \(\psi_1\) is the trigamma function. Thus \(H'\) is strictly increasing.

At the left endpoint,
\[
\psi\!\left(\frac12\right)
=
-\gamma-2\log2,
\]
so
\[
H'(0+)=-\gamma<0.
\]
As \(x\to\infty\),
\[
\psi\!\left(x+\frac12\right)\to\infty,
\]
so \(H'(x)\to\infty\). Therefore there is exactly one zero \(x_*\) of \(H'\), characterized by
\[
\psi\!\left(x_*+\frac12\right)
=-2\log2.
\]
Since \(H''>0\), this zero is the unique global minimizer of \(H\), and hence of \(K(2/x)\).

Because
\[
x=2/m
\]
is strictly decreasing in \(m\), the direction reverses when translated back to the decay exponent. For
\[
0<m<m_*
\]
one has \(x>x_*\), hence \(H'(x)>0\) and \(K'(m)<0\). For
\[
m>m_*
\]
one has \(x<x_*\), hence \(H'(x)<0\) and \(K'(m)>0\). This proves the unique-minimum statement.

For the large-\(m\) endpoint, use the expansion
\[
\log\Gamma(x)
=
-\log x
-
\gamma x
+
\frac{\zeta(2)}2x^2
-
\frac{\zeta(3)}3x^3
+
O(x^4)
\]
as \(x\downarrow0\). Subtracting the versions at \(2x\) and \(x\) gives
\[
\log K(m)^2
=
-\log2
-
\gamma x
+
\frac{3\zeta(2)}2x^2
+
O(x^3).
\]
Since \(x=2/m\),
\[
\log K(m)
=
-\frac12\log2
-
\frac\gamma m
+
\frac{\pi^2}{2m^2}
+
O(m^{-3}).
\]
Exponentiating yields
\[
K(m)
=
\frac1{\sqrt2}
\left(
1-\frac\gamma m
+
\frac{\gamma^2+\pi^2}{2m^2}
+
O(m^{-3})
\right).
\]
In particular, the limit is \(1/\sqrt2\), and the negative first correction shows that the approach is from below.

Finally, Stirling's formula applied to
\[
\Gamma(2x)/\Gamma(x)
\]
shows that this ratio tends to infinity as \(x\to\infty\), hence
\[
K(m)\to\infty
\]
as \(m\downarrow0\).

## Verification

The exact-radius input was checked in the primary source at Theorem 1.3, where the stretched-exponential family is explicitly evaluated as
\[
K(m)
=
\sqrt{\Gamma(4/m)/\Gamma(2/m)}.
\]
The source's first page also gives primary MSC 30H20.

The monotonicity proof is symbolic. After the change of variable
\[
x=2/m,
\]
the gamma duplication formula reduces the derivative to a single digamma term. Strict positivity of the trigamma function proves that there can be only one critical point, while the exact value
\[
\psi(1/2)=-\gamma-2\log2
\]
and divergence of \(\psi\) prove that the critical point exists.

High-precision numerical evaluation gives
\[
x_*=0.1450347431666722513\ldots,
\]
\[
m_*=13.7897993014103049\ldots,
\]
and
\[
K(m_*)=0.693483574639660427\ldots.
\]
These decimals are consistency checks only; existence, uniqueness, and the sign pattern are proved analytically.

The large-\(m\) coefficient was independently checked by expanding
\[
\log\Gamma(2x)-\log\Gamma(x)
\]
through second order. No finite experiment is used to infer the global theorem.

## Relationship to prior work

Wikström proves the exact Korenblum radius for every non-increasing radial Hilbert-Fock weight and explicitly records, for the family \(e^{-|z|^m}\), the formula
\[
\sqrt{\Gamma(4/m)/\Gamma(2/m)}.
\]
The inspected paper does not analyze this formula as a function of \(m\): it contains no monotonicity theorem for the stretched-exponential exponent, no critical exponent, and no large-\(m\) expansion of the radius.

Earlier work of Wee and Le obtained closed-form upper bounds for Korenblum constants in weighted Fock spaces, including gamma-function expressions for power-exponential weights. The recent theorem identifies the relevant Hilbert-space upper bounds as exact. Publicly accessible material for the earlier paper states its upper-bound program but does not expose a full-text parameter-minimization theorem; this remains a literature-access risk rather than a claimed whole-document noncoverage result.

A previous exact-radius equality analysis for general monotone weights classifies which function pairs attain equality at the sharp radius. That classification is logically different from the present question: it fixes a weight and studies extremizers, whereas the present theorem varies the stretched-exponential exponent and classifies the radius itself over the entire parameter family.

Targeted searches for the exact gamma ratio, its digamma critical equation, stretched-exponential Fock Korenblum monotonicity, and the numerical minimizer did not locate an implication-equivalent published result.

## Limitations

The theorem is a parameter classification of an already established exact-radius formula. It does not enlarge the class of weights for which Korenblum's principle is known sharply.

The numerical value of \(m_*\) is not an algebraic closed form; its exact characterization is the unique digamma equation stated above.

The result is restricted to the Hilbert-space setting. The source notes that other Fock exponents remain open in general, so no analogous phase statement is asserted there.

The full text of the most relevant 2023 weighted-Fock upper-bound paper was not available through the accessible source used for this comparison. Its abstract and the recent paper's discussion were inspected, and this access limitation is retained as a residual originality risk.

## References

1. F. Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space*, arXiv:2609.39622v1, first posted 30 September 2026.
2. J. Wee and H. K. Le, *Korenblum constants for various weighted Fock spaces*, Complex Variables and Elliptic Equations 68 (2023), 1385--1406, DOI: 10.1080/17476933.2022.2052862.
3. J. Wee and H. K. Le, *On Korenblum constants for some weighted function spaces*, Thang Long Journal of Science: Mathematics and Mathematical Sciences 2 (2023), 87--116.
