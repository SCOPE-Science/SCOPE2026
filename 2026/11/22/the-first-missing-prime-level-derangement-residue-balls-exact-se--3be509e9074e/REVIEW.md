# Review of the exact seven-adic derangement frequency law

## Correctness — PASS

The proof fixes the exact derangement normalization, defines the seven-adic falling-factorial interpolation, and proves its convergence and exact local isometries on all seven input discs. The directly computed local derivative row has no zero entries. Unique lifting gives full residue-disc images and exact fibers at every power; the parity split then yields the claimed frequencies. The delivered Python checker independently verified all seven prime-level value/derivative entries and the complete counts for exponents one through five, with 19,665 exact assertions. The proof, not those finite checks, justifies the unrestricted quantifiers.

## Originality — PASS, qualified

Closest prior results include the general prime-adic derangement interpolation and period theorem of Miska (2015), the broader interpolation study of O'Desky–Richman (2020), previously indexed exact five-adic residue frequencies, and indexed two-/three-adic residue-image results. The inspected theorems neither state nor imply the evaluated seven-adic omission and multiplicity table; general lifting tools do not determine its seven local derivatives and values. The prime-five result uses the same method and constitutes a material methodology-overlap risk, but concerns a fully surjective image rather than the first prime-level omission. Historical work outside the inspected literature could cover the special case.

## Mathematical value — PASS

The first prime at which derangement residues fail to cover the prime field is a natural sharp boundary, in contrast to both the smaller-prime surjections and the prime-five full all-power image. The theorem determines the entire infinite tower of residue classes and exact multiplicities, not merely an isolated modular example or a tiny finite gain. The five-ball image and missing two-ball obstruction are intrinsic, reusable structural data for these classical counting numbers. This is a narrow complete classification; no downstream application or broader all-prime theorem is claimed.

## Limitations

The theorem concerns only the classical derangements at prime seven; it does not classify other primes or prove independent historical priority. The analytic interpolation framework and general least-period theorem predate this result. The code supplies finite corroboration only.

Self-review: passed. Independent audit: not yet performed.
