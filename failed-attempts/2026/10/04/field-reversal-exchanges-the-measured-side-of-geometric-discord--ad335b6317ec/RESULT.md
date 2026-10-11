# Field reversal exchanges the measured side of geometric discord in an inhomogeneous XXZ dimer
## Finding
For the Gibbs state
\[
\rho_T(B,b)=\frac{e^{-H(B,b)/T}}{\operatorname{Tr}(e^{-H(B,b)/T})}
\]
of the inhomogeneous two-qubit XXZ Hamiltonian studied by Zhang, Fan, Ji, Jiang, Abliz, and Liu, define \(D_A\) and \(D_B\) to be the one-sided Hilbert--Schmidt geometric discords obtained by measuring the first and second qubit, respectively. For every real \(J,J_z,B,b\) and every \(T>0\),
\[
D_A(\rho_T(-B,b))=D_B(\rho_T(B,b)),\qquad
D_B(\rho_T(-B,b))=D_A(\rho_T(B,b)).
\]
Hence the unordered pair \(\{D_A,D_B\}\), together with \(D_A+D_B\), \(\min(D_A,D_B)\), and \(\max(D_A,D_B)\), is exactly even in the uniform field \(B\). When the field is homogeneous, \(b=0\), each one-sided discord is itself even. In particular,
\[
D_A(B,b)-D_A(-B,b)=D_A(B,b)-D_B(B,b),
\]
so the odd part of a fixed-side GQD curve under field reversal is precisely the directional discord imbalance.

## Assumptions and scope
The Hamiltonian is
\[
H(B,b)=\frac12\left[J(\sigma_x\otimes\sigma_x+\sigma_y\otimes\sigma_y)+J_z\sigma_z\otimes\sigma_z+(B+b)\sigma_z\otimes I+(B-b)I\otimes\sigma_z\right].
\]
The result concerns the finite-temperature Gibbs state with \(T>0\) and the Hilbert--Schmidt geometric discord defined in the source from the Bloch vector and correlation matrix. No claim is made for discord measures with a different metric unless they separately satisfy local-unitary invariance and the same subsystem-swap covariance.

## Proof
Let \(X=\sigma_x\otimes\sigma_x\) and let \(S\) be the qubit-swap unitary. Direct conjugation gives
\[
XH(B,b)X=H(-B,-b),\qquad SH(B,b)S=H(B,-b).
\]
Because \(S\) and \(X\) commute, \(V=SX\) satisfies
\[
VH(B,b)V^\dagger=H(-B,b).
\]
Functional calculus therefore yields
\[
\rho_T(-B,b)=V\rho_T(B,b)V^\dagger.
\]
The factor \(X\) is a local unitary. The one-sided Hilbert--Schmidt geometric discord is invariant under local unitaries, while swapping the two qubits interchanges which subsystem is measured. Therefore
\[
D_A(V\rho V^\dagger)=D_B(\rho),\qquad D_B(V\rho V^\dagger)=D_A(\rho),
\]
which proves the two identities. If \(b=0\), field reversal is already implemented by \(X\) alone, so each one-sided discord is even in \(B\). Every symmetric function of \(D_A\) and \(D_B\) is even because field reversal only exchanges the two entries.

## Verification
The analytic proof uses exact unitary-conjugation identities and the defining covariance of one-sided geometric discord. The accompanying checker independently constructs the \(4\times4\) Hamiltonian, forms Gibbs states by matrix exponentiation, evaluates both one-sided Bloch-matrix GQD formulas, and tests random real couplings and fields. It reports `VERIFY_OK`, with maximum state-covariance error \(2.225\times10^{-16}\), maximum directional-discord exchange error \(1.388\times10^{-16}\), and maximum homogeneous-field evenness error \(5.551\times10^{-17}\) over the stated finite test sets. These floating-point tests support, but are not needed for, the exact proof.

## Relationship to prior work
Zhang et al. define the one-sided GQD through the first-qubit Bloch vector and report that Bell nonlocality, MID, and concurrence are symmetric about zero magnetic field whereas GQD is not for their inhomogeneous XXZ example. The source does not state the field-reversal/measurement-side exchange identity above. The present result explains that observation exactly: reflecting \(B\) exchanges \(D_A\) with \(D_B\), so an asymmetric fixed-side curve is compatible with an exactly even unordered pair of directional discords. Searches for the same field-reversal identity, its swap formulation, and an implication-equivalent statement found no covering result in the checked literature records.

## Limitations
The claim is structural, not a new closed form for the GQD itself. It applies to the two-qubit Hamiltonian displayed above and to \(T>0\). The originality assessment cannot exclude an equivalent symmetry observation hidden in literature not located by the searches. The Hilbert--Schmidt GQD has known general limitations as a correlation measure; those issues do not affect the exact covariance identity proved here.

## References
1. G.-F. Zhang, H. Fan, A.-L. Ji, Z.-T. Jiang, A. Abliz, and W.-M. Liu, “Quantum correlations in spin models,” arXiv:1105.2866; Annals of Physics 326 (2011), DOI 10.1016/j.aop.2011.05.002.
2. B. Dakić, V. Vedral, and Č. Brukner, “Necessary and sufficient condition for nonzero quantum discord,” Physical Review Letters 105, 190502 (2010).
