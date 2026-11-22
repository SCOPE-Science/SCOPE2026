# The first mixed two-torsion isogeny classes in the dihedral genus-two family

## Finding
For each odd prime power \(q\equiv1\pmod4\), consider the coefficient-marked smooth genus-two curves
\[
C_{s,c}:\quad y^2=c(x^2+1)(x^4+s x^2+1),\qquad s\in\mathbb F_q\setminus\{2,-2\},
\]
where \(c\) represents one of the two square classes in \(\mathbb F_q^\times\). Among the \(q-2\) admissible parameters for either square class, exactly \((q-5)/4\) have \(\#\operatorname{Jac}(C_{s,c})[2](\mathbb F_q)=16\); the other \(3(q-1)/4\) have \(\#\operatorname{Jac}(C_{s,c})[2](\mathbb F_q)=4\).

Among *prime* fields \(\mathbb F_p\) with \(p\equiv1\pmod4\), the smallest characteristic in which this family contains two Jacobian-isogenous members with different rational two-torsion orders is \(p=13\). Indeed, over \(\mathbb F_{13}\), the curves
\[
C_{0,1}:y^2=(x^2+1)(x^4+1),\qquad C_{1,1}:y^2=(x^2+1)(x^4+x^2+1)
\]
have identical Weil numerators \((1+2T+13T^2)^2\), but the orders of their rational Jacobian two-torsion are respectively \(4\) and \(16\). Hence they are nonisomorphic over \(\mathbb F_{13}\) despite having isogenous Jacobians. Their full zeta functions coincide over all finite extensions.

More precisely, the eleven smooth unit-square-class parameters over \(\mathbb F_{13}\) have the following elliptic Frobenius trace \(t\), two-torsion order \(j_2\), and rational-point count \(N_1\); each entire genus-two Weil numerator is \((1-tT+13T^2)^2\):

| \(s\) | \(t\) | \(j_2\) | \(N_1\) |
|---:|---:|---:|---:|
| 0 | -2 | 4 | 18 |
| 1 | -2 | 16 | 18 |
| 3 | 2 | 4 | 10 |
| 4 | -6 | 4 | 26 |
| 5 | -6 | 4 | 26 |
| 6 | -2 | 4 | 18 |
| 7 | 0 | 4 | 14 |
| 8 | 4 | 4 | 6 |
| 9 | 2 | 4 | 10 |
| 10 | -4 | 4 | 22 |
| 12 | 2 | 16 | 10 |

Quadratic twisting reverses \(t\) and preserves \(j_2\). Thus the complete twenty-two coefficient-marked members have precisely the seven Frobenius traces \(-6,-4,-2,0,2,4,6\), with respective frequencies \(2,2,6,2,6,2,2\). Exactly the classes with \(t=\pm2\) mix two members with full rational Jacobian two-torsion and four with order-four rational two-torsion. These are counts of displayed coefficient-marked equations, not counts of unmarked geometric or arithmetic isomorphism classes.

## Assumptions and scope
All curves are understood as smooth projective models over the specified finite fields. The coefficient \(c\) is nonzero, with one chosen representative of each quadratic square class; its actual representative has no effect on trace sign or two-torsion. The requirement \(q\equiv1\pmod4\) ensures \(-1\) is a square. The characteristic is odd. The excluded parameters \(s=\pm2\) are precisely the singular sextic models. The minimum-prime claim ranges only over prime numbers congruent to one modulo four, not arbitrary prime powers.

## Proof
Write \(f_s(x)=(x^2+1)(x^4+s x^2+1)\). When \(s\notin\{\pm2\}\), the two factors are coprime and squarefree: the quartic derivative has a common root with the quartic only if \(s^2=4\); a common root with the quadratic requires \(s=2\). Consequently the hyperelliptic model is smooth and has genus two.

The established dihedral elliptic-quotient decomposition gives
\[
\operatorname{Jac}(C_{s,c})\sim_{\mathbb F_q}E_{s,c}^2,\qquad
E_{s,c}:v^2=c(u+1)(u^2+s u+1).
\]
This is the isogeny of Arul–Booher–Groen–Howe–Li–Matei–Pries–Springer, Proposition 2.8 (cited below), not a newly asserted general decomposition. In particular, if
\[
t_{s,c}=-\sum_{u\in\mathbb F_q}\chi\bigl(c(u+1)(u^2+s u+1)\bigr),
\]
where \(\chi\) is the quadratic character with \(\chi(0)=0\), the full Weil numerator is \((1-t_{s,c}T+qT^2)^2\).

The six geometric Weierstrass points are the distinct roots of \(f_s\). The two roots of \(x^2+1\) are rational. The quartic either splits completely or factors as two irreducible quadratics over \(\mathbb F_q\): to see the latter dichotomy, first suppose \(s^2-4\) is a square, so \(x^4+s x^2+1=(x^2-\alpha)(x^2-\alpha^{-1})\) for \(\alpha\in\mathbb F_q^\times\). The two values have the same quadratic character, and both quadratic factors split or neither does. If \(s^2-4\) is nonsquare, exactly one of \(2-s\) and \(-2-s\) is a nonzero square. For the corresponding \(\varepsilon\in\{1,-1\}\), take \(a^2=2\varepsilon-s\) to obtain
\[
x^4+s x^2+1=(x^2+a x+\varepsilon)(x^2-a x+\varepsilon).
\]
Neither quadratic can have rational roots, since any rational quartic root would force \(s^2-4\) to be a square. Thus the Frobenius cycle types on the six roots are only \(1^6\) and \(1^2 2^2\).

For genus two, geometric Jacobian two-torsion consists of even subsets of the six Weierstrass roots modulo complementation. Fixing all six gives \(16\) rational classes. For the permutation of type \(1^2 2^2\), the only rational classes are the zero class and the classes represented by the three pairs consisting of the two fixed roots or either of the two transposed pairs, giving \(4\) classes.

Complete splitting of the quartic is equivalent to the existence of \(w\in(\mathbb F_q^\times)^2\setminus\{1,-1\}\) with \(s=-(w+w^{-1})\). Because \(q\equiv1\pmod4\), both \(1\) and \(-1\) are squares, so inversion acts freely on the remaining \((q-1)/2-2\) squares. There are exactly \((q-5)/4\) distinct parameters \(s\) with complete splitting, and the complement has \((q-2)-(q-5)/4=3(q-1)/4\) parameters. Quadratic twisting changes none of these branch points.

For \(q=13\), the finite table in Finding follows by direct evaluation of the thirteen-term elliptic character sum. Alternatively, for \(c=1\) the genus-two affine character sum \(S_s=\sum_x\chi(f_s(x))\) gives \(\#C_{s,1}(\mathbb F_{13})=15+S_s\), using two rational points at infinity, and hence \(t=(-1-S_s)/2\). Both calculations are reproduced by the standalone verifier and agree in all eleven cases. The only fully split parameters are \(s=1,12\): the corresponding quartics have respectively four roots \(\{3,4,9,10\}\) and \(\{2,6,7,11\}\). The nonsplit quartic at \(s=0\) has no rational root, but factors into two irreducible quadratics; the two rational roots of \(x^2+1\) persist.

At \(p=5\), the only permitted parameters are \(s=0,1,4\), each with a quartic consisting of two irreducible quadratic factors and hence rational Jacobian two-torsion of order four. The only primes \(p\equiv1\pmod4\) below thirteen consist of five. For \(p=13\), parameters \(s=0\) and \(s=1\) have equal \(t=-2\) but different \(j_2\), proving the sharp minimum. Equality of Weil polynomials implies isogeny over \(\mathbb F_{13}\) by the isogeny theorem for abelian varieties over finite fields. Different rational two-torsion orders preclude isomorphism of their Jacobians, and hence of their curves, over the base field.

## Verification
Run `python3 verify.py` using a standard Python 3 installation. It independently counts the genus-two and genus-one quotient points at \(p=5,13\), enumerates all admissible parameters, constructs complete quadratic-factor certificates for each nonsplit quartic, enumerates the fixed even-subset classes for rational Jacobian two-torsion, checks quadratic twists, and verifies all twenty-two marked zeta traces and the two mixed classes. The expected first output is `D4_F13_WEIL_TORSION_FIRST_PRIME_VERIFIED`. Only finite enumerations and structural arguments are used; no probabilistic arithmetic or numerical approximations are involved.

## Relationship to prior work
The model, its dihedral group action, the elliptic quotient, and the square-Jacobian isogeny are taken from Arul and collaborators' 2021 preprint (2023 revision). That paper explicitly records \(P(13)=6\), a count of *unmarked isogenous pairs*; it does not assert the precise mixed rational-Jacobian-two-torsion statement, the two mixed marked trace classes, or the first-prime cutoff established here. Its restriction to all-rational Weierstrass points in the detailed double-isogeny study cannot itself establish the mixed splitting claim. Cardona–Quer provide earlier general dihedral genus-two isomorphism and twist classifications; these general descriptions are not claimed as new. Published related genus-two two-torsion results in other families or characteristic three do not imply the specified characteristic-thirteen parameter calculation. The structural splitting-count formula above is included as a supporting lemma, not presented as a new general classification of dihedral automorphisms.

## Limitations
This result does not assert that the two curves are doubly isogenous in the stronger sense involving unramified covers, nor that they are geometrically nonisomorphic. The tables count normalized coefficient-marked models and their designated quadratic twists, not isomorphism classes of all dihedral curves or all genus-two curves over the field. The minimality is only among primes \(p\equiv1\pmod4\) within this specified family. The originally published Magma supplementary sources could not be examined in full, so historical priority for any previously computed but unindexed characteristic-thirteen two-torsion table remains an explicit risk. Independent validation has not been carried out.

## References
1. V. Arul, J. Booher, S. Groen, E. Howe, W. Li, V. Matei, R. Pries, C. Springer, *Doubly isogenous genus-2 curves with \(D_4\)-action*, arXiv:2102.11419, first public 2021-02-22, especially Sections 2, 4 and 5. https://arxiv.org/abs/2102.11419
2. G. Cardona and J. Quer, *Curves of genus 2 with group of automorphisms isomorphic to \(D_8\) or \(D_{12}\)*, arXiv:math/0203165, first public 2002-03-17. The notation \(D_8\) refers to the dihedral group of order eight. https://arxiv.org/abs/math/0203165
