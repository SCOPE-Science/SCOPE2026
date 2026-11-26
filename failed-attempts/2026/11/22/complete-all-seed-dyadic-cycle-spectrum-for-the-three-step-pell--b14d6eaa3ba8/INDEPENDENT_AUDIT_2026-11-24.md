# Independent mathematical audit

## correctness

PASS

The determinant-one companion update is a permutation. Its irreducible mod-two polynomial gives multiplication by a nonidentity element of F8, so primitive states reduce to a seven-cycle. Independently recomputed the two integer lifting certificates by iterating the update on basis states: det((M^7−I)/2)=87 and det((M^14−I)/4)=7569. The first square needs the separate second certificate; beyond it, normalized repeated squaring preserves the leading matrix modulo two. An invertible leading matrix cannot increase the valuation of a primitive vector, hence (M^(7·2^j)−I)v has coordinate valuation t+j+1 exactly. Cancelling 2^t reduces period to that of a primitive state at depth k−t. Since the period divides the first fixing iterate in this dyadic chain and is divisible by seven, it is exactly the claimed period. The shell contains 7·8^j states, giving 4^j cycles; the zero state is separately fixed, including at k=1. An independent exact fixed-point census through k=5 matched all cumulative counts and their differences.

## originality

FAIL

Brent's published general maximal-period criterion and equality of principal and primitive-seed periods cover this claim by a direct corollary. The only evaluation required is at modulus eight, followed by cancelling scalar powers of two and dividing a shell cardinality by the common period. This is verified prior implication, not a claim that the Pell table already appeared verbatim or that an unavailable paper covers it.

## value

FAIL

The all-seed cycle spectrum is a natural invariant, but here the finished claim is the routine small-modulus specialization of an existing theorem about all primitive seeds. The extension to every seed is exactly scalar cancellation and shell division, and the integer certificates are elementary evaluations for this fixed companion. The self-contained argument may be useful exposition; it does not establish a distinct scientific finding warranting acceptance under the exact-invariant standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
