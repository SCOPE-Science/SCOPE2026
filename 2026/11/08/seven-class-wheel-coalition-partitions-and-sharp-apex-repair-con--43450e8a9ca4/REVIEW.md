# Self-review

## Correctness — PASS

The proof fixes a pair of vertices outside an apex-containing set whose open-neighborhood traces agree. The neighborhood-counting argument from the motivating paper gives the contextual upper bound \(2\Delta(H)+2\); this estimate alone is not asserted to be original. The sharp construction has precisely one original collision and \(2d+2\) one-vertex repairs for all \(d\ge2\). Non-dominating singleton complements furnish an actual coalition partition. The wheel trace table and six repairs prove the seven-class lower bound for every \(m\ge10\). The finite verifier checks the definitions directly but is not substituted for the unrestricted proof.

## Originality — PASS, with historical risk

Chellali et al., arXiv:2602.18760 (initial submission 2026-02-21), prove an at-most-\(2\Delta(G)\) partner bound for classes of arbitrary LDC partitions (Lemma 2.10) and give \(C_L(C_m)\le6\) for cycles (Lemma 3.4 and Proposition 3.7). Their proof already implies the contextual base-degree estimate, so **the estimate is not original**. They do not give the all-degree sharpness construction or an LDC partition of a wheel with seven classes. Targeted searches for wheel/cone/degree aliases, broader implication, and existing numerical tables found no covering claim. The accessible primary preprint was read through its relevant sections and references. Unindexed literature and unpublished equivalents remain genuine priority risks.

## Mathematical value — PASS

The previously implicit local bound is **attained for every base maximum degree** \(d\ge2\) by a natural subdivided-star construction. It also produces connected graphs with \(C_L(G)\ge2d+3\) and seven-class LDC partitions on every sufficiently long wheel, strictly larger than the familiar cycle ceiling of six. This extends the recent research program on degree-dependent coalition bounds by a sharp attainability theorem and two motivated infinite constructions. It is not a claim that the wheel number is exactly seven.

## Source comparisons and limitations

The closest statement is Lemma 2.10 in Chellali et al.; its neighborhood-counting proof already implies the contextual local upper bound on cones but does not imply sharpness for all degrees. The cycle classification in Proposition 3.7 concerns the base alone and cannot imply wheel partitions. Slater's earlier location-domination work is definitional, not a coalition result. The contextual bound requires the apex to be selected, the wheel conclusion is only a lower bound, and independent verification has not been undertaken.

Self-review: passed. Independent audit: not yet performed.
