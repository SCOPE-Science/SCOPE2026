# Exact capture times and dephasing optima for a lossy quantum cone

## Finding
For each integer \(n\ge2\), consider a quantum network consisting of one absorbing hub and \(n\) mutually equivalent leaves. Hub–leaf edges have hopping \(g\ne0\); every distinct pair of leaves has hopping \(h\), including \(h=0\) for the ordinary star. An excitation initially at any single leaf is absorbed with probability one whenever independent leaf-site dephasing acts at any rate \(\delta>0\). Its exact mean capture time is
\[
T=\frac{n+1}{\kappa}+\frac{n-1}{\delta}
+\frac{\kappa+\delta}{4g^2}
+\frac{[\varepsilon-(n-1)h]^2}{g^2(\kappa+\delta)}.
\]
Here \(\kappa>0\) is the population-removal rate at the hub and \(\varepsilon\) is the hub onsite energy relative to the leaves.

For each fixed \(\kappa>0\), \(T\) is strictly convex in \(\delta>0\), diverges at both endpoints, and has one optimum. Writing \(\Delta=\varepsilon-(n-1)h\), its unique minimizing value solves
\[
\frac{1}{4g^2}=\frac{n-1}{\delta_*^2}
+\frac{\Delta^2}{g^2(\kappa+\delta_*)^2}.
\]
At the hub–bright-leaf resonance \(\Delta=0\), this simplifies to \(\delta_*=2|g|\sqrt{n-1}\), independent of the sink rate. If the sink rate is also free, the resonant global optimum is
\[
\kappa_*=2|g|\sqrt{n+1},\quad
\delta_*=2|g|\sqrt{n-1},\quad
T_{\min}=\frac{\sqrt{n+1}+\sqrt{n-1}}{|g|}.
\]
In contrast, at \(\delta=0\), a localized leaf carries nondecaying dark-state mass \(1-1/n\) and is not eventually absorbed with probability one. The limit \(\delta\downarrow0\) is singular in infinite-time absorption and in the mean.

## Assumptions and scope
The single-excitation Hilbert space has orthonormal basis \(\{|0\rangle,|1\rangle,\ldots,|n\rangle\}\), with hub \(0\). Set \(P_j=|j\rangle\langle j|\) and \(\hbar=1\). The Hermitian Hamiltonian is
\[
H=\varepsilon P_0+g\sum_{j=1}^n(|0\rangle\langle j|+|j\rangle\langle0|)+h\sum_{\substack{j,k=1\\j\ne k}}^n|j\rangle\langle k|.
\]
For \(\kappa,\delta>0\), the unnormalized density matrix evolves via the completely positive, trace-decreasing generator
\[
\mathcal L(\rho)=-i[H,\rho]-\frac{\kappa}{2}\{P_0,\rho\}
+\delta\sum_{j=1}^n\left(P_j\rho P_j-\frac12\{P_j,\rho\}\right).
\]
In particular, dephasing acts on leaves only, so a hub–leaf coherence decays at rate \(\delta/2\) from dephasing and a leaf–leaf coherence at rate \(\delta\). Absorption removes hub population at rate \(\kappa\), not amplitude at that rate. For any chosen leaf \(j\), \(\rho(0)=P_j\), survival is \(S(t)=\operatorname{tr}\rho(t)\), and the **unconditional mean** absorption time is \(T=\int_0^\infty S(t)\,dt\); this is not the median time or the time to a fixed threshold. There is no additional spontaneous recombination, reset, hopping disorder, or dephasing at the hub. The signs of real \(g,h\) are unrestricted when \(g\ne0\).

## Proof
**1. Full absorption and convergence of integrals.** The loss identity is \(S'(t)=-\kappa\rho_{00}(t)\le0\). The generator is completely positive and trace nonincreasing. Suppose a normalized positive initial state has a strictly positive limiting survival probability. Finite-dimensional compactness yields a nonzero positive accumulation point \(\sigma\) on whose forward trajectory survival is constant. Positivity and the loss identity imply the entire hub row and column vanish on this trajectory. The hub–leaf equations then force the leaf block \(M(t)\) to annihilate the vector \(s=(1,\ldots,1)^\mathsf T\) for every time: \(M(t)s=0\). Hermiticity also gives \(s^\mathsf TM(t)=0\); consequently the leaf Hamiltonian \(h(ss^\mathsf T-I)\) commutes with \(M(t)\). The remaining leaf evolution is pure dephasing:
\[
M(t)=\operatorname{diag}M(0)+e^{-\delta t}(M(0)-\operatorname{diag}M(0)).
\]
From \(M(t)s=0\) for all times, comparison of constant and exponential terms gives \(\operatorname{diag}M(0)=0\); positivity forces \(M(0)=0\), contradicting \(\sigma\ne0\). Thus all initial states decay to zero in trace. The finite-dimensional generator has no stationary nondecaying modes; a positive trace-preserving dilation together with compactness excludes peripheral spectral values. Hence its spectral abscissa is strictly negative and the moment integrals below converge.

**2. Symmetric reduction.** A permutation of leaves leaves the generator unchanged. The integrated survival is therefore identical for every localized leaf, and may be computed from the equally weighted mixture \(\rho(0)=\tfrac1n\sum_{j=1}^nP_j\). Write the hub population as \(a(t)=\rho_{00}(t)\); the common leaf population as \(b(t)=\rho_{jj}(t)\); the common off-diagonal leaf coherence as \(c(t)=\rho_{jk}(t)\) for distinct leaves; and \(\rho_{0j}(t)=x(t)+iy(t)\). Hermiticity and permutation symmetry make \(a,b,c,x,y\) real. With \(q=(\kappa+\delta)/2\) and \(\Delta=\varepsilon-(n-1)h\), direct substitution into the stated generator gives
\[
\begin{aligned}
\dot a&=-\kappa a-2gn y,& \dot b&=2g y,\\
\dot c&=2g y-\delta c,& \dot x&=\Delta y-qx,\\
\dot y&=-\Delta x-qy-g\bigl(b+(n-1)c-a\bigr).
\end{aligned}
\]
Initially \(b(0)=1/n\) while \(a(0)=c(0)=x(0)=y(0)=0\).

**3. Integrated solution.** Denote time integrals of these five quantities by \(A,B,C,X,Y\). The vanishing boundary terms of the equations for \(a,b,c,x\) yield
\[
Y=-\frac{1}{2gn},\quad A=\frac1\kappa,\quad
C=-\frac1{n\delta},\quad X=\frac{\Delta}{q}Y.
\]
The integral of the last equation then yields
\[
B=A-(n-1)C-\frac{\Delta X+qY}{g}
=\frac1\kappa+\frac{n-1}{n\delta}
+\frac{\kappa+\delta}{4g^2n}
+\frac{\Delta^2}{g^2n(\kappa+\delta)}.
\]
Because \(S(t)=a(t)+nb(t)\), integration gives \(T=A+nB\), exactly the announced formula. The use of the symmetric mixture proves the same formula for **each individual localized leaf** by linearity and permutation invariance.

**4. Optimization and endpoint.** Differentiating at fixed \(\kappa\) gives
\[
\frac{\partial T}{\partial\delta}=-\frac{n-1}{\delta^2}
+\frac{1}{4g^2}-\frac{\Delta^2}{g^2(\kappa+\delta)^2},\qquad
\frac{\partial^2T}{\partial\delta^2}=\frac{2(n-1)}{\delta^3}
+\frac{2\Delta^2}{g^2(\kappa+\delta)^3}>0.
\]
The derivative changes from negative to positive, hence the unique optimum; at \(\Delta=0\) it has the stated elementary value. At resonance the two remaining variable pieces, \((n+1)/\kappa+\kappa/(4g^2)\) and \((n-1)/\delta+\delta/(4g^2)\), minimize separately, proving the joint optimum. For \(\delta=0\), the Hamiltonian leaves invariant the \((n-1)\)-dimensional leaf subspace orthogonal to \(s\); the squared projection of a localized leaf onto it is \(1-1/n\). Its complement couples to the absorbing hub and decays, completing the endpoint statement.

## Verification
The accompanying `verify.py` constructs the full complex Liouvillian directly from matrix units, independently of the five-real-variable reduction, solves \(-\mathcal L X=\rho(0)\), and compares \(\operatorname{tr}X\) against the formula for distinct localized leaves. It also numerically checks strict spectral decay and the resonance/detuning optimization conditions. Execute `python verify.py` with NumPy and SciPy installed. A representative completed run reports `VERIFY_OK lindblad_inverse_cases=40 optimization_checks=8 max_abs_error=7.11e-14 max_real_eigenvalue=-0.0297`. Computations are finite cross-checks; the proof above covers all allowed \(n\) and continuous parameter ranges.

## Relationship to prior work
Noise-assisted quantum transport, dark subspaces, and the opposing weak-dephasing and quantum-Zeno regimes are established in Rebentrost et al. [1] and Novo et al. [2]. Pepe, Pouthier and Yalouz [3] study a **different extended-star network** under dephasing with a median-absorption-time observable; their analytic approximation is based on incoherent rates and need not apply uniformly to the weak-dephasing regime. Alterman, Berman and Strauch [4] develop exact transfer-rate expressions and optimal noise for a **uniform complete graph** with dephasing on every vertex including the sink and a different population-loss convention. In particular, their printed equations (42)–(49) already establish closely related optimization mechanisms and are not asserted to be new here. The present evaluated quantity instead concerns the two independent coherent couplings \(g,h\) **and selective leaf-only dephasing**, with exact mean absorption times for all positive dephasing strengths. Pouthier [5] addresses fluctuating-bath coherences on a star; a complete copy could not be inspected, so an equivalent specialized result there has not been excluded.

## Limitations
Exactness holds for the specified homogeneous finite cone with independent identical leaf dephasers, a completely un-dephased sink, and localized leaf starts. Neither nonidentical leaf energies/rates nor multi-trap, correlated noise, many-particle, or finite-time mixing claims are proved. The mean time diverges at zero dephasing although the zero-dephasing capture probability is \(1/n\). The full text of [5] remains a publication-priority uncertainty, and even thorough literature comparisons do not establish global priority. Independent review has not been performed.

## References
[1] P. Rebentrost et al., *Environment-Assisted Quantum Transport*, arXiv:0807.0929 (first posted 2008-07-07), https://arxiv.org/abs/0807.0929.

[2] L. Novo, M. Mohseni, Y. Omar, *Disorder-assisted quantum transport in suboptimal decoherence regimes*, arXiv:1312.6989; *Scientific Reports* **6**, 18142 (2016), https://www.nature.com/articles/srep18142.

[3] L. Pepe, V. Pouthier, S. Yalouz, *Optimized excitonic transport mediated by local energy defects: survival of optimization laws in the presence of dephasing*, arXiv:2308.15857 (2023), https://arxiv.org/abs/2308.15857.

[4] S. Alterman, J. Berman, F. W. Strauch, *Optimal Conditions for Environment-Assisted Quantum Transport on the Fully Connected Network*, arXiv:2309.00164 (2023); *Physical Review E* **109**, 014310 (2024), https://arxiv.org/abs/2309.00164.

[5] V. Pouthier, *The excitonic qubit on a star graph: dephasing-limited coherent motion*, *Quantum Information Processing* **14**, 491–509 (2015), https://doi.org/10.1007/s11128-014-0891-y.
