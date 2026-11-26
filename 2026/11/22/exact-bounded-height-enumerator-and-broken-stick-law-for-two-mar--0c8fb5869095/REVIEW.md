# Independent mathematical audit

## correctness

PASS

Assessment of the delivered replacement repairs/3/RESULT.md. The frozen Finding is true, but the frozen proof at line 40 states an incorrect exact one-marker minimum on middle-gap deletion. For a=c=2,b=1, deleting the middle zero loses no one-marker pattern of length 3; the first has length 4. The replacement proves the exact minimum b+1+min(a,c) by observing that loss from the union of rectangles requires u=a+b or v=b+c, and both respective axis points attain those lengths. This supplies precisely the lower bound needed when the two-marker witness has length b+2, so the global witness formula and Finding are unchanged. The published deletion and binary identity give h=1+max lambda_i against all competitors, not only equal-length words. Taking minima with the all-zero witness and then maxima with the marker-deletion witness gives the disjoint gap strata, including the special b=1 case. Their exact polynomial sums to the stated cubic at z=1. The uniform weak compositions converge by simplex Riemann sums, the boundary has probability O(1/n), and inclusion–exclusion yields the stated limit and moments by tail integration. Replay: python3 /workspace/independent_checks.py 3 uses independently generated sets of subsequences of explicit insertions for 220 words, checks 100 coefficients, and verifies the precise counterexample to the frozen proof sentence. Frozen checker and verification were inspected, not executed. The replacement also corrects citations and delimits the contribution; the frozen files were not changed.

## originality

PASS

Best of current knowledge, the supported distinct claim is the complete two-one length-by-height census including every vanishing-gap stratum. The proof of the same-day isolated-marker result applies at t=2 for positive gaps without a new idea, despite its formally stated t>=3 hypothesis; that fact covers the interior term and implies the same limiting distribution via the negligible boundary probability. The repaired text credits this substantive overlap and does not claim separate novelty for the limit or known height machinery. Shared date does not establish priority.

## value

PASS

The two-marker family is the first fixed-weight setting with three interacting zero gaps. Its bounded-height distribution is an exact calibration case for singleton-language complexity. In fixed-length or cumulative counts, vanishing gaps cannot be discarded: their cumulative correction to the positive-gap count is 3H^2-11H+16 at z=1, and their distinct witness regimes determine small-height and boundary coefficients. This is useful as a complete finite reference even after crediting the positive interior and its classical broken-stick limit; it is not justified by a new proof of that limit alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
