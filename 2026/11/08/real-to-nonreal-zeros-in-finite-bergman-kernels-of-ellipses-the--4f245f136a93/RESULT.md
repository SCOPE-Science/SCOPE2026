# Real-to-nonreal zeros in finite Bergman kernels of ellipses: the first sharp bifurcation

## Finding
Let \(E_{a,b}=\{z\in\mathbb C:(\operatorname{Re}z)^2/a^2+(\operatorname{Im}z)^2/b^2<1\}\) with \(a>b>0\). Let \(K_d(z,w)\) denote the reproducing kernel of complex polynomials of degree at most \(d\) with respect to \(dx\,dy/(\pi ab)\) on \(E_{a,b}\). All statements below concern the complex zeros of the **finite polynomial** \(z\mapsto K_d(z,0)\), not the infinite Bergman kernel.

For each integer \(m\ge1\), \(K_{2m+1}(z,0)=K_{2m}(z,0)\) has degree exactly \(2m\). For every fixed \(m\), all \(2m\) zeros are simple, real and interior to the ellipse when its aspect ratio \(b/a\) is sufficiently small. For every fixed \(m\ge2\), at least four of its zeros are nonreal when \(b/a\) is sufficiently close to one.

The smallest degree capable of nonreal center-kernel zeros is \(d=4\). Write \(u=b^2/a^2\), and let \(y_*>2\) be the unique positive root of
\[Q(y)=225y^4-600y^3-14600y^2-44000y-32624.\]
Set \(u_*=2/(y_*+\sqrt{y_*^2-4})\approx0.0949570683147436743\). The four roots at degree four are all **distinct real** for \(0<u<u_*\), form **two real double roots** at \(u=u_*\), and are **all nonreal** for \(u_*<u<1\). The critical aspect ratio is \(b/a=\sqrt{u_*}\approx0.308151047888440052\). At degree two the two zeros remain real for every aspect ratio and are interior precisely when \(u<1/3\); degrees zero and one give a constant center kernel.

## Assumptions and scope
The area measure is normalized to total mass one. Put \(c=\sqrt{a^2-b^2}\), \(t=(a^2+b^2)/(a^2-b^2)>1\), and let \(U_j\) be the standard Chebyshev polynomial of the second kind, so \(U_0=1\), \(U_1(x)=2x\), and \(U_{j+1}(x)=2xU_j(x)-U_{j-1}(x)\). The planar orthogonality relation (Akemann–Nagao–Parra–Vernizzi, Eq. B.1) gives
\[\|U_j(z/c)\|_{L^2(E_{a,b})}^2=\frac{U_j(t)}{j+1}.\]
Consequently, \(K_d(z,w)=\sum_{j=0}^{d}\frac{j+1}{U_j(t)}U_j(z/c)U_j(\overline w/c)\). Since \(U_{2k+1}(0)=0\) and \(U_{2k}(0)=(-1)^k\),
\[K_{2m+1}(z,0)=K_{2m}(z,0)=\sum_{k=0}^{m}\frac{(-1)^k(2k+1)}{U_{2k}(t)}U_{2k}(z/c).\]
These formulas are valid for every \(a>b>0\), \(m\ge0\); the circle limit is considered only after rescaling the polynomial variable.

## Proof
**Thin-ellipse regime.** Fix \(a\) and \(m\). As \(b\downarrow0\), \(c\to a\), \(t\to1\), and \(U_{2k}(t)\to2k+1\). The finite sum tends coefficientwise to
\[\sum_{k=0}^m(-1)^k U_{2k}(z/a)=(-1)^m U_m(2(z/a)^2-1).\]
The identity follows, for \(z/a=\cos\theta\), from the finite geometric series for \(\sum(-1)^k\sin((2k+1)\theta)\), and hence holds polynomially. Its \(2m\) zeros are
\[z=\pm a\cos\!\left(\frac{j\pi}{2(m+1)}\right),\quad j=1,\ldots,m,\]
all distinct and strictly between \(-a\) and \(a\). Since the coefficients are real and depend continuously on \(b\), each simple real zero persists as a real zero under a sufficiently small real perturbation (implicit-function theorem). Hence all zeros remain real, simple, and interior for sufficiently small \(b/a>0\).

**Nearly circular regime.** Set \(u=b^2/a^2\), \(\varepsilon=1-u\) and substitute \(z=a\xi/\sqrt\varepsilon\). Since \(c=a\sqrt\varepsilon\), \(t=(2-\varepsilon)/\varepsilon\), for fixed \(k\) the leading coefficients of \(U_{2k}\) give
\[\frac{U_{2k}(\xi/\varepsilon)}{U_{2k}((2-\varepsilon)/\varepsilon)}\longrightarrow (\xi/2)^{2k},\qquad \varepsilon\downarrow0.\]
Therefore the degree-\(2m\) scaled polynomials converge coefficientwise to
\[P_m(\xi^2/4),\qquad P_m(v)=\sum_{k=0}^{m}(-1)^k(2k+1)v^k.\]
For \(m\ge2\), \(P_m(-r)>0\) for \(r\ge0\). If all \(m\) roots of \(P_m\) were real, they would be strictly positive. Their first two elementary symmetric sums, using the top three coefficients, are \(e_1=(2m-1)/(2m+1)\) and \(e_2=(2m-3)/(2m+1)\). Newton's inequalities for \(m\) nonnegative real roots require \(\big(e_1/m\big)^2\ge e_2/\binom m2\), equivalent to
\[(m-1)(2m-1)^2\ge2m(2m+1)(2m-3).\]
But the right side minus the left is \(4m^3-11m+1>0\) for every integer \(m\ge2\), a contradiction. Thus \(P_m\) contains a conjugate pair of nonreal roots. Their four square-root preimages under \(\xi^2/4\) are nonreal, remain so for all sufficiently small \(\varepsilon>0\) by continuity of polynomial roots, and rescale back to four nonreal zeros of \(K_{2m}(z,0)\).

**Exact first bifurcation.** Set \(x=(z/a)^2\). Substituting \(U_2(s)=4s^2-1\) and \(U_4(s)=16s^4-12s^2+1\) gives
\[K_4(z,0)=\frac{A(u)x^2+B(u)x+C(u)}{(u+3)(3u+1)(u^2+10u+5)(5u^2+10u+1)},\]
with
\[\begin{aligned}
A(u)&=80(u-1)^2(u+3)(3u+1),\
B(u)&=48(u-1)(5u^4+20u^3+14u^2+20u+5),\
C(u)&=45u^6+370u^5+931u^4+1404u^3+931u^2+370u+45.
\end{aligned}\]
The denominator is positive and \(A,C>0>B\) for \(0<u<1\). Its quadratic discriminant is
\[\Delta(u)=64(u-1)^2 u^4Q(u+u^{-1}).\]
The coefficient signs of \(Q\) show exactly one positive root by Descartes' rule, and \(Q(2)<0\) shows that this root \(y_*\) exceeds two. On \(0<u<1\), \(u+u^{-1}\) decreases strictly from infinity to two. Hence \(\Delta\) is positive for \(u<u_*\), zero for \(u=u_*\), and negative for \(u>u_*\). When \(\Delta>0\), positivity of \(A,C\) and negativity of \(B\) make both distinct roots in \(x\) positive, producing four distinct real zeros in \(z\). At equality the positive double \(x\) root gives two double real \(z\) roots; when \(\Delta<0\), both \(x\) roots and hence all four \(z\) roots are nonreal.

Finally \(K_2(z,0)=1-3U_2(z/c)/U_2(t)\) has the real square-root zeros determined by \(x=(3+2u+3u^2)/(6(1-u))\). Their locations obey \(x<1\) exactly when \(u<1/3\). Degree zero and one yield \(K_d(z,0)=1\), proving the first-degree assertion.

## Verification
The accompanying self-contained SymPy checker `check.py` rederives the degree-four rational kernel, its discriminant and reciprocal reduction, the degree-two boundary, the Newton deficit identity, and eight thin-limit Chebyshev identities. A successful run prints `ELLIPSE_FINITE_KERNEL_PASS`. The universal statements for all \(m\) follow from the proof above, not from those eight examples. The exact numerical value of \(u_*\) is illustrative; its defining quartic and uniqueness establish the threshold rigorously.

## Relationship to prior work
Akemann, Nagao, Parra, and Vernizzi establish planar Chebyshev orthogonality on an ellipse and the precise norms used above. Nagao, Akemann, Kieburg, and Parra write the same finite kernel for the Coulomb gas, then analyze large-particle local and global correlation limits. The result here instead determines a **finite-degree center-slice zero-geometry transition** as the ellipse changes aspect ratio. It makes no novelty claim for the Chebyshev basis, orthogonality relation, or the finite kernel formula itself. The full texts inspected below do not state the quartic discriminant threshold or the general fixed-degree thin-to-near-circle zero bifurcation.

## Limitations
The theorem concerns the zeros of the center slice of the **finite-rank polynomial reproducing kernel** as a polynomial on \(\mathbb C\). In the nearly circular regime the roots move outside the ellipse; they are not claimed to be zeros of the full infinite-dimensional Bergman kernel. No uniqueness of a transition for degrees greater than four, no effective closeness-to-circle bound depending on \(m\), and no general off-center classification are established. Historical priority remains conditional on the inspected literature; an unlocated result on elliptic planar Christoffel kernels could imply portions of the statement.

## References
1. G. Akemann, T. Nagao, I. Parra, G. Vernizzi, *Gegenbauer and other planar orthogonal polynomials on an ellipse in the complex plane*, arXiv:1905.02397 (first posted 2019-05-07), especially Corollary 4.4 and Appendix B, Eq. (B.1). https://arxiv.org/abs/1905.02397
2. T. Nagao, G. Akemann, M. Kieburg, I. Parra, *Families of two-dimensional Coulomb gases on an ellipse: correlation functions and universality*, arXiv:1905.07977 (first posted 2019-05-20), Sections 3 and 5, especially Eq. (5.3). https://arxiv.org/abs/1905.07977
3. NIST Digital Library of Mathematical Functions, Chapter 18, classical Chebyshev identities and basic properties. https://dlmf.nist.gov/18
