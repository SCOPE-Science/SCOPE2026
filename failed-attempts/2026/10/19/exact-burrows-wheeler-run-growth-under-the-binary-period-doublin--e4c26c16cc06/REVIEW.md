# Independent mathematical audit

## correctness

PASS

For a primitive cyclically 11-free input, starts in the substituted word split lexicographically into even at 1, odd at 1, even at 0, odd at 0, with separating prefixes 0001, 0010, 01, 10. Within each block, the first unequal encoded input bit reverses the strict order; odd starts have zero predecessors and even starts have complemented input predecessors. Distinct rotations prove primitivity of the image. For the singleton 0, the first two blocks are empty and the formula gives BWT(01)=10 directly. In the iterates the 1-start block is all zero, and the 0-start block begins in 1 and ends in 0 from W_2 onward. Its complemented reversal preserves this boundary and the number of runs; the new nonempty 1 and 0 prefixes add two runs and the last suffix merges. W_2 gives 1000, so induction proves the exact linear run count. The frozen checker was inspected but not run; its tests are bounded, while the four-block proof handles all lengths.

## originality

FAIL

A distinct indexed record explicitly presents the same no-sentinel dyadic transform recurrence and run count. Another distinct indexed theorem gives the full transfer on the cyclic 11-avoiding class, including imprimitive mixed words. Its apparently different first block equals the frozen block because B1=0^o, and the only all-zero primitive input is the immediate singleton case. Thus neither the main formula nor the stronger identity survives as a distinct contribution. This is a coverage finding; catalogue dates do not determine authorial priority.

## value

PASS

The structural transfer on an entire cyclic word class is a worthwhile mathematical target: it determines the full transform, not just order of growth, and identifies the boundary merges turning morphic doubling into exactly two extra runs. This assessment of mathematical interest is separate from the demonstrated redundancy of the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
