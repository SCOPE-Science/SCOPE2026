# Scientific review

## Correctness — PASS

The inverse DFT of intensity is exactly cyclic autocorrelation. Odd grid size separates the two cross-correlation lags and permits division by two modulo the length. The geometric attenuation product identifies the exact integer sum of the two support indices, whose combination with either observed lag identifies the unordered pair uniquely. Distinct attenuation values make the two zero-lag equations invertible, and one cross-correlation fixes the relative phase. The zero, one-sparse and two-sparse cases are individually covered. The one-mask lower bound follows from invisible impulses or scaled impulses at different locations. The even-grid impossibility follows from an exact conjugate antipodal pair for each real mask, not from numerical experiments. Reproduction with `CHECK.py` additionally passed 2,866 intensity reconstruction/counterexample tests and 905 exact support-signature checks. There is no claim of numerical stability.

## Originality — PASS, subject to literature risk

Huang and Li (arXiv:2608.02450, 2026) obtain a full-signal random-mask logarithmic guarantee, not the explicit two-mask classification on the two-sparse variety. Bandeira, Chen and Mixon (arXiv:1303.4458) consider masked phase retrieval with different mask and signal assumptions. The two-mask constructions surveyed by Jaganathan, Eldar and Hassibi (arXiv:1510.07713) use oversampling and generic/nonvanishing hypotheses. Ranieri et al. (arXiv:1308.3058) analyze the unmasked problem. Guerrero, Pinilla and Arguello (2020) study designed apertures and sparsity-based methods, but their inspected guarantees do not directly imply universal two-pattern unoversampled recovery of every two-sparse complex vector in odd dimension. Related cyclic short-time Fourier results concern window translations or ambiguity supports, rather than two diagonal attenuations. The genuinely distinguishing claim is the odd-order deterministic bounded-contrast two-mask theorem, decoder, and sharp mask count; the real-mask even obstruction is presented only as context.

Residual risks include a previously unnoticed deterministic two-sparse construction, especially in specialized coded-diffraction literature, and the unavailable complete main text of Li and Li (2021). Failed searches alone are not evidence of novelty. No independently performed literature audit is claimed.

## Value — PASS

Two-sparse Fourier phaseless recovery is a minimal nontrivial model for sparse coherent imaging. The result gives an explicit low-contrast acquisition design with no randomness, no Fourier oversampling, and universal rather than generic support-and-amplitude identification. The matching one-mask impossibility proves exact mask optimality, while the real-mask even obstruction distinguishes a genuine parity limitation in the same acquisition model. The reconstruction formula exhibits the arithmetic mechanism rather than relying on optimization or finite enumeration.

## Scientific limitations

The proof is exact/noiseless; conditioning can deteriorate with diminishing mask contrast and small coefficients. No claim extends to larger sparsity, missing measurements, noise, or complex-mask impossibility in even dimension. One plausible older paper was inspected only in abstract, and independent mathematical audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
