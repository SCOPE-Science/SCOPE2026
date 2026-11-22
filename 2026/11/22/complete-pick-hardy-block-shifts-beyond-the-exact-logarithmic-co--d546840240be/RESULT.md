# Complete-Pick Hardy-block shifts beyond the exact logarithmic-concavity boundary

## Finding
For \(a>c>1\), a real \(b\), and \(b^2\le(a^2-c^2)(c^2-1)\), the natural two-site Hardy-block shift defined below has a complete Nevanlinna–Pick reproducing kernel, even when it is not logarithmically concave. Its logarithmic-concavity condition is exactly
\[
 b^2\le \frac{(a^2-c^2)(c^2-1)}{c^2}.
\]
Thus there is a nonempty open interval of squared couplings, strictly between this threshold and \((a^2-c^2)(c^2-1)\), on which the complete-Pick property survives but logarithmic concavity fails. The shift remains expansive with rank-two strictly positive defect. The upper bound is a sufficient complete-Pick condition, not a claimed exact complete-Pick boundary.

## Assumptions and scope
Put \(q(z)=ac+bz\), and equip \(H^2(\mathbb D)\oplus\mathbb C^2\) with its standard Hilbert norm. Define
\[
 T(f,x_0,x_1)=(zf+cx_0+bx_1,ax_1,0),\qquad
 U(f,x_0,x_1)(z)=\frac{z^2f(z)+czx_0+q(z)x_1}{q(z)}.
\]
The parameter bound gives \(|b|<ac\), so \(q\) is nonzero on the closed unit disk. The map \(U\) is a bounded bijection onto \(H^2\) with bounded inverse (as a map of underlying function spaces): from \(g=U(f,x_0,x_1)\), recover \(x_1=g(0)\), \(x_0=ag'(0)\), and
\[
 f(z)=q(z)\frac{g(z)-g(0)-zg'(0)}{z^2}+b g'(0).
\]
The quotient is understood through its analytic value at zero. Give the range of \(U\) the transported Hilbert norm, denoting this analytic space by \(\mathcal H_{a,c,b}\). We have \(UT=M_zU\); the forward and backward shifts are bounded on this space. The kernel is normalized at zero and is
\[
 K(z,w)=1+\frac{c^2z\bar w+(z\bar w)^2/(1-z\bar w)}{q(z)\overline{q(w)}}.
\]
For the Pick claim, use the standard criterion: a nonvanishing normalized kernel on the unit disk is complete Nevanlinna–Pick when \(F(z,w)=1-1/K(z,w)\) is positive semidefinite.

## Proof
**Part I: positivity of the Pick defect.** Write \(t=z\bar w\) and \(Q=1-(1-t)K\). Then exact algebra gives
\[
 Q(z,w)=\frac{tR(z,w)}{q(z)\overline{q(w)}},\qquad
 R(z,w)=q(z)\overline{q(w)}-c^2+(c^2-1)t.
\]
The coefficient matrix of the Hermitian polynomial kernel \(R\) in the ordered basis \((1,z)\) is
\[
 \begin{pmatrix}c^2(a^2-1)&acb\\acb&b^2+c^2-1\end{pmatrix},
\]
whose determinant is \(c^2((a^2-1)(c^2-1)-b^2)>0\) under the stated assumptions. Thus \(R\), and therefore \(Q\), are positive semidefinite kernels. For \(z\in\mathbb D\), the identity \(Q(z,z)=1-(1-|z|^2)K(z,z)\), with \(K(z,z)>0\), yields \(0\le Q(z,z)<1\). Hence \(|Q(z,w)|<1\) by Cauchy–Schwarz, and \((1-Q)^{-1}=\sum_{n\ge0}Q^n\) is a positive semidefinite kernel by the Schur product theorem.

Define \(H(z,w)=c^2R(z,w)-(c^2-1)q(z)\overline{q(w)}\). Its coefficient matrix is
\[
 \begin{pmatrix}c^2(a^2-c^2)&acb\\acb&b^2+c^2(c^2-1)\end{pmatrix},
\]
with determinant \(c^4((a^2-c^2)(c^2-1)-b^2)\ge0\). Since \(a>c>1\), this matrix is positive semidefinite. A direct rational identity gives
\[
 F(z,w)=\frac{c^2t}{q(z)\overline{q(w)}}+
 \frac{t^2 H(z,w)}{[q(z)\overline{q(w)}]^2(1-Q(z,w))}.
\]
Each term is positive semidefinite: \(t\) and \(t^2\) are positive kernels, multiplication by nonvanishing analytic factors preserves positivity, \(H\) is positive, and \((1-Q)^{-1}\) is positive. Also \(K=(1-Q)/(1-t)\) never vanishes because \(|Q(z,w)|<1\) and \(|t|<1\). Thus \(F=1-1/K\) is positive and the kernel is complete Pick.

**Part II: the exact logarithmic-concavity boundary.** Let \(\Delta=T^*T-I\). It vanishes on the Hardy summand; on the finite summand, its matrix and the finite-coordinate compression of \(T\) are
\[
 D=\begin{pmatrix}c^2-1&bc\\bc&a^2+b^2-1\end{pmatrix},
 \qquad A=\begin{pmatrix}0&a\\0&0\end{pmatrix}.
\]
The determinant \(\det D=(a^2-1)(c^2-1)-b^2>0\), together with \(D_{00}=c^2-1>0\), makes \(\Delta\) positive of rank exactly two; hence the shift is expansive. The logarithmic-concavity inequality \(T^{*2}T^2\le(T^*T)^2\) is exactly \(T^*\Delta T\le\Delta+\Delta^2\), or \(P:=D+D^2-A^*DA\succeq0\). One checks
\[
 P_{00}=c^2(b^2+c^2-1)>0,
 \qquad \det P=a^2c^2\big((a^2-c^2)(c^2-1)-b^2c^2\big).
\]
The two-by-two principal-minor criterion therefore gives precisely \(b^2\le(a^2-c^2)(c^2-1)/c^2\). On the strictly larger range \((a^2-c^2)(c^2-1)/c^2<b^2<(a^2-c^2)(c^2-1)\), Part I still proves complete Pick, while \(\det P<0\) disproves logarithmic concavity. This is a nonempty open region because \(c>1\).

For the explicit parameters \((a,c,b)=(3,2,2)\), the two matrices are \(D=\left(\begin{smallmatrix}3&4\\4&12\end{smallmatrix}\right)\) and \(P=\left(\begin{smallmatrix}28&64\\64&145\end{smallmatrix}\right)\), with \(\det D=20>0\) and \(\det P=-36<0\). The Pick-positivity certificate for this point uses the matrix \(H=\left(\begin{smallmatrix}20&12\\12&16\end{smallmatrix}\right)\), whose determinant is \(176>0\).

## Verification
The standalone \(`verify_kernel.py`\) checks the symbolic polynomial/rational identities for \(Q\), \(F\), the determinants of \(R\), \(H\), \(D\), and \(P\), and the exact example, using SymPy. Executing \(`python verify_kernel.py`\) requires Python 3 and SymPy. The computational check is supplementary: the proof above establishes the kernel positivity for every point of the uncountable parameter region, not merely sample points.

## Relationship to prior work
Luo and Rydhe established that concavity of the forward shift is sufficient for the complete Pick property and gave a logarithmically concave non-Pick example of rank-three defect. Earlier analysis of this same two-site Hardy-block model covered its logarithmically concave cone. Here the new assertion concerns the **disjoint region beyond that exact cone**, where complete Pick persists but logarithmic concavity fails; in particular it does not reassert the known implication for concave shifts or the earlier model cone. This provides a converse separation, not a strengthening of the published rank-three counterexample. The normalized-kernel positivity criterion itself is classical.

## Limitations
The criterion \(b^2\le(a^2-c^2)(c^2-1)\) is only sufficient for complete Pick. No necessity result is asserted beyond the exact logarithmic-concavity boundary. These are a concrete three-parameter family of Hardy-block shifts, not all rank-two-defect shifts or arbitrary reproducing kernels. Priority relative to older, differently formulated de Branges–Rovnyak model calculations has not been independently established. Self-review is not independent validation.

## References
1. Shuaibing Luo and Eskil Rydhe, *Concave shifts and the complete Nevanlinna–Pick property*, arXiv:2611.12778v1, posted 9 November 2026. https://arxiv.org/abs/2611.12778
2. Jim Agler and John E. McCarthy, *Complete Nevanlinna–Pick kernels*, Journal of Functional Analysis **175** (2000), 111–124. (Standard positivity characterization.)
