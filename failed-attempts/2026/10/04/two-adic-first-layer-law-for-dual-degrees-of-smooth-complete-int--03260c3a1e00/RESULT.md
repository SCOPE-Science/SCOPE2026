# Two-adic first-layer law for dual degrees of smooth complete intersections
## Finding
Let
\[
X\subset\mathbb P^{n+c}_{\mathbb C}
\]
be a smooth nonlinear complete intersection of dimension \(n\ge1\), codimension \(c\ge1\), and multidegree
\[
(d_1,\ldots,d_c),
\qquad d_i\ge2.
\]
Put
\[
D=\prod_i d_i,
\qquad
x_i=d_i-1,
\]
and write \(h_n(x_1,\ldots,x_c)\) for the complete homogeneous symmetric polynomial of degree \(n\). Then the projective dual \(X^\vee\) is a hypersurface and
\[
\deg X^\vee
=
D\,h_n(d_1-1,\ldots,d_c-1).
\]

Let \(e\) be the number of even defining degrees and set
\[
A=\sum_i \nu_2(d_i).
\]
If \(e>0\), then
\[
\nu_2(\deg X^\vee)=A
\]
if and only if
\[
n\mathbin{\&}(e-1)=0.
\]
If this bitwise condition fails, then
\[
\nu_2(\deg X^\vee)\ge A+1.
\]

If \(e=0\), so every defining degree is odd, let \(f\) be the number of indices satisfying
\[
d_i\equiv3\pmod4.
\]
Then
\[
\nu_2(\deg X^\vee)=n
\]
if and only if
\[
f>0
\quad\text{and}\quad
n\mathbin{\&}(f-1)=0.
\]
Otherwise
\[
\nu_2(\deg X^\vee)\ge n+1.
\]

Every positive-dimensional smooth nonlinear complete intersection therefore has even projective-dual degree.

If \(n\ge2\), then
\[
\deg X^\vee\equiv2\pmod4
\]
if and only if exactly one defining degree is congruent to \(2\pmod4\) and every other defining degree is odd.

For curves there is one additional way to have
\[
\deg X^\vee\equiv2\pmod4:
\]
all defining degrees are odd and an odd number of them are congruent to \(3\pmod4\).

For example, a complete-intersection surface of type \((2,3,3)\) has
\[
\deg X^\vee=306,
\]
whereas a surface of type \((3,3)\) has
\[
\deg X^\vee=108.
\]

## Assumptions and scope
The ground field is \(\mathbb C\). The variety is smooth, positive-dimensional, nonlinear, and a complete intersection in its given projective embedding.

The bitwise notation
\[
a\mathbin{\&}b=0
\]
means that the binary expansions of \(a\) and \(b\) have no common position occupied by a \(1\). Equivalently, adding \(a\) and \(b\) in base two produces no carry.

The theorem determines the first possible \(2\)-adic layer exactly. When the displayed equality criterion fails, the theorem asserts at least one additional factor of \(2\), but does not give the entire higher \(2\)-adic valuation.

## Proof
Kleiman's generalized Plücker formula identifies the dual degree of a smooth nondefective projective variety with the top Segre-class degree of the twisted conormal bundle. For a smooth complete intersection, the same duality section records that the nonlinear complete-intersection case is nondefective.

For the present \(X\), the conormal bundle is
\[
N^*_{X/\mathbb P^{n+c}}
=
\bigoplus_{i=1}^c\mathcal O_X(-d_i).
\]
After twisting by \(\mathcal O_X(1)\),
\[
E=
N^*_{X/\mathbb P^{n+c}}\otimes\mathcal O_X(1)
=
\bigoplus_{i=1}^c\mathcal O_X(1-d_i).
\]
Thus
\[
s(E)
=
\frac{1}{c(E)}
=
\prod_{i=1}^c
\frac{1}{1-(d_i-1)H},
\]
where \(H\) is the hyperplane class. The coefficient of \(H^n\) is
\[
h_n(d_1-1,\ldots,d_c-1),
\]
and
\[
\int_X H^n=D.
\]
Therefore
\[
\deg X^\vee
=
D\,h_n(d_1-1,\ldots,d_c-1).
\]

Now reduce the complete homogeneous polynomial modulo \(2\). Its generating function is
\[
\sum_{m\ge0}h_m(x_1,\ldots,x_c)t^m
=
\prod_{i=1}^c(1-x_it)^{-1}.
\]

Assume first that \(e>0\). Modulo \(2\), exactly the \(e\) indices with even \(d_i\) have odd \(x_i=d_i-1\). Hence
\[
\sum_{m\ge0}h_m(x_1,\ldots,x_c)t^m
\equiv
(1-t)^{-e}
\pmod2.
\]
Therefore
\[
h_n(x_1,\ldots,x_c)
\equiv
\binom{n+e-1}{n}
\pmod2.
\]
By Kummer's theorem, equivalently Lucas's theorem, this binomial coefficient is odd exactly when the binary addition of \(n\) and \(e-1\) has no carry, namely
\[
n\mathbin{\&}(e-1)=0.
\]
Since
\[
\nu_2(D)=A,
\]
the first valuation statement follows.

Assume next that \(e=0\). Then every \(d_i\) is odd, so write
\[
d_i-1=2y_i.
\]
Homogeneity gives
\[
h_n(d_1-1,\ldots,d_c-1)
=
2^n h_n(y_1,\ldots,y_c).
\]
Now \(y_i\) is odd exactly when
\[
d_i\equiv3\pmod4.
\]
If \(f\) denotes the number of such indices, then
\[
h_n(y_1,\ldots,y_c)
\equiv
\binom{n+f-1}{n}
\pmod2
\]
when \(f>0\), while it is even when \(f=0\). Applying Kummer--Lucas once more gives
\[
h_n(y_1,\ldots,y_c)\equiv1\pmod2
\]
exactly when
\[
f>0
\quad\text{and}\quad
n\mathbin{\&}(f-1)=0.
\]
Because \(D\) is odd in this case, this proves the second valuation statement.

The universal evenness follows immediately. For the mod-\(4\) classification in dimension at least two, the all-odd case already contributes at least \(2^n\), hence at least \(4\). If some degree is even, valuation one requires
\[
A=1,
\]
which means that there is exactly one even defining degree and it is congruent to \(2\pmod4\); with \(e=1\), the bitwise criterion is automatic. For curves, the all-odd case has valuation one precisely when \(f\) is odd, because
\[
1\mathbin{\&}(f-1)=0
\]
is equivalent to \(f-1\) being even.

## Verification
The bundled exact checker computes the complete homogeneous symmetric polynomial by integer dynamic programming and checks the full first-layer valuation theorem over a bounded family of dimensions, codimensions, and multidegrees.

It separately verifies the mod-\(4\) corollaries and the Kummer--Lucas parity criterion for the relevant binomial coefficients. These calculations are regression evidence only; the infinite theorem is supplied by the Segre-class formula and the exact generating-function reduction modulo \(2\).

## Relationship to prior work
Kleiman's *The Enumerative Theory of Singularities* develops the generalized Plücker formula for projective dual degree. In the inspected duality section he identifies the ramification/conormal construction, expresses the dual degree by the top Segre class, states that nonlinear complete intersections have hypersurface duals, and records a general parity theorem of Landman saying that the dual degree is even when the variety has odd dimension.

The present result proves evenness for complete intersections in every positive dimension, including even dimension, and determines the exact first \(2\)-adic layer by the binary carry pattern determined by the defining degrees.

The closest previously checked complete-intersection findings concern a fixed-sum extremum for dual degrees of bidegree threefolds and a collision classification for dual degrees of complete-intersection curves in projective three-space. Those statements use the same classical invariant in special families, but neither implies the valuation theorem, its bitwise criterion, or the mod-\(4\) classification here.

Claim-specific searches for parity, mod-\(4\), and \(2\)-adic valuation statements for dual degrees of smooth complete intersections did not locate a source stating this result.

## Limitations
The theorem only determines the first nontrivial \(2\)-adic layer. When its equality criterion fails, further valuation depends on more detailed residue information in the multidegree.

The result is stated over \(\mathbb C\). Positive characteristic requires care because the conormal-to-dual map can be inseparable and the numerical dual degree can differ from the characteristic-zero formula by inseparable factors.

The literature comparison cannot exclude an unindexed classical source containing the same arithmetic corollary.

## References
Steven L. Kleiman, *The Enumerative Theory of Singularities*, in *Real and Complex Singularities, Oslo 1976*, pp. 297--396, 1977. DOI: 10.1007/978-94-010-1289-8_10.

Kummer's theorem and Lucas's theorem are used in their standard binary form for binomial-coefficient parity.
