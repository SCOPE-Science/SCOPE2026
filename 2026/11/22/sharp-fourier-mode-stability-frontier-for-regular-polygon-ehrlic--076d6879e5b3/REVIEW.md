# Mathematical review

## Correctness — PASS

The proof computes the exact denominator on a roots-of-unity orbit, differentiates the full simultaneous update including all off-diagonal dependencies, and diagonalizes the resulting circulant. The finite Fourier-sum recurrence is valid for every integer degree at least two; its extremal coefficient gives the sharp Euclidean-norm threshold. An independent exact-polynomial checker confirms relevant identities for degrees 2–40 and finite-difference derivatives for degrees 2–12. The checker is a consistency test, not a substitute for the arbitrary-degree proof. The order of updates, exclusion of poles, and distinction between scalar convergence and full-space linearization are explicit.

## Originality — PASS, with historical-priority qualification

The closest directly relevant published results study the same simultaneous root finder but prove generic nonconvergence by attracting cycles (Grabbel–Srkalovic–Schleicher, arXiv:2611.02143), divergence under other polynomials/starts (Reinke, arXiv:2011.01660), and comparative efficiency and conventional cubic local convergence (Shemyakov et al., arXiv:2004.03217). None of their examined full texts states the exact Fourier eigenvalues for the binomial root family, nor a sharp positive-radius ambient norm frontier. The radial cubic convergence is not claimed as original by itself. Related historical literature and unindexed work could contain the spectrum; targeted searches cannot logically exclude that possibility.

## Mathematical value — PASS

Full-space perturbation sensitivity can be worse than the convergence behavior visible within the invariant symmetry class. The result identifies, for every degree, the exact spectral norm, worst Fourier direction, and sharp radius threshold for that discrepancy. This is a motivated numerical root-finding stability benchmark and explains why an apparently well-behaved symmetric initialization can transiently magnify nonsymmetric roundoff or starting perturbations.

## Closest literature and limitations

The ambient threshold is differential and one-step only; it does not prove divergent nearby orbits and does not generalize to arbitrary polynomials, arbitrary starts, sequential updates, or floating-point arithmetic. Historical priority remains qualified by possible unindexed special-case derivations, particularly in early numerical-algorithm literature. The full texts of arXiv:2611.02143, arXiv:2011.01660, and arXiv:2004.03217 were examined in relevant sections.

Self-review: passed. Independent audit: not yet performed.
