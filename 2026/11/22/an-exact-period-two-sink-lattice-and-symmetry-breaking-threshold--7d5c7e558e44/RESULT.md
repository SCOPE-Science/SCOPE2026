# An exact period-two sink lattice and symmetry-breaking threshold in a sinusoidal planar map

## Finding
For the real planar map
\[
F_a(x,y)=\bigl(x+\sin(x+y),\,ax\bigr),\qquad a>0,
\]
there is no primitive period-two orbit for \(0<a\leq3\). In the range \(3<a<1+2\pi\), every primitive period-two orbit belongs to the explicit lattice classification below. Let
\[
c=(a-1)/2,\quad L=(a+1)/2,\quad
\theta\in(0,\pi),\quad \frac{\theta}{\sin\theta}=c,\quad d_0=\sin\theta.
\]
There is exactly one *central* primitive two-cycle per integer \(m\), with coordinate sum \(s=2\pi m/L\) and separation \(d=d_0\). If \(a>1+\pi\), two additional, distinct *side* primitive two-cycles appear per integer \(m\), with
\[
d=\frac{\pi}{a-1},\qquad Ls=2\pi m\pm\phi,
\qquad \phi=\arccos\!\left(\frac{\pi}{a-1}\right).
\]
At \(a=1+\pi\), the two side formulas coincide with the central cycle and do not give additional distinct orbits. No other primitive real two-cycles exist in the stated parameter range.

The central cycle is exponentially attracting precisely for
\[
1+\pi<a<a_*\quad\text{where}\quad
a_*=1+\frac{2\theta_*}{\sin\theta_*}=4.659463703928982997\ldots,
\]
and \(\theta_*\) is the unique solution in \((\pi/2,\pi)\) of
\[
-\left(1+\frac{2\theta_*}{\sin\theta_*}\right)\cos\theta_*=1.
\]
Every side cycle has a real return multiplier strictly greater than one, and hence never attracts. The side-cycle phase splitting at onset satisfies
\[
\phi=\sqrt{\frac2\pi}\sqrt{a-1-\pi}
+O\bigl((a-1-\pi)^{3/2}\bigr)
\qquad (a\downarrow1+\pi).
\]
Thus the exact two-cycle count per translation cell is one for \(3<a\le1+\pi\) and three for \(1+\pi<a<1+2\pi\), with exactly one attracting cycle per cell only in the stated open sink interval.

## Assumptions and scope
All coordinates and parameters are real. A primitive two-cycle is an unordered pair \(\{P,Q\}\) of different points satisfying \(F_a(P)=Q\) and \(F_a(Q)=P\). The index \(m\in\mathbb Z\) labels translation cells, with no finite global total because the map is periodic along the diagonal \((1,a)\) direction. "Attracting" means both eigenvalues of the derivative of the second iterate at either cycle point have modulus strictly less than one. Endpoints with a unit-modulus eigenvalue are not declared exponentially attracting. No claims are made about higher-period orbits, chaotic attractors or all \(a\ge1+2\pi\).

Given any admitted pair \((s,d)\) with \(d>0\), its points are exactly
\[
P=\left(\frac{s-d}{2},\frac{a(s+d)}2\right),\qquad
Q=\left(\frac{s+d}{2},\frac{a(s-d)}2\right).
\]
In particular, the choices of different \(m\) give different unordered cycles. For fixed \(m\), the \(+\phi\) and \(-\phi\) side cycles are distinct when \(\phi>0\).

## Proof
**1. Reduction to two trigonometric equations.** Let a primitive cycle have first coordinates \(x_0<x_1\), with \(d=x_1-x_0>0\) and \(s=x_0+x_1\). The second component of \(F_a\) forces \(y_0=ax_1\) and \(y_1=ax_0\). The first component of the two transition equations is therefore equivalent to
\[
d=\sin(Ls+cd),\qquad -d=\sin(Ls-cd).
\]
Necessarily \(0<d\le1\). Taking sum and difference gives precisely
\[
\sin(Ls)\cos(cd)=0,
\qquad d=\cos(Ls)\sin(cd).
\tag{1}
\]
Conversely, any \((s,d)\) satisfying (1) with \(d>0\) reconstructs a primitive two-cycle by the displayed point formula, so this reduction loses no solutions.

**2. Exhaustive cycle classification.** If \(0<a\le3\), then \(|c|\le1\) (indeed \(c>-1/2\)) and \(|cd|\le1<\pi/2\), so \(\cos(cd)\ne0\). The first relation in (1) makes \(Ls\in\pi\mathbb Z\); the second implies \(d=|\sin(cd)|\le|c|d\), with equality impossible for \(d>0\) even at \(|c|=1\). Thus no primitive two-cycle exists.

Suppose now \(3<a<1+2\pi\), so \(1<c<\pi\), \(0<cd<\pi\) and \(\sin(cd)>0\). If \(\cos(cd)\ne0\), (1) forces \(Ls\in\pi\mathbb Z\); its second equation then forces \(\cos(Ls)=1\), and \(d=\sin(cd)\). With \(\theta=cd\in(0,\pi)\), this is \(c=\theta/\sin\theta\). The function \(\theta/\sin\theta\) increases strictly from one to infinity because \(\sin\theta-\theta\cos\theta>0\) on \((0,\pi)\). Hence there is exactly one central separation for every such \(a\), and \(Ls=2\pi m\).

The remaining case \(\cos(cd)=0\) is possible exactly when \(cd=\pi/2\) (since \(0<cd<\pi\)). It gives \(d=\pi/(2c)\), requiring \(c\ge\pi/2\), and then \(\cos(Ls)=d\) by (1). At equality \(c=\pi/2\), both phase solutions collapse to \(Ls=2\pi m\), also satisfying the central equation. At strict inequality, the two solutions \(Ls=2\pi m\pm\arccos(d)\) are distinct. These cases exhaust (1), proving the census.

**3. Floquet spectrum and exact sink window.** Write
\[
J(t)=\begin{pmatrix}1+t&t\\ a&0\end{pmatrix},
\qquad t=\cos(x+y).
\]
On a central cycle, both input phases have cosine \(t=\cos\theta\), so the two-step derivative is \(J(t)^2\). Its exponential attraction is equivalent to the eigenvalues of \(J(t)\) lying strictly in the unit disk. The characteristic polynomial of \(J(t)\) is
\[
\lambda^2-(1+t)\lambda-at.
\]
The strict second-order Schur inequalities are
\[
-(1+a)t>0,\quad 2+(1-a)t>0,\quad 1+at>0.
\]
For \(a>3\), these reduce to \(-1/a<t<0\): the middle inequality holds automatically whenever \(t<0\). Since \(\theta\) increases strictly with \(a\), \(t=0\) exactly when \(\theta=\pi/2\), or \(a=1+\pi\). For \(\theta>\pi/2\), both \(a=1+2\theta/\sin\theta\) and \(-\cos\theta\) increase strictly, so their product increases strictly from zero to infinity. It equals one at the unique \(\theta_*\) stated in the finding. Therefore the central cycle is exponentially attracting exactly on \((1+\pi,a_*)\). At either endpoint one eigenvalue of \(J(t)\) has modulus one.

On a side cycle, let \(v=\sqrt{1-d^2}>0\). Its two input phases have opposite cosines \(+v\) and \(-v\). The product \(J(v)J(-v)\) (or its reversed order) has
\[
\operatorname{tr}(J(v)J(-v))=1-v^2,\qquad
\det(J(v)J(-v))=-a^2v^2.
\]
Thus the value of its monic characteristic polynomial at one is
\[
1-(1-v^2)-a^2v^2=-(a^2-1)v^2<0.
\]
Because that polynomial tends to plus infinity along the positive real axis, it has a real root greater than one. Every side cycle is therefore unstable and cannot attract.

**4. Splitting scale.** Put \(a=1+\pi+\varepsilon\), \(\varepsilon>0\). Then \(d=\pi/(\pi+\varepsilon)=1-\varepsilon/\pi+O(\varepsilon^2)\) on the side branches. As \(\arccos(1-h)=\sqrt{2h}+O(h^{3/2})\), the two phase displacements are \(\pm\phi\) with the stated square-root law. Their mean first coordinates differ from the central cell center by \(\pm\phi/(a+1)\), so they constitute distinct symmetry-related local branches.

## Verification
The analytic proof establishes the infinite census and stability statements; finite calculations are not used as substitutes for completeness. The standalone `check.py` recalculates the reconstructed point transitions, two-step trace/determinant, side-branch expansion tests and critical parameter root using standard Python. Representative diagnostic values: at \(a=4.3\), the central branch has largest one-step multiplier modulus approximately \(0.56616\), while both side branches have a positive two-step multiplier greater than one. At \(a=4.7\), the central modulus is approximately \(1.03589\). The critical value is \(a_*=4.65946370392898\ldots\).

## Relationship to prior work
Ge, Li, Li, Zhang and Tao (2023) introduced the same map and investigated symmetry, self-reproducing attractors, offset boosting, numerical bifurcation windows and electronic implementation. In their Section 2, the reported parameter sweep is \(-3.4<a<2.5\); neither its fixed-point analysis nor its numerical experiments establish the complete positive-parameter primitive-two-cycle census, the split-phase threshold \(a=1+\pi\), or the exact attracting window above that threshold. Their cited earlier Li et al. (2022) paper concerns compound lattice dynamics of another sinusoidal discrete system; a complete text comparison of that earlier source was not possible, and equivalent antecedents remain a residual originality risk. Other published periodic-orbit classifications for different sinusoidal and polynomial maps do not imply this model-specific classification without an additional reduction, for which no such reduction was found.

## Limitations
The result is restricted to real states, positive gains and the range \(0<a<1+2\pi\), although the map is defined more broadly. The theorem does not classify fixed points, prime periods larger than two, global attracting sets, basins or the qualitative nonlinear changes at nonhyperbolic endpoints. The stability conclusion is local and exponential in open intervals only. Accessible published literature does not prove global priority, and there has been no independent mathematical audit.

## References
1. X. Ge, C. Li, Y. Li, C. Zhang and C. Tao, "Multiple Alternatives of Offset Boosting in a Symmetric Hyperchaotic Map," *Symmetry* **15** (2023), 712, published 13 March 2023. https://doi.org/10.3390/sym15030712 . Model and original dynamical study; full HTML body inspected.
2. Y. Li, C. Li, S. Zhang, G. Chen and Z. Zeng, "A Self-Reproduction Hyperchaotic Map With Compound Lattice Dynamics," *IEEE Trans. Ind. Electron.* **69** (2022), 10564–10572. https://doi.org/10.1109/TIE.2022.3144592 . Related prior sinusoidal lattice literature; abstract/metadata only were accessible.
