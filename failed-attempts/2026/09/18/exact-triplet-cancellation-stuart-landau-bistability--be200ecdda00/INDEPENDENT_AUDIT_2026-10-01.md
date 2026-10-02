# Independent scientific audit — SCOPE-20260918-be200ecdda00

Audited at: 2026-10-01T08:23:38.851470Z

Disposition: **failed**

## Correctness — PASS

The published second-order phase reduction assigns coefficients proportional to \(w_{12}w_{23}\), \(w_{13}w_{32}\), and \(-2w_{12}w_{13}\) to the three explicit triplet harmonics, while the engineered physical motifs enter with independent weights and the opposite signs under the chosen scale. Choosing motif weights in the ratio 1:1:2 in the unweighted triangle therefore cancels those three coefficients exactly. The inspected symbolic verifier reconstructs the residual pairwise-additive phase field and confirms \(\lambda_{sync}+2\,Re(\lambda_{splay})=0\).

## Originality — FAIL

The motivating primary source already publishes both the emergent triplet coefficients and independent physical motif weights, explicitly discusses coefficient cancellation, and uses an all-unit choice that leaves half of the symmetric term. Setting the symmetric motif weight to two is therefore direct coefficient matching from the source equations; the subsequent three-node synchronization/splay linearization is routine.

### Equivalent formulations

The audited 1:1:2 design is the literal exact solution of those three scalar coefficient-matching equations.

### Broader coverage

The only source-specific change is choosing the already-available motif weights to match the already-published coefficients.

### Exact database or table

Exact wording does not restore originality because the claim is mechanically implied by the source equations.

### Claim versus prior implication

The final design is a direct algebraic specialization rather than a new structural implication.

## Value — FAIL

The weight adjustment is a useful design observation, but it is a one-line exact matching of already-published coefficients followed by a standard three-oscillator local stability calculation. Under the stated value bar, that is too mechanically implied to count as a distinct validated finding.

## Sources inspected

- Physical and emergent nonpairwise interactions in oscillator networks: from higher-order phase reduction to coupling design — https://arxiv.org/abs/2609.20632. COVERING: The source provides all coefficient equations and independent motif weights needed for the audited 1:1:2 cancellation.

## Checked sources

- https://arxiv.org/abs/2609.20632
- https://doi.org/10.1007/s00332-024-10053-3
- https://doi.org/10.1063/5.0307452

## Residual risks

- The exact synchronization/splay identity may not be printed in the source, but it is routine algebra after the direct coefficient match.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The cancellation is confined to the retained second-order phase reduction.
- The local stability identity concerns synchrony and three-oscillator splay only.
