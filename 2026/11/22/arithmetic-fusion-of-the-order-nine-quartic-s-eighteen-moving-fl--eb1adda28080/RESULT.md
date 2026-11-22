# Arithmetic fusion of the order-nine quartic's eighteen moving flexes

## Finding
Let \(C/\mathbb Q\) be the smooth plane quartic
\[
X^4+XY^3+YZ^3=0.
\]
Its reduced canonical Weierstrass (inflection) support over \(\mathbb Q\) has five closed points, of residue degrees
\[
\boxed{1,1,1,2,18}.
\]
The rational point \([0:0:1]\) is a hyperflex of weight two. The remaining twenty-two geometric points are ordinary flexes: two rational points, two conjugate quadratic points, and eighteen points forming one transitive absolute-Galois orbit. Thus the two nine-element free orbits under the geometric cyclic order-nine automorphism group are **arithmetically fused**. The degree-eighteen closed point is explicitly given, in \(Z=1\), by
\[
729x^{18}-270x^9-2=0,\qquad y=27x^{13}-11x^4.
\]
In characteristic seven, the curve has good reduction and the flex support has Frobenius cycle type \(1^5 18^1\); in particular its five fixed flexes are all rational over \(\mathbb F_7\).

## Assumptions and scope
All characteristic-zero assertions concern this specific rational plane model and its canonical plane embedding. A flex is a point of intersection of the smooth quartic and its Hessian; a hyperflex has contact four with its tangent and canonical weight two. We count *geometric support points* for the residue-degree list, and retain multiplicities only when computing the canonical ramification divisor. The characteristic-seven assertion concerns the reduction of this same integral model, not arbitrary twists or other primes.

## Proof
Put \(F=X^4+XY^3+YZ^3\). Its partial derivatives are
\[
F_X=4X^3+Y^3,\qquad F_Y=3XY^2+Z^3,\qquad F_Z=3YZ^2.
\]
When \(Z\ne0\), simultaneous vanishing forces \(Y=0\), contradicting \(F_Y\ne0\). On \(Z=0\), vanishing of \(F_Y\) implies \(X=0\) or \(Y=0\), and then \(F_X\ne0\). Therefore \(C\) is smooth in characteristic zero and seven. A smooth plane quartic is canonically embedded and has total Hessian-intersection degree \(4\cdot6=24\).

Direct differentiation gives the **exact polynomial identity**
\[
\det(\operatorname{Hess}F)=54Z\bigl(8X^3Y^2-2X^2Z^3-Y^5\bigr).
\]
At infinity, \(Z=0\) cuts \(C\) in the four distinct points with \(X=0\) or \(X^3+Y^3=0\), setting \(Y=1\). The second Hessian factor has value \(-Y^5\) at \(X=0\) and \(-9Y^5\) at the other three points, hence is nonzero. The hyperplane \(Z=0\) cuts \(C\) transversely at each, so these are four ordinary flexes. Two are rational (\(X/Y=0,-1\)); the remaining two form one quadratic Galois orbit.

On the affine chart \(Z=1\), write \(f=x^4+xy^3+y\) and \(q=8x^3y^2-2x^2-y^5\). A lexicographic Gröbner basis over \(\mathbb Q\), with \(y\) preceding \(x\), is precisely
\[
\left\{y+11x^4-27x^{13},\quad x^2(729x^{18}-270x^9-2)\right\}.
\]
Consequently the affine intersection of the quartic with the residual quintic factor comprises the origin with intersection multiplicity two, and eighteen simple points corresponding to the roots of
\[
P(x)=729x^{18}-270x^9-2.
\]
Indeed \(P(0)=-2\) and \(\gcd(P,P')=1\), so every nonzero root gives a reduced point. The tangent at the origin is \(Y=0\), and \(F(X,0,1)=X^4\), establishing contact order four and weight two. Thus all eighteen other affine points are ordinary flexes. Together with four simple points at infinity, the weights sum to \(2+18+4=24\), proving there are no omitted points.

To prove the arithmetical assertion, reduce \(P\) modulo seven:
\[
\overline P=x^{18}+3x^9+5\in\mathbb F_7[x].
\]
In \(\mathbb F_7[x]/(\overline P)\), exact modular exponentiation yields
\[
x^{7^6}\equiv-3x,\qquad
x^{7^9}\equiv2x^{10}-2x,\qquad
x^{7^{18}}\equiv x.
\]
The first two congruences give \(\gcd(\overline P,x^{7^6}-x)=\gcd(\overline P,x^{7^9}-x)=1\). For the second gcd, the potential nonzero common roots would satisfy \(x^9=3/2=5\) in \(\mathbb F_7\); substituting into \(\overline P\) gives \(3\ne0\). Since the prime divisors of \(18\) are \(2,3\), Rabin's irreducibility criterion shows that \(\overline P\) is irreducible of degree eighteen. Hence \(P\) is irreducible over \(\mathbb Q\), and Frobenius acts in one eighteen-cycle on its eighteen simple roots modulo seven.

The automorphism \([X:Y:Z]\mapsto[\zeta_3X:Y:\zeta_9Z]\) has order nine on \(C_{\overline{\mathbb Q}}\), since \(\zeta_9^3=\zeta_3\). It sends affine \(x\) to \(\zeta_9^2x\), keeping \(x^9\) fixed. The two quadratic values \(x^9=(5\pm3\sqrt3)/27\) therefore label its two nine-element free flex orbits, whereas the irreducibility just proved shows that absolute Galois exchanges them. Finally, all four infinity points reduce rationally modulo seven because \(X^3+1\) splits over \(\mathbb F_7\), and the origin remains rational, establishing the claimed Frobenius cycle partition.

## Verification
The accompanying `verify_flex_arithmetic.py` evaluates the full Hessian determinant, derives the exact lexicographic Gröbner basis, checks separability, and performs the modular exponentiation and gcd tests at the required exponents. Run `python verify_flex_arithmetic.py` with SymPy 1.14.0; success prints `ORDER_NINE_QUARTIC_ARITHMETIC_FLEX_DIVISOR_OK`. The symbolic checks reproduce the algebraic equalities used in the proof; the argument above, including the irreducibility criterion, supplies the deductive justification.

## Relationship to prior work
Babu and Venkataraman (2005), in their discussion of the cyclic order-nine genus-three locus, already establish **five exceptional fixed Weierstrass points and two free nine-element flex orbits**. This geometric classification is not new. Lorenzo García (2016, arXiv:1604.02410, Section 2) records the exact plane model and automorphism type. Liang (2019, arXiv:1902.02914, Sections 1–4) computes invariants and bitangents of an isomorphic cyclic-nine quartic; bitangents are not the canonical flex divisor. The arithmetic novelty asserted here is the **irreducible degree-eighteen descent of the two known geometric orbits**, with an explicit good-reduction Frobenius certificate. The closest identified mathematical research record about this curve instead determines the Galois-invariant configuration of 28 bitangents and level-two structures, not the canonical inflection divisor.

## Limitations
This result does not classify twists, their flex Galois actions, or other primes. The mod-seven calculation establishes a full cycle but does not determine the full splitting field Galois group. Although the specified primary literature and relevant indexed results were checked, absence of an earlier unindexed equivalent arithmetic computation is not proved. No independent mathematical audit has been performed.

## References
- H. Babu and P. Venkataraman, *Group Action on Genus 3 Curves and Their Weierstrass Points*, 2005, DOI: 10.1142/9789812701640_0017, https://www.academia.edu/4768194/Group_Actions_on_Genus_3_Curves_and_their_Weierstrass_Points .
- E. Lorenzo García, *Twists of Non-Hyperelliptic Curves of Genus 3*, arXiv:1604.02410v1 (public April 8, 2016), https://arxiv.org/abs/1604.02410 .
- D. Liang, *Invariants, Bitangents and Matrix Representations of Plane Quartics with 3-Cyclic Automorphisms*, arXiv:1902.02914, https://arxiv.org/abs/1902.02914 .
- Published mathematical research record, *The order-nine Picard quartic has level-two orbit profile*, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-the-order-nine-picard-quartic-has-level-two-orbit-profile-1-9-9--b8d8cc6b1ea4 .
