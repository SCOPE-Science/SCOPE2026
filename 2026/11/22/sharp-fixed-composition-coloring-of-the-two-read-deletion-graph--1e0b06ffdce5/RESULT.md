# Sharp fixed-composition coloring of the two-read deletion graph despite induced odd holes

## Finding
For integers \(n\ge 2\) and \(0\le k\le n\), let \(G_{n,k}\) be the simple graph on the binary words of length \(n\) containing exactly \(k\) ones. Two different words are adjacent if their sets of **distinct** outputs obtained by deleting one symbol have at least two common members. Set \(r=\min\{k,n-k\}\). Then the chromatic and clique numbers agree exactly:

\[
\boxed{\chi(G_{n,k})=\omega(G_{n,k})=r+1.}
\]

An explicit optimal coloring, hence a partition of the entire constant-composition layer into the minimum possible number of two-read-reconstructible codebooks, is
\[
\boxed{c(x)=\sum_{\substack{1\le i\le n\\ x_i=1}} i\pmod{r+1}.}
\]
Each color is a codebook from which **any two distinct one-deletion reads** uniquely determine the source word. There is also an explicit clique of size \(r+1\) for every layer. In contrast, whenever \(4\le k\le n-4\), the graph contains an induced five-cycle and is therefore not a perfect graph. Thus equality of the whole-graph chromatic and clique numbers does not arise from graph perfection.

## Assumptions and scope
The deletion deck of \(x=x_1\dots x_n\) is the set
\[
D_1(x)=\{x_1\dots x_{i-1}x_{i+1}\dots x_n:1\le i\le n\},
\]
where repeated deletion outputs count once. The graph has a vertex for **each indexed word**, not for rotation classes. An edge means \(\lvert D_1(x)\cap D_1(y)\rvert\ge2\), and every accepted read is an error-free word with one unknown deleted position. A proper graph coloring assigns distinct colors to adjacent words; its color classes are precisely feasible two-distinct-read reconstruction codes. Empty color classes need not be created. The integer \(r\) is zero at constant-weight boundaries, where the graph consists of a single vertex.

The proof uses the published *Type-A alternating-interval criterion* for the binary deletion channel [2]: two distinct words have two common, distinct deletion descendants precisely when they coincide outside the unique first-to-last differing interval and inside that interval they have opposite phases of an alternating binary word. The interval has length at least two. This criterion is independently verified on finite instances by the attached direct deletion-set program, but the all-length proof below relies on the published characterization.

## Proof
**1. Every fixed-weight adjacency changes the position sum by a controlled nonzero amount.** Let \(x,y\) be adjacent words of the same Hamming weight \(k\). By the Type-A criterion [2], on their differing interval they are the complementary phases of a binary alternating word. Because their total weights agree and they coincide elsewhere, the interval has an even length \(2t\), for some positive integer \(t\). Each word has exactly \(t\) ones and \(t\) zeros there. Thus \(1\le t\le\min\{k,n-k\}=r\). The occupied positions in the interval have alternating parity and switch to the other parity, so the sum of the occupied (one-indexed) positions changes by exactly \(t\) or \(-t\). Explicitly, if the interval starts at \(a\), one phase has ones at \(a,a+2,\ldots,a+2t-2\), the other at \(a+1,a+3,\ldots,a+2t-1\), and the sums differ by \(t\). No integer in \(\{\pm1,\ldots,\pm r\}\) vanishes modulo \(r+1\). Therefore the displayed residue coloring is proper, giving \(\chi(G_{n,k})\le r+1\). At \(r=0\), the claim is immediate.

**2. Construct a matching clique in every composition layer.** First suppose \(k\le n-k\), hence \(r=k\). For every integer \(j\) between zero and \(r\) inclusive, form
\[
x^{(j)}=(10)^j(01)^{r-j}0^{n-2r}.
\]
These are \(r+1\) distinct length-\(n\) binary words of weight \(r\). For any \(0\le j<\ell\le r\), the words \(x^{(j)}\) and \(x^{(\ell)}\) agree outside positions \(2j+1\) through \(2\ell\), and on that even-length interval consist of the two opposite alternating phases. The Type-A criterion makes them adjacent. If \(k>n-k\), instead complement every bit in the preceding construction for \(r=n-k\); bitwise complementation preserves all deletion-deck intersection sizes and changes the weight from \(r\) to \(n-r=k\). Hence \(\omega(G_{n,k})\ge r+1\). Every clique needs a different color on each vertex, so \(r+1\le\omega\le\chi\le r+1\), proving the equality.

**3. An induced odd hole survives in all interior layers.** At \(n=8,k=4\), take these five vertices in their cyclic order:

```
01011001
10011001
10010101
10101010
01011010
```

Directly deleting each of the eight possible positions from each word, deduplicating outputs and intersecting the resulting sets shows that every cyclicly consecutive pair has exactly two distinct common outputs and every nonconsecutive pair has **zero**. Thus the induced graph on these five vertices is exactly \(C_5\). For arbitrary \(n\ge8\) and \(4\le k\le n-4\), prepend \(n-k-4\) zeros and append \(k-4\) ones to every one of the five words. Their weights are then \(k\), and the first-to-last differing interval for each pair is unchanged. By the Type-A characterization, the ten adjacency/nonadjacency decisions are unchanged. The result is again an induced \(C_5\). Since a perfect graph cannot contain an induced five-cycle (the five-cycle has clique number two and chromatic number three), such \(G_{n,k}\) are not perfect.

The three steps prove all asserted conclusions, including the exact number of colors needed for a cover by compatible two-read codebooks. They do not prove an exact maximum cardinality for an individual codebook.

## Verification
Two independently implemented Python 3 programs, requiring only the standard library, accompany this result. `check_direct.py` constructs actual distinct deletion-output sets for every binary word of each weight at every length \(2\le n\le10\). It compares all unordered pairs, verifies separation of every edge by the proposed coloring and confirms the complete clique construction; it checks all ten pairs of the displayed five-cycle. The completed exhaustive run examined 124,453 pairs.

`check_intervals.py` separately generates opposite-phase even-length alternating-interval transformations, independently verifies all predicted coloring inequalities and clique incidences for \(2\le n\le14\), and checks the padded five-cycle for all \(8\le n\le16\) and \(4\le k\le n-4\). The completed run examined 247,598 directed edges. Run the programs with `python3 check_direct.py` and `python3 check_intervals.py`, respectively. Finite computations are consistency tests and do **not** replace the all-length alternating-interval proof or the published Type-A criterion.

## Relationship to prior work
Classical deletion-correcting codes and inversion-weight syndromes predate this result; in particular, Brakensiek, Guruswami and Zbarsky [1] discuss the Varshamov–Tenengolts position-sum syndrome in their 2015 work. Cai, Kiah, Nguyen and Yaakobi [2] give the two-read alternating-interval intersection classification and construct a related inversion-syndrome code **with a separate alternating-run restriction** (their Theorem 17). That is the essential existing mechanism behind Step 1, and the position-sum idea is **not** claimed as original. The observation that fixed Hamming weight itself bounds the length of relevant even alternating swaps enables coloring the entire layer without imposing a run restriction; the explicit matching clique establishes optimality.

Chrisnata, Kiah and Yaakobi [3] establish unrestricted reconstruction-code clique-based bounds and constructions, but no exact optimal coloring for every binary constant-composition layer. The related published note [4] gives an unrestricted maximum clique of \(\lfloor n/2\rfloor+1\) and a classification of alternating-interval pencils. Neither that unrestricted maximum nor its local classification implies a sharp layer-by-layer chromatic bound or the induced-odd-hole example. The result is thus the conjunction of an exact all-layer optimal coloring and the structural nonperfectness boundary, built explicitly upon known Type-A and inversion-syndrome ideas.

## Limitations
The result determines chromatic and clique numbers of the **whole** fixed-weight graph, not perfection of every induced subgraph, optimal independent-set sizes, exact color-class sizes, or the chromatic polynomial. In particular, the displayed coloring is optimal in its **number of color classes**, not necessarily in the size of any chosen class. The induced-five-cycle argument proves nonperfection for \(4\le k\le n-4\); it does not classify perfectness of the remaining layers. The explicit examples were exhaustively verified only in the stated finite ranges; the general proof uses the independently established alternating-interval criterion. Scientific priority has been checked against the cited and indexed sources, but equivalent unindexed prior treatments cannot be categorically excluded. No independent audit is claimed.

## References
1. J. Brakensiek, V. Guruswami and S. Zbarsky, *Efficient Low-Redundancy Codes for Correcting Multiple Deletions*, arXiv:1507.06175, originally posted 22 July 2015. https://arxiv.org/abs/1507.06175
2. K. Cai, H. M. Kiah, T. T. Nguyen and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376, originally posted January 2020. In particular, the Type-A characterization and Theorem 17. https://arxiv.org/html/2001.01376v2
3. J. Chrisnata, H. M. Kiah and E. Yaakobi, *Correcting Deletions With Multiple Reads*, IEEE Transactions on Information Theory 68 (2022), 7141–7158, DOI 10.1109/TIT.2022.3184868. Open author's PDF: https://yaakobi.net.technion.ac.il/files/2024/02/75_Multiple_Reads_Deletions_IT22.pdf
4. *Sharp clique bound and two-pencil structure in the two-read single-deletion graph*, published mathematical research note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-clique-bound-and-two-pencil-structure-in-the-two-read-sing--b19c2f7e6141
