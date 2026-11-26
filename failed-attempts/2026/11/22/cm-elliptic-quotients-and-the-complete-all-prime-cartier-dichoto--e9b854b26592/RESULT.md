# CM elliptic quotients and the complete all-prime Cartier dichotomy for a genus-two Chebyshev curve

## Finding
Let \(k\) be an algebraically closed field of odd prime characteristic \(p\ne5\). Let \(C_p\) be the smooth projective curve with affine model
\[
 C_p:\qquad y^2=x^5-5x^3+5x.
\]
Its Jacobian has precisely two possible Cartier and Newton behaviors:
\[
\begin{array}{c|c|c|c}
 p\bmod20 & \operatorname{rank}(\operatorname{Cartier})&\text{Jacobian }p\text{-rank}&a(\operatorname{Jac}(C_p))\\\hline
 1,3,7,9&2&2&0\\
 11,13,17,19&0&0&2
\end{array}
\]
(Only residue classes containing primes other than \(2,5\) are meant.) In particular, each nonordinary reduction is *superspecial*, not merely supersingular. There is no reduction with intermediate Cartier rank or intermediate \(p\)-rank.

More structurally, over \(k\) the Jacobian is related by a separable isogeny of degree \(4\) to the square of a smooth elliptic curve with
\[
 j=632000+282880\sqrt5,
 \qquad H_{-20}(j)=j^2-1264000j-681472000=0.
\]
The square root is selected as described below, and its other choice yields the algebraic conjugate \(j\). In characteristic zero this elliptic curve has complex multiplication by the maximal order of \(\mathbb Q(\sqrt{-5})\). Every reduction at \(p\ne2,5\) has its \(p\)-torsion group scheme identified, after algebraic closure, with the square of that elliptic curve's \(p\)-torsion.

## Assumptions and scope
All curves, quotient morphisms and Jacobian isogenies are taken over an algebraically closed field \(k\) of characteristic \(p\ge3\), \(p\ne5\). Choose \(d\in k\) with \(d^4=5\), and put \(c=d^2\) and \(K=5+2d^2\). Since \(p\ne2,5\), the quintic is separable and defines a smooth genus-two curve. The elliptic cubics used below have three distinct roots, since \(K(K-4d^2)\ne0\). The \(a\)-number means \(\dim_k\operatorname{Hom}(\alpha_p,\operatorname{Jac}(C_p)[p])\); it equals the dimension of the kernel of Cartier on regular differentials.

## Proof
1. **Two commuting involutions.** Define
\[
 \sigma:(x,y)\longmapsto \left(\frac{d^2}{x},\frac{d^3y}{x^3}\right),\qquad
 \iota:(x,y)\longmapsto(x,-y).
\]
The identity \(f(d^2/x)=d^6 f(x)/x^6\), for \(f(x)=x^5-5x^3+5x\) and \(d^4=5\), shows that \(\sigma\) extends to an involution. It commutes with the hyperelliptic involution \(\iota\).

2. **Explicit genus-one quotients.** Set
\[
 u=x+\frac{d^2}{x},\qquad
 v_+=\frac{y(x+d)}{x^2},\qquad
 v_-=\frac{y(x-d)}{x^2}.
\]
Direct polynomial reduction modulo \(d^4-5\) gives
\[
 v_+^2=(u+2d)(u^2-K),\qquad
 v_-^2=(u-2d)(u^2-K).
\]
The functions \((u,v_+)\) are fixed by \(\sigma\), while \((u,v_-)\) are fixed by \(\iota\sigma\), and each pair generates its respective fixed field. Thus the two degree-two quotient curves \(E_+\) and \(E_-\) are elliptic. They are isomorphic over \(k\) by \((u,v)\mapsto(-u,iv)\), where \(i^2=-1\). The pullbacks of the invariant differential on these quotients are
\[
 q_+^*(du/v_+)=(x-d)\,dx/y,\qquad
 q_-^*(du/v_-)=(x+d)\,dx/y,
\]
which are independent because \(p\ne2\). The induced map \(q_+^*+q_-^*:E_+\times E_-\to\operatorname{Jac}(C_p)\) is therefore an isogeny. Its dual composite is \(\mathrm{diag}([2],[2])\): on the diagonal \(q_{\pm,*}q_\pm^*=[2]\); the off-diagonal maps vanish since the two eigenspaces of \(\sigma\) have opposite eigenvalues, so each off-diagonal map equals its negative and \(\operatorname{Hom}(E_+,E_-)\) has no torsion. Taking degrees gives \(\deg(q_+^*+q_-^*)=4\).

3. **Elliptic CM invariant.** The first quotient is in Weierstrass form
\[
 v^2=u^3+2du^2-Ku-2dK.
\]
The standard \(c_4^3/\Delta\) formula, reduced modulo \(d^4-5\), yields
\[
 j(E_+)=\frac{8000(2d^2+3)^3}{(2d^2-5)^2(2d^2+5)}=632000+282880d^2.
\]
An exact substitution establishes \(H_{-20}(j(E_+))=0\). In characteristic zero this is the class polynomial for the imaginary quadratic order of discriminant \(-20\), hence the elliptic quotient has CM by \(\mathbb Z[\sqrt{-5}]\). Its integral Weierstrass model has good reduction at each prime not dividing \(10\) (as checked by the displayed root differences), and the classical CM reduction criterion gives that its geometric reduction is ordinary exactly when \(p\) splits in \(\mathbb Q(\sqrt{-5})\), and supersingular exactly when \(p\) is inert. All these assertions concern elliptic curves after choosing a prime of the CM field above \(p\); the ordinary/supersingular property is independent of that choice.

4. **Exact \(p\)-torsion, not only isogeny slopes.** Since the genus-two isogeny in step 2 has degree \(4\), prime to every allowed \(p\), it induces an isomorphism on \(p\)-divisible groups and therefore on \(p\)-torsion group schemes. Thus \(\operatorname{Jac}(C_p)[p]\simeq E_+[p]^2\). An ordinary elliptic curve has \(p\)-rank one and \(a\)-number zero; a supersingular elliptic curve has \(p\)-rank zero and \(a\)-number one. Accordingly, the genus-two values are respectively \((p\text{-rank},a)=(2,0)\) and \((0,2)\), and the Cartier operator is invertible or zero.

5. **Prime residue classes.** Quadratic reciprocity gives \(\left(\frac{-5}{p}\right)=+1\) precisely for \(p\equiv1,3,7,9\pmod{20}\), and \(-1\) for \(p\equiv11,13,17,19\pmod{20}\). This is the desired dichotomy.

## Verification
The standalone `check.py` uses exact polynomial reductions over \(\mathbb Q[d]/(d^4-5)\) to check both elliptic quotient identities, the rational expression for \(j\), and its class-polynomial identity. Independently, it computes the exact \(2\times2\) Cartier–Manin coefficient matrix of \(f(x)^{(p-1)/2}\) over each prime \(3\le p<200\) other than \(5\), finding rank \(0\) in the inert classes and rank \(2\) in the split classes. These finite computations confirm the claimed examples; the argument for all primes is steps 1–5 above, not extrapolation from testing. The checker requires Python 3 and SymPy.

## Relationship to prior work
Kazemifard–Tafazolian (2026) identify automorphism groups of Chebyshev hyperelliptic curves, including the degree-five reciprocal symmetry underlying \(\sigma\). Tafazolian–Top (2026) classify when Chebyshev hyperelliptic Jacobians are supersingular or maximal over an extension and describe their CM factors and Frobenius polynomials. Their supersingularity conclusions alone do not distinguish superspecial from nonsuperspecial supersingular reduction. Takei (2014, §5.2) studies the larger family \(y^2=x^5-5x^3+5x+2-4t\) and gives the zero pattern of its Cartier–Manin matrix; that theorem does not evaluate its two potentially nonzero entries at \(t=1/2\) in all characteristics. The elliptic CM \(j\)-values and Deuring's reduction theorem are classical and are not claimed as discoveries. The distinct contribution asserted here is the explicit double-elliptic quotient explanation and all-prime **group-scheme-level** ordinary/superspecial dichotomy for the specific central Chebyshev curve. The references do not constitute an exhaustive priority search.

## Limitations
The characteristic-two model and the singular characteristic-five reduction are excluded. The result concerns one fixed genus-two Chebyshev curve, not a classification of the full one-parameter family, its twists over finite prime fields, or the exact arithmetic Frobenius polynomial. The two elliptic quotients are isomorphic over an algebraic closure but need not be isomorphic over the base prime field. Although a prime-to-characteristic isogeny identifies the \(p\)-divisible groups, it does not assert an isomorphism of principally polarized Jacobians with an elliptic product. Older unindexed discussions of the central fiber may affect claims of first publication.

## References
- A. Kazemifard and S. Tafazolian, *Automorphisms of Kummer and Artin–Schreier Curves Defined by Chebyshev Polynomials*, arXiv:2611.10255v1 (first public 2026-11-06), https://arxiv.org/abs/2611.10255.
- S. Tafazolian and J. Top, *A Complete Classification of Maximal Hyperelliptic Curves Related to Chebyshev Polynomials*, arXiv:2611.14198v1 (2026-11-10), https://arxiv.org/html/2611.14198v1.
- L. K. Takei, *Arithmetic Aspects of Triangle Groups*, PhD thesis, McGill University, 2014, §5.2, https://www.math.mcgill.ca/darmon/theses/takei/thesis.pdf.
- Classical Hilbert class polynomial \(H_{-20}(X)=X^2-1264000X-681472000\) and Deuring's CM reduction theorem; a published computational reference for the CM discriminant is the SageMath elliptic-curve documentation: https://doc.sagemath.org/pdf/en/reference/arithmetic_curves/arithmetic_curves.pdf.
