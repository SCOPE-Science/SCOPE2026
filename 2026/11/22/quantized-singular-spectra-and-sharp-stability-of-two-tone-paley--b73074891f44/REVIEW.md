# Scientific review

## Correctness — PASS

The theorem fixes the Fourier normalization, input and target bandwidths, real positive amplitude, and exact quantifiers. Expanding the two shifted Fourier copies gives the operator identity \(T^*T=(1+r^2)I+r(S_{2\eta}+S_{2\eta}^*)\) on the input spectrum. A unitary residue decomposition with step \(2\eta\) has chain lengths \(\lfloor\sigma/\eta\rfloor\) and \(\lceil\sigma/\eta\rceil\), with each occurring on a positive-measure set where nonzero. A finite path's normalized sine eigenvectors yield every spectral number, its multiplicity, and the attained endpoint gains. The strict lower bound is positive even for the zero-bearing equal-amplitude multiplier. The integer-bandwidth jumps and small-frequency limit follow directly; the included script independently checks finite Gram identities and eigenvalues (`TWO_TONE_PALEY_WIENER_CHECK_OK 40704`). No finite experiment is used to prove an infinite statement.

## Originality — PASS (qualified)

The closely relevant arXiv:2508.19975 develops the spectral and dynamical theory of *unweighted composition operators*, which is not a positive-Gram spectral classification of two-tone multiplication between Paley–Wiener spaces. The earlier range treatment arXiv:1006.2793 discusses allowable weighted composition maps and bandwidth but does not provide this complete singular spectrum or attained sharp bounds. The contemporary arXiv:2611.21261 gives general boundedness and norm-comparison criteria for weights, including multipliers, but not these integer resonance eigenlevels or an exact inverse gain. Also compared were nearby weighted-bandlimited embeddings and Fourier concentration results, whose operators, supports and quantified conclusions differ. The chief residual novelty risk is implicit coverage by a more general Fourier-fiber or periodic shift theorem, since the finite path formula itself is classical. Database nonappearance alone does not establish novelty.

## Value — PASS

A multiplier may have infinitely many real zeros yet remain uniformly bounded below on a fixed bandlimited Hilbert space. Here the exact lower gain, upper gain, all singular levels, their multiplicities, infinite-dimensional extremizers, and resonance jumps are classified simultaneously for all positive bandwidths and tone ratios. This supplies a quantitative stable-recovery theorem and identifies how adding one Fourier overlap edge causes discontinuous conditioning changes. The finite path adjacency formula is standard, but the specified bandlimited operator's complete sharp stability diagram is a natural coherent application rather than an arbitrary discrete slice.

## Limitations and closest comparisons

The result is limited to a contiguous frequency band, two exponential tones, and the Hilbert \(L^2\) setting. It is not claimed that general finite path spectra or the Fourier shift identity are new. Closest inspected texts: Álvarez–Severiano arXiv:2508.19975 (composition spectra); Mukherjee–Jafari–McInroy arXiv:1006.2793 (weighted composition range); Hai–Huy–Tien arXiv:2611.21261 (general weighted composition bounds). Literature completeness and independent mathematical review remain open.

Self-review: passed. Independent audit: not yet performed.
