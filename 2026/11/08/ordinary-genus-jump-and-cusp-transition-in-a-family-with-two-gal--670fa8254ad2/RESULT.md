# Ordinary genus jump and cusp transition in a family with two Galois points

## Finding

For any odd prime \(p\), let \(k\) be algebraically closed of characteristic \(p\) and let \(c\in k^\times\). Consider the projective closure \(C_c\subset\mathbb P^2_k\) of
\[
(x^p-x)^2-(y^p-cy)^2+1=0.
\]
Write \(\widetilde C_c\) for its smooth normalization and \(f(\widetilde C_c)\) for the Jacobian \(p\)-rank. The complete classification is
\[
\boxed{(g(\widetilde C_c),f(\widetilde C_c))=\begin{cases}((p-1)^2,(p-1)^2),&c=1,\\(p^2-1,p^2-1),&c\ne1.\end{cases}}
\]
Hence every normalized curve is ordinary, even though the genus and \(p\)-rank rise by \(2(p-1)\) across the nonexceptional parameters.

The plane curve is geometrically irreducible and has exactly two singular points \(P_+=[1:1:0]\) and \(P_-=[-1:1:0]\). At \(c=1\) each is an ordinary \(p\)-fold singularity, with exactly \(p\) distinct branches and delta invariant \(p(p-1)/2\). For \(c\ne1\), each is a single-branch cusp of multiplicity \(p-1\), with tangent intersection multiplicity \(p\) and delta invariant \((p-1)(p-2)/2\). No claim is made that the entire formal analytic germ is determined by these numerical invariants.

More precisely, \(\widetilde C_c\) carries an elementary-abelian Galois cover \(\widetilde C_c\longrightarrow\mathbb P^1_t\) of degree \(p^2\), branched only above \(t=0,\infty\). Both inertia groups have order \(p\) if \(c=1\), but order \(p^2\) if \(c\ne1\). Each nontrivial local character has Swan conductor one. The number of geometric points above each of the two branch points is consequently \(p\), respectively one.

## Assumptions and scope

The prime \(p\) is odd and \(c\) is nonzero; the two additive polynomials must be separable. Geometric genus and \(p\)-rank refer to the smooth projective normalization, not the singular plane model. The two displayed points \(P_\pm\) are defined over the prime field, irrespective of \(c\). The parameter is not asserted to parametrize distinct unmarked isomorphism classes.

## Proof

**A degree-\(p^2\) cover.** Set \(A=x^p-x\) and \(B=y^p-cy\). The defining equation reads \(B^2-A^2=1\). Thus the rational function \(t=B+A\) is nonzero and satisfies \(t^{-1}=B-A\). Because \(p\ne2\),
\[
A=\frac{t-t^{-1}}2,\qquad B=\frac{t+t^{-1}}2.
\]
Choose \(\beta\in k^\times\) with \(\beta^{p-1}=c\), put \(Y=y/\beta\) and \(\alpha=\beta^{-p}\). Then \(k(C_c)\) is generated over \(k(t)\) by the two Artin–Schreier equations
\[
x^p-x=\frac{t-t^{-1}}2,\qquad Y^p-Y=\alpha\frac{t+t^{-1}}2.
\tag{1}
\]
For \((r,s)\in\mathbb F_p^2\), the associated Artin–Schreier class is represented by
\[
\frac{(r+s\alpha)t+(-r+s\alpha)t^{-1}}2.
\tag{2}
\]
If both pole coefficients vanish, then \(r=s=0\), since \(p\) is odd and \(\alpha\ne0\). Every nonzero class therefore has a simple pole. An Artin–Schreier coboundary cannot have a simple pole, so the classes in (1) are independent. The compositum is a function field of degree \(p^2\) with Galois group \((\mathbb Z/p)^2\). In particular \(C_c\) is geometrically integral. Only \(t=0,\infty\) can ramify.

**The inertia dichotomy.** The two coefficients in (2) at \(\infty\), respectively at \(0\), are \((r+s\alpha)/2\) and \((-r+s\alpha)/2\). One is zero for a nonzero pair \((r,s)\in\mathbb F_p^2\) precisely when \(\alpha\in\mathbb F_p\). But \(\alpha\in\mathbb F_p\) is equivalent to \(c=1\): if \(\beta^p\in\mathbb F_p\), uniqueness of \(p\)-th roots gives \(\beta\in\mathbb F_p\), hence \(c=\beta^{p-1}=1\); the converse is immediate. For \(c\ne1\), the local Artin–Schreier classes at each pole span rank two over \(\mathbb F_p\); inertia is all of \((\mathbb Z/p)^2\). For \(c=1\), their local rank is one and the inertia has order \(p\). Every nonzero local class has pole order one, so each nontrivial inertia character has Swan conductor one. The lower ramification filtration consequently has a single positive break at one, and a point with inertia of order \(e\) contributes different exponent \(2(e-1)\).

**Genus and \(p\)-rank.** If \(c\ne1\), there is one point above each branch location and each contributes \(2(p^2-1)\) to the different. Riemann–Hurwitz gives
\[
2g-2=-2p^2+4(p^2-1)=2p^2-4,
\]
so \(g=p^2-1\). Deuring–Shafarevich gives
\[
f-1=-p^2+2(p^2-1)=p^2-2,
\]
so \(f=p^2-1\). If \(c=1\), there are \(p\) points over each of the two branch locations, each of inertia \(p\) and different exponent \(2(p-1)\). Thus
\[
2g-2=-2p^2+4p(p-1)=2p^2-4p,
\]
so \(g=(p-1)^2\), while
\[
f-1=-p^2+2p(p-1)=p^2-2p,
\]
so \(f=(p-1)^2\). Both cases are ordinary.

**Plane singularities.** The homogenization is
\[
F=(X^p-XZ^{p-1})^2-(Y^p-cYZ^{p-1})^2+Z^{2p}.
\]
In the affine chart \(Z\ne0\), derivatives are \(F_x=-2(x^p-x)\) and \(F_y=2c(y^p-cy)\). Their simultaneous vanishing contradicts \(F=0\). On \(Z=0\), the reduced support of \(F\) is the two points \(P_\pm\). The map \(t\) sends the branches above \(t=\infty\) to \(P_+\), and those above \(t=0\) to \(P_-\). At \(P_+\) use coordinates \(X=1+u,Y=1,Z=w\). The local equation is
\[
\left(u^p+(c-1)w^{p-1}-uw^{p-1}\right)
\left(2+u^p-(1+c)w^{p-1}-uw^{p-1}\right)+w^{2p}=0.
\]
If \(c=1\), the initial homogeneous form is a nonzero scalar times \(u^p-uw^{p-1}=\prod_{a\in\mathbb F_p}(u-aw)\). This gives \(p\) distinct smooth branches and an ordinary \(p\)-fold point. The involution \(X\mapsto-X\) gives the same statement at \(P_-\). If \(c\ne1\), the lowest-degree term is a nonzero multiple of \(w^{p-1}\); hence multiplicity is \(p-1\) and the unique tangent is \(w=0\). The inertia result proves that exactly one normalization branch lies over each singular point. Restricting \(F\) to \(w=0\) gives tangent intersection multiplicity \(p\) at either point. The arithmetic genus of the integral degree-\(2p\) plane curve is \((2p-1)(p-1)\). The singularities are exchanged by \(X\mapsto-X\), so each has the same delta invariant. The genus formula above yields
\[
\delta(P_\pm)=\frac{(2p-1)(p-1)-(p^2-1)}2=\frac{(p-1)(p-2)}2.
\]
This establishes the asserted cusp data and completes the classification.

## Verification

The standalone finite-field checker `verify.py` requires only Python 3 and uses exact polynomial arithmetic with fixed irreducible polynomials over \(\mathbb F_3\). It computes projective-point counts of the normalization over \(\mathbb F_{3^n}\), via the explicit fiber product (1), for \(n=1,\ldots,4\) when \(c=1\) and \(n=1,\ldots,8\) when \(c=2\). The first halves of the respective zeta numerators are
\[
(1,2,9,14,40),\qquad (1,4,22,60,201,432,1094,1928,3956).
\]
The final coefficients \(40\) and \(3956\) are nonzero modulo three, consistent with ordinarity in genus four and eight respectively. The program independently expands local homogenized equations at both singular points for \(p=3,5,7\), checking the predicted multiplicities and leading tangent forms in the cases \(c=1\) and \(c=2\). Output is provided in `verification_output.txt`. The all-primes claims follow from the proof, not the finite tests.

## Relationship to prior work

Fukasawa, *A family of plane curves with two or more Galois points in positive characteristic*, arXiv:1308.1490 (first posted August 7, 2013), constructs the ambient family of plane curves and proves irreducibility, the two singular points, and general lower genus bounds. When \(\ell=2\), \(q=p\), and the linearized polynomials are \(x^p-x\) and \(y^p-cy\), the equality case of the genus bound is exactly \(c=1\). Its non-equality case gives only \(g\ge p^2-p+1\), whereas the present explicit classification gives \(g=p^2-1\), with complete inertia, cusp and \(p\)-rank profiles.

Arakelian and Korchmáros (arXiv:1501.02616) treat the classical Artin–Mumford curve, corresponding after a linear coordinate change to the exceptional \(c=1\) case; the latter ordinary genus and the elementary-abelian action are established prior knowledge. Van der Geer and van der Vlugt (1995) give general genus additivity for fiber products of Artin–Schreier covers. That general machinery provides an alternative route to the numerical genus once the new parameter-dependent pole-cancellation calculation is made, but their inspected paper does not state this specific family classification or its plane cusp transition. Montanucci and Zini (arXiv:1612.01731, first posted December 2016) study products of linearized polynomials, of genus \((p-1)^2\) in the prime-degree case, and do not describe the non-product \(c\ne1\) plane curves of genus \(p^2-1\).

## Limitations

No assertion is made concerning complete analytic equivalence types, the full automorphism groups, nontrivial geometric isomorphisms among distinct parameters \(c\), the Newton polygons beyond the ordinary property, or exact zeta functions for arbitrary \(c\). Originality has not received independent validation. General Artin–Schreier fiber-product results encode ingredients of the calculation; unpublished or unindexed evaluations of this precise family remain a historical-priority possibility.

## References

1. S. Fukasawa, *A family of plane curves with two or more Galois points in positive characteristic*, arXiv:1308.1490 (2013), https://arxiv.org/abs/1308.1490.
2. G. van der Geer and M. van der Vlugt, *Fibre Products of Artin–Schreier Curves and Generalized Hamming Weights of Codes*, J. Combin. Theory Ser. A 70 (1995), 337–348, DOI:10.1016/0097-3165(95)90099-3.
3. N. Arakelian and G. Korchmáros, *A characterization of the Artin–Mumford curve*, arXiv:1501.02616 (2015), https://arxiv.org/abs/1501.02616.
4. M. Montanucci and G. Zini, *Generalized Artin–Mumford curves over finite fields*, arXiv:1612.01731 (2016), https://arxiv.org/abs/1612.01731.
