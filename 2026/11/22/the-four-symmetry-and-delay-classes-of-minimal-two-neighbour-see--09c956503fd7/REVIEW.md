# Scientific review: four-cube minimal percolation orbit and delay classification

## Correctness — PASS

The definition is the usual simultaneous two-neighbour infection update on the sixteen vertices of \(Q_4\). The exact finite proof enumerates all 65,536 initial configurations, computing a terminating monotone fixed point and testing one-vertex deletions. The resulting 256 inclusion-minimal configurations have sizes and times \((3,4):48\), \((3,5):96\), \((4,3):16\) and \((4,4):96\). The independent group-action/subcube checker reproduces all minimal configurations through four seeds, verifies full orbit coverage and their distance-and-XOR classification, and proves a distinct unique delay-preserving extension of each slow triple. Direct program replay succeeded. These are exhaustive finite statements only; no infinite extrapolation is made.

## Originality — PASS, subject to priority risk

The inspected primary literature establishes the maximum possible minimal-seed size (Riedl 2010), two size-four isomorphism classes (Riedl), maximum possible completion time (Przykucki 2012), and a maximal induced-path containment theorem (Shende 2015). Their proofs and quantified results do not provide the complete 256-seed four-orbit/time distribution, the full geometric membership criteria, or the unique slow-triple extension rule. Actual searches of the indexed mathematical corpus, exact numerical phrases, natural aliases, and published hypercube-percolation results identified no implication of the complete statement. Some orbit-size information for size four can be derived from Riedl's two-type classification, so that *subresult is not claimed to be independent of his prior classification*. Unindexed numerical tables or unpublished computations remain a possible priority risk.

## Value — PASS

Dimension four is the first binary cube in which minimum-size percolating triples coexist with strictly larger inclusion-minimal four-seed sets: the equality \(m(Q_4,2)=3<E(Q_4,2)=4\) is a known sharp threshold, and the new result determines the complete geometry-and-speed landscape at that transition. The two three-seed symmetry types take four or five rounds; the two irredundant four-seed types take three or four rounds. The five-round equality case has an unexpectedly rigid one-vertex extension map, pairing each of 96 slow minimal triples with a unique distinct redundant four-seed. This resolves naturally motivated joint cardinality, geometry and spreading-time questions, not an arbitrary selection of instances. The work is finite and its value does not rely on a downstream theorem.

## Closest literature and limits

E. Riedl (2010), DOI 10.37236/352; M. Przykucki (2012), DOI 10.37236/2412; A. M. Shende (2015), DOI 10.13069/jacodesmath.15518. The result is restricted to the labelled sixteen-vertex cube, threshold two. Broader generalizations and a complete literature priority guarantee are not asserted. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
