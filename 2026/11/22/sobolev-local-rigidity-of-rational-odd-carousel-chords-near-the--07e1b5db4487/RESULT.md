# Sobolev local rigidity of rational odd-carousel chords near the circle

## Finding

Fix coprime integers \(1\le p<q\) with **odd \(q\ge7\)** and a real Sobolev exponent \(s>3/2\). Write \(h=2\pi p/q\), and use the \(2\pi\)-periodic real Sobolev spaces \(H^s(\mathbb T)\). There exist \(\varepsilon_{p,q,s}>0\) and \(C_{p,q,s}<\infty\) with the following property.

Let \(\gamma:\mathbb T\to\mathbb C\cong\mathbb R^2\) be a positively oriented, closed, unit-speed, strictly convex curve of perimeter \(2\pi\) whose tangent has the form
\[
\gamma'(t)=e^{i(t+\psi(t))},\quad \psi\in H^s(\mathbb T;\mathbb R),\quad
\int_0^{2\pi}\psi(t)\,dt=0,\quad \|\psi\|_{H^s}<\varepsilon_{p,q,s}.
\]
The mean-zero condition merely chooses an ambient rotation. Set
\[
F_\psi(t)=|\gamma(t+h)-\gamma(t)|^2,\qquad
\overline F_\psi=(2\pi)^{-1}\int_0^{2\pi}F_\psi(t)\,dt.
\]
Then
\[
\boxed{\|\psi\|_{H^s}\le C_{p,q,s}\,\|F_\psi-\overline F_\psi\|_{H^{s+1}}.}
\]
In particular, every sufficiently \(H^s\)-near-circular closed strictly convex curve whose \(p/q\)-perimeter-separating chords all have the same length is a circle. The inverse Sobolev estimate has **exactly one derivative of loss**: for every \(\beta<1\), no corresponding uniform estimate with \(H^{s+\beta}\) on the right can hold on all sufficiently small closed curves. The qualitative and quantitative statements hold simultaneously for **every** coprime numerator and odd denominator \(q\ge7\), with constants permitted to depend on them. This does not assert global rigidity away from circles.

## Assumptions and scope

Use the norm \(\|f\|_{H^u}^2=\sum_{m\in\mathbb Z}(1+m^2)^u|\widehat f(m)|^2\) with \(\widehat f(m)=(2\pi)^{-1}\int_0^{2\pi}f(t)e^{-imt}\,dt\). A positively oriented unit-speed curve close to the unit circle has a tangent lift \(t+\psi(t)\). A common constant rotation of all tangent directions changes \(\psi\) by a constant; hence its mean can be set to zero. The curve is closed exactly when \(\int_0^{2\pi}e^{it+i\psi(t)}\,dt=0\). Since \(s>3/2\) entails a continuous first derivative, sufficiently small \(\psi\) has \(1+\psi'>0\), thus defines strictly positive curvature and a strictly convex embedded boundary whenever the closure equation holds. All statements concern *perimetral* chord separation, not physical fluid density.

## Proof

**1. Exact nonlinear map and its linearization.** For a closed unit-speed curve the chord depends only on its tangent. Put \(\delta=\pi p/q\), define
\[
Z_\psi(t)=\int_0^{2\delta}e^{iu+i\psi(t+u)}\,du,
\quad F_\psi=|Z_\psi|^2,
\quad Z_0=2e^{i\delta}\sin\delta.
\]
The factor \(e^{it}\) in the original chord drops out of its squared modulus. For a real variation \(\eta\),
\[
DZ_0[\eta](t)=i\int_0^{2\delta}e^{iu}\eta(t+u)\,du,
\quad DF_0[\eta]=2\operatorname{Re}(\overline{Z_0}DZ_0[\eta]).
\]
The Fourier multiplier of this real-linear derivative at any \(|m|\ge2\) is
\[
B_m=\frac{8i\sin\delta\ e^{im\delta}}{m^2-1}
\bigl(m\sin\delta\cos(m\delta)-\cos\delta\sin(m\delta)\bigr).
\tag{1}
\]
Indeed the integral applied to \(e^{imt}\) is
\(e^{imt}2e^{i(m+1)\delta}\sin((m+1)\delta)/(m+1)\);
combining the contribution of \(\eta\) and its complex conjugate gives (1). It satisfies \(B_{-m}=\overline{B_m}\), as required on real functions.

**2. No resonance at odd rational separations.** The denominator \(q\) is odd, so \(\cos(m\delta)\ne0\) for all integers \(m\). Suppose for contradiction that \(B_m=0\) for some integer \(m\ge2\). By (1),
\[
\tan(m\delta)=m\tan\delta.
\tag{2}
\]
Let \(\zeta=e^{2\pi ip/q}\), a primitive \(q\)-th root of unity, and \(Q=q/\gcd(q,m)\). Equation (2) becomes
\[
\frac{\zeta^m-1}{\zeta^m+1}
=m\frac{\zeta-1}{\zeta+1}.
\tag{3}
\]
If \(Q=1\), the left side vanishes and the right is nonzero. Otherwise take the algebraic norm from \(\mathbb Q(\zeta)\) to \(\mathbb Q\). Since odd cyclotomic orders greater than one satisfy \(\Phi_j(-1)=1\), equation (3) implies
\[
m^{\varphi(q)}=\frac{\Phi_Q(1)^{\varphi(q)/\varphi(Q)}}{\Phi_q(1)}.
\tag{4}
\]
For each odd \(j>1\), \(\Phi_j(1)=1\) unless \(j\) is a power of an odd prime \(r\), when \(\Phi_j(1)=r\). Consequently the right-hand side of (4) is at most \(3^{\varphi(q)/2}\): indeed \(\Phi_Q(1)^{1/\varphi(Q)}\le\sqrt3\), while \(\Phi_q(1)\ge1\). Thus \(m\le\sqrt3<2\), a contradiction. Therefore every \(B_m\) with \(|m|\ge2\) is nonzero.

**3. Ellipticity of order minus one.** Since \(q\) is odd and \(p,q\) are coprime, the finite residue set gives
\[
|\cos(m\delta)|\ge\sin\frac{\pi}{2q}>0\quad(m\in\mathbb Z).
\]
Using (1) and the triangle inequality, for all sufficiently large \(|m|\),
\[
|m\sin\delta\cos(m\delta)-\cos\delta\sin(m\delta)|
\ge |m|\sin\delta\sin\frac{\pi}{2q}-|\cos\delta|.
\]
This gives \(|B_m|\ge c_{p,q}/(1+|m|)\) at high frequency, and the finitely many lower frequencies have a positive minimum by Step 2. Formula (1) also gives \(|B_m|\le C_{p,q}/(1+|m|)\). Hence
\[
\frac{c_{p,q}}{1+|m|}\le|B_m|\le\frac{C_{p,q}}{1+|m|}
\qquad(|m|\ge2).
\tag{5}
\]
Writing \(X_s=\{f\in H^s(\mathbb T;\mathbb R):\widehat f(0)=\widehat f(\pm1)=0\}\), the derivative \(\Pi_{\ge2}DF_0:X_s\to X_{s+1}\) is thus a bounded real Banach-space isomorphism, with inverse given coefficientwise by \(1/B_m\). Here \(\Pi_{\ge2}\) deletes Fourier modes \(0,\pm1\).

**4. The closure constraint and nonlinear inverse estimate.** The closure map
\[
\mathcal C(\psi)=\int_0^{2\pi}e^{it+i\psi(t)}\,dt\in\mathbb C
\]
is analytic from \(H^s\) near zero into \(\mathbb C\); \(D\mathcal C_0[\eta]=i\int e^{it}\eta(t)dt\) is a real isomorphism on the two-dimensional \(\{\cos t,\sin t\}\) space. By the analytic implicit-function theorem, all sufficiently small closed mean-zero \(\psi\) are uniquely written \(\psi=v+\Lambda(v)\), with \(v\in X_s\), \(\Lambda(v)\in\operatorname{span}_{\mathbb R}\{\cos t,\sin t\}\), and \(\Lambda(0)=0\), \(D\Lambda(0)=0\). The vanishing derivative follows because the closure derivative annihilates \(X_s\).

The map \(\psi\mapsto Z_\psi\) is analytic \(H^s\to H^{s+1}\): the exponential is analytic in the Sobolev algebra \(H^s\), while the integral operator \(f\mapsto\int_0^{2\delta}e^{iu}f(t+u)du\) has Fourier multipliers \(O((1+|m|)^{-1})\), including the one exceptional index \(m=-1\). Since products are continuous in \(H^{s+1}\), \(\psi\mapsto F_\psi\) is analytic \(H^s\to H^{s+1}\). Consequently
\[
\mathcal G(v)=\Pi_{\ge2}\big(F_{v+\Lambda(v)}-\overline F_{v+\Lambda(v)}\big)
\]
is analytic \(X_s\to X_{s+1}\), with derivative \(D\mathcal G(0)=\Pi_{\ge2}DF_0|_{X_s}\), the isomorphism from Step 3. The inverse-function theorem yields a neighborhood and constant \(C\) with \(\|v\|_{H^s}\le C\|\mathcal G(v)\|_{H^{s+1}}\). As \(\Lambda(v)=O(\|v\|_{H^s}^2)\), shrinking the neighborhood gives \(\|\psi\|_{H^s}\le2C\|\mathcal G(v)\|_{H^{s+1}}\), and the desired estimate follows from boundedness of the projection. If the chord length is constant, the right side is zero, so \(\psi=0\); integrating \(\gamma'(t)=e^{it}\) gives a unit circle up to translation.

**5. The derivative loss is sharp.** Take real \(v_m(t)=\cos(mt)\) with integers \(m\) divisible by \(q\) and tending to infinity. Then \(\cos(m\delta)=\pm1\) and \(\sin(m\delta)=0\), so (1) yields \(|B_m|=8\sin^2\delta\,m/(m^2-1)\), asymptotic to \(8\sin^2\delta/m\). If a uniform nonlinear estimate with \(H^{s+\beta}\), \(\beta<1\), replaced \(H^{s+1}\), applying it to the closed curves generated by \(tv_m+\Lambda(tv_m)\) and differentiating at \(t=0\) would require \(\|v_m\|_{H^s}\le C\|DF_0v_m\|_{H^{s+\beta}}\), uniformly in \(m\). The ratio of right to left is \(O(m^{\beta-1})\to0\), impossible. This proves sharpness without asserting global rigidity.

## Verification

The standalone `checker.py` reproduces the multiplier (1) independently by centered finite differences of direct numerical chord integrals for seven rational shifts. It also checks nonzero multiplier bounds over 394,000 finite parameter-frequency cases and compares the integer Galois-norm relation at many odd orders. These are error-detection checks; the all-denominator, all-frequency assertion comes from the cyclotomic norm argument and the local nonlinear theorem comes from the two Banach-space inverse theorems, not exhaustive computation. Run `python3 checker.py` (Python standard library only). The result is stable under the rotation gauge and requires closure; omitting closure would reintroduce the two translation-related tangent modes.

## Relationship to prior work

Asipchuk–Kosmakov (2026, arXiv:2611.18381v1) proves **global** strict-convexity rigidity for perimetral densities \(1/5\) and \(2/5\), using five-carousel Fourier identities. Bracho–Montejano–Oliveros (2004) credits analogous global small-denominator facts. The theorem here excludes those covered odd denominators and establishes a **local quantitative** assertion simultaneously for every odd \(q\ge7\), including the presently open \(1/7\) family, using the spectrum of the squared fixed-arclength chord operator rather than finite-carousel inequalities. Bor–Levi–Perline–Tabachnikov (2018), Theorem 10, constructs Zindler families with special rotation numbers satisfying a related tangent-resonance equation, but neither supplies the odd-rational Sobolev inverse estimate nor implies this local theorem. The even-denominator and half-perimeter settings are different; the conclusion explicitly does not extend to them. Negative novelty searches are not a uniqueness certification; unindexed historical treatments of local Zindler bifurcations remain a residual priority risk.

## Limitations

The theorem requires a fixed rational perimetral separation with odd denominator at least seven, a closed strictly convex near-circle curve, and Sobolev smallness of its tangent angle. The constants are not uniform as \(q\to\infty\). It does not classify non-near-circular solutions, physical density, finite smoothness below \(s>3/2\), or irrational/even-denominator separations. The exact numerical values of \(C_{p,q,s}\) and \(\varepsilon_{p,q,s}\) are not supplied. No independent external audit has been carried out.

## References

- O. Asipchuk and M. Kosmakov, *Fourier Harmonics and Pentagonal Rigidity in the Planar Ulam Floating Body Problem*, arXiv:2611.18381v1, first posted November 13, 2026. https://arxiv.org/abs/2611.18381
- J. Bracho, L. Montejano, and D. Oliveros, *Carousels, Zindler curves and the floating body problem*, Periodica Mathematica Hungarica 49 (2004), 9–23. https://www.matem.unam.mx/~luis/pdfs/volantin1.pdf
- G. Bor, M. Levi, R. Perline and S. Tabachnikov, *Tire Tracks and Integrable Curve Evolution*, International Mathematics Research Notices (2018), Theorem 10. https://www.marklevimath.com/_files/ugd/4d55eb_43c72811f87f4a01b31facab8b37d5ab.pdf
- O. Asipchuk, M. Kosmakov, and P. Zatitskii, *Rigidity in the Planar Ulam Floating Body Problem with Perimetral Density \(\sigma=1/6\)*, arXiv:2604.10330. https://arxiv.org/abs/2604.10330
- Y. Martinez-Maure and D. Rochera, *Fractal solutions to the two-dimensional floating body problem*, arXiv:2611.11309, 2026. https://arxiv.org/abs/2611.11309
