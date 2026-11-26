# Independent mathematical audit

## correctness

PASS

The domain is exactly the positive-sign encodings 0x0000 through 0x3bff, including +0 and subnormals. The source integer encoding and parity tie rule follow from the exponent bias and the parity of the low significand bit, also at the subnormal/normal and binade boundaries. The first map wraps a rounded one to zero; in the second map the represented product minus one is exactly representable when needed. Independently reconstructed both entire successor arrays using Python struct binary16 decode/encode (nearest-even), with binary64 exact for the pre-rounding dyadic products and subtractions. Indegree pruning leaves exactly the cycle vertices of each finite functional graph; following edges on that residue and traversing reverse edges from each cycle gave these (period, basin, maximum depth) triples, each for a single cycle: A (1,468,55), (3,28,15), (8,2480,144), (18,187,27), (164,12197,136); B (1,5705,155), (3,26,15), (4,3138,133), (24,2013,77), (41,4478,67). Reverse traversal assigned all 15,360 states exactly once in each map, and zero was the only fixed point of each. The comparison gave 512 differing successors, and the reconstructed little-endian arrays matched both SHA-256 digests in the frozen record.

## originality

PASS

The distinct contribution supported here is the exact paired census at beta=3/2, with transient maxima and exact edge discrepancy, not the general effect of rounding or the method of enumerating a functional graph. Klöwer et al. use the B-like implementation for Float16 and report an exhaustive invariant-measure calculation in the supplement; this is material prior overlap and may extend to individual features of B. The inspected text and captions do not give the paired binary16 graph analysis. Boghosian et al. give substantive beta=3/2 results for binary32, which do not determine either binary16 graph. The conclusion does not assert priority for a standalone census of B.

## value

PASS

Beta=3/2 is a benchmark in prior finite-precision work, and binary16 makes both deterministic, naturally used intermediate-precision rules exhaustively testable. A change in only 512 of 15,360 immediate successors moves the zero basin from 468 to 5,705 states and reduces the longest cycle from 164 to 41. Knowing the full census and transient limits, not just that rounding matters, gives exact reference answers for testing implementations and diagnosing precision-dependent attraction bias. This value is in the jointly controlled comparison, not a claim that deterministic finite-state periodicity is new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
