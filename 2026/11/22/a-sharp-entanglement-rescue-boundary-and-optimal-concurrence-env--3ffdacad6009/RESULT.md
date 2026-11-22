# A sharp entanglement-rescue boundary and optimal concurrence envelope under collective resetting with spontaneous emission

## Finding
Consider two resonantly pair-coupled qubits with identical, independent spontaneous-emission channels, together with Poisson events that reset **both** qubits to their joint ground state. If the coherent pair-conversion amplitude is \(g>0\), the single-qubit emission rate is \(\gamma>0\), and the full-state reset rate is \(r>0\), their unique stationary concurrence is
\[
\boxed{\mathcal C(g,\gamma,r)=\frac{2g}{(r+2\gamma)((r+\gamma)^2+4g^2)}\left[(r+\gamma)(r+2\gamma)-2\gamma g\right]_+,}
\]
where \([x]_+=\max\{x,0\}\). This gives a complete stationary entanglement phase boundary:
\[
\boxed{\mathcal C>0\quad\Longleftrightarrow\quad (r+\gamma)(r+2\gamma)>2\gamma g.}
\]
In particular, if \(g>\gamma\), resetting *restores* stationary entanglement at the unique positive threshold
\[
\boxed{r_{\mathrm c}=\frac{\sqrt{\gamma^2+8\gamma g}-3\gamma}{2};}
\]
otherwise stationary entanglement is present at every strictly positive reset rate. Equality at the threshold means separability, not entanglement.

For every fixed \(\gamma,r>0\), concurrence is maximized over **all** positive coherent coupling strengths at the unique value
\[
\boxed{g_*=\frac{r+\gamma}{2(r+2\gamma)}\left(\sqrt{\gamma^2+(r+2\gamma)^2}-\gamma\right).}
\]
The resulting *sharp, attainable* envelope is
\[
\boxed{\sup_{g>0}\mathcal C(g,\gamma,r)=\frac{\sqrt{\gamma^2+(r+2\gamma)^2}-\gamma}{2(r+2\gamma)}.}
\]
It **strictly increases** with the resetting rate, from the unreset, optimized spontaneous-emission limit \((\sqrt5-1)/4\) as \(r\downarrow0\), toward the universal ceiling \(1/2\) as \(r\to\infty\). For every finite positive \(\gamma,r\), the envelope lies strictly between these two limits; the ceiling is approached only along a diverging-reset/diverging-coupling sequence. This distinguishes the advantage of optimizing coupling jointly with resetting from the fixed-coupling limit, in which concurrence vanishes when \(r\to\infty\).

## Assumptions and scope
The Hilbert space is \(\mathbb C^2\otimes\mathbb C^2\) with ordered basis \(\{|00\rangle,|01\rangle,|10\rangle,|11\rangle\}\). Set \(\hbar=1\), let \(\sigma_- = |0\rangle\langle1|\), and put
\[
H=g(|00\rangle\langle11|+|11\rangle\langle00|),\quad L_1=\sqrt\gamma\,(\sigma_-\otimes I),\quad L_2=\sqrt\gamma\,(I\otimes\sigma_-).
\]
For trace-one density matrices, the exact Markovian master equation is
\[
\dot\rho=-i[H,\rho]+\sum_{j=1}^2\left(L_j\rho L_j^\dagger-\frac12\{L_j^\dagger L_j,\rho\}\right)+r(|00\rangle\langle00|-\rho).
\]
On arbitrary operators the final contribution is \(r(\operatorname{tr}\rho\,|00\rangle\langle00|-\rho)\). The reset is a **joint** pure-ground re-preparation, not independent single-qubit resets or local amplitude damping disguised as resetting. Only zero-temperature local amplitude damping is present; there is no detuning, thermal excitation, additional dephasing, or stochastic reset-age dependence. The theorem concerns the unconditional stationary density matrix and standard Wootters concurrence, not trajectory-conditioned entanglement. The theorem quantifies every positive triple \((g,\gamma,r)\), and unreset bounds are limiting comparisons.

## Proof
**Stationary existence, uniqueness, and support.** The Hamiltonian-plus-emission generator \(\mathcal L_0\) is a trace-preserving, completely positive quantum dynamical semigroup. Therefore
\[
\rho_*=r\int_0^\infty e^{-rt}e^{t\mathcal L_0}(|00\rangle\langle00|)\,dt
\]
is a normalized positive stationary state. For any two initial density operators, their evolved difference under full resetting equals \(e^{-rt}e^{t\mathcal L_0}\) applied to the initial difference, so trace-norm contraction implies uniqueness and convergence. Evolution from the reset state preserves the subspace of matrices having only diagonal entries and the possible conjugate pair \(\rho_{00,11},\rho_{11,00}\). The stationary density matrix thus has this \(X\)-form without any assumption on initial state.

**Exact stationary entries.** Put \(x=\rho_{11,11}\), \(y=\rho_{01,01}=\rho_{10,10}\), \(w=\rho_{00,11}\), and \(p_{00}=1-x-2y\). The independent driven stationary equations are
\[
0=2g\operatorname{Im}w-(2\gamma+r)x,\qquad
0=\gamma x-(\gamma+r)y,\qquad
0=ig(p_{00}-x)-(\gamma+r)w.
\]
The real part of \(w\) vanishes. Writing \(D=(\gamma+r)^2+4g^2\), direct elimination yields
\[
\boxed{
 w=i\frac{g(\gamma+r)}D,\qquad
 x=\frac{2g^2(\gamma+r)}{(2\gamma+r)D},\qquad
 y=\frac{2\gamma g^2}{(2\gamma+r)D},\qquad p_{00}=1-x-2y.}
\]
All quantities are exact. Positivity is independently assured by the completely positive resolvent representation, not inferred from numerical eigenvalues.

**Concurrence and threshold.** For an \(X\)-state with no \(\rho_{01,10}\) coherence, the exact two-qubit spin-flip expression reduces to
\[
\mathcal C=2\max\{0,|w|-\sqrt{\rho_{01,01}\rho_{10,10}}\}=2\max\{0,|w|-y\}.
\]
Substitution gives the boxed concurrence formula. Its denominator and \(2g\) are strictly positive, hence its sign depends only on \((r+\gamma)(r+2\gamma)-2\gamma g\). This is \(r^2+3\gamma r+2\gamma(\gamma-g)\), strictly increasing in \(r\ge0\); when \(g>\gamma\) it has exactly one positive root, equal to \(r_{\mathrm c}\), and otherwise it is positive for every \(r>0\). This establishes the full separability/entanglement classification including the equality boundary.

**Unique optimal coupling.** For fixed \(r,\gamma>0\), write \(q=r+\gamma\), \(d=r+2\gamma\), \(A=qd\). On the positive-concurrence interval \(0<g<A/(2\gamma)\), maximizing concurrence amounts to maximizing \(f(g)=g(A-2\gamma g)/(q^2+4g^2)\). Its derivative has the sign of
\[
Aq^2-4\gamma q^2g-4Ag^2.
\]
This polynomial decreases strictly from a positive value to negative infinity as \(g\) increases, so it has exactly one positive zero, which is the stated \(g_*\). Its root lies in the entangled region because \(f\) is positive for sufficiently small positive \(g\) and vanishes at both endpoints. Outside that region concurrence is zero; therefore this is the **unique global maximizer**. Substituting \(g_*\) and simplifying yields
\[
\mathcal C(g_*,\gamma,r)=\frac12\left(\sqrt{1+t^2}-t\right),\qquad t=\frac\gamma{r+2\gamma}.
\]
Here \(t\) strictly decreases from \(1/2\) toward zero as \(r\) increases. The displayed function has derivative \((t/\sqrt{1+t^2}-1)/2<0\), proving strict monotonicity and both sharp endpoint limits. At fixed finite \(g\), the concurrence formula gives \(\mathcal C=2g/r+O(r^{-2})\) as \(r\to\infty\); consequently there is no contradiction between the vanishing fixed-coupling value and the increasing **coupling-optimized** envelope.

## Verification
Run `python3 CHECK.py` with the Python standard library. The checker independently assembles the full sixteen-dimensional Liouvillian from Hamiltonian, local collapse operators, and joint reset; solves the trace-constrained stationary linear system; and compares all matrix entries with the above expression for 85 deterministic, logarithmically varied parameter triples. It also checks exact master-equation residuals, trace/positivity constraints, the independent partial-transpose sign, the entanglement onset, the strict coupling optimum, the sharp envelope limits, and scale covariance. The bundled checker reports 782 passing assertions. These finite experiments corroborate the proof and are not used as a proof for all real positive parameters.

## Relationship to prior work
Kulkarni and Majumdar [1] provide the general stationary Poisson-reset integral and stationary entanglement for a **closed**, transverse-Ising dimer. Their model has no local spontaneous emission and a different Hamiltonian, so their concurrence formulas do not imply the stated spontaneous-emission phase boundary or jointly optimized envelope. Hartmann, Dür, and Briegel [2] analyze open, radiatively damped coupled qubits and demonstrate reset-assisted stationary entanglement with **independent local replacements**. Their broad mechanism and the unreset dissipative principle are established antecedents, not claimed as original; local replacements do not reproduce the present **joint** reset generator. The published pair-converting, joint-reset dephasing result [3] contains no amplitude damping, hence its odd-parity populations are fixed by preparation and its reset-rate phase diagram differs; the published pair-reset bit-flip analysis [4] has unital local noise, two coherent \(X\)-state branches, and a different noise threshold. Neither covers the present zero-temperature, nonunital emission mechanism or its optimized concurrence envelope by a change of parameters. The spin-flip concurrence formula itself is standard [5] and not new.

The novelty claimed here is **only** the combined exact zero-temperature emission-plus-*joint*-reset phase diagram, unique optimal coupling, and sharp reset-enhanced concurrence envelope for the stated pair-conversion model. It is not a new general Lindblad theorem, a new concurrence definition, or a claim that reset-assisted entanglement was previously unknown. Relevant prior models overlap in mechanism but not in the mathematical generator and quantifiers. The literature comparison is necessarily bounded; an overlooked exact specialization of a more general open-system solution remains the main publication-priority risk.

## Limitations
The stationary result is not a time-dependent concurrence formula. It does not extend as stated to independent resets, nonzero thermal pumping, asymmetric emission, detuned qubits, qubits driven singly, time-correlated reset clocks, or additional interactions. A different Hamiltonian with an inactive odd-parity exchange block can give the same stationary sector, so any truly equivalent previously published reduction would supersede the novelty claim. The asymptotic half-concurrence ceiling is not attained at a finite reset rate and fixed nonzero decay. The computational tests are finite and are not an external certification. No experimental observation or independent scientific validation is asserted.

## References
[1] M. Kulkarni and S. N. Majumdar, *Generating Entanglement by Quantum Resetting*, first public arXiv submission 2023-07-14, https://arxiv.org/abs/2307.07485.

[2] L. Hartmann, W. Dür and H.-J. Briegel, *Entanglement and its dynamics in open, dissipative systems*, 2007, https://arxiv.org/abs/quant-ph/0703138.

[3] *Exact reset-rate reciprocity and thermal entanglement boundary for a dephased qubit pair*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-reset-rate-reciprocity-and-thermal-entanglement-boundary-f--1e0867d1d987.

[4] *A sharp geometric-mean noise threshold for entanglement under global quantum resetting*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-geometric-mean-noise-threshold-for-entanglement-under-gl--25a4a404999e.

[5] W. K. Wootters, *Entanglement of Formation of an Arbitrary State of Two Qubits*, 1998, https://arxiv.org/abs/quant-ph/9709029.
