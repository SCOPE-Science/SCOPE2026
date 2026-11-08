# Wild conductor geometry of the binary-quartic discriminant in characteristic two

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\). On the coefficient space \(\mathbb P^4_k\) of binary quartics
\[
f=aX^4+bX^3Y+cX^2Y^2+dXY^3+eY^4,
\]
put \(Q=ad^2+bcd+eb^2\). The integral quartic discriminant reduces in characteristic two to \(Q^2\). Its reduced support \(D=V(Q)\) is an irreducible nonnormal cubic threefold, singular along exactly the plane \(P=V(b,d)\). Its normalization is the smooth Segre product \(\mathbb P^1\times\mathbb P^2\) via
\[
\nu([s:t],[u:v:w])=[su:sw:tu+sv:tw:tv].
\]
The conductor ideal sheaf in \(\mathcal O_D\) is exactly the ideal \(\mathcal I_{P/D}=(b,d)\), and its pullback/conductor on the normalization cuts out \(C=V(w)\cong\mathbb P^1\times\mathbb P^1\). The restricted finite degree-two map \(C\to P\cong\mathbb P^2\) is the unordered-pair (symmetric-square) quotient
\[
([s:t],[u:v])\longmapsto[su:tu+sv:tv].
\]
It is étale away from the line \(L=V(c)\subset P\). Its ramification locus is the diagonal in \(C\), and the map from that diagonal to \(L\) is the absolute Frobenius \([s:t]\mapsto[s^2:t^2]\), a purely inseparable morphism of degree two.

A different inseparability occurs over the generic point of \(D\): the incidence variety of a quartic and one of its repeated roots maps finitely and *purely inseparably of degree two* onto \(D\). In particular this natural root incidence is not the normalization, despite its being smooth. For every finite field \(\mathbb F_q\) with \(q=2^m\), \(m\ge1\),
\[
\#D(\mathbb F_q)=q^3+2q^2+q+1.
\]
This last count is a consequence of the normalization and is included as a checkable corollary, not as a distinct new invariant.

## Assumptions and scope
The geometric statements are over an algebraically closed field of characteristic two; the point-count statement uses its finite subfields. All varieties are reduced unless their scheme-theoretic multiplicity is expressly stated. The quartic discriminant refers to the integral discriminant polynomial (the primitive resultant discriminant), rather than the polynomial defining its reduced divisor. \(D\) is the reduced discriminant support, whereas the specialized Cartier discriminant is \(2D\). The conductor is \(\operatorname{Ann}_{\mathcal O_D}(\nu_*\mathcal O_{\mathbb P^1\times\mathbb P^2}/\mathcal O_D)\).

## Proof
**1. Discriminant and singularities.** The classical integral quartic invariant
\[
J=72ace-27ad^2-27eb^2+9bcd-2c^3
\]
reduces modulo two to \(Q\). The integral discriminant \((4I^3-J^2)/27\), where \(I=12ae-3bd+c^2\), therefore reduces to \(Q^2\). The identity also follows from direct resultant expansion, avoiding division after reduction. The five partial derivatives of \(Q\), in the order \((a,b,c,d,e)\), are
\[
(d^2,\,cd,\,bd,\,bc,\,b^2),
\]
so the singular support is \(P=V(b,d)\). Irreducibility follows from the explicit birational parametrization below (equivalently, \(Q\) is primitive and linear in \(a,e\)). Since \(P\) has codimension one in \(D\), \(D\) is nonnormal.

**2. Finite birational normalization.** The displayed map \(\nu\) is a morphism because its five coordinates never vanish simultaneously. Substitution into \(Q\) gives zero identically. For \((b,d)\ne(0,0)\), the first source coordinate satisfies \([s:t]=[b:d]\), and the remaining source coordinates are uniquely recovered from \((a,b,c,d,e)\); hence \(\nu\) is an isomorphism above \(D\setminus P\). Above \([a:0:c:0:e]\in P\), the possible \([s:t]\) satisfy
\[
at^2+cst+es^2=0.
\]
That binary quadratic is nonzero and has finitely many roots over \(k\), so \(\nu\) is quasi-finite. It is projective, hence finite. Its source is smooth, and its generic degree is one; therefore it is the normalization.

**3. Conductor, including its thickness.** On the chart \(a=1\), write
\[
R=k[b,c,d,e]/(d^2+bcd+eb^2),\quad A=k[b,c,e].
\]
The normalized chart is \(B=A[\lambda]/(\lambda^2+c\lambda+e)=k[b,c,\lambda]\), with \(d=b\lambda\). As \(A\)-modules, \(B=A\oplus A\lambda\) and \(R=A\oplus bA\lambda\). Direct multiplication by \(\lambda\) shows
\[
(R:B)=bA\oplus bA\lambda=(b,d)\subset R,
\]
and the corresponding ideal in \(B\) is \(bB\). The same calculation after exchanging the extreme coefficients covers the chart \(e\ne0\). The remaining points of \(P\) satisfy \(a=e=0,c\ne0\); there the normal quadratic slice \(ad^2+cbd+eb^2\) in \((b,d)\) has nonzero mixed coefficient, and the completed germ splits into two transverse smooth branches. Its conductor is the reduced double-locus ideal \((b,d)\). Indeed, in the completed coefficient ring where \(c=1\), there is a unique formal unit \(\delta\) satisfying \(\delta=1+ae\delta^2\) and \(\delta\equiv1\pmod{(a,e)}\). The exact factorization \(ad^2+bd+eb^2=\delta^{-1}(b+a\delta d)(d+e\delta b)\) exhibits two transverse smooth formal branches. Thus these calculations cover all of \(D\), proving the global conductor statement. In the displayed Segre coordinates \(b=sw,d=tw\), so its inverse-image ideal is \((w)\), defining \(C\).

**4. Wild conductor map.** On \(C\) the image polynomial is
\[
aT^2+cTS+eS^2=(sT+tS)(uT+vS).
\]
Thus \(C\to P\) is the quotient of ordered pairs of linear forms by their transposition. On \(a=1\) its coordinate algebra is \(k[c,\lambda]\) over \(k[c,e]\), with \(e=\lambda^2+c\lambda\). It is free of rank two and has derivative \(c\); it is therefore étale for \(c\ne0\). At \(c=0\), the two factors coincide. Restricting the diagonal \([s:t]=[u:v]\) gives \([a:c:e]=[s^2:0:t^2]\), the Frobenius map onto the branch line. This accounts for the nonreduced branching without claiming that the entire conductor map is inseparable: it is generically separable of degree two.

**5. Repeated-root incidence and arithmetic.** On the affine chart \(Y=1\), the derivative of the quartic with respect to \(X\) is \(bX^2+d\). At a general point of \(D\), with \(b\ne0\), the repeated root \(r\) satisfies \(r^2=d/b\), and the equation \(f(r)=0\) is then exactly \(Q/b^2=0\). Since \(d/b=t/s\) in \(k(\mathbb P^1\times\mathbb P^2)\), and \(t/s\) is not a square in that rational function field, adjoining \(r\) gives a purely inseparable extension of degree two. The incidence is a projective-plane bundle over the parameter \(r\in\mathbb P^1\) (two independent linear coefficient conditions), hence smooth, and its projection to \(D\) is proper and quasi-finite and therefore finite. Finally, \(\nu\) is a bijection off \(P\); over \(P\), replace the conductor \(C\) by \(P\) in counting rational points. Thus
\[
\#D(\mathbb F_q)=\#(\mathbb P^1\times\mathbb P^2)(\mathbb F_q)-\#(\mathbb P^1\times\mathbb P^1)(\mathbb F_q)+\#\mathbb P^2(\mathbb F_q)
=q^3+2q^2+q+1.
\]

## Verification
The included standalone \(verify.py\) computes the integral univariate quartic discriminant symbolically and checks its characteristic-two square reduction; independently checks the reduction of \(J\), the Segre parametrization, and the conductor factorization; and enumerates all \(\mathbb F_q\)-rational points of the projective cubic for \(q=2,4,8,16\) with exact binary-field arithmetic. The recorded output concludes with `ALL_CHECKS_PASSED`. The general conductor argument and inseparability proof are algebraic, not deduced from finite tests.

## Relationship to prior work
The cubic \(Q\) and its role as the repeated-root invariant of characteristic-two binary quartics are recorded explicitly by du Plessis and Wall, Section 6.2 of *The moduli space of binary quintics* (2017); these facts are not presented as new. Gondim and Russo, *On cubic hypersurfaces with vanishing Hessian*, Example 1 and Theorem 4.2 (first posted 2013), identify the classical Perazzo cubic and its external Segre projection in characteristic zero. Neither the existence of this classical cubic nor the abstract Segre projection is claimed as new. The contribution here is the explicit *characteristic-two discriminant interpretation combined with its precise conductor ideal, the separable versus Frobenius branching of the conductor cover, and the distinct generically purely inseparable repeated-root incidence*. The previous results in these sources do not assert that package, and the local conductor calculation supplies an independent proof rather than relying on a characteristic-zero argument.

## Limitations
The geometric theorem is formulated over an algebraically closed field of characteristic two. The arithmetic count is for projective coefficient tuples, not projective equivalence classes of quartics. It is not claimed that the formulas for the quartic invariant, the Perazzo cubic, or its Segre projection are new. Possible older specialist descriptions of the conductor or binary-quartic incidence remain a historical-priority risk; no independent audit is asserted. Computations for finite fields do not prove the formulas for all fields.

## References
1. R. Gondim and F. Russo, *On cubic hypersurfaces with vanishing Hessian*, arXiv:1312.1618, first public version 5 December 2013, especially Example 1 and Theorem 4.2. https://arxiv.org/abs/1312.1618
2. A. du Plessis and C. T. C. Wall, *The moduli space of binary quintics*, European Journal of Mathematics (2017/2018), Section 6.2 (binary quartics in characteristic two). https://doi.org/10.1007/s40879-017-0187-8
3. L. Fiorindo, E. Mezzetti and R. M. Miró-Roig, *Perazzo 3-folds and the weak Lefschetz property*, Journal of Algebra 626 (2023), 56–81. https://doi.org/10.1016/j.jalgebra.2023.03.008 (abstract consulted; full article not inspected).
