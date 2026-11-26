# Independent mathematical audit

## correctness

PASS

The two displayed operations define closed finite graphs. Multiplication by 2^133 encodes each format value as an integer, including the subnormals; the nonnegative remainder is exactly the integer residue in these units. The exact real sums before final rounding are less than 2 (the staged quotient is at most R(1/5)); the staged product is at most 200. I reconstructed both transition rules and independently evaluated every code with an exponent-local quotient/remainder rounder instead of a neighbor-table search. The local spacing is 2^max(0,floor(log2(n/d))-7) in scaled units; an exact midpoint chooses an even quotient, with recoding at exponent boundaries. The replay tests all adjacent midpoints through 256. Separate Floyd walks from every start locate first cycle entries and traverse the primitive cycles. All representatives, associated periods and basin sizes agree, not just their multisets: A has the zero, 18- and 24-cycles; B has two fixed points and eight 3-cycles. The respective maximum depths are 51 and 44; precisely 3,545 of the 16,385 successors differ.

## originality

PASS

The reviewed distinction is the exact paired graph census for this remainder-added map and these roundings, not the underlying recurrence, the existence of finite-precision cycles or sensitivity to evaluation order. The closest inspected statements do not cover that census.

## value

PASS

A complete format-scale baseline for a published remainder-addition family can be used to test implementations and isolate the effect of moving rounding across a discontinuity. The striking exact difference is not generic eventual periodicity: a dominant 24-cycle and an 18-cycle are replaced by eight distinct 3-cycles and a nonzero fixed point, with measured encoding basins and depths completing the comparison. The scope is a single explicit parameter example, but the state set and arithmetic choices are natural and the exact census is useful on its own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
