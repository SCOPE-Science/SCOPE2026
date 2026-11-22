# Self-review

## Correctness — PASS

For every integer \(r\ge1\) and every finite unweighted tree, the proof reconstructs equal-distance center geometry using three-arm medians and projections onto tree geodesics. The crucial nonstandard step rules out unequal-arm triples: every common-radius center for the two longer/shorter arms projects to their midpoint and necessarily includes the third point. Once the arms are equilateral of length \(h<r\), a fourth branch and three singleton-branch witnesses characterize all eight traces. Four shattering is excluded by a forced four-arm configuration. A vertex-disjoint branch count proves \(3r+5\) necessary and an explicit hub-and-spurs tree realizes equality, including the small boundary \(r=2\). For \(r=1\), triples are impossible and a five-vertex path shatters a pair. The actual standalone `verify.py` execution returned `VERIFY_OK 237075` on exhaustive small trees, random trees and radius-dependent sharp witnesses. These experiments corroborate, but do not replace, the universal proof.

## Originality — PASS on inspected evidence

Direct published-finding corpus searches of fixed-radius tree spheres, equal-radius triples, tree-shell VC dimensions and the exact \(3r+5\) minimum were compared by claim implication. The closest accessible radius-two result proves only that particular case. The most relevant published published-finding corpus record for ultrametric spheres concerns a different metric; published halfspace and ball shattering results concern different concept classes. The full text of Dreier–Mählmann–Toruńczyk (arXiv:2611.08143v1), including its type-counting results and distance-based logic, was materially inspected: it does not state this specific fixed-shell tree theorem. Ball-VC literature treats inclusive graph balls of variable radius. Searches cannot establish absolute priority; older literature under *sphere ranges on tree metrics*, *distance-exact neighborhood VC*, or *tripod traces* is a residual risk. An inaccessible public full-text record was not used to infer noncoverage from a snippet.

## Value — PASS

The exact-distance predicate is a natural first-order definable relation on graphs (for fixed radius), and VC shattering controls the associated one-point type complexity. The theorem goes beyond a generic bounded-VC observation: it gives a necessary-and-sufficient, algorithmically testable structural classification of every shattered triple, an all-radius universal bound, and a sharp minimum witness order for every radius. The fourth-component and three-spur requirements identify substantive branching obstacles not visible in the earlier radius-two special case. The universal invariant has mathematical motivation independent of the verification computation.

## Closest literature and limits

Dreier–Mählmann–Toruńczyk, *First-Order Model Checking on Monadically Dependent Graph Classes* (arXiv:2611.08143v1, November 5, 2026), is the recent type-counting motivation, not a source of the present theorem. Ducoffe–Habib–Viennot (DOI:10.1137/20M136551X) treat graph balls. A relevant public ultrametric sphere record was inspected only through its published-finding corpus summary, so the full manuscript was not asserted to be checked. The theorem excludes weighted trees, variable radii and arbitrary graphs. All tests are finite; the mathematical proof covers all finite trees and integer radii. Historical priority has not been independently established.

Self-review: passed. Independent audit: not yet performed.
