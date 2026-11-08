# Scientific review: elliptic clocks and zero phase drift

## Correctness — PASS

The stated four-site vector field and lifting convention yield the exact two-dimensional system \(\dot x=-2\sin s\sin y\), \(\dot y=2\sin s\sin x\), with a constant \(s\) and normalized energy \(h=\cos x+\cos y\). The full level-set classification follows by inspecting the only four reduced critical points. On regular levels, an explicit quarter-arc integral reduces to the complete elliptic integral and is the **minimal** time of traversal, not a merely formal candidate period. The crucial nonstandard step is the global full-phase return: the coordinate exchange \(R(x,y)=(y,x)\) reverses the vector field on the **same connected oval**, so the time average of the antisymmetric common-phase velocity vanishes exactly. This is stronger than a return of phase differences alone. The logarithmic coefficient and its constant follow from the standard elliptic asymptotic. No experimental extrapolation is used to prove an infinite statement.

The standalone checker symbolically verifies five identities and numerically solves the original and reduced equations on 70 regular full orbits, including both signs of \(h\) and \(\sin s\). It separately tests a finite period monotonicity grid and the asymptotic regimes. Such computations corroborate, but do not replace, the global proof.

## Originality — PASS, with historical limits

The conservative endpoint, its lattice form, and the alternating/sine-sum first integrals are *not new*: they are explicit in Rosenau–Pikovsky (2005), while the 2026 ring paper states the conservative/Hamiltonian limit and Pikovsky (2026) analyzes conservative network structures. The claim is instead their specific four-site **complete orbit portrait, exact minimal elliptic period, no-drift lift to the full four-phase dynamics, and sharp logarithmic period constant**. The inspected sources contain their respective general conservation/basin/compacton constructions but not these specific consequences. A broader theorem implying the exact period and no-drift condition was not identified in the searched literature or compared published mathematical records. Search absence alone is not proof of uniqueness.

The particularly relevant Pikovsky–Rosenau (2006) *Phase compactons* article remained inaccessible beyond its bibliographic abstract. Its general finite-lattice discussions could overlap with aspects of the classification, although the available abstract addresses numerical finite-lattice chaos and wave dynamics rather than an elliptic four-site period formula. Full-text comparison remains a priority risk. The first-version 2026 date is the publicly verified origin of the newer motivating paper, not a novelty certificate.

## Mathematical value — PASS

The finite four-site ring is the smallest nontrivial even ring admitting both opposite-pair and Hamiltonian invariants. Its integrable limit is mathematically motivated by the 2026 study of basin complexity near the conservative boundary and by the 2005/2006 literature on dispersive phase lattices. The exact minimal period is a physically interpretable clock at finite size; its strict monotonicity and logarithmic blow-up quantify both nonisochrony and separatrix slowdown. The unexpected cancellation of global rotation establishes actual *closed trajectories in the unreduced four-oscillator phase torus*, rather than generic relative periodicity. This complete natural finite-dimensional classification is useful as a baseline for finite-size and near-conservative comparisons; it is not an arbitrary parameter slice or a mere reassertion of a known conservation law.

## Closest sources and limits

Yan–Ozawa–Kori–Sato, arXiv:2603.02135 (2026), supplies the exact nearest-neighbor family and the conservative endpoint but studies global basin metamorphosis for nonendpoint phase shifts. Rosenau–Pikovsky, Phys. Rev. Lett. 94, 174102 (2005), supplies the cosine-difference lattice and conserved sums. Pikovsky, J. Phys. Complexity 7, 025008 (2026), supplies general pair-Hamiltonian and conservative-network theory. Pikovsky–Rosenau, Physica D 218, 56–69 (2006), is a plausible related work that could not be read in full. The result does not extend to larger networks or phase shifts away from the conservative endpoint; full-text historical priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
