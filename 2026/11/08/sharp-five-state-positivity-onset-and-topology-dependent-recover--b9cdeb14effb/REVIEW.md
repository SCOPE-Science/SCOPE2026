# Scientific review

**Claim assessed.** Sharp five-state onset and topology-dependent recovery for the implicit Taylor numerical transition on unit directed cycles and unit pure-birth Markov generators. Primary mathematical classification: 65L06. The source method is arXiv:2102.11939, first public 2021-02-23.

## Correctness — PASS

The domain and sign conventions are explicit. The one-stage inverse polynomial has poles at \(1\pm i\), outside the Markov spectra. Its fourth Taylor coefficient \(-1/4\) proves an actual negative distance-four transition at arbitrarily small positive steps for any size at least five; no extrapolation from finite tests is used. Exact rational inversions supply all positivity assertions for dimensions at most five. The five-state exceptional polynomials are \(5h^2(h+2)^2-4\) on a cycle and \(h^2(h+2)(h+6)-4\) for absorption; both increase strictly on positive steps and have unique positive roots. A spectral-projector argument on cycles and a Jordan derivative asymptotic for births prove eventual positivity for every fixed finite size. The exact-arithmetic checker passed 239 assertions and is provided with its actual output. It does not constitute a proof for all sizes; that scope rests on the written analysis.

## Originality — PASS, qualified

Gottlieb, Grant, Hu and Shu (arXiv:2102.11939) introduce the method and prove a positivity-preserving SSP theorem with a backward-derivative hypothesis. The hypothesis is inapplicable here: for the unit birth generator the matrix \(-Q^2\) has a negative distance-two off-diagonal element. Gottlieb and Grant (arXiv:2412.15142) repeat the method and conditional framework but do not supply the cycle and absorbing five-state thresholds in the inspected portions. Lóczi and Ketcheson (arXiv:1303.6651) provide general absolute-monotonicity theory, which does not logically imply the family-specific low-dimensional positivity or both sharp recovery equations. Two nearby public mathematical results concern [2/2] Padé and SDIRK2(2), not this [0/2] inverse Taylor map. Query-by-query implication comparisons, material read and residual risks appear in AUDIT.json.

The inspected material supports best-knowledge originality, not guaranteed historical uniqueness. The complete text of two nearby published database records was not available; their scientific summaries identify different numerical methods. Unindexed older literature is possible.

## Value — PASS

This is a natural complete boundary classification for two basic finite-state Markov semigroups, not an arbitrary parameter slice: the first forbidden graph size is the same in both geometries, but the exact recovery time differs. The result distinguishes positivity from spectral regularity and mass preservation, and reveals why increasing the time step can restore a physically necessary property after small-step failure. It is a useful test for applying conditional high-order SSP guarantees to network transport. No general theorem for arbitrary weighted Markov chains or nonlinear semigroups is claimed.

## Verification and limitations

Reproduce with `python checker.py` using SymPy. The linked analysis is self-contained and the code checks the finite polynomial certificates, not infinitely many graphs. At the sample step \(h=2/5\), the numerical five-cycle is nonnegative whereas the five-state absorbing chain is not. Exact semigroups stay nonnegative in both cases; no contradiction to the source SSP theorem is asserted. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
