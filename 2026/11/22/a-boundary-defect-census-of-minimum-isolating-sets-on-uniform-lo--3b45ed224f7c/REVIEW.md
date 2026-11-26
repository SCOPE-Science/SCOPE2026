# Independent mathematical audit

## correctness

PASS

A private vertex covers a length-3 edge interval and a junction a length-4 interval before clipping. The bound q=ceil(m/4) is attained for m≥2 by using junctions 2,6,…,4q−6 and last junction min(4q−2,m−1); the last interval reaches m and starts no later than the first uncovered edge, with q=1 interpreted as just the last junction. An optimum cannot include nested or equal intervals. For increasing ends and starts, the width deficit telescopes to the sum of private bits, consecutive overlaps and the two overhang bits. Since t≤3, an overlap equal to 3 forces length 4 on both sides; all reconstructed endpoint increments are positive. The first start and last end force all reconstructed intervals to be valid: ending at most m+1 implies start at most m−1 for length 3 and m−2 for length 4. Private choices have weight a−1 plus one for each coincident path endpoint. For q≥2 put G=1+az/(1−z); the claimed series is G^(q−2)(G−az³/(1−z))²/(1−z), which through z³ equals G^q/(1−z)−2az³. Its coefficient is sum_k binom(q,k)binom(t,k)a^k minus 2a when t=3. Single-vertex covers at m=1,2,3,4 count r,2r−1,r,1 directly. Zero defect forces exact width-four tiling, hence uniqueness.

## originality

PASS

Best of current knowledge: the all-length labelled minimum-set multiplicities and the two endpoint weights are not covered by the inspected isolation-number theory or the available circular enumeration. The minimum size by itself is elementary and is not the novelty basis.

## value

PASS

The degeneracy of optimum isolation, not just its cardinality, describes robustness of the best choices on a standard acyclic uniform family. The exact labelled formulas give all-length alternatives and identify complete rigidity at multiples of four. The boundary correction explains where cutting a periodic geometry changes the count, without relying on arbitrary size cutoffs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
