# Scientific review: Exact mutual-nearest-neighbor component law in symmetric random-link graphs

## Correctness (C): PASS
The proof constructs the directed nearest-neighbor forest, excludes longer directed cycles by strict descending edge weights, computes simultaneous matched pair events through an order-statistics integral with all between-pair constraints, and obtains the complete PGF by finite binomial-moment inversion. The gap-integral denominators are \(j(2n-2j-1)\), and their \(j\) factors cancel the ordering factor \(k!\). The mean and variance follow from the first two factorial moments with the boundary \(n=2\) treated separately. Exact independent edge-order enumeration through \(n=5\), and 923 exact rational assertions from the packaged script, support the algebra but are not substitutes for the infinite proof. No missing nonstandard lemma or computational certificate is used.

## Originality (O): PASS, qualified
The one-pair probability in the 2009 random-link study implies the mean, and the 2023 Aldous question and answer give exactly the all-pairs-extreme probability; neither is presented as a new theorem. The 2021 Frieze–Pegden nearest-neighbor discussion gives different spanner results. Full text of the directly related MathOverflow page, relevant 2009 article sections, and relevant portions of the 2021 preprint were inspected; no displayed result there provides the complete factorial-moment sequence or full PGF for the number of reciprocal nearest-neighbor components. Searches of public research records also found no dominating same-model formula. This supports a qualified originality judgment, not a guarantee of historical novelty. An unlocated full-law calculation is the main residual risk.

## Value (V): PASS
A symmetric random-link nearest-neighbor network is a natural model of random local attraction: every component terminates at a mutual pair. The exact \(k\)-matching probabilities give the *entire finite distribution* of its component count, not an arbitrary slice. The explicit variance identifies universal strong underdispersion with limiting Fano factor \(1/4\), while specified disjoint reciprocal-pair events have positive correlation; these are mathematically informative properties beyond the previously known mean and extreme event.

## Limitations and closest literature
This covers independent atomless *undirected* common edge weights on complete graphs, not spatial geometry, heterogeneous weights, or asymmetric directed weights. The 2009 random-link paper gives only the inspected one-point calculation; the 2023 MathOverflow question gives the perfect-pair matching probability as a special case; the 2021 spanner paper studies a different global structure. Older equivalent research may exist. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
