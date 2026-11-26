# The \(a\)-number jump divisor of one-pole conductor-six Artin–Schreier curves in characteristic five

## Finding
Let \(k\) be algebraically closed of characteristic \(5\). For every \((a,b,c,d)\in k^4\), let \(C_{a,b,c,d}\) be the smooth projective model of
\[
y^5-y=x^6+a x^4+b x^3+c x^2+d x.
\]
Put \(Q=b^2+2a^3+4ac\). Then \(C_{a,b,c,d}\) is geometrically connected of genus \(10\), has \(5\)-rank zero, and its Jacobian \(a\)-number satisfies the **complete** classification
\[
a(C_{a,b,c,d})=\begin{cases}
6,&Q\ne0,\\
7,&Q=0\text{ and }(a,b,c)\ne(0,0,0),\\
10,&a=b=c=0.
\end{cases}
\]
In particular, the \(a\)-numbers \(8\) and \(9\) do not occur. The reduced jumping divisor \(D=V(Q)\subset\mathbb A_k^4\) is geometrically irreducible and normal, with singular locus precisely \(L=V(a,b,c)\), an affine line in the free parameter \(d\). Transversally to this line \(D\) has an \(A_1\) rational double point: after the invertible coordinate change \(z=c+3a^2\),
\[
Q=b^2+4az.
\]
Along the smooth locus of \(D\) the \(a\)-number equals \(7\); on \(L\) it jumps directly to \(10\). These are coefficient-marked strata, not claims about the number of isomorphism classes.

## Assumptions and scope
The prime is exactly \(5\), the ground field is algebraically closed, and every coefficient is unrestricted. The projective curve means the smooth normalization of the possibly singular affine plane model. The pole order of the right side at infinity is \(6\), prime to \(5\), so the Artin–Schreier function field extension is connected, branched at infinity only, and has genus \((5-1)(6-1)/2=10\) by wild Riemann–Hurwitz. The Deuring–Shafarevich formula gives \(5\)-rank zero. The standard normal form removes an \(x^5\)-term by an Artin–Schreier change of the \(y\)-coordinate and a constant term by a constant shift of \(y\); scaling \(x\) makes the leading coefficient one. The theorem quantifies over this complete normalized coefficient family, without identifying coefficients under coordinate changes.

## Proof
**Regular differentials.** The unique point above infinity has valuations
\[
v_\infty(x)=-5,\qquad v_\infty(y)=-6,\qquad v_\infty(dx)=18.
\]
The last follows from the different exponent \((5-1)(6+1)=28\) and the pole contribution \(-2\deg(x)=-10\) to the canonical divisor of \(dx\). Hence the following ten monomials, all with nonnegative valuations and distinct pole weights, form a basis of global regular differentials:
\[
\mathcal B=(dx,x\,dx,x^2dx,x^3dx,y\,dx,xy\,dx,x^2y\,dx,y^2dx,xy^2dx,y^3dx).
\]
Indeed the allowed indices are exactly \(5i+6j\le18\) for \(i\ge0\) and \(0\le j\le3\), giving exactly the genus.

**Cartier calculation.** Choose fifth roots \(A^5=a\), \(B^5=b\), \(C^5=c\), \(T^5=d\), possible uniquely because \(k\) is perfect. For \(f(x)=x^6+ax^4+bx^3+cx^2+dx\), the identity \(y^5=y+f(x)\) and \(5^{-1}\)-linearity of Cartier give
\[
\mathcal C(x^iy^jdx)=\sum_{m=0}^{j}(-1)^m\binom jm y^{j-m}\mathcal C(x^if(x)^m dx),
\]
where \(\mathcal C(\sum h_n x^n dx)=\sum_r h_{5r+4}^{1/5}x^r dx\). In the ordered basis above, the only nonzero entries of the Cartier matrix \(M\), indexed from one, are
\[
\begin{array}{c|l}
\text{row}&\text{column : entry}\\ \hline
1&5:-A,\ 6:-B,\ 7:-C,\ 8:2BT+C^2,\ 9:2CT,\ 10:2CT^2\\
2&8:2B,\ 9:A^2+2C,\ 10:2A^2T-ABC-B^3-CT\\
3&10:2A^2+2C\\
5&8:-2A,\ 9:-2B,\ 10:BT-2C^2\\
6&10:B\\
8&10:2A.
\end{array}
\]
All entries are interpreted in characteristic five. This identity is also directly reproduced by the accompanying symbolic verifier.

**Rank classification.** If \((A,B,C)=(0,0,0)\), the displayed matrix is identically zero, independently of \(T\). Otherwise columns \(5,6,7\) span the one-dimensional first-coordinate line. Columns \(8,9\), modulo that line and restricted to rows \(2,5\), have matrix
\[
P=\begin{pmatrix}2B&A^2+2C\\-2A&-2B\end{pmatrix}.
\]
Column \(10\) has a component in the distinct rows \(3,6,8\) equal to \((2A^2+2C,B,2A)\), which cannot vanish unless \(A=B=C=0\). Thus \(\operatorname{rank}M=2+\operatorname{rank}P\). Since \(P\ne0\) in the present case, its rank is either one or two. Direct calculation in characteristic five gives
\[
\det P=B^2+2A^3+4AC,
\qquad (\det P)^5=b^2+2a^3+4ac=Q.
\]
Consequently \(\operatorname{rank}\mathcal C\) is \(3\) when \(Q=0\) and \(4\) when \(Q\ne0\). The Jacobian \(a\)-number is the dimension of the Cartier kernel on regular differentials, namely \(10-\operatorname{rank}\mathcal C\), proving all three cases and the nonexistence of intermediate values.

**Jump-divisor geometry.** In the polynomial ring \(k[a,b,c,d]\) the triangular automorphism \(z=c+3a^2\) carries \(Q\) to \(b^2+4az\). This nondegenerate ternary quadratic is absolutely irreducible: a product of two linear forms would have quadratic rank at most two, whereas its symmetric bilinear rank is three in characteristic five. Its gradient \((4z,2b,4a)\) vanishes precisely at \(a=b=z=0\). Therefore \(D\) is an integral hypersurface of dimension three, singular only on the line \(L\) (codimension two within \(D\)). Being a hypersurface, \(D\) satisfies Serre's \(S_2\); it is regular in codimension one and hence normal by \(R_1+S_2\). The transverse slice \(b^2+4az=0\) is the ordinary \(A_1\) rational double point, completing the geometric classification.

## Verification
The accompanying `verify_symbolic.py` (Python 3 with SymPy) independently performs exact coefficient extraction in characteristic five, checks all 100 Cartier-matrix entries, the determinant of \(P\), and the quadratic coordinate change. The separate `verify_finite.py` (Python 3 standard library) constructs the Cartier matrix by direct polynomial arithmetic and finite-field row reduction for all \(5^4=625\) coefficient tuples over \(\mathbb F_5\). It finds \(500\) cases of rank \(4\), \(120\) of rank \(3\), and \(5\) of rank zero, with no mismatches. **Only the symbolic argument proves the assertion over the entire algebraic closure.** Both scripts are included as standalone source files and were executed successfully.

## Relationship to prior work
Abney-McPeek, Berg, Booher and collaborators establish that the Booher–Cais minimal \(a\)-number bound is attained for one-pole covers in characteristic five, and give concrete binomial/trinomial witnesses. Their existence and minimality results imply generic \(a\)-number \(6\) for the present conductor but do not give the complete exceptional coefficient locus, the exclusion of values \(8,9\), or the normal \(A_1\) divisor geometry. Farnell and Pries provide general Cartier methods and constant-rank families; their congruence conditions do not classify this variable-rank conductor-six family. Zhou characterizes superspecial Artin–Schreier curves in a more general setting; the fact that the special line has maximal \(a\)-number is consistent with that earlier work and is not asserted as a new superspecial-isomorphism classification. The contribution is the **complete universal stratification and the geometry of its rank-jump divisor**, not the standard genus, \(5\)-rank, minimum bound, or superspecial existence.

## Limitations
This theorem classifies the Jacobian \(a\)-number, not the full Ekedahl–Oort type, Newton polygon, or isomorphism classes. It applies only to characteristic five and ramification conductor six, and the hypersurface is in coefficient space rather than a claimed coarse moduli space. An unindexed or inaccessible prior calculation with an equivalent universal divisor equation cannot be excluded by literature searching. Independent external mathematical audit has not been performed.

## References
1. F. Abney-McPeek, H. Berg, J. Booher et al., *Realizing Artin-Schreier Covers with Minimal \(a\)-numbers in Positive Characteristic*, arXiv:2003.09028, version 1 publicly posted 2020-03-19; sections 1, 4, 6, 7. https://arxiv.org/abs/2003.09028
2. S. Farnell and R. Pries, *Families of Artin-Schreier Curves with Cartier-Manin Matrix of Constant Rank*, arXiv:1202.4183, 2012; sections on the basis and Cartier matrix. https://arxiv.org/abs/1202.4183
3. H. Zhou, *On the Existence of Curves with Prescribed \(a\)-number*, arXiv:1901.08375, 2019; Artin–Schreier superspeciality theorem. https://arxiv.org/abs/1901.08375
