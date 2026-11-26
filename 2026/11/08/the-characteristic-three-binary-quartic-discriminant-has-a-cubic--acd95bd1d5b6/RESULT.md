# The singular scheme of the binary quartic discriminant in characteristic three

## Finding

Let \(k\) be any field of characteristic \(3\). Use the unscaled coefficients \([a:b:c:d:e]\) of \(f=aX^4+bX^3Y+cX^2Y^2+dXY^3+eY^4\) on \(\mathbb P^4_k\). Let \(\Delta\) be the integral discriminant reduced modulo \(3\), and let \(Z\) be the scheme of singularities of \(V(\Delta)\), defined by \(\Delta\) and its five first partial derivatives. Put \(T=V(c,ae-bd)\) and define \(E\) to be the scheme-theoretic image of the morphism
\[
\mathbb P^2_k\longrightarrow\mathbb P^4_k,\qquad [A:B:C]\longmapsto [A^2:2AB:B^2+2AC:2BC:C^2].
\]
In particular \(E\) is not defined as the closure of the set of squares of quadratics with coefficients in \(k\). Geometrically, \(T\) is the triple-root surface and \(E\) is the surface of squares of quadratics, including the quadruple-root locus. Then
\[
\mathcal I_Z=\mathcal I_T^{\,3}\cap\mathcal I_E
\]
as ideal sheaves on all of \(\mathbb P^4_k\), with the ordinary ideal-sheaf power. The smooth surfaces \(T\) and \(E\) have degrees \(2\) and \(4\), respectively. The transverse algebra at the generic point of \(T\) has basis \(1,c,v,c^2,cv,v^2\) in the local coordinates below, hence length \(6\). The component at the generic point of \(E\) is reduced. There are no embedded associated components, and \(\deg Z=6\cdot 2+4=16\).

## Proof

**Normal form.** On \(a=1\), put \(x=X/Y=z-b\). The equation becomes \(z^4+cz^2+uz+v\), where \(u=d-b^3+bc\) and \(v=e+b^2c-bd\). These are polynomial coordinate changes. The derivative in \(z\) is \(h=z^3-cz+u\); subtracting \(zh\) from the quartic gives \(v-cz^2\). The monic quartic discriminant is the resultant with \(h\), which is \(\operatorname{Res}(h,v-cz^2)\). To evaluate it, over the fraction field take \(r^2=v/c\); it equals \((-c)^3 h(r)h(-r)\). The resulting polynomial identity also holds for \(c=0\):
\[
\Delta=v(v-c^2)^2-c^3u^2.
\]
Although Euler does not put \(\Delta\) in its gradient ideal in characteristic three, on this chart it does express \(\partial_a\Delta\) in terms of the other four partials. After the coordinate change, set \(w=v-c^2\). The partial derivatives in \(c,u,v\) are \(-cvw,c^3u,-c^2w\), and the equation, modulo \(c^3u\), is \(vw^2\). Thus the singular ideal is \(J=(c^2w,cvw,c^3u,vw^2)\), with \(b\) a free coordinate.

**Decomposition.** Write \(\mathfrak m=(c,v)\). The initial form of \(w\) for the \(\mathfrak m\)-adic filtration is \(v\), a non-zero-divisor in the associated graded ring. Hence \((\mathfrak m^3:w)=\mathfrak m^2\), and reducing modulo \(u\) gives \(\mathfrak m^3\cap(u,w)=u\mathfrak m^3+w\mathfrak m^2\). In \(J\) one has \(v^2w=vw^2+c^2vw\), so \(w\mathfrak m^2\subset J\). Starting with \(uc^3\in J\), multiply \(c^2w,cvw,v^2w\) by \(u\) in turn to obtain \(uc^2v,ucv^2,uv^3\) modulo the preceding terms. Thus \(u\mathfrak m^3\subset J\). Every generator of \(J\) belongs to the displayed sum, proving
\[
J=(c,v)^3\cap(u,v-c^2).
\]
The first component is primary with prime \((c,v)\), since the quotient is the polynomial ring in the other variables with coefficients in the truncated \((c,v)\)-algebra. More explicitly, an element with nonzero reduction in \(k[b,u]\) acts injectively on its associated graded free \(k[b,u]\)-module and hence on the quotient. The second component is prime.

**Identification and globalization.** The ideal of \(T\) on \(a=1\) is \((c,v)\). Geometrically a form with a triple root is \((\alpha X+\beta Y)^3(\gamma X+\delta Y)\), so \(c=0\) and the two-by-two matrix with rows \((a,b)\) and \((d,e)\) has rank one. Conversely, geometrically every such rank-one matrix has this form by taking cube roots of the entries of its column factor.

On the inverse image of \(a\ne0\) under the morphism defining \(E\), normalize the leading coefficient of the quadratic to \(1\). In the depressed variable \(z\) the square has no cubic term, so the monic quadratic has no linear term: it is \(z^2+C'\). Its coefficients give \(u=0\), \(c=2C'\), \(v=(C')^2=c^2\). Conversely, on the subscheme defined by these equations the square comes uniquely from \(z^2+c/2\); changing back by \(z=x+b\) yields the inverse morphism. This computation is valid in coefficient rings, not just on field-valued points.

The discriminant singular scheme, the rank-one triple-root surface, and the square morphism are invariant under invertible changes of \((X,Y)\). Over an algebraic closure the translates of \(a\ne0\) cover all of projective coefficient space, since a nonzero quartic does not vanish at every geometric point. The chart calculation on squares therefore proves that the morphism defining \(E\) is a closed immersion onto its image; in particular its formation commutes with the field extensions used here. The ideal-sheaf equality and absence of embedded components follow on these charts, and the equality, closed immersion and smoothness descend by faithful flatness. The smooth quadric \(T\) has degree \(2\), and the pullback of \(\mathcal O(1)\) to \(E\simeq\mathbb P^2_k\) is \(\mathcal O(2)\), giving degree \(4\). Localizing at the two generic points gives lengths \(6\) and \(1\); the degree follows from the fundamental cycle \(6[T]+[E]\).

## Verification and scope

The symbolic verifier `verify.py` in the record checks the local discriminant and Tjurina identities and the two containments of the affine ideal equality. The chart argument above supplies the global and arbitrary-field assertions. This is a statement about ideal sheaves and about the full singular scheme; it does not follow from the derivative ideal alone in characteristic three.

## Relationship to prior work

The reduced supports in characteristic three are described in *A Segre–Veronese singular locus for the binary-quartic discriminant in characteristic three* (Resultary, `6f35b4062788`). The claim here is the full scheme structure, including the ordinary cubic thickening along the triple-root surface even where it meets the other component, not the description of those supports. Chipalkatti, *On equations defining coincident root loci*, [arXiv:math/0110224](https://arxiv.org/abs/math/0110224), Theorem 5.4, treats singular supports over \(\mathbb C\). D’Andrea and Chipalkatti, *On the Jacobian ideal of the binary discriminant*, [arXiv:math/0601705](https://arxiv.org/abs/math/0601705), Proposition 4.1 and Remark 6.8, give the quartic decomposition in characteristic zero. Its triple-root surface has degree \(6\) and generic Jacobian length \(2\), unlike the degree \(2\) and generic length \(6\) here. No historical priority over all modular invariant-theory sources is asserted.
