# Composition-refined degree and edge spectrum of the binary two-read deletion graph

## Finding
For every integer \(n\ge1\), let \(D_1(x)\) be the set of distinct strings obtained by deleting exactly one coordinate of a binary word \(x\in\{0,1\}^n\). Two different words are *confusable* if \(|D_1(x)\cap D_1(y)|=2\). For \(0\le k\le n\), let \(G_{n,k}\) be the resulting simple undirected graph induced on the words of Hamming weight \(k\), and let \(P_{n,k,d}\) be its number of vertices of degree \(d\). The complete composition-and-degree distribution has the following explicit formal generating function.

Define the formal series
\[
 A(z,u,v)=\sum_{t\ge0}z^{2t+1}u^t v^{t(t+1)},\qquad
 C(z,u,v)=\sum_{t\ge1}z^{2t}u^t v^{t^2},
\]
and the matrix \(B=\begin{pmatrix}A&C\\ C&uA\end{pmatrix}\). With \({\bf1}=(1,1)^{\mathsf T}\),
\[
 \boxed{1+\sum_{n\ge1}\sum_{k=0}^n\sum_{d\ge0}P_{n,k,d}z^n u^k v^d
 =1+{\bf1}^{\mathsf T}B(I-B)^{-1}{\bf1}.}
\]
The inverse exists as a formal power series because every entry of \(B\) has zero constant term. Coefficients are finite and nonnegative.

Write \(E_{n,k}\) for the number of edges within weight \(k\), and \(J_{n,k}\) for the number of full-graph edges between weights \(k\) and \(k+1\). Then for every \(n\ge1\), with an out-of-range binomial coefficient interpreted as zero,
\[
\boxed{E_{n,k}=\sum_{t=1}^{\lfloor n/2\rfloor}(n-2t+1)\binom{n-2t}{k-t}},
\qquad
\boxed{J_{n,k}=\sum_{t=1}^{\lfloor(n-1)/2\rfloor}(n-2t)\binom{n-2t-1}{k-t}}.
\]
There are no edges between weight layers differing by more than one. These formulas completely stratify the edges of the unrestricted binary two-read deletion graph by endpoint compositions.

Put \(r=\min(k,n-k)\) and \(s=\max(k,n-k)\). Its exact largest within-layer degree is
\[
\boxed{\max_{|x|_1=k}\deg_{G_{n,k}}(x)=r\min(s,r+1).}
\]
Finally, for any sequence \(k=k(n)\) with \(k/n\to\rho\in(0,1)\), the mean degree of \(G_{n,k}\) satisfies
\[
\boxed{\frac{1}{n\binom nk}\sum_{|x|_1=k}\deg_{G_{n,k}}(x)
\longrightarrow\frac{2\rho(1-\rho)}{1-\rho(1-\rho)}.}
\]
In particular, at asymptotically balanced composition the mean degree is \((2/3+o(1))n\), whereas the maximum is \((1/4+o(1))n^2\).

## Assumptions and scope
The words are **indexed linear binary strings**, not necklaces. A deletion ball is a set, not a multiset of deletion positions. Two distinct reads means two different length-\(n-1\) outputs. Degree means the number of *same-weight* confusable neighbors, not degree in the full unrestricted graph. Counts include the singleton layers and the case \(n=1\), which has no edges. The generating series and all finite formulas hold for every integer \(n\ge1\), \(0\le k\le n\); the limit requires \(0<\rho<1\) and no other regularity of \(k(n)\).

## Proof
**1. Canonical alternating intervals.** Proposition 9 of Cai, Kiah, Nguyen and Yaakobi [2] states that two distinct equal-length words share two distinct one-deletion descendants precisely when they agree outside a nontrivial interval and inside it are opposite phases of a two-symbol alternating word. In the binary case this is a complementary alternating interval of length at least two. It is uniquely recovered as the interval from the first to last mismatching positions. Thus neighbors of a word \(x\) are in bijection with alternating intervals of \(x\) of length at least two, by complementing the interval. An interval of even length \(2t\) has \(t\) zeros and \(t\) ones in each phase and preserves Hamming weight; one of odd length \(2t+1\), \(t\ge1\), has phase weights \(t,t+1\) and changes the weight by one. Consequently, the same-weight degree of \(x\) counts exactly its even-length alternating intervals.

**2. Unique block decomposition and the trivariate series.** Cut \(x\) at every position between two equal consecutive symbols. The resulting maximal alternating blocks are nonempty, pairwise disjoint, and uniquely defined. If a block has \(a\) ones and \(b\) zeros, the number of its even-length alternating intervals is \(ab\): every choice of opposite-symbol endpoints determines exactly one such interval. Summing \(ab\) over all blocks therefore gives the within-layer degree.

An odd alternating block of length \(2t+1\) beginning and ending in zero contributes length \(2t+1\), weight \(t\), and degree \(t(t+1)\); the corresponding one-ended block has weight \(t+1\). An even block of length \(2t\) switches its endpoints, has weight \(t\), and degree \(t^2\). These four cases are exactly the entries of \(B\), with the row indexing the initial symbol and column indexing the final symbol of the block. Adjacent blocks have equal touching symbols, so their weights compose by matrix multiplication; conversely such a path of blocks forces a cut at every concatenation boundary and hence gives the unique maximal alternating-block decomposition. Summing paths of one or more blocks gives \({\bf1}^{\mathsf T}(B+B^2+\cdots){\bf1}\). Adding the empty string yields the claimed matrix inverse identity.

**3. Exact edge stratification.** For an edge with an even differing interval of length \(2t\), there are \(n-2t+1\) placements and \(\binom{n-2t}{k-t}\) choices for the common outside bits when both endpoints have weight \(k\). The two alternating phases form exactly one unordered edge, proving \(E_{n,k}\). For an odd differing interval of length \(2t+1\ge3\), the two endpoints differ in weight by one; the common outside word has weight \(k-t\) if the lower-weight endpoint has weight \(k\). There are \(n-2t\) placements and \(\binom{n-2t-1}{k-t}\) choices for that outside word, proving \(J_{n,k}\). Distinct placements or outside strings yield distinct edges by uniqueness of the first-to-last differing interval. There are no other edges by step 1.

**4. Sharp fixed-weight maximum.** Suppose without loss of generality that the minority symbol occurs \(r\) times and the majority symbol \(s\) times. In each alternating block \(i\), let its minority and majority counts be \(a_i,b_i\). Then \(\sum_i a_i=r\), \(\sum_i b_i=s\), and \(b_i\le a_i+1\). Thus
\[
\deg_{G_{n,k}}(x)=\sum_i a_i b_i\le rs,
\qquad
\sum_i a_i b_i\le\sum_i a_i(a_i+1)\le r(r+1).
\]
If \(s=r\), a fully alternating word of length \(2r\) attains \(r^2\). If \(s\ge r+1\), take a fully alternating block of length \(2r+1\) beginning and ending with the majority symbol and pad it with the remaining majority symbols; it attains \(r(r+1)\). When \(r=0\), the all-constant word attains zero. Hence the upper bound \(r\min(s,r+1)\) is attained in every case.

**5. Fixed-density mean.** By the handshaking lemma, the mean degree in the weight-\(k\) graph is \(2E_{n,k}/\binom nk\). For each fixed \(t\ge1\),
\[
\frac{\binom{n-2t}{k-t}}{\binom nk}
=\prod_{j=0}^{t-1}\frac{(k-j)(n-k-j)}{(n-2j)(n-2j-1)}
\longrightarrow [\rho(1-\rho)]^t.
\]
Terms outside the binomial's support are zero. Each factor of a supported product is at most \(1/2\): putting \(N=n-2j\ge2\), the product of the two numerator factors is at most \(N^2/4\), and \(N/(4(N-1))\le1/2\). Thus each whole ratio is at most \(2^{-t}\). Because \(0\le(n-2t+1)/n\le1\), dominated convergence for summable series applies to \(2E_{n,k}/(n\binom nk)\), yielding
\[
2\sum_{t\ge1}[\rho(1-\rho)]^t=\frac{2\rho(1-\rho)}{1-\rho(1-\rho)}.
\]
At \(\rho=1/2\) this gives \(2/3\); step 4 gives a quadratic maximum. This completes all assertions.

## Verification
The two standalone standard-library Python programs in `verification/` can be run with `python3 verification/bruteforce.py` and `python3 verification/transfer.py`. The direct checker enumerates distinct one-deletion output sets and all \(698{,}027\) unordered word pairs across lengths \(1\) through \(10\), checks that each intersection has size at most two, and verifies all edge-stratification identities, fixed-weight degrees, and maximum-degree formulas. The independent block-expansion checker verifies coefficient counts, both edge strata, degree sums, and maximum degrees through length \(24\), and directly enumerates all word degree histograms through length \(13\). The exact outputs are `verification/bruteforce_output.txt` and `verification/transfer_output.txt`. These finite computations test definitions and formulas; the universal conclusions come from the proved bijections and inequalities, not extrapolation from tested lengths.

## Relationship to prior work
The model and deletion-ball framework are classical [1]. Cai et al. [2], Definition 8 and Proposition 9, establish the Type-A characterization from which the canonical alternating intervals follow. Chrisnata et al. [3] develop optimal-asymptotic two-read reconstruction codes but do not enumerate degrees at fixed source composition. An existing exact unrestricted edge census [4] totals all edges, while complete unrestricted degree-spectrum theorems [5,7] provide the marginal distribution \(\sum_k P_{n,k,d}\) and the all-neighbor degree of each word. Neither the stated unrestricted degree generating functions nor the overall edge count determines the joint composition/same-weight-degree array \(P_{n,k,d}\); odd alternating intervals contribute to their degrees but not to ours. A fixed-weight-two capacity theorem [6] gives an independent-set optimum in a single layer, not its all-layer degree distribution or composition-sensitive mean/max. These related results were compared through their public result texts. The present result refines the adjacency statistic under a natural constant-content restriction; it does not claim the underlying Type-A lemma, the unrestricted degree law, or code-capacity optima as new.

## Limitations
The formulas concern single deletions and two distinct reads, not repeated identical reads, multiple deletions, or arbitrary alphabets. They count local ambiguity and exact degrees; they do not yield the independence number or optimal reconstruction-code size for general weight \(k\). The asymptotic concerns the *mean* within a weight layer; no concentration theorem is asserted. Priority is assessed against the inspected literature and mathematical records, not against all unindexed historical work. Independent mathematical validation has not been performed.

## References
1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197v1, first submitted July 22, 2002, Sections 1, 2, 5. https://arxiv.org/html/math/0207197v1
2. K. Cai, H. M. Kiah, T. T. Nguyen, E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376v1, January 6, 2020, Definition 8 and Proposition 9. https://arxiv.org/abs/2001.01376
3. J. Chrisnata, H. M. Kiah, E. Yaakobi, *Optimal Reconstruction Codes for Deletion Channels*, arXiv:2004.06032v1, April 13, 2020, Sections II–IV. https://arxiv.org/abs/2004.06032
4. *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, published October 2026, full result text. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91
5. *Complete degree spectrum of the binary two-read deletion-reconstruction graph*, published November 2026, full result text. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-degree-spectrum-of-the-binary-two-read-deletion-reconst--f45a481280b1
6. *Exact two-read single-deletion capacity in the binary weight-two layer*, published October 2026, full result text. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-two-read-single-deletion-capacity-in-the-binary-weight-two--7d25cc21af64
7. *Exact degree law and Gaussian fluctuations in the two-read deletion reconstruction graph*, published November 2026, complete public result text. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-degree-law-and-gaussian-fluctuations-in-the-two-read-delet--7fbc301106f7
