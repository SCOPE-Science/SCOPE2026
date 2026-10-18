# A log-fourth crossover law inside the noisy fermionic-Fourier model
## Finding
Within the analytic crossover model of arXiv:2610.01704v1, suppose the FFT-matched adiabatic time obeys \(T(N)=\kappa(\log N)^2(1+o(1))\) for some \(\kappa>0\), and let \(N_*(p)\to\infty\) as \(p\to0\) satisfy the paper's crossover equation \[N_*(p)=\frac{1}{a\pi^2 p\,T(N_*(p))^2}+\frac{2c}{a\,{\rm d}t},\] with fixed positive \(a,c,{\rm d}t\). Then \[pN_*(p)\bigl(\log(1/p)\bigr)^4\longrightarrow\frac{1}{a\pi^2\kappa^2},\] so \(N_*(p)=\Theta(1/[p(\log(1/p))^4])\). More generally, if the noiseless adiabatic error scales as \(T^{-\gamma}\) and the crossover balance is \(N_*(p)=\Theta(1/[pT(N_*)^{1+\gamma}])\), the same \(T(N)=\Theta((\log N)^2)\) assumption gives \(N_*(p)=\Theta(1/[p(\log(1/p))^{2(1+\gamma)}])\). These are conditional consequences of the source's analytic noise model, not hardware-universal asymptotics.

## Assumptions and scope
The statement concerns only the analytic crossover model in Granet and Dreyer, arXiv:2610.01704v1. Their tight-binding example compares a fermionic Fourier transform with an adiabatic circuit at matched gate count. In the model, the adiabatic energy-density error is approximated by \(1/(\pi^2T)+2pcT/{\rm d}t\), the FFT contribution by \(apNT\), and the crossover is written as
\[
N_*=\frac{1}{a\pi^2pT(N_*)^2}+\frac{2c}{a\,{\rm d}t}.
\]
The paper then states that a depth-\(\log^2 N\) FFT compilation gives \(T(N)\sim\log^2N\). The present result takes those two displayed assumptions at face value and determines their joint asymptotic implication. It does not assert that the phenomenological constants are universal, that the hardware data are asymptotic, or that every FFT implementation has this scaling.

## Proof
Put \(A=1/(a\pi^2)\) and \(B=2c/(a\,{\rm d}t)\). The crossover equation is equivalent to
\[
p(N_*-B)T(N_*)^2=A.
\]
Because \(A>0\), any solution along \(p\to0\) must satisfy \(N_*\to\infty\); otherwise the left side tends to zero. Hence \(N_*-B=N_*(1+o(1))\). Under
\[
T(N)=\kappa(\log N)^2(1+o(1)),
\]
we obtain
\[
pN_*(\log N_*)^4\longrightarrow\frac{A}{\kappa^2}.
\]
Taking logarithms gives
\[
\log N_*=\log(1/p)-4\log\log N_*+O(1),
\]
so \(\log N_*/\log(1/p)\to1\). Substitution yields
\[
pN_*(\log(1/p))^4\longrightarrow\frac{1}{a\pi^2\kappa^2}.
\]
For a general noiseless error \(T^{-\gamma}\), balancing it against the FFT-noise scale \(pNT\) gives \(N=\Theta(1/[pT^{1+\gamma}])\). With \(T(N)=\Theta((\log N)^2)\), the same logarithm inversion gives the exponent \(2(1+\gamma)\).

## Verification
The proof is analytic once the source model and the stated asymptotic for \(T(N)\) are assumed. The accompanying standard-library script `artifacts/verify.py` solves the simplified exact model \(N(\log N)^4=C/p\) for decreasing \(p\) and checks convergence of the normalized ratio. Those finite computations are corroborative only.

## Relationship to prior work
Granet and Dreyer, arXiv:2610.01704v1, derive the crossover equation and separately state the \(T(N)\sim\log^2N\) scaling associated with the cited low-depth FFT compilation. Their subsequent displayed crossover law uses only a squared logarithm in the denominator. The result here is the direct asymptotic consequence of the preceding crossover equation together with the stated \(\log^2N\) time law. Constantinides et al., arXiv:2510.05099v2, provide an \(O(\log^2N)\)-depth ancilla-free fermion-routing construction, supporting the relevance of the depth assumption but not analyzing this noise crossover.

## Limitations
The conclusion is conditional on the phenomenological equations used in the source and on interpreting the matched adiabatic time as \(T(N)=\kappa(\log N)^2(1+o(1))\). If the relevant matched-gate resource instead scales as \(\log N\), then a squared-logarithm crossover is compatible with the same algebra. The result therefore identifies the asymptotic consequence of the source's stated pair of assumptions; it does not decide which resource scaling best models a particular compiled circuit or device.

## References
1. E. Granet and H. Dreyer, *Less precise but less noisy: local circuits for momentum-space state preparation and measurement*, arXiv:2610.01704v1 (first public 2026-10-01).
2. N. Constantinides et al., *Low-depth fermion routing without ancillas*, arXiv:2510.05099v2.
