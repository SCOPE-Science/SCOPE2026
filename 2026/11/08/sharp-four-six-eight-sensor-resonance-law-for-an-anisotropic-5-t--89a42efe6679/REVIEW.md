# Self-review

## Correctness — PASS
The theorem is a complete parameterized statement for every positive anisotropy ratio, not an extrapolation from sampling. It follows from the 12 cosine-orbit eigenvalues, a degree-two/degree-three cyclotomic intersection proving 18 distinct resonance ratios, a maximal-eigenspace lower bound, and explicit Vandermonde block decompositions of the stated four-, six-, and eight-site sensor sets. At resonances exactly one pair of cosine orbits collides; consequently each spectrum has 11 distinct eigenvalues rather than 12. Independent floating-point tests reconstruct the full observation matrix and all spatial eigenspace ranks but are supplementary to the proof.

## Originality — PASS relative to inspected evidence
The 2026 graph-dynamical-sampling paper gives the general eigenspace observability test, not this exact arithmetic stratification or these optimal vertex placements. The survey is likewise general. The 2020 work on Cartesian products concerns structural observability under generic edge weights, whereas the theorem addresses exact weighted spectral degeneracies in one constrained parameter. The existing closely related square prime torus result is not an implication: it uses equal cycle lengths and no one-parameter 18-coupling resonance classification. Searches for aliases, weighted product-cycle observability, and eigenvalue resonance disclosed no dominating statement; this is evidence of noncoverage in inspected records, not proof of global publication priority.

## Value — PASS
The smallest unequal odd-prime torus gives a natural complete exact model of exceptional weights in network reconstruction. The proven optimal spatial budget has three distinct levels, with constructive placements, rather than a generic lower bound. The fact that a four-site rectangle fails at mixed-axis coincidences yet a four-site skew pattern succeeds makes the distinction between eigenspace dimension and physical vertex placement substantive. The finite classification is useful for choosing sensors and for testing robustness near spectral collisions.

## Closest literature and limitations
Bulai et al., arXiv:2609.25472, Section 4/Theorem 4.1, contains the generic observability criterion; Aldroubi et al., arXiv:2511.10769, Section 2.2.1, reviews it. Doostmohammadian, arXiv:2001.04699, develops structural observability for Cartesian networks without exact anisotropic Fourier degeneracies. A related exact square-torus sensor theorem concerns identical prime cycle lengths and a distinct collision mechanism. The result does not provide perturbation-uniform conditioning, noisy reconstruction, or a shortest-time horizon; publication-priority residual risk remains.

Self-review: passed. Independent audit: not yet performed.
