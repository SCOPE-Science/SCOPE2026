# Sharp concurrence frontier for phase-blind cascaded quantum charging

## Finding

Consider two identically coupled charger qubits and one battery qubit with an excitation-conserving Hamiltonian, as specified below. Let \(c\in[0,1]\) be the pure-state Wootters concurrence of the two-qubit charger, let \(e\in[0,1]\) be the initial battery excitation, and let \(L\in[0,1]\) be the collision's bright-sector exchange probability. Define the **phase swing** of the unconditional next-step battery excitation by
\[
\mathscr S(\phi_a;e,L)=\max_{\gamma\in[0,2\pi]}E_{\phi_a}(e,\gamma)-\min_{\gamma\in[0,2\pi]}E_{\phi_a}(e,\gamma).
\]
Here the variation is over the battery's relative phase \(\gamma\), with charger and collision parameters fixed; it is not an energy-projective shot-noise variance.

**Theorem (sharp fixed-concurrence phase frontier and maximally entangled charging law).** For every \(c,e,L\in[0,1]\), the exact range over normalized *pure* two-qubit charger states of concurrence \(c\) is
\[
\boxed{\big\{\mathscr S(\phi_a;e,L): C(\phi_a)=c\big\}
=\left[0,\ 2\sqrt{2e(1-e)L(1-L)}\sqrt{1-c^2}\right].}
\]
Every value in the interval is attained. In particular, **every** pure maximally entangled two-qubit charger is phase-blind, including states supported in all four computational basis vectors. For a maximally entangled charger, define \(s=(b+c_1)/\sqrt2\) when the charger amplitudes are \((a,b,c_1,d)\), and put
\[
Q=|a|^2+2|s|^2+|d|^2\in[0,2].
\]
After each collision, an outcome-conditioned local product-basis measurement can equalize the battery excitation of every measurement branch with nonzero probability. Under such measurements, the excitation is pathwise deterministic and satisfies
\[
\boxed{e_{n+1}-\tfrac12=(1-LQ)(e_n-\tfrac12).}
\]
If \(0<L<1\), all maximally entangled chargers other than the antisymmetric singlet (the unique \(Q=0\) charger up to phase) converge geometrically to \(e_n=1/2\). The singlet is dark and leaves the excitation unchanged. At \(L=1\), the fully symmetric one-excitation Bell state has \(Q=2\) and produces an exact period-two energy sequence rather than convergence.

For an explicit non-Bell, four-component example,
\[
|\phi_a\rangle=(|00\rangle+i|01\rangle+i|10\rangle+|11\rangle)/2,
\qquad C(\phi_a)=1,\quad Q=3/2,
\]
and therefore \(e_n=1/2+(1-3L/2)^n(e_0-1/2)\), for any permitted detuning, coupling and collision duration.

## Assumptions and scope

Write \(\sigma_j^-=|0\rangle_j\langle1|\), \(n_j=\sigma_j^+\sigma_j^-\), and take the charger qubits \(1,2\) and battery \(B\). The Hamiltonian is
\[
H=\omega_0(n_1+n_2)+\omega_B n_B+g\sum_{j=1}^{2}(\sigma_j^-\sigma_B^++\sigma_j^+\sigma_B^-),
\]
where \(\omega_0,\omega_B>0\), \(g>0\), and the collision duration \(\tau\ge0\). Put \(\Delta=\omega_B-\omega_0\) and \(\Omega=\sqrt{\Delta^2+8g^2}\). Define
\[
\xi=-i\frac{2\sqrt2g}{\Omega}\sin\frac{\Omega\tau}{2},\quad
\chi=\cos\frac{\Omega\tau}{2}-i\frac{\Delta}{\Omega}\sin\frac{\Omega\tau}{2},\quad
L=|\xi|^2,\quad |\chi|^2=1-L.
\]
Fresh, identically prepared pure charger pairs interact sequentially with the same battery, each for one interval \(\tau\). The measurement chosen after each collision may depend on the incoming battery pure state, and is a rank-one *local product* von Neumann measurement of the two charger qubits. All bounds concern the expectation \(\langle n_B\rangle\), not single-shot energy outcomes, ergotropy or thermal noise.

Let \(|\phi_a\rangle=a|00\rangle+b|01\rangle+c_1|10\rangle+d|11\rangle\), normalized, and define \(s=(b+c_1)/\sqrt2\), \(t=(b-c_1)/\sqrt2\). The input battery state is \(\sqrt{1-e}|0\rangle+\sqrt e\,e^{i\gamma}|1\rangle\), with arbitrary phase when \(0<e<1\). Its phase is immaterial at the endpoints.

## Proof

**1. Exact excitation-sector reduction.** The total excitation is conserved. In the charger-symmetric/antisymmetric basis, the active one- and two-excitation blocks are respectively \((|S,0\rangle,|00,1\rangle)\) and \((|11,0\rangle,|S,1\rangle)\), with \(|S\rangle=(|01\rangle+|10\rangle)/\sqrt2\). Each has coupling \(\sqrt2g\) and diagonal detuning \(\Delta\); the two blocks differ only by an overall energy offset. The antisymmetric vectors are dark. Thus the off-diagonal propagator entry in either active block is \(\xi\), and the upper-state diagonal entry is \(\chi\), after removal of a blockwise global phase.

Starting with the battery in \(|0\rangle\), the excited-battery output components are \(\xi s\) in \(|00,1\rangle\) and \(\xi d\) in \(|S,1\rangle\). Starting with the battery in \(|1\rangle\), the excited components are \(\chi a\) in \(|00,1\rangle\), \(\chi s\) in \(|S,1\rangle\), the dark \(t\) component, and the unchanged three-excitation \(d\) component, with phases of unit modulus. The output excitation for the general coherent input consequently is
\[
\begin{aligned}
E_{\phi_a}(e,\gamma)&=(1-e)L(|s|^2+|d|^2)
+e\big[1-L(|a|^2+|s|^2)\big]\\
&\quad+2\sqrt{e(1-e)}\operatorname{Re}\big(e^{i\gamma}Z\big),\\
Z&=\bar\xi\chi\,(\bar s a+\bar d s).
\end{aligned}
\]
The global phases cancel separately in each of the two active excitation blocks in the cross term. This formula also follows by direct eight-dimensional exponentiation; it does not rely on an approximate master equation.

**2. The concurrence-resolved bound.** Let \(M=\begin{pmatrix}a&b\\c_1&d\end{pmatrix}\) be the two-qubit amplitude matrix. Its pure-state concurrence is \(c=2|\det M|\). Each reduced single-charger-qubit density matrix has Bloch-vector length \(r=\sqrt{1-c^2}\), because its determinant equals \(|\det M|^2\). The collective transverse coherence obeys
\[
\langle\sigma_1^-+\sigma_2^-\rangle
=\sqrt2\,(\bar a s+\bar s d),\qquad
|\langle\sigma_j^-\rangle|\le r/2.
\]
The triangle inequality gives \(|\bar s a+\bar d s|\le r/\sqrt2\). The cosine term in the exact excitation formula has peak-to-trough variation \(4\sqrt{e(1-e)}|Z|\), with \(|Z|=\sqrt{L(1-L)}|\bar s a+\bar d s|\). This proves the stated upper endpoint and nonnegativity proves the lower endpoint.

Both endpoints and all intermediate values are obtained without limiting arguments. Choose \(\lambda=(1+r)/2\), \(\mu=(1-r)/2\), and prepare the Schmidt state \(\sqrt\lambda|00\rangle+\sqrt\mu|11\rangle\), which has concurrence \(c\). Apply the same local real \(y\)-axis rotation \(R_y(\theta)=\exp(-i\theta\sigma_y/2)\) to both qubits. Both resulting local Bloch vectors have transverse length \(r|\sin\theta|\) and are parallel, so the absolute collective transverse coherence equals \(r|\sin\theta|\). As \(\theta\) runs through \([0,\pi/2]\), the phase swing runs continuously and exactly through the entire stated interval. This also settles \(c=0\), \(c=1\), and \(L,e\in\{0,1\}\).

**3. Existence of a local measurement equalizing all conditional energies.** After any pure joint evolution, write \(|\Psi\rangle=|v_0\rangle|0\rangle+|v_1\rangle|1\rangle\), with \(|v_j\rangle\in\mathbb C^2\otimes\mathbb C^2\) and \(P_j=\|v_j\|^2\). If one \(P_j\) vanishes, every nonzero measurement outcome already has the same battery energy. Otherwise form the traceless Hermitian operator
\[
T=P_0|v_1\rangle\langle v_1|-P_1|v_0\rangle\langle v_0|.
\]
Choose a first-qubit orthonormal basis that makes the diagonal of \(\operatorname{Tr}_2 T\) zero. Such a basis always exists: any traceless qubit Hermitian operator has a Bloch vector, and one can measure along a perpendicular Bloch axis. The two resulting second-qubit conditional blocks \(T_\pm=\langle u_\pm|T|u_\pm\rangle\) are individually traceless. Choose a second-qubit Bloch axis perpendicular to **both** Bloch vectors of \(T_+\) and \(T_-\), which exists in three dimensions. In the resulting product basis each diagonal entry of \(T\) vanishes. Hence in every nonzero-probability branch, \(P_0|\langle u_jv_k|v_1\rangle|^2=P_1|\langle u_jv_k|v_0\rangle|^2\), and the conditional battery excitation equals the unconditional value \(P_1\). This construction is a product projective measurement, not a general entangling measurement. It applies afresh after every collision.

**4. Maximally entangled pathwise law.** When \(c=1\), both charger marginals are maximally mixed, so their transverse Bloch vectors vanish and \(Z=0\). Moreover, \(\sqrt2M\) is unitary; every two-by-two unitary has equal magnitudes in opposite diagonal entries, whence \(|a|^2=|d|^2\). Consequently the exact excitation map reduces to
\[
E_{\phi_a}(e,\gamma)=L(|s|^2+|d|^2)+(1-LQ)e,
\quad Q=|a|^2+2|s|^2+|d|^2,
\]
and its fixed point is \(e=1/2\). The measurement lemma and induction make the recurrence pathwise deterministic. By normalization \(0\le Q\le2\). Equality \(Q=0\) requires \(a=d=s=0\), leaving only the normalized antisymmetric \(|A\rangle\). For \(0<L<1\) and \(Q>0\), one has \(|1-LQ|<1\), proving geometric convergence. At \(L=1,Q=2\), the multiplier is \(-1\), establishing the stated period-two exception.

## Verification

The accompanying standalone `checker.py` constructs the full eight-by-eight Hamiltonian using tensor products and computes \(e^{-iH\tau}\) independently from the excitation-sector formula. With fixed-seed randomized normalized pure chargers, detunings, nonzero couplings, collision durations, input excitations and phases, it compares the output population to the exact formula. It also checks the sharp concurrence frontier and its three explicit attaining rotations, constructs two local measurement bases for equal conditional battery energy, and checks the exact non-Bell maximally entangled recurrence. Execute with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python checker.py` using NumPy and SciPy. The execution performed 525 randomized/constructive checks plus 24 closed-recursion checks; all passed. These finite calculations check the formula and edge cases but are not substitutes for the all-state proof above.

## Relationship to prior work

Gong, Zhang and Li, *Fluctuation-free Quantum Battery Charging Enabled by Bell-like Entangled and Separable Charger States*, arXiv:2610.31242v1 (first public October 22, 2026), establish this two-charger model, the adaptive-measurement objective and a general phase-dependent recurrence, and identify two special Bell-like fluctuation-free families. Their general recurrence is important prior coverage; this theorem does **not** claim the Hamiltonian, generic phase dependence or the Bell-like cases as new. The exact fixed-concurrence attainable *interval*, its sharp upper coefficient, universal phase blindness of the entire maximally entangled orbit and deterministic half-charge law are separate extremal and dynamical classifications. The general phase-recurrence expression in the earlier paper algebraically contains some of the ingredients, so priority risk remains for deductions implicit in that expression.

Gong, Zhang and Li, *Achieving Identical Stored Energy in Cascaded Collisional Quantum Battery Charging: Analytical Result*, arXiv:2610.01332v1 (first public October 1, 2026), address a single-qubit charger, not the two-qubit concurrence constraint. Li, Chen, Yu and Hao, *Charging optimization of quantum battery via phase-controlled coherent ancillae*, Physical Review A **113**, 052437 (May 15, 2026), examine phase-controlled atomic pairs charging a multilevel battery in a different dynamical regime; a sharp concurrence-resolved phase-swing frontier for this three-qubit unitary cascade was not found in the accessible description.

## Limitations

The theorem assumes *pure* identical two-qubit chargers, equal real exchange couplings, excitation-conserving collision dynamics, ideal adaptive local product measurements and no decoherence. The phase swing is a conditional input-phase susceptibility, not the actually observed trajectory variance before adaptivity; deterministic stored-energy expectation does **not** eliminate energy shot noise. A maximally entangled charger may be dark, or at an endpoint collision may produce a period-two sequence. A general published energy recurrence is prior art; this work isolates a new optimized frontier, and independent priority assessment is not performed. No claim is made for mixed charger states, asymmetric couplings, imperfect measurements or noise.

## References

1. L. Gong, J. Zhang and Y. Li, *Fluctuation-free Quantum Battery Charging Enabled by Bell-like Entangled and Separable Charger States*, arXiv:2610.31242v1, October 22, 2026. https://arxiv.org/abs/2610.31242
2. L. Gong, J. Zhang and Y. Li, *Achieving Identical Stored Energy in Cascaded Collisional Quantum Battery Charging: Analytical Result*, arXiv:2610.01332v1, October 1, 2026. https://arxiv.org/abs/2610.01332
3. H. Li, X. Chen, W. Yu and Y. Hao, *Charging optimization of quantum battery via phase-controlled coherent ancillae*, Phys. Rev. A 113, 052437 (2026), https://doi.org/10.1103/39yj-zgwf
4. W. K. Wootters, *Entanglement of formation of an arbitrary state of two qubits*, Phys. Rev. Lett. 80, 2245 (1998), https://doi.org/10.1103/PhysRevLett.80.2245
