# Exponentially small reset-rate threshold for partial-transpose entanglement of noisy W states

## Finding
For each integer \(n\geq 3\), prepare the symmetric single-excitation W state on \(n\) qubits, apply independent identical local depolarization at rate \(\gamma>0\) between common Poisson resets at rate \(r>0\) to that W state, and observe the unique stationary density matrix \(\rho_{n,r}\). Let \(\rho_{n,r}^{\Gamma_1}\) be the partial transpose on qubit 1. There is a finite positive critical rate \(r_{\mathrm{PPT}}(n)\) such that \(\rho_{n,r}^{\Gamma_1}\) is positive semidefinite for \(0<r\leq r_{\mathrm{PPT}}(n)\) and has a strictly negative eigenvalue for \(r>r_{\mathrm{PPT}}(n)\). Its exact large-population scale is
\[
\lim_{n\to\infty}\frac{r_{\mathrm{PPT}}(n)}{\gamma n^{3/2}2^{-n}}=\frac12.
\]
More precisely, for every fixed \(c>0\), with \(r_n=\gamma c n^{3/2}2^{-n}\),
\[
\lim_{n\to\infty}2^n\lambda_{\min}\!\left(\rho_{n,r_n}^{\Gamma_1}\right)=1-2c.
\]
Hence this cut is PPT for all sufficiently large \(n\) if \(c<1/2\), and NPT entangled for all sufficiently large \(n\) if \(c>1/2\). No boundary classification is asserted for the exact finite-size choice \(c=1/2\).

## Assumptions and scope
Use \(\mathcal H_n=(\mathbb C^2)^{\otimes n}\), \(|W_n\rangle=n^{-1/2}\sum_{j=1}^n|0\cdots1_j\cdots0\rangle\), and the one-qubit semigroup
\[
\mathcal D_t(X)=e^{-\gamma t}X+(1-e^{-\gamma t})\operatorname{tr}(X)I_2/2.
\]
All qubits have the same strictly positive depolarization rate; the instantaneous resets reprepare the *entire* entangled state and are independent of the local noise. The stationary state is
\[
\rho_{n,r}=\int_0^\infty r e^{-rt}\mathcal D_t^{\otimes n}(|W_n\rangle\langle W_n|)\,dt
=\alpha\int_0^1u^{\alpha-1}\mathcal E_u^{\otimes n}(|W_n\rangle\langle W_n|)\,du,
\]
where \(\alpha=r/\gamma\), \(\mathcal E_u(X)=uX+(1-u)\operatorname{tr}(X)I_2/2\), and \(u=e^{-\gamma t}\). The PPT assertion concerns the bipartition one qubit versus the remaining \(n-1\). For this cut, NPT implies entanglement; PPT does **not** in general imply separability when \(n>2\). No claim of genuine multipartite entanglement, operational error-correction gain, or imperfect preparation tolerance is made.

## Proof
**1. Order of rates and the existence of a threshold.** Write \(\Phi_t=\mathcal D_t^{\otimes n}\), a product local semigroup. For \(0<r_1<r_2\), if \(T_i\sim\operatorname{Exp}(r_i)\), then \(T_1\) has the same distribution as \(T_2+S\), independently, where \(S\) is zero with probability \(r_1/r_2\) and otherwise exponential of rate \(r_1\). This follows by multiplying Laplace transforms. Consequently
\[
\rho_{n,r_1}=\mathbb E_S\,\Phi_S(\rho_{n,r_2}).
\]
Every \(\Phi_S\) is product local and preserves PPT across the selected cut, as does its mixture. Thus the PPT rates form an initial interval. When \(r\downarrow0\), the stationary state tends to \(I_{2^n}/2^n\), strictly PPT, and as \(r\to\infty\) it tends to the NPT pure W state, whose cut partial transpose has a negative eigenvalue \(-\sqrt{n-1}/n\). Analytic continuity supplies a unique finite positive boundary \(r_{\mathrm{PPT}}(n)\), with PPT at equality.

**2. Exact primary partial-transpose block.** Put \(m=n-1\), \(p=(1-u)/2\), \(q=(1+u)/2\), and let \(|W_m\rangle\) denote the normalized one-excitation vector among the last \(m\) qubits. Decompose the partially transposed state as \(D_\alpha+X_\alpha\), where \(D_\alpha\) is the pinching onto the two first-qubit diagonal blocks and is positive semidefinite. On the orthonormal pair \(v=|0\rangle|0^m\rangle\) and \(w=|1\rangle|W_m\rangle\), the compression is
\[
\begin{pmatrix} A_n(\alpha)&C_n(\alpha)\\ C_n(\alpha)&B_n(\alpha)\end{pmatrix},
\]
with
\[
 A_n=\alpha\int_0^1u^{\alpha-1}p q^m\,du,
\quad B_n=\frac\alpha n\int_0^1u^{\alpha-1}p q^{m-2}\bigl(2q^2+(m-1)(p^2+u^2)\bigr)\,du,
\]
\[
 C_n=\frac{\alpha\sqrt m}{n}\int_0^1u^{\alpha+1}q^{m-1}\,du.
\]
These follow by applying the one-qubit channel to the decomposition \(|W_n\rangle=\sqrt{m/n}\,|0\rangle|W_m\rangle+n^{-1/2}|1\rangle|0^m\rangle\). The cross matrix element contains two off-diagonal channel factors \(u\), one from the first qubit and one from the excited rest qubit.

**3. Scale of the primary block.** Choose \(\alpha_n=c n^{3/2}2^{-n}\) with fixed \(c>0\). For either diagonal integrand \(f(u)\) above, \(f(0)=2^{-n}\). Write its beta-age integral as \(2^{-n}+\alpha_n\int_0^1u^{\alpha_n-1}(f(u)-f(0))du\). On \(u\leq1/2\), the mean-value bound is a polynomial in \(n\) times \((3/4)^n\); on \(u\geq1/2\), the integrated absolute difference is \(O(n^{-2})\), by \(q^m\leq\exp[-m(1-u)/2]\). Thus the correction is \(o(2^{-n})\), and
\[
2^n A_n\to1,\qquad 2^nB_n\to1.
\]
Boundary-layer integration at \(u=1\) gives \(\int_0^1u^{\alpha_n+1}q^{m-1}du\sim2/n\), hence \(2^n C_n\to2c\). The unit vector \((v-w)/\sqrt2\) yields the upper spectral bound
\[
\limsup 2^n\lambda_{\min}(\rho_{n,r_n}^{\Gamma_1})\leq1-2c.
\]

**4. All other coherences are negligible.** Every off-diagonal matrix element of \(X_\alpha\) connects a first-qubit-zero state with exactly \(k\) excitations in the other qubits to a first-qubit-one state with exactly \(k+1\) excitations. For \(0\leq k\leq m-1\), the corresponding block is a scalar times the incidence matrix between the \(k\)- and \((k+1)\)-subsets of an \(m\)-set. Its operator norm is
\[
 h_k=\frac\alpha n\sqrt{(k+1)(m-k)}\int_0^1 u^{\alpha+1}q^{m-k-1}p^k\,du.
\]
The incidence norm follows from its constant positive row/column sums, or by a Perron singular-vector argument. Here \(h_0=C_n\) and the other blocks have disjoint support. Since \(0\le p/q\le1\), for \(k\ge1\) the integral divided by the \(k=0\) integral is at most the \(k=1\) ratio, which is \(O(1/n)\) by concentration at \(u=1\). Also \(\max_{k\ge1}\sqrt{(k+1)(m-k)}/\sqrt m=O(\sqrt n)\). Therefore \(\max_{k\ge1}h_k=o(C_n)=o(2^{-n})\).

**5. Uniform lower bound for the diagonal part.** For \(u\leq n^{-2}\), expand \(\mathcal E_u^{\otimes n}(|W_n\rangle\langle W_n|)\) into tensor-Pauli operators. Every nonidentity Pauli coefficient has modulus at most one, so its operator-norm distance to the maximally mixed state is at most
\[
2^{-n}\bigl((1+3u)^n-1\bigr)=O(2^{-n}/n).
\]
Pinching cannot increase this norm. The beta-age mass of \([0,n^{-2}]\) equals \(n^{-2\alpha_n}=1-o(1)\). Contributions outside this interval are positive semidefinite in the diagonal part. Thus \(D_{\alpha_n}\succeq (1-o(1))2^{-n}I\), where \(\succeq\) is the Loewner order. The primary coherence has norm \(C_n=(2c+o(1))2^{-n}\), and all other coherence blocks have norm \(o(2^{-n})\). This proves
\[
\liminf 2^n\lambda_{\min}(\rho_{n,r_n}^{\Gamma_1})\ge1-2c.
\]
Combined with Step 3, it proves the stated spectral limit. By the initial-interval property in Step 1, the PPT threshold divided by \(\gamma n^{3/2}2^{-n}\) tends to \(1/2\).

## Verification
Run the standalone file `check.py` with Python, NumPy, and SciPy. It constructs independently the complete channel matrices for sizes \(3\leq n\leq7\), integrates the reset age with Gauss–Jacobi quadrature, compares the analytic primary block against the complete partial transpose, and checks finite-size root trends through size \(120\). A representative execution passed 210 numerical assertions. These are checks, not proofs of the uniform incidence and Pauli bounds. All limits and the existence of the all-size boundary are established analytically above.

## Relationship to prior work
Kulkarni and Majumdar, *Generating Entanglement by Quantum Resetting* (arXiv:2307.07485, first public 14 July 2023), derive a general Poissonian renewal state and analyze entanglement for a **closed, coherently coupled two-spin system**. The renewal identity is reused here, but the simultaneous local depolarizing semigroup, growing W states, and asymptotic partial-transpose boundary are not consequences of their two-spin concurrence formula. Gao and collaborators, *Scalable generation and detection of on-demand W states* (arXiv:2307.06116), motivate large-W preparation and discuss witnessing, not this reset-noise threshold. Wald and collaborators, *Stochastic resetting in discrete-time quantum dynamics* (arXiv:2410.11497), study gate-driven discrete-time quantum resetting and mostly few-qubit correlations, not continuous-time local depolarization. Earlier studies of unreset depolarized W states may contain spectral tools but do not themselves provide the exponentially small **Poisson renewal** threshold. No blanket uniqueness or independent publication-priority certification is claimed.

## Limitations
The limit is a **partial-transpose** threshold for the one-qubit-versus-rest cut, not a full separability or genuine-multipartite-entanglement theorem. The critical rate is exponentially small, but the negative eigenvalue in the crossover window is itself of order \(2^{-n}\), so the result is not evidence of robustness to fixed-size experimental perturbations. Instantaneous perfect global preparation of the entangled W state is assumed; the physical cost of doing so is unmodeled. The case where the scaled reset rate equals exactly \(1/2\) requires a finer finite-size expansion. Source coverage and publication priority remain subject to independent validation.

## References
- M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, arXiv:2307.07485 (2023), https://arxiv.org/html/2307.07485v2.
- J. Gao et al., *Scalable generation and detection of on-demand W states in nanophotonic circuits*, arXiv:2307.06116 (2023), https://arxiv.org/abs/2307.06116.
- S. Wald et al., *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, arXiv:2410.11497 (2024), https://arxiv.org/html/2410.11497v3.
- Z. Li, S. Sang, and T. H. Hsieh, *Entanglement dynamics of noisy random circuits*, Phys. Rev. B 107, 014307 (2023), https://doi.org/10.1103/PhysRevB.107.014307.
