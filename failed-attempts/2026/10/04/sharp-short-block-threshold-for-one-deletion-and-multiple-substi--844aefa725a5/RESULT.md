# Sharp short-block threshold for one deletion and multiple substitutions
## Finding
For every alphabet size \(q\ge 2\) and integer \(s\ge 0\), let \(M_{q,s}(n)\) denote the largest size of a length-\(n\) code over an alphabet \(\Sigma_q\) such that the sets of words obtainable from distinct codewords by exactly one deletion and at most \(s\) substitutions are disjoint. Then
\[
M_{q,s}(n)=1\qquad(1\le n\le 2s+1),
\]
and
\[
M_{q,s}(2s+2)=q.
\]
Hence \(2s+2\) is the first block length at which this channel permits a code with more than one codeword. At that first nontrivial length, the \(q\) constant words \(a^{2s+2}\), one for each \(a\in\Sigma_q\), form an optimal code.

## Assumptions and scope
The alphabet is any finite set \(\Sigma_q\) with \(q\ge2\). A channel output is obtained by deleting exactly one source symbol and then changing at most \(s\) of the remaining symbols; the order of deletion and substitution is immaterial for the set of possible length-\(n-1\) outputs. A code corrects this error pattern when distinct codewords have disjoint output sets. The statement concerns only the sharp short-block boundary \(n\le2s+2\); it makes no claim about optimal code sizes at longer block lengths.

## Proof
Fix a codeword \(x=x_1\cdots x_n\) and delete its last coordinate. The resulting prefix \(p(x)=x_1\cdots x_{n-1}\) has length \(m=n-1\). Every word in the Hamming ball of radius \(s\) around \(p(x)\) is therefore a legal channel output of \(x\).

Suppose two distinct codewords \(x,y\) belong to a correcting code. Their channel-output sets are disjoint, so the two radius-\(s\) Hamming balls centered at \(p(x)\) and \(p(y)\) must also be disjoint. Two \(q\)-ary Hamming balls of radius \(s\) intersect whenever their centers have Hamming distance at most \(2s\). Indeed, if the center distance is at most \(s\), one center lies in the other ball. If the distance is \(d\) with \(s<d\le2s\), change \(d-s\) of the differing coordinates of the first center to the corresponding symbols of the second; the resulting word is at distance \(d-s\le s\) from the first center and distance \(s\) from the second. Therefore every pair of distinct codewords must satisfy
\[
d_H(p(x),p(y))\ge2s+1.
\]

If \(n\le2s+1\), then \(m=n-1\le2s\), whereas two length-\(m\) words have Hamming distance at most \(m\). Thus no two distinct codewords can coexist, and \(M_{q,s}(n)=1\).

Now let \(n=2s+2\), so \(m=2s+1\). The same inequality forces every pair of prefixes to differ in all \(m\) positions. In particular, their first symbols are distinct. The first-coordinate map is therefore injective on the code, giving \(|C|\le q\).

For the matching lower bound, take
\[
C_0=\{a^{2s+2}:a\in\Sigma_q\}.
\]
Deleting any coordinate of \(a^{2s+2}\) gives the single descendant \(a^{2s+1}\). For distinct symbols \(a,b\), these descendants have Hamming distance \(2s+1>2s\), so their radius-\(s\) Hamming balls are disjoint by the triangle inequality. Hence \(C_0\) corrects the stated error pattern and has size \(q\), proving optimality.

## Verification
The proof is all-parameter and does not depend on finite computation. The accompanying standard-library verifier independently constructs the channel output set by explicit deletion and Hamming-ball enumeration. It checks all words for \(0\le s\le2\) and \(2\le q\le3\): below the threshold it confirms that every pair of source words has intersecting output sets, and at \(n=2s+2\) it checks that every compatible pair has different first symbols and that all \(q\) constant words are pairwise compatible. The recorded run ends with `VERIFY_OK short_block_threshold s<=2 q<=3 direct_channel`.

## Relationship to prior work
Smagloy, Welter, Wachter-Zeh, and Yaakobi introduced and analyzed single-deletion single-substitution correcting codes and defined the corresponding deletion/substitution error balls and extremal code-size notation. Their 2020 conference paper gives nonasymptotic bounds for the one-substitution problem and extends constructions to multiple substitutions in the binary setting; its displayed nonbinary upper-bound theorem for one substitution applies only from substantially longer block lengths. Later work by Song, Polyanskii, Cai, and He develops systematic constructions for multiple deletions and substitutions, again with an asymptotic coding focus. The present statement instead determines the exact first nontrivial block length and its exact optimum simultaneously for every finite alphabet and every substitution radius.

## Limitations
The result is deliberately local in block length: it determines all lengths through \(2s+2\) and does not estimate \(M_{q,s}(n)\) for \(n\ge2s+3\). The finite verifier is corroborative rather than a proof of the universal quantifiers. The literature comparison cannot exclude an unindexed or differently phrased prior statement of this elementary sharp boundary.

## References
1. A. Smagloy, L. Welter, A. Wachter-Zeh, and E. Yaakobi, “Single-Deletion Single-Substitution Correcting Codes,” arXiv:2005.09352, first public version 2020-05-19; IEEE ISIT 2020, DOI: 10.1109/ISIT44484.2020.9174213.
2. W. Song, N. Polyanskii, K. Cai, and X. He, “Systematic Codes Correcting Multiple-Deletion and Multiple-Substitution Errors,” IEEE Transactions on Information Theory 68 (2022), DOI: 10.1109/TIT.2022.3177169.
3. A. Smagloy, L. Welter, A. Wachter-Zeh, and E. Yaakobi, extended journal treatment of single-deletion single-substitution correcting codes, IEEE Transactions on Information Theory (2023), DOI: 10.1109/TIT.2023.3319088.
