# Frobenius-scroll normalization and square conductor of the characteristic-three Schur quartic

## Finding

For the **fixed coefficientwise integral model** of Schur's quartic
\[
 x^4-xy^3=z^4-zw^3,
\]
reduction to characteristic \(3\) gives a nonnormal ruled quartic. Its normalization, conductor, complete geometric line set, and point counts over all finite extensions are determined simultaneously:

\[
 \widetilde S\cong\mathbb F_2,\qquad
 \mathfrak c_{\widetilde S/S}=\mathcal I_L^2,\qquad
 \#S(\mathbb F_{q^m})=(q^m+1)^2.
\]

There are exactly two distinguished directrix lines and one \(\mathbb P^1\)-family of rulings (set-theoretically). The singular scheme is a complete intersection of two cubics supported on a line, of degree \(9\) and arithmetic genus \(10\). The formula is not asserted for a separately chosen *good-reduction model* of the smooth generic Schur quartic.

## Assumptions and scope

Let \(k\) be a field of characteristic \(3\), with algebraic closure \(\bar k\), and let \(S\subset\mathbb P^3_k\) be the hypersurface defined by precisely the integral polynomial displayed above. Set
\[
 X=x,\quad Z=z,\quad U=x-y,\quad V=z-w.
\]
This is an invertible linear change of projective coordinates, and in characteristic \(3\), the surface is exactly
\[
 S=V(XU^3-ZV^3)\subset\mathbb P^3_{[X:Z:U:V]}.
\]
The two skew lines are \(L=V(U,V)\) and \(L_0=V(X,Z)\). All structural assertions hold for arbitrary \(k\) of characteristic \(3\), while counting statements require finite \(k=\mathbb F_q\) with \(q\) a power of \(3\).

## Proof

**The reduced surface and its singular scheme.** The equation is irreducible: on \(U\ne0\), its affine equation solves for \(X\) uniquely as \(X=Z(V/U)^3\), and the excluded locus \(U=0\) has no surface component. Partial derivatives in \(X,Z,U,V\) are \(U^3,-V^3,0,0\). Since the defining polynomial lies in the ideal \((U^3,V^3)\), the full Jacobian subscheme is
\[
 J=V(U^3,V^3)\subset\mathbb P^3.
\]
The cubics form a homogeneous regular sequence. Thus \(J\) is a complete-intersection multiple structure on \(L\), with degree \(3\cdot3=9\) and arithmetic genus \(1+\tfrac12(3\cdot3)(3+3-4)=10\). Its Hilbert polynomial is \(9m-9\), and \(S\) is smooth off \(L\).

**Normalization.** Over \(\mathbb P^1_{[s:t]}\), take the rank-two subbundle \(E=\mathcal O(-3)\oplus\mathcal O(-1)\subset\mathcal O^4\) with fibre vectors \((t^3,s^3,0,0)\) and \((0,0,s,t)\). The corresponding map
\[
 \nu:\mathbb P(E)\longrightarrow S,\qquad
 ([s:t],[\lambda:\mu])\longmapsto
 [\lambda t^3:\lambda s^3:\mu s:\mu t]
\]
is everywhere defined and lands on \(S\). Over \(S\setminus L\), the ratio \([s:t]=[U:V]\) recovers the base coordinate, and the map is an isomorphism. On \(L\), the restriction of \(\nu\) to the \(\mu=0\) section is \([s:t]\mapsto[t^3:s^3]\), the degree-three purely inseparable Frobenius map. Thus every geometric fibre is finite, hence the proper morphism \(\nu\) is finite; it is birational and its source is smooth. It is the normalization. Since \(\mathbb P(E)\cong\mathbb P(\mathcal O\oplus\mathcal O(2))\), this normalization is the Hirzebruch surface \(\mathbb F_2\).

**Exact conductor.** On the chart \(Z=1\) near \(L\), write \(a=X/Z\), \(u=U/Z\), \(v=V/Z\). The local ring is
\[
 R=k[a,u,v]/(v^3-au^3)=k[t^3,u,tu]\subset k[t,u]=\widetilde R,
 \quad a=t^3,\ v=tu.
\]
Here \(t=v/u\) is in the fraction field, integral over \(R\), and \(\widetilde R\) is normal. The monomials \(u^j t^e\) in \(R\), considered over \(k[t^3]\), have allowed residues \(e\bmod3\) equal to \(0\) for \(j=0\), \(0,1\) for \(j=1\), and \(0,1,2\) for every \(j\ge2\). It follows by multiplication by \(1,t,t^2\) that the conductor is exactly
\[
 (R:\widetilde R)=(u^2,uv,v^2)=(u,v)^2.
\]
The symmetric chart \(X=1\) gives the same statement, while outside \(L\) normalization is an isomorphism. Hence globally \(\mathfrak c_{\widetilde S/S}=\mathcal I_L^2\) as an ideal of \(\mathcal O_S\); its pullback to \(\widetilde S\) is the square of the ideal of the positive section lying over \(L\).

**All projective lines.** The rulings \(R_{[s:t]}\) are the lines spanned by the two vectors in the normalization formula, and \(L,L_0\) are additional lines. Let an arbitrary geometric line \(\ell\subset S\) be given. If \(U,V\) are linearly independent when restricted to \(\ell\), use them as homogeneous coordinates \([s:t]\) on that line and write \(X=as+bt\), \(Z=cs+dt\). The identity
\[
 (as+bt)s^3-(cs+dt)t^3=0
\]
forces \(a=b=c=d=0\), since the four monomials \(s^4,s^3t,st^3,t^4\) are linearly independent. This yields \(L_0\). If \(U,V\) restrict dependently, \(\ell\) lies in a plane \(tU-sV=0\), whose intersection with \(S\) consists of the triple line \(L\) and the unique ruling \(R_{[s:t]}\). Thus \(\ell=L\) or that ruling. This exhausts the geometric lines and proves there are no unlisted line families.

**Arithmetic.** Over a finite field \(\mathbb F_{q^m}\) of characteristic \(3\), the Frobenius map on \(L\) is bijective on rational points. Therefore \(\nu\) induces a bijection on rational points (it is already an isomorphism off \(L\)). Every \(\mathbb P^1\)-bundle over \(\mathbb P^1\) has \((q^m+1)^2\) rational points, proving the count for \(S\). Exponentiation of all extension-field counts gives
\[
 Z(S/\mathbb F_q,T)=
 \frac1{(1-T)(1-qT)^2(1-q^2T)}.
\]
The disjoint rational directrices contribute \(2(q^m+1)\) points. Thus, for \(W=S\setminus(L\cup L_0)\),
\[
 \#W(\mathbb F_{q^m})=q^{2m}-1,\qquad
 Z(W/\mathbb F_q,T)=\frac{1-T}{1-q^2T}.
\]

## Verification

Run `python3 verify_schur.py` using Python's standard library. The verifier performs independent projective-point enumeration over \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_{27}\), returning respectively \(16,100,784\) points. It enumerates every projective line over \(\mathbb F_3\) and \(\mathbb F_9\) by reduced-row-echelon matrices and tests exact binary quartic coefficients, obtaining respectively \(6\) and \(12\) lines, exactly the two directrices plus all rational rulings. It also tests the exponent-semigroup conductor calculation and the large-degree complete-intersection Hilbert polynomial. The recorded output ends with `CHECK_OK`.

These finite-field checks are corroborations, not proofs of the claims over all fields or of the infinite-extension zeta identities. Those rely on the preceding geometric and algebraic arguments.

## Relationship to prior work

Schur's quartic and its 64-line smooth realization are classical. Rams and Schütt, *64 lines on smooth quartic surfaces*, arXiv:1212.3511 (first public posting 2012-12-14), identify the same integral equation and explicitly distinguish a **different** good-reduction model in characteristic \(3\) isomorphic to the Fermat quartic. Their good-reduction statement does not describe the nonnormal coefficientwise reduction of this particular equation. Polo-Blanco, van der Put and Top, *Ruled quartic surfaces, models and classification*, arXiv:0904.2374 (first public posting 2009-04-15), give a triple-singular-line normal form in §3.1.1 that **already includes the same monomial equation** after specializing their two degree-three forms. The equation and the general idea of the two-directrix ruled geometry are therefore not claimed as novel. Their quartic classification explicitly assumes characteristic zero or greater than three and does not establish the characteristic-three *purely inseparable* directrix, degree-nine Jacobian thickening, exact conductor, or extension-field arithmetic of this coefficientwise specialization. Rams and Schütt, arXiv:1512.01358, also discuss Schur and Fermat models across exceptional characteristics without the conductor or arithmetic assertions above.

The contribution claimed here is the **wild-characteristic structure** of the *fixed-model* special fibre: its ninefold Jacobian scheme, radicial Frobenius normalization with exact square conductor, and extension-field arithmetic. The full line classification is included to make the characteristic-three degeneration transparent, not claimed independently of the earlier ruled-quartic normal form. No universal classification of nonnormal quartics or claim of historical priority is made.

## Limitations

This result applies only to the displayed coefficientwise model in characteristic \(3\), not to every integral model of Schur's smooth generic fibre. Its geometric line classification is set-theoretic and does not determine the nilpotent structure of the Hilbert scheme of lines. The ninefold singular subscheme is the Jacobian singular scheme of this hypersurface, not a statement about the reduced singular line alone. Historical priority against uninspected specialist nonnormal-surface literature remains provisional.

## References

- I. Polo-Blanco, M. van der Put, J. Top, *Ruled quartic surfaces, models and classification*, arXiv:0904.2374, first posted 2009-04-15, https://arxiv.org/abs/0904.2374.
- S. Rams, M. Schütt, *64 lines on smooth quartic surfaces*, arXiv:1212.3511, first posted 2012-12-14, https://arxiv.org/abs/1212.3511.
- S. Rams, M. Schütt, *At most 64 lines on smooth quartic surfaces (characteristic 2)*, arXiv:1512.01358, first posted 2015-12-04, https://arxiv.org/abs/1512.01358.
