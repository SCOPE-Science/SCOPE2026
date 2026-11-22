# Scientific review

## Correctness — PASS

The polynomial certificate and all contact-root signs are exact. The integral proof applies to arbitrary positive Borel measures, not just finitely supported examples. Equality fixes the cosine pushforward weights; opposite signs of the two Chebyshev sine ratios force symmetric splitting, so there are no nonsymmetric omitted optimizers. The included standalone SymPy checker verifies critical finite algebra and not the infinite quantifier.

## Originality — PASS (best knowledge)

The published \(\{1,2,6\}\)-notch circle gap and its six-atom optimizer were compared at full-statement/proof level and do not imply the \(\{1,4\}\)-notch claim, because the vanishing-moment hypotheses are mutually nonnested. Peherstorfer's characterization assumes contiguous Fourier exactness, while di Dio and Kummer's sparse-moment theorem bounds numbers of atoms rather than missing arc length. Searches for the exact radical, alias formulations, dominated parameters and numerical constant found no direct predecessor. Broadly relevant older extremal-cosine publications were inaccessible in full and remain a residual priority risk. No global novelty or independence certification is asserted.

## Mathematical value — PASS

The statement gives a sharp geometric sparsity limit under a natural pair of nonconsecutive Fourier vanishing conditions, together with the exact positive four-node measure and complete rotation/scaling rigidity. The distinction from the regular three-node rule demonstrates that the maximum gap is not read off from a naive equal-spacing construction. This can serve as a benchmark for sparse spectral quadrature and support-hole problems without requiring a general theorem for every sparse frequency set.

## Verification limits

`python CHECK.py` checks the exact algebra, ordering, weights and sine-system signs. The analytical proof establishes all measures and all rotations. An inaccessible older dual-polynomial source alone is not asserted to cover or not cover this exact specialization.

Self-review: passed. Independent audit: not yet performed.
