# Scientific review — magnetic-square absorption-time theorem

## Correctness — PASS

The theorem specifies a single-excitation four-cycle, uniform hopping, total Peierls flux, one continuously coupled irreversible sink and an opposite initial site. In the parity basis its Hamiltonian splits into two real two-state couplings. The full occupation-integral matrix in `RESULT.md` satisfies the exact Lyapunov equation; its trace yields the generic mean. At zero flux an inaccessible uncoupled mode must be excluded, changing the mean by precisely \(1/\kappa\). At half flux the initial state belongs to a detector-orthogonal invariant subspace. All other fluxes have unit capture probability. Differentiation and strict convexity establish the unique optimum and its half-flux asymptotic. Reproducible exact symbolic and independent original-site-basis numerical checks are in `verify.py`. The limitations are a single perfect square with no additional dissipation and infinite-time first-jump statistics.

## Originality — PASS, qualified

The closest physics is magnetic-flux transmission suppression in L. Jin, *Quantum transport in coupled resonators enclosed synthetic magnetic flux* (arXiv:1611.10015), and dark-state quantum-network transport in Le et al., *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures* (arXiv:1707.07482). The former calculates unitary scattering through attached leads; the latter gives general dark-subspace and Lindblad-sink machinery, but neither states the piecewise opposite-site jump-time mean, its finite zero-flux jump, or its optimal irreversible sink strength. Friedman et al. (arXiv:1611.05676) and Liu et al. (arXiv:2001.00231) study ring first detection at repeated projective measurement instants rather than continuous absorption. Holzinger et al. (arXiv:2309.11376) concern different interacting emitter-ring arrays and do not use a Peierls flux. The analytic distinction is an exact all-rate and all-flux classification including a nonuniform infinite-time limit, not merely restating the known interference dark state. The comparison is not an exhaustive literature review; an implicit prior formula in uninspected work remains possible.

## Mathematical value — PASS

The four-site equal-arm Aharonov–Bohm ring is the smallest natural closed geometry with opposite-source and detector interference. The theorem exactly solves a physically operational first-absorption time, identifies a finite discontinuity at zero flux despite unchanged capture probability, and gives a sharp rate-matching prescription with a singular scaling transition as half flux is approached. The distinction between ordinary finite-time continuity and infinite-time non-uniformity is structural; the result is not just a numerical example or a normalization check.

## Residual limitations

No result is asserted for asymmetric arms, disorder, dephasing, other initial states, several sinks, or larger rings. At half flux the probability of capture is zero rather than a very long finite mean. The analysis supplies one proof and computational replay, not independent validation or priority certification.

Self-review: passed. Independent audit: not yet performed.
