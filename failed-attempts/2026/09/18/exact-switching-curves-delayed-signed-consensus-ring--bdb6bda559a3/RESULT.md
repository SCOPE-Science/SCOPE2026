# Exact switching geometry and no robust bounded phase in a delayed signed consensus ring

## Statement

Consider Wu's directed signed ring
\[
\dot x_i(t)=-(K_p-K_n)x_i(t)+K_p x_{i+1}(t-\tau_1)-K_nx_{i-1}(t-\tau_2),
\]
with periodic indices, \(K_p>K_n>0\), and \(N\ge2\). For the Fourier mode
\(\theta_k=2\pi k/N\), the transverse characteristic equation is
\[
\Delta_k(\lambda)=\lambda+K-K_p e^{i\theta_k}e^{-\lambda\tau_1}
+K_n e^{-i\theta_k}e^{-\lambda\tau_2}=0,
\qquad K=K_p-K_n.
\tag{1}
\]

### Theorem 1: complete two-delay imaginary-root geometry

Fix a transverse mode. Every positive imaginary root \(\lambda=i\omega\) is obtained from some \(s\in(0,\pi)\) by
\[
\omega(s)=2\sqrt{K_pK_n}\sin s,
\tag{2}
\]
\[
\psi(s)=\operatorname{atan2}(\omega(s),K),\qquad
\chi(s)=\operatorname{atan2}((K_p+K_n)\sin s,K\cos s),
\tag{3}
\]
and
\[
\tau_1=\frac{\theta_k-s-\psi(s)+\chi(s)+2\pi m}{\omega(s)},
\qquad
\tau_2=\frac{s-\psi(s)+\chi(s)-\theta_k+2\pi n}{\omega(s)},
\tag{4}
\]
where \(m,n\in\mathbb Z\) are chosen so that both delays are nonnegative. Conversely, every pair in (4) gives the root \(i\omega(s)\). Hence every transverse Hopf frequency satisfies the sharp bound
\[
0<\omega\le2\sqrt{K_pK_n}.
\tag{5}
\]
Negative-frequency roots are represented by the conjugate Fourier mode, so the union over modes gives the full nonzero imaginary spectrum.

### Theorem 2: no robust open bounded-nonconvergent phase

For fixed \(K_p>K_n>0\) and finite \(N\), the set of delay pairs for which a transverse characteristic root lies on the imaginary axis is a finite union over modes of countable unions of real-analytic curves (4). It therefore has two-dimensional Lebesgue measure zero and empty interior.

Off this switching set, the linear transverse dynamics has only two robust open spectral regimes: exponential convergence to consensus, or transverse instability. Neutral bounded transverse motion can occur on the switching set, but it cannot fill an open region of delay space. Special histories that exactly annihilate unstable eigendirections are nongeneric and do not define a robust system-level phase.

Thus the numerically reported "bounded non-convergent" band in the source cannot be a third open asymptotic phase of this linear autonomous model; absent another mechanism, it should be interpreted as a finite-time near-neutral/switching-boundary classification.

### Theorem 3: exact common-delay stability margin

Set \(\tau_1=\tau_2=\tau\) and
\[
\rho=\frac{\sqrt{K_p}-\sqrt{K_n}}{\sqrt{K_p}+\sqrt{K_n}}.
\tag{6}
\]
For a conjugate mode pair represented by \(\theta\in(0,\pi)\), its first loss of stability occurs at
\[
\omega_\theta=2\sqrt{K_pK_n}\sin\theta,
\tag{7}
\]
\[
\tau_c(\theta)=\frac{\arctan\!\left(\rho\tan(\theta/2)\right)}{\sqrt{K_pK_n}\sin\theta}.
\tag{8}
\]
The crossing is simple and destabilizing. Moreover \(\tau_c(\theta)\) is strictly increasing on \((0,\pi)\). Therefore, for \(N\ge3\), the first destabilizing modes are always \(k=1,N-1\), and the exact common-delay transverse consensus margin is
\[
\boxed{
\tau_*=
\frac{\arctan\!\left(\rho\tan(\pi/N)\right)}{\sqrt{K_pK_n}\sin(2\pi/N)}.
}
\tag{9}
\]
The transverse system is exponentially stable for \(0\le\tau<\tau_*\), critical at \(\tau_*\), and unstable for \(\tau>\tau_*\). For \(N=2\), the unique transverse mode is stable for every finite common delay. Finally,
\[
\tau_*(N)\downarrow\frac{\rho}{2\sqrt{K_pK_n}}>0
\qquad (N\to\infty).
\tag{10}
\]

## Proof

At zero delay,
\[
\operatorname{Re}\lambda_k(0)=-(K_p-K_n)(1-\cos\theta_k)<0
\]
for every transverse mode. Also \(\lambda=0\) cannot be a transverse root: the imaginary part of (1) at zero forces \(\sin\theta_k=0\), and \(\theta_k=\pi\) then contradicts \(K_p-K_n>0\).

For \(\lambda=i\omega\), set
\[
\alpha=\theta_k-\omega\tau_1,\qquad
\beta=\theta_k+\omega\tau_2,
\]
\[
s=(\alpha+\beta)/2,\qquad d=(\alpha-\beta)/2.
\]
Equation (1) becomes
\[
K+i\omega=e^{id}\left[K\cos s+i(K_p+K_n)\sin s\right].
\tag{11}
\]
Taking moduli gives
\[
\omega^2=4K_pK_n\sin^2s.
\]
Choosing the representative \(s\in(0,\pi)\) yields (2). Comparing arguments in (11) gives
\[
d=\psi(s)-\chi(s)\pmod{2\pi},
\]
which reconstructs (4). Reversing the steps proves the converse.

Each branch in (4) is real analytic away from its endpoint limits. Standard retarded-DDE spectral theory implies that the number of right-half-plane characteristic roots is locally constant until a root reaches the imaginary axis. Since a finite ring has finitely many modes, the switching set has empty interior and measure zero, proving Theorem 2.

For common delay, define
\[
c_\theta=K_p e^{i\theta}-K_n e^{-i\theta}.
\]
Then
\[
\lambda+K=c_\theta e^{-\lambda\tau},
\tag{12}
\]
with the exact Lambert-W spectrum
\[
\lambda_j=-K+\tau^{-1}W_j(\tau c_\theta e^{K\tau}).
\tag{13}
\]
At a positive-frequency crossing, \(|K+i\omega|=|c_\theta|\), giving (7). The factorizations
\[
c_\theta=(\sqrt{K_p}e^{i\theta/2}-\sqrt{K_n}e^{-i\theta/2})
(\sqrt{K_p}e^{i\theta/2}+\sqrt{K_n}e^{-i\theta/2}),
\]
\[
K+i\omega_\theta=(\sqrt{K_p}e^{i\theta/2}-\sqrt{K_n}e^{-i\theta/2})
(\sqrt{K_p}e^{-i\theta/2}+\sqrt{K_n}e^{i\theta/2})
\]
show that the phase gap is
\[
2\arctan\!\left(\rho\tan\frac\theta2\right),
\]
which yields (8). The negative-frequency crossing of the same complex mode occurs later.

Implicit differentiation of (12) gives
\[
\frac{d\lambda}{d\tau}=-\frac{\lambda(\lambda+K)}{1+\tau(\lambda+K)},
\]
and therefore at \(i\omega_\theta\),
\[
\operatorname{Re}\frac{d\lambda}{d\tau}
=\frac{\omega_\theta^2}{(1+K\tau)^2+(\omega_\theta\tau)^2}>0.
\tag{14}
\]
Thus the first crossing is transversal and destabilizing.

To order the modes, put \(x=\tan(\theta/2)>0\). Apart from a positive constant, (8) equals
\[
F(x)=(x+x^{-1})\arctan(\rho x).
\]
For \(x\ge1\), \(F'(x)>0\) directly. For \(0<x<1\), using \(\arctan(\rho x)<\rho x\) in the negative term of \(F'\) gives the strict lower bound
\[
F'(x)>
\frac{\rho x(2-\rho^2+\rho^2x^2)}{1+\rho^2x^2}>0.
\]
Hence (8) is strictly increasing in \(\theta\), proving (9). For \(N=2\), the transverse equation is
\[
\lambda+K+Ke^{-\lambda\tau}=0.
\]
If \(\operatorname{Re}\lambda\ge0\), then \(|\lambda+K|\ge K\) while \(|Ke^{-\lambda\tau}|\le K\); equality would force \(\lambda=0\), which is not a root. This proves stability for all finite \(\tau\). The small-angle limit in (9) gives (10).

## Example

For \(K_p=2\), \(K_n=1\), \(N=20\),
\[
\tau_*\approx0.06216657113,\qquad
\omega_*\approx0.87403204890,
\]
and the large-ring limit is approximately \(0.06066017178\). The compact verification script in `artifacts/check_common_delay.py` reproduces these values, checks that \(k=1\) is the first mode, and evaluates the characteristic residual at the crossing.

## Relation to prior literature

Wu derives (1), writes the imaginary-axis conditions only implicitly, constructs a numerical three-region phase diagram, and lists sharper analytical stability boundaries as future work. General D-decomposition/CTCR methods, Lambert-W representations, and frequency-domain methods for two-delay LTI systems are established and are not claimed as new here. The contribution is the source-specific closed switching geometry (2)--(4), the no-open-neutral-phase consequence for the finite linear ring, and the exact all-\(N\) common-delay margin (9) with mode ordering and limit (10).

A 2026 signed-Laplacian paper on heterogeneous constant delays studies a different graph-theoretic formulation and gives consensusability conditions; it does not, in the inspected abstract, state these ring-specific formulas.

## Limitations

- Stability conclusions assume \(K_p>K_n>0\). Other coupling orderings may exhibit different delay-induced behavior.
- The no-open-bounded-phase conclusion is a transverse spectral statement for the linear homogeneous model; specially prepared histories are not a robust phase.
- The full two-delay formulas parametrize all switching curves but do not by themselves label every connected stability cell.
- Nonlinear signed-consensus systems, switching graphs, noise, and time-varying delays are outside scope.
- Originality is asserted only to the best of our knowledge; the general delay-equation tools used in the proof are standard.

## References

1. H. Wu, *Delay-Induced Stability Transitions in Directed Signed Consensus Networks*, arXiv:2604.15570 (2026). https://arxiv.org/abs/2604.15570
2. C. Yuan, S. Song, Q. Gao, H. R. Karimi, L. Pekar, and S. Guo, *A Novel Frequency-Domain Approach for the Exact Range of Imaginary Spectra and the Stability Analysis of LTI Systems With Two Delays*, IEEE Access 8 (2020), 36595--36601. https://doi.org/10.1109/ACCESS.2020.2973834
3. S. Yi et al., *Fast consensus in a large-scale multi-agent system with directed graphs using time-delayed measurements*, Philosophical Transactions of the Royal Society A 377 (2019), 20180130. https://doi.org/10.1098/rsta.2018.0130
4. Y. Song, M. Xue, J. Hou, Y. Lu, and Q. Liu, *Consensusability of Continuous-Time Multi-Agent Systems With Unbounded Heterogeneous Constant Delays: A Signed Laplacian Perspective*, arXiv:2608.15133 (2026). https://arxiv.org/abs/2608.15133
