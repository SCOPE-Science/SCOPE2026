# The wild Artin–Schreier Gauss cover of characteristic-two bitangent quartics

## Finding
Let \(k\) be a perfect field of characteristic \(2\). Fix \(a,b,c,d\in k\), subject to
\(b\ne0\) and \(\Delta:=ab^2+c^2+1\ne0\), and define the projective quartic
\[
C:\quad Y^4+aZ^4+bX^2Y^2+cX^2Z^2+bX^3Z+dX^4=0.
\]
Write \(D=d/b^2\) and let \(\lambda\in k^\times\) be the unique fourth root of \(\Delta/b^4\).
The normalization \(\widetilde C\) is a projective line with a rational parameter \(s\) for which the extension of the Gauss map to the **reduced dual line** is
\[
\boxed{t=\frac{\lambda}{s^4+s^2+D}}.\tag{1}
\]
Here the tangent line indexed by \(t\in k\) is \(X+tZ=0\), with \(t=\infty\) representing \(Z=0\). Thus the Gauss map has inseparable degree two and separable degree two. Its connected separable factor is
\[
\boxed{v^2+v=D+\lambda/t},\qquad v=s^2.\tag{2}
\]
This quadratic cover is ramified only at \(t=0\), with Artin–Schreier lower jump one and different exponent two. The unique point over \(t=0\) maps to the singularity \([0:a^{1/4}:1]\).

Over \(k=\mathbb F_q\) with \(q=2^m\), there are exactly \(q\) rational dual lines tangent at smooth geometric points (all lines of the pencil except \(X=0\)). Exactly \(q/2\) contain two \(k\)-rational smooth contacts, and exactly \(q/2\) contain two quadratic-conjugate smooth contacts. The split-contact criterion is
\[
\operatorname{Tr}_{k/\mathbb F_2}(D+\lambda/t)=0\quad(t\in k^\times),
\]
with the convention that the expression equals \(D\) for \(t=\infty\).

## Assumptions and scope
All geometric statements hold over every **perfect** characteristic-two ground field satisfying \(b\Delta\ne0\). The existence and uniqueness of the required square and fourth roots use perfection. The finite-field count holds for every \(q=2^m\), every positive integer \(m\), and every such marked coefficient tuple. The locus \(\Delta=0\) is excluded because its fibre is geometrically reducible into conics, and the locus \(b=0\) has a nonreduced fibre; neither is covered by this Gauss-map theorem.

## Proof
**1. Tangent pencils and integrality.** The partial derivatives are
\[
F_X=bX^2Z,\qquad F_Y=0,\qquad F_Z=bX^3.
\]
Thus every smooth geometric point has \(X\ne0\), and its tangent is \(ZX_0+XZ_0=0\), where \(X_0,Z_0\) denote dual linear coordinates. It follows that the reduced dual curve is exactly the line of lines through \([0:1:0]\), with affine tangent parameter \(t=x/z\). At \(x=0\) the unique point on the quartic is \([0:a^{1/4}:1]\), a singular point. For \(x\ne0\) the gradient is nonzero, including points at \(z=0\).

Work on \(z=1\) with \(t=x\), and set \(u=y^2/(bt^2)\). The equation becomes
\[
u^2+u=\frac{A}{t^4}+\frac{B}{t^2}+\frac{C_0}{t}+D,
\quad A=\frac a{b^2},\quad B=\frac c{b^2},\quad C_0=\frac1b.
\]
Choose \(r=A^{1/4}\) and \(h=r^2/t^2+\eta/t\) with \(\eta=B^{1/2}+r\). Since \(\eta^2+r^2=B\), replacing \(u\) by \(v=u+h\) gives
\[
v^2+v=\frac{\lambda}{t}+D,\qquad
\lambda=C_0+B^{1/2}+A^{1/4}.
\]
In characteristic two, \(\lambda^4=(ab^2+c^2+1)/b^4=\Delta/b^4\). Therefore \(\lambda\ne0\) and \(t=\lambda/(v^2+v+D)\). The right side has a pole of order one at \(t=0\), hence the Artin–Schreier equation defines a connected separable quadratic extension, with rational function field \(k(t,v)=k(v)\).

Differentiating the first Artin–Schreier equation with respect to \(t\) gives \(du/dt=C_0/t^2\), while differentiating the second gives \(dv/dt=\lambda/t^2\). Hence
\[
\frac{du}{dv}=\frac{C_0}{\lambda}\ne0.
\]
In particular \(u\notin k(v)^2\), and adjoining \(y\) to \(k(v)\) gives a genuinely nontrivial purely inseparable extension of degree two, since \(y^2=bt^2u\). A perfect constant field implies the unique degree-two purely inseparable extension inside its perfect closure is \(k(v^{1/2})\). Thus
\[
k(C)=k(v^{1/2})=k(s),\qquad s^2=v,
\]
and substituting \(v=s^2\) proves (1). It also proves geometric integrality and rationality of \(C\): the displayed argument remains valid over an algebraic closure. Because (1) is a nonconstant map of degree four, and factors as \(s\mapsto s^2=v\) followed by the separable quadratic function \(v\mapsto \lambda/(v^2+v+D)\), the claimed inseparable and separable degrees follow.

**2. Ramification.** The Artin–Schreier function \(D+\lambda/t\) has exactly one pole, at \(t=0\), of order one. Its connected quadratic cover is unramified elsewhere, totally wildly ramified at zero, with lower ramification jump one and different exponent \((2-1)(1+1)=2\). The unique place \(v=\infty\) over zero becomes the unique \(s=\infty\) on the full normalization; geometrically this maps to the singular point above.

**3. Rational contact splitting.** For each \(t\in k^\times\), the line \(X+tZ=0\) restricts the quartic to
\[
Y^4+b t^2 Y^2Z^2+(a+ct^2+bt^3+dt^4)Z^4=0.
\]
This factors over the algebraic closure as the square of a product of two distinct linear forms, yielding exactly two distinct smooth contact points, each of intersection multiplicity two. At \(t=\infty\) the restriction is \(Y^4+bX^2Y^2+dX^4\) and has the same property. Their two points are simultaneously rational exactly when the separable quadratic \(v^2+v=D+\lambda/t\) splits over \(k\), because the intermediate purely inseparable square-root map does not change rationality over a perfect field. Over \(\mathbb F_q\), splitting is equivalent to the absolute trace vanishing. The bijection
\[
\mathbb P^1(\mathbb F_q)\setminus\{0\}\longrightarrow\mathbb F_q,
\qquad t\longmapsto\begin{cases}\lambda/t,&t\ne\infty,\\0,&t=\infty,\end{cases}
\]
therefore gives precisely \(q/2\) trace-zero and \(q/2\) trace-one values. In the latter case Frobenius exchanges the two geometric contacts, so they are separately rational over \(\mathbb F_{q^2}\) and not over \(\mathbb F_q\). The line \(X=0\) cuts \(C\) only at the singular point with multiplicity four, so is excluded from the smooth-contact count. This proves all claims.

## Verification
The standalone file `verify_char2_gauss.py` implements polynomial-basis arithmetic and verifies the trace criterion against direct line-section roots for every permitted marked coefficient tuple over fields with \(2\), \(4\), and \(8\) elements, and a deterministic sample of \(560\) integral tuples over \(\mathbb F_{16}\). It confirms equal numbers of split and nonsplit rational tangent lines in each field, and returns `GAUSS_CONTACT_SPLITTING_VERIFIED`. These finite tests supplement, but do not replace, the proof for all perfect characteristic-two fields.

## Relationship to prior work
Hilario and Stöhr (2023, first public June 14) introduce the universal quartic family and prove that tangents at the smooth points of its integral second-type fibres are bitangents and concurrent. Their published result describes the geometry of the fibres but does not give the explicit normalized Gauss-cover morphism, its wild ramification filtration, or the rational-contact trace distribution. Hilario and Stöhr (2024) analyze the larger five-family classification of regular geometrically rational quartics; their generic-function-field normal forms do not supply this finite-field Gauss-cover arithmetic. An earlier independent calculation of this specific separable/inseparable dual cover, especially in classical strange-curve literature, remains possible. The previous exact finite-field fibre and zeta classification of this same quartic family is expressly not newly claimed here: it does not identify the cover of the dual pencil or classify which rational tangent lines split into rational contact pairs.

## Limitations
This is a theorem about the integral locus \(b\Delta\ne0\). It does not classify Gauss maps of nonreduced or geometrically reducible boundary fibres. It does not assert any new count of rational points on the original quartic, a new family of curves, or a classification of projective isomorphism classes. Independent external validation and exhaustive historical-priority verification have not been performed.

## References
- C. Hilario and K.-O. Stöhr, *Fibrations by plane quartic curves with a canonical moving singularity*, arXiv:2306.08579 (first public June 14, 2023), especially §§4–5. https://arxiv.org/abs/2306.08579
- C. Hilario and K.-O. Stöhr, *Fibrations by plane projective rational quartic curves in characteristic two*, arXiv:2409.05464 (first public September 9, 2024), especially the normal forms in §1 and classification in §3. https://arxiv.org/abs/2409.05464
