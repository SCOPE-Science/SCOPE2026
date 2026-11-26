# The six-level trisecant-multiplicity spectrum of a Hermitian cubic over \(\mathbb F_{64}\)

## Finding
Let \(K=\mathbb F_2[t]/(t^6+t+1)\cong\mathbb F_{64}\), and let \(E\subset\mathbb P^2_K\) be the smooth Hermitian elliptic cubic
\[
E:\qquad Y^2Z+YZ^2+X^3=0.
\]
Write \(\Omega=E(K)\). For every point \(P\in\mathbb P^2(K)\), let
\[
s(P)=\#\{\ell\in(\mathbb P^2_K)^\vee(K):P\in\ell,\ \#(\ell(K)\cap\Omega)=3\}.
\]
Thus \(s(P)\) counts **distinct lines**, not triples of points or intersection multiplicities.

There are exactly \(81\) points of \(\Omega\) and exactly \(1056\) three-secants to \(\Omega\). The complete distribution **outside the curve** is

| \(s(P)\) | \(\#\{P\in\mathbb P^2(K)\setminus\Omega:s(P)\text{ has this value}\}\) |
|---:|---:|
| 11 | 72 |
| 14 | 648 |
| 16 | 2052 |
| 17 | 864 |
| 18 | 432 |
| 26 | 12 |

In particular, every external point lies on at least **eleven** distinct rational three-secants. Moreover,
\[
s(P)=26\quad\Longleftrightarrow\quad
P\in\mathbb P^2(\mathbb F_4)\setminus E(\mathbb F_4),
\]
where \(\mathbb F_4\) is the unique degree-two subfield of \(K\). Thus the twelve points in this subplane complement are exactly the maximum-multiplicity locus.

For context, the numbers of rational lines meeting \(\Omega\) in respectively \(0,1,2,3\) points are \(1080,1953,72,1056\). On the curve itself, \(s(P)=40\) at the nine flexes \(E(\mathbb F_4)\), and \(s(P)=39\) at the other seventy-two rational points.

## Assumptions and scope
All point and line counts are **over the single specified field** \(K=\mathbb F_{64}\); no claim is made for an arbitrary power of two or for other Hermitian curves. The polynomial \(t^6+t+1\) is irreducible over \(\mathbb F_2\). The subfield \(\mathbb F_4\subset K\) comprises exactly the elements \(u\) with \(u^4=u\). The partial derivatives of the defining cubic, in characteristic two, are \(X^2,Z^2,Y^2\), which never vanish simultaneously at a projective point; hence \(E\) is geometrically smooth.

## Proof
**1. The curve and the three-secants.** Over \(\mathbb F_4\), the curve has nine rational points: for \(x=0\) there are two choices of \(y\), for each nonzero \(x\in\mathbb F_4\) there are two, and there is one point at infinity. Equality in the genus-one Hasse bound gives both Frobenius eigenvalues equal to \(-2\) for the \(\mathbb F_4\)-Frobenius. Passing to its third power, we obtain
\[
\#E(\mathbb F_{64})=64+1-2(-2)^3=81.
\]
The point at infinity is a flex. At an affine point \((a,b)\), substitution of the tangent line \(y=b+a^2(x+a)\) into \(x^3+y^2+y=0\), with \(x=a+h\), gives
\[
h^3+(a+a^4)h^2.
\]
Thus the flexes are exactly the nine points of \(E(\mathbb F_4)\); in the elliptic group law they are precisely the rational three-torsion points.

An \(E(K)\)-rational tangent at a nonflex point \(T\) meets \(E\) again at the distinct rational point \(-2T\). Distinct tangent points cannot determine the same line with two distinct tangencies on a cubic. Hence precisely \(81-9=72\) rational lines meet \(\Omega\) in exactly two distinct points. Every unordered pair of distinct rational points determines a unique line, and all line intersections have at most three geometric points by Bézout. Therefore the number of lines meeting \(\Omega\) in three distinct rational points is
\[
\frac{\binom{81}{2}-72}{3}=1056.
\]
The \(4161=64^2+64+1\) lines contain a total of \(81\cdot65\) point-line incidences with \(\Omega\). Solving the two elementary incidence equations yields the claimed line-character counts \((1080,1953,72,1056)\).

For a fixed \(P\in\Omega\), the elliptic group law says that a three-secant through \(P\) corresponds to an unordered pair of distinct points \(Q,R\not=P\) satisfying \(Q+R=-P\). Since doubling is a bijection of the odd-order group \(E(K)\), this gives \((81-3)/2=39\) such lines unless \(3P=0\), when the exclusions coincide and the count is \((81-1)/2=40\).

**2. Exact external multiplicities by a finite algebraic certificate.** We specify the complete enumeration, not a sampling argument. Every projective point has exactly one of the representatives
\[
(a,b,1)\ (a,b\in K),\qquad (1,m,0)\ (m\in K),\qquad(0,1,0).
\]
Every projective line likewise has a unique coefficient triple normalized at its first nonzero coordinate; its incidence with \((x,y,z)\) is tested by \(Ax+By+Cz=0\). The standalone program `verify_hermitian_secants.py` constructs the finite field by six-bit polynomial arithmetic modulo \(t^6+t+1\), checks that all nonzero elements have unique multiplicative inverses, enumerates the \(4161\) points and lines, evaluates the cubic, determines the \(1056\) three-secants, and then counts their incidences with every point. It obtains exactly the six rows of the displayed external table, and checks that the maximum-multiplicity locus is the subplane complement specified above. Every point and every line is explicitly included, so this is an exhaustive finite proof of the stated finite-field census.

The certificate additionally checks the table by a **different** method using affine cubic root counts, not by reusing the first incidence matrix. For each \(m,v\in K\), define
\[
T_m(v)=\#\{x\in K:x^3+m^2x^2+mx=v\},\qquad
A=\{u^2+u:u\in K\}.
\]
For an affine point \(P=(a,b,1)\), the nonvertical line \(y=m(x-a)+b\) cuts \(E\) in three distinct rational points exactly when
\[
T_m((b+ma)^2+b+ma)=3.
\]
The vertical line through \(P\) is a three-secant exactly when \(a^3\in A\). Consequently the independently evaluated formula is
\[
s(a,b,1)=\mathbf 1_{\{a^3\in A\}}
 +\sum_{m\in K}\mathbf 1_{\{T_m((b+ma)^2+b+ma)=3\}}.
\]
For a point at infinity \((1,m,0)\) the corresponding formula is
\[
s(1,m,0)=\sum_{c\in K}\mathbf 1_{\{T_m(c^2+c)=3\}},
\]
and for the point \((0,1,0)\) it is
\[
s(0,1,0)=\#\{a\in K:a^3\in A\}.
\]
These independently computed multiplicities agree at **all \(4161\) points** with those obtained from full projective line incidence. The program tests the exact subfield condition \(u^4=u\) in all three homogeneous coordinates and proves by complete enumeration that precisely the twelve external subplane points have multiplicity \(26\).

**3. Cross-checks.** The external frequencies sum to \(4080=4161-81\), and their weighted sum is
\[
72\cdot11+648\cdot14+2052\cdot16+864\cdot17+432\cdot18+12\cdot26=65472.
\]
The same number follows independently by counting the incidences of the \(1056\) three-secants with their \(65\) rational points and removing those on the cubic:
\[
1056\cdot65-(72\cdot39+9\cdot40)=65472.
\]
In particular, the minimum of the six confirmed values is exactly \(11\), proving the robust covering claim.

## Verification
Run `python3 verify_hermitian_secants.py` from the directory containing this report. It uses only the Python standard library and prints `H64_TRISECANT_MULTIPLICITY_PASS` on success. It checks all field inverses, both complete enumerations, line characters, all six external multiplicities, the flex multiplicities, the subfield maximum locus, and incidence-sum identities. The finite-field enumeration completes the proof for this specific finite problem; no sample-to-infinite inference is made.

## Relationship to prior work
Korchmáros, Nagy and Szőnyi (first public version February 20, 2023) study completeness of Hermitian-curve arcs in extension planes and give the line characters, with a general result for extension exponent at least four. Their paper highlights the exponent-three question. Bartoli, Marcugini and Pambianco (October 28, 2015), Table 99, **already list the \(81\)-point equianharmonic cubic over \(\mathbb F_{64}\) as complete**. Consequently **neither completeness nor the existence of this cubic is asserted here as new**. Bartoli and Timpanella (2025) establish an asymptotic large-parameter completeness result at extension exponent three and supply lower bounds of order cubic in that parameter. Their result does not state the six-level small-field distribution here.

The separately assessed contribution is the exact per-external-point three-secant multiplicity distribution, its sharp minimum \(11\), and the precise subplane characterization of its maximum. The previously known binary fact “at least one three-secant through each external point” does not determine any of those numerical or geometric refinements.

## Limitations
Only the specified embedded cubic over \(\mathbb F_{64}\) is classified. The result says nothing about corresponding multiplicity spectra for larger Hermitian curves or other extension degrees, and does not classify all complete cubic arcs. A prior equivalent exterior-point incidence table might exist under finite-geometry terminology; literature search cannot rule that out. The proof of the six-valued exterior spectrum is an exhaustive, auditable finite calculation, not a closed symbolic general formula.

## References
1. G. Korchmáros, G. P. Nagy, T. Szőnyi, *Algebraic approach to the completeness problem for \((k,n)\)-arcs in planes over finite fields*, arXiv:2302.10162 (first posted 2023-02-20), J. Combin. Theory Ser. A 204 (2024), 105851. https://arxiv.org/abs/2302.10162
2. D. Bartoli, S. Marcugini, F. Pambianco, *Completeness of cubic curves in \(\mathrm{PG}(2,q)\), \(q\le81\)*, arXiv:1510.08375 (first posted 2015-10-28), especially Table 99. https://arxiv.org/abs/1510.08375
3. D. Bartoli, M. Timpanella, *Complete \((k,q+1)\)-arcs in \(\mathrm{PG}(2,\mathbb F_{q^6})\) from the Hermitian curve*, J. Algebraic Combin. 62 (2025), article 21. https://doi.org/10.1007/s10801-025-01456-w
