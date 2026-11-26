# Independent mathematical audit

## correctness

PASS

Greedy full-alphabet blocks characterize scattered universality: the last symbol of the shortest complete prefix has no earlier occurrence, so the targets starting with that symbol force (k−1)-universality in the remaining suffix. The even length bound qk follows by counting blocks. For odd k, at most one symbol of a palindrome can have odd multiplicity; k occurrences of each letter requires length at least q(k+1)−1. Both bounds are achieved by the displayed mirrored blocks. At even equality, every complete block has length q with no remainder. At odd equality, relative to any partition with 2m+1 complete blocks (and possibly a tail), the first m left and right greedy blocks stop no farther inward than those of the same partition. Hence they are disjoint and leave a central palindrome containing the partition's middle complete block. Its length is at least 2q−1, with equality exactly for VcV^R; each of the removed blocks must then have length q. This includes m=0. Fixed block boundaries give unique decoding, with q! choices for each initial permutation and q(q−1)!=q! choices for the odd center.

## originality

FAIL

The minimum, all equality forms, and counts are routine shortest-block consequences of the earlier, stronger palindrome midpoint relation of Barker et al., arXiv:2003.04629v1, Proposition 15, together with its greedy arches. The exact bundled extremal statement need not be printed in the prior paper to be covered. A distinct later Resultary distribution theorem independently covers all extremal counts and explicitly gives the same structural lever. This is coverage, not an inference about provenance of the submitted proof.

## value

FAIL

The normal forms make a useful illustration of the midpoint theorem, but the asserted contribution consists solely of minimizing the lengths of its already characterized arches and remainder and multiplying their independent permutation counts. There is no new structural constraint or unresolved extremal choice after applying the theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
