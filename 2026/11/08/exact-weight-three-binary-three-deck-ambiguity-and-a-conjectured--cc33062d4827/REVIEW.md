# Scientific review: exact weight-three three-deck equivalence

## Correctness (C): PASS

The claim is quantified over all binary length-\(n\) words with exactly three ones, \(n\ge3\). The three two-one subsequence counts constrain any gap-vector difference to an integral multiple of \((1,-3,3,-1)\). The \(001\) count then gives exactly two possibilities for that multiple, one zero and one determining the unique candidate partner. For the second possibility, the one-zero counts are shown to agree from the first two moments of the three prefix-zero counts. This verifies necessity and sufficiency for all eight deck entries and rules out larger fibers. A uniquely oriented parametrization of each pair derives the exact generating function. The claimed quasipolynomial and asymptotics follow by elementary coefficient extraction. Direct independent enumeration and the packaged standalone program corroborate the finite cases; finite enumeration is not substituted for the infinite proof.

## Originality (O): PASS, with remaining source risk

The exact generating function is **Conjecture 1** in the full text of Chrisnata et al., *On the Number of Distinct \(k\)-Decks: Enumeration and Bounds*, Section 5.3. The paper gives the critical null vector, partial inequalities, a first collision, an \(\Theta(n^3)\) bound, and finite checks of its conjecture, but not a proof of the generating function or a complete ambiguity involution. The present proof explicitly credits those ingredients, completes the missing equivalence criterion, and enumerates all collision classes.

Nilforoushan–Parvaresh (September 19, 2026) classify the algebraic degrees of freedom for general three-decks and prove global \(\Theta(n^9)\) growth; these statements do not determine the exact fixed-three-one slice. Angal et al. (October 30, 2026) prove restricted reconstruction bounds but no equivalence enumeration at three ones. Lejeune–Rigo–Rosenfeld give general binomial-equivalence results and a two-binomial algorithm, not this solution. Database semantic searches on the conjecture, exact rational generating function, gap involution, and associated aliases returned no equivalent result. A literature search is not a uniqueness proof; unindexed or later equivalent work is a residual risk.

## Value (V): PASS

This is an explicitly motivated mathematical gap: the formula itself was conjectured as an open problem in Section 5.3 of Chrisnata et al., after they established only a cubic-order bound and a finite table. The new exact all-length proof supplies a stronger structural classification of every three-deck fiber, a closed period-four doubleton-count quasipolynomial, and the optimal size and limiting density of zero-error readout codes at fixed content. The exact constant \(7/8\) and constructive partnership criterion are intrinsic to that decoding question. This is more than a numerical extension, verification of known table entries, or a generic instance of a general bound.

## Closest literature and residual limitations

- Chrisnata et al., DOI:10.3934/amc.2021032, Section 5.3, Conjecture 1: formula conjectured, small cases checked, preparatory linear relations and lower bound proved.
- Nilforoushan and Parvaresh, arXiv:2609.23106: general three-deck independent-coordinate and asymptotic results, without exact fixed-weight-three fibers.
- Angal et al., arXiv:2610.41110v1: restricted reconstruction thresholds, without the all-length fixed-weight-three equivalence census.
- Lejeune, Rigo and Rosenfeld (2020): general binomial equivalence, especially the two-binomial case.

Scope is restricted to exactly three ones in a binary linear word and the exact scattered three-deck. The check does not establish a universal absence of previous proofs, and no independent mathematical audit has yet been performed.

Self-review: passed. Independent audit: not yet performed.
