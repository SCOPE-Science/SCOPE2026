# Sharp fourth moments of the three consecutive centered real Fourier harmonics

## Finding

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with normalized Haar measure \(dt/(2\pi)\), and let
\[
\mathcal H=\left\{f(t)=\operatorname{Re}\!\left(Ue^{it}+Ve^{2it}+We^{3it}\right):U,V,W\in\mathbb C\right\}\subset L^4(\mathbb T;\mathbb R).
\]
For \(f\ne0\), write \(K(f)=\|f\|_4^4/\|f\|_2^4\). Define \(r_-\) as the unique zero in \((1/4,3/10)\) of
\[
3r^3-3r^2-3r+1=0,
\]
and \(r_+\) as the unique positive zero of
\[
3r^3+6r^2-3r-4=0.
\]
Then the complete, **sharp** fourth-moment range is
\[
\boxed{\quad
\kappa_-:=\frac{\frac32(1+r_-^4)+6r_-^2-2r_-}{(1+r_-^2)^2}
\le K(f)\le
\kappa_+:=\frac{9+12r_+^2+\frac32r_+^4+8r_+}{(2+r_+^2)^2}.
\quad}
\]
Numerically, \(\kappa_-=1.220691895037155\ldots\) and \(\kappa_+=3.408011581218152\ldots\). Equivalently, the endpoints are the specified real roots of
\[
208x^3-1224x^2+2268x-1323=0,
\qquad
3344x^3-22644x^2+47736x-32049=0,
\]
respectively; each must be selected using its above interval, since the polynomials can have other roots.

The lower equality family is **exactly**
\[
f(t)=A\bigl[\cos(t-\theta)-r_-\cos(3(t-\theta))\bigr],
\quad A\in\mathbb R\setminus\{0\},\quad\theta\in\mathbb R.
\]
The upper equality family is **exactly**
\[
f(t)=A\bigl[\cos(t-\theta)+\varepsilon\cos(2(t-\theta))+r_+\cos(3(t-\theta))\bigr],
\quad A\in\mathbb R\setminus\{0\},\quad\theta\in\mathbb R,\quad\varepsilon\in\{1,-1\}.
\]
All intermediate values occur. In particular, adding the second harmonic cannot improve the sharp lower fourth moment of the first/third-harmonic subspace, while it is essential at the upper endpoint.

## Assumptions and scope

All functions and norms are real-valued, the measure is normalized uniform Haar measure on the continuous circle, and all three first positive harmonics with arbitrary real sine/cosine coefficients are permitted. The coefficients \(U,V,W\) are otherwise unrestricted complex Fourier-coordinate parameters, and \(f\ne0\). The claim concerns the **fourth power** of the \(L^4/L^2\) ratio; the actual norm constants are its fourth roots. No discrete sampling or finite cyclic aliasing is asserted.

For \(a=|U|\), \(b=|V|\), \(c=|W|\), put \(S=a^2+b^2+c^2\). Orthogonality gives \(\|f\|_2^2=S/2\). Direct zero-sum Fourier expansion gives the exact polynomial identity
\[
S^2K(f)=\frac32(a^4+b^4+c^4)+6(a^2b^2+a^2c^2+b^2c^2)
+2\operatorname{Re}(U^3\overline W)
+6\operatorname{Re}(UW\overline V^{\,2}). \tag{1}
\]
The two last terms are the distinct fourth-order additive resonances \(1+1+1=3\) and \(1+3=2+2\). Their phases can be made simultaneously positive or simultaneously negative by suitable choices of Fourier coefficient phases.

## Proof

**1. Phase reduction.** By \(\operatorname{Re}(z)\in[-|z|,|z|]\), for any prescribed magnitudes \(a,b,c\), expression (1) lies between
\[
N_-(a,b,c)=\frac32(a^4+b^4+c^4)+6(a^2b^2+a^2c^2+b^2c^2)-2a^3c-6ab^2c
\]
and the same expression \(N_+(a,b,c)\) with the last two signs positive. These are simultaneously attainable for every \(a,b,c\ge0\): take the phase of \(U\) to be zero, the phase of \(V\) to be zero, and the phase of \(W\) to be respectively \(\pi\) or zero. Thus it suffices to optimize \(N_-/S^2\) and \(N_+/S^2\) over nonnegative magnitudes.

**2. Reduction of the minimum to two harmonics.** Let \(t_0=a^2+c^2\) and \(y=b^2\). For \(t_0>0\), define \(K_2(a,c)\) to be the normalized lower-phase fourth moment with only the first and third harmonics:
\[
K_2(a,c)=\frac{\frac32(a^4+c^4)+6a^2c^2-2a^3c}{(a^2+c^2)^2}.
\]
There is the exact decomposition
\[
N_-(a,b,c)=t_0^2K_2(a,c)+\frac32y^2+(6t_0-6ac)y.\tag{2}
\]
Since \(2ac\le t_0\), the last coefficient obeys \(6t_0-6ac\ge3t_0\). Put \(m=\min_{a,c\ge0,\ a^2+c^2>0} K_2(a,c)\); we shall prove \(m<3/2\). Consequently
\[
N_- -m(t_0+y)^2
\ge \left(\frac32-m\right)y^2+(3-2m)t_0y\ge0.
\]
For \(t_0=0\), the only nonzero harmonic is the second and \(K=3/2>m\). Equality in the full lower bound forces \(y=b^2=0\), because both displayed coefficients are strictly positive.

For \(a>0\), set \(r=c/a\). The remaining one-variable function is
\[
F_-(r)=\frac{\frac32(1+r^4)+6r^2-2r}{(1+r^2)^2},\qquad
F_-'(r)=-\frac{2(3r^3-3r^2-3r+1)}{(1+r^2)^3}.\tag{3}
\]
The cubic numerator decreases strictly on \((0,1)\), increases strictly on \((1,\infty)\), has one zero \(r_-\in(1/4,3/10)\), and has one further zero between 1 and 2. Hence \(F_-\) decreases, then increases, then decreases. Since \(F_-(0)=\lim_{r\to\infty}F_-(r)=3/2\) and \(F_-'(0)<0\), its unique global minimum is \(F_-(r_-)<3/2\). Equality requires \(c/a=r_-\), \(b=0\), and \(\operatorname{Re}(U^3\overline W)=-a^3c\); this is exactly the lower stated family after rotation and real scaling.

**3. Symmetrization for the maximum.** Fix \(s=a^2+b^2\) and \(c\). The positively phase-aligned expression can be written
\[
N_+(a,b,c)=\frac32(s+c^2)^2+3a^2b^2+3sc^2+2c\,a(3s-2a^2).\tag{4}
\]
Here \(a^2b^2\le s^2/4\), with equality if and only if \(a=b\). Independently, on \(0\le a\le\sqrt s\), the cubic \(a(3s-2a^2)\) has its unique maximum at \(a=\sqrt{s/2}\), also equivalent to \(a=b\). A particularly explicit deficit identity, for \(s>0\) and \(v=a/\sqrt{s/2}\), is
\[
\sqrt2\,s^{3/2}-a(3s-2a^2)=\frac{s^{3/2}}{\sqrt2}(v-1)^2(v+2)\ge0.\tag{5}
\]
Thus the maximizer must satisfy \(a=b\) (including the cases where one of these is zero by continuity). With \(a=b>0\), put \(r=c/a\); then
\[
F_+(r)=\frac{9+12r^2+\frac32r^4+8r}{(2+r^2)^2},\qquad
F_+'(r)=-\frac{4(3r^3+6r^2-3r-4)}{(2+r^2)^3}.\tag{6}
\]
The derivative cubic first decreases and then strictly increases on \([0,\infty)\); it is negative at zero and positive at one. Therefore it has exactly one positive root \(r_+\in(4/5,9/10)\), at which \(F_+\) has its unique global maximum. The boundary values \(F_+(0)=9/4\) and \(\lim_{r\to\infty}F_+(r)=3/2\) are smaller. The cases \(a=b=0\) and \(c=0\) cannot attain this global maximum. Finally, positive equality in each resonance forces \(\arg W=3\arg U\pmod{2\pi}\) and \(\arg V=2\arg U\pmod\pi\), which gives precisely the stated upper family.

**4. Exact stability identities.** These also show equality rigidity without reliance on numerical optimization. Let
\[
\delta_1=a^3c-\operatorname{Re}(U^3\overline W),\qquad
\delta_2=ab^2c-\operatorname{Re}(UW\overline V^{\,2}),
\]
so both are nonnegative. With \(m=\kappa_-\), the exact lower deficit is
\[
\boxed{\ S^2(K(f)-m)=t_0^2(K_2(a,c)-m)
+\left(\frac32-m\right)y^2+igl[(6-2m)t_0-6ac\bigr]y+2\delta_1+6\delta_2.\ }\tag{7}
\]
If \(t_0=0\), the first term is defined to be zero. Every term on the right is nonnegative, since the bracket is at least \((3-2m)t_0\).

For the upper endpoint, let \(s=a^2+b^2\) and
\[
\mathcal U(s,c)=\frac94s^2+6sc^2+\frac32c^4+2\sqrt2\,s^{3/2}c.
\]
The exact upper deficit is
\[
\begin{aligned}
S^2(\kappa_+-K(f))={}&\bigl[\kappa_+S^2-\mathcal U(s,c)\bigr]
+\frac34(a^2-b^2)^2\\
&+2c\bigl[\sqrt2\,s^{3/2}-a(3s-2a^2)\bigr]+2\delta_1+6\delta_2.
\end{aligned}\tag{8}
\]
All terms are nonnegative by (5), (6), and the resonance phase inequalities. When \(s>0\), the first bracket equals \(S^2[\kappa_+-F_+(\sqrt2 c/\sqrt s)]\); at \(s=0\), it follows from \(F_+(\infty)=3/2\). The identity proves the asserted sharpness and rigidity.

**5. Every intermediate value.** The coefficient unit sphere in the six-dimensional real space \(\mathcal H\) is connected and the fourth-moment ratio is continuous on it. The two sharp endpoints therefore imply every intermediate value is attained.

## Verification

Run \(`python verify_fourier_triad.py`\) from the directory containing the embedded checker. It enumerates all zero-sum four-term Fourier combinations, independently integrates the real cosine polynomial symbolically, checks the two cubic derivative formulas and exact root counts, verifies algebraic symmetrization and endpoint resultants, and executes a reproducible finite sample of complex Fourier-coordinate cases. The exact symbolic checks support the proof; random tests are diagnostics only. Analytical inequalities (2), (5), (7), and (8), not finite experiments, establish the universal assertions.

## Relationship to prior work

The norm problem is a finite-frequency, real-valued sharp \(L^2\)-to-\(L^4\) inequality. Nursultanov–Ruzhansky–Tikhonov (2014) prove general Nikol'skii inequalities on compact Lie groups and discuss trigonometric polynomials, but the inspected full text gives general spectral-count estimates and a sharp \(L^2\)-to-\(L^\infty\) instance, not these exact six-dimensional \(L^4/L^2\) endpoints or their equality cases. Schmidt (2013) studies fourth moments of **analytic polynomials with unimodular coefficients**, using Fourier autocorrelations; his theorems concern large-degree asymptotics, not unrestricted real signed-frequency trigonometric polynomials. Related published exact complex-character results on three- and four-frequency one-sided spectra concern different Fourier-support sets and do not imply a sharp classification for the conjugate-symmetric support \(\{\pm1,\pm2,\pm3\}\). The lower endpoint agrees with the two-frequency first/third-harmonic minimum, but the new statement proves that it remains sharp after allowing the intermediate harmonic and determines the new upper endpoint and all six-dimensional equality cases.

## Limitations

The result is specific to normalized Haar measure on the continuous circle, the real mean-zero degree-at-most-three trigonometric subspace, and the exponent four. It does not cover general complex-valued functions, the constant Fourier mode, arbitrary higher degrees, other exponents, discrete cyclic sampling with possible aliasing, or a Banach–Mazur distance classification. The literature comparison cannot exclude an equivalent statement hidden in unindexed sources; independent mathematical assessment remains unperformed.

## References

1. E. Nursultanov, M. Ruzhansky, S. Tikhonov, *Nikolskii inequality and Besov, Triebel-Lizorkin, Wiener and Beurling spaces on compact homogeneous manifolds*, arXiv:1403.3430v1, first public 2014-03-13. https://arxiv.org/abs/1403.3430 . Full arXiv-rendered paper inspected, especially introduction, Theorems 3.1 and 4.2, and their proofs.
2. K.-U. Schmidt, *On a problem due to Littlewood concerning polynomials with unimodular coefficients*, arXiv:1302.2766v1, first public 2013-02-12. https://arxiv.org/html/1302.2766v1 . Full HTML paper inspected, especially the introduction, Theorems 1 and 2, and the autocorrelation identity in Section 2.
