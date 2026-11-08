# Self-review

**Claim assessed:** For the eight-point family consisting of two concentric regular square orbits, global recovery of every quadratic complex polynomial from squared magnitudes holds exactly for distinct positive radii and nonresonant relative angle, and the full lifted singular spectrum and squared-product determinant have the specified closed forms. The count eight is minimal even among unrestricted complex phase-retrieval designs in dimension three.

## Correctness — PASS

Direct four-point discrete Fourier decomposition separates a diagonal block, two copies of an adjacent-coefficient block, and an outer-coefficient Nyquist block. With distinct positive radii and \(\sin(2\alpha)\ne0\), the real Hermitian kernel is exactly the line through \(\operatorname{diag}(uv,-(u+v),1)\); every nonzero element has rank three, so no difference of two rank-one positive lifts lies in the kernel. Each excluded parameter range has an explicit pair of distinct polynomials with identical intensities. Frobenius-orthonormal input and output transforms give the eight stated singular values and the squared-product determinant; symbolic two-row Gram factoring and direct numerical construction agree. The universal eight-sample lower bound follows from the odd determinant on any real two-plane in the nine-dimensional Hermitian lifting kernel of seven or fewer measurements, together with the rank-two obstruction. The quantitative bound follows from best rank-two approximation to the invertible kernel generator. The standalone checker passed 782 assertions. The proof, rather than those finite tests, establishes the universal claims.

## Originality — PASS, historical priority provisional

Closest primary full texts inspected: Chalendar–Partington, arXiv:2403.16255 (especially Theorems 2.11 and 2.16), proves equality up to phase from **complete traces** on disjoint circles; Bodmann–Hammen, arXiv:1302.5487 (Theorem 2.3), provides eight magnitude evaluations in dimension three on **intersecting** circles; Philipp, arXiv:1403.4769 (Theorem 1.1), uses a mixture of polynomial and derivative measurements; Conca–Edidin–Hering–Vinzant, arXiv:1312.0158 (Theorem 1.1 and Proposition 3.1), proves generic eight-measurement sufficiency and supplies the known rank-two criterion. None of these inspected theorems implies the exact nonresonant/degenerate parameter classification, complete block spectrum, or angular determinant maximizer for **two concentric four-point square orbits**. Related published records for three Hermitian measurements in dimension two and finite-grid trinomial peak minima are on different objects. Search coverage cannot rule out implicit equivalent calculations in earlier interferometric or low-redundancy-frame literature; this is an explicit residual priority risk.

## Mathematical value — PASS

A complex three-dimensional quadratic-polynomial model needs at least eight intensity samples for universal phase retrieval. The theorem gives a **highly symmetric, exactly minimal** eight-sample construction, a complete necessary-and-sufficient geometric design rule rather than a generic existence assertion, and the entire lifted spectral law. The sharp \(\sin^2(2\alpha)\) angular determinant dependence identifies the optimal orientation for the natural squared-product stability objective, and an explicit uniform rank-one-difference lower bound quantifies reconstruction robustness. These properties answer a natural sensor-placement question in finite Fourier and analytic-signal measurements. No arbitrary-radius minimax assertion is made.

## Limitations and close literature

The frame is restricted to the stated two square orbits and raw squared magnitudes. Sharp global Lipschitz constants and arbitrary eight-point design classification remain open here. The determinant objective is not interchangeable with full condition-number optimization. An earlier equivalent special construction could remain undiscovered despite the specified overlap comparisons. Independent mathematical audit and experimental validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
