# Scientific review — flux-selective two-boson collision loss

## Correctness: PASS

The theorem is an exact all-size Fourier-sector classification for \(n\ge3\), real nonzero hopping, arbitrary Peierls phase, and strictly positive sitewise two-body collision loss. The dissipative spectral argument proves that indefinite survival equals the free-eigenspace component annihilated by every collision bra, including the treatment of nonnormal decaying modes. At fixed total momentum the cosine dispersion has no distinct *bosonic* equal-energy pair except when its center-of-mass factor vanishes. The unique flat sector then has a one-dimensional collision image; the projection and dimension follow from an explicit involution count. The complete localized capture law follows from two translation overlaps, including the even-ring antipodal exception. These are analytical proofs; finite computation is not used as an infinite-size certificate.

Reproducibility: `python3 verify.py` with NumPy independently diagonalizes the symmetric free matrices, computes collision-map nullities, counts real eigenvalues of nonuniform-loss generators, and checks proposed projectors and all localized-pair survival values for 40 ring/flux cases, \(3\le n\le10\). It passed. Numerical eigenvalue clustering is a finite corroboration only.

## Originality: PASS on inspected evidence, with priority risk

The exact zero-flux two-walker cycle classification is prior work: the special \(\Phi=0\) rank and capture values are not asserted as new. The new target is **all magnetic fluxes**, particularly generic complete destruction of bosonic collision-dark states, quarter-flux emergence for odd cycles, the zero/half-flux rank exchange for even cycles, and an all-state capture projector for unequal positive loss rates. These new assertions do not follow from the zero-flux statement because gauge-invariant flux cannot generally be gauged away on a ring.

Relevant published comparisons include Krovi and Brun (2006), which gives a general dark-eigenstate mechanism without two-body magnetic collision-loss evaluation; Kepesidis and Hartmann (2012), which places single-particle loss at one site; Qin et al. (2014), which treats two-particle periodic walks but no flux or collision losses; Polo et al. (2019), which gives the full spectrum and persistent currents for *real-interaction* two-boson rings threaded by flux, without an irreversible loss projector or asymptotic capture classification; and Zhang, Jin and Song (2017), which employs imaginary Hubbard interactions and pair tunnelling in a different ladder geometry without a magnetic-flux capture classification. Published mathematical results about Fourier diagonalization and general non-Hermitian loss are not claimed as original. The remaining risk is an unindexed two-particle magnetic transport/dark-state calculation or a stronger derivation from an extended non-Hermitian Bethe-ansatz treatment.

## Mathematical value: PASS

The result exhibits a sharp flux selection rule for exact collision immunity that is not a parameter relabeling: at fixed odd ring size the dark dimension changes from zero at zero flux to \((n-1)/2\) at quarter flux; on even rings, generic flux destroys entire finite-dimensional protected subspaces and half flux switches the antipodal response. The all-initial-state, arbitrary-positive-loss theorem is a useful structural diagnostic for coherent loss engineering and for distinguishing eventual capture from near-resonant slow decay. It is an infinite family with all fluxes treated, not a finite example or a tiny numerical improvement.

## Limits and closest antecedents

No finite-time decay rate or robustness to nonuniform hopping, interactions, extra potentials or missing collision detectors is claimed. The 2019 full real-Hubbard spectral solution is the closest potential generalizing antecedent, while the 2017 imaginary-Hubbard analysis is the closest non-Hermitian mechanism; neither examined treatment explicitly supplies the same claim. No independent scientific audit is reported.

Self-review: passed. Independent audit: not yet performed.
