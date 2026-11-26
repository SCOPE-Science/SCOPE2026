# Independent mathematical audit

## correctness

PASS

From the specified open neighborhoods I encoded the synchronous successors using color indicators and a reversed ternary digit convention, then found the first cycle entry and least period by Floyd's algorithm for every one of the 531441 initial states. The collision occurs on the cycle at a step divisible by its least period; resetting one pointer to the start and advancing both identifies the first orbit entry, and one circuit gives the least period. There were zero pointwise mismatches. All six population counts, both primitive-orbit columns (entry-zero counts divided by least period), the sharp depths 8 and 10 with shells 192 and 64, and every one of the 165 joint census cells matched. No initial bounds on periods or entry times were assumed. The frozen peeling and iterate checkers implement valid exhaustive methods; they were inspected, not executed.

## originality

PASS

Best of the inspected evidence supports distinct Chvátal-specific joint concordance, CCA orbit/entry data and the joint census. The GHM-only census and sharp GHM depth are existing results and do not receive originality credit. Same-day equality records on other graphs are technically relevant but not equivalent; their date establishes no priority.

## value

PASS

The canonical small triangle-free four-chromatic graph gives a meaningful exact test of when cyclic and refractory dynamics retain the same least period despite period division occurring on other standard graphs. The paired census separates basin period, time to recurrence and the recurrent-orbit populations, and is useful as a finite benchmark for any proposed comparison theorem. Value does not rest on recomputing the known GHM margin.

The dated certificate retains the supplied scientific assessment, sources and limitations.
