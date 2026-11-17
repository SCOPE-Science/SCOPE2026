# Independent mathematical audit

## correctness

PASS

For all n>=3, bit changes under synchronous three-neighbor majority exactly when both adjacent disagreement edges are 1. Equal bonds persist and each finite one-run of g edges erodes by two at each end until length <=1, so T=floor(g/2), checkerboards on even rings being immediate 2-cycles. The parity-constrained cyclic edge word has exactly two spin preimages; the 2(2t+2)-state run/parity transfer counts even one-run words of length <=2t+1 and the two checkerboards add 2. Cyclic parity gives max floor((n-1)/2) with 2n maximizers. Standard longest-run union and disjoint-block probability bounds prove T/log2 n ->1/2. Independent exhaustive simulation n3..10 reproduced all first-entry layers (n10: 124,590,230,60,20).

## originality

FAIL

FAIL. October 25 published Resultary work proves exactly the same edge-run identity, 2n extremizers and trace with a state index cap L=2t+2 (j=0..L-1), equivalent to the submitted L=2t+1 (j=0..L), plus stronger Poisson critical-window and expectation laws. A November 2 source gives the same periodic-ring run-length identity and complete fixed-time GF; the checkerboard correction converts its fixed-entry count to this periodic-entry count. The logarithmic law follows from the stronger earlier distribution/expected time.

## value

FAIL

FAIL. Complete exact transient-layer enumeration and logarithmic clock would be valuable if unknown, but they are mathematically contained in the stronger earlier October 25 theorem for the same synchronous map, ring and initial distribution. An equivalent transfer-coordinate renaming adds no independent exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
