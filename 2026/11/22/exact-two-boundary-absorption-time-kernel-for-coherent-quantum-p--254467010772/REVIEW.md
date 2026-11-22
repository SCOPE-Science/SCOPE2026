# Scientific review — exact two-boundary absorption-time kernel

## Correctness — PASS
The statement quantifies over every finite open path \(N\ge2\), positive hopping magnitude \(J\), equal positive Lindblad end-loss rate \(\kappa\), and every matrix entry of the integrated survival-time operator. A non-Hermitian generator with two endpoint sinks is proved spectrally stable: a putative undamped eigenvector must vanish at an end and hence everywhere by the tridiagonal recursion. The closed matrix is verified algebraically from four exact matrix identities and uniqueness of the Lyapunov solution. The diagonal gives the mean time, and strict convexity of the positive-coefficient expression \(a/\kappa+b\kappa\) gives a unique finite optimum for every interior site. At the two endpoints \(b=0\), correctly excluding a finite optimum. The \(N=2\) boundary is included.

A standalone integer recurrence checker confirms 338,349 coefficientwise matrix positions across lengths 2–100. A separate numerical Sylvester solver confirms full complex kernels in 21 parameter cases. These calculations corroborate but do not replace the infinite-length proof.

## Originality — PASS on examined evidence; historical priority provisional
Kassal and Aspuru-Guzik (arXiv:1201.5202v1) study a finite chain with one localized trapping mechanism and additional noise or recombination. Razzoli, Paris and Bordone (arXiv:2011.13794v1) study transport efficiency with one trap, not the two-terminal mean-time Gramian. Riberi (arXiv:2605.08056v1) solves a semi-infinite, one-boundary absorber, where the second endpoint and the finite-length integrated operator are absent. The previously published finite-path Gramian covers one end loss, and the published two-loss lattice result is stationary infinite-line scattering with a different optimization observable. Neither directly implies the claimed two-end, all-site, all-length formula; the proof also gives a new finite-size dependence on both source-to-boundary distances.

Relevant abstract, full-text and indexed-result comparisons were completed. An equivalent older derivation in the broad Lyapunov/linear-systems or quantum-transport literature remains possible, and no exhaustive historical-priority claim is made.

## Mathematical value — PASS
The result resolves the entire integrated lifetime *operator*, not merely one chosen site's expected time, for an arbitrarily long network of coherent coupled sites with two competing irreversible traps. Its closed affine-parity kernel exposes coherent off-diagonal effects, a concrete boundary-geometry dependence of the uniquely optimal equal trap strength, and distinct bulk and boundary large-system limits. Two-end competition is a natural physical transport design, not an arbitrary parameter slice, and is not a routine substitution in the one-end result.

## Limits and source comparisons
The proof does not cover unequal sink strengths, alternative boundary conditions, detection channel allocation, many-particle systems or other graphs. The source comparisons establish provisional originality only. The theorem is a closed finite-size statement, not a thermodynamic transition or a claim of a universal optimal quantum-control strategy.

Self-review: passed. Independent audit: not yet performed.
