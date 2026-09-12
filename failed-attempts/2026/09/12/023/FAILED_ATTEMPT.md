# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Proved BKZ-64 Dual-Fourier Distinguishing Threshold for ML-KEM-512
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1098
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Cryptography
- **Method:** dual-lattice Fourier distinguishing with BKZ-profile simulation

## Problem

Decide whether BKZ reduction with blocksize 64 applied to the full 512-dimensional dual of ML-KEM-512 Module-LWE (ring Z_3329[x]/(x^256+1), module rank k=2) provably yields a dual vector short enough that the standard discrete-Gaussian Fourier distinguisher achieves advantage at least 0.20 within 2^40 samples.

## Attempted claim

For Decision-MLWE at ML-KEM-512 parameters (n=256, k=2, q=3329, centered-binomial errors eta1=3 and eta2=2), BKZ-64 achieves a dual vector v with Euclidean length at most 1.05 times the BKZ-2.0 simulator prediction for dimension 512, and the associated Fourier distinguisher has advantage at least 0.20 using at most 2^40 samples.

## Research outcome

Rigorously disproved the admitted BKZ-64 dual-Fourier threshold for ML-KEM-512: the literal square 512-dim dual is generically exactly qZ^512, so every dual vector gives Fourier advantage exactly 0 and overall advantage is at most 1.2e-5, not 0.20.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL: the actual negative headline (square 512-dim dual generically qZ^512, advantage exactly 0, overall <=1.2e-5) is substantively implied by prior textbook plus spec facts without new mathematics. Standard q-ary definition Lambda_q^perp(A)={x:A^T x=0 mod q} immediately gives triviality when square M is invertible; Kyber/Bogdanov et al. and FIPS 203 already publish q=3329, n=256,k=2 and the NTT factorization of x^256+1 into 128 quadratics; GL_2 counting plus union bound is mechanical parameter substitution. No prior states the beta=64+0.20 pair verbatim, but a prior source need not do so when its stronger general lemma exhaustively covers the claim as a special case. value: FAIL: ADMISSION_DEFECT. Admission target_integrity and triviality_preflight claimed standardized full-dimension scope with no type confusion, vacuity, or sublattice artifact requiring genuine analysis. The refutation instead exposes a type/normalization error: the literal square dual (m=n=512) is generically trivial qZ^512, while the cryptographically relevant duals used by estimator/dual-attack literature are rectangular (e.g. lattice-estimator Kyber512 dual d=1024, beta~387-424). The exact-zero therefore says nothing about deployed ML-KEM-512 hardness, BKZ budgets, or fine-grained LWE gaps; it is a textbook exercise plus known NTT table plus mechanical counting, with rectangular case explicitly left open. Per TARGET policy a negative resolution that is only a type error fails value even if literally false.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The refutation covers the literal claim (square 512-dimensional dual of the 512-secret); rectangular duals from m>512 samples are different lattices not named by the claim and are not decided here. The singular branch (probability at most 1.2e-5) is bounded by advantage 1 rather than analyzed exactly. No BKZ binary was executed; none is needed since the invertible-branch lattice is exactly qZ^512, and the simulator figures are closed-form GSA values.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
