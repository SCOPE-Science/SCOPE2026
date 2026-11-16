# Phase-anisotropic restoration of the half-density Gabor frame for an odd rational window

## Finding
For complex \(c=u+iv\), consider the rational window
\[
g_c(t)=\frac{t+c}{(t^2+1)(t^2+4)},\qquad t\in\mathbb R,
\]
and the Gabor system \(\{e^{\pi i m t}g_c(t-n):m,n\in\mathbb Z\}\) in \(L^2(\mathbb R)\). Let \(A(c)\) denote its **optimal lower frame bound**, with \(A(c)=0\) if no positive lower frame bound exists. There is \(\eta>0\) such that \(A(0)=0\) but \(A(c)>0\) for every \(0<|c|<\eta\). Moreover, uniformly in the argument of \(c\),
\[
\boxed{A(u+iv)=C_Ru^2+C_Iv^2+o(u^2+v^2)\qquad(c\to0).}
\]
Both constants are explicit and strictly positive. Define
\[
\begin{aligned}
q&=e^{-2\pi},\\
h_0&=\frac{\pi}{3}\left(\coth\pi-\tfrac12\coth2\pi\right),&
h_1&=\frac{\pi}{3}\left(\operatorname{csch}\pi-\tfrac12\operatorname{csch}2\pi\right),\\
d_0&=\frac{\pi^2}{3}\left(\operatorname{csch}^2\pi-\operatorname{csch}^22\pi\right),&
d_1&=\frac{\pi^2}{3}\left(\operatorname{csch}\pi\coth\pi-\operatorname{csch}2\pi\coth2\pi\right),\\
b_0&=-\frac{2\pi^2}{3}\frac{1-q}{1+q},&
b_1&=\frac{4\pi^2\sqrt q}{3}\frac{(1-\sqrt q)^2}{1-q^2}.
\end{aligned}
\]
Then
\[
\boxed{C_R=\frac{(h_0d_1-h_1d_0)^2}{d_0^2+d_1^2}
=0.267745213797018\ldots,}
\qquad
\boxed{C_I=\frac{(h_0b_1-h_1b_0)^2}{b_0^2+b_1^2}
=0.0169530120582406\ldots.}
\]
In particular, at equal small perturbation magnitude, a **real numerator perturbation** protects the lower frame bound approximately \(15.793\) times as effectively as a purely imaginary perturbation. Equal magnitudes also have equal \(L^2\) window norms, because the odd and even real parts are orthogonal.

## Assumptions and scope
Use the integer Zak transform \(Zf(x,\omega)=\sum_{n\in\mathbb Z}f(x-n)e^{2\pi in\omega}\), regarded with its quasiperiodic boundary identifications. The frame bound is the largest \(A\ge0\) satisfying
\[
A\|f\|_2^2\le\sum_{m,n\in\mathbb Z}
\left|\left\langle f,e^{\pi im(\cdot)}g_c(\cdot-n)\right\rangle\right|^2
\quad\text{for all }f\in L^2(\mathbb R).
\]
No normalization by \(\|g_c\|_2\) is imposed. The expansion is local near \(c=0\), without a global classification for large \(|c|\). Real and imaginary perturbations are independent real parameters.

## Proof
**1. Exact fiber multiplier.** Write \(g_c=g_0+ch\), with \(g_0(t)=t/[(t^2+1)(t^2+4)]\) and \(h(t)=1/[(t^2+1)(t^2+4)]\). Integer-lattice Zak Parseval, applied separately to the two modulation cosets, gives the scalar symbol
\[
S_c(x,\omega)=|Zg_c(x,\omega)|^2+|Zg_c(x,\omega+1/2)|^2.
\]
The continuous and bounded symbol has \(A(c)=\min S_c\) on the compact Zak torus. The Zak sums for \(g_0\), \(h\), and the first derivatives of \(Zg_0\) converge absolutely and uniformly (the required derivatives have summands of order at most \(|n|^{-2}\)). Consequently the following first-order expansions are uniform on small neighborhoods.

**2. The only vanishing fibers at \(c=0\).** For this particular rational window, the Zak zero set is exactly
\[
\{(0,0),(1/2,0),(0,1/2)\}\pmod{\mathbb Z^2}.
\]
This is an established, explicitly proved rational-Zak identity [3], not a new assertion. For clarity its algebraic certificate is as follows. Put \(q=e^{-2\pi}\), \(z=e^{2\pi ix}\), \(r=e^{2\pi\omega}\). Up to a nonzero prefactor and complex conjugation, \(Zg_0\) equals
\[
B(z,r)=\frac{rqz}{1-qz}-\frac{r^2q^2z}{1-q^2z}
-\frac{r^{-1}}{1-q/z}+\frac{r^{-2}}{1-q^2/z}.
\]
For \(0<\omega<1\) and \(z\ne\pm1\), separation of the real and imaginary parts and elimination give
\[
(q-1)(qr^2-1)(q^2r^4+q^2r^2+2qr^2+r^2+1)=0.
\]
The last factor is positive, so \(r=q^{-1/2}\). At this value the expression factors as \((z-1)\) times a strictly positive real factor on the unit circle (positivity follows from \(1+q^2>\sqrt q(1+q)\)), leaving only \(z=1\). At \(z=1\), direct factorization gives \(B(1,r)=(r-1)(qr-1)(qr^2-1)/[r^2(q-1)(q+1)]\). The \(z=-1\) case has no interior-frequency zero, and on the frequency boundary \(\omega=0\), the imaginary part is \(2\sin(2\pi x)[q/D_1-q^2/D_2]\), where \(D_j=|1-q^jz|^2\) and \(D_2-qD_1=(1-q)(1-q^3)>0\). This proves the three-point list. Thus the two terms of \(S_0\) vanish simultaneously only at \((0,0)\) and \((0,1/2)\), which are the same two-channel configurations with their order exchanged. Away from these two points, compactness gives a strictly positive lower bound.

**3. Exact local derivatives.** At the two frequencies \(\omega_0=0\) and \(\omega_1=1/2\), evaluated at \(x=0\), oddness implies \(Zg_0(0,\omega_j)=0\); evenness gives \(Zh(0,\omega_j)=h_j>0\). The spatial and frequency derivatives satisfy
\[
\partial_xZg_0(0,\omega_j)=d_j\in\mathbb R,
\qquad\partial_\omega Zg_0(0,\omega_j)=i b_j,
\]
with the six constants in the Finding. One exact derivation uses the partial fraction identity
\[
 g_0(t)=\tfrac13\left(\frac{t}{t^2+1}-\frac{t}{t^2+4}\right),
\qquad h(t)=\tfrac13\left(\frac1{t^2+1}-\frac1{t^2+4}\right),
\]
paired with the classical cotangent and cosecant periodization formulas for ordinary and alternating integer sums; alternatively, termwise differentiation of the convergent rational-Zak formula above supplies \(b_0,b_1\). In particular \(h_0>h_1>0\), \(0<d_0<d_1\), and \(b_0<0<b_1\). Hence both determinants \(h_0d_1-h_1d_0\) and \(h_0b_1-h_1b_0\) are strictly nonzero.

**4. Global sharp expansion.** Near \((0,0)\), for small real \((x,\omega,u,v)\), the two-channel first-order vector has components
\[
Zg_c(x,\omega+\omega_j)=d_jx+h_ju+i(b_j\omega+h_jv)
+o(|x|+|\omega|+|c|),\qquad j=0,1.
\]
The two other possible common-zero configurations simply exchange the indices. The positive real numbers \(d_0^2+d_1^2\) and \(b_0^2+b_1^2\) make the unperturbed quadratic fiber form strictly positive definite in the spatial and frequency coordinates. Evaluating \(S_c\) at a common zero gives \(A(c)=O(|c|^2)\). Compactness and the local nondegeneracy then force every minimizing fiber to lie within \(O(|c|)\) of one of the common-zero points: otherwise its unperturbed fiber amplitude would exceed the uniform \(O(|c|)\) perturbation. Consequently the minimization reduces, with error \(o(|c|^2)\) uniform in phase, to
\[
\min_{X,W\in\mathbb R}\sum_{j=0}^1
\bigl[(d_jX+h_ju)^2+(b_jW+h_jv)^2\bigr].
\]
Orthogonal projection onto the two one-dimensional directions yields \(C_Ru^2+C_Iv^2\) with exactly the determinants above. Since both coefficients are strictly positive, the uniform little-oh remainder implies \(A(c)>0\) for all sufficiently small nonzero \(c\). At \(c=0\) the common Zak zero forces \(A(0)=0\). This proves every assertion.

## Verification
The standalone `CHECK.py` evaluates the hyperbolic constants, compares independent periodized lattice sums and spatial/frequency derivatives, and tests the predicted quadratic minimum at small real and imaginary perturbations. On execution it prints `CHECK_OK`. Truncation and numerical agreement are consistency checks; the rigorous proof is the Zak zero certificate, local derivative formulas, compactness, and two-dimensional orthogonal projection. Finite tests do not establish the infinite-frame assertion.

## Relationship to prior work
Ghosh [1] gives a rational-density frame analysis for the original odd rational window, rather than the local complex numerator perturbation considered here. The parity obstruction in Lyubarskii and Nes [2] implies that the unperturbed odd window cannot generate a frame at half density, but does not determine either sharp recovery coefficient. The known two-frequency-coset result [3] classifies non-integer *frequency-offset* perturbations of the fixed odd window and finds the sharp offset-loss coefficient; it does not perturb the window or determine the two distinct real/imaginary numerator coefficients. A recent exact Gaussian–first-Hermite mixture calculation [4] likewise studies sharp phase anisotropy, but its Gaussian profile and theta-series coefficient formulas do not determine the present rational-window constants. The use of Zak fibers and least-squares quadratic minimization is classical; the contribution claimed here is this concrete rational-window theorem with its two sharp positive coefficients and their strong directional separation.

## Limitations
No exact lower frame bound is claimed for arbitrary \(c\), and no global frame classification away from \(c=0\) is established. This theorem pertains only to unit integer translations and half-integer modulations. The two decimal values are evaluations of exact formulas, not independent certifications. Older equivalent perturbation results might exist under nonharmonic sampling or rational Zak terminology; publication priority is provisional. No independent scientific audit has been performed.

## References
1. R. Ghosh, *Gabor Frames for Rational Windows with Symmetric Poles*, arXiv:2608.10568v1, first public August 11, 2026, https://arxiv.org/abs/2608.10568.
2. Y. Lyubarskii and P. Gråberg Nes, *Gabor frames with rational density*, arXiv:1108.2684v1 (2011), https://arxiv.org/abs/1108.2684.
3. *Two-coset Gabor frame classification and sharp half-shift instability for an odd rational window*, published October 26, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-two-coset-gabor-frame-classification-and-sharp-half-shift-instab--4b04938a33b6.
4. *Phase-anisotropic sharp recovery of a singular Hermite Gabor frame*, published November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-phase-anisotropic-sharp-recovery-of-a-singular-hermite-gabor-fra--127b6b75a1f5.
