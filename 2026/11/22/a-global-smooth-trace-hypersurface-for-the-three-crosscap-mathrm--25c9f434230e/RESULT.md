# A global smooth trace hypersurface for the three-crosscap \(\mathrm{SL}_2\) character variety

## Finding
Let \(k=\mathbb C\), let
\[
\Gamma=\langle x,y,z\mid x^2y^2z^2=1\rangle,
\]
and let \(R\) be the **reduced** affine variety of triples \((A,B,C)\in\mathrm{SL}_2(k)^3\) satisfying \(A^2B^2C^2=I\). Define the reduced affine character variety \(X=R/\!/\mathrm{SL}_2(k)\), with simultaneous conjugation, and the invariant trace functions
\[
a=\operatorname{tr}A,\quad b=\operatorname{tr}B,\quad
c=\operatorname{tr}C,\quad s=\operatorname{tr}(ABC).
\]
**Theorem.** These four traces identify the entire reduced affine character variety with the **smooth irreducible affine threefold**
\[
X\ \cong\ \operatorname{Spec}\frac{\mathbb C[a,b,c,s]}
{\bigl(2a^2+2b^2+2c^2-abcs-8\bigr)}.
\]
As a boundary consequence (consistent with an earlier complete boundary calculation), the closed trace-zero stratum is the smooth affine cylinder
\[
X\cap V(c)\ \cong\ \operatorname{Spec}\frac{\mathbb C[a,b,s]}{(a^2+b^2-4)}
\ \cong\ \mathbb G_m\times\mathbb A^1.
\]
For every representation, the three remaining standard traces satisfy the **global**, including \(c=0\), identities
\[
\operatorname{tr}(AB)=\frac{cs}{2},\qquad
\operatorname{tr}(BC)=\frac{as}{2},\qquad
\operatorname{tr}(CA)=\frac{bs}{2}.
\]
On the trace-zero stratum the first two matrices commute, and every such triple admits the explicit parametrization in the proof. The trace map to the coordinates \((a,b,c,\operatorname{tr}(AB))\) collapses the cylinder onto the conic \(c=0,\operatorname{tr}(AB)=0,a^2+b^2=4\).

## Assumptions and scope
All varieties, invariant rings and quotients are over \(\mathbb C\). The representation variety is given its **reduced** algebraic-variety structure; the theorem makes no claim about potential nilpotents in the unreduced representation scheme or its derived structure. The generator order \(A,B,C\), word \(ABC\), and trace normalizations are fixed as above. The GIT quotient is affine \(\operatorname{Spec}(\mathbb C[R]^{\mathrm{SL}_2})\), not the space of all raw conjugacy orbits. The trace-zero boundary is the closed subvariety of this quotient defined by \(c=0\).

## Proof
**1. Matrix classification at trace zero.** Suppose \(c=0\). Cayley--Hamilton gives \(C^2=-I\), hence \(A^2B^2=-I\). If \(a\ne0\), then \(B\) commutes with \(B^2=-A^{-2}\) and therefore with \(A^2\). But \(A^2=aA-I\), so \(B\) commutes with \(A\). If \(a=0\), then \(A^2=-I\) and \(B^2=I\), which over \(\mathbb C\) forces \(B=I\) or \(B=-I\). Thus \(A\) and \(B\) commute in every case.

Put \(Z=AB\). Then \(Z^2=-I\) and \(\operatorname{tr}Z=0\); its eigenvalues \(i,-i\) are distinct, so its centralizer in \(M_2(\mathbb C)\) is \(\mathbb C[I,Z]\). Writing \(A=\alpha I+\beta Z\) and \(B=A^{-1}Z\), tracing both matrices gives \(a=2\alpha\), \(b=2\beta\), and
\[
A=\frac{aI+bZ}{2},\qquad B=\frac{bI+aZ}{2},\qquad a^2+b^2=4.
\]
Conversely, for each \((a,b)\) on this conic and each pair \((Z,C)\) of trace-zero determinant-one matrices, the displayed formula has determinants one and gives \(AB=Z\), \(A^2B^2=C^2=-I\). Hence the reduced trace-zero representation variety is **equivariantly isomorphic** to \(T\times Q\times Q\), where \(T=V(a^2+b^2-4)\) and \(Q=\{M\in\mathrm{SL}_2:\operatorname{tr}M=0\}\). The inverse is the regular map \((A,B,C)\mapsto(a,b,AB,C)\).

Fix \(Z=\operatorname{diag}(i,-i)\) by conjugation. Its centralizer in \(\mathrm{SL}_2\) is the diagonal torus. Write
\[
C=\begin{pmatrix}t&v\\w&-t\end{pmatrix},\qquad vw=-1-t^2.
\]
The residual torus acts on \(v,w\) with opposite nonzero weights, fixing \(t\). Its invariant ring is \(\mathbb C[t,vw]/(vw+1+t^2)=\mathbb C[t]\). Moreover \(\operatorname{tr}(ZC)=2it=s\). Therefore the reduced boundary quotient is \(T\times\mathbb A^1_s\). With \(u=(a+ib)/2\) and \(u^{-1}=(a-ib)/2\), \(T\cong\mathbb G_m\). Direct tracing also gives \(p:=\operatorname{tr}(AB)=0\), \(q:=\operatorname{tr}(BC)=as/2\), and \(r:=\operatorname{tr}(CA)=bs/2\) on this stratum.

**2. Trace identities away from the boundary.** Define \(D=(A^2B^2)^{-1}=C^2\), and \(p=\operatorname{tr}(AB)\). Cayley--Hamilton gives
\[
cC=I+D,\qquad
c^2=\operatorname{tr}D+2=abp-a^2-b^2+4.
\]
The last equality is the \(2\times2\) trace identity \(\operatorname{tr}(A^2B^2)=abp-a^2-b^2+2\). Taking traces of \(AB(cC)\), \(B(cC)\), and \((cC)A\) yields
\[
cs=2p,\qquad c\,\operatorname{tr}(BC)=ap,\qquad
c\,\operatorname{tr}(CA)=bp.
\]
For \(c\ne0\) these give the claimed formulas \(p=cs/2\), \(q=as/2\), \(r=bs/2\). Step 1 established the same three formulas at every point of \(c=0\), so they are identities in the coordinate ring of the **reduced** representation variety. Substituting \(p=cs/2\) in the second displayed equality gives
\[
F:=2a^2+2b^2+2c^2-abcs-8=0.
\]

**3. The invariant ring has no additional generators.** The classical rank-three Fricke--Procesi invariant theorem (in Goldman's notation, Section 5.1) generates \(\mathbb C[\mathrm{SL}_2^3]^{\mathrm{SL}_2}\) by the seven traces \(a,b,c,p,q,r,s\); the eighth frequently listed trace \(\operatorname{tr}(ACB)\) is eliminated by the Fricke sum identity. Since \(\mathrm{SL}_2\) is linearly reductive over \(\mathbb C\), taking invariants is exact for the quotient by the conjugation-stable reduced representation ideal. Thus \(\mathbb C[R]^{\mathrm{SL}_2}\) is generated by the restrictions of these seven trace functions, which by Step 2 reduce to \(a,b,c,s\). Therefore there is a surjective homomorphism
\[
\mathbb C[a,b,c,s]/(F)\longrightarrow\mathbb C[R]^{\mathrm{SL}_2}.
\]

**4. No further relation.** The polynomial \(F\) is irreducible: regarded as a linear polynomial in \(s\), its coefficients \(-abc\) and \(2(a^2+b^2+c^2-4)\) are coprime in the UFD \(\mathbb C[a,b,c]\). Let \((a,b,c,s)\) satisfy \(F=0\) and \(c\ne0\). Set \(p=cs/2\); choose a root \(t\in\mathbb C\) of \((a-t)(b-t)+2=p\), and put
\[
A=\begin{pmatrix}a&-1\\1&0\end{pmatrix},\qquad
B=\begin{pmatrix}b-t&1\\(b-t)t-1&t\end{pmatrix}.
\]
These matrices belong to \(\mathrm{SL}_2\), with traces \(a,b\) and product trace \(p\). Set \(D=(A^2B^2)^{-1}\). The relation \(F=0\) implies \(\operatorname{tr}D+2=c^2\). Hence
\[
C=\frac{I+D}{c}
\]
has trace \(c\), determinant \(\det(I+D)/c^2=1\), and square \(C^2=D\) by Cayley--Hamilton. Thus \((A,B,C)\in R\), and \(\operatorname{tr}(ABC)=2p/c=s\). Every point of \(V(F)\cap\{c\ne0\}\) is therefore attained by a representation. Because \(V(F)\) is irreducible and \(c\) does not divide \(F\), this image is dense in \(V(F)\). The displayed surjection of rings has zero kernel and is the desired isomorphism.

**5. Smoothness and the complete boundary.** At a singular point of \(V(F)\), differentiation in \(s\) gives \(abc=0\). If, for example, \(a=0\), differentiation in \(b,c\) gives \(b=c=0\), contradicting \(F=-8\); the other cases are symmetric. Therefore \(V(F)\) is smooth. Its \(c=0\) section is \(a^2+b^2=4\) with arbitrary \(s\), precisely the cylinder found in Step 1. This completes the proof.

## Verification
The included `VERIFY.py` uses exact symbolic arithmetic to check the companion-matrix realization, square-root construction, boundary parametrization, global trace formulas, Fricke relation after substitution, and the unit ideal generated by \(F\) and its partial derivatives. Execute `python VERIFY.py` with the supplied `requirements.txt`. All assertions passed in the recorded run. These computations verify essential algebraic identities; the density, invariant-generation, and quotient arguments above supply the infinite algebraic proof.

## Relationship to prior work
Yinxi Chen, *An Explicit Equation for the \(\mathrm{SL}_2(\mathbb C)\) Character Variety of \(\mathbb{RP}^2\#\mathbb{RP}^2\#\mathbb{RP}^2\)*, arXiv:2611.08513v1 (October 14, 2026), describes the open \(c\ne0\) trace hypersurface and identifies the trace-zero matrix equation; Section 5.2 explicitly leaves the boundary's full GIT classification open. The complete trace-zero cylinder was also obtained in an earlier related calculation and is **not** the new claim here. The new contribution is the **global** smooth character ring with the trace \(s=\operatorname{tr}(ABC)\) as fourth generator: this ring presentation and the proof that there are no additional generators, relations or gluing defects are not asserted by either the earlier boundary calculation or Chen's previously established \(c\ne0\) open equation.

Goldman's arXiv:0901.1404v1, Section 5.1, provides the general rank-three free-group trace invariant theorem used in the proof; it does not impose the particular nonorientable surface relation. Benyash-Krivets and Chernousov (1997) study nonorientable representation varieties and their irreducible components, dimensions and rationality; the inspected material does not supply this specialized trace-zero quotient or global four-coordinate equation.

## Limitations
Only the reduced complex affine character variety and its reduced trace-zero boundary are asserted. Unreduced representation schemes, character stacks, real forms, arithmetic descent, and other nonorientable genera are not classified. The proof rests on standard characteristic-zero reductivity and the classical rank-three trace-generation theorem. The trace-zero boundary cylinder and the generic punctured description are prior results; novelty is restricted to the full reduced invariant-ring presentation. The novelty comparison cannot exclude an unindexed equivalent older global trace presentation; independent review is not claimed.

## References
1. Y. Chen, *An Explicit Equation for the SL₂(C) Character Variety of RP²#RP²#RP²*, arXiv:2611.08513v1 (2026-10-14), https://arxiv.org/abs/2611.08513 , especially §5.2.
2. W. M. Goldman, *Trace Coordinates on Fricke Spaces of Some Simple Hyperbolic Surfaces*, arXiv:0901.1404v1 (2009), https://arxiv.org/abs/0901.1404 , especially §5.1.
3. V. V. Benyash-Krivets and V. I. Chernousov, *Representation Varieties of the Fundamental Groups of Compact Non-orientable Surfaces*, Sbornik: Mathematics 188 (1997), 997--1039, https://www.mathnet.ru/links/c0e6f6316f4e1e38715eaf171cbb6d83/sm242_eng.pdf .
