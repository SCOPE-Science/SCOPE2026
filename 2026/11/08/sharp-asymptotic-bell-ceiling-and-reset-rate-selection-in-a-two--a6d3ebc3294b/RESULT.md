# Sharp asymptotic Bell ceiling and reset-rate selection in a two-spin Ising model

## Finding

For the two-qubit ferromagnetic transverse-field Ising Hamiltonian
\[
H=-J\sigma_z\otimes\sigma_z+\frac{\Omega}{2}(\sigma_x\otimes I+I\otimes\sigma_x),\qquad J,\Omega>0,
\]
subject to independent Poisson reinitializations of the *whole two-spin state* to \(|\downarrow\downarrow\rangle\) at rate \(r>0\), let \(\rho_{J,\Omega,r}\) be its ensemble-averaged stationary density matrix. Let \(\mathcal B(\rho)\) be the maximum absolute Clauser–Horne–Shimony–Holt (CHSH) expectation over two projective dichotomic observables on each qubit (local-hidden-variable threshold \(2\)). Set
\[
j=J/\Omega,\quad q=r/\Omega,\quad \delta_j=\sqrt{j^2+1}-j,\quad \kappa=q/\delta_j.
\]
There is a **uniform-in-reset-rate** strong-interaction approximation
\[
\left|\mathcal B(\rho_{J,\Omega,r})-2\sqrt{1+\left(\frac{\kappa}{1+\kappa^2}\right)^2}\right|
\le 4\sqrt2\,\sqrt{1-\frac{j}{\sqrt{j^2+1}}}.
\]
Consequently, as \(j\to\infty\),
\[
\sup_{r>0}\mathcal B(\rho_{J,\Omega,r})=\sqrt5+O(j^{-1}).
\]
For all sufficiently large \(j\), at least one positive maximizing reset rate exists; **every** such maximizing choice satisfies
\[
\frac{r_*(j)}{\Omega\delta_j}\longrightarrow1,
\qquad r_*(j)\sim\frac{\Omega^2}{2J}.
\]
At the distinguished scaling \(r=\Omega\delta_j\), the CHSH value tends to \(\sqrt5>2\), even though the reset rate itself tends to zero. Conversely, for every **fixed finite** \(j>0\), the weak-reset limit is CHSH-local:
\[
\lim_{q\downarrow0}\mathcal B(\rho_{j,q})=
\frac{\sqrt{(2j^2+1)^2+1}}{j^2+1}<2.
\]
These are coupled parts of one claim: an asymptotically optimal, vanishing-rate Bell-nonlocality ridge, distinct from the fixed-coupling weak-reset limit. The bound is on the maximal two-qubit CHSH expression, **not** a universal upper bound over arbitrary two-qubit states.

## Assumptions and scope

Time is scaled by \(\Omega^{-1}\); hence the dimensionless Hamiltonian is
\[
h_j=-j\sigma_z\otimes\sigma_z+\tfrac12(\sigma_x\otimes I+I\otimes\sigma_x).
\]
At positive dimensionless reset rate \(q\), independent exponential waiting times produce the unique stationary age mixture
\[
\rho_{j,q}=q\int_0^\infty e^{-qt}e^{-ih_jt}|\downarrow\downarrow\rangle\langle\downarrow\downarrow|e^{ih_jt}\,dt.
\]
The construction makes no claim about trajectory-wise Bell tests before averaging, arbitrary reset states, collective many-spin Bell inequalities, detector loopholes, or other quantum dynamics. The uniform error estimate concerns \(j>0\) and \(q>0\); its right-hand side is useful in the strong-coupling limit.

## Proof

**1. Exact three-dimensional invariant subspace.** Put
\[
|B\rangle=\frac{|\uparrow\uparrow\rangle+|\downarrow\downarrow\rangle}{\sqrt2},\quad
|A\rangle=\frac{|\uparrow\uparrow\rangle-|\downarrow\downarrow\rangle}{\sqrt2},\quad
|S\rangle=\frac{|\uparrow\downarrow\rangle+|\downarrow\uparrow\rangle}{\sqrt2}.
\]
The antisymmetric middle-spin vector is unoccupied. Direct application of \(h_j\) gives \(h_j|A\rangle=-j|A\rangle\), while on the ordered basis \((|B\rangle,|S\rangle)\),
\[
h_j\big|_{\{B,S\}}=\begin{pmatrix}-j&1\\1&j\end{pmatrix}.
\]
Its eigenvalues are \(\pm\omega_j\), where \(\omega_j=\sqrt{j^2+1}\). Write \(|L\rangle=\cos\theta_j|B\rangle-\sin\theta_j|S\rangle\) for the negative-energy eigenvector and \(|H\rangle=\sin\theta_j|B\rangle+\cos\theta_j|S\rangle\) for the positive-energy eigenvector. Here
\[
\sin^2\theta_j=\frac{1-j/\omega_j}{2},\qquad 0<\theta_j<\pi/4.
\]
As \(|\downarrow\downarrow\rangle=(|B\rangle-|A\rangle)/\sqrt2\), the exact unreset wave function differs from
\[
|\phi_j(t)\rangle=e^{ijt}\frac{e^{i\delta_jt}|B\rangle-|A\rangle}{\sqrt2}
\]
by a vector of norm at most \(\sqrt2\sin\theta_j\), **uniformly in time**. Indeed, the difference is exactly \(\sin\theta_j(e^{-i\omega_jt}-e^{i\omega_jt})|H\rangle/\sqrt2\). This bound uses the exact spectral decomposition and makes no long-time perturbation expansion.

**2. Uniform comparison after Poisson averaging.** For normalized vectors, the trace distance between their rank-one projectors is at most twice their vector distance. Integrating with the probability density \(qe^{-qt}\) therefore shows that, uniformly over every \(q>0\),
\[
\|\rho_{j,q}-\Sigma_{q/\delta_j}\|_1
\le 2\sqrt2\sin\theta_j
=2\sqrt{1-j/\omega_j},
\]
where the explicit effective state \(\Sigma_\kappa\) is computed next. The norm bound is independent of the observation time and of the reset rate.

**3. Effective density matrix and CHSH diagnostic.** Dropping the irrelevant common phase from \(|\phi_j(t)\rangle\), integrate its outer product against \(qe^{-qt}\). In the four-dimensional computational basis \((|\uparrow\uparrow\rangle,|\uparrow\downarrow\rangle,|\downarrow\uparrow\rangle,|\downarrow\downarrow\rangle)\), the only nonzero entries of \(\Sigma_\kappa\) are
\[
(\Sigma_\kappa)_{11}=\frac{1}{2(1+\kappa^2)},\quad
(\Sigma_\kappa)_{44}=\frac{1+2\kappa^2}{2(1+\kappa^2)},\quad
(\Sigma_\kappa)_{14}=\frac{i\kappa}{2(1+\kappa^2)},\quad
(\Sigma_\kappa)_{41}=\overline{(\Sigma_\kappa)_{14}}.
\]
For \(T_{ab}=\operatorname{tr}[\Sigma_\kappa(\sigma_a\otimes\sigma_b)]\), \(a,b\in\{x,y,z\}\), direct multiplication gives
\[
T=\begin{pmatrix}0&-h&0\\-h&0&0\\0&0&1\end{pmatrix},\qquad
h=\frac{\kappa}{1+\kappa^2}.
\]
Its squared singular values are \(1,h^2,h^2\). The Horodecki CHSH criterion then gives
\[
\mathcal B(\Sigma_\kappa)=2\sqrt{1+h^2}.
\]
The CHSH operator has norm at most \(2\sqrt2\) for all local dichotomic observables. The variational definition implies
\[
|\mathcal B(\rho)-\mathcal B(\sigma)|\le2\sqrt2\|\rho-\sigma\|_1.
\]
Combining this inequality with the previous uniform trace-distance estimate proves the displayed error bound.

**4. Sharp optimization, including maximizer location.** The function \(h=\kappa/(1+\kappa^2)\) has its unique global maximum \(1/2\) at \(\kappa=1\), and tends to zero at both endpoints of \((0,\infty)\). Thus the limiting Bell profile has unique maximum \(\sqrt5\). Uniform convergence of the actual Bell profiles gives the asymptotic supremum. Moreover, given any neighborhood of \(1\), the limiting profile has a strictly smaller supremum outside it; the uniform bound therefore forces every maximizer of the actual profile into that neighborhood for all sufficiently large \(j\). For each fixed \(j\), continuity at positive reset rates and finite endpoint limits follow from the finite-dimensional spectral formula. Since the value at \(q=\delta_j\) exceeds \(2\) for large \(j\), whereas its \(q\to\infty\) limit is \(2\) and its \(q\downarrow0\) limit is below \(2\), at least one interior maximizer exists. Finally \(\delta_j=1/(\omega_j+j)\sim1/(2j)\), so \(r_*(j)\sim\Omega^2/(2J)\).

**5. Why the fixed-interaction zero-rate limit differs.** For fixed \(j>0\), all three accessible eigenvalues \(-j,-\omega_j,+\omega_j\) are distinct. The \(q\downarrow0\) stationary state is the energy-diagonal dephasing of \(|\downarrow\downarrow\rangle\). Direct substitution of these three normalized eigenvectors gives the only nonzero two-spin Pauli correlators
\[
T_{yy}=\frac{1}{2(1+j^2)},\qquad
T_{zz}=\frac{2j^2+1}{2(1+j^2)}.
\]
Since \(T_{zz}\ge T_{yy}\ge0\), the same criterion gives the stated fixed-\(j\) Bell limit. Its square is strictly below \(4\), because
\[
4(j^2+1)^2-\big[(2j^2+1)^2+1\big]=4j^2+2>0.
\]
The order of limits is essential: the small splitting \(\delta_j\) collapses only in the strong-coupling regime.

## Verification

The included standalone `check.py` (NumPy dependency listed in `requirements.txt`) constructs the exact stationary density matrix in two independent ways: by spectral averaging and by a sixteen-dimensional stationary Liouville solve. It computes the Pauli correlation singular values, checks the uniform trace-distance and CHSH error inequalities, and tests the fixed-interaction weak-reset limit. On the packaged sources the checker reported **262 passing assertions**, including the near-optimum values \(\mathcal B(20,\delta_{20})\approx2.234349357295\), \(\mathcal B(100,\delta_{100})\approx2.235999040117\), and \(\mathcal B(500,\delta_{500})\approx2.236065219695\). The finite checks are illustrations only; the infinite-limit and sharp-optimization claims rely on the explicit uniform analytic bounds above. The script uses the convention \(\Omega=1\).

## Relationship to prior work

Kulkarni and Majumdar (first public version 2023-07-14) establish this resetting Ising-dimer Hamiltonian, its exact stationary density matrix, and its concurrence. In particular, their Appendix A discusses a strong-interaction/weak-reset scaling with \(j q\) fixed, and their figures report a concurrence peak approaching \(1/2\). **Neither the stationary-state formula, the scaling variable, nor the concurrence ceiling is claimed as new here.** The additional mathematical result is the optimized Bell-inequality observable, an explicit uniform approximation valid over **all** reset rates, its sharp limiting optimum \(\sqrt5\), and the forcing of every optimal rate onto the splitting scale. CHSH nonlocality is strictly stronger than mere entanglement and is not determined by concurrence for arbitrary mixed two-qubit states. Horodecki et al. (1995) supply the general two-qubit CHSH criterion, not the model-specific optimized asymptotics. A recent related two-qubit reset-entanglement study (Murauer et al., first public 2026-10-29) is visible through its abstract, but its full text was inaccessible during this comparison; potential overlap with a broader exact-state analysis remains a priority risk.

## Limitations

The claim concerns the maximal ideal projective CHSH expectation of the **ensemble-averaged** stationary state in the specified two-qubit model. No global \(\sqrt5\) bound at arbitrary finite coupling is proved, nor is the limiting Bell optimum claimed for other Hamiltonians, many-body chains, non-Poissonian clocks, or noisy measurements. The explicit error is \(O(j^{-1})\) and may not be the sharp convergence order. The cited source already gives the exact state and the strong-coupling entropy crossover; originality here is the *uniform rate optimization and Bell measurement classification*, and independent publication-priority verification remains outstanding.

## References

1. M. Kulkarni and S. N. Majumdar, “Generating Entanglement by Quantum Resetting,” arXiv:2307.07485, first submitted 2023-07-14; *Physical Review A* **108**, 062210 (2023). https://arxiv.org/abs/2307.07485 ; https://doi.org/10.1103/PhysRevA.108.062210 . Inspected relevant arXiv full-text passages in Secs. II–IV and Appendix A.
2. R. Horodecki, P. Horodecki and M. Horodecki, “Violating Bell inequality by mixed spin-1/2 states: necessary and sufficient condition,” *Physics Letters A* **200**, 340–344 (1995). https://doi.org/10.1016/0375-9601(95)00214-N .
3. J. Murauer et al., “Entanglement diagnostics of stochastic-resetting steady states: theory and measurement on superconducting qubits,” arXiv:2610.40638, first submitted 2026-10-29. https://arxiv.org/abs/2610.40638 . Abstract available; full text not inspected.
