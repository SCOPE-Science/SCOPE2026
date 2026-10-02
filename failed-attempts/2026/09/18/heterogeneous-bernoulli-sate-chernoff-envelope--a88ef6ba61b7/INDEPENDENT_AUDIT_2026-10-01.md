# Independent audit — 2026-10-01

## Final claim

The mathematical derivation is correct, but the submitted final claim is rejected because it is covered by an earlier published result after an elementary interval substitution and does not add a sufficiently nonmechanical mathematical contribution.

## Correctness — PASS

The centered estimation error reduces unitwise to a centered Bernoulli variable multiplied by a scalar ranging over the interval obtained from the arm-specific outcome bounds. Convexity of the log moment generating function makes the endpoint supremum exact, and reflection about the interval midpoint yields the two-sided minimax center. Independent checks reproduced the rare-arm orientation of the two directional moment generating functions and the stated variance scale.

Sources checked: published archive record SCOPE-20260917-40d55355f1a6; https://arxiv.org/abs/2609.18586.

Residual risks: The Chernoff inversion is a valid exponential bound, not an exact least-favorable tail probability.

## Originality — FAIL

A published 2026-09-17 record already proves the exact heterogeneous-Bernoulli directional cgf envelope, pointwise midpoint minimaxity, the rare-arm closed form, Chernoff interval, Bernstein scale and endpoint lower-bound mechanism. The audited arm-specific-bound version follows by the mechanical substitution that the scalar \(d_i=(1-\pi_i)Y_i(1)+\pi_iY_i(0)-m_i\) ranges over the weighted interval \([(1-\pi_i)a_{i1}+\pi_i a_{i0}-m_i,(1-\pi_i)b_{i1}+\pi_i b_{i0}-m_i]\). Thus the final claim is a routine parameter generalization of an earlier published theorem.

Sources checked: published archive record SCOPE-20260917-40d55355f1a6; https://arxiv.org/abs/2609.18586; https://arxiv.org/abs/2601.11744; https://arxiv.org/abs/2605.20572.

## Scientific value — FAIL

Although arm-specific outcome bounds can be useful in applications, the mathematical change here is only the elementary weighted-endpoint substitution inside an already published exact cgf theorem. It does not establish a new structural boundary, classification, invariant, or nonmechanical consequence beyond the earlier result.

Sources checked: published archive record SCOPE-20260917-40d55355f1a6.

## Disposition

Failed on originality and scientific value. Preserve the complete package and evidence in the assigned failed-attempt path.
