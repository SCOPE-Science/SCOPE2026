# Sharp dephasing ceiling and a memory-matched exceptional point in recency-reset qubits

## Finding
Consider a qubit whose Poisson resets sample its own prior evolution with an exponentially distributed *look-back age*, clipped at the initial preparation. The decay exponent of every nonzero Bohr coherence is bounded above by the Poisson reset rate. This bound is attained **if and only if** the look-back decay rate matches the reset rate and the Bohr gap is at least twice the reset rate. At the boundary gap the exact coherence evolution has a second-order exceptional point, yet there are no coherence revivals: the entire matched-rate qubit evolution is completely-positive-divisible.

More precisely, let \(r>0\), \(\gamma>0\), and real \(\omega\ne0\), and set
\[
\Delta=(r+\gamma)^2-\omega^2+2i\omega(r-\gamma),\qquad
G(r,\gamma,\omega)=\frac{r+\gamma-\operatorname{Re}\sqrt{\Delta}}{2},
\]
with the principal square root. If \(f(t)\) multiplies the initial upper-right coherence, then
\[
\lim_{t\to\infty}-\frac1t\log|f(t)|=G(r,\gamma,\omega),\qquad
0<G(r,\gamma,\omega)\le r.
\]
Equality holds precisely at \(\gamma=r\) with \(|\omega|\ge2r\), so \(\gamma=r\) is the **unique** decay-rate-maximizing age parameter for every fixed \(|\omega|\ge2r\). For \(|\omega|<2r\), no claim is made that matched rates optimize the decay.

At \(\gamma=r\), define \(\delta=\sqrt{4r^2-\omega^2}\). The exact coherence factor is
\[
f(t)=e^{-(r+i\omega/2)t}
\left[\cosh\left(\frac{\delta t}{2}\right)
+\frac{2r-i\omega}{\delta}\sinh\left(\frac{\delta t}{2}\right)\right],
\]
interpreted continuously at \(\delta=0\). For all \(t>0\), \(|f(t)|\) is strictly decreasing; in particular, at \(|\omega|=2r\),
\[
|f(t)|^2=e^{-2rt}(1+2rt+2r^2t^2).
\]
The coalescence at \(\gamma=r,|\omega|=2r\) is a genuine non-diagonalizable second-order exceptional point of the coherence generator, visible as a linear-exponential contribution to \(f(t)\), but it does not cause trace-distance information backflow.

## Assumptions and scope
The system has \(H=(\omega/2)\sigma_z\), \(\hbar=1\), and an arbitrary initial density matrix \(\rho_0\). Resets occur at the points of a homogeneous Poisson process of rate \(r\). At each event at elapsed time \(t>0\), independently sample an age \(A\) with density \(\gamma e^{-\gamma A}\) on \((0,\infty)\). If \(A<t\), return to the trajectory's state at \(t-A\); if \(A\ge t\), return to \(\rho_0\). Equivalently, the reset-time distribution on \([0,t]\) is \(e^{-\gamma t}\delta_0(ds)+\gamma e^{-\gamma(t-s)}\mathbf1_{(0,t)}(s)ds\). This initial-time atom is part of the protocol and ensures exact normalization and an autonomous exponential-memory embedding. It is **not** the conditional exponential density normalized on \([0,t]\); the latter is a different model. The density matrix in the claim is averaged over the resetting history. Populations are preserved; for upper-right coherence, \(\rho_{01}(t)=f(t)\rho_{01}(0)\). All parameters \(r,\gamma\) are strictly positive; \(\omega\ne0\), \(t\ge0\).

## Proof
1. **Exact causal closure.** The averaged memory input at time \(t\) is
\[
M(t)=e^{-\gamma t}\rho_0+\gamma\int_0^t e^{-\gamma(t-s)}\rho(s)\,ds.
\]
The reset event rate and Liouville term give \(\dot\rho=-i[H,\rho]+r(M-\rho)\). Differentiating the normalized convolution yields \(\dot M=\gamma(\rho-M)\), with \(\rho(0)=M(0)=\rho_0\). Therefore every nonzero upper-right coherence obeys the two-component homogeneous system
\[
\frac d{dt}\binom{f}{h}=
\begin{pmatrix}-r-i\omega&r\\\gamma&-\gamma\end{pmatrix}
\binom{f}{h},\qquad(f(0),h(0))=(1,1).
\]
This derivation holds for mixed and pure initial states and does not assume an equilibrium limit.

2. **Spectrum, noncancellation, and decay.** The characteristic discriminant is \(\Delta\), and the two eigenvalues are \(\lambda_\pm=-(r+\gamma+i\omega)/2\pm\sqrt\Delta/2\). For \(\gamma\ne r\) the imaginary part of \(\Delta\) is nonzero, so the eigenvalues have distinct real parts. The initial vector excites the dominant mode: otherwise \(f(t)\) would be a single exponential with logarithmic derivative \(-i\omega\) at \(t=0\), but \(-i\omega\) is not an eigenvalue since \(\det(A+i\omega I)=-ir\omega\ne0\). The same argument applies when \(\gamma=r\) and \(|\omega|<2r\). When \(\gamma=r\) and \(|\omega|>2r\), the explicit solution below has a nonvanishing continuous periodic modulus after removing \(e^{-rt}\); at equality it has a nonzero linear polynomial. Hence the stated limit equals the negative leading real spectral part in all cases.

3. **Stability and sharp ceiling.** For \(z=(f,h)\), the quadratic form \(Q=\gamma|f|^2+r|h|^2\) satisfies
\[
\dot Q=-2r\gamma|f-h|^2.
\]
No eigenvector at a purely imaginary eigenvalue can have \(f=h\ne0\) when \(\omega\ne0\), since the second component would have zero derivative while the first rotates. Thus both eigenvalues have strictly negative real parts and \(G>0\). If \(\gamma<r\), then \(G\le(r+\gamma)/2<r\). For \(\gamma>r\), put \(d=\gamma-r\) and \(a=(r+\gamma)^2-\omega^2\). With \(\Delta=a-2i\omega d\),
\[
|\Delta|^2-(2d^2-a)^2=16r\gamma d^2>0.
\]
Since \((\operatorname{Re}\sqrt\Delta)^2=(|\Delta|+a)/2\), it follows that \(\operatorname{Re}\sqrt\Delta>d\), whence \(G<r\). At \(\gamma=r\), \(\Delta=4r^2-\omega^2\) is real and \(G=r-\tfrac12\sqrt{(4r^2-\omega^2)_+}\). This establishes the exact equality criterion and unique maximum for fixed \(|\omega|\ge2r\).

4. **The exceptional point and absence of backflow.** Exponentiating the two-by-two generator at \(\gamma=r\) gives the claimed closed form. The discriminant vanishes exactly when \(\gamma=r\) and \(|\omega|=2r\), at which point the off-diagonal positive entries prevent diagonalizability. For \(\delta\ne0\), direct differentiation yields
\[
\frac{d}{dt}|f(t)|^2
=-2r\omega^2e^{-2rt}
\frac{\cosh(\delta t)-1}{\delta^2}\le0,
\]
where the ratio is real and nonnegative for either real \(\delta\) or imaginary \(\delta\). At \(\delta=0\), this becomes \(-r\omega^2t^2e^{-2rt}\). The derivative vanishes at most at isolated times, so \(|f(t)|\) is strictly decreasing for positive times. The closed form has no finite-time zeros (for imaginary \(\delta\), its nonzero imaginary sine term and real cosine cannot vanish together; the real and zero-discriminant cases are also nonvanishing). Consequently the intermediate dephasing map from \(s\) to \(t\ge s\) multiplies coherences by \(f(t)/f(s)\) of modulus at most one and is completely positive and trace preserving. Thus the matched-rate reduced qubit evolution is CP-divisible and admits no trace-distance revival, including at the exceptional point.

## Verification
Run `python3 verify.py` with Python 3. It compares the exact matrix-exponential expression against an independently integrated fourth-order Runge--Kutta version of the causal two-component equations at 270 parameter-time triples, checks the strict spectral bound on a parameter grid, and tests the derivative, exceptional-point polynomial law, and its monotone sign across the matched-rate regimes. It uses only the standard library. These computations are numerical regression checks; the parameter-global claims are established by the algebraic proof above, not by sampling.

## Relationship to prior work
De Mauro, Kulkarni and Majumdar [1, Secs. 2--3, 5] develop quantum resetting to a **uniformly chosen** past time. Their coherence is governed by an ever-expanding \(1/t\) memory average and decays algebraically; the present exactly normalized *clipped exponential-age* model instead has a two-dimensional autonomous closure and exponential dephasing. The paper explicitly identifies nonuniform history kernels as a future direction, but does not prove this sharp optimization, its exceptional-point locus, or its CP-divisibility conclusion. Boyer, Evans and Majumdar [2] provide a classical nonuniform-memory diffusion framework, which does not imply these quantum coherence or CP properties. Chen et al. [3] analyze exceptional-point visibility in colored-Gaussian-bath non-Markovian quantum-state diffusion, not preferential-return resetting; their general distinction between Jordan modes and observed coherences motivates explicitly verifying noncancellation here. These are substantive comparisons, not claims that a search proves uniqueness.

## Limitations
The result is restricted to an idealized qubit with independent classical history-sampling and clamped exponential memory ages. It does not assert the same sharp ceiling for a truncated-and-renormalized recency kernel, for general nonexponential age laws, or for interacting multipartite systems. A qubit CP-divisibility conclusion does not automatically extend to multi-gap systems. For \(|\omega|<2r\), matched rates need not be optimal. The exceptional-point and coherence monotonicity statements are analytically proved, but there is no independent external mathematical audit. An unindexed formulation of the same exponential-memory closure remains a publication-priority risk.

## References
[1] G. de Mauro, M. Kulkarni and S. N. Majumdar, *Quantum resetting with memory*, arXiv:2608.02297v1 (first submitted 2026-08-03), https://arxiv.org/abs/2608.02297.

[2] D. Boyer, M. R. Evans and S. N. Majumdar, *Diffusion with preferential relocation in a confining potential*, arXiv:2411.00641 (first submitted 2024-11-01), https://arxiv.org/abs/2411.00641.

[3] Y. Chen et al., *Exceptional points in non-Markovian quantum-state diffusion: From coefficient dynamics to state signatures*, arXiv:2611.13221v1 (first submitted 2026-11-09), https://arxiv.org/abs/2611.13221.
