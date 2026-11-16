# Scientific review: critical circular Fourier-extension fourth-moment gaps

## Correctness — PASS

The claim concerns fixed nonnegative integer indices and the one-variable radial Bessel moments defined in RESULT.md. The common pole is verified by the uniform Hankel expansion and periodic averaging. Adjacent-order subtraction cancels the zero-frequency tail, allowing the critical limit. The Bessel recurrence converts each limiting gap to two convergent fourth-over-radius moments. A Neumann-product representation combined with the two-dimensional logarithmic potential identity evaluates those moments in terms of odd harmonic sums. Telescoping proves all pairwise gaps, and the mean-value theorem gives the squared-coefficient scaling. Boundary terms and convergence regimes are specified in the proof. The checker independently compares the identities for finite orders and cutoffs, passing 45 checks. Numerical agreement is not substituted for a proof of the all-index result.

## Originality — PASS relative to examined sources

Xu (arXiv:2610.19648, first public 2026-10-14) proves strict modal dominance for the range above the endpoint and analyzes the common critical divergence, but Sections 3.2 and 6 of the inspected HTML do not state the exact fixed-index cancellation formula or squared-coefficient endpoint law. Carneiro, Oliveira e Silva and Sousa (arXiv:1710.10365) give the classical modal restriction framework; Ciccone and Sousa (arXiv:2312.07309) study fixed finite-exponent comparisons. Neither inspected primary work supplies the exact critical odd-harmonic gap for all fixed pairs. Relevant published-finding corpus entries describe different Fourier/Bessel problems, notably the finite-field and spherical-harmonic fourth-moment results. Neumann products, Bessel recurrences and logarithmic-potential integrals are established ingredients, and an older integral-table equivalent of the intermediate fourth-over-radius identity remains a genuine residual priority risk. Searches do not constitute a proof of global novelty.

## Value — PASS

The critical power-four radial Bessel moments separately diverge, so mere finite-exponent comparison does not determine their limiting difference. The exact all-mode positive limit and its odd-harmonic dependence identify a natural critical obstruction's first finite spectral separation, with explicit square-root endpoint scaling for the associated pure-mode coefficients. The result does not claim the global best Fourier-extension stability constant or any uniform growing-degree bound.

## Primary-source comparison and limitations

Relevant read material: Xu arXiv:2610.19648, Sections 1, 3.2 and 6; Carneiro--Oliveira e Silva--Sousa arXiv:1710.10365, introductory results and Bessel comparison arguments; Ciccone--Sousa arXiv:2312.07309, first results and relevant comparison section; NIST DLMF, Bessel classical identities. Outstanding risk: an equivalent critical difference might occur in a specialized older Weber--Schafheitlin or Bessel-integral source not located under the examined aliases. All index limits are fixed-index only. The universal claim is analytic, not experimentally exhaustive.

Self-review: passed. Independent audit: not yet performed.
