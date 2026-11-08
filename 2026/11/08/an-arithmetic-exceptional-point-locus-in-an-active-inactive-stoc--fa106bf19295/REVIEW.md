# Scientific review

## Correctness — PASS

The column-convention master equations and discrete Fourier transform lead to the explicitly stated two-by-two blocks. Their characteristic equation excludes the eigenvalue \(-s\), making the eigenvalue-to-Fourier-index map injective. The discriminant vanishes for nonreal Fourier harmonics precisely at the displayed positive-rate pairs; the zero and (when applicable) alternating harmonics remain nondefective. At a repeated eigenvalue, the nonzero off-diagonal entry forces a size-two Jordan block. The full-generator inactive-probability mode follows exactly from the block exponential. The density of the rate pairs and the sharp \(r\le p/4\) bound are elementary consequences of the continuous, increasing sine parameter. The attached separately assembled generator checker passed 420 Fourier Jordan identities, 900 off-locus checks, and 100 full-generator propagations. These finite tests corroborate but do not replace the proof.

## Originality — PASS on examined evidence, with residual risk

The 2013 Pinkoviezky–Gov active/immobile motor exclusion work uses the same physically motivated two-motility-state motif but studies interacting motors, stationary current–density relations and jam statistics, not a rate-exact classification of exceptional points in the finite, one-particle continuous-time ring. Their second 2013 paper treats an open linear track with interacting motors. Weber–Pande (2015) study complex eigenmodes and damped oscillations in a biased network of triangular cycles with a special slow link, rather than the uniform two-state ring's Jordan degeneracies. Berry–Uzdin (2011) establish general non-Hermitian exceptional-point methods for a different Hamiltonian model; no priority is claimed for the discriminant method itself. Searches for the displayed parametric exceptional locus, aliasing as active–inactive Markov Fourier eigenvalue coalescence, and its time-domain signature returned no exact covering source. The nearby 2016 run–pause motor paper's full text was not inspected, and historical priority remains provisional.

## Mathematical value — PASS

This is a full classification, over all ring sizes and all strictly positive switching rates, of when a natural irreversible kinetic generator loses diagonalizability. The exceptional set has an exact finite arithmetic count, a shared parabolic geometry, a dense infinite-size union, and a sharp universal upper bound on the pause-entry rate. Unlike a bare determinant calculation, the coalescence is tied to a directly observable time-linear, exponentially damped oscillatory Fourier response. These features furnish a reproducible benchmark for transient relaxation and non-Hermitian Markov kinetics without requiring any unproved downstream claim.

## Sources and limitations

Primary comparison: Pinkoviezky and Gov (2013), https://doi.org/10.1088/1367-2630/15/2/025009; Pinkoviezky and Gov (2013), https://doi.org/10.1103/PhysRevE.88.022714; Weber and Pande (2015), https://doi.org/10.1103/PhysRevE.91.032136. Methodological context: Berry and Uzdin (2011), https://doi.org/10.1088/1751-8113/44/43/435303. The current proof assumes a single particle, homogeneous rates, clockwise motion, and exact rate tuning. Independent literature-completeness and experimental validation are not claimed.

Self-review: passed. Independent audit: not yet performed.
