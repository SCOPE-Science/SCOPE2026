# Poisson two-deletion sphere deficiency for random permutations

## Finding
For uniform \(\pi\in S_n\), let \(B_{n,2}(\pi)\) be its exact two-position permutation-invariant deletion sphere. Put \(D_n(\pi)=\binom{n}{2}-B_{n,2}(\pi)\). Then
\[
D_n(\pi)=(n-2)J_n(\pi)+O_{\mathbb P}(1),\qquad D_n(\pi)/n\ \xrightarrow{d}\ \operatorname{Poisson}(2),
\]
where \(J_n(\pi)=\sum_{i=1}^{n-1}\mathbf1\{|\pi_{i+1}-\pi_i|=1}\).

## Assumptions and scope
All \(n\ge3\) are integers, \(\pi=(\pi_1,\ldots,\pi_n)\) is uniform on permutations of \(\{1,\ldots,n\}\), and \(\operatorname{std}\) replaces every survivor by its relative rank. Two deleted position sets count as the same output exactly when their standardized survivors agree. The randomness is in the source permutation, not in the deletion positions. No cyclic wraparound is allowed.

## Proof
**1. Nearby pairs.** Define \(T_n(\pi)\) to count unordered original index pairs \(\{i,j}\) with \(1\le |i-j|\le2\) and \(1\le|\pi_i-\pi_j|\le2\). Uniformity gives
\[
\mathbb E T_n=(2n-3)\frac{4n-6}{n(n-1)}=O(1).
\]
Consequently \(T_n=O_{\mathbb P}(1)\). Each original *unit bond* \(\{i,i+1}\), satisfying \(|\pi_{i+1}-\pi_i|=1\), produces \(n-2\) equality edges between the two-deletion sets \(\{i,u}\) and \(\{i+1,u}\), as \(u\) runs outside the bond. This equality holds because deleting either end of two consecutive positions carrying consecutive values yields the same standardized sequence, even after deletion of another index.

**2. Bond-equivalence graph.** Form a graph on the \(\binom n2\) two-deletion sets by including all those unit-bond equality edges. Assume no two unit bonds share an endpoint. Its edge count is \((n-2)J_n\). A vertex representing two deleted positions can slide each deleted position along its unit bond; the connected components are isolated vertices, single edges, and squares, with exactly one square per pair of distinct bonds. (If the deleted set contains both endpoints of one bond, that bond offers no slide.) Hence the number of vertices minus connected components, which we call \(D_n^\circ\), is exactly
\[
D_n^\circ=(n-2)J_n-\binom{J_n}{2}.
\]
Every bond graph component has a single standardized output, so \(D_n\ge D_n^\circ\).

**3. Bounding every remaining collision.** Take two different two-deletion sets \(S,S'\) with the same standardized output. For any two original survivor entries matched at the same standardized position, their original indices differ by at most two (each embedding omits two positions). Their original VALUES also differ by at most two (each standardization omits two distinct values). Thus every unmatched-index pairing is an edge counted by \(T_n\).

If \(|S\cap S'|=1\), call their common deletion \(u\). In the length-\(n-1\) permutation obtained by removing \(u\), the remaining two single-deletion outputs agree. The elementary single-deletion run lemma says that two deletion positions have the same standardized output exactly when they lie in one monotone run of consecutive values. To verify it, compare the two ordered survivor sequences: entries between the deleted endpoints must each shift by one rank with a common sign; this forces successive values to be consecutive, and the converse follows by adjacent swaps of which endpoint is deleted. Therefore this collision is joined by a chain of adjacent single-deletion slides after removal of \(u\). Any such slide comes from an original unit bond, unless removal of \(u\) makes two originally non-bonded entries adjacent both in POSITION and in VALUE. The latter pair has original position and value gaps at most two and hence belongs to \(T_n\). Because at least one of its two gaps equals two, the intermediate position or intermediate value uniquely determines \(u\); each non-bond nearby pair can generate at most one exceptional slide edge over all \(u\). There are therefore at most \(T_n\) exceptional edges required for all common-deletion collisions.

If \(S\cap S'=\varnothing\), every one of the four indices in \(S\cup S'\) survives in one of the two outputs but not the other. At its survivor-rank it must be matched to a *different* original index, so each of those four indices is an endpoint of an edge counted by \(T_n\). There are at most \(2T_n\) such endpoints, hence at most \(\binom{2T_n}{2}^2\) ordered pairs of disjoint deletion sets possibly giving this type of collision. Adding these pairs as graph edges can increase the number of identified vertices by at most their number.

Putting the two cases together gives on the event of disjoint unit bonds the deterministic inequality
\[
(n-2)J_n-\binom{J_n}{2}\le D_n\le(n-2)J_n-\binom{J_n}{2}+T_n+\binom{2T_n}{2}^2.
\]
For the random source, the probability of two consecutive unit bonds sharing an endpoint is \(O(n^{-1})\): three values must form a monotone run of consecutive integers, an event of probability \(2(n-2)/(n(n-1)(n-2))\) for any specified three positions. Since \(J_n\le T_n=O_{\mathbb P}(1)\), the displayed inequality proves \(D_n-(n-2)J_n=O_{\mathbb P}(1)\).

**4. Poisson limit.** For fixed \(k\), expand the falling-factorial moment \(\mathbb E(J_n)_k\) over ordered selections of distinct adjacent-position edges. Collections with \(k\) mutually disjoint edges have \(n^k+O_k(n^{k-1})\) selections and satisfy all \(k\) adjacent-value constraints with probability \((2/n)^k(1+O_k(n^{-1}))\). Selections whose positional edges form only \(c<k\) runs number \(O_k(n^c)\), while the probability of all their constraints is \(O_k(n^{-k})\): each run of \(r\) edges forces a monotone string of \(r+1\) consecutive values and so has only \(O(n)\) value placements. Their total contribution vanishes. Therefore \(\mathbb E(J_n)_k\to2^k\) for every fixed \(k\), the factorial moments of \(\operatorname{Poisson}(2)\). The method of moments gives \(J_n\xrightarrow{d}\operatorname{Poisson}(2)\). Slutsky's theorem and step 3 finish the proof.

## Verification
A standalone checker compares exact standardized two-deletion outputs, the bond-graph component count, and the deterministic deficiency sandwich exhaustively for \(4\le n\le8\). It additionally tests randomly sampled permutations of larger lengths. These finite checks are regression tests; the all-length proof is above.

## Relationship to prior work
Wu, Bui, Niu, Vu and Wang (2026) define and study permutation-invariant deletions, primarily through constructive systematic code families. Ray and West (2003) analyze the permutation pattern poset, especially its two-insertion *upper* shadow; their introduction distinguishes the harder downward shadow. Diaconis, Evans and Graham (2013) study unseparated value pairs in random permutations and related Poisson laws; the Poisson limit for the bond count is not claimed as new. The statement here concerns the normalized collision deficit of the **two-deletion downward sphere**; it is not a consequence of an insertion count, a one-deletion count, or the known bond law alone without the collision comparison in step 3.

## Limitations
The theorem is asymptotic, for exactly two standardized deletions of uniform permutations. It does not give a finite-\(n\) exact distribution, expected deficit correction, nonuniform-source laws, or optimal correcting-code sizes. The prior-art comparison is based on accessible literature and cannot rule out unindexed equivalent results. No independent mathematical audit has been carried out.

## References
1. B. Wu, Q. D. Bui, K. Niu, V. K. Vu and S. Wang, *Order-Optimal Systematic Permutation Codes for Correcting t Deletions*, arXiv:2609.37578v1, first public September 29, 2026, https://arxiv.org/abs/2609.37578.
2. N. Ray and J. West, *Posets of matrices and permutations with forbidden subsequences*, Annals of Combinatorics 7 (2003), 55–88, https://eprints.maths.manchester.ac.uk/609/1/lume2wjganftta0j.pdf.
3. P. Diaconis, S. N. Evans and R. Graham, *Unseparated pairs and fixed points in random permutations*, arXiv:1308.5459, https://arxiv.org/abs/1308.5459.
4. P. Hegarty, *Permutations all of whose patterns of a given length are distinct*, arXiv:1206.0966, https://arxiv.org/abs/1206.0966.
