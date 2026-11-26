# One-query angular law for unknown qubit Hamiltonians

## Finding

For a qubit Hamiltonian \(H_j=\mathbf n_j\cdot\boldsymbol\sigma\), where \(\|\mathbf n_j\|=1\), if the unknown evolution time is uniformly distributed on \([0,\pi]\), the two Hamiltonians have equal prior probability, and only one query is allowed, then the optimal average success probability over all probes (including ancillas) is \(P_{\rm succ}=\frac12+\frac14\sqrt{1-(\mathbf n_0\cdot\mathbf n_1)^2}\).

The formula is an exact angular interpolation. If \(c=\mathbf n_0\cdot\mathbf n_1\), orthogonal axes give success probability \(3/4\), while parallel or antiparallel axes give \(1/2\), because the time-averaged channels then coincide.

## Assumptions and scope

The Hilbert space is one qubit. The candidate Hamiltonians are \(H_j=\mathbf n_j\cdot\boldsymbol\sigma\), with real unit vectors \(\mathbf n_j\in\mathbb R^3\). The candidate is selected with prior probability \(1/2\) each. Conditional on the candidate, the single evolution time \(\theta\) is averaged uniformly over \([0,\pi]\), and one call to \(U_j(\theta)=e^{-iH_j\theta}\) is permitted. The probe may be entangled with an untouched ancilla, and the final measurement is unrestricted. The claim concerns the ideal average success probability, not finite-shot estimation or a multi-query strategy.

## Proof

Write \(\sigma_{\mathbf n}=\mathbf n\cdot\boldsymbol\sigma\). The averaged one-query channel for axis \(\mathbf n\) is

\[
\mathcal E_{\mathbf n}(\rho)=\frac1\pi\int_0^\pi e^{-i\theta\sigma_{\mathbf n}}\rho e^{i\theta\sigma_{\mathbf n}}\,d\theta
=\frac12\bigl(\rho+\sigma_{\mathbf n}\rho\sigma_{\mathbf n}\bigr),
\]

because the terms proportional to \(\sin(2\theta)\) and \(\cos(2\theta)\) integrate to zero. For equal priors, Helstrom's channel-discrimination formula gives

\[
P_{\rm succ}=\frac12+\frac14\|\mathcal E_{\mathbf n_0}-\mathcal E_{\mathbf n_1}\|_\diamond.
\]

It remains to compute the diamond norm. It is enough to optimize over pure inputs \(|\Psi\rangle\) on the qubit and an ancilla. Set \(|\Psi_j\rangle=(\sigma_{\mathbf n_j}\otimes I)|\Psi\rangle\). The difference of the two output states is \(\frac12(|\Psi_0\rangle\langle\Psi_0|-|\Psi_1\rangle\langle\Psi_1|)\), whose trace norm equals

\[
\sqrt{1-|\langle\Psi_0|\Psi_1\rangle|^2}.
\]

Let \(\rho_S=(I+\mathbf r\cdot\boldsymbol\sigma)/2\) be the reduced qubit state, so \(\|\mathbf r\|\le1\), and put \(c=\mathbf n_0\cdot\mathbf n_1\). The Pauli product identity gives

\[
\langle\Psi_0|\Psi_1\rangle
=\operatorname{Tr}(\rho_S\sigma_{\mathbf n_0}\sigma_{\mathbf n_1})
=c+i(\mathbf n_0\times\mathbf n_1)\cdot\mathbf r.
\]

Consequently,

\[
|\langle\Psi_0|\Psi_1\rangle|^2=c^2+\bigl((\mathbf n_0\times\mathbf n_1)\cdot\mathbf r\bigr)^2\ge c^2,
\]

so every probe gives trace norm at most \(\sqrt{1-c^2}\). A maximally entangled probe has \(\mathbf r=0\), attaining this bound. Thus \(\|\mathcal E_{\mathbf n_0}-\mathcal E_{\mathbf n_1}\|_\diamond=\sqrt{1-c^2}\), which proves the claim.

## Verification

The derivation uses the exact integral over \([0,\pi]\), the Pauli identity \(\sigma_{\mathbf a}\sigma_{\mathbf b}=(\mathbf a\cdot\mathbf b)I+i\sigma_{\mathbf a\times\mathbf b}\), the trace-norm formula for the difference of two pure-state projectors, and the equal-prior Helstrom formula. The extremizing input is explicit: any maximally entangled two-qubit state. No numerical experiment is needed for the identity.

As consistency checks, \(c=0\) yields \(P_{\rm succ}=3/4\), matching the one-query orthogonal-axis case in the Hamiltonian-recognition paper. If \(|c|=1\), then \(\mathcal E_{\mathbf n_0}=\mathcal E_{\mathbf n_1}\), so the optimal success is exactly the prior baseline \(1/2\).

## Relationship to prior work

Zhu, He, Chen, Zhang, and Wang analyze the same unknown-time Hamiltonian-recognition model and prove the all-query optimum for orthogonal qubit axes; their theorem gives \((2k+1)/(2k+2)\), hence \(3/4\) when \(k=1\). The present statement evaluates the one-query case for every relative axis angle. Sacchi's treatment of Pauli-channel discrimination supplies the general discrimination framework and the role of maximally entangled probes, but its explicit Pauli-channel formulas assume a common Pauli basis; generic dephasing channels about nonorthogonal axes are not jointly diagonal in one such basis.

## Limitations

This result is restricted to one query, equal priors, unit-norm qubit Hamiltonians, and a uniform time average on \([0,\pi]\). It does not give the optimal success probability for multiple calls with the same unknown time, nonuniform time priors, noisy implementations, or higher-dimensional Hamiltonians. The literature search was targeted rather than exhaustive, so an unindexed source may contain an equivalent one-query formula.

## References

1. C. Zhu, S. He, Y.-A. Chen, L. Zhang, and X. Wang, “Optimal Hamiltonian recognition of unknown quantum dynamics,” arXiv:2412.13067 (first public version 17 December 2024); later published in *npj Quantum Information* 12, 36 (2026). https://arxiv.org/abs/2412.13067 ; https://doi.org/10.1038/s41534-026-01182-6
2. M. F. Sacchi, “Minimum error discrimination of Pauli channels,” arXiv:quant-ph/0506072 (2005). https://arxiv.org/abs/quant-ph/0506072
