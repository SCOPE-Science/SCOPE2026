# Asymmetry-blind Bell thresholds and opposing concurrence order under Poisson reinitialization

## Finding

Consider two noninteracting qubits, each subject to independent zero-temperature amplitude damping, jointly reinitialized at Poisson times into the Bell state \(\lvert\Phi^+\rangle=(\lvert00\rangle+\lvert11\rangle)/\sqrt2\). The decay rates may be unequal or one may vanish. At fixed total decay rate, the entire stationary CHSH-violation threshold is **independent of the allocation of decay between the qubits**, even though the stationary concurrence is strictly sensitive to that allocation. There is an exact, complementary ordering of these two diagnostics before nonlocality appears.

Precisely, let \(\gamma_1,\gamma_2\ge0\), \(S=\gamma_1+\gamma_2>0\), \(Q=\gamma_1\gamma_2\in[0,S^2/4]\), and let \(r>0\) be the joint reinitialization rate. Write \(B(r,S,Q)\) for the maximal unconditional stationary CHSH value and \(C(r,S,Q)\) for Wootters concurrence, without filtering or postselection. Define
\[
 t=\frac{2r}{2r+S},\qquad
 v=\frac{r^3+Sr^2+Q(S+3r)}{(r+S)(r^2+Sr+Q)}.
\]
Then
\[
 \boxed{B(r,S,Q)=2\sqrt{t^2+\max\{t^2,v^2\}}},\qquad
 \boxed{C(r,S,Q)=t-\frac{r\sqrt Q}{(r+S)\sqrt{r^2+Sr+Q}}>0}.
\]
The Bell threshold is sharp and **asymmetry-blind**:
\[
 \boxed{B(r,S,Q)>2\quad\Longleftrightarrow\quad r>\frac{1+\sqrt2}{2}S,\qquad 0\le Q\le\frac{S^2}{4}.}
\]
At equality in the rate, \(B=2\); below it, \(B<2\). More strongly, whenever \(r\ge S\), the complete optimized CHSH value, not merely its violation status, is
\[
 \boxed{B(r,S,Q)=\frac{4\sqrt2\,r}{2r+S},}
\]
independent of \(Q\), whereas \(C(r,S,Q)\) decreases strictly in \(Q\). Thus, at a fixed total loss, more unequal local loss increases concurrence without changing any optimized CHSH statistic in this rate range.

For every \(0<r<S\), there is a unique witness-switch product
\[
 \boxed{Q_c(r,S)=\frac{Sr^2(S+r)}{S^2+3Sr+4r^2}\in(0,S^2/4).}
\]
If \(Q\le Q_c\), then \(v\le t\) and \(B=2\sqrt2\,t\) is independent of \(Q\). If \(Q>Q_c\), then \(v>t\) and \(B=2\sqrt{t^2+v^2}\) increases strictly with \(Q\), **while concurrence decreases strictly** throughout the admissible interval. The switch product grows strictly with \(r\), reaching \(S^2/4\) at \(r=S\). This constitutes the complete ordering of optimized Bell correlations and concurrence with respect to loss asymmetry.

An exact comparison: for \(S=2\) and \(r=1\), concentrating all decay on one qubit (\(Q=0\)) gives \((B,C)=(\sqrt2,1/2)\); equal rates (\(Q=1\)) give \((B,C)=(5/3,1/3)\). At \(r=3\), both allocations instead give \(B=3\sqrt2/2>2\), but their concurrences remain different, \(3/4\) and \(3/5\) respectively.

## Assumptions and scope

The basis is \((\lvert00\rangle,\lvert01\rangle,\lvert10\rangle,\lvert11\rangle)\), with \(\sigma_-\lvert1\rangle=\lvert0\rangle\) and \(\sigma_-\lvert0\rangle=0\). Between complete, instantaneous, state-independent reset events, the density matrix evolves according to
\[
 \mathcal L_0(\rho)=\sum_{j=1}^2\gamma_j\left(\sigma_-^{(j)}\rho\sigma_+^{(j)}-\tfrac12\{\sigma_+^{(j)}\sigma_-^{(j)},\rho\}\right).
\]
The only coupling between the qubits is their **shared reset event**, returning the full joint density matrix to \(\rho_0=\lvert\Phi^+\rangle\langle\Phi^+\rvert\). No Hamiltonian, excitation, extra dephasing, finite-temperature bath, measurement feedback, or postselection acts between resets. The CHSH value maximizes over all pairs of local dichotomic projective measurements on the unconditional stationary state. The theorem applies to all real parameters \(\gamma_j\ge0\), \(S>0\), and \(r>0\), including both one-sided-loss endpoints; it does not include the fully lossless case \(S=0\).

## Proof

**Stationary density.** Joint Poisson resetting makes the stationary state unique and regenerative:
\[
 \bar\rho=r\int_0^\infty e^{-rt}e^{t\mathcal L_0}(\rho_0)\,dt.
\]
The unreset Bell coherence is \(\rho_{00,11}(t)=e^{-St/2}/2\), the double-excitation population is \(\rho_{11,11}(t)=e^{-St}/2\), and the singly excited populations are
\[
 \rho_{01,01}(t)=\tfrac12e^{-\gamma_2t}(1-e^{-\gamma_1t}),\quad
 \rho_{10,10}(t)=\tfrac12e^{-\gamma_1t}(1-e^{-\gamma_2t}).
\]
Consequently \(\bar\rho\) is a real X-state with diagonal entries \((1-p_{01}-p_{10}-p_{11},p_{01},p_{10},p_{11})\) and only off-diagonal entries \(\bar\rho_{00,11}=\bar\rho_{11,00}=c\), where
\[
 c=\frac{r}{2(r+S/2)},\quad p_{11}=\frac r{2(r+S)},\quad
 p_{01}=\frac r2\left(\frac1{r+\gamma_2}-\frac1{r+S}\right),\quad
 p_{10}=\frac r2\left(\frac1{r+\gamma_1}-\frac1{r+S}\right).
\]
This representation proves normalization, positivity and uniqueness directly, including the vanishing-loss endpoint.

**Correlations and concurrence.** The real Pauli correlation matrix is \(T=\operatorname{diag}(2c,-2c,1-2(p_{01}+p_{10}))=\operatorname{diag}(t,-t,v)\). The Horodecki two-qubit CHSH criterion gives the displayed closed form for \(B\); \(v>0\) follows from its explicit rational numerator. The X-state concurrence is \(2\max\{0,c-\sqrt{p_{01}p_{10}}\}\), since the other spin-flip candidate is nonpositive. Using
\[
 p_{01}p_{10}=\frac{r^2Q}{4(r+S)^2(r^2+Sr+Q)}
\]
gives the asserted formula for \(C\). It is strictly positive because \(\sqrt{Q/(r^2+Sr+Q)}<1\) and \(r/(r+S)<2r/(2r+S)\). At fixed \(r,S\), the function \(\sqrt{Q/(r^2+Sr+Q)}\) is strictly increasing in \(Q\ge0\); hence concurrence is strictly decreasing throughout \([0,S^2/4]\).

**Exact witness branch.** Subtraction and cancellation yield
\[
 v-t=\frac{(S^2+3Sr+4r^2)Q-Sr^2(S+r)}{(S+r)(S+2r)(r^2+Sr+Q)}.
\]
Every denominator is positive, so the sign changes precisely at \(Q=Q_c(r,S)\). At fixed \(r,S\), \(v\) is strictly increasing in \(Q\) because
\[
 v=1-\frac{r(2r+S)}{r^2+Sr+Q}+\frac{2r}{r+S}.
\]
Using \(x=r/S\), the normalized threshold is \(Q_c/S^2=x^2(1+x)/(1+3x+4x^2)\); direct differentiation gives \(2x(2x+1)(x^2+x+1)/(4x^2+3x+1)^2>0\) for every \(x>0\). In particular \(Q_c(S,S)=S^2/4\), and for \(r\ge S\) one has \(Q_c(r,S)\ge S^2/4\), proving the complete CHSH invariance in the high-reset regime. For \(r<S\), \(0<Q_c<S^2/4\), and the two asserted monotonic branches follow.

**Sharp nonlocality threshold.** Since \(t,v>0\), CHSH violation is equivalent to either \(2t^2>1\) or \(t^2+v^2>1\). The first condition is \(r>(1+\sqrt2)S/2\). For \(0<r\le S\), \(v\) is maximal at \(Q=S^2/4\), where
\[
 v_{\mathrm{bal}}=\frac{S^2+Sr+2r^2}{(S+r)(S+2r)},\qquad
 1-t^2-v_{\mathrm{bal}}^2=\frac{4r(S^3+S^2r-r^3)}{(S+r)^2(S+2r)^2}>0.
\]
The last numerator is positive because \(r^3\le S^2r\) for \(r\le S\); hence both possible CHSH branches are strictly below their threshold there. For \(S<r\le (1+\sqrt2)S/2\), the proved witness ordering gives \(v\le t\), so \(B=2\sqrt2t\le2\). For larger \(r\), the same formula is strictly greater than two. This proves the claimed if-and-only-if, including both equality and strict-boundary cases.

**Concrete diagnostic separation.** At \(S=2,r=1\), \(t=1/2\), \(v(Q=0)=1/3\) and \(v(Q=1)=2/3\); substitution gives \((B,C)=(\sqrt2,1/2)\) versus \((5/3,1/3)\). At \(S=2,r=3\), \(t=3/4\); the high-reset branch yields \(B=3\sqrt2/2\), while the concurrence formula gives \(3/4\) and \(3/5\) for the two endpoints. The distinction is exact rather than numerical or asymptotic.

## Verification

The standalone `checker.py` runs with NumPy and SymPy. It checks the rational identities symbolically, reconstructs the full stationary four-by-four state by independently solving the 16-dimensional Lindblad-resolvent linear system for 187 pairs of damping rates and five reset rates each, reconstructs all nine Pauli correlations, verifies the optimized CHSH value using singular values, evaluates concurrence by the spin-flip eigenvalue formula, and tests the universal threshold and limiting cases. Additional dense parameter grids include one-sided loss, the equal-loss case, both sides of the critical reset rate and the boundary itself. The program passed 6,895 assertions. Analytical uniqueness, all-parameter monotonicity and global inequalities are proved above, not inferred from the finite checks.

To reproduce: execute `python checker.py` with Python 3, NumPy and SymPy installed. No network access or external data are required.

## Relationship to prior work

Kulkarni and Majumdar (arXiv:2307.07485, first posted 14 July 2023) introduce Poisson reinitialization of interacting **closed** quantum systems, including a two-spin concurrence calculation, but do not give this locally damped asymmetric-Bell-reset classification. Carollo, Lesanovsky and Garrahan (arXiv:2310.06981, first posted 10 October 2023) develop reset quantum-jump statistics in **open** systems, not optimized CHSH ordering by unequal local losses. Wald and collaborators (arXiv:2410.11497, first posted 15 October 2024) analyze reset-induced correlations for **discrete unitary gates**, not independent asymmetric amplitude-damping baths.

A publicly available result titled *A sharp Bell-nonlocality phase boundary under Poisson Bell-pair reinitialization and local decoherence* proves an exact threshold in the **equal-damping** case, with optional symmetric dephasing (https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-bell-nonlocality-phase-boundary-under-poisson-bell-pair--2d77b15719bb). Its zero-dephasing case reproduces the equal-loss specialization \(r_c=(1+\sqrt2)S/2\), which is **not** claimed as new here. The present claim instead proves that this same threshold survives **every asymmetric split**, and classifies the strict opposition of concurrence and Bell-response orders and the exact witness-switch locus. Those assertions do not follow from the symmetric statement alone. The Horodecki and Wootters criteria are standard tools and are not original contributions.

## Limitations

The result does not imply that all quantum correlations or density-matrix elements are insensitive to loss asymmetry: in fact concurrence and single-qubit populations detect it. The full CHSH value is independent of asymmetry only for \(r\ge S\); for \(0<r<S\) it generally depends on the split. The model assumes ideal simultaneous reinitialization, no Hamiltonian, zero-temperature local loss, no additional dephasing, and independent Markovian baths. It makes no claim about general non-Markovian resetting, finite-temperature pumping, detector inefficiency, steering, Bell inequalities beyond optimized projective CHSH, filtering, or experimental noise. A more general existing channel treatment might implicitly imply the result; independent validation and publication-priority certification have not been performed.

## References

- M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485, first posted 2023-07-14, https://arxiv.org/abs/2307.07485.
- F. Carollo, I. Lesanovsky and J. P. Garrahan, *Universal and nonuniversal probability laws in Markovian open quantum dynamics subject to generalized reset processes*, arXiv:2310.06981, first posted 2023-10-10, https://arxiv.org/html/2310.06981.
- S. Wald et al., *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497, first posted 2024-10-15, https://arxiv.org/html/2410.11497.
- *A sharp Bell-nonlocality phase boundary under Poisson Bell-pair reinitialization and local decoherence*, published online, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-bell-nonlocality-phase-boundary-under-poisson-bell-pair--2d77b15719bb.
- R. Horodecki, P. Horodecki and M. Horodecki, *Violating Bell inequality by mixed spin-1/2 states: necessary and sufficient condition*, Phys. Lett. A 200 (1995), https://doi.org/10.1016/0375-9601(95)00214-N.
- W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, Phys. Rev. Lett. 80 (1998), https://doi.org/10.1103/PhysRevLett.80.2245.
