# Mathematical review of a fractional sine-map period-three window

## Correctness — PASS

The source map is normalized exactly by \(r=e/\mu\). The rational intervals \(I_0,I_1,I_2\) and rational parameter interval \(R\) satisfy strict cyclic image inclusions, with derivative signs \(+,+,-\) and combined derivative between \(-0.499\) and \(-0.479\). Banach contraction of the third iterate proves a genuine primitive attracting three-cycle for every parameter in \(R\), not just a numerically observed orbit. The exact-rational checker derives its trigonometric bounds from the Machin arctangent identity and Taylor remainder estimates; it was executed successfully. Its calculations can be reproduced using only Python's standard library.

## Originality — PASS within inspected evidence

The accessible originating paper's Sections 2.1–2.3 provide fixed-point and numerical studies and claim absence of periodic windows in the specified robust-chaos region; they do not provide an attracting three-cycle certificate. A public 2026 mathematical synopsis concerning the same rational sine map gives the exact period-two threshold, which neither implies nor excludes a primitive attracting period-three orbit. Comparisons to the standard sine-map and rational-logistic three-cycle literature involve different maps or parameters. Exact-phrase and equivalent-form searches found no statement proving this specific interval and multiplier bound. This search cannot exclude unindexed or uninspected equivalent work.

## Value — PASS

A rigorously certified positive-width attracting periodic window directly tests an explicit, application-relevant assertion about the chaotic behavior of a named published map. The result identifies a concrete dynamical failure mode of a claimed robustly chaotic parameter range; the counterexample is a global-in-time existence theorem, not a short numerical negative check. No cryptographic-security inference is asserted.

## Limits and risks

This proves a nonempty subwindow but not a sharp window boundary, complete period-three census, or global basin classification. Coexisting chaotic invariant sets are not ruled out. General unimodal-map theory and unindexed studies could contain closely related examples, and the 2026 same-family research comparison was available as a synopsis rather than full mathematical text.

Self-review: passed. Independent audit: not yet performed.
