# Equal-product classification of four partially shared derivative values

## Finding

Let
\[
a,b,c,d\in\mathbb C^*
\]
be four distinct complex numbers. There exists a nonconstant meromorphic function
\[
f:\mathbb C\longrightarrow\widehat{\mathbb C},
\qquad
f\not\equiv f',
\]
such that
\[
f(z)=v\Longrightarrow f'(z)=v
\]
for every
\[
v\in\{a,b,c,d\},
\]
if and only if the four values can be partitioned into two pairs having the same product.

More explicitly, after relabeling the values so that
\[
a,b
\]
are the two Picard exceptional values forced by the nontrivial four-value classification, the remaining values satisfy
\[
ab=cd.
\]

Conversely, every four distinct nonzero values satisfying
\[
ab=cd
\]
are realized. Put
\[
\kappa=\frac{1}{c+d-a-b}.
\]
Then for every
\[
\eta\in\mathbb C^*
\]
the function
\[
q(z)=\eta e^{\kappa(a-b)z},
\qquad
f(z)=\frac{a-bq(z)}{1-q(z)}
\]
partially shares exactly
\[
a,b,c,d
\]
among finite values with its derivative.

Thus the nontrivial four-value problem admits a parameter-free value-space classification: admissible quadruples are exactly those with an equal-product pairing.

## Assumptions and scope

A finite value \(v\) is partially shared by \(f\) with \(f'\) when
\[
f(z)=v\Longrightarrow f'(z)=v
\]
for every
\[
z\in\mathbb C.
\]

The four values are assumed distinct and nonzero. The nonzero condition is necessary for a nontrivial realization by Theorem 2.1 of Sauer and Schweizer: if one of four partially shared finite values is zero, then
\[
f\equiv f'.
\]

The statement classifies value quadruples only for the first derivative and for meromorphic functions on the complex plane. It does not address three-value partial sharing, higher derivatives, shifts, or small functions.

## Proof

Assume first that
\[
f\not\equiv f'
\]
partially shares four distinct finite values.

The source theorem implies that all four values are nonzero and that
\[
f(z)=M(e^{\lambda z})
\]
for a Möbius transformation \(M\). More importantly for the present argument, the proof of the theorem shows that two of the four partially shared values, say
\[
a,b,
\]
are the two Picard exceptional values of \(f\), and derives a nonzero constant
\[
\kappa
\]
such that
\[
f'=\kappa(f-a)(f-b).
\]

The other two values
\[
c,d
\]
are not exceptional and hence are attained. At any point where
\[
f=c,
\]
partial sharing gives
\[
f'=c.
\]
Therefore
\[
\kappa(c-a)(c-b)=c.
\]
Similarly,
\[
\kappa(d-a)(d-b)=d.
\]
Hence \(c,d\) are the two roots of
\[
\kappa(y-a)(y-b)-y=0.
\]
The constant term and leading coefficient of this quadratic are
\[
\kappa ab
\quad\text{and}\quad
\kappa,
\]
so Vieta's formula gives
\[
cd=ab.
\]

This proves necessity.

For sufficiency, suppose
\[
a,b,c,d\in\mathbb C^*
\]
are distinct and
\[
ab=cd.
\]
If
\[
c+d=a+b,
\]
then the two monic quadratics with roots \(a,b\) and \(c,d\) would have the same sum and product, forcing
\[
\{a,b\}=\{c,d\},
\]
contrary to distinctness. Thus
\[
\kappa=\frac{1}{c+d-a-b}
\]
is well defined and nonzero.

Fix
\[
\eta\in\mathbb C^*
\]
and define
\[
q(z)=\eta e^{\kappa(a-b)z},
\qquad
f(z)=\frac{a-bq(z)}{1-q(z)}.
\]
Since
\[
q'(z)=\kappa(a-b)q(z),
\]
direct differentiation gives
\[
f'
=
\kappa\frac{(a-b)^2q}{(1-q)^2}.
\]
Also,
\[
f-a=\frac{(a-b)q}{1-q},
\qquad
f-b=\frac{a-b}{1-q}.
\]
Consequently
\[
f'=\kappa(f-a)(f-b).
\]

Because
\[
q(\mathbb C)=\mathbb C^*,
\]
the Möbius expression for \(f\) omits exactly
\[
a,b.
\]
Thus \(a,b\) are partially shared vacuously, while every other finite value is attained.

For an attained finite value \(y\), the derivative is constant on its full fiber:
\[
f(z)=y
\quad\Longrightarrow\quad
f'(z)=\kappa(y-a)(y-b).
\]
Therefore \(y\) is partially shared exactly when
\[
\kappa(y-a)(y-b)=y.
\]
Using
\[
\frac1\kappa=c+d-a-b
\]
and
\[
ab=cd,
\]
we obtain the polynomial identity
\[
\kappa(y-a)(y-b)-y
=
\kappa(y-c)(y-d).
\]
Its only roots are
\[
c,d.
\]
Hence the finite partially shared values are exactly
\[
a,b,c,d.
\]

The function has poles because
\[
q(z)=1
\]
has solutions, so it cannot satisfy
\[
f\equiv f'.
\]
This completes the converse and the classification.

## Verification

The open primary paper was inspected through its definition of partial sharing, Theorem 2.1, Example 2.2, and the proof of the four-value theorem. The proof explicitly identifies two of the four values as Picard exceptional and derives the Riccati equation
\[
f'=\kappa(f-a)(f-b).
\]

The necessity calculation is then an exact Vieta argument.

The converse was independently reconstructed rather than inferred from a parameter count. The explicit function
\[
f(z)=\frac{a-b\eta e^{\kappa(a-b)z}}
{1-\eta e^{\kappa(a-b)z}}
\]
was differentiated symbolically, giving
\[
f'=\kappa(f-a)(f-b).
\]
The identity
\[
\kappa(y-a)(y-b)-y
=
\kappa(y-c)(y-d)
\]
was checked algebraically from
\[
ab=cd
\]
and
\[
1/\kappa=c+d-a-b.
\]

No numerical experiment, finite search, or unproved completeness assumption is used.

## Relationship to prior work

Sauer and Schweizer classify the nontrivial meromorphic functions that partially share four finite values with their derivative. Their theorem gives the form
\[
M(e^{\lambda z}),
\]
and their proof derives the two exceptional values and the Riccati equation used here. Their Example 2.2 describes how the remaining two partially shared values arise from the zeros of
\[
\lambda wM'(w)-M(w).
\]

The source does not state the parameter-free characterization of which four-point value sets are realizable, the equal-product invariant
\[
ab=cd,
\]
or the converse construction from an arbitrary equal-product quadruple.

Earlier work on values shared by \(f\) and \(f'\) chiefly concerns symmetric sharing, entire-function uniqueness, normality, or smaller numbers of shared values. The 2024 Sauer--Schweizer entire-function paper classifies a different two-value implication problem and does not imply the meromorphic four-value locus described here.

Targeted searches under product invariants, Picard-exceptional pairings, four partially shared values, and Möbius-exponential classifications did not locate an implication-equivalent statement.

## Limitations

The equal-product pairing may not be unique for a specially symmetric four-point set; different admissible pairings can therefore lead to different exceptional-pair realizations.

The classification concerns four distinct nonzero finite values. It does not resolve the more complicated three-value problem highlighted in the source.

The result is algebraic after the source's deep four-value classification is available; it does not replace the Nevanlinna-theoretic work needed to obtain that classification.

## References

1. A. Sauer and A. Schweizer, *Meromorphic functions that partially share values with their first derivative*, arXiv:2508.09548v1, 2025; Results in Mathematics 81 (2026), Article 66, DOI: 10.1007/s00025-026-02624-5.
2. A. Sauer and A. Schweizer, *A uniqueness problem concerning entire functions and their derivatives*, Computational Methods and Function Theory 24 (2024), 163--183; arXiv:2208.11341.
3. G. G. Gundersen, *Meromorphic functions that share finite values with their derivative*, Journal of Mathematical Analysis and Applications 75 (1980), 441--446.
4. E. Mues and N. Steinmetz, *Meromorphe Funktionen, die mit ihrer Ableitung Werte teilen*, Manuscripta Mathematica 29 (1979), 195--206.
