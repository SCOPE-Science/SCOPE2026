# Self-review

## Correctness — PASS
The area normalization uses the squared polar radius, so the mean-zero perturbation preserves area exactly. Disk Hermite/Fock eigenvalues are incomplete-gamma integrals with a simple maximum. Differentiability of the coherent-projector boundary integral in trace-class norm supports the infinite-dimensional perturbation formula. The resulting Fourier shape Hessian, optimizing-eigenvector response and sharp strict frequency ordering follow by direct algebra and Parseval. The independent finite-section checker passed 1035 assertions on the exact packaged source; it is supporting numerical evidence rather than the universal proof.

## Originality — PASS, provisional
The closest full-text source is Gómez–Guerra–Ramos–Tilli (arXiv:2307.09304), whose Section 5 computes a signal-side Hessian while optimizing its superlevel domain. It does not state the mode-resolved domain-shape Hessian of the leading localization eigenvalue or the reciprocal spectral-gap eigenfunction response for prescribed boundary profiles. Nicola–Tilli (arXiv:2106.03423) gives global optimality of the disk and its exact norm, but not these second derivatives. A 2026 inverse-domain preprint (arXiv:2607.21590) may be relevant; only its abstract was accessible, so full-priority verification remains an unresolved limitation. An equivalent calculation hidden in older perturbation literature also remains possible. Failure of a semantic search alone is not treated as proof of novelty.

## Mathematical value — PASS
The theorem determines the complete local spectral shape sensitivity at the natural Gaussian concentration optimizer, including all angular frequencies, exact translation degeneracy, the unique sharp least-stable non-translation mode and waveform response. This quantitatively refines the geometric meaning of disk optimality rather than introducing an arbitrary special case; the constant depends sharply on disk area and the normalizing shape variable.

## Limitations
The result is a directional second-order theorem for one-dimensional Gaussian STFT localization. It does not supply a global best quantitative stability constant, higher spectral bands, or finite-perturbation uniformity. Historical priority needs independent specialist assessment, especially regarding the inaccessible full 2026 manuscript. The finite numerical checker is not an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
