# A Catalan and dyadic formula for the Gauss degree of a general Prym theta divisor
## Finding
Let
\[
g\ge3,
\]
and let \(\Xi\) be the theta divisor of a general Prym variety of dimension \(g-1\). Let
\[
\gamma:\Xi\dashrightarrow\mathbb P^{g-2}
\]
be its Gauss map.

Then
\[
\boxed{
\deg\gamma
=
2^{g-3}\bigl(C_{g-2}+1\bigr)
},
\]
where
\[
C_m=\frac{1}{m+1}\binom{2m}{m}
\]
is the \(m\)-th Catalan number.

Equivalently, if \(D(g)\) denotes the degree of the projective variety of quadrics of rank at most \(3\) in \(\mathbb P^{g-1}\), then
\[
\boxed{
D(g)=2^{g-3}C_{g-2}.
}
\]

The exact two-adic valuation of the Prym Gauss degree is
\[
\boxed{
\nu_2(\deg\gamma)
=
g-3+
\mathbf 1_{\{g-1\text{ is a power of }2\}}.
}
\]

Hence the normalized degree
\[
\frac{\deg\gamma}{2^{g-3}}
=
C_{g-2}+1
\]
is even exactly in genera
\[
g=2^r+1,
\]
and in those genera it is exactly
\[
2\pmod4.
\]
For every other \(g\), the normalized degree is odd.

The first values are
\[
2,\ 6,\ 24,\ 120,\ 688,\ 4256,\ 27520,\ldots
\]
for \(g=3,4,\ldots,9\).

## Assumptions and scope
The base field is \(\mathbb C\). The Prym variety and its theta divisor are general in the sense of the classical generic Prym construction used in the cited source.

The Gauss map is the rational map given at a smooth point of \(\Xi\) by its translated tangent hyperplane. Its degree is the number of points in a general fiber.

The published geometric theorem used here is
\[
\deg\gamma=D(g)+2^{g-3},
\]
where \(D(g)\) is the degree of the rank-at-most-\(3\) symmetric determinantal locus.

The new statement simplifies the classical product for \(D(g)\) to a Catalan number and extracts the complete two-primary content of the Gauss degree.

## Proof
The classical product recorded with the Prym Gauss-degree theorem is
\[
D(g)
=
\prod_{j=0}^{g-4}
\frac{
\binom{g+j}{g-3-j}
}{
\binom{2g-7-2j}{g-3-j}
}.
\]
Reindex with
\[
k=g-3-j.
\]
A factorial expansion gives
\[
D(g)
=
\prod_{k=1}^{g-3}
\frac{(2g-3-k)!(k-1)!}
{(2g-3-2k)!(2k-1)!}.
\]

Direct cancellation in the quotient of two consecutive products yields
\[
\frac{D(g+1)}{D(g)}
=
\frac{4(2g-3)}{g}.
\]
Also
\[
D(3)=1.
\]

Now define
\[
A(g)=2^{g-3}C_{g-2}.
\]
The Catalan recurrence gives
\[
\frac{A(g+1)}{A(g)}
=
2\frac{C_{g-1}}{C_{g-2}}
=
\frac{4(2g-3)}{g},
\]
and
\[
A(3)=1.
\]
Therefore
\[
D(g)=2^{g-3}C_{g-2}
\]
for all \(g\ge3\). Substitution into the published Prym formula gives
\[
\deg\gamma
=
2^{g-3}(C_{g-2}+1).
\]

It remains to analyze the factor \(C_{g-2}+1\).

For every \(m\ge0\), Legendre's factorial formula gives
\[
\nu_2(C_m)
=
s_2(m+1)-1,
\]
where \(s_2\) is the binary digit sum. Hence \(C_m\) is odd exactly when
\[
m+1
\]
is a power of \(2\).

If \(m+1\) is not a power of \(2\), then \(C_m\) is even, so
\[
C_m+1
\]
is odd.

Now let
\[
m=2^r-1.
\]
A short odd-factorial induction gives
\[
C_{2^r-1}\equiv1\pmod4.
\]
For completeness, let \(\operatorname{odd}(N!)\) denote \(N!\) after removal of all factors of \(2\). Splitting \((2N)!\) into its even and odd factors gives
\[
\operatorname{odd}((2N)!)
=
\operatorname{odd}(N!)
\prod_{j=1}^{N}(2j-1).
\]
Applying this with powers of \(2\), and noting that translation by \(2^{r-1}\) changes each odd factor by a multiple of \(4\) for \(r\ge2\), reduces
\[
C_{2^r-1}\pmod4
\]
to
\[
C_{2^{r-1}-1}\pmod4.
\]
The base value is
\[
C_1=1.
\]
Thus
\[
C_{2^r-1}+1\equiv2\pmod4.
\]

Taking
\[
m=g-2
\]
proves
\[
\nu_2(C_{g-2}+1)
=
\mathbf 1_{\{g-1\text{ is a power of }2\}},
\]
and therefore the stated exact valuation of \(\deg\gamma\).

## Verification
The bundled checker reconstructs \(D(g)\) directly from the classical binomial product and independently compares it with
\[
2^{g-3}C_{g-2}
\]
for every
\[
3\le g\le300.
\]

It then computes the Prym Gauss degree from both formulas and checks the exact two-adic valuation through the same range. It separately verifies
\[
C_{2^r-1}\equiv1\pmod4
\]
for every power-of-two index in the test range.

These finite computations are regression evidence only. The all-genus theorem is proved by the product recurrence, Legendre's formula, and the odd-factorial congruence above.

## Relationship to prior work
Verra proves that the Gauss degree of a general Prym theta divisor is
\[
D(g)+2^{g-3}
\]
and records a classical product for \(D(g)\), the degree of the rank-at-most-\(3\) quadric locus.

Codogni, Grushevsky, and Sernesi later study the stratification of principally polarized abelian varieties by Gauss-map degree and explicitly recall Verra's formula for generic Pryms.

The inspected full texts state the product and the Prym Gauss-degree formula, but do not rewrite \(D(g)\) as a power of two times a Catalan number and do not state the resulting exact two-adic law. Targeted searches using Prym, theta, Gauss degree, rank-three quadrics, Catalan numbers, and two-adic valuation likewise did not locate this reformulation.

## Limitations
The theorem concerns the generic Prym theta divisor. It does not classify Gauss degrees on special Prym loci or degenerations.

Only the ordinary degree of the Gauss map is treated. No statement is made about monodromy, ramification, or finer geometry of its fibers.

The Catalan identity is an elementary simplification of a classical symmetric-determinantal degree product. An older or unindexed source may contain that product simplification even if the Prym two-adic consequence is not stated there.

## References
Alessandro Verra, *The degree of the Gauss map for a general Prym Theta Divisor*, arXiv:math/9809067, first submitted 14 September 1998; *Journal of Algebraic Geometry* 10 (2001), 215--246.

Giulio Codogni, Samuel Grushevsky, and Edoardo Sernesi, *The degree of the Gauss map of the theta divisor*, arXiv:1608.02686, first submitted 9 August 2016; *Algebra & Number Theory* 11 (2017), 983--1001.
