# Scientific review

## Correctness

**PASS.** Each of the six nonunary length-three subsequences has exactly one avoiding representative, when its arithmetic condition is met. The six explicit canonical words are derived by forced placement of the letter that could close a forbidden subsequence. Coincidences occur at exactly six nonendpoint parameter equalities and the two endpoints; all six corrected counts have been checked algebraically, and the resulting class-size and composition identities follow from a standard Gaussian-partition bijection. The standalone verifier independently tests 48,200 binary words and 1,125 exact fibers; 17,885 additional parameter fibers check canonical collision counts. Finite verification is a consistency check, not a proof of the unrestricted parameters.

## Originality

**PASS, with priority risk.** Fazekas–Huang–Mercaş (arXiv:2610.06717, Sections 4 and 5) already establish per-pattern existence criteria and the yes/no condition that *every* member is 3-universal. Their Lemma 4.3 proves the structural avoidance forms from which the six unique representatives can be recovered. This finding does not claim those ingredients as new: it classifies their intersections, determines the exact **number** of non-3-universal representatives of each fixed two-deck, supplies the conditional probability and a uniform two-exception theorem, and sums the counts for every fixed composition. Richomme (arXiv:2510.07159) and Golafshan (arXiv:2606.23426) give class geometry and Gaussian fiber sizes, not this conditional refinement. A published unrestricted-length universality law does not condition on the two-deck parameter. The collision computation is a comparatively short extension of a very close antecedent, so unindexed equivalent refinements or an overlooked remark in the prior literature remain material risks; no independent historical priority determination is claimed.

## Value

**PASS.** The natural probabilistic refinement in the motivating paper asks for the frequency of subsequence properties inside a two-deck class. This exact result identifies the full 3-universality numerator for every unbounded triple of class parameters, with at most two exceptions in even huge fibers, rather than only yes/no extremes. The exceptional set is structurally and arithmetically classified and gives a closed fixed-composition count. This is a meaningful complete classification at the first nontrivial universal subsequence length, not a finite tabulation or an arbitrary parameter slice.

## Limitations and closest literature

The result depends on the six avoidance conditions from the 2026 primary paper and does not resolve four-letter pattern probabilities, arbitrary subsequence universality, or historical priority. The Gaussian coefficient is not claimed as new. The proof is self-contained given elementary counting arguments; the checker cannot replace its all-parameter reasoning.

Self-review: passed. Independent audit: not yet performed.
