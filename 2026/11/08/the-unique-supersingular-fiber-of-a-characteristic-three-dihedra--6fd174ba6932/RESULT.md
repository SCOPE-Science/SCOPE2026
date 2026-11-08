# The unique supersingular fiber of a characteristic-three dihedral genus-four family

## Finding

For an algebraically closed field \(k\) of characteristic \(3\), consider the smooth projective hyperelliptic curves
\[
C_a:\qquad y^2=x^{10}+a x^5+1,\qquad a\in k,\quad a^2\ne1.
\]
The entire smooth marked family has just two Newton polygons. If \(a\ne0\), the genus-four Jacobian \(J_a\) is ordinary: its \(3\)-rank is \(4\), its \(a\)-number is \(0\), and its Newton slopes are four \(0\)'s and four \(1\)'s. At \(a=0\), it has \(3\)-rank \(0\) and \(a\)-number \(2\), and it is supersingular but not superspecial: all eight Newton slopes equal \(1/2\). No other intermediate rank or slope type occurs in the smooth family.

The coefficient Hasse–Witt determinant, with the normalization below, is \(-a^2\); thus the Hasse nonordinary divisor on the smooth marked coefficient line has multiplicity exactly two at its unique support. Under the explicit parameter identification \(a\sim-a\), induced by \((x,y)\mapsto(-x,y)\), the invariant parameter \(u=a^2\) gives a simple equation \(u=0\) for the corresponding divisor on the quotient parameter line. This is a statement about the displayed parameter quotient, not a claimed complete coarse moduli classification.

For every \(q=3^n\) the number of smooth *marked coefficient values* over \(\mathbb F_q\) is \(q-2\); exactly one is supersingular and the remaining \(q-3\) are ordinary.

## Assumptions and scope

The field is algebraically closed of characteristic exactly \(3\) for the geometric conclusions. The coefficient parameter lies in \(k\setminus\{1,-1\}\); the curve means the smooth projective model of the displayed affine equation. The \(3\)-rank is the dimension over \(\mathbb F_3\) of geometric \(3\)-torsion of the Jacobian, and the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_3,J_a[3])\). Newton slopes are counted with multiplicity eight. Finite-field counts concern displayed marked equations, not geometric isomorphism classes.

## Proof

**Smoothness and genus.** Put \(f=x^{10}+a x^5+1\). In characteristic \(3\), \(f'=x^4(x^5-a)\). Since \(f(0)=1\), a common root of \(f,f'\) exists precisely when \(x^5=a\) and \(f(x)=2a^2+1=1-a^2=0\). Thus \(f\) is squarefree exactly for \(a^2\ne1\). Its degree ten gives genus four.

**Hasse–Witt and Cartier ranks.** In the standard basis \(x^{j-1}\,dx/y\), \(1\le j\le4\), the coefficient matrix for the characteristic-three Hasse–Witt/Cartier computation is \(H_{ij}=[x^{3i-j}]f\), namely
\[
H=\begin{pmatrix}
0&0&1&0\\
a&0&0&0\\
0&0&0&a\\
0&1&0&0
\end{pmatrix},\qquad \det H=-a^2.
\]
The actual Cartier matrix uses cubic roots of these entries, and has the same rank. For \(a\ne0\), \(H\) is invertible, so the curve is ordinary. For \(a=0\), the matrix has rank \(2\) and its semilinear square \(H H^{(3)}\) vanishes. Thus the stable Frobenius rank, hence \(3\)-rank, is zero, while the \(a\)-number is \(4-2=2\).

**The two genus-two quotients.** Let \(\iota:(x,y)\mapsto(x,-y)\), and define commuting involutions
\[
\tau_+:(x,y)\mapsto (x^{-1},y/x^5),\qquad
\tau_-:=\iota\tau_+:(x,y)\mapsto (x^{-1},-y/x^5).
\]
Set \(T=x+x^{-1}\), \(D_5(T)=T^5-5T^3+5T=x^5+x^{-5}\), and \(Y_\pm=y(x\pm1)/x^3\). The functions \(T,Y_\pm\) are invariant under \(\tau_\pm\), respectively, and satisfy
\[
B_\pm:\qquad Y_\pm^2=(T\pm2)(D_5(T)+a).
\]
The fixed points of \(\tau_+\) on the smooth curve are exactly the two points over \(x=1\); those of \(\tau_-\) are exactly the two over \(x=-1\) (the excluded \(a=\pm1\) ensure the branch values are nonzero). Riemann–Hurwitz for tame involutions gives genus two for both quotient curves. Because the invariant subfields each have degree two, \(B_\pm\) are their smooth projective models.

Write \(\pi_\pm:C_a\to B_\pm\) for the quotient maps. The induced map
\[
\Phi=\pi_+^*+\pi_-^*:\quad J(B_+)\times J(B_-)\longrightarrow J_a
\]
is an isogeny: the two differential eigenspaces of \(\tau_+\) are complementary and each has dimension two. For principal polarizations, the adjoint map has components the norms \(\pi_{\pm *}\). By the deck involutions and \(\tau_- =\iota\tau_+\), its cross terms are zero, and \(\pi_{\pm *}\pi_\pm^*=[2]\). Hence \(\Phi^\vee\Phi=[2]\times[2]\), so \(\deg\Phi=16\). The degree is prime to the characteristic, and the \(3\)-divisible group of \(J_a\) is consequently isomorphic, up to the induced prime-to-three isogeny, to the product of those of the two genus-two quotients.

At \(a=0\) the product has \(3\)-rank zero, so both genus-two factors have \(3\)-rank zero. In genus two, a \(3\)-rank-zero Newton polygon must be supersingular: all four slopes are \(1/2\) by the slope denominator/multiplicity restrictions and symmetry. Therefore both factors are supersingular and \(J_0\) has eight slopes \(1/2\). Its \(a\)-number is \(2<4\), so it is not superspecial.

**Multiplicity and counts.** The Hasse coefficient determinant \(-a^2\) has exactly order two at \(a=0\). The involution \((x,y)\mapsto(-x,y)\) identifies the coefficient curves at \(a\) and \(-a\); on the corresponding affine parameter quotient the invariant coordinate is \(u=a^2\), in which the determinant is \(-u\). Over \(\mathbb F_q\), the only excluded values are \(a=\pm1\), giving \(q-2\) smooth coefficients. Exactly \(a=0\) is supersingular, leaving \(q-3\) ordinary coefficients.

## Verification

Run \(\texttt{python3 verify.py}\) using the embedded standalone program. It verifies the Dickson-polynomial and genus-two quotient identities exactly over integers and checks the Hasse coefficient matrix, nilpotence at zero, smooth coefficient exclusions and arithmetic counts exhaustively over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\). The recorded output is included in \(\texttt{verification_output.txt}\). The infinite-field conclusion and supersingularity are proved above, not inferred from the finite samples.

## Relationship to prior work

Shaska (2003) develops the automorphism and normal-form viewpoint for hyperelliptic curves in characteristic zero, not the characteristic-three Newton stratification here. Moonen (2010) classifies special families of cyclic covers in characteristic zero; the degree-five signature \((1,1,4,4)\) of this family is distinct from his degree-five genus-four entry \((1,3,3,3)\). Li–Mantovan–Pries–Tang (2018) calculate Newton polygons for Moonen's special families, not the coefficientwise full stratification of this distinct reciprocal hyperelliptic family. Kudo–Harashita–Senda (2020) explicitly recall the known supersingular genus-four curve \(y^{10}=x(1-x)\), which over characteristic three becomes isomorphic after coordinate changes to the exceptional curve \(C_0\); **existence and supersingularity of that individual curve are not claimed new**. The contribution assessed here is the complete smooth one-parameter ordinary/supersingular boundary, the scheme multiplicity and parameter-quotient normalization, and its explicit genus-two quotient decomposition.

## Limitations

The coefficient parameter quotient \(u=a^2\) is not asserted to be the full geometric coarse moduli space. The result does not classify full automorphism groups, principal polarizations on the product factors, or stable limits at excluded parameters \(a=\pm1\). Historical priority remains provisional: a general older formula for Cartier–Manin matrices could make parts of the rank calculation routine, and an unindexed treatment of this exact genus-four family might already provide the complete statement. The finite-field tests do not independently establish infinite-field claims.

## References

1. T. Shaska, *Determining the Automorphism Group of a Hyperelliptic Curve*, arXiv:math/0312284, first arXiv posting 2003-12-15, https://arxiv.org/abs/math/0312284.
2. B. Moonen, *Special subvarieties arising from families of cyclic covers of the projective line*, arXiv:1006.3400, first posting 2010-06-17, https://arxiv.org/abs/1006.3400.
3. W. Li, E. Mantovan, R. Pries, Y. Tang, *Newton polygons arising from special families of cyclic covers of the projective line*, arXiv:1805.06914, first posting 2018-05-17, https://arxiv.org/abs/1805.06914.
4. M. Kudo, S. Harashita, H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, *Research in Number Theory* 6 (2020), article 44, https://doi.org/10.1007/s40993-020-00217-x.
