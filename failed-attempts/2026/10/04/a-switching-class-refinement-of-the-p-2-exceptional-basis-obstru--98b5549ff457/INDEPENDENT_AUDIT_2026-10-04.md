# Independent mathematical audit

## correctness

PASS

The covariance calculation is correct: mutation has integral basis-change matrix congruent modulo \(p\) to the adjacent transposition because its coefficient is \(0\pmod p\); conjugating \(B-B^T\), dividing by \(p\), and reducing gives \(P^TAP\). Sign changes give \(DAD\), and Euler-form isometries preserve \(B\). Triangle products are sign-switching invariant and square away orientation reversal. Fresh exact enumeration reproduces both displayed fingerprints.

## originality

FAIL

Eliseev's Proposition 2 proof already tracks every Gram entry modulo \(p^2\) under the same mutation, sign-change, and isometry operations. Because the mutation coefficient is divisible by \(p\), the correction terms are \(0\pmod{p^2}\), the mutated adjacent entry is the negative of the old one, sign changes multiply the corresponding row/column by \(-1\), and isometries leave the Gram matrix fixed. Dividing the skew part by \(p\) therefore gives exactly the assigned signed-permutation covariance. The triangle-square multiset is then the standard elementary invariant of such a signed switching action. Thus the claim is a useful repackaging, but mechanically implied by the inspected primary proof.

## value

FAIL

As an efficiently computable presentation the fingerprint is useful, but the scientific content is a routine invariant extracted from an entrywise mod-\(p^2\) transformation proof already in the initiating paper, with no new separating example supplied. Under the shared value standard, an invariant mechanically implied by the prior proof does not constitute an independently valuable new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
