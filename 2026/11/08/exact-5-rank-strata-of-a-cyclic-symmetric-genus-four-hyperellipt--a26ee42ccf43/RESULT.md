# Exact \(5\)-rank strata of a cyclic-symmetric genus-four hyperelliptic family

## Finding

Let \(k=\overline{\mathbb F}_5\). For \(a,b\in k\), write \(H_{a,b}\) for the smooth projective model of
\[
 y^2=x^{10}+x^7+ax^4+bx.
\]
Put
\[
 \Delta=a^3+a^2+3ab+3b^2+b,\quad
 w=a^2+2b,\quad
 \lambda=(2a+1)^5b^2+2(2a+2b)^5.
\]
All expressions and equalities of parameters are in characteristic five. The model has genus four exactly in the smooth parameter locus \(S=\{(a,b):b\Delta\ne0\}\). For every point of \(S\), the Jacobian's \(5\)-rank and the curve's Cartier \(a\)-number are, respectively,
\[
 f_5(H_{a,b})=2\mathbf1_{\lambda\ne0}+\mathbf1_{w\ne0},
 \qquad a(H_{a,b})=1+\mathbf1_{w=0}.
\]
In particular, every curve in this characteristic-five family is nonordinary, its \(a\)-number is either one or two, and every \(5\)-rank from zero through three occurs. The entire smooth \(5\)-rank-zero parameter locus is the single **reduced** point
\[
 (a,b)=(-1,2)=(4,2)\in\mathbb F_5^2.
\]
These statements count parameter pairs, not geometric isomorphism classes; \(5\)-rank zero is not asserted to imply supersingularity of the Jacobian.

The four strata are nonempty already over \(\mathbb F_5\): examples at ranks \(0,1,2,3\) are, respectively, \((a,b)=(4,2),(0,1),(1,2),(0,2)\). Their \(a\)-numbers are \(2,1,2,1\). Over \(\mathbb F_5\) itself, there are, respectively, \(1,2,2,12\) smooth coefficient pairs of these four ranks.

## Assumptions and scope

The base field \(k\) is the **entire algebraic closure** of \(\mathbb F_5\); no finite-field rationality assumption is imposed on \(a,b\). All curves are smooth, geometrically connected, and defined by the normalization of the displayed hyperelliptic equation. The \(5\)-rank \(f_5\) means the integer with \(\#\operatorname{Jac}(H)[5](k)=5^{f_5}\). The \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_5,\operatorname{Jac}(H)[5])\), equivalently the genus minus the rank of the Cartier operator on regular differentials.

The coefficient normalization is part of the claim: the unique zero-rank result is for this two-parameter equation, not for every genus-four hyperelliptic curve, and not a claim of one geometric isomorphism class among all such curves.

## Proof

**1. Smoothness and genus.** Set \(t=x^3\) and \(g(t)=t^3+t^2+at+b\), so that \(x^{10}+x^7+ax^4+bx=xg(x^3)\). In characteristic five, the map \(x\mapsto x^3\) is separable off zero. Thus the degree-ten right side has ten distinct roots if and only if \(b\ne0\) and \(g\) has three distinct roots. Its cubic discriminant is
\[
 \operatorname{disc}(g)=a^2-4a^3-4b-27b^2+18ab
                  =a^3+a^2+3ab+3b^2+b=\Delta
\]
in \(k\). The smooth double cover of \(\mathbb P^1\), branched at these ten roots, has genus \((10-2)/2=4\) by Riemann--Hurwitz. If \(b\Delta=0\), the displayed branch polynomial is not squarefree and does not yield a smooth genus-four curve of the claimed form.

**2. Cartier operator.** A basis of \(H^0(H_{a,b},\Omega^1)\) is \(\omega_j=x^{j-1}dx/y\), \(1\le j\le4\). Write \(f(x)^2=\sum_r c_r x^r\). The Cartier operator is \(5^{-1}\)-semilinear and satisfies
\[
 \mathscr C(\omega_j)=\sum_{i=1}^4 c_{5i-j}^{1/5}\omega_i.
\]
Exact expansion of the four-term polynomial gives the coefficient matrix
\[
 B=(c_{5i-j})_{i,j=1}^4=
 \begin{pmatrix}
 0&0&b^2&0\\
 0&w&0&0\\
 u&0&0&v\\
 0&0&2&0
 \end{pmatrix},
 \qquad u=2a+1,\quad v=2a+2b.
\]
This formula requires **no** assumption that the parameter coefficients are fixed by fifth-power Frobenius. In particular, using an untwisted square of \(B\) would not establish a universal \(5\)-rank formula over \(k\).

**3. The \(a\)-number.** The first and fourth rows of \(B\) span one nonzero row direction. The third row is another independent direction unless \(u=v=0\). The equations \(u=v=0\) give \((a,b)=(2,3)\); there \(\Delta=0\), so this point is excluded from \(S\). The second row contributes precisely when \(w\ne0\). Therefore \(\operatorname{rank}B=2+\mathbf1_{w\ne0}\) on \(S\), proving \(a(H)=4-\operatorname{rank}B=1+\mathbf1_{w=0}\).

**4. Stable Cartier rank, hence \(5\)-rank.** The operator preserves the decomposition \(\langle\omega_2\rangle\oplus P\), where \(P=\langle\omega_1,\omega_3,\omega_4\rangle\). On the first summand, \(\mathscr C(\omega_2)=w^{1/5}\omega_2\); its stable image has dimension one if \(w\ne0\), and zero otherwise.

On \(P\),
\[
 \mathscr C(\omega_1)=u^{1/5}\omega_3,\quad
 \mathscr C(\omega_4)=v^{1/5}\omega_3,\quad
 \mathscr C(\omega_3)=\eta:=b^{2/5}\omega_1+2\omega_4.
\]
Another application, **including the semilinear coefficient twist**, gives
\[
 \mathscr C(\eta)=\bigl(b^{2/25}u^{1/5}+2v^{1/5}\bigr)\omega_3
 =\lambda^{1/25}\omega_3.
\]
Since \((u,v)\ne(0,0)\) on \(S\), the first image of \(P\) is exactly \(\langle\omega_3,\eta\rangle\), of dimension two. If \(\lambda\ne0\), Cartier permutes these two lines nontrivially (semilinearly), so this two-dimensional image is stable and invertible. If \(\lambda=0\), Cartier kills \(\eta\) and then all of \(P\) after at most three iterations. Hence the stable Cartier rank on \(P\) is \(2\) or \(0\), according as \(\lambda\ne0\) or \(\lambda=0\). The stable Cartier rank equals the \(5\)-rank of the Jacobian; summing the invariant summands yields the formula in the Finding.

**5. Unique reduced rank-zero point.** Both summands must have stable rank zero, so \(w=\lambda=0\). From \(w=0\), necessarily \(b=2a^2\) in characteristic five. Direct polynomial reduction gives
\[
 \Delta(a,2a^2)=2a^2(a-2)^2,
 \qquad
 \lambda(a,2a^2)=-2a^4(a+1)(a-2)^5.
\]
Smoothness excludes \(a=0\) and \(a=2\), leaving only \(a=-1\) and \(b=2\). At this point \(\Delta=3\ne0\). The surviving factor \(a+1\) appears to the first power, and \(\partial w/\partial b=2\ne0\); thus the intersection \(V(w,\lambda)\cap S\) is reduced, not merely set-theoretically a singleton. In fact, its Jacobian determinant in parameters \((a,b)\) equals \(3\in\mathbb F_5^\times\) at \((-1,2)\).

The other ranks occur at the explicit smooth witnesses stated above. The additional \(\mathbb F_5\) coefficient-pair census is a finite enumeration of the 25 pairs using the proved formulas and the displayed smoothness test; it is not used for the geometric universal result.

**6. Geometric context.** The order-three symmetry \((x,y)\mapsto(\zeta_3x,\zeta_3^2y)\) has genus-one quotient
\[
 E_{a,b}:\quad Y^2=X(X^3+X^2+aX+b),\quad X=x^3,\quad Y=xy.
\]
Its degree-four branch polynomial has Hasse invariant \(w=a^2+2b\), the coefficient of \(X^4\) in \((X^4+X^3+aX^2+bX)^2\). Thus the one-dimensional Cartier summand in the proof is the expected elliptic contribution; the complementary block has stable rank exactly zero or two. This explains why the four ranks occur in the specific two-component pattern above, rather than merely being numerical accidents.

## Verification

Execute `python3 verify_cartier_rank.py` with SymPy. It independently expands \(f^2\), verifies the coefficient matrix, the cubic discriminant, the semilinear \(\lambda\) polynomial and both rank-zero elimination identities. It checks the singularity of the sole potential \(a\)-number-three coefficient pair and exhausts all \(25\) rational parameter pairs. The exact success tag is `GENUS4_P5_CARTIER_PASS`.

Execute `python3 verify_point_counts.py` with Python's standard library. It constructs \(\mathbb F_{5^n}\) explicitly for \(n=1,2,3,4\) using irreducible polynomials, counts points on each of the four displayed witness curves, reconstructs the first four reduced zeta-numerator coefficients by Newton identities, and independently obtains the four asserted \(5\)-ranks. The exact success tag is `GENUS4_P5_POINTCOUNTS_PASS`. These finite-field checks support the examples but do not replace the semilinear proof over \(\overline{\mathbb F}_5\).

## Relationship to prior work

Kudo, Nakagawa and Takagi introduced and studied the same normalized family for superspecial genus-four hyperelliptic curves with order-six automorphisms. Their analysis, in particular the cyclic-character bound \(\operatorname{rank}\mathscr C\le3\) when \(p\equiv2\pmod3\), explains the already known universal nonordinarity mechanism. Their stated main calculation and enumeration concern \(p\ge7\), and do not give the characteristic-five full \(a\)-number/\(5\)-rank stratification or the unique smooth rank-zero parameter. Neither the family itself nor nonordinarity is claimed as new.

Frei's earlier work proves the absence of smooth genus-four hyperelliptic curves with \(a\)-number three in characteristic five; that general prohibition is likewise not claimed as new. The separate new point here is the complete, coefficient-explicit stable Cartier-rank stratification on the characteristic-five specialization of the cyclic-symmetric family, including a reduced unique zero-rank parameter and the other three nonempty ranks. General moduli results on cyclic-cover rank strata establish existence/dimensional statements, not these exact normalized coefficient equations and their unique intersection.

## Limitations

All counts concern the displayed normalized equation. Isomorphic curves can be represented by different coefficient pairs, so no geometric isomorphism-class count is asserted. \(5\)-rank zero is not equivalent to supersingular or superspecial, and the Newton polygons are not determined. The work does not classify every hyperelliptic genus-four curve or all order-six-symmetric families in characteristic five. Historical-priority risk remains for unindexed or differently normalized calculations. Independent mathematical audit has not been performed.

## References

- M. Kudo, T. Nakagawa and T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing \(\mathbb Z_6\)*, arXiv:2210.14822v1 (first public version 2022-10-26), §§2.2–2.3, 3.0–3.2. https://arxiv.org/html/2210.14822v1
- S. Frei, *The \(a\)-number of hyperelliptic curves*, arXiv:1703.03516 (2017), §4.2. https://arxiv.org/abs/1703.03516
- *The boundary of the \(p\)-rank \(0\) stratum of the moduli space of cyclic covers of the projective line*, *Nagoya Mathematical Journal* **248** (2022), 865–887. https://doi.org/10.1017/nmj.2022.12
