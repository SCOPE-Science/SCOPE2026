# Review of exact primitive-two-cycle census

## Correctness — PASS

The proof exhausts negative, zero and positive states. The negative half-line is strictly ordered, excluding swapped pairs. All positive swapped pairs satisfy a sign-sensitive product identity and split exhaustively into same-side and cross-side cases. Each case is reduced to an explicit polynomial and every resulting pair is checked in the original recurrence. Threshold equalities and neutral multipliers are treated separately. A symbolic expansion proves the complete factorization of \(f_\eta^2(t)-t\), and the multiplier identities and root threshold were independently recomputed within the same mathematical review. The standalone symbolic checker provides reproducible calculations; it does not replace the infinite-domain proof.

## Originality — PASS under available-source comparisons

The 2024 originating article (https://doi.org/10.28919/afpt/8562, Section 4) gives numerical period-two examples for the \(n=2\) branch, not an exact all-real census or the \(\eta>8\) external attracting branch. The full text was read in the relevant construction, fixed-point and numerical-cycle sections; exact parameter and period searches found no equivalent theorem. Franco-Medrano and Solis (https://doi.org/10.1155/2015/680970, Sections 2.1–2.2 and conclusions) analyze cubic fixed-point stability and explicitly say period-two points cannot generally be calculated by their method. Their general setting contains cubic maps, but their **stated conclusions** do not imply these explicit orbit counts and multipliers. Indexed closely related cubic Allee-logistic classifications require nonnegative growth coefficients and cannot be specialized to a factor with coefficient \(-1\). Other indexed results concern distinct maps. Risks: unseen preprints or full-text passages in other cubic-map references may establish equivalent parameter-dependent formulas; novelty is evidence-relative, not proved by search failure.

## Value — PASS

The full real-line phase space is expressly studied in the originating family. The complete period-two census reveals an external saddle-node at \(\eta=8\), an exact narrow attracting interval after the familiar inner attractor loses stability, and a geometric explanation for why this window is absent from simulations limited to \([0,1]\). The two window boundaries and the cycles themselves are exact natural invariants, not arbitrary sample parameters. No claim is made that the external attractor models nonnegative population dynamics within a carrying-capacity interval.

Self-review: passed. Independent audit: not yet performed.
