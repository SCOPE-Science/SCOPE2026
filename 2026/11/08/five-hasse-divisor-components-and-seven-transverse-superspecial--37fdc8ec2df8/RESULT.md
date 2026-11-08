# Five Hasse-divisor components and seven transverse superspecial parameters for a characteristic-seven Ciani quartic family

## Finding
Let \(k=\overline{\mathbb F}_7\). On the smooth parameter surface
\[
U=\{(a,b)\in k^2:a\ne\pm2,\ b\ne\pm2,\ a\ne b^2-2\},
\]
consider the smooth, nonhyperelliptic genus-three curves
\[
C_{a,b}:X^4+Y^4+Z^4+aX^2Y^2+b(X^2+Y^2)Z^2=0.
\]
Put \(v=b^2\), \(L=(3v+4)a+4v+1\), and set
\[
\lambda=2b(a-2)^2L,\qquad
\mu=4(v-2a)(a+v+1)(a-2v-1)
\]
in characteristic seven. The Hasse--Witt matrix in a canonical monomial basis is diagonal with entries \((\lambda,\lambda,\mu)\). Thus the geometric Jacobian \(7\)-rank \(f\) and Cartier \(a\)-number \(\alpha\) obey
\[
(f,\alpha)=\bigl(2\mathbf1_{\lambda\ne0}+\mathbf1_{\mu\ne0},\ 2\mathbf1_{\lambda=0}+\mathbf1_{\mu=0}\bigr).
\]
The nonordinary locus in \(U\), with its reduced structure, is a simple-normal-crossings divisor with **five irreducible smooth components**: \(b=0\), \(L=0\), \(a=v/2\), \(a=-v-1\), and \(a=2v+1\). It has exactly **seven** singular points, all ordinary transverse intersections of its \(\lambda\)- and \(\mu\)-components, precisely
\[
(a,b)=(0,0),(1,0),(-1,0),\quad
(a,b)=(4,\pm3),\quad
(a,b)=(3,\pm\sqrt{-1}).
\]
These, and only these, are the superspecial coefficient parameters. All seven are defined over \(\mathbb F_{49}\).

Among the \(2163\) smooth ordered coefficient pairs \((a,b)\in\mathbb F_{49}^2\), the complete distribution is

| Jacobian \((7\text{-rank},a\text{-number})\) | Number of coefficient pairs |
| --- | ---: |
| \((0,3)\) | 7 |
| \((1,2)\) | 84 |
| \((2,1)\) | 128 |
| \((3,0)\) | 1944 |

## Assumptions and scope
All geometric statements are over \(\overline{\mathbb F}_7\). Parameter pairs are ordered coefficients in the displayed fixed equation, **not** distinct geometric isomorphism classes. The count over \(\mathbb F_{49}\) is for the same fixed normal form. A genus-three Jacobian is called superspecial exactly when its Cartier \(a\)-number is three. The nonordinary divisor means the *reduced* zero locus of the Hasse determinant in \(U\), not a claim about the scheme multiplicity of that determinant.

## Proof
**Smoothness and genus.** For the general Ciani quartic \(X^4+Y^4+Z^4+rX^2Y^2+sY^2Z^2+tZ^2X^2\), the Jacobian criterion gives smoothness precisely when \(r,s,t\ne\pm2\) and \(r^2+s^2+t^2-rst-4\ne0\). Taking \((r,s,t)=(a,b,b)\), the last expression factors as \((a-2)(a-b^2+2)\). This is exactly the stated domain \(U\). Every smooth plane quartic is nonhyperelliptic of genus three.

**Frobenius calculation.** Put \(R=X^2,S=Y^2,T=Z^2\) and \(Q=R^2+S^2+T^2+aRS+bRT+bST\). In the standard \(X,Y,Z\) monomial basis for plane-quartic Hasse--Witt coefficient extraction, the diagonal entries are the coefficients of \(X^{12}Y^6Z^6\), \(X^6Y^{12}Z^6\), and \(X^6Y^6Z^{12}\) in \(F^6\), where \(F=Q(X^2,Y^2,Z^2)\). Every off-diagonal target has at least one odd exponent and is zero, since \(F\) is even in each coordinate. Symmetry gives the first two entries equal. Thus, in terms of \(Q^6\), they are \([R^6S^3T^3]Q^6\) and \([R^3S^3T^6]Q^6\).

Independently, the three involution quotients have (after completing squares) elliptic quartic models with coefficient triples
\[
(A,C,B),\ (A,C,B),\ (B,D,B),
\]
where \(A=a^2-4\), \(B=b^2-4\), \(C=2b(a-2)\), and \(D=2(b^2-2a)\). The characteristic-seven elliptic Hasse coefficient of \(w^2=Ax^4+Cx^2+B\) is
\[
[x^6](Ax^4+Cx^2+B)^3=C^3+6ABC.
\]
Exact multinomial expansion of \(Q^6\) produces the same three quantities \(C(C^2+6AB),C(C^2+6AB),D(D^2+6B^2)\). Their factorizations modulo seven are exactly \(\lambda,\lambda,\mu\) above. The two independently calculated forms are compared by `verify_plane.py` and `verify_geometry.py`.

Because the matrix is diagonal, every Frobenius iterate remains diagonal, with a diagonal entry zero exactly when the original entry is zero. Hence the stable Frobenius rank, which is the geometric \(7\)-rank, is the number of nonzero entries. The Cartier \(a\)-number is three minus the rank of this Hasse--Witt matrix, giving the displayed formula.

**Divisor components and intersections.** On \(U\), the factor \(a-2\) never vanishes. Therefore \(\lambda=0\) consists of \(b=0\) and \(L=0\). The latter is irreducible and smooth because its coefficient \(3b^2+4\) in \(a\) cannot vanish simultaneously with its constant term \(4b^2+1\). These two curves do not meet on \(U\): setting \(b=0\) in \(L\) forces \(a=-2\), excluded. The factorization of \(\mu\) gives three smooth graphs \(a=v/2\), \(a=-v-1\), \(a=2v+1\), each irreducible. Any two of the three graphs meet only at \(v=4\), excluded by \(b\ne\pm2\).

The intersections with the \(b=0\) component are \(a=0,-1,1\). For the other component \(L=0\), substituting the three graph equations and multiplying by units gives, respectively, polynomials proportional to
\[
(v-4)(v-6),\quad (v-4)(v-2),\quad(v-4)^2.
\]
Since \(v=4\) is excluded, there are just the two geometric roots \(b^2=6\) with \(a=3\) and the two roots \(b^2=2\) with \(a=4\). Direct substitution into the defining nonvanishing conditions of \(U\) verifies that these four and the three points at \(b=0\) are smooth parameters. At \(b=0\) the two crossing components have independent tangent directions; at \(v=2,6\), both nonzero, the displayed factors have simple roots and \(dv/db=2b\ne0\), so all seven intersections are transverse. There are no other intersections. Thus the reduced nonordinary divisor has exactly five smooth irreducible components and seven ordinary nodes.

**Exact finite-field counts.** Every nonzero element of \(\mathbb F_7\) is a square in \(\mathbb F_{49}\), so all seven intersection points lie in that field. There are \(49^2\) raw coefficient pairs. Removing \(a=\pm2\) and \(b=\pm2\) leaves \(47^2=2209\); removing \(a=b^2-2\) for the \(46\) remaining \(b\)-values other than \(0,\pm2\) gives \(2163\).

In \(U(\mathbb F_{49})\), the curve \(b=0\) has \(47\) points, and \(L=0\) has \(44\): it has exactly one permitted \(a\) for each \(b\) with \(b^2\notin\{0,1,4\}\). Thus \(\#\{\lambda=0\}=91\). The three disjoint \(\mu\)-components each have \(45\) points, since on each graph exactly four \(b\)-values are excluded, giving \(\#\{\mu=0\}=135\). Their intersection consists of the seven already proved points. Inclusion--exclusion yields \(7\), \(91-7=84\), \(135-7=128\), and \(2163-91-135+7=1944\). The independent exhaustive finite-field program `verify_geometry.py` reproduces all four counts.

## Verification
Run `python3 verify_plane.py` and `python3 verify_geometry.py` using Python 3 without external packages. The former constructs \(F^6\) termwise and verifies all three symbolic Hasse entries against independent elliptic-quotient coefficient formulas. The latter independently implements \(\mathbb F_{49}=\mathbb F_7[t]/(t^2+1)\), exhausts all \(2401\) parameter pairs, checks the two factorizations, domain exclusions, four rank strata and all seven nonzero transversality determinants. The scripts completed successfully with outputs `PASS`; their computations are checks of the explicit proof, not the only justification for claims over the algebraic closure.

## Relationship to prior work
Ohashi's Ciani-curve paper (arXiv:2201.12996, first public January 31, 2022), especially Lemma 2.1 and Section 3, establishes the general smoothness criterion, involution elliptic quotients, prime-to-characteristic isogeny, and superspeciality criterion. Those facts are prior work. Moriya and Kudo (arXiv:2209.02926, September 7, 2022), Section 5.3, give algorithms and counts of isomorphism classes of superspecial nonhyperelliptic Howe curves for characteristics beginning at eleven. Ohashi and collaborators (arXiv:2401.10500; 2025 article) provide broader genus-three isomorphism-class enumerations. The present *coefficient-space p-rank divisor decomposition, five-component normal-crossings geometry, seven transverse points, and complete \(\mathbb F_{49}\) coefficient distribution* are not asserted in those inspected materials. A general algorithm or isomorphism-class table is not equivalent to these parameter-divisor statements without a further specialization and incidence calculation.

## Limitations
This is the particular two-parameter \(D_8\)-symmetric Ciani subfamily in characteristic seven. We do not count distinct curves up to projective or abstract isomorphism; different coefficient pairs may represent the same curve. We do not classify all Ciani quartics in three parameters, other characteristics, full Newton polygons, or finer Ekedahl--Oort strata. The reduced normal-crossings statement is not a claim that the unreduced Hasse-determinant divisor has simple multiplicity: the determinant includes \(\lambda^2\). A prior unindexed equivalent coefficient calculation remains a historical-priority risk.

## References
1. R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996 (first public 2022-01-31), especially Sections 2--4; https://arxiv.org/abs/2201.12996.
2. T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926 (first public 2022-09-07), especially Section 5.3; https://arxiv.org/abs/2209.02926.
3. R. Ohashi, H. Onuki, M. Kudo, R. Yoshizumi and K. Nuida, *Listing superspecial curves of genus three by using Richelot isogeny graph*, arXiv:2401.10500 (first public 2024-01-19), https://arxiv.org/abs/2401.10500.
