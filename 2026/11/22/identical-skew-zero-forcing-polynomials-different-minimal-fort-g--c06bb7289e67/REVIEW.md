# Scientific review

## Correctness — PASS

The two graph encodings are explicit, six-regular, and have two common neighbors per pair. The skew color rule is correctly normalized to allow both blue and white witnesses, consistent with Definition 3.4 of the original 2010 reference. A non-successful blue set is equivalent to a white complement containing a nonempty skew fort, by the first-forced-vertex and terminal-configuration arguments. The C++17 checker tests each of 65,536 white masks per graph, verifies the fort-obstruction equivalence mask by mask, and enumerates inclusion-minimal forts by direct strict-subset tests. The independent Python checker reconstructs the graphs using coordinate sets and enumerates cardinality layers. Both produce the same complete forcing polynomials, the 60 plus 256 minimal-fort distribution, and the three four-vertex degree types. The Python program checks all 666 tabulated data rows against recomputation. No probabilistic or partial count is used.

## Originality — PASS, with residual risks

The 2010 primary paper establishes the skew forcing rule and related minimum-rank bound, not the sixteen-vertex twin-polynomial statement. An existing general rook-graph Grundy total domination formula already supplies the single numerical skew forcing number for the rook graph, but does not classify every forcing set or provide any Shrikhande comparison. The inspected later failed-skew forcing work focuses on related forcing parameters, not the pair. A primary 2022 work explicitly compares these two graphs for *positive-semidefinite* forcing, not skew forcing. The closest ordinary zero-forcing and ordinary fort statements use different color-change rules; the ordinary census has distinct order-ten and order-eleven coefficients and cannot imply their skew counterparts. Investigated other-pair invariant results (domination, matchings, neighborhood shattering) likewise do not cover this skew claim. No retrieved table or paper was found giving the exact shared skew polynomial or the different four-fort geometries. This is best-knowledge originality, not proof of global priority; inaccessible or unindexed historical computations remain a risk.

## Value — PASS

The nonisomorphic cospectral strongly regular pair is a standard test case for which invariants distinguish graphs. Equality of a full forcing-set enumerator is more informative than equality of a single forcing number, while unequal small-fort geometries show how the equality masks genuinely different combinatorial obstructions. Counting all inclusion-minimal skew forts, rather than a single optimum, supplies a natural obstruction classification useful in searching for conceptual explanations of polynomial coincidence. This is a complete exact finite fact, not asserted as a broad theorem.

## Limitations and sources

The exhaustive proof has finite scope, and no full structural classification of the six-vertex skew forts is claimed. The extant primary literature and related exact results were compared at the level of rules and implications. Independent scholarly audit is still needed to assess long-term priority and exposition.

Sources: https://doi.org/10.1016/j.laa.2009.10.001 ; https://www.academia.edu/58516479/Failed_skew_zero_forcing_on_a_graph ; https://journals.uwyo.edu/index.php/ela/article/download/6737/5787/11861 ; https://www.mdpi.com/2673-9909/5/2/32 .

Self-review: passed. Independent audit: not yet performed.
