# Scientific review

## Correctness (PASS)

The integer state domain is the complete grid \(S\) with \(6401\) states. The formula's branch boundaries, nearest-even tie convention, and coefficients are fixed explicitly. Two independent exact successor-evaluation methods agree on every input, and two global graph algorithms independently yield all recurrent periods, basin sizes, maximum transients, and the \(5122\) changed successors. The attached checker is the complete finite computational certificate. No result on infinite real trajectories is inferred.

## Originality (PASS within accessible evidence)

The primary 2023 electronics study reports approximate and fixed-point trajectories and notes 16-bit discrepancies, but it does not give the precise two-map exhaustive census. The 2021 original article treats exact-real chaos, and accessible exact-real related results address Lyapunov floors, real period-three cycles, or attracting resonance windows. These do not imply the finite-scale, explicitly rounded successor graphs. Exact finite-precision studies of other interval maps do not provide the same-map answer. The 2021 article was only available in publisher preview; full-text priority remains uncertain.

## Value (PASS)

The chosen parameter is the article's exact chaotic hardware-study example, and the seven-fractional-bit state representation directly addresses low-width recurrence. Exact whole-grid period/basin inventories give a useful diagnostic for numerical fidelity; the difference is not just an illustrative short trajectory. No general hardware or cryptographic conclusions are suggested.

## Limitations and priority risk

The coefficient-quantized version is an idealized model with the same branch boundaries, not a verified FPGA execution. The 2021 primary full text and some later closely related full texts were inaccessible. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
