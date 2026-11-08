# Subextensive Rényi entropy and a sharp attainment threshold for common-clock quantum resetting

## Finding
Let \(N\ge1\) noninteracting qubits undergo coherent rotations at angular frequency \(\Omega>0\) and simultaneous complete resets to \(\lvert0\rangle^{\otimes N}\). All qubits share one iid renewal reset clock with interarrival \(T>0\) almost surely and \(0<\mu=\mathbb ET<\infty\). Work in the **stationary equilibrium-renewal ensemble**, not necessarily the large-time limit from a synchronized initial reset. Set \(\tau=\pi/\Omega\) and write \(\rho_N\) for the ensemble-averaged \(N\)-qubit density matrix and \(P_N=\operatorname{Tr}\rho_N^2\). For \(k\in\mathbb Z\setminus\{0\}\), define
\[
 m_k=\frac{\mathbb E[e^{2ik\Omega T}]-1}{2ik\Omega\mu},\qquad m_0=1.
\]
Then for every \(N\ge1\), the **exact purity** is
\[
 P_N=4^{-N}\sum_{k=-N}^{N}{2N\choose N+k}|m_k|^2.
\]
The universal many-qubit limit is
\[
 \sqrt{\pi N}\,P_N\longrightarrow
 \mathcal A(T)=\sum_{k\in\mathbb Z}|m_k|^2
 =\tau\int_0^\tau g(a)^2\,da\in[1,\infty),
\]
where the wrapped stationary-age density is
\[
 g(a)=\frac1\mu\sum_{j=0}^\infty \mathbb P(T>a+j\tau),\qquad 0\le a<\tau.
\]
Consequently, the stationary global second Rényi entropy obeys
\[
 S_2(\rho_N)=-\log P_N
 =\tfrac12\log(\pi N)-\log\mathcal A(T)+o(1).
\]
For every \(N\), the sharp distribution-free lower bound is
\[
 P_N\ge4^{-N}{2N\choose N};
\]
**equality for one (equivalently every) \(N\ge1\) holds if and only if \(T\in\tau\mathbb N\) almost surely.** Fixing both \(\mu>0\) and \(\Omega>0\), for each fixed \(N\), the infimum of \(P_N\) over all positive interarrival laws of mean \(\mu\) is always this lower bound, and the infimum of \(\mathcal A\) is \(1\). These minima are **attained if and only if \(\mu\ge\tau\)**. If \(\mu<\tau\), neither infimum is attained; two-point reset clocks with a vanishingly short component approach both infima.

As a concrete benchmark, for exponential reset intervals of rate \(r>0\),
\[
 \mathcal A(T)=\frac{\pi r}{2\Omega}\coth\!\left(\frac{\pi r}{2\Omega}\right),\qquad
 P_N\sim\frac{r\sqrt\pi}{2\Omega}\coth\!\left(\frac{\pi r}{2\Omega}\right)N^{-1/2}.
\]

## Assumptions and scope
The Hamiltonian is \(H=\hbar\Omega\sum_{j=1}^N\sigma_x^{(j)}\); between resets the state is the pure product \(\lvert\psi(a)\rangle^{\otimes N}\), with \(\lvert\psi(a)\rangle=\cos(\Omega a)\lvert0\rangle-i\sin(\Omega a)\lvert1\rangle\). Each resetting event acts globally and instantaneously. Interarrival times are independent of the coherent evolution, iid, strictly positive almost surely, with finite positive mean; no density, higher moments, or nonlattice assumption is imposed. The observation age \(A\) has stationary density \(w(a)=\mathbb P(T>a)/\mu\) on \([0,\infty)\), and \(\rho_N=\mathbb E[\lvert\psi(A)\rangle^{\otimes N}\langle\psi(A)\rvert^{\otimes N}]\). All logarithms are natural. Quantum Rényi entropy here quantifies mixing of the averaged state, not entanglement: every trajectory is a product state and \(\rho_N\) is separable.

## Proof
**Step 1 (renewal age and overlap).** Stationary renewal-reward theory gives \(w(a)=\mathbb P(T>a)/\mu\), including when the interarrival law has atoms. For independent stationary ages \(A,A'\), the rank-one trace identity yields
\[
 P_N=\mathbb E|\langle\psi(A)|\psi(A')\rangle|^{2N}
 =\mathbb E\cos^{2N}(\Omega(A-A')).
\]
The trigonometric-binomial identity
\[
 \cos^{2N}z=4^{-N}\sum_{k=-N}^{N}{2N\choose N+k}e^{2ikz}
\]
and independence of \(A,A'\) give the claimed exact finite-\(N\) purity, where \(m_k=\mathbb E[e^{2ik\Omega A}]\). For every \(k\ne0\), Tonelli/Fubini applied to the equilibrium age yields
\[
 \mathbb E[e^{2ik\Omega A}]
 =\frac1\mu\mathbb E\!\left[\int_0^T e^{2ik\Omega a}\,da\right]
 =\frac{\mathbb E[e^{2ik\Omega T}]-1}{2ik\Omega\mu}.
\]

**Step 2 (thermodynamic scaling).** As \(|\mathbb E[e^{2ik\Omega T}]-1|\le2\), we have \(|m_k|\le1/(|k|\Omega\mu)\). Therefore \(\sum_{k\in\mathbb Z}|m_k|^2<\infty\). Let \(b_N=4^{-N}{2N\choose N}\); for each fixed integer \(k\), \({2N\choose N+k}/{2N\choose N}\to1\), and this ratio is between zero and one. Dominated convergence for the absolutely summable Fourier-square sequence implies \(P_N/b_N\to\sum_{k\in\mathbb Z}|m_k|^2\). The central binomial estimate \(\sqrt{\pi N}b_N\to1\) finishes the asymptotic and the Rényi-entropy formula. Periodizing \(w\) gives the stated \(g\); its Fourier coefficients are \(m_k\). It satisfies \(\int_0^\tau g=1\) and \(g(a)\le1/\mu+1/\tau\) by monotonicity of the survival function and an integral comparison. Thus Parseval gives \(\sum|m_k|^2=\tau\int g^2\); Cauchy–Schwarz gives \(\mathcal A\ge1\).

**Step 3 (exact optimizer characterization).** Every finite-\(N\) coefficient in the exact formula is positive. Equality with \(b_N\) requires \(m_1=0\), equivalently \(\mathbb E e^{2i\Omega T}=1\). A unit-modulus complex random variable has expectation one only when it equals one almost surely. Hence \(e^{2i\Omega T}=1\) almost surely, or \(T\in\tau\mathbb N\) almost surely (strictly positive reset times). Conversely such clocks give \(m_k=0\) for all nonzero \(k\), proving equality for every \(N\) and \(\mathcal A=1\). The same characterization follows for \(\mathcal A=1\), because all its nonnegative Fourier-square terms must vanish. Any clock supported on \(\tau\mathbb N\) has mean at least \(\tau\). Conversely, for any prescribed \(\mu\ge\tau\), mixing the adjacent positive multiples \(j\tau,(j+1)\tau\) bracketing \(\mu\) realizes that mean and all equalities (at an exact multiple use a point mass).

**Step 4 (sharp unattained infimum below a period).** Fix \(0<\mu<\tau\). For \(0<\epsilon<\mu\), let \(T_\epsilon=\epsilon\) with probability \(1-p_\epsilon\) and \(T_\epsilon=\tau\) with probability
\[
 p_\epsilon=\frac{\mu-\epsilon}{\tau-\epsilon}\in(0,1).
\]
Then \(\mathbb ET_\epsilon=\mu\), while for each nonzero \(k\),
\[
 m_k(T_\epsilon)=\frac{(1-p_\epsilon)(e^{2ik\Omega\epsilon}-1)}{2ik\Omega\mu}\longrightarrow0.
\]
The uniform \(O(1/|k|)\) bound from Step 2 permits dominated convergence for \(\mathcal A(T_\epsilon)\to1\), and the finite sum gives \(P_N(T_\epsilon)\to b_N\) for each \(N\). By Step 3 neither infimum is attained, proving the claimed sharp attainment transition. Equivalently the equilibrium phase density has two levels, \(1/\mu\) for \(0<a<\epsilon\) and \(p_\epsilon/\mu\) for \(\epsilon<a<\tau\), converging in \(L^2\) to the uniform density \(1/\tau\).

**Step 5 (Poisson constant).** For exponential intervals \(T\) of rate \(r\), the stationary age is exponential of rate \(r\), so \(|m_k|^2=r^2/(r^2+4k^2\Omega^2)\). The classical partial-fraction identity \(\sum_{k\in\mathbb Z}(k^2+x^2)^{-1}=\pi\coth(\pi x)/x\), with \(x=r/(2\Omega)\), gives the displayed \(\mathcal A\) and therefore the explicit purity asymptotic.

## Verification
`verify.py` is a standalone Python 3 checker requiring only the standard library. It tests finite-\(N\) Fourier purity against independent two-dimensional midpoint quadrature for a deterministic reset clock, the exact resonant lower bound, the fixed-mean two-point approximation of nonattained infima, convergence of the universal \(\sqrt{N}\) coefficient for Poisson clocks, the Poisson hyperbolic cotangent summation, and a direct Parseval calculation for two-point clocks. Those are finite deterministic checks, not proofs of the all-\(N\) or all-renewal statements.

## Relationship to prior work
Magoni, Carollo, Perfetto and Lesanovsky (arXiv:2202.12655, first posted February 25, 2022) study the same noninteracting globally reset Rabi-spin model, with an exponential reset clock in their unconditional protocol; they establish induced two-spin correlations, not a general-clock many-body purity scaling/optimization theorem. Sevilla and Valdés-Hernández (arXiv:2209.05643v1, September 12, 2022), especially Sec. 3.3 and Eq. (42), establish a **more general stationary quantum-purity spectral formula for arbitrary resetting**. The finite-\(N\) identity here is an explicit specialization of that established principle rather than a newly discovered general renewal formula. The assessed added claims are the exact thermodynamic \(N^{-1/2}\) prefactor for arbitrary finite-mean clocks, the corresponding subextensive Rényi law, and the sharp fixed-mean attainable/unattainable optimizer classification. Wald et al. (arXiv:2410.11497v1, October 15, 2024) discuss resonance and correlations for discrete-time, few-qubit resets, not this continuous-time global purity phase diagram.

## Limitations
The fixed-mean short-interval approximating sequence converges to the optimum for each fixed population size; no uniform-in-population approximation rate is asserted. The theorem concerns the stationary equilibrium-renewal ensemble. For deterministic or lattice clocks, a process initialized with all spins synchronized at a reset may remain periodic; no ordinary pointwise convergence from that initialization is asserted. The infimum below one Rabi period exploits arbitrarily short positive resetting intervals and need not persist with a hardware-imposed lower cutoff. The result is not an entanglement claim and does not cover interacting spins, heterogeneous local Rabi frequencies, independent per-spin clocks, or measurements of a single random trajectory. The general stationary renewal equation and spectral purity identity are established in the cited literature, and an unindexed direct thermodynamic or optimization analysis could diminish publication priority.

## References
1. M. Magoni, F. Carollo, G. Perfetto and I. Lesanovsky, *Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting*, arXiv:2202.12655 (first posted 2022-02-25), https://arxiv.org/abs/2202.12655 .
2. F. J. Sevilla and A. Valdés-Hernández, *Dynamics of closed quantum systems under stochastic resetting*, arXiv:2209.05643v1 (first posted 2022-09-12), https://arxiv.org/html/2209.05643v1 .
3. S. Wald, L. H. Yao, T. Platini, C. Hooley and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497v1 (first posted 2024-10-15), https://arxiv.org/html/2410.11497v3 .
