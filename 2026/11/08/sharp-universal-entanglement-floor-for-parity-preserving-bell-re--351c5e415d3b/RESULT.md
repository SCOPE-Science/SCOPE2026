# Sharp universal entanglement floor for parity-preserving Bell resetting

## Finding

Let \(\mathsf H_{\mathrm e}=\operatorname{span}\{|00\rangle,|11\rangle\}\). For every probability distribution \(w=(w_m)_{m\geq0}\) on nonnegative integer ages, put

\[
f_w(\theta)=\sum_{m=0}^{\infty}w_m\cos(m\theta),\qquad
\kappa_w=\min_{\theta\in[0,2\pi]}f_w(\theta).
\]

Reset to \(|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2\) and evolve between resets with any two-qubit unitary \(U\) preserving \(\mathsf H_{\mathrm e}\). The Wootters concurrence of the age-averaged state \(\rho_w(U)\) has the **exact attained worst-case value**

\[
\boxed{\inf_{U\mathsf H_{\mathrm e}=\mathsf H_{\mathrm e}} C(\rho_w(U))=\max\{0,\kappa_w\}.}
\]

Consequently, strictly positive \(\kappa_w\) is necessary and sufficient for a universal gate-independent entanglement guarantee. In particular, Bernoulli resetting of probability \(p\in(0,1]\) at each step has the sharp guarantee

\[
\boxed{\inf_U C(\rho_p(U))=\frac{p}{2-p}.}
\]

For stationary phase-randomized deterministic resets every integer \(k\ge2\) steps, by contrast, the exact infimum is zero. Matching mean intervals using \(p=1/k\) does not match the entanglement guarantee: Bernoulli resetting retains \(1/(2k-1)\) at worst, while the phase-randomized deterministic protocol can lose all ensemble entanglement.

## Assumptions and scope

All gates are ideal noiseless discrete-time two-qubit unitaries preserving the even computational-parity subspace; in particular, no amplitude damping, local depolarization, measurement back-action or leakage is allowed between resets. The reset is the exact Bell state \(|\Phi^+\rangle\), and concurrence is computed **after averaging the density matrix over reset ages**:

\[
\rho_w(U)=\sum_{m=0}^{\infty}w_mU^m|\Phi^+\rangle\langle\Phi^+|(U^\dagger)^m.
\]

The age probabilities are arbitrary normalized nonnegative \(w_m\), so the mathematical theorem also applies to prepared age mixtures not arising from an equilibrium renewal clock. For a physical stationary discrete renewal clock whose positive integer inter-reset time \(L\) has finite mean, the age law is \(w_m=\Pr(L>m)/\mathbb E L\). For Bernoulli resets it is \(w_m=p(1-p)^m\). A deterministic interval \(L=k\) is periodic rather than convergent from a fixed starting phase; its **stationary phase-randomized version** has \(w_0=\cdots=w_{k-1}=1/k\). The latter convention, not an unqualified pointwise late-time limit of deterministic resetting, is used in the comparison.

## Proof

**Step 1: concurrence reduces to a Bloch-plane length.** Identify \(|00\rangle\) and \(|11\rangle\) with the logical qubit basis \(|0_{\mathrm L}\rangle,|1_{\mathrm L}\rangle\). The Bell reset has logical Bloch vector \(e_x=(1,0,0)\). Since all evolved states remain in this two-dimensional subspace, the averaged two-qubit density matrix has no matrix entries involving \(|01\rangle,|10\rangle\). The two-qubit X-state specialization of Wootters' formula is

\[
C(\rho_w)=2|\langle00|\rho_w|11\rangle|
=\sqrt{\overline r_x^{\,2}+\overline r_y^{\,2}}
\ge \overline r_x,
\]

where \(\overline r\) is the Bloch vector of the logical averaged state. This identity also follows directly by evaluating the eigenvalues of \(\rho_w(\sigma_y\otimes\sigma_y)\rho_w^*(\sigma_y\otimes\sigma_y)\): the nonzero spin-flipped eigenvalue square roots differ by \(2|\rho_{00,11}|\).

**Step 2: exact universal lower bound.** Every parity-preserving unitary restricts to some \(2\times2\) unitary, whose adjoint action rotates logical Bloch vectors by a proper rotation of an angle \(\theta\in[0,2\pi]\) around a unit axis \(n=(n_x,n_y,n_z)\). Rodrigues' rotation formula gives

\[
e_x\cdot R_n(m\theta)e_x=n_x^2+(1-n_x^2)\cos(m\theta).
\]

Consequently,

\[
\overline r_x=n_x^2+(1-n_x^2)f_w(\theta)
\ge n_x^2+(1-n_x^2)\kappa_w\ge\kappa_w,
\]

because \(\kappa_w\le f_w(0)=1\). Therefore \(C(\rho_w(U))\ge\max\{0,\kappa_w\}\) for every admissible \(U\).

**Step 3: construct an attaining gate.** The sum defining \(f_w\) converges uniformly since \(\sum_mw_m=1\), so \(f_w\) is continuous and achieves its minimum. A logical rotation about the \(y\)-axis through angle \(\theta\) sends \(e_x\) into the \(xz\)-plane, hence \(\overline r_y=0\) and \(C(\rho_w(U_\theta))=|f_w(\theta)|\). If \(\kappa_w>0\), choose an angle minimizing \(f_w\). If \(\kappa_w\le0\), continuity together with \(f_w(0)=1\) supplies an angle with \(f_w(\theta)=0\); use that angle. The required logical rotation extends to a physical parity-preserving two-qubit gate by letting it act as the identity on the odd sector. Thus the infimum is attained and equals \(\max\{0,\kappa_w\}\).

**Step 4: stochastic and periodic clock frontiers.** Write \(q=1-p\). The geometric cosine transform is

\[
f_p(\theta)=p\operatorname{Re}\frac{1}{1-qe^{i\theta}}=
\frac{p(1-q\cos\theta)}{1-2q\cos\theta+q^2}.
\]

As a function of \(x=\cos\theta\), its derivative equals \(pq(1-q^2)/(1-2qx+q^2)^2\), nonnegative, strictly positive for \(0<p<1\). Therefore the minimum is at \(\theta=\pi\), with value \(p/(2-p)\). This also holds directly at \(p=1\). The physical gate \(Z\otimes I\), a logical \(z\)-axis half-turn, maps \(|\Phi^+\rangle\) to \(|\Phi^-\rangle\) at each odd age and attains this minimum, because the geometric even-minus-odd weight is \(p/(2-p)\).

For deterministic inter-reset time \(k\ge2\) with uniformly randomized phase, \(w_m=1/k\) for \(0\le m<k\), hence \(f_w(2\pi/k)=k^{-1}\sum_{m=0}^{k-1}\cos(2\pi m/k)=0\). A logical \(y\)-rotation at that angle makes the mixed state separable. Both protocols have mean reset interval \(k\) when the Bernoulli parameter is \(p=1/k\), but their sharp floors are respectively zero and \(1/(2k-1)\). At \(k=2\) one can instead use \(Z\otimes I\): the two pure-age states are \(|\Phi^+\rangle,|\Phi^-\rangle\), both maximally entangled, while their uniform mixture is \((|00\rangle\langle00|+|11\rangle\langle11|)/2\), with concurrence zero. Geometric resetting with \(p=1/2\) leaves a mixture with concurrence exactly \(1/3\). This completes the proof.

## Verification

The accompanying standalone script `checks/verify.py` uses only the Python standard library and reconstructs physical amplitudes via explicit \(2\times2\) unitary matrix products, independently comparing ensemble concurrence to the Bloch/Fourier formula. It checks finite-support random age laws, arbitrary logical gate axes and angles, sharp deterministic-versus-geometric equal-mean contrasts, and the Bell toggle witness. Run `python checks/verify.py` from the unpacked result directory. It completed **1061 bounded assertions** on the supplied version. These finite checks are diagnostic; the all-gate and all-clock assertions follow from the preceding proof.

## Relationship to prior work

Murauer *et al.* (arXiv:2610.40638; first publicly posted October 29, 2026) derive the geometric reset-age stationary mixture and calculate two-qubit Bell-reset entanglement diagnostics for a specified transverse-field Ising family. Their geometric resolvent and fixed-gate concurrence calculations are prior work. Wald *et al.* (arXiv:2410.11497; October 15, 2024) give the more general stochastic-reset stationary-state and non-Poissonian-reset framework. These works supply the reset-age mixture, not an identified closed-form **infimum across every parity-preserving gate for an arbitrary age distribution**, nor the exact positivity classification via the minimum cosine transform or equal-mean phase-randomized periodic-versus-Bernoulli gate guarantee. The derivation does not re-claim their state mixture or the known two-qubit X-state concurrence formula. No claim of literature-wide uniqueness is made.

## Limitations

The strict guarantee fails outside ideal parity-preserving evolution: a gate that leaks into \(|01\rangle\) or \(|10\rangle\), imperfect reset, and depolarizing noise invalidate the present lower bound. The theorem concerns concurrence after ensemble mixing, not the mean of trajectory-wise concurrence. A deterministic reset clock is compared in its stationary phase-randomized formulation, not as a pointwise convergent autonomous reset process from a known initial phase. The arbitrary-law theorem does not assert every age distribution is realizable by a stationary renewal clock. Published generic reset-renewal identities may allow the present criterion to be derived by specialists; absence of an explicit prior statement in inspected sources is not proof of priority. No independent audit has been performed.

## References

1. J. Murauer, S. Tornow, M. Kulkarni, E. Barkai, S. N. Majumdar and M. Singh Roy, *Entanglement diagnostics of stochastic-resetting steady states: theory and measurement on superconducting qubits*, arXiv:2610.40638, first public October 29, 2026, https://arxiv.org/abs/2610.40638.
2. S. Wald, L. H. Yao, T. Platini, C. Hooley and F. Carollo, *Stochastic resetting in discrete-time quantum dynamics: steady states and correlations in few-qubit systems*, Quantum **9**, 1742 (2025), first preprint October 15, 2024, https://arxiv.org/abs/2410.11497.
3. W. K. Wootters, *Entanglement of formation of an arbitrary state of two qubits*, Physical Review Letters **80**, 2245–2248 (1998), https://doi.org/10.1103/PhysRevLett.80.2245.
