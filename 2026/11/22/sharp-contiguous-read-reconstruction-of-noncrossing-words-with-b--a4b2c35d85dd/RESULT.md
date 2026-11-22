# Sharp contiguous-read reconstruction of noncrossing words with bounded symbol multiplicities

## Finding

Fix an integer \(k\geq2\). A word is **noncrossing** if no two distinct letters \(a,b\) occur in the order \(a,b,a,b\) as a scattered subsequence (in either labeling order). Its **complete contiguous \(k\)-spectrum** records, for every nonempty factor of length at most \(k\), its number of overlapping occurrences, with the factor's orientation retained.

**Sharp rigidity theorem.** Every noncrossing finite word in which each letter occurs at most \(2k-2\) times is uniquely determined by its complete contiguous \(k\)-spectrum **among all words over the same alphabet**, not just among noncrossing words. This bound is sharp for every \(k\geq2\): the two distinct noncrossing words
\[
 a^{k}ba^{k-1}\quad\text{and}\quad a^{k-1}ba^{k}
\]
contain \(2k-1\) copies of \(a\), and have identical complete contiguous \(k\)-spectra.

Let \(\mathcal N_{n,k}\) be the canonical restricted-growth encodings of the noncrossing partitions of \(\{1,\ldots,n\}\) with every block of size at most \(2k-2\). Under the readout above, the exact maximum zero-error codebook in this source is the **whole source**. Its cardinality \(N_{n,k}\) is given for every \(n\ge0\) by
\[
 F_k(z)=\sum_{n\ge0}N_{n,k}z^n=1+\sum_{j=1}^{2k-2}z^jF_k(z)^j,
 \qquad F_k(0)=1.
\]
This equation specifies a unique formal power series. The counting recurrence itself is the standard noncrossing block decomposition; its reconstruction-code interpretation follows from sharp rigidity. At \(k=2\) it yields the Motzkin sequence \(1,1,2,4,9,21,51,127,323,\ldots\); at \(k=3\), the sequence begins \(1,1,2,5,14,41,125,393,1265,\ldots\).

## Assumptions and scope

The alphabet is any finite set of distinct, individually observable symbols. Words can have arbitrary lengths, including zero. For length at most \(k\), the complete spectrum includes the whole word and reconstruction is immediate. Factors are contiguous and directed, not scattered or reversal-identified; repeated factors are counted with multiplicity. The noncrossing condition applies to the true source, but **not** to rival reconstructions. For partition encodings, the first occurrence of the first block is symbol \(1\), and a new block receives the next unused positive label.

## Proof

**1. Distinct-letter bigrams cannot repeat.** If \(ab\), with \(a\ne b\), occurred at two different starting positions, the two occurrences would give positions in the order \(a,b,a,b\). Hence in any noncrossing word every contiguous factor containing two distinct letters appears at most once: such a factor contains a distinct-letter bigram whose second occurrence would be forbidden.

**2. The full spectrum supplies both endpoints.** Let \(n\ge k\), and let \(D\) be the directed order-\(k-1\) de Bruijn multigraph whose vertices are the observed \((k-1)\)-factors and whose directed edges are observed \(k\)-factors from their \((k-1)\)-prefix to their \((k-1)\)-suffix. For a vertex \(v\), its observed multiplicity as a \((k-1)\)-factor minus its indegree equals \(1\) exactly when \(v\) is the starting \((k-1)\)-factor; its multiplicity minus its outdegree equals \(1\) exactly when \(v\) is the final \((k-1)\)-factor. Thus the full spectrum identifies start and end even when they coincide. A word with this spectrum is precisely an Euler trail from the prescribed start to the prescribed end, spelling the overlap labels.

**3. Contraction of homogeneous loops.** By step 1, any vertex repeated in the trail must be homogeneous, of the form \(a^{k-1}\). Its self-loop is exactly the factor \(a^k\). A source run \(a^r\) produces \(\max(0,r-k+2)\) visits to this vertex and \(\max(0,r-k+1)\) consecutive self-loops. If a letter occurred in two separate runs each of length at least \(k-1\), their lengths would total at least \(2k-2\); the multiplicity bound therefore forces **exactly two such runs of length \(k-1\)** and no self-loop. Conversely, if a self-loop exists, there is only one run of length at least \(k-1\) and its self-loops form one forced consecutive block. Removing all homogeneous self-loops from the spelled trail leaves every vertex occurring **at most twice**. Restoring a removed loop block to any different visit would require two separate runs of lengths at least \(k\) and \(k-1\), hence at least \(2k-1\) copies of that letter, which is excluded.

**4. No interleaved repeated vertices.** After contraction, two distinct vertices appearing twice cannot have visits interleaved in the order \(u,v,u,v\). Both must be homogeneous by step 1; if \(u=a^{k-1}\) and \(v=b^{k-1}\) with \(a\ne b\), this order would give the forbidden subsequence \(a,b,a,b\). (There is only one homogeneous vertex per letter.)

**5. Euler-trail uniqueness.** The elementary trail-switch principle says that two different spellings of Euler trails with the **same prescribed start and end** require either a vertex appearing at least three times in the contracted trail or two different repeated vertices with interleaved occurrences. One proof cuts the two trails at their first differing outgoing edge, follows the displaced edge until the prefixes can rejoin, and repeats at the first return; absence of three visits forces the endpoints of two switched return segments to interleave. This is the linear-endpoint form of the classical repeat/interleaving criterion for \(k\)-mer assembly. Parallel identical self-loops do not change a spelling. Steps 3 and 4 exclude both possibilities, while step 3 fixes all removed loops. Therefore every Euler trail compatible with the spectrum spells the same original word.

**6. Sharpness.** The two displayed words have the same multiset of factors of length \(k\): each contains one \(a^k\), and for each \(0\le i\le k-1\), each contains one factor \(a^i b a^{k-1-i}\). They have the same prefix and suffix of length \(k-1\), both \(a^{k-1}\). The standard endpoint-count identity then gives equality of the counts of all shorter factors. Their letters are noncrossing (the letter \(b\) is a singleton), and the two words differ for \(k\ge2\).

**7. Capacity count.** In a noncrossing partition, the block containing \(1\) has some size \(j\). Its \(j\) ordered gaps support independent noncrossing partitions, so the ordinary generating function satisfies \(F_k=1+\sum_{j=1}^{2k-2}z^j F_k^j\). The rigidity theorem makes all restricted-growth words pairwise spectrum-distinguishable, proving that the entire source is an optimal zero-error code (no code can have more words than its source).

## Verification

The embedded Python program `verify.py` independently enumerates all words over small alphabets with the stipulated letter multiplicity, groups them by full directed contiguous spectra, and checks that every group containing a noncrossing source contains **exactly one** word. It additionally tests the sharpness pair for read lengths \(2\) through \(8\) and compares the partition-count generating function to direct enumeration of restricted-growth words. The reported bounded tests are not substitutes for the all-length argument in the Proof.

## Relationship to prior work

Karhumäki, Saarela and Zamboni (2013) define \(k\)-Abelian equivalence using exactly this complete factor-count spectrum and establish the endpoint characterization (Lemma 2.3). The Ukkonen–Pevzner repeat/interleaving criterion for spectrum assembly, described concretely by Bresler, Bresler and Tse (2013), supplies the general Euler-trail principle, not the noncrossing multiplicity threshold. Lin and Fu (2017) characterize the 1212-avoiding restricted-growth representation of noncrossing partitions and study different partition statistics; their results do not assert a sharp all-read-length rigidity threshold. The special case of fully doubled noncrossing words at read length two is already known and is strictly subsumed here; the all-\(k\) optimal \(2k-2\) boundary and its limited-block partition capacity are the points being assessed.

## Limitations

The result concerns error-free factor-count readout, not noisy or missing reads, circular spectra, unordered factors, or scattered subsequences. The capacity is for a constrained noncrossing partition source and does not imply a capacity formula for unrestricted words. The general repeat/interleaving assembly principle and classical noncrossing enumeration are antecedents, not new discoveries. Novelty relative to earlier unindexed combinations of these principles is not externally certified; independent review has not been performed.

## References

- J. Karhumäki, A. Saarela, and L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104v1, first public 2013-01-22. https://arxiv.org/html/1301.5104v1
- G. Bresler, M. Bresler, and D. Tse, *Optimal assembly for high throughput shotgun sequencing*, BMC Bioinformatics 14 (2013), S18, 2013-07-09. https://doi.org/10.1186/1471-2105-14-S5-S18
- Z. Lin and S. Fu, *On 1212-avoiding restricted growth functions*, Electronic Journal of Combinatorics 24 (2017), P1.53, 2017-03-17. https://doi.org/10.37236/6728
- E. Şaşoğlu and D. Tse, *DNA assembly from paired reads as 2-D jigsaw puzzles*, IEEE International Symposium on Information Theory (2014), section II.A on the existing one-dimensional assembly criterion. https://web.stanford.edu/~dntse/papers/conf_st14.pdf
