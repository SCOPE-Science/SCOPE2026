# Asymmetric slit equality for the hyperbolic four-domain conjecture

## Finding

For arbitrary independent parameters
\[
a,b\in(0,1),
\]
define
\[
D_{+}(a)
=
\mathbb D\setminus[a,1)
\]
and
\[
D_{-}(b)
=
\mathbb D\setminus(-1,-b].
\]
Both domains are simply connected and contain
\[
0.
\]
Their union is exactly
\[
D_{+}(a)\cup D_{-}(b)=\mathbb D.
\]

At the origin, these domains satisfy equality in the four-domain additive inequality conjectured by He and Tang:
\[
\lambda_{D_{+}(a)\cap D_{-}(b)}(0)
+
\lambda_{D_{+}(a)\cup D_{-}(b)}(0)
=
\lambda_{D_{+}(a)}(0)
+
\lambda_{D_{-}(b)}(0).
\]

Put
\[
A=a+a^{-1},
\qquad
B=b+b^{-1}.
\]
Then the four densities are
\[
\lambda_{D_{+}(a)}(0)
=
\frac{A+2}{4},
\]
\[
\lambda_{D_{-}(b)}(0)
=
\frac{B+2}{4},
\]
\[
\lambda_{D_{+}(a)\cap D_{-}(b)}(0)
=
\frac{A+B}{4},
\]
and
\[
\lambda_{D_{+}(a)\cup D_{-}(b)}(0)
=
\lambda_{\mathbb D}(0)
=
1.
\]
Thus the equality is the identity
\[
\frac{A+B}{4}+1
=
\frac{A+2}{4}+\frac{B+2}{4}.
\]

The associated Fuchs quotient is therefore
\[
Q_{a,b}(0)
=
\frac{
\lambda_{D_{+}(a)\cap D_{-}(b)}(0)
}{
\lambda_{D_{+}(a)}(0)+\lambda_{D_{-}(b)}(0)
}
=
\frac{A+B}{A+B+4},
\]
so its exact deficit from the simply connected upper endpoint is
\[
1-Q_{a,b}(0)
=
\frac{4}{A+B+4}.
\]

The symmetric family recorded in the source corresponds to the diagonal
\[
a=b.
\]
Allowing the two slit depths to vary independently gives a full two-parameter equality family. In particular, equality in the proposed four-domain inequality does not force reflection symmetry, even among radial two-slit domains.

## Assumptions and scope

The hyperbolic density is normalized by
\[
\lambda_{\mathbb D}(0)=1,
\]
as in the cited source.

The result concerns the value at the common point
\[
0.
\]
It does not prove the four-domain conjecture for arbitrary simply connected domains and does not classify all equality cases.

The two parameters are independent. No relation between
\[
a
\]
and
\[
b
\]
is assumed beyond
\[
0<a,b<1.
\]

## Proof

The source proves that if
\[
G\subset\mathbb D
\]
is simply connected and contains
\[
0,
\]
then
\[
\lambda_G(0)
=
\operatorname{cap}(K_G),
\]
where
\[
K_G
=
\left\{
\frac1\zeta:
\zeta\in\widehat{\mathbb C}\setminus G
\right\}.
\]

For
\[
D_{+}(a)
=
\mathbb D\setminus[a,1),
\]
inversion gives
\[
K_{+}(a)
=
\overline{\mathbb D}\cup[1,a^{-1}].
\]
The unbounded complementary component is
\[
\Omega_{+}(a)
=
\{|w|>1\}\setminus[1,a^{-1}].
\]
The Joukowski map
\[
J(w)=w+\frac1w
\]
is conformal on
\[
\{|w|>1\}
\]
and maps
\[
[1,a^{-1}]
\]
onto
\[
[2,A],
\qquad
A=a+a^{-1}.
\]
Hence
\[
J:
\Omega_{+}(a)
\longrightarrow
\widehat{\mathbb C}\setminus[-2,A]
\]
is conformal and satisfies
\[
J'(\infty)=1.
\]
Since a real interval
\[
[u,v]
\]
has logarithmic capacity
\[
\frac{v-u}{4},
\]
capacity invariance under this normalized conformal map gives
\[
\lambda_{D_{+}(a)}(0)
=
\frac{A+2}{4}.
\]

The negative slit is identical after reflection:
\[
K_{-}(b)
=
\overline{\mathbb D}\cup[-b^{-1},-1],
\]
and therefore
\[
\lambda_{D_{-}(b)}(0)
=
\frac{B+2}{4},
\qquad
B=b+b^{-1}.
\]

Now consider
\[
U_{a,b}
=
D_{+}(a)\cap D_{-}(b).
\]
It is connected, and its inverted compact set is
\[
K_{a,b}
=
\overline{\mathbb D}
\cup
[-b^{-1},-1]
\cup
[1,a^{-1}].
\]
Its unbounded complementary component is
\[
\Omega_{a,b}
=
\{|w|>1\}
\setminus
\left(
[-b^{-1},-1]
\cup
[1,a^{-1}]
\right).
\]

Because the Joukowski map is injective on
\[
\{|w|>1\},
\]
and because
\[
J([-b^{-1},-1])=[-B,-2],
\]
while
\[
J([1,a^{-1}])=[2,A],
\]
one obtains
\[
J(\Omega_{a,b})
=
\widehat{\mathbb C}\setminus[-B,A].
\]
Again
\[
J'(\infty)=1.
\]
Therefore
\[
\lambda_{U_{a,b}}(0)
=
\operatorname{cap}(K_{a,b})
=
\operatorname{cap}([-B,A])
=
\frac{A+B}{4}.
\]

Finally,
\[
D_{+}(a)\cup D_{-}(b)=\mathbb D,
\]
because each removed radial slit is contained in the other domain. Thus
\[
\lambda_{D_{+}(a)\cup D_{-}(b)}(0)=1.
\]
Substitution gives
\[
\frac{A+B}{4}+1
=
\frac{A+2}{4}+\frac{B+2}{4},
\]
which proves the claimed equality and the quotient formula.

## Verification

The proof uses the same three exact ingredients as the source's symmetric computation: inversion to logarithmic capacity, the Joukowski map on the exterior disk, and
\[
\operatorname{cap}([u,v])=\frac{v-u}{4}.
\]

The only new geometric step is allowing different positive and negative slit depths. It is valid because
\[
J
\]
is injective on the full exterior disk. Therefore deleting
\[
[1,a^{-1}]
\]
and
\[
[-b^{-1},-1]
\]
deletes independently the image intervals
\[
[2,A]
\]
and
\[
[-B,-2].
\]
Together with the already excluded interval
\[
[-2,2],
\]
these form the single interval
\[
[-B,A].
\]

Direct substitution also verifies the equality algebraically:
\[
\frac{A+B}{4}+1
-
\frac{A+2}{4}
-
\frac{B+2}{4}
=
0.
\]

No numerical approximation is used in the proof.

## Relationship to prior work

He and Tang solve Fuchs's original extremal problem for the hyperbolic density and formulate a stronger open four-domain additive inequality. They explicitly note that equality is possible and exhibit the reflection-symmetric one-parameter family
\[
\mathbb D\setminus[a,1),
\qquad
\mathbb D\setminus(-1,-a].
\]

Their sharpness calculation already supplies the one-slit capacity formula and the symmetric two-slit Joukowski computation. The inspected full text keeps the two slit depths equal throughout that equality example. It does not state the independent-parameter family or the resulting non-rigidity of reflection symmetry.

The multiplicative intersection inequality of Solynin and the strong submultiplicativity result of Kraus and Roth concern a different multiplicative relation between the same four domains. They do not imply the additive equality family above.

Targeted searches using the source identifier, asymmetric-slit terminology, independent slit parameters, and four-domain equality formulations did not locate an implication-equivalent published statement.

## Limitations

The result supplies a two-parameter equality family for the conjectured inequality; it does not prove the conjecture itself.

Equality is established at the origin. No claim is made that the same pair gives equality at every point of the intersection.

The family shows that reflection symmetry is unnecessary, but it does not classify all equality configurations.

The domains are radial slit disks. More general slit geometries may have a substantially richer equality structure.

## References

1. Y. He and Q. Tang, *On Fuchs's additive intersection problem for the hyperbolic metric*, arXiv:2603.16676v1, first posted 17 March 2026.
2. A. Yu. Solynin, *Ordering of sets, hyperbolic metrics, and harmonic measures*, Journal of Mathematical Sciences 95 (1999), 2256--2266.
3. D. Kraus and O. Roth, *Strong submultiplicativity of the Poincaré metric*, Journal of Analysis 24 (2016), 39--50.
