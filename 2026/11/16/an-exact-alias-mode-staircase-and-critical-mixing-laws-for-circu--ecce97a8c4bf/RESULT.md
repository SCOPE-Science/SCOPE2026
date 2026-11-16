# An exact alias-mode staircase and critical mixing laws for circular Fock interpolation

## Finding

Fix an integer \(N\ge2\) and a real \(\rho>0\). In the classical Bargmann–Fock Hilbert space, let \(f_{N,\rho}\) be the minimum-norm entire function satisfying \(f_{N,\rho}(\sqrt{\rho N}\,e^{2\pi i j/N})=1\) for all integers \(0\le j<N\). Let \(e_m(z)=z^m/\sqrt{m!}\). Its exact finite-parameter expansion is
\[
 f_{N,\rho}(z)=\frac{1}{S_N(\rho)}\sum_{k=0}^{\infty}\frac{(\sqrt{\rho N}\,z)^{kN}}{(kN)!},\qquad
 S_N(\rho)=\sum_{k=0}^{\infty}\frac{(\rho N)^{kN}}{(kN)!},\qquad
 \|f_{N,\rho}\|^2=\frac1{S_N(\rho)}.
\]
This exact expansion is background implicit in the established cyclic Fock-kernel spectrum and in circular-coherent-state formulas, not a novelty assertion. The result is a **complete fixed-ratio alias-mode phase diagram, including all higher-order transitions and the different first critical window**.

For integers \(k\ge1\), define the strictly increasing thresholds
\[
 \tau_1=e^{-1},\qquad
 \tau_k=\frac{k^k}{e(k-1)^{k-1}}\quad(k\ge2),\qquad \tau_0=0.
\]
For every fixed integer \(k\ge0\) and fixed \(\tau_k<\rho<\tau_{k+1}\), the normalized minimum-norm interpolant \(u_{N,\rho}=f_{N,\rho}/\|f_{N,\rho}\|\) satisfies
\[
 \|u_{N,\rho}-e_{kN}\|\longrightarrow0\quad(N\to\infty).
\]
The convergence is exponentially fast in squared Hilbert norm. For \(k=0\), the squared optimal interpolation norm tends to one; for \(k\ge1\), letting \(\Phi_\rho(k)=k(1+\log(\rho/k))\), it obeys
\[
 \|f_{N,\rho}\|^2\sim \sqrt{2\pi kN}\,e^{-N\Phi_\rho(k)}.
\]
Every one of the countably many thresholds changes the dominant Fourier alias. The corresponding **exact finite-\(N\) switching radii** are
\[
 \tau_{k,N}=\frac1N\left(\frac{(kN)!}{((k-1)N)!}\right)^{1/N},\qquad k\ge1,
\]
and are strictly increasing in \(k\); at \(\rho=\tau_{k,N}\), exactly the two adjacent individual summands indexed \(k-1,k\) tie for the maximum. For every fixed \(k\ge2\),
\[
 \log\tau_{k,N}=\log\tau_k+\frac{\log(k/(k-1))}{2N}+O_k(N^{-2}),
\]
whereas the first switch has an anomalously wider logarithmic correction:
\[
 \log\tau_{1,N}=-1+\frac{\log(2\pi N)}{2N}+O(N^{-2}).
\]

For a fixed integer \(k\ge2\) and real \(x\), tune \(\rho_N=\tau_k e^{x/N}\), and let \(\Phi_k=\Phi_{\tau_k}(k)=\Phi_{\tau_k}(k-1)>0\). Write
\[
 c_{k,-}(x)=\frac{e^{(k-1)x}}{\sqrt{k-1}},\quad
 c_{k,+}(x)=\frac{e^{kx}}{\sqrt k},\quad
 C_k(x)=c_{k,-}(x)+c_{k,+}(x).
\]
Then, with convergence in the indicated moving two-dimensional Fock subspace,
\[
 \left\|u_{N,\rho_N}-\sqrt{\frac{c_{k,-}(x)}{C_k(x)}}e_{(k-1)N}
 -\sqrt{\frac{c_{k,+}(x)}{C_k(x)}}e_{kN}\right\|\longrightarrow0,
\]
and
\[
 \frac{e^{N\Phi_k}}{\sqrt{2\pi N}}\|f_{N,\rho_N}\|^2\longrightarrow \frac1{C_k(x)}.
\]
The relative weight of the larger alias follows an exact logistic crossover in \(x\), with equal limiting weights precisely at \(x=\frac12\log(k/(k-1))\).

At the first threshold, the appropriate critical window is **not** of order \(N^{-1}\) without recentering. For fixed \(x\in\mathbb R\), put
\[
 \rho_N=e^{-1}\exp\left(\frac{\frac12\log(2\pi N)+x}{N}\right),\qquad
 q(x)=\frac{e^x}{1+e^x}.
\]
Then
\[
 \left\|u_{N,\rho_N}-\sqrt{1-q(x)}\,e_0-\sqrt{q(x)}\,e_N\right\|\longrightarrow0,
 \qquad \|f_{N,\rho_N}\|^2\longrightarrow\frac1{1+e^x}.
\]
In particular, at the unshifted fixed ratio \(\rho=e^{-1}\), the vacuum is still dominant, with \(\|f_{N,e^{-1}}\|^2=1-(2\pi N)^{-1/2}+O(N^{-1})\).

## Assumptions and scope

The space is \(\mathcal F^2=\{f(z)=\sum_{m\ge0}a_mz^m:\sum_{m\ge0}m!|a_m|^2<\infty\}\), with reproducing kernel \(K(z,w)=e^{z\overline w}\). The interpolation data are **unnormalized constant values equal to one** at exactly \(N\) equally spaced nodes on the circle of squared radius \(\rho N\). The minimizer is unique. Parameter \(\rho\) is held fixed for the phase diagram, except in the displayed \(N\)-dependent critical windows where the positive integer \(k\) and real \(x\) are fixed. The moving Fock basis \(e_{kN}\) makes norm convergence meaningful; there is no claimed convergence of a moving high-degree basis element to a fixed vector. All asymptotics are for \(N\to\infty\), without uniformity over growing \(k\) or unbounded \(x\).

## Proof

**1. Exact constant-data solution.** Rotation by \(2\pi/N\) preserves the Fock norm, permutes the nodes and preserves constant data. Uniqueness of Hilbert-space minimum-norm interpolation therefore forces the minimizer to be a sum of monomials whose degrees are divisible by \(N\). Write \(f(z)=\sum_{k\ge0}a_kz^{kN}\). The single constraint at \(z=r=\sqrt{\rho N}\) is \(\sum_k a_kr^{kN}=1\), and the squared norm is \(\sum_k (kN)!|a_k|^2\). Cauchy–Schwarz gives \(1\le \|f\|^2 S_N(\rho)\); equality is attained by the displayed coefficients. For each \(N,\rho\), the sum converges absolutely and all coefficients are positive. Dividing by its norm yields
\[
 u_{N,\rho}=\sum_{k\ge0}\sqrt{p_{N,k}(\rho)}\,e_{kN},\qquad
 p_{N,k}(\rho)=\frac{T_{N,k}(\rho)}{S_N(\rho)},\quad
 T_{N,k}(\rho)=\frac{(\rho N)^{kN}}{(kN)!}.
 \tag{1}
\]
This identity is explicitly not asserted to be new: it is the residue-zero component of established circular-kernel Fourier formulas.

**2. Exact dominant-index switches.** The ratio of successive weights is
\[
 \frac{T_{N,k}(\rho)}{T_{N,k-1}(\rho)}
 =\left(\frac{\rho}{\tau_{k,N}}\right)^N.
 \tag{2}
\]
The products of successive \(N\) positive integers strictly increase with \(k\), so \(\tau_{k,N}\) strictly increases and tends to infinity with \(k\) for each fixed \(N\). Thus the sequence of weights is strictly unimodal away from switching radii; at any switch exactly the two consecutive largest weights tie. Stirling's formula gives, for fixed \(k\ge2\),
\[
 \begin{aligned}
 \log \tau_{k,N}
 &=\frac1N\{\log\Gamma(kN+1)-\log\Gamma((k-1)N+1)\}-\log N\\
 &=k\log k-(k-1)\log(k-1)-1
 +\frac{\log(k/(k-1))}{2N}+O_k(N^{-2}).
 \end{aligned}
\]
For \(k=1\), apply Stirling directly to \(N!\), obtaining the exceptional \(\log N/(2N)\) correction. Strict convexity of \(t\mapsto t\log t\) shows \(\tau_k\) strictly increases; its asymptotic growth is linear, so it diverges.

**3. Concentration away from all switches.** For fixed integer \(j\ge1\), Stirling gives
\[
 T_{N,j}(\rho)=\frac{e^{N\Phi_\rho(j)}}{\sqrt{2\pi jN}}(1+O_{j,\rho}(N^{-1})),
 \quad \Phi_\rho(j)=j(1+\log(\rho/j)),
 \tag{3}
\]
whereas \(T_{N,0}=1\) and \(\Phi_\rho(0)=0\). The adjacent difference \(\Phi_\rho(j)-\Phi_\rho(j-1)=\log(\rho/\tau_j)\) for \(j\ge1\). Hence exactly one integer \(k\) maximizes these exponents when \(\tau_k<\rho<\tau_{k+1}\). To justify the infinite tail, choose an integer \(J>2\rho+2\). For \(j\ge J\), (2) and the elementary factorial-product bound give \(T_{N,j+1}/T_{N,j}\le(\rho/j)^N\le2^{-N}\); consequently the sum over \(j\ge J+1\) is bounded by \(T_{N,J+1}/(1-2^{-N})\). For the finite first \(J\) terms, the strict exponent gap from (3) makes all other weights exponentially small relative to the \(k\)-th term. Therefore \(p_{N,k}=1-O_\rho(e^{-c_\rho N})\) and the norm convergence in the statement follows from the orthonormal expansion (1). Taking the reciprocal of the dominant term gives the squared interpolation norm asymptotic; when \(k=0\), \(S_N\to1\).

**4. Higher critical windows.** At \(\rho=\tau_k\) for fixed \(k\ge2\), the maximal exponent is attained only at \(k-1,k\) and is strictly positive. Put \(\rho_N=\tau_k e^{x/N}\). For each fixed \(j\ge1\), equation (3) becomes
\[
 T_{N,j}(\rho_N)=\frac{e^{N\Phi_{\tau_k}(j)+jx}}{\sqrt{2\pi jN}}(1+O_{j,k,x}(N^{-1})).
\]
By the same finite-gap and uniform-tail argument, only terms \(k-1,k\) survive relative to \(e^{N\Phi_k}/\sqrt{2\pi N}\). This proves both the scaled optimal norm and the two-component Fock-norm convergence. The ratio of their limiting probabilities is \(c_{k,+}/c_{k,-}=e^x\sqrt{(k-1)/k}\), proving the logistic law and its exact centering.

**5. Vacuum critical window.** With \(\rho_N=e^{-1}\exp((\frac12\log(2\pi N)+x)/N)\), Stirling yields
\[
 T_{N,1}(\rho_N)=\frac{(\rho_N N)^N}{N!}
 =e^x(1+O(N^{-1})),\quad T_{N,0}=1.
\]
Every \(j\ge2\) has a strictly negative limiting exponential rate \(\Phi_{e^{-1}}(j)<0\), so its mass vanishes uniformly after the same tail argument (the \(O(\log N)\) extra exponent cannot eliminate a fixed negative rate gap). Equation (1) then gives the two-mode limit and \(S_N\to1+e^x\). At exactly \(\rho=e^{-1}\), one has \(T_{N,1}=(2\pi N)^{-1/2}(1+O(N^{-1}))\), with all other terms exponentially smaller, and \((1+T_{N,1}+\cdots)^{-1}=1-(2\pi N)^{-1/2}+O(N^{-1})\). This completes the proof.

## Verification

The standalone `CHECK.py` uses only the Python standard library. It independently checks exact finite-\(N\) threshold equalities using factorial products, the rotational interpolation conditions and Hilbert norm of the explicit extremizer, the mode-concentration hierarchy for several fixed ratios, and the two distinct critical-window probability profiles at multiple \(N\). The executable finite checks supplement the exact Hilbert-space argument and uniform tail estimates above. No finite calculation establishes all \(N\), all \(k\), or historical priority.

## Relationship to prior work

Alpay, De Martino and Diki (2026) [1], in their originally public April 24 preprint, develop representer methods for complex RKHS and Fock interpolation; their Section 4.1 discusses collinear superoscillatory interpolation rather than constant-value regular polygons. Horoshko, De Bièvre, Kolobov and Patera (2016) [2], especially Eqs. (9), (11), (14), (38)–(40), **already prove the same exact cyclic Poisson-residue expansion for rotationally invariant circular coherent states and discuss the first vacuum-dominance transition**. Neither the exact expansion nor existence of a first transition is claimed as original here. The new mathematical object is the complete **all-index** dominance diagram for the fixed-ratio family and its **sharp two-regime critical limits**, including the logarithmic displacement of the vacuum boundary.

Published work on sharp circular Fock interpolation conditioning [3] and minimax interpolation cost [4] already diagonalizes the same kernel Gram and computes its extreme Poisson-residue spectral asymptotics. In particular, [4] gives the explicit Fourier-mode minimum-norm interpolant, so its \(m=0\) case **implies the exact finite formula in (1)**. Its principal minimax result concerns the *least* residue mass and its competing aliases, not the largest individual alias in fixed residue zero, all higher switching scales or the moving-vector critical mixtures. Its identric-mean function evaluated at nonnegative integers equals the thresholds \(\tau_k\), making it a close mathematical predecessor but not an established implication for the stated critical profiles.

Luo, Tang and Zhang (2024) [5] study optimization of circular coherent states for mean photon number. A publisher preview and abstract were available, but complete original text could not be examined: the possibility that an equivalent transition calculation is buried in this related work is a material unresolved bibliographical risk, not evidence of absence. Terminological variants include circular coherent states, residue-conditioned Poisson distributions, and projected coherent states.

## Limitations

These statements concern one Gaussian Fock space, constant data on a single equal-angle circle, fixed \(k\) in the critical windows, and the specified \(\rho N\) scaling. No uniform growing-index critical theorem, general irregular-node stability, or uniformity as \(x\to\pm\infty\) is asserted. The exact finite-\(N\) Fock solution is a known consequence of circular coherent-state formulas. The novelty comparison is evidence-limited, especially by the inaccessible 2024 paper and unindexed quantum-optics terminology. There has been no independent audit.

## References

[1] N. Alpay, A. De Martino and K. Diki, *Representer theorem in complex reproducing kernel Hilbert spaces with applications to Fock and Hardy spaces and superoscillations*, arXiv:2604.22165v1, first public 24 April 2026, Sec. 4.1. https://arxiv.org/html/2604.22165v1

[2] D. B. Horoshko, S. De Bièvre, M. I. Kolobov and G. Patera, *Entanglement of quantum circular states of light*, arXiv:1602.07852v1, 25 February 2016, Eqs. (9), (11), (14), (38)–(40). https://arxiv.org/pdf/1602.07852

[3] *A sharp \(e^{-1}\) conditioning transition for circular Fock interpolation*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-sharp-e-1-conditioning-transition-for-circular-fock-interpolat--3eb6ee5c2781

[4] *Sharp exponential minimax interpolation cost on expanding Fock circles*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-exponential-minimax-interpolation-cost-on-expanding-fock-c--7b97c5b1856d

[5] S. Luo, S. Tang and Y. Zhang, *Optimal circular states*, *Journal of Physics A* 57 (2024), 465301, DOI:10.1088/1751-8121/ad8792; available abstract and publisher preview, full manuscript not inspected.
