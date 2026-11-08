# The maximal-contact locus on cyclic Frobenius plane curves

## Finding

For every prime power \(q=p^r\ge 2\), let \(C_q\subset\mathbb P^2_{\mathbb F_q}\) be the smooth degree-\(q+1\) curve
\[
 C_q:\quad X^qY+Y^qZ+Z^qX=0.
\]
For a geometric point \(P=[x:y:z]\), its tangent line is
\[
 T_P:\quad z^qX+x^qY+y^qZ=0.
\]
Write \(H_q\) for the set of geometric points where the tangent has the **maximal possible** intersection multiplicity \(q+1\) with \(C_q\). The residual-point morphism is
\[
 R([x:y:z])=[y^{q^2}:z^{q^2}:x^{q^2}],
 \qquad T_P\cdot C_q=q[P]+[R(P)].
\]
The maximal-contact locus is precisely the fixed-point locus of \(R\), and
\[
 \boxed{\#H_q=q^3+1.}
\]
Every point of \(H_q\) is defined over \(\mathbb F_{q^6}\). More precisely, if \(a_d\) denotes the number of **geometric points of exact degree** \(d\) over \(\mathbb F_q\), then
\[
 (a_1,a_2,a_3,a_6)=(h_q,0,q+1-h_q,q^3-q),
\]
with no other degrees occurring, where
\[
 h_q=\begin{cases}1,&p=3,\\2,&q\equiv1\pmod3,\\0,&q\equiv2\pmod3.\end{cases}
\]
Thus there are \(h_q\) closed points of degree one, \((q+1-h_q)/3\) closed points of degree three, and \((q^3-q)/6\) closed points of degree six. The zeta function of this reduced finite scheme is
\[
 Z(H_q/\mathbb F_q,T)=
 \frac{1}{(1-T)^{h_q}(1-T^3)^{(q+1-h_q)/3}(1-T^6)^{(q^3-q)/6}}.
\]
For \(q=3\) this reproduces the **known** 28 hyperflexes of the characteristic-three Klein/Fermat quartic. The substantive uniform assertion concerns the higher-degree curves, with their complete arithmetic osculation-orbit distribution.

## Assumptions and scope

A prime power is \(q=p^r\) with prime \(p\) and integer \(r\ge1\). All geometric points and intersection multiplicities are taken over an algebraic closure of \(\mathbb F_q\). An exact-degree-\(d\) point is a geometric point whose smallest definition field is \(\mathbb F_{q^d}\), not a closed point; closed points of degree \(d\) are counted by dividing the geometric count by \(d\). For \(q=2\), maximal contact is ordinary inflection contact three, while for \(q\ge3\) every tangent has contact at least \(q\). The finite scheme in the zeta function is the reduced fixed-point locus of the indicated morphism.

## Proof

**1. Smoothness and the residual osculation map.** Because the characteristic divides \(q\) and \(q+1\) is prime to \(p\), the partial derivatives of the defining equation are \(Z^q,X^q,Y^q\). They cannot simultaneously vanish projectively, so \(C_q\) is smooth. If \(P=(x,y,z)\) and \(V=(u,v,w)\), the restriction of its equation to \(P+tV\) is
\[
 F(P+tV)=t\bigl(z^qu+x^qv+y^qw\bigr)
 +t^q\bigl(u^qy+v^qz+w^qx\bigr)+t^{q+1}F(V).
\]
For \(V\) on \(T_P\), the linear term vanishes. Thus the intersection multiplicity is at least \(q\). The point \(R(P)\) lies on \(C_q\), because \(F(R(P))=F(P)^{q^2}\), and lies on \(T_P\), because its tangent-line equation evaluates to \(F(P)^q=0\). Bézout's theorem then gives \(T_P\cdot C_q=q[P]+[R(P)]\), even when the two support points coincide. Contact is exactly \(q+1\) if and only if \(R(P)=P\).

**2. Rationality and a norm–trace parametrization.** Let \(\sigma\) denote the cyclic coordinate permutation \([x:y:z]\mapsto[y:z:x]\), and let \(\Phi\) be arithmetic \(q\)-power Frobenius. Then \(R=\sigma\Phi^2\) and \(R^3=\Phi^6\). Hence \(R(P)=P\) implies \(P\in\mathbb P^2(\mathbb F_{q^6})\). At a fixed point no coordinate can vanish, since the cyclic map permutes the three coordinate-zero conditions transitively. By the multiplicative form of Hilbert's Theorem 90 for \(\mathbb F_{q^6}/\mathbb F_{q^2}\), a fixed projective point has a homogeneous representative fixed as a vector by this semilinear map; it can consequently be written
\[
 P_a=[a:a^{q^4}:a^{q^2}],\qquad
 a\in\mathbb F_{q^6}^{\times},
\]
where two values of \(a\) give the same projective point exactly if they differ by an element of \(\mathbb F_{q^2}^{\times}\). (Every such vector is manifestly fixed.) Substituting into \(F\), and putting \(b=a^{q^3+1}\), gives
\[
 F(P_a)=b+b^q+b^{q^2}
 =\operatorname{Tr}_{\mathbb F_{q^3}/\mathbb F_q}
 \bigl(\operatorname N_{\mathbb F_{q^6}/\mathbb F_{q^3}}(a)\bigr).
\]
The norm is surjective, with fibers of cardinality \(q^3+1\). The trace has exactly \(q^2-1\) nonzero zeros. Dividing by the free scaling group \(\mathbb F_{q^2}^{\times}\), of size \(q^2-1\), proves \(\#H_q=q^3+1\). Every fixed point is reduced: in any affine chart the differential of \(R\) is zero, so the equations \(R(P)=P\) have invertible Jacobian \(-I\) at a fixed point.

**3. The degree-one and degree-two subloci.** For \(P\in\mathbb P^2(\mathbb F_{q^2})\), \(R(P)=\sigma(P)\). Thus a fixed projective point must be an eigenline of the three-cycle \(\sigma\). If \(p=3\), \(\sigma\) has just one geometric eigenline \([1:1:1]\), which lies on \(C_q\). If \(p\ne3\), the eigenlines with primitive cubic eigenvalues lie on \(C_q\) precisely when \(q\equiv1\pmod3\); the eigenline with eigenvalue one does not lie on \(C_q\). If \(q\equiv2\pmod3\), the primitive-eigenvalue eigenlines do not satisfy the curve equation. The two points in the \(q\equiv1\) case already lie over \(\mathbb F_q\). Consequently \(\#H_q(\mathbb F_q)=\#H_q(\mathbb F_{q^2})=h_q\) and no maximal-contact point has exact degree two.

**4. The degree-three sublocus.** For \(P\in\mathbb P^2(\mathbb F_{q^3})\), the fixed-point relation \(R(P)=P\) is equivalent to \(\Phi(P)=\sigma(P)\), because \(\sigma\) commutes with Frobenius and \(\sigma^3=\Phi^3=1\) on these points. This is a twisted projective plane. Hilbert 90 gives all its points as
\[
 [a:a^q:a^{q^2}],\qquad a\in\mathbb F_{q^3}^{\times}/\mathbb F_q^{\times}.
\]
For these points the curve equation is \(\operatorname{Tr}_{\mathbb F_{q^3}/\mathbb F_q}(a^2)=0\). If \(q\) is odd, the trace pairing is nondegenerate and its quadratic form is a smooth conic in this projective plane, with exactly \(q+1\) points. If \(q\) is even, the same expression equals \(\operatorname{Tr}(a)^2\), defining a projective line, again with \(q+1\) points. Therefore \(\#H_q(\mathbb F_{q^3})=q+1\).

**5. Closed-point spectrum.** Since all points are over \(\mathbb F_{q^6}\), their minimal degrees divide six. The previously determined counts give \(a_1=h_q\), \(a_2=0\), \(a_3=q+1-h_q\), and \(a_6=q^3-q\), with no other possibilities. These integers are multiples of their respective degrees, because they are unions of Frobenius orbits. The displayed finite-scheme zeta function follows from the product over closed points.

## Verification

The accompanying standalone standard-library program `verify_osculation.py` constructs finite fields of sizes \(64,729,4096,15625\), and exhaustively verifies the norm–trace parametrization and the exact Frobenius degree profiles for \(q=2,3,4,5\). It checks, for every nonzero parameter \(a\), the projective fixed-point equation, curve membership, multiplicity of the scaling classes, and minimal Frobenius period. Run `python3 verify_osculation.py`; its actual output is recorded in `verification_output.txt` and ends in `OSCULATING_VERIFY_OK`. These finite checks corroborate, but cannot substitute for, the proof for every prime power.

## Relationship to prior work

Oyono and Ritzenthaler (2010, Section 2) explicitly identify the characteristic-three Klein quartic with the nonclassical Fermat quartic, state that every point is a flex, and give its **28 hyperflexes**. Accordingly, neither the 28-point result at \(q=3\) nor the general idea of nonclassical tangency is claimed as novel. Arakelian and Borges (2014) develop Frobenius nonclassicality and exact point-count theory for a broader different family of curves defined by power substitutions; they do not state the residual morphism and exact arithmetic fixed-locus spectrum of the present cyclic family in their inspected full text. Related studies of the general Klein family and finite designs provide geometric background. The new contribution assessed here is the uniform maximal-contact classification for all prime powers, particularly \(q\ge4\), with the explicit norm–trace model and the degree-one/three/six closed-point distribution. Priority remains provisional pending a specialist comparison with older papers on osculating points of nonclassical curves.

## Limitations

This theorem concerns the displayed cyclic plane curve and tangent **lines**, not arbitrary Frobenius nonclassical curves or higher-order osculating curves. The old \(q=3\) hyperflex count is a consistency check rather than a separate discovery. The executable verifies only four base fields; the proof establishes the asserted infinite family. Independent mathematical review and exhaustive historical priority certification have not been performed.

## References

1. R. Oyono and C. Ritzenthaler, *On rationality of the intersection points of a line with a plane quartic*, arXiv:1006.0873, first posted 2010-06-04. Relevant full text: Section 2, cases of infinite flexes and hyperflexes. https://arxiv.org/abs/1006.0873 .
2. N. Arakelian and H. Borges, *Frobenius nonclassicality with respect to linear systems of curves of arbitrary degree*, arXiv:1409.8549, first posted 2014-09-30. Relevant full text: Sections 1–3, the definition of Frobenius nonclassicality and family of power-substitution plane curves. https://arxiv.org/abs/1409.8549 .
