# A sharp Schoenberg staircase for second-harmonic modulation of geodesic exponential kernels

## Finding
Let \(\mathbb S^2\subset\mathbb R^3\) be the unit round sphere, let \(\theta(x,y)=\arccos\langle x,y\rangle\in[0,\pi]\), and for \(a>0\), \(b\in\mathbb R\) define
\[
K_{a,b}(x,y)=e^{-a\theta(x,y)}\bigl(1+b\cos(2\theta(x,y))\bigr).
\]
The following is a *necessary and sufficient*, finite-algebraic positive-definiteness criterion for all finite point sets, with a sharp unbounded staircase of controlling harmonic degrees.

Put \(z=a^2\) and, for every integer \(n\ge0\), define
\[
R_n(z)=\frac{n^4+2n^3+(2z+7)n^2+(2z+6)n+z^2+z-12}{((n-2)^2+z)((n+3)^2+z)}.
\]
Define the quartic
\[
F_z(t)=-3t^4-12t^3+(4z+1)t^2+(8z+26)t+7z^2+35z+28.
\]
For each \(z>0\), \(F_z\) has a unique positive real zero \(\rho(z)>1\). If this zero is not an integer, set \(m(z)=\lceil\rho(z)\rceil\); if it is an integer, set \(m(z)=\rho(z)\). Define \(M(z)=R_{m(z)}(z)\), and at an integer zero note \(R_{m(z)}=R_{m(z)+1}=M(z)\). In all cases \(M(z)>1\).

Then \(K_{a,b}\) is positive semidefinite on **every** finite subset of \(\mathbb S^2\) if and only if
\[
\boxed{\begin{cases}
-1/M(z)\le b\le(z+9)/(3-z),&0<z<3,\\[2pt]
b\ge-1/M(z),&z\ge3.
\end{cases}}
\]
Every admitted kernel, **including every parameter boundary**, is strictly positive definite on every finite set of pairwise distinct sites. The pure oscillatory covariance \(e^{-a\theta}\cos(2\theta)\) is positive semidefinite, in fact strictly positive definite, if and only if \(a\ge\sqrt3\).

The maximizing harmonic degree advances through an infinite sequence of sharp changes. For every integer \(k\ge2\), put
\[
B_k=4k^2+8k+35,\quad C_k=-3k^4-12k^3+k^2+26k+28,\quad
z_k=\frac{\sqrt{B_k^2-28C_k}-B_k}{14}.
\]
These are strictly increasing positive real numbers. For \(0<z<z_2\), the controlling degree is \(m(z)=2\); for \(z_{k-1}<z<z_k\) with \(k\ge3\), it is \(m(z)=k\). At \(z=z_k\), exactly degrees \(k,k+1\) tie. In particular \(m(a^2)\sim\sqrt{7/3}\,a\) as \(a\to\infty\). At \(a=1\), \(m=3\), \(M=115/37\), and the exact admissible interval is \(-37/115\le b\le5\).

## Assumptions and scope
Positive semidefiniteness means that \((K_{a,b}(x_i,x_j))_{i,j}\) is Hermitian positive semidefinite for every finite choice of sites. Strict positive definiteness is asserted only for pairwise distinct sites. All angles are intrinsic shorter geodesic angles, not chordal Euclidean distances. There is no normalization to a unit diagonal: \(K_{a,b}(x,x)=1+b\), which is automatically positive in the admitted region. All assertions quantify over \(a>0\), real \(b\), all harmonic degrees, and arbitrary finite point configurations on \(\mathbb S^2\). No result is asserted at \(a=0\) or for other sphere dimensions.

## Proof
**1. Base Legendre moments.** With \(P_n(1)=1\), let
\[
A_n(a)=\int_0^\pi e^{-a\theta}P_n(\cos\theta)\sin\theta\,d\theta,
\quad E_n(a)=\int_0^\pi e^{-a\theta}P_n(\cos\theta)\,d\theta.
\]
Direct integration gives \(A_0=(1+e^{-\pi a})/(a^2+1)>0\) and \(A_1=(1-e^{-\pi a})/(a^2+4)>0\). The Legendre derivative identity \(P'_{n+1}-P'_{n-1}=(2n+1)P_n\), with integration by parts and the matching endpoint values of \(P_{n+1},P_{n-1}\), yields \(a(E_{n-1}-E_{n+1})=(2n+1)A_n\) for \(n\ge1\). The Legendre differential equation, integrated against \(e^{-a\theta}\), together with \((2n+1)xP_n=(n+1)P_{n+1}+nP_{n-1}\), gives
\[
a[nE_{n-1}+(n+1)E_{n+1}]=(2n+1)[a^2+n(n+1)]A_n.
\]
Solving yields \(E_{n+1}=(a^2+n^2)A_n/a\) and \(E_{n-1}=(a^2+(n+1)^2)A_n/a\). Comparing the formula for \(E_{n+1}\) at indices \(n\) and \(n+2\), including \(n=0\) by direct integration, proves
\[
A_{n+2}=\frac{a^2+n^2}{a^2+(n+3)^2}A_n\qquad(n\ge0).
\]
Thus \(A_n>0\) for all \(n\).

**2. Exact second-harmonic coefficients.** Write
\[
B_n(a)=\int_0^\pi e^{-a\theta}\cos(2\theta)P_n(\cos\theta)\sin\theta\,d\theta.
\]
The identity \(\cos(2\theta)=2\cos^2\theta-1\) and two applications of the three-term Legendre recurrence yield
\[
\cos^2\theta\,P_n(\cos\theta)=u_nP_{n+2}+v_nP_n+w_nP_{n-2},
\]
where \(u_n=(n+1)(n+2)/[(2n+1)(2n+3)]\), \(v_n=(n+1)^2/[(2n+1)(2n+3)]+n^2/[(2n+1)(2n-1)]\), and \(w_n=n(n-1)/[(2n+1)(2n-1)]\), with the last summand absent for \(n=0,1\). Substituting the base-moment recurrence gives exactly \(B_n=A_nR_n(z)\), including \(n=0,1\) by direct evaluation. In particular
\[
R_0=\frac{z-3}{z+9},\qquad R_1=\frac{z+4}{z+16},\qquad
R_n-1=\frac{6[3n(n+1)-2z-8]}{((n-2)^2+z)((n+3)^2+z)}.
\]
For \(n\ge1\), \(R_n>0\): it is immediate for \(n=1\), and for \(n\ge2\) every coefficient of the displayed numerator is nonnegative, with strictly positive constant part at \(n=2\). Also \(R_1-R_0=84/[(z+9)(z+16)]>0\). For any finite \(z\), all sufficiently large \(n\) have \(R_n>1\), while \(R_n\to1\), so a maximum \(M(z)>1\) exists and cannot be attained at degree zero.

**3. Unique sharp degree and its staircase.** Exact rational subtraction gives, for each integer \(n\ge0\),
\[
R_{n+1}-R_n=\frac{12(n+1)F_z(n)}{[(n-2)^2+z][(n-1)^2+z][(n+3)^2+z][(n+4)^2+z]}.
\]
For positive \(z\), the coefficients of \(F_z(t)\), in descending powers of \(t\), have signs \(-,-,+,+,+\). Descartes' rule and \(F_z(0)>0\), \(F_z(t)\to-\infty\), show that there is exactly one positive root and the sign changes from positive to negative there. Moreover \(F_z(1)>0\), so \(\rho(z)>1\). Hence the discrete sequence \(R_n\) increases up to one index and decreases afterward, with a possible tie across a single adjacent pair at integer \(\rho\). This proves the stated maximizer rule.

For every fixed \(t\ge0\), \(\partial_z F_z(t)=4t^2+8t+14z+35>0\); consequently \(\rho(z)\) is strictly increasing. For integers \(k\ge2\), \(F_0(k)<0\), whereas \(F_z(k)\to+\infty\) as \(z\to\infty\), and the unique positive root of \(F_z(k)=0\) is precisely \(z_k\). These crossing values increase with \(k\), and their comparisons give the stated sharp intervals and ties. Substituting \(t=ca\), \(z=a^2\) into \(F_z(t)=0\) and dividing by \(a^4\) yields in the limit \(-3c^4+4c^2+7=0\), whose unique positive solution is \(c=\sqrt{7/3}\), proving the asymptotic.

**4. Schoenberg positivity and strictness.** The degree-\(n\) Legendre coefficient of \(K_{a,b}\) has the sign of \(A_n+bB_n=A_n(1+bR_n(z))\). By Schoenberg's isotropic positive-definiteness criterion on \(\mathbb S^2\), nonnegativity for every \(n\) is necessary and sufficient. The positive ratios \(R_n\), \(n\ge1\), give exactly \(b\ge-1/M(z)\). The degree-zero coefficient contributes \(1+b(z-3)/(z+9)\ge0\), which gives the upper inequality only for \(z<3\). This proves the complete region and all boundary equalities. At the lower boundary, zero coefficients occur in at most two adjacent positive degrees; at the upper boundary, only degree zero vanishes. At any admissible parameter, all sufficiently high even and odd Legendre coefficients are strictly positive, since \(R_n\to1\) and \(-1/M>-1\). The standard strict-Schoenberg criterion (infinitely many positive coefficients of each parity on \(\mathbb S^2\)) proves strict positivity for distinct sites. Finally, the pure \(e^{-a\theta}\cos(2\theta)\) has coefficients \(B_n=A_nR_n\), all nonnegative exactly when \(R_0\ge0\), i.e. \(a^2\ge3\), and strictness follows by the same parity argument.

## Verification
The accompanying standalone `check.py` checks algebraically with SymPy the second-harmonic coefficient ratio and the exact first difference; it compares 40 independent high-precision Legendre integrals and modulation integrals at four damping values, checks the two-step base recurrence, and tests the first nineteen staircase crossings on either side. The checker was executed successfully from its delivered source. These finite computations corroborate identities; the full degree-uniform statements follow from the exact recurrence, Descartes sign argument, and Schoenberg theorem, not from numerical truncation.

## Relationship to prior work
The spherical positive-definiteness and Legendre-expansion framework is classical (Schoenberg 1942; Gneiting 2013). Buhmann and Jäger (first public arXiv version 2021-05-06) give general strictness tools for spherical kernels, but their studied radial/convolutional and axial results do not supply the sharp parameter cone or changing controlling harmonic degree of this doubly modulated geodesic exponential. White and Porcu (first public arXiv version 2018-07-11) develop spherical covariance modeling, not the evaluated second-harmonic cone.

A closely related evaluated cosine-*first*-harmonic exponential criterion computes a lower coefficient bound for \(e^{-a\theta}(1+b\cos\theta)\). Here the multiplier is instead \(1+b\cos(2\theta)\); its degree-zero coefficient changes sign with damping, yielding a genuinely different *two-sided/unbounded* admissible region and a different controlling-degree staircase. Another evaluated result for \(e^{-a\theta}\cos(m\theta)\) treats \(\mathbb S^3\), whose Gegenbauer coefficients and sharp frequency-two damping threshold differ from those on \(\mathbb S^2\). The prior results' general criteria can be used to test our coefficients but do not state or imply the finite evaluated cone without this new computation. An unindexed equivalent classification remains possible.

## Limitations
The cone applies to the unit two-sphere and to the specified second-geodesic-harmonic modulation; no necessity theorem for other sphere dimensions or noninteger oscillation frequency is claimed. Normalization to a correlation kernel is possible by dividing by \(1+b>0\). The mathematical proof is analytic, but the result has not undergone independent external audit or complete historical-priority verification. The positive-definiteness definition does not concern coincident duplicated sites for strictness.

## References
1. M. Buhmann and J. Jäger, *Strict positive definiteness of convolutional and axially symmetric kernels on d-dimensional spheres*, arXiv:2105.02586v1 (2021-05-06), https://arxiv.org/abs/2105.02586.
2. P. White and E. Porcu, *Towards a Complete Picture of Stationary Covariance Functions on Spheres Cross Time*, arXiv:1807.04272v1 (2018-07-11), https://arxiv.org/abs/1807.04272.
3. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077v1 (2011-11-30), https://arxiv.org/abs/1111.7077.
4. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal 9 (1942), 96–108.
5. D. Chen, V. A. Menegatto and X. Sun, *A necessary and sufficient condition for strictly positive definite functions on spheres*, Proceedings of the American Mathematical Society 131 (2003), 2733–2740.
