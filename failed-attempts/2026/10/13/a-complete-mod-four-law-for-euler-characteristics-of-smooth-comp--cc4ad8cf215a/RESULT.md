# A complete mod-four law for Euler characteristics of smooth complete intersections
## Finding
Let
\[
X\subset\mathbb P^{n+c}_{\mathbb C}
\]
be a smooth complete intersection of complex dimension
\[
n\ge1,
\]
codimension
\[
c\ge1,
\]
and multidegree
\[
(d_1,\ldots,d_c),
\qquad
d_i\ge2.
\]
Put
\[
D=\prod_{i=1}^c d_i
\]
and let
\[
f=\#\{\,i:d_i\equiv3\pmod4\,\}.
\]

The topological Euler characteristic is
\[
\chi_{\mathrm{top}}(X)
=
D[t^n]\frac{(1+t)^{n+c+1}}{\prod_i(1+d_i t)}.
\]

Its residue modulo four is completely determined as follows.

If
\[
4\mid D,
\]
then
\[
\boxed{\chi_{\mathrm{top}}(X)\equiv0\pmod4.}
\]

Suppose exactly one defining degree is even. If that degree is divisible by \(4\), the preceding case applies. If it is congruent to \(2\) modulo \(4\), while every other defining degree is odd, then
\[
\boxed{
\chi_{\mathrm{top}}(X)\equiv
\begin{cases}
2\pmod4,&n\equiv0,1\pmod4,\\
0\pmod4,&n\equiv2,3\pmod4.
\end{cases}}
\]

Finally, if every defining degree is odd, then
\[
\boxed{
\chi_{\mathrm{top}}(X)
\equiv
(-1)^f\bigl(n+1+2fn\bigr)
\pmod4.
}
\]

Consequently,
\[
\boxed{
\chi_{\mathrm{top}}(X)\ \text{is odd}
\iff
n\ \text{is even and every }d_i\text{ is odd}.
}
\]

The exact first positive two-adic layer is also explicit:
\[
\boxed{
\nu_2(\chi_{\mathrm{top}}(X))=1
}
\]
precisely in either of the following disjoint situations:

\[
\begin{aligned}
&\text{exactly one }d_i\equiv2\pmod4,\ \text{all other }d_j\text{ odd, and }n\equiv0,1\pmod4;\\
&\text{all }d_i\text{ odd},\ n\text{ odd},\ \text{and }\frac{n+1}{2}+f\text{ is odd}.
\end{aligned}
\]

All remaining even cases have Euler characteristic divisible by \(4\).

## Assumptions and scope
The base field is \(\mathbb C\), and \(X\) is smooth and projective. Linear defining equations are omitted, so every defining degree is at least \(2\).

The result concerns only the ordinary topological Euler characteristic. It does not determine higher two-adic valuations once divisibility by \(4\) begins.

The characteristic-class input is the standard complete-intersection tangent-bundle identity
\[
[T_X]
=
[T_{\mathbb P^{n+c}}|_X]
-
\sum_i[\mathcal O_X(d_i)]
\]
in \(K\)-theory, equivalently
\[
c(T_X)
=
\frac{(1+H)^{n+c+1}}{\prod_i(1+d_iH)}.
\]

## Proof
By Gauss--Bonnet,
\[
\chi_{\mathrm{top}}(X)
=
\int_Xc_n(T_X).
\]
Since
\[
[X]=D H^c
\]
in the Chow ring of \(\mathbb P^{n+c}\), the tangent-bundle formula gives
\[
\chi_{\mathrm{top}}(X)
=
D[t^n]\frac{(1+t)^{n+c+1}}{\prod_i(1+d_it)}.
\]
Write the coefficient as
\[
C=[t^n]\frac{(1+t)^{n+c+1}}{\prod_i(1+d_it)}.
\]

If \(4\mid D\), then \(4\mid\chi_{\mathrm{top}}(X)\) immediately.

Now suppose exactly one defining degree \(e\) is even and
\[
e\equiv2\pmod4,
\]
while all other degrees are odd. Since \(D\equiv2\pmod4\), it is enough to determine \(C\) modulo \(2\). Modulo \(2\), the even-degree denominator contributes \(1\), while every odd-degree factor \(1+d_it\) reduces to \(1+t\). There are \(c-1\) odd degrees, hence
\[
C
\equiv
[t^n](1+t)^{n+c+1-(c-1)}
=
[t^n](1+t)^{n+2}
=
\binom{n+2}{2}
\pmod2.
\]
The binomial coefficient is odd exactly when
\[
n\equiv0,1\pmod4.
\]
This proves the single-even branch.

It remains to treat the all-odd case. Split the degrees according to their residues modulo \(4\). If
\[
q=c-f
\]
of them are \(1\pmod4\), then modulo \(4\)
\[
\prod_i(1+d_it)
\equiv
(1+t)^q(1-t)^f.
\]
Therefore
\[
C
\equiv
[t^n](1+t)^{n+1}
\left(\frac{1+t}{1-t}\right)^f
\pmod4.
\]
But
\[
\frac{1+t}{1-t}
=
1+\frac{2t}{1-t},
\]
so
\[
\left(\frac{1+t}{1-t}\right)^f
\equiv
1+\frac{2ft}{1-t}
\pmod4.
\]
Hence
\[
C
\equiv
(n+1)
+
2f[t^{n-1}]\frac{(1+t)^{n+1}}{1-t}
\pmod4.
\]
The remaining coefficient is
\[
\sum_{k=0}^{n-1}\binom{n+1}{k}
=
2^{n+1}-n-2.
\]
For every \(n\ge1\), this has the same parity as \(n\). Thus
\[
C\equiv n+1+2fn\pmod4.
\]

Because every \(d_i\) is odd,
\[
D\equiv(-1)^f\pmod4.
\]
Multiplying gives
\[
\chi_{\mathrm{top}}(X)
\equiv
(-1)^f(n+1+2fn)
\pmod4.
\]

If \(n\) is even, the right-hand side is odd. If \(n\) is odd, it is either \(0\) or \(2\) modulo \(4\); it equals \(2\) exactly when
\[
\frac{n+1}{2}+f
\]
is odd. This proves every stated classification.

## Verification
The bundled checker computes the Euler characteristic independently by truncated multiplication of the Chern-series
\[
(1+t)^{n+c+1}\prod_i(1+d_it)^{-1}.
\]

It enumerates all unordered multidegrees with
\[
1\le n\le12,\qquad
1\le c\le4,\qquad
2\le d_i\le9,
\]
and compares the exact integer Euler characteristic with every branch of the mod-four theorem.

It separately checks the oddness and exact-\(\nu_2=1\) criteria.

These finite computations are regression evidence only. The theorem for all dimensions, codimensions, and multidegrees is the symbolic congruence argument above.

## Relationship to prior work
Characteristic-class treatments of global complete intersections identify their virtual tangent bundle as the ambient tangent bundle minus the normal bundle; for smooth complete intersections, virtual and ordinary characteristic classes agree. Classical literature gives explicit formulas and generating functions for complete-intersection Euler characteristics.

The present statement extracts the complete residue modulo \(4\) for arbitrary multidegree. The key simplification is that modulo \(4\), all odd defining degrees collapse to the two signs \(1\) and \(-1\), while the single-even case reduces to one binomial coefficient modulo \(2\).

A modern full-text treatment of quadratic Euler characteristics of same-degree complete intersections refines the ordinary Euler characteristic in a different direction. The inspected text does not state a mod-four, parity, or two-adic classification.

Targeted searches for complete-intersection Euler characteristics together with parity, mod-four, divisibility, and two-adic terminology did not locate the all-multidegree theorem above.

## Limitations
No claim is made about \(\nu_2(\chi_{\mathrm{top}}(X))\) once it is at least \(2\).

The argument uses smoothness essentially through the tangent bundle and Gauss--Bonnet formula. Singular complete intersections require correction terms.

The arithmetic reduction is elementary after the classical Euler formula is known. Older literature devoted specifically to Euler characteristics of complete intersections is a residual novelty risk because some full texts were not available in searchable form during this comparison.

## References
Laurentiu Maxim, Morihiko Saito, and Jörg Schürmann, *Hirzebruch-Milnor Classes of Complete Intersections*, arXiv:1205.6447, first submitted 29 May 2012; *Advances in Mathematics* 241 (2013), 220--245.

John Ewing and Suresh Moolgavkar, *Euler Characteristics of Complete Intersections*, *Proceedings of the American Mathematical Society* 56 (1976), 390--391.

Vicente Navarro Aznar, *On the Chern Classes and the Euler Characteristic for Nonsingular Complete Intersections*, *Proceedings of the American Mathematical Society* 78 (1980), 143--148.

Anna M. Viergever, *The Quadratic Euler Characteristic of a Smooth Projective Same-Degree Complete Intersection*, arXiv:2306.16155, first submitted 28 June 2023.
