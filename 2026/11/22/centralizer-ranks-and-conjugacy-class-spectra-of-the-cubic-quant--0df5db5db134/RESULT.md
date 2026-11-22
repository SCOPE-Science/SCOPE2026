# Centralizer ranks and conjugacy-class spectra of the cubic quantum complete-intersection algebra group

## Finding
Let \(k=\mathbb F_q\) be a finite field containing a primitive cube root \(\zeta\), equivalently \(q\equiv1\pmod3\). Consider the nine-dimensional unital associative algebra
\[
A=k\langle x,y\rangle/(x^3,y^3,yx-\zeta xy),\qquad J=(x,y),\qquad G=1+J.
\]
For \(u\in A\), let \(r(u)=\dim_k\operatorname{im}(\operatorname{ad}_u)\), where \(\operatorname{ad}_u(v)=uv-vu\). Write \(N_r\) for the number of elements of \(A\) of adjoint rank \(r\), and \(K_r\) for the number of conjugacy classes of \(G\) of size \(q^r\). The **complete** spectra are

| \(r\) | \(N_r\) | \(K_r\) |
|---|---|---|
| \(0\) | \(q^2\) | \(q\) |
| \(1\) | \((q^2-1)q^2\) | \(q^2-1\) |
| \(2\) | \((q^2+q-2)q^4\) | \(q(q^2+q-2)\) |
| \(3\) | \((q-1)(q^2-1)q^4\) | \((q-1)(q^2-1)\) |
| \(4\) | \((q^2-1)q^7\) | \(q^2(q^2-1)\) |

No other ranks or conjugacy-class sizes occur. In particular, the class number and ordinary commuting probability of the algebra group are
\[
\boxed{k(G)=q^4+2q^3-2q},\qquad
\boxed{\operatorname{cp}(G)=\operatorname{cp}(A)=\frac{q^3+2q^2-2}{q^7}}.
\]
Here \(\operatorname{cp}(A)\) means the probability that two independently uniform elements commute multiplicatively in \(A\), not the probability that a sampled element is invertible. All formulas hold in characteristic two as well as odd characteristics other than three.

## Assumptions and scope
The parameter \(q\) is any prime power congruent to one modulo three, and \(\zeta\) is either primitive cubic root in \(k\). The quotient has PBW basis \(x^iy^j\) with \(0\le i,j\le2\); its radical \(J\) is eight-dimensional and nilpotent, so \(G=1+J\) is a group of order \(q^8\). Scalars commute with everything. The algebra relation is written \(yx=\zeta xy\), the inverse-parameter convention to some literature. No claim is made for other exponents, for a commutative twist, or for fields without a primitive cubic root.

## Proof
**Explicit commutator matrix.** Write the general element as
\[
u=s1+ax+by+cx^2+dxy+ey^2+fx^2y+gxy^2+hx^2y^2.
\]
The skew relation gives the multiplication rule
\[
(x^iy^j)(x^ky^l)=\zeta^{jk}x^{i+k}y^{j+l}
\]
when both resulting exponents are at most two, and zero otherwise. This also proves the claimed PBW basis, by the standard skew-polynomial normal-form argument. Since \(\zeta^3=1\) and \(1+\zeta+\zeta^2=0\), divide the matrix of \(\operatorname{ad}_u\) by its nonzero common factor \(\zeta-1\). On input columns \((x,y,x^2,xy,y^2,x^2y,xy^2)\), and output rows \((xy,x^2y,xy^2,x^2y^2)\), the resulting matrix is exactly
\[
M(u)=\begin{pmatrix}
b&-a&0&0&0&0&0\\
d&\zeta^2c&-\zeta^2b&-a&0&0&0\\
-\zeta^2e&-d&0&b&\zeta^2a&0&0\\
-\zeta^2g&\zeta^2f&e&0&-c&-\zeta^2b&\zeta^2a
\end{pmatrix}.
\]
The omitted input columns \(1,x^2y^2\) are zero, and the omitted output rows are zero. Thus \(r(u)=\operatorname{rank}M(u)\) in every allowed characteristic.

**Classification.** If \((a,b)\ne(0,0)\), the first row is nonzero, the restrictions of rows two and three to the degree-two input columns are independent, and the fourth row is independent because its degree-three input restriction \((-\zeta^2b,\zeta^2a)\) is nonzero. Hence \(r(u)=4\).

If \(a=b=0\), the first row vanishes, and the degree-one-input part of rows two and three is
\[
B=\begin{pmatrix}d&\zeta^2c\\-\zeta^2e&-d\end{pmatrix},
\qquad \det B=\zeta ce-d^2.
\]
When \((c,e)\ne(0,0)\), the fourth row is independent of these two rows because its degree-two-input restriction is \((e,0,-c)\ne0\). In that case the rank equals \(1+\operatorname{rank}B\), namely three if \(\zeta ce\ne d^2\) and two if equality holds; \(B\) cannot vanish. When \(c=e=0\) but \(d\ne0\), rows two and three are independent while row four lies in their span, so the rank is two. If \(c=d=e=0\), the rank is one when \((f,g)\ne(0,0)\), and zero otherwise. These alternatives are exhaustive, regardless of \(s,h\).

**Counting.** The split quadratic cone \(\zeta ce=d^2\) has precisely \(q^2\) points in \(k^3\). Indeed, for \(d\ne0\), there are \((q-1)^2\) choices of \((c,d,e)\); for \(d=0\), there are \(2q-1\) choices, giving \(q^2\). The cases \(c=e=0,d\ne0\) contribute \(q-1\) exceptional rank-two triples outside this cone. Consequently the numbers of degree-two triples producing ranks three and two (with no linear part) are \((q-1)(q^2-1)\) and \(q^2+q-2\), respectively. The coefficients \(f,g,s,h\) are arbitrary, supplying \(q^4\) choices. If the quadratic part vanishes, \((f,g)\ne(0,0)\) gives \((q^2-1)q^2\) elements of rank one, while \(s,h\) alone gives \(q^2\) central elements. Elements with nonzero linear part contribute \((q^2-1)q^7\) of rank four. This yields the displayed \(N_r\), which sum to \(q^9\).

**Conjugacy and commuting.** For each \(u\in J\), the unit \(1+u\) commutes with \(1+v\in G\) if and only if \(uv=vu\). The adjoint map has image in \(J\) and annihilates scalars, so its restriction to \(J\) still has rank \(r(u)\). Therefore \(|C_G(1+u)|=q^{8-r(u)}\) and the conjugacy class of \(1+u\) has size \(q^{r(u)}\). Every rank stratum of \(A\) has exactly \(1/q\) of its elements inside \(J\), because the scalar coefficient is free. Thus \(K_r=N_r/q^{r+1}\), giving the five class-count formulas. Summing gives \(k(G)=q^4+2q^3-2q\). The usual class-number identity yields \(\operatorname{cp}(G)=k(G)/q^8\); alternatively averaging \(q^{-r}\) over \(A\) gives the same commuting probability for \(A\), since scalars do not affect commutators.

## Verification
The included independent direct-multiplication checker `check_cubic_centralizers.py` implements the PBW product and finite-field Gaussian elimination, without using the displayed four-by-seven matrix to obtain ranks. It exhaustively checks every five-tuple of coefficients controlling the low-degree cases over \(\mathbb F_4,\mathbb F_7,\mathbb F_{13}\) (respectively \(1024\), \(16807\), and \(371293\) tuples), checks degree-three variations on independent slices, and verifies all full-algebra rank multiplicities and commuting-pair totals. Its output is included as `verification_output.txt`. Exhaustive checks of parameter slices are not exhaustive enumeration of all \(q^9\) elements and do not replace the all-field proof.

## Relationship to prior work
Bergh and Erdmann's 2007 paper defines two-generator quantum complete intersections and studies Hochschild (co)homology via bimodule resolutions. Its stated invariants and inspected initial sections do not calculate all elementwise commutant ranks. The published census *A six-stratum Jordan census and principal right-ideal count for the cubic quantum complete intersection* concerns **left multiplication** Jordan partitions and principal right ideals of the same algebra. Its complete proof was inspected. Neither its statements nor its stratification imply the adjoint ranks: within its left-multiplication rank-four stratum, \(xy\) and \(x^2+y^2\) have adjoint ranks two and three respectively. *Cyclotomic resonance in the centralizer spectra of two-generator quantum complete intersections* treats exponent-two algebras \(x^2=y^m=0\), not the present exponent-three algebra, and its full formula and proof were inspected. Earlier rank-variety work and later general constant-Jordan-type results concern restrictions of modules along linear pencils rather than conjugacy-class spectra of \(1+J\). The present result identifies an intrinsic conjugacy-class-size distribution not determined by those previous enumerators.

## Limitations
This is a result for the symmetric cubic primitive-root quantum complete intersection, not a general theorem about arbitrary two-generator quantum complete intersections or all associated groups. Finite-field verification checks only specified fields and coefficient slices, not the complete infinite family. The conjugacy-class-size spectrum does not classify conjugacy-class representatives or irreducible characters. A previously unindexed class-number computation for an isomorphic finite algebra group remains possible; the literature comparison does not certify absolute publication priority. No independent mathematical audit has been performed.

## References
1. P. A. Bergh and K. Erdmann, “(Co)homology of quantum complete intersections,” arXiv:0709.3029v1, first posted 2007-09-19, https://arxiv.org/abs/0709.3029.
2. D. J. Benson, K. Erdmann and M. Holloway, “Rank varieties for a class of finite-dimensional local algebras,” *J. Pure Appl. Algebra* 211 (2007), 497–510, DOI: 10.1016/j.jpaa.2007.02.006.
3. “Cyclotomic resonance in the centralizer spectra of two-generator quantum complete intersections,” published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-cyclotomic-resonance-in-the-centralizer-spectra-of-two-generator--56b11792d0e8.
4. “A six-stratum Jordan census and principal right-ideal count for the cubic quantum complete intersection,” published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-six-stratum-jordan-census-and-principal-right-ideal-count-for--7f6201de1b8d.
