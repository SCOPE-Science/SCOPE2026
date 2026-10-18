# A sharp dual–primal degree crossover for Veronese varieties
## Finding
Let
\[
V_{n,e}=v_e(\mathbb P^n_{\mathbb C}),
\qquad
n\ge1,\quad e\ge2,
\]
be the \(e\)-uple Veronese variety. Write
\[
P_{n,e}=\deg V_{n,e}
\]
for its projective degree and
\[
Q_{n,e}=\deg V_{n,e}^{\vee}
\]
for the degree of its projective dual hypersurface.

The classical formulas are
\[
P_{n,e}=e^n
\]
and
\[
Q_{n,e}=(n+1)(e-1)^n.
\]

Define the real threshold
\[
T_n=
\frac{1}{1-(n+1)^{-1/n}}.
\]
Then
\[
\boxed{Q_{n,e}<P_{n,e}\iff e<T_n}
\]
and
\[
\boxed{Q_{n,e}>P_{n,e}\iff e>T_n}.
\]

Equality occurs only for the conic:
\[
\boxed{Q_{n,e}=P_{n,e}\iff(n,e)=(1,2)}.
\]

Consequently, for every
\[
n\ge2,
\]
the least integer Veronese order at which the dual degree overtakes the primal degree is
\[
\boxed{
e_n=\left\lceil
\frac{1}{1-(n+1)^{-1/n}}
\right\rceil.
}
\]

The threshold has the asymptotic expansion
\[
\boxed{
T_n
=
\frac{n}{\log(n+1)}
+\frac12
+\frac{\log(n+1)}{12n}
+
O\!\left(
\frac{\log^3(n+1)}{n^3}
\right)
}.
\]
In particular,
\[
e_n=\frac{n}{\log n}+O(1).
\]

Thus the dual discriminant degree is initially smaller than the degree of the Veronese image in high dimension, but it overtakes it at a sharply determined embedding order of size \(n/\log n\).

## Assumptions and scope
The base field is \(\mathbb C\). The Veronese embedding is defined by the complete linear system
\[
|\mathcal O_{\mathbb P^n}(e)|.
\]

The projective degree of \(V_{n,e}\) is
\[
e^n,
\]
because the pullback of the ambient hyperplane class is \(eH\) on \(\mathbb P^n\).

The projective dual of \(V_{n,e}\) is the discriminant hypersurface parametrizing singular degree-\(e\) hypersurfaces in \(\mathbb P^n\). Boole's formula gives its degree
\[
(n+1)(e-1)^n.
\]

The statement concerns only these two canonical projective degrees. It does not compare higher polar or higher Gauss-map image degrees.

## Proof
Taking the quotient of the dual and primal degrees gives
\[
\frac{Q_{n,e}}{P_{n,e}}
=
(n+1)\left(1-\frac1e\right)^n.
\]
For fixed \(n\), this is strictly increasing in \(e\).

The equality
\[
Q_{n,e}=P_{n,e}
\]
is equivalent to
\[
(n+1)\left(1-\frac1e\right)^n=1.
\]
Solving over the positive real variable \(e\) gives
\[
e=T_n
=
\frac{1}{1-(n+1)^{-1/n}}.
\]
Since the ratio is strictly increasing,
\[
e<T_n
\]
is equivalent to \(Q_{n,e}<P_{n,e}\), and
\[
e>T_n
\]
is equivalent to \(Q_{n,e}>P_{n,e}\).

It remains to classify integral equality. From
\[
(n+1)(e-1)^n=e^n
\]
and
\[
\gcd(e,e-1)=1,
\]
we get
\[
(e-1)^n\mid e^n.
\]
Hence
\[
e-1=1,
\]
so \(e=2\). The equality then becomes
\[
n+1=2^n.
\]
This has the unique positive solution
\[
n=1,
\]
because
\[
2^n>n+1
\]
for all \(n\ge2\). Therefore the conic is the unique integral equality case.

For \(n\ge2\), \(T_n\) is not an integer. Hence the least integer \(e\) with \(Q_{n,e}>P_{n,e}\) is
\[
e_n=\lceil T_n\rceil.
\]

For the asymptotic expansion, put
\[
x=\frac{\log(n+1)}{n}.
\]
Then
\[
(n+1)^{-1/n}=e^{-x}
\]
and
\[
T_n=\frac{1}{1-e^{-x}}.
\]
The standard expansion at \(x=0\) is
\[
\frac{1}{1-e^{-x}}
=
\frac1x+\frac12+\frac{x}{12}+O(x^3).
\]
Substituting
\[
x=\frac{\log(n+1)}{n}
\]
gives the asserted formula.

## Verification
The bundled checker evaluates
\[
P_{n,e}=e^n
\]
and
\[
Q_{n,e}=(n+1)(e-1)^n
\]
for all
\[
1\le n\le300,
\qquad
2\le e\le300.
\]

It verifies that equality occurs only at \((1,2)\), that the sign changes exactly once for each fixed \(n\), and that for \(n\ge2\) the first integer with \(Q_{n,e}>P_{n,e}\) agrees with the ceiling of the real threshold computed at high precision.

It also checks exact monotonicity by the integer identity
\[
\frac{Q_{n,e+1}/P_{n,e+1}}{Q_{n,e}/P_{n,e}}
=
\left(\frac{e^2}{e^2-1}\right)^n>1.
\]

These finite computations are regression evidence only. The all-parameter classification is proved symbolically above.

## Relationship to prior work
Boole's classical formula identifies the discriminant degree
\[
(n+1)(e-1)^n,
\]
and modern treatments recover it as the degree of the projective dual of the Veronese variety. Benoist records the formula as the hypersurface case of his discriminant-degree theory, while Kaji explicitly treats Boole's formula as the ordinary-dual case of higher Gauss maps of Veronese varieties.

The primal degree
\[
e^n
\]
is the standard intersection-theoretic degree of the Veronese embedding.

The result here compares those two canonical degrees uniformly in both the dimension and the embedding order. Targeted searches for a dual-versus-primal crossover, equality classification, and the exact threshold
\[
1/(1-(n+1)^{-1/n})
\]
did not locate an equivalent statement. Nearby literature concerns higher Gauss-map degrees, polar-degree divisibility, or fixed-dimensional toric dual-degree excess rather than this two-parameter crossover.

## Limitations
The theorem compares only the primal projective degree and the ordinary projective-dual degree.

No statement is made about higher dual, polar, Euclidean-distance, or coisotropic degrees.

The crossover is an elementary consequence once the two classical closed formulas are juxtaposed. An older or unindexed source may contain the same comparison without using crossover terminology.

## References
Olivier Benoist, *Degrés d'homogénéité de l'ensemble des intersections complètes singulières*, arXiv:1009.0704, first submitted 3 September 2010; *Annales de l'Institut Fourier* 62 (2012), 1189--1214, DOI 10.5802/aif.2720.

Hajime Kaji, *Higher Gauss Maps of Veronese Varieties---a generalization of Boole's formula and degree bounds for higher Gauss map images---*, arXiv:1509.04935, first submitted 16 September 2015.
