# Exactly \(4{,}800\) ternary universal cycles of four-letter words with three distinct symbols

## Finding
For the labeled ternary alphabet \(A=\{0,1,2\}\), let \(\mathcal T\subseteq A^4\) consist of every word using exactly three distinct symbols. Then there are precisely \(4{,}800\) circular 36-letter words whose cyclic length-four factors are exactly \(\mathcal T\), once each. Distinct circular words are counted modulo rotation only, not alphabet relabeling or reversal. An explicit representative is `012001210021012201020112021102210212`.

## Assumptions and scope
A circular word is a word with its indices interpreted cyclically, considered equivalent to all its rotations. Its cyclic length-four factor beginning at position \(i\) is \(w_iw_{i+1}w_{i+2}w_{i+3}\). Each factor must occur once, so the length is \(\lvert\mathcal T\rvert=3\binom42(3-1)!=36\): choose the doubled letter (three choices), its positions (six choices), and order the other two symbols (two choices). The alphabet remains labeled, and reversals are not identified.

## Proof
Construct the directed overlap graph \(D\) with vertices the length-three words and one directed arc for each \(abcd\in\mathcal T\), from \(abc\) to \(bcd\). An Euler circuit in \(D\) records a universal circular word, and conversely: the ordered arcs are exactly the consecutive cyclic length-four windows. Since all 36 arcs have distinct labels, the correspondence is bijective modulo cyclic shifts.

Only 24 vertices have positive degree. Six vertices \(abc\) with all three letters distinct have indegree and outdegree three. Eighteen vertices with exactly two distinct letters have indegree and outdegree one: their unique incoming and outgoing completion is the absent third alphabet letter. The three constant length-three words are isolated and can be discarded. Suppress all 18 one-in/one-out vertices. The 18 resulting directed arcs each have a uniquely determined path of length one, two, or three in \(D\), and every original arc lies on one such path. For each permutation \(abc\) of \(012\), the three resulting destinations are exactly \(bca\), \(cab\), and \(cba\). Indeed, the paths starting with the appended letters \(a,b,c\) are, respectively,

- \(abca\), length one, reaching \(bca\);
- \(abcb,bcba\), length two, reaching \(cba\);
- \(abcc,bcca,ccab\), length three, reaching \(cab\).

Thus the contracted graph \(H\) is the bidirected triangular prism: its six vertices are the six permutations of three symbols; even and odd permutations each induce a bidirected three-cycle, and the reversals \(abc\leftrightarrow cba\) form three matching edges between those cycles. Each of the nine undirected prism edges contributes its two opposite directed arcs. Hence \(H\) is strongly connected and has indegree and outdegree three at every vertex. The suppression/expansion is a bijection between cyclic Euler circuits in \(H\) and \(D\), because every suppressed vertex has exactly one possible incoming and outgoing arc.

The undirected triangular prism is \(C_3\square K_2\). Its Laplacian eigenvalues are \(0,2,3,3,5,5\). Kirchhoff's matrix-tree theorem gives exactly \(2\cdot3\cdot3\cdot5\cdot5/6=75\) spanning trees. In a bidirected connected graph, each spanning tree determines exactly one directed in-arborescence toward a fixed root, so the number of such in-arborescences in \(H\) is also 75. The BEST theorem counts cyclic Euler circuits of an Eulerian digraph with distinguishable arcs, fixing any one arc to normalize rotations, as the root in-arborescence count times \(\prod_v(\deg^+(v)-1)!\). It follows that the required number is

\[
75\prod_{v\in V(H)}(3-1)!=75\cdot 2^6=4{,}800.
\]

The 36 target length-four words are distinct and each occurs once, so the resulting circular word has no smaller period; fixing an arc really does identify each rotation class exactly once.

## Verification
Two standalone standard-library Python programs accompany the proof. `verify_cycles.py` constructs all 36 four-mers directly, suppresses 18 unary overlap states, enumerates all Euler tours beginning with a fixed directed edge, and reconstructs and checks every resulting circular word. It counts exactly 4,800 and checks the stated representative. `verify_prism.py` independently constructs the six-permutation graph from its three transition rules, confirms its prism structure and bidirectionality, and exhaustively checks its 75 spanning trees among the \(\binom95=126\) five-edge subsets. These are finite exact checks; the all-possible-cycle result follows from the structural bijection, matrix-tree theorem, and BEST theorem, not from a bounded sample.

Reproduce with `python3 verify_cycles.py` and `python3 verify_prism.py`. No external packages or data are needed.

## Relationship to prior work
Champlin, Godbole and Tomlinson (2013) prove existence of universal cycles for words having at least one repeated letter when the window length is at least four. That class is broader and does not provide the exact count for the 36 four-letter ternary words using exactly three symbols. Chen, Kitaev and Sun (2020) study general existence probabilities after deletions of allowed windows and small binary instances, not this fixed-content enumeration. Published work on exactly two-symbol length-four universal cycles and on adjacent-double four-letter universal cycles concerns different allowed-window sets: neither count entails the present three-distinct-symbol result. The key new exact reduction is to a bidirected triangular prism with 75 spanning trees.

## Limitations
Only length-four factors over a **labeled ternary** alphabet using exactly three distinct letters are counted. No formula for larger alphabets, different factor lengths, or counts modulo symbol permutations or reversal is claimed. The claim of historical novelty is limited by possible unindexed equivalent work and by incomplete availability of some related sources. Independent mathematical validation has not been performed.

## References
1. M. Champlin, A. Godbole, B. Tomlinson, *Universal Cycles of Complementary Classes*, arXiv:1303.3323, originally public 2013-03-14. https://arxiv.org/abs/1303.3323
2. H. Z. Q. Chen, S. Kitaev, B. Y. Sun, *Lower Bounds, and Exact Enumeration in Particular Cases, for the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, *Mathematics* **8** (2020), 778, https://doi.org/10.3390/math8050778
3. The BEST theorem for Eulerian circuits and Kirchhoff's matrix-tree theorem are standard graph-theoretic tools; both are applied with the explicit six-vertex contracted graph above.
