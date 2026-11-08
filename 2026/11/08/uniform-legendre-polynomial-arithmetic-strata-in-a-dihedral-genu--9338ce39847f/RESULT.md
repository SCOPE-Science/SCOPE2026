# Uniform Legendre-polynomial arithmetic strata in a dihedral genus-three pencil

## Finding
Let \(p\ge3\) be an odd prime, \(k=\overline{\mathbb F}_p\), and let \(c\in k\) satisfy \(c^2\ne4\). Let \(C_c\) be the smooth projective curve
\[
 C_c:\quad y^2=x^8+cx^4+1.
\]
It has genus three. The involution \((x,y)\mapsto(-x,y)\) induces an elliptic quotient \(E_c\) and an abelian-surface Prym \(P_c\). Put \(n=(p-1)/2\), \(m=\lfloor(p-1)/4\rfloor\), and let \(P_j(z)\) denote the ordinary degree-\(j\) Legendre polynomial, reduced modulo \(p\). Set
\[
 A_p(c)=P_m(c/2),\qquad B_p(c)=P_n(c/2)\quad\text{in }\mathbb F_p[c].
\]
With \(\mathbf1\) denoting an indicator, **for every smooth geometric parameter** the \(p\)-ranks and Cartier \(a\)-numbers are
\[
 (f_p(P_c),a(P_c))=(2\mathbf1_{A_p(c)\ne0},\;2\mathbf1_{A_p(c)=0}),
\]
\[
 (f_p(E_c),a(E_c))=(\mathbf1_{B_p(c)\ne0},\;\mathbf1_{B_p(c)=0}),
\]
\[
 (f_p(J(C_c)),a(J(C_c)))=(2\mathbf1_{A_p(c)\ne0}+\mathbf1_{B_p(c)\ne0},\;2\mathbf1_{A_p(c)=0}+\mathbf1_{B_p(c)=0}).
\]
In particular the Prym is superspecial at **exactly** \(m\) distinct smooth geometric coefficients, the elliptic quotient is supersingular at exactly \(n\), and the number of coefficients with superspecial genus-three Jacobian is exactly
\[
 d_p=\deg\gcd(A_p,B_p)\in\{0,1,\dots,m\}.
\]
Thus the numbers of geometric parameters of types \((f_p(J),a(J))=(0,3),(1,2),(2,1)\) are respectively \(d_p,m-d_p,n-d_p\). Every other smooth parameter is ordinary \((3,0)\). These counts are of **distinct coefficient parameters over \(k\)**, not of curve-isomorphism classes. The polynomials and their gcd give a finite exact procedure for every odd prime; no closed arithmetic formula for \(d_p\) is asserted.

## Assumptions and scope
The base field is algebraically closed of odd characteristic, the coefficient \(c\) is any element of that field except \(\pm2\), and all invariants are geometric. The exclusion is precisely the squarefreeness condition for \(x^8+cx^4+1\). The Prym is the connected kernel of the norm \(J(C_c)\to E_c\), of dimension two. Superspecial means Cartier \(a\)-number equal to the dimension (equivalently, isomorphic over \(k\) to a product of supersingular elliptic curves). All isogenies used below have degree a power of two, hence are prime to \(p\).

## Proof
**1. Genus and three elliptic quotients.** The derivative of \(f(x)=x^8+cx^4+1\) is \(4x^3(2x^4+c)\). A common zero of \(f,f'\) exists precisely when \(c^2=4\); for the admitted coefficients \(f\) has eight distinct roots. Thus \(C_c\) is smooth of genus three. Introduce commuting involutions \(\alpha(x,y)=(-x,y)\), \(\beta(x,y)=(x^{-1},y/x^4)\), and \(\gamma=\alpha\beta\). Their three quotient curves have genus one; explicit maps are
\[
 E_0:\ v^2=u^4+cu^2+1,\quad(u,v)=(x^2,y),
\]
\[
 E_1:\ v^2=t^4-4t^2+c+2,\quad(t,v)=(x+x^{-1},y/x^2),
\]
\[
 E_2:\ v^2=s^4+4s^2+c+2,\quad(s,v)=(x-x^{-1},y/x^2).
\]
Each quartic has four simple roots for \(c^2\ne4\). Choosing \(i\in k\) with \(i^2=-1\) identifies \(E_2\simeq E_1\). The invariant differential pullbacks from these three quotient elliptic curves are proportional respectively to \(x\,dx/y\), \((x^2-1)dx/y\), and \((x^2+1)dx/y\), a basis of \(H^0(C_c,\Omega^1)\), since \(p\ne2\). Hence the product of pullbacks gives an isogeny \(E_0\times E_1\times E_2\to J(C_c)\). More precisely the group-ring identity \(1+\alpha+\beta+\gamma=0\) on \(J(C_c)\) (the Klein-four quotient has genus zero) makes the sum of the three pullback–norm composites equal to multiplication by two. Consequently the isogeny has 2-power degree and gives an isomorphism on \(p\)-divisible groups. The Prym of \(C_c\to E_0\) is 2-power-isogenous to \(E_1^2\). In particular its \(p\)-rank and \(a\)-number are twice those of \(E_1\), while those of \(J(C_c)\) are the sums of the three elliptic invariants.

**2. Exact elliptic Hasse invariants.** For an elliptic quartic \(v^2=g(t)\), its Cartier/Hasse scalar vanishes precisely when \([t^{p-1}]g(t)^n\) vanishes, where \(n=(p-1)/2\). For \(E_1\) this scalar is
\[
 H_1(c)=[t^{p-1}](t^4-4t^2+c+2)^n
 =\sum_{j=0}^{m}\frac{n!}{j!^2(n-2j)!}(-4)^{n-2j}(c+2)^j.
\]
The coefficients are taken modulo \(p\). The constant term of the expansion about \(c=-2\) is \((-4)^n\), and the ratio of consecutive coefficients is
\[
 \frac{(n-2j)(n-2j-1)}{16(j+1)^2}\quad (0\le j<m).
\]
The ordinary hypergeometric identity
\[
 P_m(-1+z/2)=(-1)^m\sum_{j=0}^{m}\frac{(-m)_j(m+1)_j}{(j!)^2}(z/4)^j
\]
has consecutive coefficient ratio \((j-m)(j+m+1)/(4(j+1)^2)\). Since \(2n\equiv-1\pmod p\) and \(m(m+1)\equiv-3/16\pmod p\), these ratios agree modulo \(p\). Therefore, including the constant normalization,
\[
 H_1(c)=(-4)^n(-1)^m P_m(c/2)\pmod p.
\]
For \(E_0\), direct expansion gives
\[
 H_0(c)=[u^{p-1}](u^4+cu^2+1)^n
       =\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n!}{j!^2(n-2j)!}c^{n-2j}.
\]
Comparing successive coefficients with the standard factorial expression for \(P_n(c/2)\), using \(2n=p-1\), yields the explicit nonzero normalization
\[
 H_0(c)=\frac{2^{2n}(n!)^2}{(2n)!}\,P_n(c/2)\pmod p.
\]
All factorial denominators here are nonzero modulo \(p\), including for \(p=3\).

**3. Simplicity and the four arithmetic strata.** For any \(0\le r<p\), the polynomial \(P_r(z)\) has degree \(r\) over \(\mathbb F_p\) when \(r=m\) or \(r=n\), and satisfies \((1-z^2)P_r''-2zP_r'+r(r+1)P_r=0\). It takes values \(P_r(\pm1)=(\pm1)^r\), so it has no roots at the excluded parameters \(c=\pm2\). A repeated root away from \(\pm1\) would make all derivatives vanish successively by the differential equation; because \(r<p\), this would force the polynomial to be zero, a contradiction. Thus \(A_p\) has exactly \(m\) distinct geometric roots and \(B_p\) exactly \(n\), with the common roots precisely those of their squarefree gcd. One-dimensional elliptic Hasse scalars now distinguish ordinary from supersingular curves. Step 1 adds their \(p\)-ranks and \(a\)-numbers, giving exactly the claimed stratification and counts.

## Verification
The companion standalone script `verify_prym.py` reconstructs both elliptic Hasse polynomials by multinomial coefficients and by an independent modular Legendre recurrence for every odd prime below 110; it compares them up to a nonzero scalar. It then directly expands \((x^8+cx^4+1)^n\) and computes the full genus-three Cartier matrix at each smooth rational parameter \(c\in\mathbb F_p\), confirming the predicted rank in every such case. It prints `VERIFY_OK`. This exhaustive finite-prime validation is a check, **not** the proof for arbitrary primes; the universal argument is the coefficient identity and differential-equation proof above.

For illustration the exact degree \(d_p\) for \(p=3,5,7,11,13,17,19,23,31,47\) is respectively \(0,0,1,0,0,2,0,1,3,7\); these values follow from Euclidean polynomial gcd calculations. They count coefficient parameters, not geometric isomorphism classes.

## Relationship to prior work
Ohashi's 2021 preprint (arXiv:2112.11152, especially Sections 2–4 and Example 4.3) studies the superspecial and maximality geometry of general genus-three hyperelliptic Howe curves and includes the dihedral octic type. Its established elliptic-product decomposition and small-prime isomorphism-class tabulations are prior work. Borówka–Shatsila (arXiv:2308.07038, especially Sections 3–4) develop elliptic quotient and Prym geometry in the general two-involution genus-three family. The present statement specializes to the one-parameter dihedral pencil but provides a uniform, *all-odd-prime*, explicit Legendre-polynomial classification of **all** geometric \(p\)-rank/\(a\)-number strata, including exact Prym superspecial coefficient counts and a computable gcd for superspecial Jacobians. It does not claim novelty for elliptic quotient decompositions or for the classical Legendre-polynomial theory separately. Small-prime cases in previously available calculations are subsumed, not claimed as separate discoveries.

## Limitations
The formula for \(d_p\) is an exact polynomial-gcd prescription rather than a prime-congruence-only closed formula. Coefficient parameters can define isomorphic curves, and no moduli-isomorphism census is claimed. The theorem does not determine full Newton polygons or rational-point counts over finite extensions. The all-prime result has not received independent mathematical audit. An earlier treatment applying the same Legendre reduction to this pencil, including unindexed computations or the cited source's implications, remains a specific priority risk.

## References
1. R. Ohashi, *On the maximality of hyperelliptic Howe curves of genus 3*, arXiv:2112.11152, first public 2021-12-21, Sections 2–4 and Example 4.3. https://arxiv.org/abs/2112.11152
2. P. Borówka and A. Shatsila, *Hyperelliptic genus 3 curves with involutions and a Prym map*, arXiv:2308.07038, first public 2023-08-14, Sections 3–4. https://arxiv.org/abs/2308.07038
3. T. Shaska, *Genus 3 hyperelliptic curves with (2, 4, 4)-split Jacobians*, arXiv:1306.5284 (historical background on decomposable Jacobians, not the eligible motivating source).
