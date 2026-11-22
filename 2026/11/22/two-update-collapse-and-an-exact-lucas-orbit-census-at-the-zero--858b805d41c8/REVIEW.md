# Self-review

## Correctness — PASS

The claimed statement concerns every binary configuration on each periodic \(H\)-by-\(W\) board with \(H,W\ge4\) and coincident intervals \([0,\varepsilon]\), \(0\le\varepsilon<1/(9HW)\). Positive normalized field values cannot fall in that interval, since the unnormalized positive products are positive integers and the normalization maximum is at most \(9HW\). The original two-dimensional rule therefore reduces exactly to a union of zero-row and zero-column masks, not an approximation. The case split handles empty masks, two nonempty masks, and one nonempty mask, including the absorbing empty state. On a stripe the update is closed-neighborhood NOR, which satisfies \(T^3=T\) by the adjunction identities for dilation and erosion. This gives \(F^4=F^2\), with a one-live-cell witness showing that entry time two is sharp. Every nonempty recurrent state is an eligible stripe; the 4-state transfer graph counts precisely the nonempty nonfull closed binary rings. Its characteristic polynomial yields the stated Lucas and six-periodic correction. The independent full-grid enumeration in `checker.py` verifies the reduction's all-state consequences on two small grids, and the one-dimensional exhaustive checks cover lengths 4 through 13. These checks supplement, not prove, the unbounded claims.

## Originality — PASS within inspected evidence

Shi and Huang's original June 8, 2026 model [1] motivates an exact regime classification; the inspected original equations and available scientific descriptions present numerical phases, not the present zero-field theorem. A published analysis [2] treats the opposite near-*maximum*-field interval \([1-\eta,1]\), showing eventual rectangle dynamics and at most period two, but not the zero-field union-of-stripes mechanism, uniform two-update horizon, or exact periodic populations. Another analysis of the same model concerns a nonzero-threshold stripe subsystem corresponding to Rules 54/18, not the NOR dynamics here. Ordinary mathematical morphology [3] supplies the standard closing identities used in the proof; it does not specify the global normalized model's cross-mask update or its complete finite-torus orbit population. The closest available published-result summaries and direct semantic searches did not establish a dominating statement. Full-text priority access to the source preprint and some repository records was incomplete, so historical equivalence remains a residual risk; the search evidence is not a uniqueness proof.

## Mathematical value — PASS

The two equal endpoint intervals at the zero-field boundary are intrinsic to the normalized separable-field model, not a randomly selected numerical slice. The positive-width guarantee makes this a robust finite-board regime. Unlike the source's numerically observed long transients and the previously studied opposite near-maximum endpoint, the zero-field regime has a *sharp universal two-update cutoff* and a closed, all-size count of each primitive temporal orbit. The coupling between rows and columns is essential to the transient case split; the recurrent-state census identifies both the spatial geometry and exact multiplicity of all surviving two-cycles. This is a natural solvable boundary against which other numerical phase classifications can be compared, although it does not determine basin sizes or larger threshold widths.

## Closest sources and limitations

[1] X. Shi and M. Huang, *Dynamics in a Low-Rank Separable Field Cellular Automaton*, arXiv:2606.08983 (2026-06-08), especially section 2.1.

[2] *A sharp near-max selection window and a global two-cycle cutoff for a separable-field automaton* (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-near-max-selection-window-and-a-global-two-cycle-cutoff--cc868950d182 . The indexed scientific summary was available; the repository's complete paper was not retrieved.

[3] Standard mathematical-morphology dilation/erosion adjunction and idempotent closing, https://en.wikipedia.org/wiki/Mathematical_morphology .

The positive-width threshold \(1/(9HW)\) is sufficient but not claimed optimal; the theorem concerns only the stated finite cyclic dimensions, equal threshold windows, and empty-state convention. A complete PDF of [1] was not obtained for a whole-document originality comparison. No independent mathematical audit is represented.

Self-review: passed. Independent audit: not yet performed.
