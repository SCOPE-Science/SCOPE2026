# Independent mathematical audit

## correctness

PASS

The n=3 distance-class bound sums min(C(3,k)2^k,C(3,k)2^(3-k))=1+6+6+1=14. At equality cardinalities force (2,7) up to user swap. Two words at Hamming distance r generate 2^(3-r) disjoint cross-row collision pairs in the entire cube; deleting one word can remove all collisions only at r=3. With antipodal words, deleting either of their two elements removes the unique collision. Four antipodal unordered pairs times two omitted words times two user orientations gives exactly 16 ordered extrema and one common-cube-isometry/user-swap orbit. Independent exhaustive enumeration of all 255^2 ordered nonempty binary-code pairs returned max 14 and 16 extremizers. The finite experiment is exhaustive for n=3 only.

## originality

FAIL

FAIL: Van Tilborg (1984) Theorem 2.4 already proves, for EVERY block length n, that a uniquely decodable pair with size-two first user has second size at most 2^n-1, with equality if and only if the two words are antipodal and the second code is the whole cube with one of those words deleted (after common coordinate-complement normalization). Its Table I explicitly lists the length-three size-(2,7) construction. Combined with Van Tilborg 1983 distance-class upper bound 14, this entails every equality case, the 16 labeled counts and the single orbit by routine counting. This is complete prior coverage, not a search gap.

## value

FAIL

FAIL: Although exact blocklength-three equality classification is a natural question and correct, its complete answer was already explicitly characterized by the general 1984 Theorem 2.4 and the n=3 table. Counting the 16 marked antipodal pairs and one symmetry orbit is an immediate specialization, not independently unknown substantive mathematics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
