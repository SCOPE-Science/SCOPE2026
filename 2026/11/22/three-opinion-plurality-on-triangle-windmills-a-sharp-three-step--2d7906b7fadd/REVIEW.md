# Scientific review: three-opinion plurality on friendship graphs

## Correctness — PASS

The claim is a universal finite-state theorem with explicitly defined graph, colors, synchronous open-neighborhood rule, and incumbent-retention tie convention. The local two-neighbor petal argument proves that every peripheral edge becomes monochromatic by the second update unless the hub initially stays fixed, in which case a third update suffices. With fixed petals, the hub selection map is idempotent. The sharp time-three threshold is supported by three explicit residue-class witnesses and a complete, symmetry-reduced exact enumeration of all cases with one through four petals. A multinomial decomposition proves the exact fixed-state count; a constant-term integral and Laplace asymptotics give the square-root law. A two-coordinate concentration argument proves the exponentially small three-update tail and the limiting first-entry fractions. The included standard-library checker reproduces the compressed full-state counts through ten petals and the independent labelled-graph counts through five petals. The analytic proof, not bounded experimentation, establishes all-size assertions.

## Originality — PASS, qualified

The closest same-graph prior results give (i) a binary majority fixed-point/basin census with two-step stabilization and (ii) three-color threshold-two *cyclic successor* dynamics with genuine three-cycles. Neither statement implies a three-opinion tie-retaining plurality theorem: the update maps disagree on mixed petals and even on the existence of oscillations. The earlier general multicolor plurality theorem of Mossel, Neeman and Tamuz assumes *no ties* and proves an eventual period bound, not a sharp three-step transient, hub retention law, or exact equilibrium count on this graph. The surveyed many-opinion gossip dynamics samples neighbors randomly; the alternative deterministic three-opinion rules use different change criteria. Searches for plurality, friendship/windmill graphs, hub-pair locking, exact equilibrium growth and three-color first-entry distributions found no covering result. Indexed and searchable sources cannot exclude an unindexed or differently expressed historical equivalent.

## Value — PASS

Friendship graphs are a canonical family with a universal hub and independent triangle petals. The three-opinion extension is structurally different from binary majority: an additional sharp third step appears precisely from five petals onward, while the equilibrium population gains a nontrivial square-root correction to its exponential growth. The near-sure preservation of the hub's first color coexists with a limiting two-point relaxation-time law. These joint exact, asymptotic and sharp-boundary facts give a meaningful interpretable model of locally shared-neighbor plurality, not an arbitrary finite sample or a reparameterized earlier calculation.

## Limitations and closest coverage

The result does not characterize individual equilibrium attraction basins and does not extend to random tie-breaking, unequal opinion probabilities, more than three colors, or arbitrary triangle cacti. Reproducibility certificates cover finitely many sizes, while the proof handles unbounded sizes. Related primary sources are the 2012 multicolor plurality analysis of Mossel, Neeman and Tamuz (tie-free weighted graphs), the 2013 binary-majority work of Tamuz and Tessler, and the published binary and cyclic-successor friendship-graph results listed in RESULT.md. Their hypotheses and conclusions were compared rather than assuming distinct titles prove novelty.

Self-review: passed. Independent audit: not yet performed.
