# Sharp scalar–Hilbert variance gap on Euclidean rectangle corners

## Finding
Let \(X_{a,b}=\{(0,0),(a,0),(0,b),(a,b)\}\subset\mathbb R^2\), where \(a\ge b>0\), carry Euclidean distance and uniform probability. For a real Hilbert space \(H\), set
\[
\mathcal V_H(a,b)=\sup_{\operatorname{Lip}(f)\le1}\frac14\sum_{x\in X_{a,b}}\|f(x)-\bar f\|_H^2,
\qquad\bar f=\frac14\sum_{x\in X_{a,b}}f(x).
\]
For the real line and every Hilbert target of dimension at least two, respectively, the sharp values are
\[
\boxed{\mathcal V_{\mathbb R}(a,b)=\frac{a^2+(\sqrt{a^2+b^2}-a)^2}{4}},\qquad
\boxed{\mathcal V_H(a,b)=\frac{a^2+b^2}{4}\quad(\dim H\ge2)}.
\]
All real extremizers, modulo an additive constant, are the maps
\[
f(\sigma_1,\sigma_2)=u\sigma_1+v\sigma_2,\qquad
(|u|,|v|)=\left(\frac a2,\frac{\sqrt{a^2+b^2}-a}{2}\right),
\]
with either assignment of the two absolute values allowed only when \(a=b\). The coordinates \(\sigma_i\in\{-1,1\}\) label the long and short sides respectively. Signs are independent. For \(\dim H\ge2\), all Hilbert-target extremizers are precisely \(f(\sigma_1,\sigma_2)=c+u\sigma_1+v\sigma_2\) with \(\|u\|=a/2\), \(\|v\|=b/2\), and \(\langle u,v\rangle=0\).

The absolute gap equals \(a(\sqrt{a^2+b^2}-a)/2>0\). Its fraction of the Hilbert optimum is
\[
\frac{\mathcal V_H-\mathcal V_{\mathbb R}}{\mathcal V_H}
=\frac{2(\sqrt{1+t^2}-1)}{1+t^2},\qquad t=b/a\in(0,1],
\]
which increases strictly with \(t\), attaining its unique maximum \(\sqrt2-1\) at the square. In particular, for \(a=b=1\) the scalar constant is \(1-1/\sqrt2\), the Hilbert constant is \(1/2\), and their ratio is \(1+1/\sqrt2\).

## Assumptions and scope
The rectangle is nondegenerate, the four points have equal masses, and the Lipschitz bound is imposed for *all six unordered pairs* with their actual Euclidean distances; it is not the intrinsic graph-path metric. Functions are arbitrary maps to a real Hilbert space. The inequalities concern squared variance and a Lipschitz seminorm; constants may be added freely.

## Proof
Write the uniform corners by independent signs \(\sigma_1,\sigma_2\in\{-1,1\}\). Any real-valued map has a unique Walsh expansion
\[
f=c+u\sigma_1+v\sigma_2+w\sigma_1\sigma_2,\qquad
\operatorname{Var}(f)=u^2+v^2+w^2.
\]
Set \(A=a/2\), \(B=b/2\), \(C=\sqrt{A^2+B^2}\). The four side distances give exactly \(|u|+|w|\le A\) and \(|v|+|w|\le B\); the two diagonal distances give exactly \(|u|+|v|\le C\). Thus the scalar problem is to maximize \(p^2+q^2+r^2\) subject to \(p,q,r\ge0\), \(p+r\le A\), \(q+r\le B\), \(p+q\le C\).

For fixed \(r\in[0,B]\), let \(U=A-r\), \(V=B-r\), and \(r_0=(A+B-C)/2\in(0,B)\). If \(0\le r\le r_0\), then \(U+V\ge C\), and elementary convexity in \((p,q)\), together with \(U\ge V\), shows the maximum is achieved at \((p,q)=(U,C-U)\). Indeed, the two possible sum-boundary endpoints have squared-norm difference \(2(U-V)(U+V-C)\ge0\). The full objective is therefore
\[
G_-(r)=(A-r)^2+(C-A+r)^2+r^2\qquad(0\le r\le r_0).
\]
If \(r_0\le r\le B\), the sum constraint is redundant, so the objective is
\[
G_+(r)=(A-r)^2+(B-r)^2+r^2.
\]
Both are strictly convex in \(r\), hence their maxima on the indicated closed intervals occur at endpoints. The values at \(r_0\) agree, and
\[
G_-(r_0)-G_-(0)
=\frac{r_0}{2}(C-5A+3B)<0,
\]
because \(B\le A\) and \(C\le\sqrt2 A<2A\). At the remaining endpoint,
\[
G_-(0)-G_+(B)=2B(A-B)+(C-A)^2>0.
\]
Consequently \(r=0\) uniquely maximizes the three-variable objective. On the active sum boundary, \(U=A\), \(V=B\), the same endpoint comparison implies \((p,q)=(A,C-A)\) when \(A>B\); both permutations are possible when \(A=B\). This proves the scalar constant and every scalar equality case.

For a real Hilbert target, expand similarly with \(c,u,v,w\in H\). The two opposite sides in the first direction imply \(\|u+w\|,\|u-w\|\le A\), whence by the parallelogram identity \(\|u\|^2+\|w\|^2\le A^2\). Similarly \(\|v\|^2+\|w\|^2\le B^2\). Orthogonality of the Walsh functions gives
\[
\operatorname{Var}_H(f)=\|u\|^2+\|v\|^2+\|w\|^2
\le A^2+B^2-\|w\|^2\le A^2+B^2.
\]
Equality forces \(w=0\), \(\|u\|=A\), \(\|v\|=B\). The two diagonal distances additionally force \(\|u+v\|,\|u-v\|\le C\). Since \(C^2=A^2+B^2\), these inequalities are then equivalent to \(\langle u,v\rangle=0\). Orthogonal \(u,v\) exist exactly when the target dimension is at least two and attain the bound. Dimension one is covered by the scalar classification.

Finally, writing \(y=\sqrt{1+t^2}\in(1,\sqrt2]\), the normalized deficit equals \(2(y-1)/y^2\). Its derivative is \(2(2-y)/y^3>0\); thus the normalized gap is uniquely largest for \(t=1\).

## Verification
The standalone `check_rectangle.py` reconstructs the six scalar linear inequalities and enumerates feasible three-constraint vertices for ten rational side-length pairs using exact quadratic radicals in SymPy. It verifies each feasible vertex lies below the claimed objective, checks attainment and the Hilbert–scalar gap identity. Its successful execution reported 84 feasible-vertex comparisons and ten exact gap identities. This finite computation is a diagnostic; all aspect ratios and all equality assertions follow from the proof above.

## Relationship to prior work
Mendel–Naor (2012), *Nonlinear spectral calculus and super-expanders*, introduces nonlinear Poincaré/spectral-gap comparisons for vector-valued maps. Naor (2013), *Comparison of metric spectral gaps*, discusses average distortion and scalar Lipschitz maps on Euclidean Boolean cubes, including the order of their large-dimensional variance in Section 6.2. Those results provide the motivated framework, but do not give the parameter-dependent four-corner optimum, its full extremizers, or the maximally separated square aspect ratio established here. The general framework must not be conflated with the precise four-point equality statement.

## Limitations
The result does not extend without further argument to nonuniform corner weights, general parallelograms, larger cubes, arbitrary Banach targets, or higher powers of distances. Originality is judged relative to the inspected and indexed literature; an older unindexed four-point computation remains possible.

## References
1. M. Mendel and A. Naor, *Nonlinear spectral calculus and super-expanders*, arXiv:1207.4705, first submitted 2012-07-19. https://arxiv.org/abs/1207.4705
2. A. Naor, *Comparison of metric spectral gaps*, arXiv:1308.2851, first submitted 2013-08-13; see Section 6.2 on Euclidean Boolean cubes. https://arxiv.org/abs/1308.2851
