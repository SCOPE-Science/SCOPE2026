# Scientific review

## Correctness — PASS

The real Frobenius-orthonormal Hermitian basis and unitary four-point Fourier decomposition produce mutually orthogonal DC, first-harmonic, and Nyquist sectors. Their exact singular values reconstruct all eight output singular values. The DC block has rank two, each lag-one block is strictly invertible because \(a>c\), and the Nyquist block has rank two exactly when \(\sin(2\eta)\ne0\). The largest singular value is always the DC plus mode; comparison of the least fixed singular value with the smaller Nyquist singular value proves the sharp condition number, plateau, and reciprocal-distance blow-up. The attached numerical checker directly constructs the full lifting matrix and tests the derived values; these tests do not replace the proof.

## Originality — PASS relative to the inspected sources

The motivating 2026 two-frequency-bin Morlet/Gaussian work establishes infinite-sample uniqueness for square-integrable bandlimited functions, not the finite three-atomic signal singular spectrum. Generic eight-vector phase retrieval work establishes an injectivity threshold, not the exact structured condition number. The qualitative eight-sample phase retrieval criterion for two rotated four-point circles is already known; no novelty is claimed for that criterion. The added quantitative content is the complete eight-value Hermitian-lifting spectrum, sharp best stagger set, and instability coefficient. Targeted searches of equivalent angular spectra, Gaussian-bin aliases, and finite structured phase retrieval designs revealed no explicit dominating result.

## Mathematical value — PASS

Eight phaseless samples meet the generic \(4d-4\) complex-dimension-three threshold. Exact linear-lifting singular values quantify how much noise that minimally sampled design amplifies and distinguish a unique quarter-grid optimum from a plateau of optimal offsets; the singular degeneration at aligned offsets has an exact sharp coefficient. These are practical quantitative design properties beyond mere existence of uniqueness.

## Limitations and risks

The result does not assert optimal nonlinear reconstruction stability or stability among all possible intensity designs; it covers this symmetric Gaussian-bin two-grid family alone. Earlier studies of discrete phaseless Fourier sampling could have obtained a specialized equivalent spectrum under a different normalization, and priority is not independently certified. The recorded full-text inspections concern the most directly motivating 2026 paper and the general eight-measurement comparison; lower-ranked adjacent results were compared by abstract and accessible statements only.

Self-review: passed. Independent audit: not yet performed.
