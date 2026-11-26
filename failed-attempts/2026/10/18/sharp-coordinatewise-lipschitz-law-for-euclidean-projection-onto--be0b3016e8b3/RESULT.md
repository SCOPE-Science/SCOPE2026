# Sharp coordinatewise Lipschitz law for Euclidean projection onto Lorentz cones

## Finding
For an integer \(d\ge1\), define the Lorentz cone and its Euclidean metric projection by
\[
\mathcal L_{d+1}=\{(t,z)\in\mathbb R\times\mathbb R^d:t\ge\|z\|_2\},\qquad P_d(x)=\operatorname*{argmin}_{y\in\mathcal L_{d+1}}\|x-y\|_2.
\]
Set \(L_{d,r}=\sup_{x\ne y}\|P_d(x)-P_d(y)\|_r/\|x-y\|_r\) for \(r\in\{1,\infty\}\), with *ordinary unweighted coordinate norms* in \(\mathbb R^{d+1}\). Then \(L_{d,1}=L_{d,\infty}=:L_d\) and
\[
L_d=\begin{cases}
1,&d=1,\\
1+\dfrac12\max_{0\le a\le1}\left[a-a^2+\sqrt{d-1}\,a\sqrt{1-a^2}\right],&2\le d\le4,\\
\dfrac{1+\sqrt d}{2},&d\ge5.
\end{cases}
\]
For \(2\le d\le4\), the scalar optimization has a unique maximizer \(a_d\in(0,1)\), characterized by
\[
1-2a_d+\sqrt{d-1}\,\frac{1-2a_d^2}{\sqrt{1-a_d^2}}=0.
\]
The transition at spatial dimension five is strict. For \(d\ge5\), the worst output coordinate is the scalar or cone-axis coordinate; for \(2\le d\le4\), a spatial coordinate is worse. The projection is \(\ell_1\)- and \(\ell_\infty\)-nonexpansive precisely for \(d=1\).

## Assumptions and scope
The field is real, the projection uses Euclidean distance, and the Lipschitz quotients use respectively \(\ell_1^{d+1}\) and \(\ell_\infty^{d+1}\). Both norms have **unweighted** standard coordinates consisting of one axis coordinate and \(d\) spatial coordinates. No assertion is made for weighted coordinates, non-Euclidean projections, general cones, or infinite-dimensional spaces. The displayed maxima are global over all distinct point pairs; limiting Jacobians at a boundary are legitimate witnesses to the sharp Lipschitz supremum.

## Proof
**Projection and derivative.** Write \(r=\|z\|_2\). The Moreau decomposition of the self-dual Lorentz cone gives
\[
P_d(t,z)=\begin{cases}
(t,z),&t\ge r,\\
(0,0),&t\le-r,\\
\bigl((t+r)/2,(1+t/r)z/2\bigr),&-r<t<r.
\end{cases}
\]
For the middle case the displayed projected point belongs to the cone, the residual belongs to its negative dual, and their Euclidean inner product vanishes, directly proving the projection formula. At a differentiability point in the middle region set \(u=z/r\in\mathbb S^{d-1}\) and \(s=t/r\in(-1,1)\). Direct differentiation yields the symmetric block matrix
\[
DP_d(t,z)=\frac12\begin{pmatrix}
1&u^{\mathsf T}\\
u&(1+s)I_d-suu^{\mathsf T}
\end{pmatrix}.
\]
Elsewhere the derivative is \(I\) or zero. Every displayed derivative is symmetric. For a matrix, the induced \(\ell_\infty\)-norm is the largest absolute row sum, whereas its induced \(\ell_1\)-norm is the largest absolute column sum; thus they coincide for these derivatives. Bounding these derivatives gives a global Lipschitz bound: the continuous, piecewise smooth projection is locally Lipschitz, and line-segment integration, first on generic segments crossing differentiability regions almost everywhere and then by continuity, gives the bound for arbitrary pairs. Conversely, the norm of every derivative is bounded above by the optimal global Lipschitz constant. Limits of derivatives approaching the cone boundary are also valid lower bounds.

**Reduction to scalar optimization.** The scalar-output row has absolute sum \((1+\|u\|_1)/2\), with maximum
\[
T_d=(1+\sqrt d)/2.
\]
For a spatial row \(i\), put \(a=|u_i|\) and \(b=\sum_{j\ne i}|u_j|\). Its absolute row sum is
\[
R_i(s,u)=\frac12\bigl[a+1+s(1-a^2)+|s|ab\bigr].
\]
Here the diagonal term remains nonnegative throughout \(-1<s<1\). The largest endpoint of this piecewise-linear expression is \(s\uparrow1\), since its value there exceeds its value at \(s\downarrow-1\) by \(1-a^2\); the value at zero cannot be larger. By Cauchy–Schwarz,
\[
b\le\sqrt{(d-1)(1-a^2)},
\]
with equality when all other spatial coordinates have equal absolute value. For \(d\ge2\) this yields the *exact* spatial-row supremum
\[
S_d=1+\frac12\max_{0\le a\le1}\left[a-a^2+\sqrt{d-1}\,a\sqrt{1-a^2}\right].
\]
The equality directions just described, followed by \(s\uparrow1\), show that this is an attainable supremum of derivatives. Hence \(L_d=\max\{1,T_d,S_d\}\). For \(d=1\), \(u=\pm1\) and every nonzero middle derivative has both row sums one; hence \(L_1=1\).

**Uniqueness.** For \(d\ge2\), the function within the scalar maximum has second derivative \(-2+\sqrt{d-1}\,a(2a^2-3)/(1-a^2)^{3/2}<0\) in \((0,1)\), derivative positive at zero and tending to negative infinity at one. It therefore has exactly one interior maximizer, satisfying the equation in the finding.

**Sharp dimension threshold.** Set \(B_d(a)=1+a-a^2+a\sqrt{d-1}\sqrt{1-a^2}\). Then \(S_d=(1+\max_a B_d(a))/2\) and \(T_d=(1+\sqrt d)/2\). For \(2\le d\le4\), testing \(a=2/3\) gives
\[
B_d(2/3)=\frac{1}{9}\bigl[11+2\sqrt{5(d-1)}\bigr].
\]
To see that this exceeds \(\sqrt d\), note that \(\frac{11+2\sqrt{5(d-1)}}9-\sqrt d\) is decreasing on \([2,4]\) and is positive at \(d=4\), where \(11+2\sqrt{15}>18\). Thus \(S_d>T_d\) in these three dimensions.

For \(d=5\), concavity of \(a\mapsto\sqrt{1-a^2}\) and its tangent at \(a=3/5\) give
\[
\sqrt{1-a^2}\le\frac54-\frac34a,
\qquad
B_5(a)\le1+\frac72a-\frac52a^2\le\frac{89}{40}<\sqrt5.
\]
For any fixed \(a\in[0,1]\), the function \(q\mapsto\sqrt q-a\sqrt{1-a^2}\sqrt{q-1}\) is strictly increasing for \(q\ge2\) because \(a\sqrt{1-a^2}\le1/2\). Consequently \(B_d(a)<\sqrt d\) for every integer \(d\ge5\). This proves \(S_d<T_d\) and completes the exact phase classification.

## Verification
A standalone Python 3 script `check_soc_projection.py` verifies the explicit derivative against central differences, row/column symmetry, directional lower witnesses, the scalar critical-point equations, the proposed dimension ordering for tested dimensions, and the rational inequality \((89/40)^2<5\). A deterministic run completed 130,484 assertion groups in dimensions \(1\) through \(15\). The universal dimension statement and all sharp equalities follow from the preceding proof, not from finite computation. Execute `python3 check_soc_projection.py` using only the Python standard library.

## Relationship to prior work
Wang and Xiu (2011), Section 2.2, equations (10)–(11) and Propositions 2.2–2.4, give projection and generalized derivative formulas for axis-weighted second-order cones; the unit-weight special case supplies the standard Lorentz-cone formula independently reconstructed above. Kong, Tunçel, and Xiu (2009), Section 3, develop the generalized Jacobian of symmetric-cone projections, which includes these cones. Their statements concern derivative structures, rather than optimization of coordinatewise \(\ell_1\)- or \(\ell_\infty\)-Lipschitz constants, the scalar uniqueness law, and the exact dimension-five switch. Those sharp global norms require the row-sum optimization and dimension inequalities proved here.

Outrata and Sun (2008) analyze the coderivative of the same projection. Its original full text was not accessible during the comparison; this is a bibliographic limitation, not evidence that it lacks a relevant statement. A general nonsmooth sensitivity theorem could also subsume the present conclusion under different terminology.

## Limitations
The result is finite-dimensional, real and unweighted. It does not characterize all point pairs attaining the supremum; spatial dominance is witnessed by limiting derivatives. The numerical checker supplies corroboration only. The originality assessment is conditional on the literature inspected; especially the Outrata–Sun full text remains uninspected. No independent audit has been performed.

## References
1. Y. Wang and N. Xiu, *Strong Semismoothness of Projection onto Slices of Second-Order Cone*, Journal of Optimization Theory and Applications **150** (2011), 599–614, DOI `10.1007/s10957-011-9834-2`. Published online 20 April 2011.
2. L. Kong, L. Tunçel and N. Xiu, *Clarke Generalized Jacobian of the Projection onto Symmetric Cones*, Set-Valued and Variational Analysis **17** (2009), 135–151, DOI `10.1007/s11228-009-0113-4`; author's full-text preprint at `https://www.math.uwaterloo.ca/~ltuncel/publications/CGJ-SVVA2.pdf`.
3. J. V. Outrata and D. Sun, *On the Coderivative of the Projection Operator onto the Second-Order Cone*, Set-Valued Analysis **16** (2008), 999–1014, DOI `10.1007/s11228-008-0092-x`.
