# Independent mathematical audit

## correctness

PASS

Conjugation by \(\sigma_x\otimes\sigma_x\) flips both Zeeman terms and preserves the XXZ interaction, giving \(H(B,b)\mapsto H(-B,-b)\). Qubit swap sends \(b\mapsto-b\) while preserving \(B\), and the two unitaries commute, so their product maps \(H(B,b)\) to \(H(-B,b)\). Functional calculus transfers this to the Gibbs state. Hilbert--Schmidt geometric discord is invariant under local unitaries and qubit swap exchanges which side is measured, yielding the two identities and all symmetric-function corollaries. The assigned numerical checker independently confirms the covariance to machine precision. No correctness defect is present.

## originality

FAIL

The same primary paper prints the exact XXZ Hamiltonian, the thermal state, and the one-sided Hilbert--Schmidt GQD formula, then explicitly remarks that its fixed-side GQD curve is not symmetric in magnetic field. The audited theorem is the immediate symmetry explanation already encoded in those formulas: a local spin flip changes both field signs, qubit swap reverses only the inhomogeneity, and standard local-unitary invariance plus swap covariance exchanges the measured side. No nonstandard lemma, spectral calculation, or optimization is needed. Under the implication-based originality rule this is a direct corollary of the published model and standard discord covariance, even though the source does not print the exchange identity.

## value

FAIL

The identity is a useful explanation of the source's asymmetric fixed-side plot, but it is obtained by composing two obvious symmetries of the printed Hamiltonian and invoking standard covariance of the discord measure. This is a short textbook symmetry check rather than an independently difficult structural result under the common value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
