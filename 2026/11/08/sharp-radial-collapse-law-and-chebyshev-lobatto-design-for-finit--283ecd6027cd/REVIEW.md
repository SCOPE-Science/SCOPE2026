# Scientific review

## Correctness — PASS
For the all-Hermitian, Frobenius-normalized Gaussian coherent-state map, the angular DFT yields one square radial Vandermonde block and two copies of every narrower lag block. Lagrange inversion gives an explicit rank-one inverse limit; the narrower blocks decay less quickly, proving that the radial diagonal mode sets the exact smallest singular value. Direct limiting block norms identify the largest singular value. The monic Chebyshev interpolation identity with weighted Cauchy–Schwarz proves both the sharp lower bound and the complete, unique positive-weight optimizer. The direct-matrix script passed 105 assertions; its tests do not replace these proofs.

## Originality — PASS, historical priority provisional
The exact scalar Chebyshev optimal-design step is classical (Pukelsheim and Studden, 1993) and is not considered a new theorem on its own. The specific new claim combines the complete real-Hermitian Fock angular-block argument, the exact all-mode coalescence coefficient, and the unique radial-design classification. The 2017 continuous-variable Husimi tomography paper develops polynomial interpolation but not this coalescing-ring spectral result. The Gaussian multi-window and two-circle phase-retrieval sources prove different uniqueness statements. Clustered Fourier Vandermonde bounds concern a different operator and do not imply this coefficient. Closely ranked public mathematical research records on concentric Szegő frames and harmonic Bergman traces also concern different operators. Classical experimental design or quantum tomography may contain an equivalent formulation; independent historical priority checking is still needed.

## Mathematical value — PASS
The result quantifies the central singularity of a natural radially compressed heterodyne experiment, distinguishes it from other Hermitian angular sectors, and supplies an exact sensor-radius and positive-budget prescription. These information-completeness and instability constants are motivated by finite-dimensional Gaussian tomography, not by a parameter chosen solely for computation.

## Scope and remaining risks
All parameters are held fixed while the squared-radius band collapses; the proof does not establish finite-width optimality, adaptive weighting bounds, nonlinear pure-state reconstruction guarantees, or photon-counting noise accuracy. The classical Chebyshev ingredient must be credited. A quantum-design equivalence not located in the inspected literature remains possible.

Self-review: passed. Independent audit: not yet performed.
