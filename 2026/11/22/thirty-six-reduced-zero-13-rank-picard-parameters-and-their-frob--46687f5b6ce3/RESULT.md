# Thirty-six reduced zero-\(13\)-rank Picard parameters and their Frobenius splitting

## Finding

Consider the centered, constant-normalized genus-three Picard family over \(\mathbb F_{13}\),
\[
C_{a,b}:\quad y^3=x^4+a x^2+b x+1.
\]
Let \(\Delta=3a^4-4a^3b^2+2a^2+ab^2-b^4-4\) in \(\mathbb F_{13}[a,b]\). On the smooth coefficient base \(U=\{(a,b):\Delta\ne0\}\), there are exactly three geometric strata:

| Condition | Jacobian \(13\)-rank | Cartier \(a\)-number |
|---|---:|---:|
| \(a^2\ne8\) | \(3\) | \(0\) |
| \(a^2=8\), \(Q_a(b)\ne0\) | \(1\) | \(2\) |
| \(a^2=8\), \(Q_a(b)=0\) | \(0\) | \(2\) |

Here
\[
Q_a(b)=b^{18}+3ab^{16}+7b^{14}+7ab^{12}+2b^{10}+6ab^8+4b^6+2ab^4+7b^2-a.
\]
The last locus is a reduced finite \(\mathbb F_{13}\)-scheme of length \(36\), disjoint from the discriminant, with **three degree-four closed points and two degree-twelve closed points**. Its arithmetic point-count and zeta formulas are
\[
\#Z(\mathbb F_{13^n})=12\mathbf1_{4\mid n}+24\mathbf1_{12\mid n},\qquad
Z(Z,T)=(1-T^4)^{-3}(1-T^{12})^{-2}.
\]
In particular, a Cartier \(a\)-number of two does not determine the geometric \(13\)-rank, even within this natural two-parameter Picard family.

## Assumptions and scope

The base field is algebraically closed of characteristic exactly \(13\); arithmetic splitting is for the literal marked coefficient scheme over \(\mathbb F_{13}\). Since the equation is a cubic tame cover of the line branched at the four simple roots of the quartic and at infinity, its smooth projective completion has genus three. The curve is smooth precisely when \(\Delta\ne0\), because the quartic is squarefree and the point at infinity of the plane quartic is smooth. No counts of unmarked geometric isomorphism classes are asserted.

Write \(u\in\mathbb F_{169}\) for a root of \(u^2=8\). The polynomial \(a^2-8\) is irreducible over \(\mathbb F_{13}\), so \(u^{13}=-u\). The displayed zero-rank stratum consists of both fibers \(a=u\) and \(a=-u\).

## Proof

**1. Explicit Cartier matrix.** The differential basis is \(\omega_1=dx/y^2\), \(\omega_2=x\,dx/y^2\), \(\omega_3=dx/y\). For \(f(x)=x^4+a x^2+b x+1\), applying Cartier to \(f^8\,dx/y^{26}\) and \(f^4\,dx/y^{13}\) gives a block diagonal \(13^{-1}\)-semilinear operator with coefficient matrix, before extracting thirteenth roots,
\[
\begin{pmatrix}B&0\\0&h\end{pmatrix},\quad
B=\begin{pmatrix}
[x^{12}]f^8 &[x^{11}]f^8\\
[x^{25}]f^8 &[x^{24}]f^8
\end{pmatrix},\qquad h=[x^{12}]f^4.
\]
A direct multinomial coefficient calculation in \(\mathbb F_{13}[a,b]\) establishes
\[
h=6(a^2+5),\qquad \det B=4(a^2+5)\Delta^2.
\]
Both identities are asserted and recomputed from the original quartic in the supplied exact verifier. Hence Cartier has full rank three off \(a^2=8\) on \(U\). On \(a^2=8\) it has rank exactly one: its scalar block vanishes, while in the indicated basis the second row of \(B\) equals \((-4b,2-ab^2)\), which never vanishes simultaneously.

**2. Stable Frobenius rank, beyond first Cartier rank.** The geometric \(13\)-rank of a Jacobian equals the stable rank of Cartier. Along \(a^2=8\), only the rank-one two-dimensional block \(B\) matters. Cartier on coefficient vectors is represented by \(B^{[1/13]}\) followed by coefficient-wise thirteenth roots; the square is therefore represented by \(B^{[1/13]}B^{[1/13^2]}\). Its zero/nonzero test is equivalently \(B^{[13]}B=0\), with \([13]\) denoting entry-wise raising to the thirteenth power. A rank-one semilinear endomorphism either has nonzero stable rank one or has zero square, since the scalar controlling its second iterate controls all further iterates up to Frobenius powers. Thus this single test completely distinguishes ranks zero and one.

Modulo \(a^2-8\), one obtains
\[
B=\begin{pmatrix}
a(4b^6+2b^2)-2b^4&a(4b^5-b)-5b^7+5b^3\\
-4b&2-ab^2
\end{pmatrix}.
\]
Compute the four entries of \(B^{[13]}B\) in the polynomial ring \(\mathbb F_{169}[b]\), using \(a^{13}=-a\) and replacing \(b\) by \(b^{13}\). Their **monic polynomial greatest common divisor** is exactly
\[
G_a(b)=\Delta(a,b)^2Q_a(b),\qquad
\Delta(a,b)|_{a^2=8}=9+8ab^2-b^4.
\]
The equality is an exact polynomial Euclidean-algorithm identity; the attached \(\texttt{verify.py}\) generates \(B\) from \(f\), forms the four large polynomials, calculates their gcd over \(\mathbb F_{169}\), and verifies the displayed factorization. No sampling or numerical approximation enters this step.

**3. Reduced zero-rank locus.** The same exact Euclidean calculation establishes
\[
\gcd(Q_a,\Delta(a,\cdot))=1,\qquad
\gcd(Q_a,Q_a')=1
\]
in \(\mathbb F_{169}[b]\). Each of the two values of \(a\) therefore contributes exactly eighteen simple roots on the smooth coefficient base, yielding a reduced finite scheme of degree \(36\) over the algebraic closure. The first-step Cartier rank remains one at these parameters, hence their \(a\)-number equals two; their stable rank is zero. Every other smooth member of the double Cartier-rank divisor has stable rank one.

**4. Frobenius splitting.** Put \(k_2=\mathbb F_{169}\) and fix \(a=u\). Direct Euclidean gcds with the \(k_2\)-Frobenius polynomials yield
\[
\deg\gcd\bigl(Q_u(b),b^{169^d}-b\bigr)=
\begin{cases}0&d=1,3,\\6&d=2,4,\\18&d=6.\end{cases}
\]
Because \(Q_u\) is squarefree of degree eighteen, it has exactly three irreducible factors of degree two and two of degree six over \(k_2\). The \(13\)-Frobenius exchanges the two parameter fibers \(a=u\) and \(a=-u\); thus over \(\mathbb F_{13}\) their union has precisely three degree-four and two degree-twelve closed points. This gives the claimed point-count and zeta formulas.

## Verification

Execute `python verify.py` with Python 3 and SymPy. It expands \(f^4\) and \(f^8\) exactly modulo thirteen; proves the determinant identity directly as a polynomial identity; implements finite-field pair arithmetic modulo \(u^2-8\), Euclidean gcd and repeated Frobenius powers; then asserts the exact factorization, coprimality, squarefreeness and irreducible-degree profile. Success prints `VERIFY_OK` and the geometric and arithmetic conclusions. The executable is a standalone deterministic certificate; it uses no external datasets.

## Relationship to prior work

Bouw, Koutsianas, Sijsling and Wewers give the canonical monic-quartic presentation and discriminant framework for Picard curves. Nourozi and Rahmati study the first Cartier rank and \(a\)-number, not the refined stable-rank splitting here. Related work on the one-parameter bielliptic subfamily, where the linear coefficient is zero, does not determine the rank-zero parameters with nonzero linear coefficient: indeed \(Q_a(0)=-a\ne0\) on \(a^2=8\). Published work on the two-parameter Hasse divisor detects first-rank degeneracy but does not imply the exact \(36\)-point stable-rank scheme, its reducedness or the \(4\)-and-\(12\) Frobenius decomposition. Full-text comparisons and search coverage are qualified by possible unindexed equivalent computations.

## Limitations

The theorem is specific to characteristic thirteen and the marked constant-one slice; it does not classify unmarked Picard isomorphism classes, full Newton polygons, Ekedahl–Oort types, or ranks outside this family. Its exact polynomial computation is independently reproducible from the supplied code, but no independent scholarly validation of the new claim is asserted. An older equivalent computation in another coordinate system remains a residual priority risk.

## References

1. I. I. Bouw, A. Koutsianas, J. Sijsling and S. Wewers, *Conductor and discriminant of Picard curves*, arXiv:1902.09624 (first public 2019-02-25), https://arxiv.org/abs/1902.09624.
2. V. Nourozi and F. Rahmati, *The Rank of the Cartier operator on Picard Curves*, arXiv:2306.07823 (first public 2023-06-13), https://arxiv.org/abs/2306.07823.
3. J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297 (first public 2023-08-29), https://arxiv.org/abs/2308.15297.
4. Y. Takizawa, *A Picard family of curves and hypergeometric functions over finite fields I*, arXiv:1608.07474 (first public 2016-08-25), https://arxiv.org/abs/1608.07474.
5. J. Estrada-Sarlabous, *On the Jacobian varieties of Picard curves defined over fields of characteristic p > 0*, Math. Nachr. 152 (1991), 329–340, https://doi.org/10.1002/mana.19911520125 (publisher abstract inspected; complete article unavailable).
