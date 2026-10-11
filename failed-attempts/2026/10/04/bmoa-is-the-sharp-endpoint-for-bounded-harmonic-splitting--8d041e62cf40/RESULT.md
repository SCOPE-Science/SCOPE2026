# BMOA is the sharp endpoint for bounded harmonic splitting

## Finding

Let
\[
f=h+\overline g
\]
be a bounded complex-valued harmonic mapping on the unit disk \(\mathbb D\), with the canonical normalization
\[
g(0)=0.
\]
Then there is an absolute constant \(C\) such that
\[
\|h\|_{\mathrm{BMOA}}+\|g\|_{\mathrm{BMOA}}
\le
C\|f\|_\infty.
\]

In the standard derivative-Carleson formulation this gives
\[
\sup_{I\subset\mathbb T}
\frac1{|I|}
\int_{S(I)}
\left(
|h'(z)|^2+|g'(z)|^2
\right)
(1-|z|^2)\,dA(z)
\le
C\|f\|_\infty^2,
\]
where \(S(I)\) is a Carleson box over an arc \(I\subset\mathbb T\).

This endpoint is sharp even under strong geometric restrictions. For every
\[
K>1
\]
there exists a bounded globally univalent harmonic mapping
\[
f=h+\overline g
\]
whose maximal quasiconformal dilatation is at most \(K\) and for which
\[
h,g\in\mathrm{BMOA}\setminus H^\infty.
\]

Consequently the canonical splitting of bounded harmonic mappings is uniformly controlled in \(\mathrm{BMOA}\), but cannot be uniformly controlled in \(H^\infty\), even on any fixed globally univalent \(K\)-quasiconformal subclass with \(K>1\).

## Assumptions and scope

The decomposition
\[
f=h+\overline g
\]
is unique after requiring
\[
g(0)=0.
\]
No sense-preserving or quasiconformal hypothesis is needed for the universal \(\mathrm{BMOA}\) estimate.

One convenient norm on \(\mathrm{BMOA}\) is equivalent to
\[
|u(0)|
+
\sup_{I\subset\mathbb T}
\left[
\frac1{|I|}
\int_{S(I)}
|u'(z)|^2(1-|z|^2)\,dA(z)
\right]^{1/2}.
\]
The numerical value of \(C\) depends on the chosen equivalent norm convention; no optimal numerical constant is claimed.

The sharpness assertion uses quasiconformal dilatation in the usual upper-bound sense. Given any prescribed \(K>1\), the example may be chosen with maximal dilatation no larger than \(K\).

## Proof

Because \(f\) is bounded and harmonic, it has radial boundary values
\[
F\in L^\infty(\mathbb T)
\]
with
\[
\|F\|_{L^\infty}\le \|f\|_\infty,
\]
and \(f\) is the Poisson extension of \(F\).

Write
\[
h(z)=a_0+\sum_{n\ge1}a_nz^n,
\qquad
g(z)=\sum_{n\ge1}b_nz^n.
\]
Then the boundary Fourier expansion is
\[
F(e^{it})
=
a_0
+
\sum_{n\ge1}a_ne^{int}
+
\sum_{n\ge1}\overline{b_n}e^{-int}.
\]
Hence the nonnegative-frequency Riesz projection of \(F\) is exactly the boundary function of \(h\):
\[
P_+F=h^*.
\]
Likewise,
\[
P_+\overline F-\overline{a_0}=g^*.
\]

The endpoint Riesz projection theorem says
\[
P_+:L^\infty(\mathbb T)\longrightarrow\mathrm{BMO}(\mathbb T)
\]
boundedly. Since \(P_+F\) and
\[
P_+\overline F-\overline{a_0}
\]
have only nonnegative Fourier modes, their analytic Poisson extensions belong to \(\mathrm{BMOA}\). Therefore
\[
\|h\|_{\mathrm{BMOA}}+\|g\|_{\mathrm{BMOA}}
\le
C\|F\|_{L^\infty}
\le
C\|f\|_\infty.
\]
The standard \(\mathrm{BMOA}\) Carleson-measure characterization yields the displayed derivative estimate.

It remains to prove sharpness. Kalaj constructs, for every
\[
0<k<1,
\]
a bounded globally one-to-one harmonic mapping
\[
f=h+\overline g
\]
such that
\[
|g'(z)|\le k|h'(z)|
\]
throughout \(\mathbb D\), while \(h\) is unbounded. The differential inequality gives maximal quasiconformal dilatation at most
\[
\frac{1+k}{1-k}.
\]

Given \(K>1\), choose
\[
k=\frac{K-1}{K+1}.
\]
Kalaj's construction then gives a bounded globally univalent harmonic mapping of maximal dilatation at most \(K\) whose analytic part \(h\) is unbounded.

The coanalytic part is also unbounded. Indeed, if \(g\) were bounded, then
\[
h=f-\overline g
\]
would be bounded, contradicting the construction. Applying the universal part of the theorem to this bounded harmonic mapping gives
\[
h,g\in\mathrm{BMOA}.
\]
Thus
\[
h,g\in\mathrm{BMOA}\setminus H^\infty,
\]
which proves endpoint sharpness.

## Verification

The Fourier-mode identification was checked directly from the canonical harmonic expansion. The constant term belongs to \(h\) because of the normalization
\[
g(0)=0.
\]

The only functional-analytic input in the universal estimate is the classical endpoint boundedness of the Hilbert transform, equivalently the Riesz projection,
\[
L^\infty(\mathbb T)\to\mathrm{BMO}(\mathbb T),
\]
followed by the standard analytic \(\mathrm{BMOA}\) identification and its derivative-Carleson characterization.

The quasiconformal sharpness input was checked in the full primary source. Its theorem holds for every
\[
0<k<1
\]
and produces a bounded globally one-to-one harmonic map satisfying
\[
|g'|\le k|h'|
\]
with unbounded analytic part. The source explicitly converts this derivative bound into maximal dilatation
\[
(1+k)/(1-k).
\]

No limiting argument, numerical experiment, or assumption about boundary smoothness is used.

## Relationship to prior work

The harmonic \(\mathrm{BMO}\) framework is classical. In particular, harmonic \(\mathrm{BMO}\) spaces are Poisson extensions of boundary \(\mathrm{BMO}\) data, their analytic subspace is \(\mathrm{BMOA}\), and component seminorms are quantitatively comparable with the corresponding harmonic seminorms. Thus the universal \(\mathrm{BMOA}\) control is an endpoint projection fact.

Kalaj's 2026 theorem establishes the complementary phenomenon: boundedness, global univalence, and arbitrarily small quasiconformal distortion do not force the analytic component to be bounded. The paper does not identify \(\mathrm{BMOA}\) as the surviving uniform endpoint, nor does it state that both canonical components necessarily lie in
\[
\mathrm{BMOA}\setminus H^\infty.
\]

The combination gives a sharp endpoint dichotomy: \(\mathrm{BMOA}\) always survives, while \(H^\infty\) fails on every fixed quasiconformal class above the conformal endpoint. This conclusion is stronger than either ingredient alone.

Targeted searches using the source identifier, canonical harmonic splitting, analytic and coanalytic \(\mathrm{BMOA}\) components, and the globally univalent quasiconformal subclass did not locate a published statement of this endpoint-sharpness formulation.

## Limitations

No optimal numerical constant is claimed in the \(\mathrm{BMOA}\) estimate.

The theorem does not assert that \(\mathrm{BMOA}\) is minimal among all possible function spaces ordered by inclusion. Its sharpness statement is specifically the failure of the natural stronger target
\[
H^\infty.
\]

The unbounded-component examples use the geometry of Kalaj's construction. The theorem does not classify which additional boundary or image-domain regularity assumptions restore \(H^\infty\) control of the canonical components.

## References

1. D. Kalaj, *A bounded globally univalent quasiconformal harmonic map whose analytic part is unbounded*, arXiv:2605.01842v1, 2026.
2. M. Aljuaid and F. Colonna, *Composition Operators on Some Banach Spaces of Harmonic Mappings*, Journal of Function Spaces 2020, Article 9034387.
3. J. B. Garnett, *Bounded Analytic Functions*, revised first edition, Springer, 2007.
