# Independent mathematical audit

## correctness

PASS

Over the fixed field F_q, commuting idempotents are ordered decompositions of the nilpotent F_q[t]-module into image and kernel; the projection is unique for each decomposition. The multiplicities add by uniqueness of the cyclic summands, and orbit-stabilizer gives the stated ordered profile count. Independently checking the unit-group factor: Hom between cyclic blocks of sizes i,j has dimension min(i,j). Reducing modulo t gives a block triangular matrix ordered by lengths, since maps from a shorter source into a longer block reduce to zero. Invertibility is equivalent to invertibility on M/tM by the finite nilpotent filtration, hence to each same-length leading block being invertible; this gives exactly q^D times the product of the stated Phi factors. The resulting Gaussian coefficient formula follows. The identity gives degree n, and the empty space gives polynomial 1. The first positive rank d is the shortest summand length. Its coefficient equals q^(2d(B−1)) times the geometric sum of m_d terms lying in [1,q), including at q=2; the exact base-q integer logarithm recovers B. After shorter multiplicities are known, their contributions at rank j need only the number B−S_j of blocks of length ≥j, since min(i,l)=i for i<j≤l. The rank-j residual can use only a single length-j summand; it is zero if absent and otherwise a known power of q times a strictly increasing finite geometric sum giving m_j. This closes the induction through n and similarity is equivalent to partition equality in the nilpotent class. Separate direct enumeration of every 3×3 candidate over F₂, for each of the three partitions, gave coefficient vectors (1,0,0,1), (1,4,4,1), (1,28,28,1); replay details are in /workspace/branches/9ec909e3-e716-425f-a9cb-fbdae5be481d/record3-independent-check.md. Source scripts and recorded logs were inspected, not executed. The exhaustive small-matrix check and the separate logged formula tests through n=22 are finite corroboration only.

## originality

PASS

The forward profile count is existing orbit-stabilizer input and is not credited as new. The distinct surviving claim is the inverse for every nilpotent Jordan partition from its ordinary-rank commuting-idempotent polynomial. Actual inspected analogues use other ranks, idempotents, or operator classes, and the closest forward formulas do not supply the rank-coefficient inverse.

## value

PASS

The invariant is natural: it grades all splittings of an operator module by image dimension without observing image Jordan types. It is not apparent that the resulting coarse sums can separate arbitrary partitions. Recovering the total number of blocks from the shortest-rank term and subtracting lower-length contributions with limited information gives a uniform constructive rigidity theorem, not a re-enumeration or a small-table observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
