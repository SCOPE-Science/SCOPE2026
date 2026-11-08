# Mathematical review

## Correctness: PASS
The weighted-centered spectral norm is convex under mass-preserving automorphisms, so averaging is genuinely globally nonworsening. The parity-periodic Fourier blocks yield the full spectrum, and endpoint eigenvalues reduce the objective to the maximum of two affine functions. A direct inequality proves the sharp mass-ratio threshold; the finite verifier checks the exact statement on many instances. The proof does not rely on finite enumeration.

## Originality: PASS (qualified)
The 2007 Boyd--Diaconis--Parrilo--Xiao paper derives an explicit uniform-stationary cycle solution. Prescribing unequal alternating masses changes the feasible kernels and spectra, so the present sharp threshold is not a substitution into the uniform eigenvalue formula. The 2010 Jafarizadeh symmetric K-partite/cyclic topologies and the 2020 clique-lifted star/path treatments were compared. Nothing in the relevant accessible material implies the specific alternating-stationary-mass formula; the 2010 full text could not be inspected, leaving a genuine publication-priority risk. Relevant research-record searches for aliases and stationary-periodic cycles returned no equivalent result. This is evidence-supported novelty, not a claim of exhaustive literature coverage.

## Value: PASS
Alternating stationary masses are a natural minimal periodic inhomogeneity in reversible finite-state MCMC and consensus modeling. The result identifies the precise ratio at which the optimizer switches from balancing extreme eigenmodes to saturating the smaller-mass vertices' transition capacity; the threshold also scales nontrivially with cycle length. It is an exact global optimization result for infinitely many even cycles, not a routine numerical tabulation.

## Closest work and limits
Boyd et al. (arXiv:0709.0955), §§2--4 and 3.1.1, gives the general symmetry-convexity framework and the equal-mass cycle. Jafarizadeh (arXiv:1008.2588) gives symmetric cyclic K-partite families; only its abstract could be inspected, so hidden overlap cannot be ruled out. Jafarizadeh (DOI:10.1109/TSIPN.2020.2964211), §§VI--VII, treats star/path and clique-lifted graphs. The claim requires fixed alternating masses, detailed balance and self-loops; it does not cover other stationary distributions or nonreversible chains. The analytical proof was checked in the same review process; independent external validation remains absent.

Self-review: passed. Independent audit: not yet performed.
