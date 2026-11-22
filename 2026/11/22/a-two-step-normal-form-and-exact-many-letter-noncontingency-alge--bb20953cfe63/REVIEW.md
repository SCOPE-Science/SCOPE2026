# Self-review

## Correctness — PASS

The result makes a precise all-valuation claim for finite bicliques with \(k\geq2\) letters. Propositional minterms recover any non-singleton opposite support; depth-two tests \(\Delta(\chi_a\wedge\Delta\chi_b)\) recover the reverse support whenever the opposite support has at least two colors. The singleton-opposite case collapses exactly because its worlds share the same complete modal behavior. An induction on formula syntax proves that the stated finite descriptor is stable under arbitrary nesting; Boolean isolation of the finite descriptors proves the exact algebra size. The two-color and four-color symbolic refinements and independently constructed small labelled-model checks in `verify.py` agree with the formulas. The proof, not finite enumeration, covers unbounded numbers of letters and frame sizes.

## Originality — PASS within inspected evidence

Full published results on noncontingency stars (arbitrary letters, one-way terminal successors), all complete multipartite frames (one letter), and irreflexive cliques (one letter) were compared by mathematical implication. None states or implies the all-\(k\geq2\) exact biclique spectrum or the two-sided normal form without a new analysis of feedback between the two independent sides. Recent Wang–Zenger arXiv:2609.38975 and Fan–Wang–van Ditmarsch general knowing-whether work provide the semantics and theory, rather than a located exact formula-algebra classification. The latest Wang–Zenger paper was available by abstract, not its complete full text; this is a residual priority risk. Searches, inspected material, and scope comparisons are recorded in `AUDIT.json`. Historical uniqueness is not certified.

## Value — PASS

Complete all-parameter classification is motivated by the concrete expressivity question: how many properties can a noncontingency-only language detect on the simplest two-way nonreflexive neighborhood geometry? The exact sharp second modal layer, explicitly observable reverse-side information, exact exponential-size formula algebra, and least common witness biclique are significant structural invariants, not just finite sample counts or renamed one-sided calculations. The distinction from the rooted-star and one-letter multipartite cases is mathematically substantive.

## Remaining limits

The normal form does not cover arbitrary graph frames, reflexive bicliques, higher modal signatures or constrained valuations. The comparison with one recent plausible paper could not include full-text inspection, and equivalent old terminology may remain unindexed. The computational verification is finite and does not independently audit the proof or historical priority.

Self-review: passed. Independent audit: not yet performed.
