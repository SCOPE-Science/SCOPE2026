# Mathematical review

## Correctness — PASS

The claim is fully finite-dimensional for each integer \(n\ge4\), with explicitly normalized conditional sampling on each weight-congruence class. The root-of-unity filter produces the exact four moments. The constant/singleton/pair incidence decomposition gives a 3-by-3 trivial block, two identical standard-representation coordinates in an explicit 2-by-2 block, and a scalar on the quadratic harmonic representation. There is no use of finite enumeration as an infinite proof. The rank formula follows from the number of nonzero weight layers available to each of the three representation types; the cutoff is checked directly against those counts. The asymptotic statement follows from Weyl's inequality and a dominant entry of order \(n^2 2^{-n}\), with all remaining matrix corrections of smaller order. The packaged checker independently verifies the invariant actions and rank in 18 nontrivial finite cases.

## Originality — PASS, with historical-priority limitations

The nearest work includes Filmus and Srinivasan on harmonic/Johnson decomposition, Rao on the Fourier analysis of a single Boolean slice, Cornelissen and colleagues on query complexity of the modulo-three Hamming-weight function, and previously published exact quadratic-band concentration on **one** Hamming shell. Those mathematical tools and special cases are not claimed as new. The exact spectrum for the **union** of every third shell is not supplied by individual single-shell eigenvalue lists: the rank-one restrictions in each multiplicity block need to be summed and then diagonalized. The specific Fourier moment collapse, universal rank threshold, exact paired isospectrality and asymptotic gap are the added results. A stronger unlocated theorem on arbitrary exchangeable Boolean sampling masks could imply this case; the priority comparison remains provisional until broad independent literature review.

## Mathematical value — PASS

The object is a natural deterministic one-third-density sampler for the first nontrivial nonlinear Walsh band. Knowing precisely when such sampling ceases to have a kernel matters for reconstruction and stable degree-two Fourier interpolation. The exact spectrum replaces an exponentially growing matrix with 3-by-3 and 2-by-2 matrices, while the rank theorem distinguishes the two recoverable masks in dimension seven from the unique unrecoverable one and proves universal recovery in dimension eight. Paired asymptotic conditioning is a property of the quadratic band that is not settled by the known degree-one classification. These are intrinsic sampling invariants, not an arbitrary table or a fixed small example.

## Closest literature and limits

- Rao, arXiv:2111.03213v1 (2021-11-05): Fourier restriction and coefficients on one slice, not exact degree-two congruence-mask spectral blocks.
- Filmus, arXiv:1406.0142, and Srinivasan, arXiv:1001.0280: the general harmonic-slice and Terwilliger machinery is established prior work.
- Cornelissen et al., arXiv:2112.14682v1: modulo-three weight under a quantum-query objective; not the same Gram operator.
- Published exact quadratic Walsh concentration on single Hamming shells (2026-10-11): exact one-shell eigenvalues and resonances, but no asserted three-shell-residue summation or resulting universal injectivity threshold.

No optimality among arbitrary sets of comparable size is proved. Eventual superiority of the isospectral pair is asymptotic, with no asserted minimal finite threshold. Historical novelty is not an external certification.

Self-review: passed. Independent audit: not yet performed.
