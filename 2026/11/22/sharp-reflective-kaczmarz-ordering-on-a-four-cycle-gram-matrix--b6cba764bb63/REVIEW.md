# Self-review

## Correctness — PASS

All hypotheses, boundaries, and order quantifiers are explicit. The positive Gram spectrum ensures the four normalized row vectors exist in the stated interval. Products of the exact four row-basis reflection matrices give both characteristic polynomials for all 24 permutations, with exhaustive counts 8 and 16. Eigenvalue location, strict gap ordering and the boundary ratio follow from exact algebra. The standalone checker reproduces the exact permutation census, symbolic identities and independent numerical coordinate realizations; numerical samples do not replace the universal proof.

## Originality — PASS (qualified)

Shao's foundational reflective-Kaczmarz paper defines the inverse-angle objective, and the 2024 follow-up (Theorem 5.18) explicitly gives the already-known general characteristic determinant, attributed to Coxeter (1939). Neither inspected paper states the exact optimizer among the 24 orders for the positive four-cycle Gram family, or the strict comparison and sharp boundary ratio. Dax's discussion of row order concerns classical projection Kaczmarz, not reflective products. The closest available four-cycle ordinary Gauss–Seidel classification measures one-sweep energy rather than the reflection eigengap. Priority is subject to historical limitations: the original Coxeter papers and any unindexed equivalent special classifications were not read.

## Value — PASS

The inverse eigengap is a motivated control parameter in deterministic reflective Kaczmarz averaging. Products of at most three real reflections have order-invariant spectra, whereas the four-cycle is a natural minimal example with distinct ordering types, and the result completely classifies the permutations, identifies the strict optimum, and quantifies its sharp near-singular advantage. This is a precise finite optimization fact, not a generic claim about large systems or finite-horizon runtime.

## Limits

Only four equally coupled rows on a positive cycle with zero opposite-row correlation are covered. This is a bound-constant comparison; at a fixed number of epochs the oscillatory error factor need not favor the cyclic order. Independent literature and proof audit are outstanding.

Self-review: passed. Independent audit: not yet performed.
