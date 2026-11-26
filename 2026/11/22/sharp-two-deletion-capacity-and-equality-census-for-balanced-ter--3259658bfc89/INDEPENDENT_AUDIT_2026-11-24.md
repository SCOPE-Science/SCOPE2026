# Independent mathematical audit

## correctness

PASS

The 90 sources are precisely the ordered strings with two of each of three labeled symbols. Two sources are confusable if and only if they both contain the same length-four subsequence: duplicate deletion choices from one source contribute one read, not several. Independently generated all sources and the 54 admissible reads by filtering Cartesian products, tested subsequences by a greedy scan, and iteratively grew increasing lists of sources with disjoint read masks, using the union of occupied read masks rather than a compatibility graph. Each admissible codebook appears once, since it has a unique increasing order. The counts from sizes 0 to 5 are 1,90,1164,1788,144,0; absence of size five excludes larger codes. The four-word example was found among the 144. The images of the 14 frozen representatives are pairwise disjoint and exactly exhaust the 144, with four classes of size six and ten of size twelve, for the stated action of symbol relabelings and reversal. Independently tested both fractional certificates in integer units: primal objective 300/60 and maximum read load 60/60; dual has 30 positive reads of weight 1/6 and minimum source coverage 6/6. Weak duality proves exactly five, distinct from the integer optimum four. Replay: python3 /workspace/reproductions/2.py. This exhaustive argument applies to the specified length, composition, and ordered read channel only.

## originality

PASS

Best-of-knowledge pass for the precise ordered-shadow packing number, maximizing-codebook and orbit censuses, and fractional optimum. The strongest same-parameter Ulam hit has a different metric and symmetry, not a conflicting enumeration of this problem; the same-source one-deletion theorem is a different confusability graph. Full-text limitations for the direct multipermutation literature remain material risks, not support for negative coverage claims.

## value

PASS

Composition (2,2,2) is the smallest uniformly repeated ternary source space, a natural benchmark for ordered deletions with repeated symbols. It gives an exact integral obstruction not captured by the natural deletion-shadow LP, which permits five rather than four. Moreover the census specifies all equality configurations up to the channel's natural symmetries, useful for comparing short-code designs and stronger relaxations even though no asymptotic claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
