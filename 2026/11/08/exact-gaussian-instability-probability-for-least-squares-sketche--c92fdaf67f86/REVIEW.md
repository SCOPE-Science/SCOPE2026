# Self-review

## Correctness — PASS

The claim is an exact probability theorem with explicit quantifiers (integer sketch width \(k\ge2\), ambient half-dimension \(N\ge k+1\), coupling \(\gamma>0\)); there is no inference from a finite simulation to an infinite statement. The full Hessian is SPD by a determinant-one principal block and identity complement; the fixed basis is explicitly ortho-symplectic; and the exact Galerkin Hessian is identity. Direct least squares followed by symmetrization gives the two closed eigenvalues. The smaller eigenvalue crosses zero exactly on the stated Gaussian-regression event, which is equivalent to real exponential Hamiltonian growth because the determinant is negative and the two-dimensional Hamiltonian trace is zero. The standard Wishart conditional-normal calculation is reconstructed using a congruence Jacobian, producing an explicit normalized radial law. Uniform angular integration and two endpoint limit arguments give the probability and both asymptotics. The standalone checker ran successfully from the actual package contents. Roundoff, finite tests and unmodeled sketch families are not proof inputs.

## Originality — PASS, with bounded priority risk

The direct source [1, Section 4.1, equations (18)–(19)] defines the sketched symmetrized Hessian, and [1, Lemma 2] proves sufficient subspace-embedding control. It does not report the exact unconditional Gaussian chance of a sign-indefinite reduced Hessian, the equivalence to exponentially unstable trajectories on this positive-definite oscillator, or the sharp coupling/sketch-width asymptotics. Earlier symplectic papers [2,3] address randomized *basis construction*; [4,5] develop sketched Galerkin or minimal-residual *approximation and quasi-optimality bounds*. These do not imply the exact tail mixture at issue. Both Gaussian-regression and arcsine formulas are classical ingredients and are not individually presented as novel. The novelty assessment remains conditional on historical coverage: a general theorem on eigenvalue-cone crossing of symmetrized Gaussian regressions, if it exists and subsumes this construction, would supersede the claim. No inspected source establishes that implication.

## Value — PASS

Preservation of canonical Hamiltonian structure is distinct from preservation of a positive-definite energy norm, and the latter matters for qualitative stability of long-time reduced dynamics. This new exact probability serves as a quantitative finite-sketch stress test for the just-introduced assembly procedure, not merely as an arbitrary numerical counterexample. The family retains positive definiteness for every \(\gamma\), allows arbitrarily weak coupling, keeps the exact reduced oscillator fixed and stable, and gives a sharp dimension-calibration law that distinguishes rare finite-sketch failures from deterministic sufficient embedding guarantees. It makes no unsupported claim for CountSketch or other sketch families.

## Sources and residual risks

The compared full text of [1] includes the assembly formulas, Lemma 2, energy-error theorem, experiments and conclusion. The full text of [2] and [3] covers basis construction. The author-hosted full-text manuscripts [4,5] cover randomized Galerkin/minimal-residual estimates; none reports the exact numerical Hamiltonian instability law. General Gaussian regression cone-crossing priority and the lack of a fully exhaustive historical census remain explicit risks, not a proof of novelty by absence.

Self-review: passed. Independent audit: not yet performed.
