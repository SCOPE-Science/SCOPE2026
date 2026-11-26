# Independent mathematical audit

## correctness

PASS

Baranwal et al.'s Theorem 11 and Proposition 18 give the eight-factor reduction for periodic, not arbitrary finite, words. After banning length-two runs, consecutive long runs cannot have opposite symbols: zero intervening singletons creates 0011 or 1100, two creates 001011 or 110100, and at least four creates a six-letter alternation. A nonconstant period without a long run is itself alternating. Between two long runs of the same symbol there must be one or three singletons (five creates a six-letter alternation). Conversely the resulting cyclic grammar avoids every forbidden factor. Marking any of r block starts yields n choices of indexed marked position per ordered block tuple, even for nonprimitive periods, giving the logarithmic weight factor 1/r. Adding the constant words yields the two denominators; differentiation recovers the count recurrence. Möbius inversion multiplies weight by repetition count and divides the number of primitive indexed points by n. Equality at minority density 1/3 forces every block to be 000101 or its complement, of least period six. Independent direct cyclic bit-shift enumeration of 8190 words through period 12 agrees coefficientwise with the zeta and with the primitive inversion; at n=6 the weight vector is (1,6,6,0,6,6,1). Replay: node /workspace/independent_checks.js, section 1. For the bit check the order cutoff is valid on an n-periodic word: reduce a larger order modulo n; a nonzero residue >=2 gives an antisquare at that residue, residue 1 gives one at n+1, and residue 0 cannot give a bitwise complement. The enumeration is finite in n; the run proof is not. The frozen verifier was inspected, not executed.

## originality

FAIL

The earlier October 25 transition-refined result gives an exact indexed census of precisely the same periodic words, with census -2z times the z-derivative of log(1-z-v^2 z^4-v^4 z^6). On every nonconstant admissible period all minority letters are isolated by the run grammar, so its number of cyclic changes is twice its minority weight. Complementation preserves transition count and exchanges the two possible weights. Thus every transition-census coefficient at t=2j divides equally between weights j and n-j, including t=0 for the two constants. Equivalently, halve the logarithmic census and substitute v^2=u to get the first factor, then take its bitwise complement by (z,u)→(uz,u^{-1}) for the second. This gives the identical zeta without a new enumeration. The primitive counts use exactly the same relabeling and standard Möbius inversion. The sharp density boundary and equality count follow from extrema of the earlier transition polynomial: every monomial of either nontrivial block has at most one unit of minority weight per three positions, with equality only on the degree-six term; the exhibited period and its six rotations exhaust that coefficient. The later exact indexed statement 585d5e7587a7 corroborates equivalence but is not the basis for prior coverage.

## value

FAIL

The periodic avoidance model and its exact enumeration are naturally motivated. In this specific language, however, the purported Hamming-weight refinement is a relabeling of a known exact transition refinement, and the density extremes and primitive counts are direct consequences. It does not contribute a previously undetermined invariant, obstruction, or cutoff beyond that correspondence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
