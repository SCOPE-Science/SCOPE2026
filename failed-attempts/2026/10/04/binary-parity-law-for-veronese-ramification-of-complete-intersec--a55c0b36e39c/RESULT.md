# Binary parity law for Veronese ramification of complete-intersection curves
## Finding
Let \(C\subset\mathbb P^N_{\mathbb C}\) be a smooth complete-intersection curve of multidegree
\[
(d_1,\ldots,d_{N-1}),
\qquad d_i\ge2.
\]
Write
\[
D=\prod_i d_i,
\qquad
S=\sum_i d_i.
\]
Fix an integer \(k\) with
\[
1\le k<\min_i d_i.
\]
Restrict all degree-\(k\) homogeneous forms on \(\mathbb P^N\) to \(C\). Because the complete-intersection ideal has no nonzero element in degree below \(\min_i d_i\), these sections form a base-point-free linear series of projective dimension
\[
r=M-1,
\qquad
M=\binom{N+k}{k},
\]
on the line bundle \(\mathcal O_C(k)\), whose degree is \(kD\).

Let \(R_k\) be its Wronskian ramification divisor. Then
\[
\deg R_k
=
M\left(
kD+(M-1)\frac{D(S-N-1)}2
\right).
\]
Its parity has the following complete binary classification:
\[
\deg R_k\equiv1\pmod2
\]
if and only if all three conditions hold:
\[
k\equiv1\pmod2,
\qquad
d_i\equiv1\pmod2\ \text{for every }i,
\qquad
N\mathbin{\&}k=0,
\]
where \(N\mathbin{\&}k=0\) means that the binary expansions of \(N\) and \(k\) have no position containing a \(1\) in both numbers.

Equivalently, odd total ramification occurs exactly when \(kD\) is odd and adding \(N\) and \(k\) in base two produces no carry. In particular, for the original projective embedding \(k=1\), the ramification degree is odd exactly when \(N\) is even and all defining degrees are odd.

If the complete intersection and the linear series are defined over \(\mathbb R\), odd \(\deg R_k\) forces at least one real point in the support of \(R_k\). Thus every real smooth complete intersection satisfying the binary criterion has a real inflection or hyperosculating point in its \(k\)-th Veronese re-embedding.

## Assumptions and scope
The ground field for the complex statement is \(\mathbb C\), so the ordinary Wronskian theory is separable and no positive-characteristic correction is needed. The curve is smooth and is cut out scheme-theoretically by \(N-1\) hypersurfaces of degrees \(d_i\).

The condition \(k<\min_i d_i\) is structural, not cosmetic. It guarantees
\[
H^0(\mathbb P^N,\mathcal I_C(k))=0,
\]
so all \(\binom{N+k}{k}\) ambient degree-\(k\) monomials remain linearly independent on \(C\). For larger \(k\), relations from the complete-intersection ideal change the dimension of the restricted linear series and the stated binomial criterion need not apply.

For the real consequence, the equations defining \(C\) are real and smooth over \(\mathbb C\), and the restricted degree-\(k\) series is taken over \(\mathbb R\). The conclusion is existence of a real ramification point counted in the Wronskian divisor; it does not assert simplicity of that ramification.

## Proof
For a base-point-free linear series of projective dimension \(r\) and degree \(e\) on a smooth curve of genus \(g\), the Wronskian is a section of
\[
L^{\otimes(r+1)}
\otimes
K_C^{\otimes r(r+1)/2}.
\]
Hence its ramification divisor has degree
\[
(r+1)\bigl(e+r(g-1)\bigr).
\]
This is the classical Plücker--Wronskian formula.

Here
\[
r=M-1,
\qquad
e=kD.
\]
Adjunction for a smooth complete-intersection curve gives
\[
2g-2=D(S-N-1),
\]
so
\[
g-1=\frac{D(S-N-1)}2.
\]
Substituting yields
\[
\deg R_k
=
M\left(
kD+(M-1)\frac{D(S-N-1)}2
\right).
\]

It remains to determine the parity. If \(M\) is even, then \(\deg R_k\) is even. If \(M\) is odd, then \(M-1\) is even, so
\[
\deg R_k\equiv kD\pmod2.
\]
Therefore
\[
\deg R_k\ \text{is odd}
\]
if and only if \(M\), \(k\), and \(D\) are all odd.

By the mod-\(2\) case of Kummer's theorem, equivalently Lucas's theorem,
\[
\binom{N+k}{k}
\]
is odd exactly when the addition of \(N\) and \(k\) in base two has no carry. This is exactly the bitwise condition
\[
N\mathbin{\&}k=0.
\]
Also, \(D\) is odd exactly when every \(d_i\) is odd. This proves the classification.

For the real consequence, \(R_k\) is an effective divisor defined over \(\mathbb R\). Every non-real point in its support occurs together with its complex conjugate, with the same multiplicity, so the non-real contribution to \(\deg R_k\) is even. If \(\deg R_k\) is odd, a real point must occur. Such a point is precisely a ramification point of the Veronese linear series, equivalently an inflection or hyperosculating point of the corresponding projective re-embedding.

## Verification
The bundled exact-integer checker recomputes the complete-intersection genus and Wronskian degree and verifies the parity criterion for every nondecreasing multidegree in a broad bounded family satisfying \(k<\min_i d_i\). It also verifies independently that
\[
\binom{N+k}{k}\equiv1\pmod2
\]
is equivalent to
\[
N\mathbin{\&}k=0
\]
for all tested pairs \(N,k\) in a much larger binary range.

These computations are regression evidence only. The infinite theorem follows from the Wronskian line-bundle degree, adjunction, and Kummer--Lucas parity.

## Relationship to prior work
Dan Laksov develops the Wronskian construction and Plücker formulas for linear systems on curves, including the total ramification-weight formula underlying the first step above. R. H. Dye studies hyperosculating spaces of special complete-intersection curves and gives explicit results for a particular equal-degree self-polar family. Viatcheslav Kharlamov and Frank Sottile study real ramification of rational curves, using the Wronskian to encode inflection and defining maximally inflected curves by reality of all ramification points.

The present statement combines the general Wronskian degree with complete-intersection adjunction and the dimension of the low-order Veronese series, then applies Kummer--Lucas parity to classify exactly when the total ramification degree is odd. The inspected sources do not state the resulting bitwise criterion \(N\mathbin{\&}k=0\) for complete intersections, nor the resulting forced-real-ramification theorem for the Veronese re-embeddings considered here. Claim-specific searches using Wronskian, ramification, complete-intersection, Veronese, binary parity, and real-inflection terminology did not locate an equivalent statement.

## Limitations
The result concerns only the low-order range
\[
k<\min_i d_i,
\]
before the defining equations of the complete intersection introduce degree-\(k\) relations. Extending the parity law beyond that threshold requires replacing the binomial dimension \(M\) by the Hilbert-function value of the restricted series.

Odd total ramification forces a real ramification point but gives no lower bound larger than one and no information about multiplicity or topology of the real locus. The theorem is characteristic-zero; in positive characteristic the ordinary Wronskian can exhibit inseparability phenomena.

The originality comparison cannot exclude an unindexed classical source in which the same parity corollary is written explicitly.

## References
Dan Laksov, *Wronskians and Plücker formulas for linear systems on curves*, Annales scientifiques de l'École Normale Supérieure 17 (1984), 45--66. DOI: 10.24033/asens.1465.

R. H. Dye, *The hyperosculating spaces to certain curves in projective \(n\)-space*, Proceedings of the Edinburgh Mathematical Society 19 (1975), 301--309. DOI: 10.1017/S0013091500015583.

Viatcheslav Kharlamov and Frank Sottile, *Maximally inflected real rational curves*, arXiv:math/0206268, first submitted 25 June 2002; Moscow Mathematical Journal 3 (2003), 947--987.
