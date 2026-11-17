# Rigorous supercritical onset of stable two-cluster oscillations in a delayed eight-market network

## Finding

For the eight-node cube-coupled, finite-window memory system defined below, the first loss of stability of zero is a simple supercritical Hopf bifurcation in its alternating parity mode. Its unique crossing parameter and angular frequency satisfy
\[
0.0952971135<\alpha_*<0.0952971226,\qquad
0.0923907340<\omega_*<0.0923907345.
\]
For all sufficiently small \(\alpha-\alpha_*>0\) there exists a branch of **orbitally asymptotically stable periodic solutions in the full eight-component delay phase space**, with two precisely opposite groups of four nodes. Every sufficiently small periodic orbit near zero is, up to time translation, on this branch. With parity signs \(s_i\in\{1,-1\}\), each component obeys
\[
x_i(t)=s_i\left[B\sqrt{\alpha-\alpha_*}\cos(\Omega(\alpha)t+\varphi)+O(\alpha-\alpha_*)\right],
\qquad 3.87622<B<3.87624.
\]
Here \(\Omega(\alpha)=\omega_*+O(\alpha-\alpha_*)\) is the actual nonlinear orbit frequency. The local characteristic root has positive crossing speed \(0.04596360<\operatorname{Re}\lambda'(\alpha_*)<0.04596366\), whereas the cubic complex-amplitude coefficient has strictly negative real part,
\[
-0.01223645<\operatorname{Re}c<-0.01223642.
\]
These signed, rigorous numerical bounds apply to the exact rational parameter choices below. The periodic attractor is asserted only for a sufficiently small one-sided parameter neighborhood, not for every distant parameter.

## Assumptions and scope

Identify the eight nodes with \(\{0,1\}^3\). Put \(c_1=3/20\), \(c_2=1/20\), \(c_3=1/100\), and set \(C_{ij}=c_d\) when distinct vertices \(i,j\) have Hamming distance \(d\); set \(C_{ii}=0\). For \(\alpha\ge0\), consider the autonomous retarded functional differential equation on continuous histories of length 60,
\[
\dot x_i(t)=\frac1{25}[x_i(t)-x_i(t-20)]-\frac12x_i(t)
-\alpha\tanh\!\left(\frac15\int_{t-60}^{t}x_i(v)\,dv\right)
-\tanh\!\left(\sum_j C_{ij}x_j(t)\right).
\]
The source calls this a finite-window pseudoneutral market model; here it is explicitly interpreted as a retarded equation. Define \(s_i=(-1)^{i_1+i_2+i_3}\). A local periodic orbit is orbitally asymptotically stable when it attracts all sufficiently close compatible continuous histories modulo phase. No stochastic or economic interpretation is used as a mathematical premise.

## Proof

**1. Exact spatial decomposition.** Walsh characters of the three-cube diagonalize the Hamming-distance coupling matrix. Its four eigenvalues are \(61/100,9/100,-19/100,-31/100\), with multiplicities \(1,3,3,1\). Hence the four effective instantaneous linear coefficients \(a_j=1/2+\mu_j\), in increasing order, are
\[
\{a_j\}=\{19/100,31/100,59/100,111/100\}.
\]
The least coefficient is simple, with eigenvector \(s\). Since odd scalar functions preserve this parity line, \(x_i=s_i u\) is an exactly invariant nonlinear subspace, and on it
\[
\dot u=\frac1{25}(u-u_{20})-\frac12u
-\alpha\tanh\!\left(\frac15\int_{t-60}^t u(v)\,dv\right)
-\tanh(-\tfrac{31}{100}u),
\]
where \(u_{20}=u(t-20)\). This equality is an identity of the original eight equations, not an approximate modal truncation.

**2. Exhaustive enumeration of all possible first imaginary crossings.** For an effective coefficient \(a_j\), the characteristic factor is the entire function
\[
\Delta_j(\alpha,z)=z+a_j-\tfrac1{25}(1-e^{-20z})
+\frac\alpha5 H(z),\qquad
H(z)=\int_0^{60}e^{-zv}\,dv.
\]
It is important that \(H(0)=60\), so there is no spurious zero characteristic root. If \(z=i\omega\), \(\omega>0\), write \(\theta=20\omega\). The imaginary equation gives, whenever \(1-\cos(3\theta)\ne0\),
\[
\alpha=\mathcal A(\theta):=
\frac{\theta[\theta-(4/5)\sin\theta]}{80[1-\cos(3\theta)]}.
\]
The case \(1-\cos(3\theta)=0\) is impossible because \(\omega-(1/25)\sin(20\omega)>0\) for \(\omega>0\). Eliminating \(\alpha\) from the real equation yields
\[
Q_j(\theta):=[100a_j-4+4\cos\theta]\sin(3\theta/2)
+[5\theta-4\sin\theta]\cos(3\theta/2)=0.
\]
Any imaginary crossing for \(0\le\alpha\le0.0953\) must obey
\[
\omega^2\le\tfrac1{25}\omega+\tfrac{2\alpha}{5},
\]
whence \(0<\theta<4.34<5\pi/3\). This bounds *all* possible frequencies, not just those tested numerically.

Put \(A_j(\theta)=100a_j-4+4\cos\theta\) and \(B(\theta)=5\theta-4\sin\theta\). Both are strictly positive for \(\theta>0\). In \(0<\theta<5\pi/3\), the signs of the sine and cosine factors show that a root of \(Q_j\) can occur only in \((\pi/3,2\pi/3)\) or \((\pi,4\pi/3)\). On either interval it solves
\[
\tan(3\theta/2)+B(\theta)/A_j(\theta)=0.
\]
The tangent is strictly increasing from \(-\infty\) to zero. Moreover, putting \(K=100a_j-4\ge15\),
\[
B'A_j-BA_j'=5K-16+(20-4K)\cos\theta+20\theta\sin\theta>0.
\]
For \(\theta\in(\pi/3,2\pi/3)\) this follows directly from \(\sin\theta>0\) and \(\cos\theta\le1\); for \(\theta\in(\pi,4\pi/3)\) it follows from the lower bound \(7K-26-40\pi\sqrt3/3>0\). Thus there is exactly one root in each of these two intervals. Increasing \(a_j\) decreases \(B/A_j\), so each root moves strictly right. On both intervals \(\mathcal A(\theta)\) increases strictly because its numerator is positive and strictly increasing and its denominator positive and decreasing. Therefore, among *all* the four spectral factors, the first and second possible center parameters are bounded below by the corresponding two roots for the smallest coefficient \(a_j=19/100\).

For that coefficient the center equation is
\[
Q(\theta)=(15+4\cos\theta)\sin(3\theta/2)
+(5\theta-4\sin\theta)\cos(3\theta/2)=0.
\]
Exact interval evaluation encloses its first root in \((1.84781468,1.84781469)\) and its second in \((3.49962992,3.49962994)\). The respective parameters obey
\[
0.0952971135<\mathcal A(\theta_1)<0.0952971226
<0.1119912731<\mathcal A(\theta_2)<0.1119912789.
\]
Thus \(\alpha_*=\mathcal A(\theta_1)\) is the **first center across every spatial mode and every positive frequency**. At \(\alpha=0\) there are no right-half-plane roots: for \(\operatorname{Re}z\ge0\), \(\operatorname{Re}\Delta_j(0,z)\ge \operatorname{Re}z+a_j-2/25>0\). Roots cannot enter the right half-plane from infinity over a bounded parameter interval, as the nonnegative-real-part root bound \(|z|\le a_j+2/25+12\alpha\) shows. Therefore all characteristic roots have negative real part below \(\alpha_*\), and at the critical point the only imaginary roots are the simple pair \(\pm i\omega_*\).

**3. Explicit cubic Hopf coefficient.** Define \(H_*:=H(i\omega_*)\), \(D_*:=\partial_z\Delta_1(\alpha_*,i\omega_*)\). Implicit differentiation yields
\[
\lambda'(\alpha_*)=-\frac{H_*}{5D_*}.
\]
Expansion of both odd hyperbolic tangents in the exact parity-line equation yields a cubic nonlinearity
\[
\frac{\alpha_*}{375}\left(\int_{t-60}^t u(v)\,dv\right)^3
+\frac{(-31/100)^3}{3}u^3.
\]
There is no quadratic term. For \(u(t)=A(t)e^{i\omega_*t}+\overline{A(t)}e^{-i\omega_*t}+O(|A|^3)\), the fundamental Fourier component of the cubic terms is \(\{\alpha_* (1/5)^3H_*|H_*|^2+(-31/100)^3\}|A|^2 A\). Expansion of the retarded linear operator on a slowly varying fundamental amplitude produces the factor \(D_*\), giving the standard scalar Hopf normal form in this explicitly specified complex-amplitude normalization,
\[
\dot A=\lambda'(\alpha_*)(\alpha-\alpha_*)A+c|A|^2A
+O(|A|^5+|\alpha-\alpha_*||A|^3+|\alpha-\alpha_*|^2|A|),
\quad c=\frac{\alpha_*(1/5)^3H_*|H_*|^2+(-31/100)^3}{D_*}.
\]
The third harmonic is nonresonant by Step 2, so the expansion is legitimate. Outward-rounded interval evaluation on the root bracket gives
\[
0.04596360<\operatorname{Re}\lambda'(\alpha_*)<0.04596366,
\qquad -0.01223645<\operatorname{Re}c<-0.01223642.
\]
All strict signs and root brackets are reproduced by `VERIFY.py`. Hence the first Hopf is nondegenerate and **supercritical**, with a stable radial amplitude \(|A|=\sqrt{-\operatorname{Re}\lambda'/\operatorname{Re}c}\sqrt{\alpha-\alpha_*}+O((\alpha-\alpha_*)^{3/2})\); the physical cosine coefficient is \(2\sqrt{-\operatorname{Re}\lambda'/\operatorname{Re}c}\), enclosed between 3.87622 and 3.87624.

**4. Stability in the full history space.** All noncritical spatial factors are strictly stable at \(\alpha_*\) by Step 2. Normal hyperbolicity and spectral continuity persist under sufficiently small amplitude changes of the periodic state. The center-manifold Hopf theorem for retarded equations, with \(\operatorname{Re}c<0\) and \(\operatorname{Re}\lambda'>0\), gives a radially attracting periodic orbit. Its sole neutral multiplier corresponds to time translation; all remaining multipliers lie inside the unit circle. It is therefore orbitally asymptotically stable in \(C([-60,0],\mathbb R^8)\), not merely inside the invariant parity line. Local uniqueness follows from the simple Hopf pair and the local center manifold. 

## Verification

Run `python VERIFY.py` after installing `mpmath==1.3.0`. The checker computes four strict interval signs of \(Q\), enclosures of the two center parameters, the real parts of the characteristic-root crossing speed and cubic normal-form coefficient, and the physical cosine coefficient. It also exactly checks the four Walsh-mode eigenvalues as rational numbers. The analytic argument proves that the checked roots exhaust all potential first crossings; the interval checker alone is not a root-exhaustiveness proof. The numerical root brackets have width \(10^{-8}\) or \(2\times10^{-8}\), far smaller than the sign margins.

## Relationship to prior work

Crane's pseudoneutral-memory study, arXiv:2604.20740v2 (Section 6), supplies this exact eight-market model, identifies the approximate first center in its one-dimensional antisymmetric mode, and reports numerical Floquet stability of sampled two-cluster cycles. Its global equivariant-degree theorem proves existence of bifurcating solutions but does **not** prove their local orbital attraction or calculate a first Lyapunov coefficient. The present contribution is the exhaustive analytic proof that this center is the first across all delay frequencies and spatial modes, the signed nonlinear cubic normal form, and the full-phase-space supercritical stability theorem with a sharp leading oscillation amplitude. The source's numerical frequency/threshold and observed stable cycles are not presented as new. Chen--Crane--Hensley (2026) treats global symmetric Hopf bifurcation for a related but different distributed-delay network; general retarded Hopf and center-manifold theory, including cubic coefficient calculations, is classical. The particular specialized coefficient and exact first-crossing ordering here are not asserted to create a new normal-form method.

## Limitations

The result is local near the first center and is specific to the rational parameters and the cube coupling of the cited example. It does not certify stability at the larger sample offsets in the source, exclude remote periodic solutions, or prove global attraction or long-term financial predictions. The interval calculations check concrete transcendental signs, while strict monotonicity and characteristic-root completeness require the separate analytic steps above. Earlier literature may contain equivalent specialized computations; historical priority is provisional, particularly because the related 2026 dissertation could not be examined in full. No independent mathematical audit has been performed.

## References

1. C. Crane, *Global Hopf bifurcation and symmetric periodic solutions in multi-agent systems with pseudoneutral memory*, arXiv:2604.20740v2 (2026-10-30), first preprint 2026-04-22. https://arxiv.org/html/2604.20740v2
2. C. M. Crane, *Consensus-breaking global Hopf bifurcation in memory-based multi-agent systems*, arXiv:2607.02388 (2026-07-02), related dissertation; abstract consulted, full dissertation inaccessible. https://arxiv.org/abs/2607.02388
3. C. Chen, C. Crane and T. Hensley, *Global Hopf bifurcation in symmetric configurations of distributed delay differential equations*, Communications on Pure and Applied Analysis 27 (2026), 170–194. https://doi.org/10.3934/cpaa.2025118
4. J. K. Hale and S. M. Verduyn Lunel, *Introduction to Functional Differential Equations*, Springer, 1993 (retarded spectral/center-manifold theory).
