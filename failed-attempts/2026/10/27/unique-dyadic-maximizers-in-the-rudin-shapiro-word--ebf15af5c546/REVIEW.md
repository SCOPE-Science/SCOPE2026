# Independent mathematical audit

## correctness

PASS

At length L=2^k every start has an aligned block pair and offset; the eight legal pairs follow from internal and boundary pairs of the substitution and all occur in σ^4(a). Splitting at half the block gives the two stated branches for F: add the first block's second-half sum for the first branch, and the next block's first-half sum for the second. Taking maxima checks T and the G matrices from k=2,3 and their parity updates. Restricting to legal pairs excludes da for even k and cb for odd k, leaving ba and ca respectively. For even k with parameter t=2^(k/2), the ca/cb child branches compare 4t-2 versus 2t, strictly inheriting J_k(da). For odd k with parameter t=2^((k+1)/2), the ba/da branches compare t versus 3t-2, strictly inheriting J_k(cb) with a shift of 2^k. At k=2 the ba and da words have the sole maximizing offset 3; the resulting recursion gives j_k and stays strictly below L. This proves uniqueness of the distinct word, not of its occurrence. A separate finite check used signs (-1)^popcount(i&(i>>1)) and running sums and compared the actual maximizing words and offsets in the prefix of length 2^(k+4), for 2≤k≤12; this prefix contains all legal pairs at scale k. It agreed, for example (k,M_k,j_k)=(2,4,3),(3,6,3),(12,190,2731). The bundled verification.py was inspected but not executed; neither finite check is used in place of induction.

## originality

FAIL

The extremal sums are already a specialization of the published Abelian-complexity recurrence. A distinct indexed first-attainment record has the same offset and blocks, and its proof mechanically implies uniqueness, not merely the existence of an earliest witness. This is demonstrable current mathematical coverage; the catalogue paths are not used to adjudicate historical priority or copying.

## value

FAIL

Distinguishing the extremal word from its sum and from its occurrence positions is a worthwhile question. In this record, however, current coverage supplies the sums, blocks and offsets and forces uniqueness by the two strict prefix comparisons. The alternate max-matrix proof does not establish an additional invariant or consequence outside that coverage. There is no remaining claim to repair on the stated dyadic range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
