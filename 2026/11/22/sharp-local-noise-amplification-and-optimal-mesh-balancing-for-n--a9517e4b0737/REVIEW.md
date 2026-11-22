# Scientific review — sharp local nonuniform PCHIP noise amplification

## Correctness — PASS

The claim is a global two-input Lipschitz coefficient for monotone data, not an interpolation error estimate. The proof starts from the four-node cubic Hermite formula and weighted harmonic-mean interior derivatives. The four data Jacobian signs are respectively negative, positive, positive, negative, their sum is one by translation equivariance, and the two negative magnitudes are uniformly bounded by the displayed rational functions of consecutive knot lengths. Sending both *outer* secants to zero at a fixed positive central secant makes both upper bounds sharp in the same limiting configuration; a sign-matched perturbation stays inside the nondecreasing cone. Strict convexity of the mesh coefficient, plus the midpoint lower bound, establishes unique optimal balancing at fixed outer-length sum. The uniform and graded examples and small-neighbor asymptotic follow algebraically. The standalone exact-fraction verifier passes 1,200 two-input bounds, 1,000 Jacobian bounds, three sharpness witnesses and 300 balancing checks. The finite tests do not replace any universal proof.

## Originality — PASS (historical priority provisional)

Fritsch and Butland (1984), SciPy's documented PCHIP formula, and Aràndiga, Baeza and Yáñez (2021) cover the harmonic-mean slope and monotone interpolation, so neither is claimed new. Aràndiga, Donat and Santágueda (2016) study stability of the iterated *uniform-grid subdivision scheme*, rather than this exact single-cell nonuniform, two-input pointwise amplification or minimax balancing. Baeza, Donat and Martínez-Gavara (2024), available as full HTML, use monotonicity-preserving interpolation for multilevel balance laws but do not give this coefficient. Two closely related mathematical records give sharp *total variation* constants for, respectively, uniform harmonic-mean Hermite and nonuniform **Steffen** Hermite; their conclusions do not imply the claimed nonuniform PCHIP maximum-norm coefficient. Original 2013 nonuniform monotone Hermite work and the full 2016 subdivision article remain historical-priority risks (abstracts and secondary descriptions inspected; full articles not inspected). Searching for aliases and result-level implications did not reveal a stronger published theorem, but this is not a proof of novelty.

## Value — PASS

The mathematical gap is material to placing sensors or interpolation knots for monotonicity-preserving multilevel numerics: preservation of each signal's range does not bound the *sensitivity of the difference* between two signals. The exact pointwise profile identifies where noise amplification is largest, while the unique balanced-neighbor design is a natural minimax choice when the total neighboring mesh length is fixed. Unbounded gain under neighbor collapse is a structural mesh-conditioning obstruction rather than an arbitrary computed constant.

## Scope and outstanding limits

Only four consecutive knots and the middle cell of the standard nonuniform PCHIP interior rule are covered; endpoint cells, moving knots, oscillatory data and distributional noise were not analyzed. Independent mathematical validation and definitive historical-priority review have not been performed.

Self-review: passed. Independent audit: not yet performed.
