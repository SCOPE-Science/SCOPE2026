# Scientific review: binary two-burst deletion sphere fluctuations

## Correctness

**PASS.** The domain is binary independent uniform source words of length \(n\ge4\) and exactly two disjoint length-two deletion bursts, with distinct outputs rather than multiplicity-weighted histories. Canonical maximal histories are counted once using the published burst-deletion normal-form theorem. For two bursts the resulting sphere size is exactly the quadratic polynomial (1) in the independent fair delayed-difference indicators. Expanding in centered indicators proves the exact mean and variance by orthogonality, and separates an order-\(n^{3/2}\) independent-sum fluctuation from an order-\(n\) quadratic remainder. The independent direct-output checker confirmed the formula and exact moments for all binary words of lengths 4–13, plus 1,000 larger samples. The published normal-form lemma is a necessary premise and is properly attributed.

## Originality

**PASS against the examined record, with priority uncertainty.** Wang et al. (arXiv:2606.01245) provide canonical representations, bounds, and arbitrary-word tools for multiple burst-deletion spheres. Lan et al. (arXiv:2504.20460) establish an extremal sphere-size formula. The new claim is the explicitly evaluated source-averaged variance and an asymptotic Gaussian law in the two-disjoint-double-burst binary channel. The deterministic canonicalization is stronger than an individual pointwise count, but neither inspected source states or computes the claimed second moment or limit law. The transformation to independent delayed differences and centered quadratic orthogonality are the additional arguments. The analogous known exact variance for two *individual* deletions concerns a different channel. This review cannot establish absolute priority against all earlier sources.

## Value

**PASS.** Error-ball size is a natural measure of output ambiguity in deletion/reconstruction channels. The known exact worst-case formula does not describe the typical-center variability. An exact finite-length variance and central limit theorem provide a fluctuation scale \(n^{3/2}\), a sharp leading dispersion coefficient, and a Gaussian approximation across all binary source lengths. This is information about the random-source channel that worst-case sphere maxima alone do not provide. The result does not by itself yield a coding-rate improvement.

## Closest sources, scope and risks

The main scientific inputs are Wang–Kong–Yaakobi–Duman (2026), Propositions 1–2, and the extremal baseline of Lan–Sun–Yu–Ge (2025). An indexed result on the variance of two *single-symbol*-deletion balls is mathematically distinct. Residual risks include undiscovered earlier averaged-sphere formulas and dependence on the published canonical representation theorem. No claims are made for larger alphabets, unequal source laws, or more bursts.

Self-review: passed. Independent audit: not yet performed.
