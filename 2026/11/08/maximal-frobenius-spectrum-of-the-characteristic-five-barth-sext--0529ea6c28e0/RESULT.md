# Maximal Frobenius spectrum of the characteristic-five Barth sextic

## Finding

Let \(k=\mathbb F_5\) and let \(X\subset\mathbb P^3_k\) be the coefficientwise reduction at the unique prime above five of the standard integral golden-ratio equation of the Barth sextic. Writing \(S=x^2+y^2+z^2\), its defining equation is

\[
F=(x^2+y^2)(y^2+z^2)(z^2+x^2)-2(S-w^2)^2w^2=0.
\]

The geometric singular locus consists of **exactly 65 distinct \(k\)-rational ordinary double points**, with 50 in \(w\ne0\) and 15 in \(w=0\). There are six orbits under permutations and independent sign changes of \(x,y,z\), of sizes \(6,24,12,8,3,12\). The surface has exactly \(91\) points over \(k\), of which \(26\) are smooth, and exactly \(1651\) points over \(\mathbb F_{25}\).

For **every integer \(n\ge1\)**,

\[
\#X(\mathbb F_{5^n})=1+5^{2n}+5^n\bigl(27+14(-1)^n\bigr).
\]

Consequently its Hasse–Weil zeta function is

\[
Z(X/k,T)=\frac{1}{(1-T)(1-25T)(1-5T)^{27}(1+5T)^{14}}.
\]

For the minimal resolution \(\pi:Y\to X\), the second étale cohomology has dimension \(106\) and geometric Frobenius eigenvalues \(+5\) with multiplicity \(92\) and \(-5\) with multiplicity \(14\). In particular, all its weight-two eigenvalues become \(25\) over \(\mathbb F_{25}\). Here Frobenius refers to the convention compatible with the displayed point-count trace formula.

## Assumptions and scope

All geometry is over \(\mathbb F_5\) and its algebraic closure, and all cohomology below is \(\ell\)-adic for a prime \(\ell\ne5\). Start with the classical equation

\[
4(\varphi^2x^2-y^2)(\varphi^2y^2-z^2)(\varphi^2z^2-x^2)
 -(1+2\varphi)(x^2+y^2+z^2-w^2)^2w^2,
\]

where \(\varphi^2=\varphi+1\). Its coefficient ring \(\mathbb Z[\varphi]\) has a unique prime above five and the image of \(\varphi\) there is \(3\); hence \(\varphi^2=4\) and \(1+2\varphi=2\). Substitution gives the equation in the Finding section, with no division by a multiple of five. This specifies the model: the statement is not about arbitrary characteristic-five models carrying the name Barth sextic.

## Proof

**1. Classify the singular points geometrically.** Put \(a=x^2\), \(b=y^2\), \(c=z^2\), \(d=w^2\), and \(S=a+b+c\). Direct differentiation modulo five gives

\[
F_x=2x\bigl((S-2d)^2-a^2\bigr),\quad
F_y=2y\bigl((S-2d)^2-b^2\bigr),\quad
F_z=2z\bigl((S-2d)^2-c^2\bigr),
\]
\[
F_w=-4w(S-3d)(S-d).
\]

Because the homogeneous degree is six, Euler's identity becomes \(F=\sum uF_u\) in characteristic five, so every common zero of the four partial derivatives lies on \(X\).

In the chart \(w=1\), the last derivative forces \(S=1\) or \(S=3\). In either case \((S-2)^2=1\), and each nonzero coordinate among \(x,y,z\) satisfies \(u^4=1\). All such coordinates therefore lie in \(\mathbb F_5\) and have square \(+1\) or \(-1\). Write \(p,m\) for the numbers of squared coordinates equal to \(+1,-1\), respectively. The equation \(p-m\equiv S\pmod5\), with \(p+m\le3\), gives exactly the following four types:

| Chart | \(p\) | \(m\) | Points | Representative |
| --- | ---: | ---: | ---: | --- |
| \(w=1\), \(S=1\) | 1 | 0 | 6 | \([1:0:0:1]\) |
| \(w=1\), \(S=1\) | 2 | 1 | 24 | \([1:1:2:1]\) |
| \(w=1\), \(S=3\) | 0 | 2 | 12 | \([2:2:0:1]\) |
| \(w=1\), \(S=3\) | 3 | 0 | 8 | \([1:1:1:1]\) |

The counts include the choices of positions and square roots. They sum to \(50\).

On \(w=0\), the value \(S\) cannot vanish at a projective singular point: otherwise the three displayed partial equations force \(a=b=c=0\). Over the algebraic closure, rescale so that \(S=1\). Every nonzero squared coordinate is then \(\pm1\), and the condition \(p-m=1\) forces exactly \((p,m)=(1,0)\) or \((2,1)\). Modulo common projective sign, these give respectively \(3\) and \(12\) points, represented by \([1:0:0:0]\) and \([1:1:2:0]\). They are all \(\mathbb F_5\)-rational, since both square roots of \(-1\) lie in \(\mathbb F_5\). Thus no geometric singularities outside the listed \(65\) exist.

**2. Check that every singularity is a node.** The equation is invariant under permutations and individual sign changes of \(x,y,z\). The six preceding classes are transitive under these symmetries. For each representative, compute the determinant of the \(3\times3\) Hessian in its displayed affine chart: use \(w=1\) for the four affine types and \(x=1\) for the two infinite types. In the order displayed above, the determinants modulo five are respectively \(1,1,4,4,4,4\), all nonzero. The standalone exact-arithmetic verifier derives the derivatives from the polynomial and checks all six matrices. Since the characteristic is not two, the singularities are ordinary quadratic nodes. A projective hypersurface with only isolated singularities cannot factor geometrically into positive-degree components, since two such components would meet along a curve. Hence \(X\) is geometrically integral.

**3. Determine the first two rational-point counts.** Exhaustively enumerate the disjoint canonical affine charts of \(\mathbb P^3(\mathbb F_q)\) for \(q=5,25\): one chart has three free coordinates, the next two, the next one, and the final chart only one point. For \(q=5\), evaluation of \(F\) yields \(91\) points (\(70\) with \(w\ne0\), \(21\) at infinity). Among them \(65\) are exactly the already classified nodes. The six affine square-pattern types on \(w=1\) have populations \(6,24,12,8,12,8\), where the last two are smooth. At infinity the smooth count is \(6\), giving \(26\) smooth \(\mathbb F_5\)-points.

For \(q=25\), take either \(\mathbb F_5[t]/(t^2-2)\) or \(\mathbb F_5[t]/(t^2-3)\). Both are fields because \(2\) and \(3\) are nonsquares. In each field, a complete enumeration of all \(25^3+25^2+25+1=16276\) projective points yields the same counts in the disjoint charts \(w=1\), \((w,z)=(0,1)\), \((w,z,y)=(0,0,1)\), and the remaining axis: \(1510,137,3,1\). Their sum is \(1651\). The included self-contained checker reproduces both enumerations. This is an exhaustive finite computation, not an extrapolation from sampled points.

**4. Pass to the smooth resolution.** Blow up the \(65\) distinct rational nodes to obtain the smooth projective minimal resolution \(Y\). Each exceptional curve is a smooth conic over a finite field, hence a projective line over \(\mathbb F_5\); replacing its singular rational point contributes exactly \(5^n\) extra points over \(\mathbb F_{5^n}\). Thus

\[
\#Y(\mathbb F_5)=91+65\cdot5=416,\qquad
\#Y(\mathbb F_{25})=1651+65\cdot25=3276.
\]

The nodes are rational double points, so \(R^1\pi_*\mathcal O_Y=0\), and \(K_Y=\pi^*\mathcal O_X(2)\). The hypersurface exact sequence gives \(h^1(\mathcal O_X)=0\); by Serre duality \(h^2(\mathcal O_Y)=h^0(\mathcal O_Y(K_Y))=h^0(\mathbb P^3,\mathcal O(2))=10\). Hence \(\chi(\mathcal O_Y)=11\) and \(K_Y^2=4\deg X=24\). Noether's formula gives \(c_2(Y)=12\cdot11-24=108\), equal to its \(\ell\)-adic Euler characteristic. Since \(h^1(\mathcal O_Y)=0\), the Albanese is trivial and the first \(\ell\)-adic Betti number vanishes. Poincaré duality then gives \(b_3=0\), so \(b_2=c_2-2=106\).

**5. Derive the entire Frobenius spectrum.** Let \(\alpha_1,\ldots,\alpha_{106}\) be the eigenvalues of geometric Frobenius on \(H^2_{\mathrm{\acute et}}(Y_{\overline k},\mathbb Q_\ell)\), under the point-count convention. The Weil bounds give \(|\alpha_j|=5\) for each complex embedding. The Lefschetz trace formula and the two exact counts yield

\[
\sum_j\alpha_j=416-1-25=390,
\qquad
\sum_j\alpha_j^2=3276-1-625=2650=106\cdot25.
\]

Equality in the triangle inequality for the latter sum forces \(\alpha_j^2=25\) for every \(j\). Thus each eigenvalue is \(+5\) or \(-5\). The first trace and total dimension force respective multiplicities \(92\) and \(14\). Consequently

\[
\#Y(\mathbb F_{5^n})=1+5^{2n}+5^n(92+14(-1)^n).
\]

Subtracting the \(65\cdot5^n\) exceptional-point correction proves the stated formula and zeta function for \(X\).

## Verification

The files `verify.py` and `verify_f125.cpp` are standalone exact-arithmetic checkers. The first constructs the defining polynomial and all first and second partial derivatives over \(\mathbb F_5\), tests the six orbit representatives and local Hessians, enumerates every projective point over \(\mathbb F_5\), and independently performs two exhaustive enumerations over \(\mathbb F_{25}\) using different nonsquare quadratic generators. The second uses \(\mathbb F_{125}=\mathbb F_5[t]/(t^3+t+1)\) to enumerate every projective point and independently checks the predicted \(\#X(\mathbb F_{125})=17251\). This third extension-degree check is not an input into the Frobenius-spectrum deduction.

The human-readable code outputs are included in `verification_results.txt`. All numerical assertions were checked on the packaged code, including the nonzero Hessian determinants. Only the finite enumerations are computational: the conclusions for all extension degrees rely on the cohomological argument above.

## Relationship to prior work

Barth's original sextic is the classical complex surface with \(65\) nodes. Its equation, the split \(50+15\) into affine and infinite nodes, and its icosahedral symmetry are classical. Jaffe–Ruberman prove the complex upper bound of \(65\) nodes, and the cited modern exposition reproduces the equation and geometric node distribution. The square-coordinate cover of a Cayley cubic is also noted in existing descriptions. These facts are not claimed as new.

The result isolated here is different: the **particular ramified characteristic-five fiber** retains exactly \(65\) distinct ordinary nodes, all defined over \(\mathbb F_5\), and its minimal resolution has the completely specified maximal two-step Frobenius spectrum and exact zeta function. The inspected accessible treatments of the complex sextic do not state these finite-field arithmetic assertions. The full original Barth paper and the body of Jaffe–Ruberman's old postscript were not accessible for complete-text comparison. No claim of exhaustive historical priority or independent validation is made.

## Limitations

The model is the coefficientwise reduction of the displayed integral golden-ratio equation. This result does not assert that every sextic with \(65\) nodes in characteristic five has the same zeta function, and it does not identify the Néron–Severi rank with the second Betti number: the Frobenius statement is cohomological. General characteristic-five bounds on the maximum possible number of nodes are not invoked. The two finite field counts and Hessian calculations have explicit reproducible finite certificates, while the infinite-extension formula uses standard theorems about rational double points, étale cohomology, and Weil weights.

## References

1. W. Barth, *Two projective surfaces with many nodes, admitting the symmetries of the icosahedron*, J. Algebraic Geometry 5 (1996), 173–186 (original construction; complete text not accessed).
2. D. B. Jaffe and D. Ruberman, *A sextic surface cannot have 66 nodes*, arXiv:alg-geom/9502001, submitted 1995-02-01, https://arxiv.org/abs/alg-geom/9502001 (abstract and distribution note accessed; main text inaccessible).
3. J. Baez, *Barth Sextic*, AMS Visual Insight, 2016-04-15, https://blogs.ams.org/visualinsight/2016/04/15/barth-sextic/ (complete relevant webpage read, classical formula and 50+15 count).
4. E. W. Weisstein, *Barth Sextic*, MathWorld, https://mathworld.wolfram.com/BarthSextic.html (complete article read; includes classical square-coordinate Cayley cubic relationship).
