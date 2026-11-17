# Self-review

## Correctness — PASS

For the specified nonuniform Steffen tangent map, the coordinatewise derivatives of each knot slope belong to \([0,2]\) almost everywhere. The Hermite derivative basis is nonnegative in the relevant two-parameter square and integrates to one. Each neighboring derivative basis has \(L^1\)-integral exactly \(8/27\). Therefore the complete column variation of a one-secant perturbation is at most the coefficient in the theorem. Summing changed columns establishes the two-input estimate; BV truncation is justified whenever the coefficient is finite. An explicit strict-branch choice simultaneously saturates both neighbor derivatives and attains the sharp bound for any chosen cell. The bundled exact-rational checker confirms the basis identities and a sample attaining \(107/27\); the infinite theorem relies on the complete analytical argument, not on numerical trials.

## Originality — PASS, qualified

The indexed and accessible prior record includes uniform-grid Hermite norm results, nonuniform monotonicity/accuracy studies, and a distinct \(Q_1\) averaging TVD operator. The new conclusion is an exact two-input BV norm of Steffen interpolation for *every fixed nonuniform grid* and a necessary-and-sufficient neighboring-cell ratio criterion; these statements are not logically implied by the compared results. The original Steffen article from 1990 and the most relevant 2013 nonuniform Hermite study were unavailable in full text. They are named material residual priority risks; a negative search is not proof of historical uniqueness.

## Mathematical value — PASS

The theorem locates a structural conditioning boundary that individual-signal variation preservation conceals. The formula is sharp at every chosen cell, and an unbounded mesh-ratio condition yields a genuine loss of global two-input BV Lipschitz regularity. This gives a mathematically motivated quantitative diagnostic for shape-preserving interpolation on locally refined meshes.

## Limits and closest literature

The result does not pertain to moving knot positions, finite interval boundary prescriptions, or other monotone Hermite selectors. The uniform-grid special case alone would not merit a new claim; the proof and value concern the entire nonuniform mesh family and the sharp necessity of shape regularity. References and the precise inspection limitations are in `RESULT.md` and `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
