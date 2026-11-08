# Normalization and embedded Jacobian structure of the reduced characteristic-two quintic discriminant

## Finding

Let \(k\) be an algebraically closed field of characteristic two and put
\[
f(T)=T^5+aT^4+bT^3+cT^2+dT+e,
\qquad (a,b,c,d,e)\in\mathbb A_k^5.
\]
The ordinary integral polynomial discriminant, reduced to \(k\), equals \(H^2\), where
\[
H=a^2d^2+ab^2e+abcd+bce+c^2d+e^2.
\]
The **reduced** discriminant \(Y=V(H)\) is an integral fourfold. Set \(U=e+ad\) and \(V=c+ab\). This triangular polynomial automorphism gives
\[
\mathcal O(Y)\cong k[a,b,d,U,V]/(U^2+bUV+dV^2).
\]
Its reduced singular locus is the smooth irreducible threefold \(Z=V(U,V)\cong\mathbb A^3_{a,b,d}\). The scheme-theoretic Jacobian singular locus has ideal, inside \(\mathcal O(Y)\),
\[
J=(U^2,UV,V^2,bU,bV)
  =(U,V)\cap(b,(U,V)^2).
\]
In particular, the Jacobian scheme has an embedded associated prime \((b,U,V)\); it is reduced over \(b\ne0\).

The normalization is the affine four-space \(\mathbb A^4_{a,b,R,V}\), via
\[
\nu(a,b,R,V)=(a,b,d=R^2+bR,U=RV,V).
\]
Its conductor in \(\mathcal O(Y)\) is exactly \((U,V)\). Over the conductor locus the normalization induces the degree-two cover \(R^2+bR=d\), generically separable when \(b\ne0\), and purely inseparable along \(b=0\).

The singular quintics are exactly those expressible as
\[
f(T)=(T+a)(T^4+bT^2+d).
\]
Over \(k\) the quartic factor is a square of a quadratic. In contrast, a quintic with one triple root and two other distinct roots need not lie in \(\operatorname{Sing}(Y)\). Finally, over any finite field \(\mathbb F_q\) of characteristic two, \(\#Y(\mathbb F_q)=q^4\) and \(\#Z(\mathbb F_q)=q^3\).

## Assumptions and scope

All scheme structures refer to the **reduced** discriminant \(Y=V(H)\), not the nonreduced degree-eight hypersurface cut out by the original polynomial discriminant \(H^2\). Coordinates describe the affine space of monic degree-five polynomials; no quotient by projective linear transformations is taken. The normalization map and conductor are asserted globally over \(k\), including all boundary values \(b=0\).

## Proof

**1. Discriminant and integral equation.** In characteristic two, \(f'(T)=T^4+bT^2+d\), a perfect square over \(k\). The resultant identity or exact expansion of the integral polynomial discriminant gives \(\operatorname{Disc}(f)=H^2\). Substituting \(c=V+ab\), \(e=U+ad\) expands \(H\) to \(U^2+bUV+dV^2\). View this expression as a primitive degree-one polynomial in \(d\) over \(k[a,b,U,V]\): the coefficient \(V^2\) is coprime to \(U^2+bUV\), so it is irreducible by Gauss's lemma. Thus \(Y\) is integral.

**2. Reduced and scheme-theoretic singular loci.** The derivatives of \(H=U^2+bUV+dV^2\) with respect to \(a,b,d,U,V\) are \((0,UV,V^2,bV,bU)\). Modulo \((H)\), the first two nonzero generators imply \(U^2=0\) as well. Hence the Jacobian ideal is \((U^2,UV,V^2,bU,bV)\). Its radical is \((U,V)\). Since \(b\) is independent of \(U,V\), the elementary ideal identity \((U,V)^2+b(U,V)=(U,V)\cap(b,(U,V)^2)\) holds, giving the embedded component. Every point with \(U=V=0\) has \(H=0\), and the quotient coordinate ring is \(k[a,b,d]\).

**3. Finite birational normalization.** Let \(B=k[a,b,d,U,V]/(H)\) and \(S=k[a,b,R,V]\), with \(d\mapsto R^2+bR\) and \(U\mapsto RV\). These assignments respect \(H\). The element \(R\) satisfies the monic equation \(R^2+bR+d=0\) over \(B\), so \(S=B[R]\) is finite over \(B\). On \(V\ne0\), \(R=U/V\), and the two rings agree; since \(B\) is a domain, the map is birational and injective. The target \(S\) is a polynomial ring and thus normal, so it is the integral closure of \(B\).

**4. Conductor.** Write \(P=k[a,b,d]\). Since \(R^2+bR=d\), \(S=P[V]\oplus R P[V]\) is free of rank two over \(P[V]\). The image \(B\) equals \(P[V]\oplus RV P[V]\): every power of \(U=RV\) reduces using \(U^2+bUV+dV^2=0\), while the directness follows from the preceding basis. Therefore \(S/B\cong P\cdot\overline R\), killed by \(V\) and \(U\) but by no nonzero element of \(P\). The conductor \(\operatorname{Ann}_B(S/B)\) is exactly \((U,V)\). The preimage of its support in \(S\) is \(V=0\), with ring \(k[a,b,R]\), and the map to \(k[a,b,d]\) is \(d=R^2+bR\), generically étale for \(b\ne0\) and purely inseparable over \(b=0\).

**5. Root geometry and transverse branches.** The equations \(U=V=0\) translate to \(c=ab\), \(e=ad\), so \(f=(T+a)(T^4+bT^2+d)\). Since \(k\) is algebraically closed and characteristic two, the quartic is \((T^2+\sqrt b\,T+\sqrt d)^2\). At the generic point of \(Z\) with \(b\ne0\), the quadratic form \(U^2+bUV+dV^2\) factors into two distinct transverse linear forms after an algebraic extension of the residue field, giving two normal branches. For comparison, choose \(\lambda\notin\{0,1\}\) and \(f=T^3(T+1)(T+\lambda)\). It has \(b=\lambda\), \(c=d=e=0\), \(a=1+\lambda\), hence \(U=0\), \(V=\lambda(1+\lambda)\ne0\). The derivative of \(H\) in \(d\) equals \(V^2\ne0\), so this triple-root polynomial represents a smooth point of \(Y\).

**6. Rational-point count.** Over \(\mathbb F_q\), when \(V=0\) the equation forces \(U=0\), contributing \(q^3\) points in \((a,b,d)\). When \(V\ne0\), choose \((a,b,U,V)\) arbitrarily and solve uniquely \(d=(U^2+bUV)/V^2\), contributing \(q^3(q-1)\). Thus \(\#Y(\mathbb F_q)=q^4\), and \(Z\cong\mathbb A^3\) has \(q^3\) points.

## Verification

The accompanying self-contained script `verify_quintic.py` uses exact polynomial arithmetic to compute the integer quintic discriminant modulo two, test its square identity, verify the triangular-coordinate equation, test the integral normalization relation, and derive the partial derivatives. It also exhausts all \(4^5=1024\) monic quintics over \(\mathbb F_4\), checking equality of reduced-discriminant membership with nonsquarefreeness. It returns 768 squarefree polynomials, 256 discriminant points, and 64 reduced singular points. The calculation is supporting evidence for polynomial identities, not a replacement for the general algebraic proof of normalization or conductor.

## Relationship to prior work

Krishnamoorthy, Shaska, and Voelklein, *Invariants of Binary Forms* (arXiv:1209.0446, posted September 3, 2012), examine binary-form invariants in characteristics covered by their approach, specifically \(p>5\). Their formulas do not establish characteristic-two normalization or a conductor. Du Plessis and Wall, *The moduli space of binary quintics* (online November 1, 2017, DOI:10.1007/s40879-017-0187-8), Section 6, explicitly establish that the characteristic-two quintic discriminant is the square of an invariant \(i_4\), and analyze binary-quintic moduli and repeated-root normal forms. The square-discriminant observation itself is established literature, not the claimed contribution. Their characteristic-two section does not state this affine reduced discriminant's normalization, conductor, or embedded Jacobian scheme. The claimed extension is that full scheme-theoretic and birational package for the unquotiented monic coefficient space; it is not inferred merely from a search without matches.

## Limitations

No projective compactification, global \(\mathrm{PGL}_2\)-quotient normalization, test-ideal calculation, or resolution of the inseparable boundary is claimed. The normalization is for the reduced affine discriminant only; the un-reduced hypersurface \(H^2=0\) has a different scheme structure. Historical priority relative to unindexed or earlier general normalization results is not independently established.

## References

1. V. Krishnamoorthy, T. Shaska, H. Voelklein, *Invariants of Binary Forms*, arXiv:1209.0446, original arXiv posting September 3, 2012, https://arxiv.org/abs/1209.0446.
2. A. du Plessis and C. T. C. Wall, *The moduli space of binary quintics*, European Journal of Mathematics 4 (2018), 423–436, first online November 1, 2017, https://doi.org/10.1007/s40879-017-0187-8 (Section 6).
