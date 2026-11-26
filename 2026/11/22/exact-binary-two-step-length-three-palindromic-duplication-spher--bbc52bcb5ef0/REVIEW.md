# Independent mathematical audit

## correctness

PASS

The specified operation retains the prefix through the copied triple, inserts its reversal, and retains the original suffix. The two start ranges are 0..n-3 and 0..n inclusive; the second range includes windows involving newly inserted symbols. With fixed output length n+6 the bit encoding is injective and the frozen C++ loop generates all histories, sorts, and counts distinct output words, without overflow on this domain. Complementation commutes with every operation and partitions sources into free pairs. Independently reproduced all twenty rows with big-endian vectorized integer encodings, keeping one history from each commuting pair and computing exact distinct-word counts, not hashes or ordered-history totals. Precisely the omitted histories duplicate the right original window at i first and then the unchanged left window j<=i-3; each is equivalent to the retained history starting at j and then using i+3. These pairs are disjoint in history space and there are binom(max(n-4,0),2) of them, proving the upper bound. This reduction's entire output set was also compared with literal unreduced string histories at all 2,040 sources of lengths 3..10. The independent census visited 4,194,300 complement representatives through n=22. It agrees on maxima 4,9,16 at n=3,4,5 with labeled populations 2,4,4; for n=6..22 it finds only the two specified complementary prefixes and exactly n(n+3)/2-3 outputs, including 272 at n=22. Subtracting this expression from the commutation bound gives 2n-9. Review did not execute the uploaded C++ program; the independent complete computation is the replay. No n>22 conclusion follows.

## originality

PASS

Evidence supports distinctness of the finite binary sharp values and full optimizer census, not the two-step operator, encoding idea, or disjoint-window bound. The closest same-day result attains that bound at q>=3 with a different periodic word; it neither claims nor implies sharpness or equality classification at q=2. Same-day indexing is not used to infer priority.

## value

PASS

Binary is the alphabet-size boundary at which universal-bound attainment for length-three duplication fails, not a randomly chosen set of words. The full finite optimum and both maximizing words give exact calibration of worst-case distinct descendants and collision loss, useful for testing finite channel bounds and prospective analytic binary equality conditions. Length 22 is a computational endpoint, not a structural transition; what makes the result informative is coverage of every source at twenty consecutive lengths with a persistent sharp linear deficit and rigid equality pattern. Neither a coding-capacity result nor an infinite-length result is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
