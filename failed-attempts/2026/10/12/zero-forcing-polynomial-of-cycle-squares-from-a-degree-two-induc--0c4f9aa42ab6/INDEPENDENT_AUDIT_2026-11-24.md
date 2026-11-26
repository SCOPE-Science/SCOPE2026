# Independent mathematical audit

## correctness

PASS

In the four-regular cycle square, initial induced degree at most two at all blue vertices permits no first force. A blue vertex with three or four blue neighbors fills its closed neighborhood, which consists of five consecutive cyclic vertices. In any proper maximal blue interval containing these five, the penultimate vertex can force the next vertex beyond the interval, so propagation reaches the whole graph. The length-five window test therefore describes exactly the failed sets for n≥7. Four-bit states give one closed walk with fixed time origin per labeled valid word, of weight z to the number of blue vertices. I reproduced det(I−uT) independently by sparse signed Laplace expansion, obtaining exactly 1−u−zu²−z²u³−z³u⁵+z⁴u⁷+z⁵u⁸. The negative logarithmic derivative in u, multiplied by u, gives the trace numerator and hence the failed-set coefficients; subtracting from (1+z)^n gives the forcing polynomial. Only coefficients n≥7 are interpreted as graph enumerators. At size four, the center plus three neighbors gives 4n presentations; two centers at distance one require the two remaining vertices to be the other consecutive common neighbors, and centers at distance two have only one common neighbor for n≥7. Thus only the n consecutive four-sets are counted twice, and they have exactly two centers. The crossing-edge bound gives 2|S|≤4(n−|S|) for failed S; the stated cyclic words attain the floor by the local test, including both residue boundaries. Replay: python3 /workspace/branches/independent_exact_checks.py, check_cycle_determinant(). The packaged Newton-identity checker and recorded n=7 through 14 census were inspected, not run; the unrestricted result follows from propagation and the fixed-size formal calculation.

## originality

FAIL

The strongest distinct indexed comparison, a06a1735df72, gives an all-forts gap law on the identical labeled cycle square throughout the frozen range. Every stalled initial blue set has a nonempty white complement that is itself a fort, and conversely a white fort makes the blue complement failed. Thus the other record's rule is equivalent to the full set classification, not merely to the numerical largest-failed-size corollary. Moreover the exact frozen rational function is a direct weighted cyclic-word evaluation of that very rule; the implication is exhibited below. The rational form is not stated verbatim in the comparison record. This is a decision on demonstrable coverage in the inspected corpus, not an attribution of historical priority or a claim that the later-displayed record preceded the frozen one.

## value

FAIL

The family and full cardinality distribution are naturally motivated, and the compact rational form is convenient. But as a separate contribution against the matched all-forts law, the frozen result adds only a complement reformulation and its routine weighted evaluation; the same local rule gives the identical denominator on a smaller state space. The extremal consequences are covered as well. No additional structural or quantitative conclusion survives this comparison to support a separate valuable claim, and no merely expository repair is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
