# Arithmetic primitivity of the Pluecker triple for a general smooth plane curve
## Finding
Let
\[
C\subset\mathbb P^2_{\mathbb C}
\]
be a general smooth plane curve of degree
\[
d\ge4.
\]
Consider the three classical Pluecker enumerative invariants
\[
D=d(d-1),
\]
the degree of the dual curve,
\[
F=3d(d-2),
\]
the number of inflection tangents, and
\[
B=\frac12d(d-2)(d-3)(d+3),
\]
the number of bitangents.

Their common divisor is exactly
\[
\gcd(D,F,B)=d.
\]
Thus the normalized triple
\[
\left(\frac Dd,\frac Fd,\frac Bd\right)
\]
is primitive for every degree.

In fact the complete pairwise common-divisor pattern is
\[
\gcd(D,F)
=
d\begin{cases}
3,&d\equiv1\pmod3,\\
1,&d\not\equiv1\pmod3,
\end{cases}
\]
\[
\gcd(D,B)
=
d\begin{cases}
1,&d\text{ even},\\
4,&d\equiv1\pmod4,\\
2,&d\equiv3\pmod4,
\end{cases}
\]
and
\[
\gcd(F,B)
=
d\,u_d
\begin{cases}
3,&3\mid d,\\
1,&3\nmid d,
\end{cases}
\]
where
\[
u_d=
\begin{cases}
(d-2)/2,&d\text{ even},\\
d-2,&d\text{ odd}.
\end{cases}
\]
Hence every common factor shared by two of the three fundamental dual-line counts is explicit, but no prime survives in all three after the unavoidable factor coming from the degree of the original curve is removed.

## Assumptions and scope
The curve is general and smooth over \(\mathbb C\), with degree at least four. Generality ensures that the singularities of the dual relevant here are ordinary nodes and cusps, corresponding respectively to simple bitangents and simple inflection tangents.

The integers \(B\) and \(F\) count geometric bitangent and inflection lines without multiplicity in this generic situation. For special smooth curves, higher tangency can merge classical Pluecker contributions, so the same literal count of distinct lines need not apply.

## Proof
For a general smooth plane curve of degree \(d\), the classical Pluecker formulas give
\[
D=d(d-1),
\qquad
F=3d(d-2),
\qquad
B=\frac12d(d-2)(d-3)(d+3).
\]
The first formula is the degree of the dual curve. The second is also obtained by intersecting the curve with its Hessian, whose degree is \(3(d-2)\). The third follows from the genus formula for the dual curve after inserting its degree and its cusp count.

Divide the three integers by their evident common factor \(d\), and set
\[
A=d-1,
\qquad
C=3(d-2),
\qquad
E=\frac{(d-2)(d-3)(d+3)}2.
\]
We prove the pairwise formulas for \(A,C,E\).

First,
\[
\gcd(A,C)
=
\gcd(d-1,3(d-2))
=
\gcd(d-1,3),
\]
because consecutive integers are coprime. Hence this gcd is \(3\) exactly when
\[
d\equiv1\pmod3.
\]

Next consider \(\gcd(A,E)\). If \(d\) is even, then \(d-1\) is odd and
\[
E=\frac{d-2}{2}(d^2-9).
\]
The first factor is coprime to \(d-1\), while
\[
d^2-9\equiv-8\pmod{d-1}.
\]
Since \(d-1\) is odd, the gcd is \(1\).

If \(d\) is odd, then
\[
E=(d-2)\frac{d^2-9}{2}.
\]
Again \(d-2\) is coprime to \(d-1\). No odd prime can divide both \(d-1\) and \((d^2-9)/2\), because modulo \(d-1\) the numerator is \(-8\). The common factor is therefore purely dyadic. A direct valuation check gives
\[
\gcd(A,E)=4
\]
when \(d\equiv1\pmod4\), and
\[
\gcd(A,E)=2
\]
when \(d\equiv3\pmod4\).

Finally, both \(C\) and \(E\) contain the factor \(d-2\). If \(d\) is even, write
\[
E=\frac{d-2}{2}(d^2-9),
\]
so
\[
\gcd(C,E)
=
\frac{d-2}{2}\gcd(6,d^2-9).
\]
Here \(d^2-9\) is odd, and it is divisible by \(3\) exactly when \(3\mid d\). If \(d\) is odd, then
\[
\gcd(C,E)
=
(d-2)\gcd\left(3,\frac{d^2-9}{2}\right),
\]
and the last gcd is again \(3\) exactly when \(3\mid d\). This proves the third pairwise formula.

For the triple gcd, the first pair has normalized gcd at most \(3\). If
\[
d\not\equiv1\pmod3,
\]
that normalized gcd is already \(1\). If
\[
d\equiv1\pmod3,
\]
then
\[
E=\frac{(d-2)(d^2-9)}2\not\equiv0\pmod3,
\]
so the possible extra factor \(3\) does not divide the third normalized invariant. Therefore
\[
\gcd(A,C,E)=1,
\]
and hence
\[
\gcd(D,F,B)=d.
\]

## Verification
The bundled exact checker evaluates the three classical formulas for every
\[
4\le d\le10000
\]
and verifies the triple gcd and all three pairwise formulas by direct integer arithmetic.

It also checks the standard calibrations
\[
(D,F,B)=(12,24,28)
\]
for a general quartic and
\[
(D,F,B)=(20,45,120)
\]
for a general quintic.

These finite checks are regression evidence only. The infinite statement follows from the elementary gcd reductions above once the classical Pluecker formulas are fixed.

## Relationship to prior work
Classical Pluecker theory identifies the degree of the dual curve and the node and cusp counts of the dual with the dual degree, bitangent count, and inflection count of the original curve. Leung's archival work gives a modern conormal interpretation of the Pluecker formula for projective duality. More recent work on Pluecker formulas for curves with prescribed Newton polygon explicitly takes the classical smooth plane-curve bitangent and inflection formulas as its starting case and generalizes them.

The result here concerns a different invariant of that classical enumerative package: the exact common-divisor lattice of its three principal counts. Searches using gcd, common-divisor, primitive-triple, dual-degree, bitangent, inflection, and Pluecker formulations did not locate the triple identity or the pairwise residue laws above.

The formulas for \(D\), \(F\), and \(B\) themselves are prior work. The contribution is the simultaneous arithmetic classification of how their prime factors can overlap.

## Limitations
The statement is about a general smooth plane curve. For special smooth curves, hyperflexes or other non-generic tangencies can change the number of distinct bitangent or inflection lines even though the corresponding intersection-theoretic Pluecker classes persist with multiplicity.

The result classifies gcds among the three basic dual-line counts only. It does not address higher-order generalized Pluecker numbers.

Because the arithmetic proof is short after the classical formulas are written down, an unindexed historical source could contain the same gcd classification.

## References
Naichung Conan Leung, *A general Plucker formula*, arXiv:math/0111179, first submitted 15 November 2001.

Aliaksandr Yuran, *Plucker Formulas for Plane Algebraic Curves with a Given Newton Polygon*, arXiv:2204.04626, first submitted 10 April 2022.
