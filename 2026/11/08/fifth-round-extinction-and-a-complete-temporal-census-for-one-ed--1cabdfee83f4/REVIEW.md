# Review: Fifth-round extinction and a complete temporal census for one-edge-defective bipartite excitation

## Correctness

PASS. The proof states the precise three-state update and all graph-size quantifiers, reduces the infinite two-parameter graph family to exactly 441 support signatures, and separately verifies that each of 41 periodic signatures lifts to labelled periodicity with precisely the recorded period. Exhaustive integer transition classification supplies the fifteen matrices. Inclusion–exclusion gives the exact weights; in particular \(N_{5,1}=2^m+2^n+2\). The standalone quotient and direct graph implementations both passed. The latter is corroboration, not a proof by finite extrapolation.

## Originality

PASS with historical caveat. The relevant full arXiv manuscript by Gravner, Lyu and Sivakoff (2016, Section 2 Theorem 3 and Section 4) gives global synchronization and activity criteria. Its diameter bound, plus refractory cooldown, already gives the five-update **upper bound** for synchronizing inputs; it does not imply the new exact last-layer count, the oscillator entry census or primitive orbit counts. The foundational Greenberg–Hastings (1978) abstract concerns excitable spatial patterns rather than this complete finite graph class. The intact-biclique results address no deleted edge, and a three-color **cyclic contact** model on the same defective graph has a different local rule and different quantitative behavior. No covering claim was found in the available mathematical literature and indexed-result searches, but unindexed equivalent work remains possible.

## Mathematical value

PASS. A one-edge perturbation changes the sharp transient cutoff from four to five while creating an exactly quantified exponential-sized but vanishing-proportion late-extinction layer. The complete fifteen-class census and primitive-period counts classify the recurrent and transient responses, rather than merely producing an isolated edge-effect example.

## Limits and verification status

The result concerns exactly the stated deterministic graph family and local rule. Numerical graph-size tests are finite, while the 441-case reduction and lifting proof cover all graph sizes. The first Greenberg–Hastings article was only available at abstract level here; hidden historical duplicates cannot be ruled out. No external mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
