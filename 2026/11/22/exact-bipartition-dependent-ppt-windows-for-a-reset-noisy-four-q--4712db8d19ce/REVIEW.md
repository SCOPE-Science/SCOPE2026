# Scientific review

## Correctness — PASS

The stated quantum channel and Poisson-age integral give a unique positive normalized stationary state. All exact partial-transpose characteristic polynomials are reconstructed in `checker.py`, independently of the claimed closed eigenvalue lists. The only candidates for negative eigenvalues are identified by strict positive polynomial identities in the proof, and the critical quadratic has exactly one positive zero. Two independent normalization limits reproduce the correct Dicke-state bipartite negativities. Numerical checks of thirteen parameter choices are supporting evidence, not an infinite proof.

## Originality — PASS, with residual risk

Actual claim-and-equivalence searches were made against related published research, and the most relevant accessible mathematical documents were materially read. Earlier static Pauli-spectrum results do not evaluate the resetting resolvent, and earlier two-qubit global-reset bit-flip work concerns a different input and noise model. The full Kulkarni–Majumdar quantum-resetting article develops the general renewal resolvent, not this four-qubit noisy Dicke classification. Nawareg's full noisy-Dicke work studies white-noise mixtures with one admixture parameter, rather than the multiple local Pauli-weight attenuation factors here. Chen and Jiang (2020) and Campbell, Tame, and Paternostro (2009) establish substantial prior Dicke-noise results. The former's full text was unavailable, creating a real risk of implicit coverage by its more general entanglement criteria. No unconditional novelty or independent priority certification is claimed.

## Mathematical value — PASS

All six one-versus-three and balanced bipartitions of a physically motivated four-qubit resource are distinguished by an exact finite-rate PPT/NPT hierarchy, not just by a single witness or numerical sample. The interval where smaller cuts are NPT but balanced cuts PPT and the distinct inertia changes at two later rates provide actionable structural information for interpreting how different bipartitions retain entanglement indicators under repeated state re-preparation. The result does not claim that PPT cuts are separable or that the state is genuinely multipartite entangled throughout the interval.

## Prior literature and limitations

The closest relevant references are Chen–Jiang (2020), DOI 10.1103/PhysRevA.101.012308; Campbell–Tame–Paternostro (2009), arXiv:0903.3939; Kulkarni–Majumdar (2023), arXiv:2307.07485; Nawareg (2025), DOI 10.1007/s11128-025-04994-1; and the published two-excitation Dicke Pauli-spectrum result (2026). Full source access was incomplete for Chen–Jiang; publication priority remains subject to further inspection. The proof is confined to the named physical channel and perfect full-state resets.

Self-review: passed. Independent audit: not yet performed.
