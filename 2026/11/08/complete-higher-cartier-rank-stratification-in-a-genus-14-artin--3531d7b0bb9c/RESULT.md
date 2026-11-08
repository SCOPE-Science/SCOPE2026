# Complete higher Cartier-rank stratification in a genus-14 Artin–Schreier family

## Finding
Let \(k\) be an algebraically closed field of characteristic \(5\). For arbitrary \(a,b,c,e,f\in k\), let \(C\) be the smooth projective model of
\[
y^5-y=F(x),\qquad F(x)=x^8+a x^6+b x^4+c x^3+e x^2+f x.
\]
The curve has genus \(14\), and its Jacobian has \(5\)-rank zero. Write \(\mathcal C\) for its semilinear Cartier operator on regular differentials, and put
\[
\Delta=ae+2a^2b-b^2.
\]
The complete ranks of its positive iterates are as follows; all unlisted higher ranks vanish:

| Condition | \(\operatorname{rk}\mathcal C\) | \(\operatorname{rk}\mathcal C^2\) | \(\operatorname{rk}\mathcal C^3\) |
|---|---:|---:|---:|
| \(b\ne0,\ \Delta\ne0\) | 6 | 3 | 1 |
| \(b\ne0,\ \Delta=0\) | 5 | 3 | 1 |
| \(b=0,\ ae\ne0,\ ae^5+1\ne0\) | 6 | 2 | 0 |
| \(b=0,\ ae^5+1=0\) | 6 | 1 | 0 |
| \(b=0,\ ae=0,\ (a,e)\ne(0,0)\) | 5 | 2 | 0 |
| \(b=a=e=0\) | 4 | 2 | 0 |

In particular the Jacobian \(a\)-number, \(14-\operatorname{rk}\mathcal C\), takes precisely the values \(8,9,10\). The first-rank jumping hypersurface \(\Delta=0\) is an irreducible quadric cone after the polynomial coordinate change \(e'=e+2ab\); its singular locus is \(a=b=e=0\). Independently, \(b=0\) is exactly the locus where \(\mathcal C^3=0\). Within \(b=0\), the smooth irreducible codimension-two locus \(ae^5+1=0\) has \(\operatorname{rk}\mathcal C^2=1\), although the first Cartier rank remains the generic value \(6\). Thus the \(a\)-number does not determine even the second Cartier rank in this family.

## Assumptions and scope
All statements concern the smooth projective normalization of the indicated affine Artin–Schreier equation over any algebraically closed characteristic-five field. The leading coefficient is \(1\), and the terms of exponents \(7\) and \(5\) have been eliminated in the usual one-pole standard form. No restriction on the five remaining coefficients is imposed. Iterated ranks mean the dimensions over \(k\) of the images of the semilinear Cartier maps. They do not assert a complete Ekedahl–Oort classification.

## Proof
The polynomial \(F\) has one pole of order \(8\) on the base projective line; this order is prime to \(5\). Riemann–Hurwitz gives \(2g-2=26\), so \(g=14\). There is one point above infinity, where the valuations of \(x,y,dx\) are respectively \(-5,-8,26\). Consequently a basis for regular differentials is
\[
\mathcal B=\{x^i y^j\,dx: i,j\ge0,\ 5i+8j\le26\},
\]
ordered by \(j\) then \(i\). Explicitly it consists of \(dx,x\,dx,\ldots,x^5\,dx\), then \(y\,dx,xy\,dx,x^2y\,dx,x^3y\,dx\), then \(y^2\,dx,xy^2\,dx,x^2y^2\,dx\), then \(y^3\,dx\). The basis contains \(6+4+3+1=14\) elements.

For \(j<5\), use \(y^j=(y^5-F(x))^j\) and the identities \(\mathcal C(h^5\omega)=h\mathcal C(\omega)\) and \(\mathcal C(x^{5m+4}\,dx)=x^m\,dx\) (other monomials have zero Cartier image). Let \(M\) be the matrix obtained by raising each entry of the semilinear Cartier matrix to its fifth power. Its entries are **polynomials** in \(a,b,c,e,f\); explicitly its column for \(x^i y^j\,dx\) is recovered by the coefficient formula
\[
M_{(u,\ell),(i,j)}=
(-1)^{j-\ell}\binom j\ell
[x^{5u+4}]\bigl(x^i F(x)^{j-\ell}\bigr),\qquad 0\le\ell\le j,
\]
with rows and columns indexed by \(\mathcal B\), and zero in the remaining positions. This completely specifies the finite matrix in arbitrary characteristic-five coefficients.

Elementary elimination of four constant nonzero pivots in \(M\) leaves the two-by-two block
\[
\begin{pmatrix}2a&a^2+2b\\-2b&-2e\end{pmatrix}.
\]
Its determinant is \(\Delta=ae+2a^2b-b^2\). Its rank is two for \(\Delta\ne0\), one for \(\Delta=0\) except at \(a=b=e=0\), and zero at that latter locus. Therefore the first Cartier rank is respectively \(6,5,4\).

Because Cartier is inverse-Frobenius-semilinear, the matrices \(M^{[5]}M\), \(M^{[25]}M^{[5]}M\), and \(M^{[125]}M^{[25]}M^{[5]}M\) have the ranks of \(\mathcal C^2,\mathcal C^3,\mathcal C^4\), respectively; brackets mean entrywise Frobenius powers. Exact polynomial multiplication shows that \(M^{[5]}M\) has nonzero rows only at the positions for \(dx,x\,dx,x^2\,dx,y\,dx\), and nonzero columns only at the positions for \(y^2\,dx,xy^2\,dx,x^2y^2\,dx,y^3\,dx\). Of the relevant entries, the coefficient at \((dx,y^2\,dx)\) is \(2b^6\), that at \((x\,dx,xy^2\,dx)\) is \(2\), and that at \((y\,dx,y^3\,dx)\) is \(b^6\). Both the \(x^2\,dx\) row and the \(y\,dx\) row are supported only in the last column. Hence the rank is exactly three when \(b\ne0\).

When \(b=0\), only the first two of these rows survive. Their columns for \(xy^2\,dx\) and \(y^3\,dx\) form
\[
\begin{pmatrix}
2c^5&-ac^6-ae^5-c^5f-1\\
2&-ac-f
\end{pmatrix},
\]
whose determinant is \(2(ae^5+1)\). The rank is one on \(ae^5+1=0\), and two otherwise. Finally \(M^{[25]}M^{[5]}M\) has exactly one potentially nonzero entry: row \(dx\), column \(y^3\,dx\), equal to \(-b^{31}\). The fourth product is identically zero. These calculations establish all six rows of the table. In particular \(\mathcal C^4=0\) proves the asserted \(5\)-rank zero.

The claimed geometry follows from \(\Delta=a(e+2ab)-b^2\). The quadric \(ae'-b^2=0\) has singular locus \(a=b=e'=0\); the other two parameters are free. The locus \(b=0,ae^5=-1\) has \(a,e\ne0\) and is isomorphic to \(\mathbb G_m\times\mathbb A^2\) using \(e,c,f\) as coordinates; it is disjoint from \(\Delta=0\). This also proves every row of the classification is realized over \(k\).

## Verification
The standalone program `verify_cartier.py` reconstructs \(M\) coefficient by coefficient from the defining equation, computes the Frobenius-twisted matrix products symbolically modulo five, verifies the determinant and entry claims, and exhaustively tests all \(5^5=3125\) coefficient tuples over \(\mathbb F_5\) with an independently implemented modular Gaussian elimination. The recorded output is `verification_output.txt`. The symbolic argument establishes the result over every algebraically closed characteristic-five field; the finite-field census is a consistency check and not an infinite-field proof.

## Relationship to prior work
Farnell's 2010 thesis and Farnell–Pries (arXiv:1202.4183, first public preprint 2012-02-19) develop the regular-differential basis and determine constant Cartier rank when pole orders divide \(p-1\). Here the sole pole order is \(8\), which does not divide \(4\), and the \(a\)-number is not constant. Booher–Cais (arXiv:1807.10313) give bounds for \(a\)-numbers, while Groen (arXiv:2208.06504) gives bounds for the ranks of Cartier powers and examples in other pole-order families. The complete five-parameter rank stratification, including the Frobenius-twisted codimension-two jumping locus, is not a stated consequence of those inspected results. This comparison is provisional, not a claim of exhaustive historical priority.

## Limitations
The claims concern only the indicated normalized one-pole family and the Cartier-rank sequence. They neither classify the full \(5\)-torsion group schemes nor determine Newton polygons, and the coefficient parameter space is not asserted to represent distinct unmarked isomorphism classes. Independent historical-priority assessment and independent scientific validation remain outstanding.

## References
1. S. Farnell, *Artin-Schreier Curves*, Colorado State University thesis, 2010, persistent identifier `hdl:10217/44957`.
2. S. Farnell and R. Pries, *Families of Artin-Schreier curves with Cartier-Manin matrix of constant rank*, arXiv:1202.4183v1 (19 February 2012).
3. J. Booher and B. Cais, *a-numbers of curves in Artin-Schreier covers*, arXiv:1807.10313; *Algebra & Number Theory* 14 (2020).
4. S. R. Groen, *Powers of the Cartier operator on Artin-Schreier covers*, arXiv:2208.06504v2 (2024 revision; original preprint 2022).
