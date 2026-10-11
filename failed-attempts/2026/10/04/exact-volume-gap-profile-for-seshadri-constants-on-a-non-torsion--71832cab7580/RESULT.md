# Exact volume-gap profile for Seshadri constants on a non-torsion elliptic ruled surface

## Finding
Let \(X\) be a smooth elliptic curve, let \(\eta\in\operatorname{Pic}^0(X)\) be non-torsion, and let
\[
S=\mathbb P(\mathcal O_X\oplus\mathcal O_X(\eta)).
\]
Write \(X_0,X_1\) for the two disjoint minimal sections and \(f\) for a fiber. Fix
\(x\in S\setminus(X_0\cup X_1)\). For an ample numerical class
\[
A\equiv aX_0+b f,\qquad a,b>0,
\]
put
\[
t=\frac{a}{2b},\qquad n=\lfloor\sqrt t\rfloor .
\]
Fuentes García's exact formula gives
\[
\varepsilon(A,x)=\frac{2n(n+1)b+a}{2n+1},
\qquad A^2=2ab.
\]
From it one obtains the exact volume-gap factorization
\[
A^2-\varepsilon(A,x)^2
=
\frac{(a-2bn^2)(2b(n+1)^2-a)}{(2n+1)^2}.
\]
Therefore \(\varepsilon(A,x)=\sqrt{A^2}\) if and only if \(t\) is a positive integer square.

For every chamber \(n\ge1\),
\[
\sqrt{1-\frac1{(2n+1)^2}}\,\sqrt{A^2}
\le
\varepsilon(A,x)
\le
\sqrt{A^2},
\]
and the lower equality holds exactly when
\[
t=n(n+1).
\]
In particular, on the whole region \(a\ge2b\),
\[
\frac{\varepsilon(A,x)}{\sqrt{A^2}}
\ge
\frac{2\sqrt2}{3},
\]
with equality exactly on the numerical ray \(a=4b\). The optimal relative square-deficit in the \(n\)-th chamber is \(1/(2n+1)^2\), hence the normalized Seshadri constants approach the volume bound uniformly as the chamber index tends to infinity.

## Assumptions and scope
The base field is \(\mathbb C\). The line bundle parameter \(\eta\in\operatorname{Pic}^0(X)\) is non-torsion, and the point lies off the two distinguished sections. The statement concerns numerical ample classes; it therefore applies in particular to ample integral divisor classes.

The source formula is the non-torsion elliptic ruled-surface case of Fuentes García. His preceding construction produces the curves
\[
C_n\equiv 2n(n+1)X_0+f
\]
with multiplicity \(2n+1\) at \(x\), and identifies their influence chambers by
\[
n^2<\frac{a}{2b}<(n+1)^2.
\]
At chamber boundaries the same displayed formula remains valid by continuity and the explicit floor convention.

## Proof
Set \(t=a/(2b)\). Since \(A^2=2ab=4b^2t\), Fuentes García's formula can be rewritten as
\[
\varepsilon(A,x)
=
2b\frac{t+n(n+1)}{2n+1}.
\]
Consequently
\[
A^2-\varepsilon(A,x)^2
=
4b^2\left(
t-\frac{(t+n(n+1))^2}{(2n+1)^2}
\right).
\]
The numerator factors identically:
\[
(2n+1)^2t-(t+n(n+1))^2
=
(t-n^2)((n+1)^2-t).
\]
Substituting \(t=a/(2b)\) gives
\[
A^2-\varepsilon(A,x)^2
=
\frac{(a-2bn^2)(2b(n+1)^2-a)}{(2n+1)^2}.
\]

Because \(n=\lfloor\sqrt t\rfloor\), one has
\[
n^2\le t<(n+1)^2.
\]
Thus the two factors in the numerator are nonnegative. For \(n\ge1\), equality with the volume bound occurs precisely at a chamber wall; globally this says
\[
t=m^2
\]
for some positive integer \(m\). When \(0<t<1\), one has \(n=0\) and \(\varepsilon(A,x)=a\); equality with \(\sqrt{A^2}\) again occurs only at \(t=1\). Hence the perfect-square characterization is complete.

For \(n\ge1\),
\[
\frac{\varepsilon(A,x)^2}{A^2}
=
\frac{(t+n(n+1))^2}{(2n+1)^2t}.
\]
Let \(c=n(n+1)\). The numerator after division by \(t\) is
\[
t+2c+\frac{c^2}{t},
\]
which is minimized at \(t=c\) by the arithmetic-geometric mean inequality, or equivalently by differentiation. Therefore
\[
\frac{\varepsilon(A,x)^2}{A^2}
\ge
\frac{4c}{(2n+1)^2}
=
1-\frac1{(2n+1)^2},
\]
with equality exactly at \(t=n(n+1)\).

The chamber lower bounds increase strictly with \(n\), so the smallest one for \(n\ge1\) occurs at \(n=1\):
\[
\frac{\varepsilon(A,x)}{\sqrt{A^2}}
\ge
\sqrt{1-\frac19}
=
\frac{2\sqrt2}{3}.
\]
Its equality condition is \(t=2\), equivalently \(a=4b\). Finally,
\[
0\le
1-\frac{\varepsilon(A,x)^2}{A^2}
\le
\frac1{(2n+1)^2},
\]
which gives the uniform convergence assertion.

## Verification
The source theorem was inspected in the full paper, including the construction of the curves \(C_n\), their influence chambers, and the exact formula for \(\varepsilon(A,x)\). The general upper bound \(\varepsilon(A,x)\le\sqrt{A^2}\) is also stated there.

The bundled checker verifies the factorization as exact rational arithmetic over a large finite box, checks the perfect-square equality criterion there, and checks the sharp chamber lower bound and its equality locus. These finite checks are regression tests only; the proof above establishes the universal statement.

## Relationship to prior work
Fuentes García completely determines Seshadri constants on rational and elliptic ruled surfaces and gives the exact formula used here. His paper also emphasizes comparison with the volume bound \(\sqrt{A^2}\) and constructs examples arbitrarily close to it. The later primer by Bauer, Di Rocco, Harbourne, Kapustka, Knutsen, Syzdek, and Szemberg summarizes the ruled-surface formulas and the near-maximality theme.

The present statement is not a new formula for the Seshadri constant itself. Its contribution is the exact factorization of the volume gap on the non-torsion elliptic surface, the classification of all maximal numerical rays by square slopes, and the sharp chamber-by-chamber normalized stability profile, including the optimal global constant \(2\sqrt2/3\) on \(a\ge2b\).

## Limitations
The result is restricted to the decomposable elliptic ruled surface with non-torsion degree-zero parameter and to points off the two distinguished sections. It does not address the torsion cases, the indecomposable elliptic ruled surfaces, multipoint Seshadri constants, or blow-ups. The originality search cannot exclude an equivalent observation hidden under different notation; the residual risk is confined to that possibility.

## References
1. L. Fuentes García, *Seshadri constants on ruled surfaces: the rational and the elliptic cases*, arXiv:math/0503253 (first public version 2005-03-14); Manuscripta Math. 119 (2006), 483–505.
2. T. Bauer, S. Di Rocco, B. Harbourne, M. Kapustka, A. L. Knutsen, W. Syzdek, T. Szemberg, *A primer on Seshadri constants*, arXiv:0810.0728.
