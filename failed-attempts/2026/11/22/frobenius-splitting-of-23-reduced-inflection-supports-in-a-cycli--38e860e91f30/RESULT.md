# Frobenius splitting of 23 reduced inflection supports in a cyclic-six quartic family

## Finding

Let \(k=\mathbb F_q\) have characteristic \(p\ge5\), and let
\[
C_r:\quad X^3Z+Y^4+rY^2Z^2+Z^4=0,
\qquad r\in k.
\]
Put \(D(r)=11r^4-1080r^2+3888\). If \(r(r^2-4)D(r)\ne0\), then the reduced geometric inflection-point locus \(W_r\) consists of exactly **23** points (of total inflection weight \(24\)): the rational hyperflex \([1:0:0]\), four ordinary flexes with \(X=0\), and eighteen ordinary flexes with \(XZ\ne0\).

The Frobenius permutation of all 23 points is determined, for every finite field and every admissible parameter, by factoring just
\[
f_r(U)=U^4+rU^2+1,
\qquad
\Phi_r(U)=2U^6+5rU^4+(18-r^2)U^2+3r.
\]
Every monic irreducible factor of \(f_r\) of degree \(d\) contributes one Frobenius orbit of degree \(d\). Every monic irreducible factor \(h\) of \(\Phi_r\) of degree \(e\) contributes the following orbits. Write \(L=k[U]/(h)\), \(u=U\bmod h\), and \(c=-(u^4+ru^2+1)\in L^\times\):

- If \(q^e\equiv2\pmod3\), contribute one orbit of degree \(e\) and one of degree \(2e\).
- If \(q^e\equiv1\pmod3\) and \(c^{(q^e-1)/3}=1\) in \(L\), contribute three orbits of degree \(e\).
- Otherwise, contribute one orbit of degree \(3e\).

Add the rational singleton \([1:0:0]\). Thus if \(m_d\) is the number of resulting degree-\(d\) orbits, the complete zeta function of this reduced zero-dimensional scheme is
\[
Z(W_r,T)=\prod_{d\ge1}(1-T^d)^{-m_d}.
\]
This is a classification of finite-field splitting for the whole stated open family, not a classification of the exceptional hyperflex-jump fibres.

For the four admissible parameters over \(\mathbb F_7\), the exhaustive table is:

| \(r\) | Frobenius cycle partition on \(W_r\) | Rational flex supports |
|---|---|---:|
| \(1\) | \(1^5 3^6\) | 5 |
| \(3\) | \(1^7 2^5 3^2\) | 7 |
| \(4\) | \(1^7 2^5 6\) | 7 |
| \(6\) | \(1\,2^2 6^3\) | 1 |

The curves at \(r=3\) and \(r=4=-3\) become isomorphic over \(\mathbb F_{49}\) by scaling the \(Y\)-coordinate by a square root of \(-1\); they are not isomorphic over \(\mathbb F_7\), as their intrinsic reduced inflection schemes have different Frobenius cycle partitions. They both have seven rational flex supports, yet
\[
Z(W_3,T)=\frac1{(1-T)^7(1-T^2)^5(1-T^3)^2},
\quad
Z(W_4,T)=\frac1{(1-T)^7(1-T^2)^5(1-T^6)}.
\]
In particular, the two curves have respectively 13 and 7 flex supports over \(\mathbb F_{7^3}\), despite having the same counts over \(\mathbb F_7\) and \(\mathbb F_{49}\).

## Assumptions and scope

All schemes, Frobenius actions and finite fields in the theorem are in characteristic at least five. The parameter \(r\) is coefficient-marked in the displayed normal form. The product \(r(r^2-4)D(r)\) is required to be nonzero in \(k\). These restrictions remove singular curves and the geometric hyperflex-jump fibres, ensuring a reduced support of size 23. The zeta function is that of the **reduced inflection-support scheme**, not the zeta function of the curve and not the weighted Weierstrass divisor. The characteristic-zero genus-three automorphism classification supplies context, but no characteristic-zero conclusion is substituted for the positive-characteristic proof.

## Proof

1. The curve is nonsingular precisely for \(r^2\ne4\), by its partial derivatives (equivalently, by the normal-form smoothness criterion). Its only point on \(Z=0\) is \(P_\infty=[1:0:0]\). The tangent line there is \(Z=0\), meeting the quartic to order four. In local coordinates \(X=1\), \(Y=t\), the equation gives \(Z=-t^4+O(t^6)\), and the Hessian restriction starts with \(-108t^2\); hence the inflection weight at \(P_\infty\) is exactly two.

2. In the affine chart \(Z=1\), write \(f_r(y)=y^4+ry^2+1\). The Hessian determinant of the homogeneous quartic is
\[
H=6XZ\big((12Y^2+2rZ^2)(2rY^2+12Z^2)-16r^2Y^2Z^2\big)-9X^4(12Y^2+2rZ^2).
\]
Substitution of \(x^3=-f_r(y)\) on the curve gives the exact identity
\[
H\big|_{C_r\cap\{Z=1\}}=54x\Phi_r(y).
\]
Since \(54\) is invertible in every characteristic under consideration, the affine flex locus is exactly the union of the four points \((0,y)\) with \(f_r(y)=0\) and the points satisfying \(\Phi_r(y)=0\), \(x^3=-f_r(y)\).

3. Set \(u=y^2\) and \(P_r(u)=2u^3+5ru^2+(18-r^2)u+3r\), so \(\Phi_r(y)=P_r(y^2)\). Direct polynomial identities over \(\mathbb Z[r]\) give
\[
\operatorname{disc}_u(P_r)=3(r^2-4)D(r),
\qquad
\operatorname{Res}_u(P_r,u^2+ru+1)=16(r^2-4)^2.
\]
Therefore \(P_r\) has three distinct nonzero geometric roots, because \(3r\ne0\); their square roots give six distinct \(y\)'s. For each, \(f_r(y)\ne0\), and \(x^3=-f_r(y)\) has three distinct geometric roots, giving eighteen distinct points. As \(x\ne0\), \(F_x=3x^2\ne0\), so \(y\) is a local parameter there. Since \(\Phi_r\) is squarefree, \(H\) has a simple zero and each point is an ordinary flex. At the four branch points \(x=0\), the smoothness of \(f_r\) makes \(x\) a local parameter, and the Hessian vanishes simply by the nonzero resultant above; these are also ordinary flexes. The weights total \(2+4+18=24\), agreeing with the canonical genus-three inflection divisor.

4. The rational point \(P_\infty\) is fixed by Frobenius. The four points at \(x=0\) have \(y\)-coordinates equal to the roots of the separable polynomial \(f_r\); their Frobenius cycles are precisely its irreducible-factor degrees. For a monic irreducible \(h\mid\Phi_r\) of degree \(e\), the \(e\) conjugate \(y\)-coordinates form a single Frobenius orbit; above each are three roots of \(x^3=c\) with \(c\ne0\). Over \(L=\mathbb F_{q^e}\), the third roots are three fixed roots if \(\mu_3\subset L\) and \(c\) is a cube; a three-cycle if \(\mu_3\subset L\) and \(c\) is a noncube; or a fixed root plus a transposed pair when \(\mu_3\not\subset L\). Translating these cycles for the \(q^e\)-Frobenius into cycles for the \(q\)-Frobenius multiplies their lengths by \(e\), giving the asserted rule. Its total number of geometric supports is always \(1+4+18=23\).

5. In characteristic seven, the admissible set is exactly \(\{1,3,4,6\}\). Factoring the two displayed polynomials and applying the cubic-root test produces the four table entries (complete arithmetic certificates and an independent direct field-point test are in `verify_flex.py`). For \(r\) and \(-r\), the transformation \(Y\mapsto iY\) with \(i^2=-1\) gives an isomorphism after adjoining \(i\), since \(i^4=1\). As \(-1\) is nonsquare in \(\mathbb F_7\), this is a quadratic extension. Different Frobenius actions on intrinsic flex loci rule out an \(\mathbb F_7\)-isomorphism of the two curves.

## Verification

Run `python verify_flex.py` with Python 3; it requires no third-party packages. The verifier factors both polynomials using exact finite-field division, checks the full \(\mathbb F_7\) parameter table and the 23-support degree sum, tests admissible parameters in characteristics \(5,7,11,13,17,19\), and independently enumerates the curve–Hessian intersection over \(\mathbb F_7\), \(\mathbb F_{49}\), and \(\mathbb F_{343}\) for the twist pair. The expected terminal line is `CYCLIC_SIX_QUARTIC_FLEX_FROBENIUS_VERIFIED`. Polynomial identities in Step 3 can also be checked directly by symbolic integer expansion; the all-field assertion follows from the algebraic proof, not from these finite examples.

## Relationship to prior work

Ohashi–Kudo–Harashita, arXiv:2111.09777 (first public 2021-11-18), establish the cyclic-six canonical model, the geometric isomorphism criterion \(r^2=s^2\), and Cartier/\(p\)-rank strata. They do not give finite-field Frobenius cycles on reduced flex supports. Kulikov, arXiv:1703.10430 (2017), proves generic full monodromy for the inflection points of plane curves of degree at least four; it does not supply the arithmetic splitting for this special automorphism pencil. Previously available geometric calculations of the same pencil identify the hyperflex-jump polynomial \(D(r)\), including its characteristic-eleven degeneration. The present result uses precisely the complementary open set where that polynomial does not vanish; its contribution is **all** Frobenius orbits and reduced-flex zeta functions, including a twist separation that geometric hyperflex counts do not imply. These earlier mathematical inputs are credited, not re-asserted as discoveries.

## Limitations

The singular parameters \(r=\pm2\), the enhanced-automorphism member \(r=0\), and the exceptional hyperflex-jump parameters \(D(r)=0\) are excluded. The result classifies the reduced flex locus, not its scheme-theoretic multiplicities outside the generic range, the curve's Weil polynomial, or the Jacobian isogeny type. Although the exact cycle rule works for all prime powers of characteristic at least five, only selected finite fields were computationally checked. Unindexed equivalent arithmetic flex calculations remain a historical-priority risk; mathematical novelty is a best-knowledge assessment, not a formal uniqueness certificate.

## References

- R. Ohashi, M. Kudo, S. Harashita, *The a-numbers of non-hyperelliptic curves of genus three with large cyclic automorphism group*, arXiv:2111.09777, initial version 2021-11-18, https://arxiv.org/abs/2111.09777.
- V. S. Kulikov, *On the monodromy of the inflection points of plane curves*, arXiv:1703.10430, initial version 2017-03-30, https://arxiv.org/abs/1703.10430.
- Related established geometric hyperflex-jump classification in the cyclic-six quartic pencil, public published-finding corpus records dated 2026-11-02 and 2026-11-08 (precise claim comparisons in `AUDIT.json`).
