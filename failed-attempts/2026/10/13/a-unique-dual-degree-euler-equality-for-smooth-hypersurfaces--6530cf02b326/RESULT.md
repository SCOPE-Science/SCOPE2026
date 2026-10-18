# A unique dual-degree–Euler equality for smooth hypersurfaces
## Finding
Let
\[
X_d^n\subset\mathbb P^{n+1}_{\mathbb C}
\]
be a smooth hypersurface of complex dimension
\[
n\ge1
\]
and degree
\[
d\ge2.
\]
Let
\[
(X_d^n)^\vee
\]
denote its projective dual hypersurface. Then
\[
\boxed{
\deg((X_d^n)^\vee)=d(d-1)^n
}
\]
and
\[
\boxed{
\chi_{\mathrm{top}}(X_d^n)
=
\frac{(1-d)^{n+2}-1}{d}+n+2.
}
\]

These two canonical complexities admit a complete comparison:
\[
\boxed{
\deg((X_d^n)^\vee)
=
\left|\chi_{\mathrm{top}}(X_d^n)\right|
}
\]
if and only if
\[
(n,d)=(1,2).
\]
Thus the smooth plane conic is the unique equality case, with both sides equal to \(2\).

For quadrics of dimension at least two,
\[
\boxed{
\deg((X_2^n)^\vee)
<
\left|\chi_{\mathrm{top}}(X_2^n)\right|
\qquad(n\ge2).
}
\]
For every degree at least three,
\[
\boxed{
\deg((X_d^n)^\vee)
>
\left|\chi_{\mathrm{top}}(X_d^n)\right|
\qquad(d\ge3,\ n\ge1).
}
\]

## Assumptions and scope
The base field is \(\mathbb C\), the hypersurface is smooth, and the projective dual is taken in the dual projective space with its standard polarization.

The comparison uses the absolute value of the topological Euler characteristic because odd-dimensional hypersurfaces can have negative Euler characteristic.

The theorem concerns ordinary smooth projective hypersurfaces. Singular hypersurfaces require correction terms on both the dual-degree and Euler-characteristic sides.

## Proof
For a smooth degree-\(d\) hypersurface, the classical projective-duality class formula gives
\[
\deg((X_d^n)^\vee)=d(d-1)^n.
\]

For the Euler characteristic, the tangent-normal exact sequence gives
\[
c(TX_d^n)
=
\frac{(1+H)^{n+2}}{1+dH}.
\]
Gauss--Bonnet and
\[
\int_{X_d^n}H^n=d
\]
therefore give
\[
\chi_{\mathrm{top}}(X_d^n)
=
d[t^n]\frac{(1+t)^{n+2}}{1+dt}.
\]
Expanding and simplifying the binomial sum yields
\[
\chi_{\mathrm{top}}(X_d^n)
=
\frac{(1-d)^{n+2}-1}{d}+n+2.
\]

Set
\[
q=d-1.
\]
Then
\[
\deg((X_d^n)^\vee)=(q+1)q^n.
\]

Assume first
\[
q\ge2,
\]
equivalently \(d\ge3\).

If \(n\) is even, then
\[
\chi_{\mathrm{top}}(X_d^n)
=
\frac{q^{n+2}-1}{q+1}+n+2>0.
\]
Multiplying the difference by \(q+1\) gives
\[
(q+1)\left(
\deg((X_d^n)^\vee)-\chi_{\mathrm{top}}(X_d^n)
\right)
=
q^n(2q+1)+1-(n+2)(q+1).
\]
Since
\[
q^n\ge2^n\ge n+1,
\]
the right-hand side is at least
\[
(n+1)(2q+1)+1-(n+2)(q+1)
=
nq>0.
\]
Hence the dual degree is larger.

If \(n\) is odd, then
\[
\chi_{\mathrm{top}}(X_d^n)
=
-\frac{q^{n+2}+1}{q+1}+n+2\le0,
\]
with equality only at
\[
(n,q)=(1,2).
\]
Thus
\[
\left|\chi_{\mathrm{top}}(X_d^n)\right|
=
\frac{q^{n+2}+1}{q+1}-(n+2),
\]
and
\[
(q+1)\left(
\deg((X_d^n)^\vee)-|\chi_{\mathrm{top}}(X_d^n)|
\right)
=
q^n(2q+1)-1+(n+2)(q+1)>0.
\]
So the dual degree is again strictly larger.

It remains to take
\[
q=1,
\]
that is \(d=2\). Then
\[
\deg((X_2^n)^\vee)=2.
\]
The Euler formula becomes
\[
\chi_{\mathrm{top}}(X_2^n)
=
\begin{cases}
n+2,&n\text{ even},\\
n+1,&n\text{ odd}.
\end{cases}
\]
Therefore equality occurs only at
\[
n=1,
\]
and strict reverse inequality holds for every \(n\ge2\).

This proves the complete classification.

## Verification
The bundled checker computes the Euler characteristic in two independent exact ways:

\[
\chi_{\mathrm{closed}}
=
\frac{(1-d)^{n+2}-1}{d}+n+2,
\]
and
\[
\chi_{\mathrm{Chern}}
=
d\sum_{j=0}^{n}
\binom{n+2}{j}(-d)^{n-j}.
\]

It verifies equality of these formulas, checks the classical dual-degree expression
\[
d(d-1)^n,
\]
and tests the complete comparison over
\[
1\le n\le100,
\qquad
2\le d\le100.
\]

Finite computation is regression evidence only. The all-parameter theorem follows from the symbolic inequalities in the proof.

## Relationship to prior work
Classical projective duality expresses the degree of the dual of a smooth hypersurface in terms of its Chern data; modern Chern--Mather treatments recover this as the smooth case of general duality formulas. Independently, the tangent-normal sequence gives the standard Euler-characteristic formula for smooth projective hypersurfaces.

The comparison made here is the sharp global statement obtained by placing those formulas against one another. Targeted searches for smooth hypersurface dual degree together with Euler characteristic, absolute Euler characteristic, equality, and crossover language did not locate this complete classification.

The closest indexed literature treats dual degrees of complete intersections, arithmetic of dual degrees, or Euler characteristics separately rather than the exact ordering of these two invariants.

## Limitations
The result concerns smooth hypersurfaces and ordinary topological Euler characteristic. It does not extend verbatim to singular hypersurfaces.

Absolute Euler characteristic is used only for numerical comparison; no claim is made that it is an algebro-geometric degree.

The two input formulas are classical and the final comparison is elementary. A historical source or exercise may contain the same inequality without emphasizing it as a duality-versus-topology crossover.

## References
Paolo Aluffi, *Projective duality and a Chern-Mather involution*, arXiv:1601.05427, first submitted 20 January 2016; *Transactions of the American Mathematical Society* 370 (2018), 1803--1822.

James Fullwood and Martin Helmer, *On the Euler characteristic of a relative hypersurface*, arXiv:1603.03553, first submitted 11 March 2016.
