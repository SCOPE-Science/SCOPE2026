# Exact Floquet instability staircase of the circular wave in a planar delay system

## Finding

Consider the planar nonlinear unit-delay equation, in complex form,
\[
\dot z(t)=-\alpha(1-|z(t)|^2)e^{i\theta}z(t-1),
\qquad 0<\theta<\pi/2,
\]
with real \(\alpha>0\). Put \(\beta=\pi/2-\theta\). For every \(\alpha>\beta\), the equation admits the circular periodic wave
\[
 z_\alpha(t)=R e^{-i\beta t},\qquad R=\sqrt{1-\beta/\alpha},\qquad T=2\pi/\beta.
\]
The complete orbital linear-instability staircase of this wave is explicit. Set
\[
 \alpha_j=\frac{(2j+1)^2\pi^2}{4\beta},\qquad j=0,1,2,\ldots.
\]
For \(\beta<\alpha<\alpha_0\), the wave is locally exponentially orbitally attracting. For \(\alpha_j<\alpha<\alpha_{j+1}\), its co-rotating linearization has exactly \(2(j+1)\) characteristic roots with positive real part, counting algebraic multiplicities, and the wave is orbitally unstable. At \(\alpha=\alpha_j\), there are exactly \(2j\) roots in the open right half-plane, a simple conjugate imaginary-axis pair \(\lambda=\pm i(2j+1)\pi\), and the single symmetry root \(\lambda=0\). All other roots lie in the open left half-plane. Each pair crosses from left to right with nonzero speed as \(\alpha\) increases. In particular the first sharp orbital linear-stability boundary is
\[
 \alpha_0=\frac{\pi^2}{4(\pi/2-\theta)}.
\]
This theorem concerns transverse Floquet spectra and local orbital stability, not the existence or nonlinear type of a secondary bifurcating branch.

## Assumptions and scope

The delay is exactly one time unit; the phase \(\theta\) is fixed in \((0,\pi/2)\); and \(\alpha>\beta=\pi/2-\theta\), so the circular wave has strictly positive radius. The history phase space is \(C([-1,0],\mathbb C)\), viewed as a real Banach space. Characteristic roots are those of the constant-coefficient linearized retarded equation after rotating by \(e^{-i\beta t}\). Multiplicities are algebraic; stability is modulo the phase-rotation symmetry. The same condition for negative \(\theta\) follows by complex conjugation, but the theorem is stated for strictly positive \(\theta\).

## Proof

**Exact rotating-frame linearization.** Write \(z(t)=e^{-i\beta t}(R+u(t))\) with \(u=x+iy\), \(x,y\) real. The two identities \(e^{i(\theta+\beta)}=i\) and \(\alpha(1-R^2)=\beta\) show that the wave solves the original equation. Keeping first-order terms gives
\[
 \dot u=i\beta[u(t)-u(t-1)]+i\alpha R^2[u(t)+\overline{u(t)}].
\]
Setting \(k=2\alpha R^2=2(\alpha-\beta)>0\), this is the real delay system
\[
 \dot x=-\beta[y(t)-y(t-1)],\qquad
 \dot y=\beta[x(t)-x(t-1)]+kx(t).
\]
Its characteristic determinant, with \(h(\lambda)=1-e^{-\lambda}\), is
\[
 F(\lambda;k)=\lambda^2+\beta^2 h(\lambda)^2+\beta k h(\lambda).
\]
The symmetry root \(\lambda=0\) is simple for \(k>0\), since \(F_\lambda(0;k)=\beta k>0\).

**Stable baseline.** At \(k=0\), the determinant factors as
\[
 F(\lambda;0)=[\lambda-i\beta h(\lambda)]
 [\lambda+i\beta h(\lambda)].
\]
For \(0<\beta<1\), the identity \(h(\lambda)=\lambda\int_0^1 e^{-s\lambda}\,ds\) excludes every nonzero root with \(\operatorname{Re}\lambda\ge0\), because the integral has modulus at most one. This property extends continuously throughout \(0<\beta<\pi/2\): an imaginary-axis root of either factor with \(\lambda=i\omega\ne0\) would have \(\sin\omega=0\) and \(|\omega|=2\beta\); the smallest nonzero odd multiple of \(\pi\) requires \(\beta\ge\pi/2\). Each factor's zero root is simple because its derivative there equals \(1\mp i\beta\). There can be no roots arriving from infinity in the closed right half-plane, since a root of either factor there satisfies \(|\lambda|\le2\beta\). Thus at \(k=0\) all roots other than a double zero have negative real part. For small \(k>0\), the double zero splits into the persistent simple root at zero and
\[
 \lambda_*(k)=-\frac{\beta}{1+\beta^2}k+O(k^2)<0.
\]
All other roots remain strictly in the left half-plane. Thus the wave is spectrally attracting, apart from symmetry, for sufficiently small positive \(k\).

**All imaginary crossings.** For \(\lambda=i\omega\) with \(\omega\ne0\), the imaginary part of \(F\) is
\[
 \operatorname{Im}F(i\omega;k)
 =\beta\sin\omega\,[2\beta(1-\cos\omega)+k].
\]
The bracket is strictly positive, so \(\sin\omega=0\). If \(\omega\) is an even multiple of \(\pi\), then \(h(i\omega)=0\) and \(F=-\omega^2\ne0\). If \(|\omega|=(2j+1)\pi\), then \(h=2\), and the remaining real equation is
\[
 k=k_j:=\frac{(2j+1)^2\pi^2-4\beta^2}{2\beta}.
\]
Since \(k=2(\alpha-\beta)\), this is exactly \(\alpha=\alpha_j\). No other nonzero imaginary roots occur.

**Simplicity, direction, and the complete count.** At each critical pair, let \(\omega_j=(2j+1)\pi\) and \(A_j=(\omega_j^2+4\beta^2)/2\). Direct differentiation yields
\[
 F_\lambda(i\omega_j;k_j)=-A_j+2i\omega_j\ne0,
 \qquad
 \operatorname{Re}\left.\frac{d\lambda}{d\alpha}\right|_{\alpha_j}
 =\frac{4\beta A_j}{A_j^2+4\omega_j^2}>0.
\]
For real \(\lambda\ge0\), \(F(\lambda;k)>0\) when \(\lambda>0\); the root at zero remains simple for every \(k>0\). Moreover, for \(\operatorname{Re}\lambda\ge0\), \(|h(\lambda)|\le2\), so every nonzero characteristic root in that half-plane satisfies \(|\lambda|^2\le4\beta^2+2\beta k\). On any bounded parameter interval this precludes unstable roots arriving from infinity. The right-half-plane root count can therefore change only at the identified simple imaginary crossings. Starting from zero unstable roots for small \(k>0\), each crossing adds precisely two, giving the asserted full staircase and the spectrum exactly at the critical values.

**Orbital conclusions.** In the co-rotating frame the wave is a circle of equilibria generated by the \(S^1\) phase action. Below the first threshold it has precisely one simple neutral root and all transverse characteristic roots have negative real part. The linearized stability theorem for retarded functional differential equations, applied transverse to the phase orbit, gives local exponential orbital attraction. Above the first threshold a positive-real-part characteristic pair gives orbital instability by the principle of linearized instability. No claim is made about nonlinear stability at any \(\alpha_j\).

## Verification

Run the standalone `verify.py` using Python 3. It tests the characteristic determinant directly, exact critical-frequency substitutions over several parameter families, positive crossing direction, and numerical Newton continuations on both sides of the first three critical values. The analytic inequalities and continuity argument above, not the finite checks, prove the all-parameter and all-index statements.

## Relationship to prior work

Motonaga and Takayasu (2026), arXiv:2611.04530, introduce no new equation: they study Hara's existing planar delay equation, prove seven noncircular star-shaped solutions by rigorous computation, and explicitly leave the instability threshold of the circular solution open (end of their Theorem 1.5 discussion). The circular solution and its existence threshold \(\alpha>\beta\) are earlier results of Hara, not part of this finding. The present result establishes the full transverse spectrum crossing ladder and its first exact instability threshold; it does not assert that a noncircular stable solution appears there. A 1999 paper of Sakata and Hara treats a different piecewise-constant-argument approximation, not the continuous unit-delay model. Generic delay stability and spectral-crossing methods are standard and are used without novelty claims.

## Limitations

The result gives local orbital stability and the exact linear instability dimension only. It does not prove stability or even existence of secondary star-shaped solutions, determine a nonlinear Hopf normal-form sign, establish a global basin, or identify the global attractor-selection threshold in Hara's conjecture. The original 1997 Hara article was not accessible in full during comparison, so historical priority is provisional; the accessible 2026 treatment explicitly describes the relevant circular-orbit instability threshold as open. The exact all-parameter result is a mathematical claim subject to independent verification.

## References

1. S. Motonaga and A. Takayasu, *Star-shaped periodic solutions of a system of delay differential equations: A computer-assisted proof*, arXiv:2611.04530v1 (first posted November 3, 2026), https://arxiv.org/html/2611.04530v1 .
2. T. Hara, *The asymptotic stability and star shaped periodic solutions for delay differential system*, Nonlinear Analysis 30 (1997), 4555–4563, https://doi.org/10.1016/S0362-546X(97)00318-0 (complete primary text not inspected).
3. S. Sakata and T. Hara, *Star-shaped periodic solutions for a system with piecewise constant argument*, RIMS Kôkyûroku 1083 (1999), 63–74, https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1083-7.pdf .
4. T. Hara and S. Sakata, *Star-shaped periodic solutions for a system with piecewise constant argument*, Nonlinear Analysis 49 (2002), 455–470, https://doi.org/10.1016/S0362-546X(01)00112-2 (publisher excerpt inspected; different discrete-argument model).
