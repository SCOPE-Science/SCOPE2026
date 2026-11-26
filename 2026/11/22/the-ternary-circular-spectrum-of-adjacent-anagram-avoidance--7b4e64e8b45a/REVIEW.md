# Independent mathematical audit

## correctness

PASS

The triple-overlap rule tests exactly the specified four-letter windows. For a closed walk with distinguished time zero, the first coordinates give the indexed periodic word, and the other coordinates are forced to be its next two symbols, including at periods 1, 2 and 3. Thus traces count all indexed periodic words, not just those of least period n. I built the adjacency independently by excluding (a=c and b=d) or (a=d and b=c), used exact characteristic-polynomial arithmetic instead of Newton sums, and recovered lambda^6 times the reverse F, G and H^2 factors. The logarithmic derivative gives the stated first fifteen counts. Möbius inversion partitions fixed points by least period; a rotation through j positions fixes exactly C_gcd(n,j) words, proving the total necklace formula by Burnside. Direct exhaustive word and rotation-class checks of both formulas through n=9 also agree. Replay: python -B /workspace/branches/independent_checks.py 5.

## originality

PASS

No inspected distinct statement determines this ternary periodic spectrum. The closest located catalogue statements use the same type of orbit invariant but impose different alphabet and window rules; the closest primary circular-avoidance formulations impose different period ranges and/or equality predicates. Credit the established transfer and orbit inversion methods, not as part of the new claim. This is a bounded comparison, not a claim of historical priority.

## value

PASS

Length two is the first root length at which anagrams give a different obstruction from literal repetition. The ternary case is a natural fixed local constraint, and periodic multiplicities are information not supplied by linear-word totals. The explicit cubic, quartic and doubled septic give the complete all-period counts and permit primitive rotation-class enumeration without constructing or powering the 27-state graph anew. Value is the exact orbit invariant for this natural rule, not novelty of the transfer procedure or a claim about all Abelian squares.

The dated certificate retains the supplied scientific assessment, sources and limitations.
