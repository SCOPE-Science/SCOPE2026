# Exact mixed-radius Szegő orbit determinant design and its quarter-power angular collapse

## Finding
Let \(0<r,s<1\). For distinct points \(a_1,a_2\) of modulus \(r\) and a point \(a_3\) of modulus \(s\), let \(B\) be the finite Blaschke product with these three simple zeros. In \(H^2(\mathbb D)\), set
\[
 k_a(z)=\frac{\sqrt{1-|a|^2}}{1-\overline a z},
 \qquad \mathcal F=\{B^n k_{a_j}:n\ge0,\ 1\le j\le3\}.
\]
This is a Riesz basis, and its three-by-three seed Gram determinant \(\det G\) (equivalently the squared three-generator synthesis volume of each orbit block) is maximized, uniquely up to common rotation and interchange of \(a_1,a_2\), by
\[
 a_3=s,\qquad a_1=-r e^{i\theta_*},\qquad a_2=-r e^{-i\theta_*},\qquad 0<\theta_*<\frac\pi2.
\]
Define \(A=r^2+s^2\), \(C=1+r^2s^2\), \(b=2rs\), \(h=(1-r^2)^2\), and \(q=4r^2\). Then \(c_*:=\cos\theta_*\) is the **unique** root in \((0,1)\) of
\[
 c h(A+bc)(C+bc)=b(C-A)(1-c^2)\bigl[h+q(1-c^2)\bigr]. \tag{1}
\]
The exact maximum is
\[
 \boxed{D_*(r,s)=\frac{q(1-c_*^2)}{h+q(1-c_*^2)}
 \left(\frac{A+bc_*}{C+bc_*}\right)^2.} \tag{2}
\]
This includes the equal-radius consistency case \(r=s\), for which \(c_*=1/2\) (the regular triangle). The new mixed-radius conclusion concerns \(r\ne s\).

For every fixed \(s\in(0,1)\), the **sharp boundary-clustering law** is
\[
 \boxed{\theta_*(r,s)\sim
 \left(\frac{(1+s)^4}{8s(1-s^2)}\right)^{1/4}
 (1-r^2)^{1/4}\qquad(r\uparrow1).} \tag{3}
\]
Thus the optimal separation of the two radius-\(r\) nodes, equal to \(2\theta_*\), tends to zero at a quarter-power scale even though the optimized Gram determinant tends to one. In fact
\[
 D_*(r,s)=1-\frac{2(1-s)}{1+s}(1-r^2)
 +O_s\bigl((1-r^2)^{3/2}\bigr). \tag{4}
\]
The problem is D-optimal design: maximizing the Gram determinant, **not** minimizing the spectral condition number or maximizing the smallest frame eigenvalue.

## Assumptions and scope
The Hardy-space norm is \(\|\sum_{n\ge0}f_nz^n\|^2=\sum_{n\ge0}|f_n|^2\). The three points are free to move angularly while their respective Euclidean moduli are constrained to \(r,r,s\). No repeated points are allowed; the strict optimizer is automatically distinct. The seed vectors are raw normalized Szegő kernels, not orthogonalized Malmquist–Walsh generators. The finite Gram determinant is used; no determinant of an infinite-dimensional frame operator is asserted. Statements (3)–(4) fix \(s\) before sending \(r\) to one.

## Proof
**1. Reduction to three pseudohyperbolic distances.** For a finite Blaschke product with simple zeros \(a_j\), the model space \(K_B=H^2\ominus BH^2\) has dimension three and contains the three kernels \(k_{a_j}\). The Cauchy double-alternant gives
\[
 \det G=\prod_{i<j}\rho(a_i,a_j)^2,
 \qquad \rho(u,v)=\left|\frac{u-v}{1-\overline u v}\right|.
 \tag{5}
\]
The determinant is positive for distinct nodes, hence the three kernels form a basis of \(K_B\). The Wold decomposition \(H^2=\bigoplus_{n\ge0}B^nK_B\), orthogonal because \(B\) is inner, shows that \(\mathcal F\) is a Riesz basis and has the same three-by-three Gram block on every level. Formula (5) therefore exactly describes the volume objective.

**2. Global reflection of the optimal geometry.** Rotate so \(a_3=s>0\). Every unordered pair on the radius-\(r\) circle may be represented as
\[
 a_1=r e^{i(u+t)},\quad a_2=r e^{i(u-t)},\quad
 0\le t\le\pi/2,
\]
by taking their shorter angular separation (and adjusting \(u\)). Write \(c=\cos t\in[0,1]\), \(x=\cos u\in[-1,1]\). The first factor in (5) depends only on \(t\). The product of the other two factors is
\[
 R(x)=\frac{Q_A(x)}{Q_C(x)},\qquad
 Q_L(x)=L^2-b^2(1-c^2)-2Lbcx+b^2x^2.
 \tag{6}
\]
Both \(Q_A,Q_C\) are positive for distinct configurations; at any coincident configuration the objective is zero and cannot maximize. Direct algebra gives
\[
 \begin{split}
 Q_A(-1)Q_C(x)-Q_A(x)Q_C(-1)
 ={}&b(A-C)(x+1)\bigl[b(A+C)(x-1)\\
 &-2ACc+2b^2c(c^2+x-1)\bigr].
 \end{split} \tag{7}
\]
Since \(C-A=(1-r^2)(1-s^2)>0\), \(AC\ge b^2\) by the two arithmetic–geometric mean inequalities, \(x\le1\), and \(c\ge0\), the bracket in (7) is nonpositive. Consequently \(R(x)\le R(-1)\). For \(c>0\) equality forces \(x=-1\). Thus one can—and, at any strict interior optimum, must—place the equal-radius points symmetrically about the ray opposite \(a_3\). The degeneracies \(c=0,1\) are dealt with in Step 3.

**3. Exact scalar optimization.** With \(u=\pi\), (5) becomes
\[
 F(c)=\frac{q(1-c^2)}{h+q(1-c^2)}
 \left(\frac{A+bc}{C+bc}\right)^2,
 \qquad 0\le c\le1. \tag{8}
\]
It is positive for \(c<1\), with \(F(1)=0\). Direct logarithmic differentiation shows
\[
 \frac12\frac{F'(c)}{F(c)}=
 -\frac{ch}{(1-c^2)[h+q(1-c^2)]}
 +\frac{b(C-A)}{(A+bc)(C+bc)}.
 \tag{9}
\]
At \(c=0\), this derivative is strictly positive. For \(c\uparrow1\) it is negative. The equation \(F'=0\) is (1): its left side is strictly increasing in \(c\in[0,1]\), its right side strictly decreasing, the former starts at zero and the latter ends at zero. Hence it has exactly one interior root, the unique global maximum. By Step 2 its complete angular configuration is uniquely determined modulo rotations and swapping the equal-radius nodes. Equation (2) follows.

**4. Boundary-clustering scale.** Fix \(0<s<1\), write \(\epsilon=1-r^2\) and \(\delta=1-c_*^2=\sin^2\theta_*\). Cancel one \(\epsilon\) in (1) to get
\[
 c_*\epsilon(A+bc_*)(C+bc_*)
 =b(1-s^2)\delta(\epsilon^2+4r^2\delta). \tag{10}
\]
As \(r\uparrow1\), the right side would stay strictly positive if \(\delta\) did not tend to zero, while the left side tends to zero. Hence \(\delta\to0\), \(c_*\to1\). Since the left side is asymptotic to \(\epsilon(1+s)^4\), (10) forces \(\delta\gg\epsilon^2\) and then
\[
 \delta^2\sim\epsilon\frac{(1+s)^4}{8s(1-s^2)}.
\]
Because \(\sin\theta_*\sim\theta_*\), this is precisely (3).

Finally the first factor of (8) is \(1-O_s(\epsilon^{3/2})\) by \(\delta\asymp\epsilon^{1/2}\). The other factor equals \([1-\epsilon(1-s^2)/(C+bc_*)]^2\), with \(C+bc_*=(1+s)^2+O_s(\epsilon^{1/2})\). Expanding proves (4).

## Verification
Run the standalone pure-Python file `CHECK.py`. It compares the exact Cauchy-Gram determinant with the product in (5); checks algebraic identity (7) on rational inputs using exact fractions; tests (1)–(2) against direct angular sampling for mixed radii; verifies the equal-radius special case; and evaluates the asymptotic ratio in (3) for decreasing \(1-r^2\). These finite experiments are consistency checks only. The global optimality, uniqueness, and asymptotic are proved analytically in Steps 1–4.

## Relationship to prior work
Aguilera and Carando [1, Theorem 2.6 and Example 2.7] establish finite-Blaschke orbit bases and use orthogonalized Malmquist–Walsh generators. They do not optimize the determinant of unorthogonalized point-evaluation kernels at constrained radii. The published result [2] proves a sharp equiradial \(d\)-point determinant inequality and exact regular-polygon frame spectrum; its stated scope explicitly excludes *mixed radii*. Its \(d=3\) equal-radius case agrees with \(c_*=1/2\), but it does not imply the asymmetric optimizer, unique scalar equation (1), or quarter-power law (3). General kernel Fekete-point constructions [3] motivate determinant design but concern approximate determinants and mainly Gaussian kernels rather than this mixed-radius Hardy orbit problem. Classical Cauchy determinant and pseudohyperbolic identities are used as known tools, not claimed to be new.

## Limitations
The theorem treats exactly three simple zeros with prescribed moduli \((r,r,s)\), not arbitrary three unequal moduli, larger configurations, multiplicities, or other reproducing kernels. The objective is the *determinant*, not the minimum singular value. The sharp quarter-power law is for fixed interior \(s\). General historical Fekete-energy rearrangement results might contain an equivalent prescribed-modulus extremal under another formulation; no assertion of exhaustive publication priority or independent validation is made.

## References
[1] A. Aguilera and D. Carando, *Frames of orbits of multiplication operators on Hardy spaces*, arXiv:2606.00912v1, first public 30 May 2026, https://arxiv.org/abs/2606.00912.

[2] *Sharp determinant stability and conditioning of concentric Szegő orbit frames*, public mathematical record, 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-determinant-stability-and-conditioning-of-concentric-szeg--44f30fce73fa.

[3] T. Karvonen, S. Särkkä, and K. Tanaka, *Kernel-based interpolation at approximate Fekete points*, Numerical Algorithms 87 (2021), 445–468; arXiv:1912.07316, https://arxiv.org/abs/1912.07316.
