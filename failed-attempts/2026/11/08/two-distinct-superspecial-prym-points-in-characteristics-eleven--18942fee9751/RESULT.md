# Two distinct superspecial Prym points in characteristics eleven and thirteen

## Finding
Let \(k\) be algebraically closed of characteristic \(p\in\{11,13\}\), and for every \((a,b)\in k^2\) with \(b(a^2-4b)\ne0\), consider the smooth genus-three bielliptic Picard curve
\[
 C_{a,b}:\qquad y^3=x^4+a x^2+b.
\]
Let \(\tau(x,y)=(-x,y)\), let \(E_{a,b}=C_{a,b}/\langle\tau\rangle\) be the elliptic quotient, and let \(P_{a,b}=\ker(1+\tau^*)^0\) be the associated abelian-surface Prym. The marked-curve coarse parameter is
\[
 j=\frac{4b-a^2}{4b}\in k^\times.
\]
Exactly the following geometric arithmetic strata occur:

* **Characteristic eleven.** For \(j\ne1\), \(P_{a,b}\) is ordinary with \(11\)-rank two and \(a\)-number zero. Its Jacobian has \(11\)-rank two and \(a\)-number one, with Newton slopes \(0,0,\tfrac12,\tfrac12,1,1\). At the sole exceptional coarse point \(j=1\), the Prym and the entire genus-three Jacobian are **superspecial**: the Jacobian has \(11\)-rank zero, \(a\)-number three, and six Newton slopes all equal to \(\tfrac12\).
* **Characteristic thirteen.** For \(j\ne-1\), both the Prym and the full Jacobian are ordinary (Jacobian \(13\)-rank three, \(a\)-number zero). At the sole exceptional coarse point \(j=-1\), the Prym is superspecial, but the elliptic quotient is ordinary. The Jacobian then has \(13\)-rank one, \(a\)-number two, with Newton slopes \(0,\tfrac12,\tfrac12,\tfrac12,\tfrac12,1\).

Fix the Prym differential basis \((\eta_0,\theta)=(dx/y^2,dx/y)\), and let \(H_P\) denote its matrix of **coefficients before taking \(p\)-th roots** in the Cartier formula. Then
\[
 \boxed{\frac{\det H_P}{b^5}=5j^2(1-j)\quad(p=11)},\qquad
 \boxed{\frac{\det H_P}{b^6}=4j^2(j+1)^2\quad(p=13)}.
\]
Thus, on the smooth coarse \(j\)-line (where \(j\ne0\)), the Prym Hasse-determinant zero divisor is a **single simple point at \(j=1\)** in characteristic eleven, but a **double point at \(j=-1\)** in characteristic thirteen. In each characteristic the *Cartier-rank-zero* locus is nevertheless supported at one reduced coarse \(j\)-point. The two exceptional parameters coincide with the distinct \(j=1\) and \(j=-1\) points listed among the rational complex-multiplication values in the motivating arithmetic geometry of the family; their moduli interpretation is therefore intrinsic rather than an arbitrary coefficient slice.

## Assumptions and scope
The base field is algebraically closed of characteristic eleven or thirteen. The quartic \(f(x)=x^4+a x^2+b\) is separable precisely when \(b(a^2-4b)\ne0\), because simultaneous zeros of \(f\) and \(f'=4x^3+2ax\) are exactly those excluded by this condition. The tame triple cover \(C\to\mathbb P^1_x\), branched at four finite roots and infinity, has genus three by Riemann--Hurwitz. All ranks, \(a\)-numbers and Newton polygons are geometric. The \(p\)-rank of an abelian variety is the rank of its maximal étale \(p\)-torsion; its \(a\)-number is the dimension of the Cartier kernel. An abelian surface is superspecial when its \(a\)-number is two, equivalently when it is geometrically isomorphic to a product of supersingular elliptic curves. The family, marked coarse \(j\)-coordinate and Prym construction are those of Laga--Shnidman; no new claim is made about these pre-existing definitions.

## Proof
**1. Holomorphic differentials and the Prym splitting.** At the unique point at infinity, \(\operatorname{ord}(x)=-3\), \(\operatorname{ord}(y)=-4\), and \(\operatorname{ord}(dx)=-4\). Hence
\[
 \eta_0=dx/y^2,\qquad \eta_1=x\,dx/y^2,\qquad \theta=dx/y
\]
are three linearly independent holomorphic differentials, of respective orders \(4,1,0\) at infinity, so form a basis. The involution fixes \(\eta_1\) and negates \(\eta_0,\theta\). With \(u=x^2\), the elliptic quotient has model \(E:y^3=u^2+au+b\); completing the square identifies it with a \(j(E)=0\) elliptic curve. It is supersingular in characteristic eleven and ordinary in characteristic thirteen. The natural map \(E\times P\to\operatorname{Jac}(C)\) is an isogeny of two-power degree. Since the characteristic is odd, it induces isomorphisms on \(p\)-divisible groups and \(p\)-torsion group schemes. Thus Newton polygons, \(p\)-ranks and \(a\)-numbers split as those of \(E\) and \(P\).

**2. Cartier extraction rule.** Let \(m\in\{1,2\}\) and choose \(m'\in\{1,2\}\) uniquely satisfying \(p m'\equiv m\pmod3\), and put \(e=(pm'-m)/3\). The identity
\[
 x^i\,dx/y^m=(y^{-m'})^p x^i f^e\,dx
\]
and Cartier's rule \(\mathcal C(x^{p-1+pt}dx)=x^t dx\), with the required \(p\)-th roots of coefficients, show that the coefficient of \(x^t dx/y^{m'}\) in \(\mathcal C(x^i dx/y^m)\) is the \(p\)-th root of \([x^{p-1+pt-i}]f^e\). This is valid over the algebraic closure and gives an exhaustive symbolic description; the finite-field point counts below are independent checks, not a substitute for the calculation.

**3. Characteristic eleven.** Expanding \(f^3\) and \(f^7\) in \(\mathbb F_{11}[a,b,x]\) gives
\[
 \mathcal C(\eta_0)=(3a)^{1/11}\theta,\quad
 \mathcal C(\eta_1)=0,\quad
 \mathcal C(\theta)=\bigl(-a b^2(a^2-4b)^2\bigr)^{1/11}\eta_0.
\]
Indeed the coefficients \([x^{10}]f^3=3a\) and \([x^{10}]f^7=-ab^2(a^2-4b)^2\) are exact, while both relevant odd-degree coefficients vanish. As \(b(a^2-4b)\ne0\), the two-dimensional Prym Cartier block is invertible if and only if \(a\ne0\), and vanishes entirely when \(a=0\). The elliptic differential \(\eta_1\) is killed by Cartier, consistently with \(j(E)=0\) and \(11\equiv2\pmod3\). Therefore, outside \(a=0\), the Jacobian has an ordinary two-dimensional part and a supersingular elliptic part. On \(a=0\), the entire genus-three Cartier operator is zero, so the Jacobian is superspecial.

The coefficient matrix on \((\eta_0,\theta)\) is
\[
 H_P=\begin{pmatrix}0&-ab^2(a^2-4b)^2\\3a&0\end{pmatrix},
 \qquad \det H_P=3a^2b^2(a^2-4b)^2.
\]
Put \(t=a^2/b\), so \(j=1-t/4\). Then
\[
 \det H_P/b^5=3t(t-4)^2=5j^2(1-j)\quad\text{in }\mathbb F_{11}[j,j^{-1}].
\]
The only zero on \(j\ne0\) is a simple zero at \(j=1\). On the coefficient cover, both Prym matrix entries vanish precisely along the reduced divisor \(a=0\); it maps to the unique coarse point \(j=1\).

**4. Characteristic thirteen.** Since \(p\equiv1\pmod3\), the Cartier matrix is diagonal in the basis \((\eta_0,\eta_1,\theta)\). Directly extracting coefficients from \(f^8\) and \(f^4\) gives
\[
 \begin{aligned}
 \mathcal C(\eta_0)&=\bigl(2b^2(a^2-4b)^2(a^2+5b)\bigr)^{1/13}\eta_0,\\
 \mathcal C(\eta_1)&=\bigl(5(a^2-4b)^2\bigr)^{1/13}\eta_1,\\
 \mathcal C(\theta)&=\bigl(6(a^2+5b)\bigr)^{1/13}\theta.
 \end{aligned}
\]
In particular, the quotient eigenvalue on \(\eta_1\) is always nonzero on the smooth locus. The Prym block is invertible if and only if \(a^2+5b\ne0\), and is identically zero when \(a^2+5b=0\). The latter locus is smooth because \(b\ne0\) and \(a^2-4b=-9b=4b\ne0\) in characteristic thirteen. Thus the Prym there is superspecial, while the elliptic quotient is ordinary, yielding Jacobian \(13\)-rank one and \(a\)-number two. Off that locus the full Jacobian is ordinary.

The pre-root Prym determinant is
\[
 \det H_P=12b^2(a^2-4b)^2(a^2+5b)^2.
\]
With \(t=a^2/b\) and \(j=1-t/4\) as before,
\[
 \det H_P/b^6=12(t-4)^2(t+5)^2=4j^2(j+1)^2.
\]
Therefore the determinant vanishes to order two at the unique smooth coarse point \(j=-1\). However the entire Prym Cartier block vanishes exactly when \(a^2+5b=0\), which equals a unit multiple of \(j+1\) on \(b\ne0\). Hence the *matrix-rank-zero* locus is a reduced point in the coarse \(j\)-coordinate, even though the determinant has multiplicity two. The rank and Newton claims follow from the elliptic/Prym decomposition in Step 1.

## Verification
The standalone `verify_cartier.py` performs coefficient arithmetic in \(\mathbb F_p[a,b,x]\) without symbolic-math dependencies. It reconstructs the complete three-dimensional Cartier matrices for \(p=11,13\), verifies the factorization of every entry, and checks the two \(j\)-formulas at every nonsingular prime-field coarse parameter. The standalone `verify_zeta.py` constructs \(\mathbb F_{p^n}\) for \(n=1,2,3\), independently counts points on all smooth coefficient curves over \(\mathbb F_p\), recovers the first three zeta coefficients by Newton's identities, and compares them modulo \(p\) with the independently computed Cartier characteristic polynomial. It checks all 100 smooth pairs in \(\mathbb F_{11}^2\): 10 of rank zero, 90 of rank two; and all 144 smooth pairs in \(\mathbb F_{13}^2\): 12 of rank one, 132 of rank three. Different coefficient pairs need not be distinct geometric isomorphism classes, and these finite checks do not prove the algebraic-closure statements; the symbolic Cartier argument above does.

## Relationship to prior work
Laga--Shnidman, arXiv:2308.15297 (first posted 29 August 2023), give the bielliptic Picard family, coarse \(j\)-line, elliptic quotient and quaternionic Prym. Their rational CM table includes \(j=1\) (discriminant \(-4\)) and \(j=-1\) (discriminant \(-24\)), but their sections on quaternionic multiplication, arithmetic torsion and reductions do not determine the exact characteristic-eleven and characteristic-thirteen Prym Hasse divisors, their multiplicities, or the complete Newton strata claimed here.

Nourozi--Rahmati, arXiv:2306.07823 (first posted 13 June 2023), derive general Cartier coefficient formulas for Picard curves and give broad \(a\)-number statements. Their Theorem 3.1, as printed for separable quartics with nonzero constant coefficient, asserts \(a(C)=0\) for \(p\equiv1\pmod3\) and \(a(C)=1\) for \(p\equiv2\pmod3\). The smooth exceptional curves in the present theorem have respectively \(a(C)=2\) at \(p=13,j=-1\) and \(a(C)=3\) at \(p=11,j=1\), so they furnish explicit counterexamples to those unqualified assertions. Their coefficient-based Cartier machinery is antecedent, but their stated constant \(a\)-number theorem neither covers nor implies the new exceptional Prym-moduli classification. Estrada-Sarlabous (1991) discusses general Hasse--Witt criteria for Picard Jacobians, but its primary full text could not be inspected, so implicit earlier coverage is a genuine residual priority risk. The abstract alone does not settle a full Prym-moduli comparison. A previous explicit characteristic-seven subfamily classification concerns a different prime and does not imply the two characteristic-eleven/thirteen Hasse divisors; no new characteristic-seven result is claimed.

## Limitations
The result applies only to the displayed smooth marked bielliptic Picard family in characteristics eleven and thirteen, not to all Picard curves, to unmarked global automorphism classes, or to arbitrary primes. The term *superspecial* at the exceptional characteristic-thirteen point applies to the Prym surface, not the full genus-three Jacobian. In characteristic eleven the full Jacobian is superspecial at its exceptional point. The normalized determinant formulas depend on the differential basis, but their vanishing orders on the indicated coarse \(j\)-line are unambiguous. The finite-field point-count tests check only prime-field coefficient parameters; the proof works over the algebraic closure. Independent mathematical audit and independent historical-priority review have not been performed.

## References
1. J. Laga and A. Shnidman, *The geometry and arithmetic of bielliptic Picard curves*, arXiv:2308.15297 (first public version 29 August 2023), especially Sections 2, 4, 6 and Table 1. https://arxiv.org/html/2308.15297v3
2. V. Nourozi and F. Rahmati, *The Rank of the Cartier operator on Picard Curves*, arXiv:2306.07823 (first public version 13 June 2023), especially Section 3. https://arxiv.org/abs/2306.07823
3. J. Estrada-Sarlabous, *On the Jacobian Varieties of Picard Curves Defined over Fields of Characteristic p > 0*, Mathematische Nachrichten 152 (1991), 329--340, DOI:10.1002/mana.19911520125 (abstract inspected; full text inaccessible).
4. I. Bouw and collaborators, *Conductor and discriminant of Picard curves*, Journal of the London Mathematical Society 102 (2020), 368--404, DOI:10.1112/jlms.12323 (smooth models and arithmetic context).
