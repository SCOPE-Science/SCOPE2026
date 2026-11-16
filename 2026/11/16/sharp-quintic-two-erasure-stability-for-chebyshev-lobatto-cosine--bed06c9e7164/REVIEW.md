# Scientific assessment: two-erasure Chebyshev–Lobatto sampling

## Correctness — PASS

The statement is for exact orthonormal type-I discrete cosine sampling, with \(N+1\) Lobatto observations and exactly two erased rows, retaining Chebyshev degrees at most \(N-2\). The proof derives the complete spectrum from an orthogonal-matrix complement, evaluates the two-dimensional trace and determinant exactly, and shows positivity for every two-erasure pattern. Its worst-pattern classification is proved for every \(N\ge4\) by an explicit uniform lower bound on the smallest complementary eigenvalue, compared against an endpoint-pattern Rayleigh upper bound. The bounded comparisons separate interior pairs, non-nearest endpoint pairs, and the two-endpoint pair; no unexamined erasure cases remain. Taylor expansion yields the fifth-power asymptotic constant. The packaged checker passed 52,800 independent finite assertions, including direct singular-value comparisons. The proof does not rely on finite enumeration.

## Originality — PASS with provisional historical priority

The closest open-access primary paper is Weisbrich–Malissiovas–Neitzel (2021, DOI: `10.1515/jag-2021-0010`), inspected in its entirety in HTML, including its Chebyshev-node definition, numerical approximation methods and conclusion. It studies intact-grid interpolation and point-cloud noise, not optimal two-erasure Fourier sampling spectra. Goren–Zamir (2021, DOI: `10.1109/TIP.2021.3087404`) is a relevant earlier application of DCT erasure sensitivity, but only its published abstract could be inspected; equivalent detailed calculations cannot be ruled out. The publicly available full result *Single-erasure boundary layers for Chebyshev–Lobatto interpolation* (published-finding corpus identifier `a3c5beff381f`) studies a different \(L^\infty\) norm and exactly one erasure. Existing Gauss-grid two-erasure analysis uses type-II rather than type-I cosine nodes and does not determine the displayed quintic constant. Search results did not show an equivalent theorem, but search absence alone is not evidence of originality. This review compares the exact mathematical statements, including the sampling normalization and extremizer classification.

## Mathematical value — PASS

Two-erasure tolerance is a natural reliability question for near-Nyquist spectral sampling. The theorem gives both a uniform finite-size complete singular spectrum and a sharp worst-case erasure design classification, allowing precise weighted \(\ell^2\) noise-amplification prediction for any failed pair. The new fifth-power law distinguishes endpoint-containing Lobatto measurements from half-shifted Gauss measurements, where the extreme stability exponent is seven. This difference is not a relabeling of a parameter: the quadrature boundary nodes, complementary high-frequency functions, and their near-alignment geometry change the leading power. The result makes no unsupported downstream application claims.

## Limits

All statements concern the explicitly weighted exact coefficient-to-observation matrix and squared \(\ell^2\) condition ratio, not ordinary pointwise Lebesgue norms or unweighted data. Published DCT coding details not accessible in full remain a historical-priority risk. There has been no independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
