# Exact capacity of binary weight-two single-deletion codes

## Finding
For each integer \(n\ge 2\), let \(\mathcal{W}_{n,2}\) be the binary words of length \(n\) with exactly two ones, and let \(D_1(w)\) denote the set of *distinct* words obtained from \(w\) by deleting exactly one symbol. A code \(\mathcal C\subseteq\mathcal W_{n,2}\) corrects one deletion if \(D_1(u)\cap D_1(v)=\varnothing\) for distinct \(u,v\in\mathcal C\). Its maximum possible cardinality is
\[
M_{n,2}=\left\lfloor\frac{3n-2}{4}\right\rfloor\quad\text{for every integer }n\ge2.
\]
An explicit optimal family is given below, in \(O(n)\) word-position operations. In particular, \(M_{n,2}=3n/4+O(1)\).

## Assumptions and scope
Positions are one-indexed, the channel deletes exactly one symbol at an arbitrary position, and the receiver observes the full resulting binary word (not merely its weight). All codewords have Hamming weight exactly two. A word is specified by its two one-positions \((i,j)\), with \(1\le i<j\le n\); denote this word by \(w_{i,j}\). Deleting a one produces an output of weight one, while deleting a zero produces an output of weight two. The theorem concerns set-valued deletion balls, so repeated outputs from different deletion positions are counted once.

## Proof
Put \(m=n-1\). The weight-one descendants of \(w_{i,j}\) have unique-one positions
\[
T(i,j)=\{i,j-1\}\subseteq\{1,\ldots,m\}.
\]
Indeed, deleting the one at position \(j\) leaves the one at \(i\); deleting the one at position \(i\) shifts the later one to \(j-1\). When \(j=i+1\), these positions coincide. Thus a word with adjacent ones consumes one available weight-one output, while a word with nonadjacent ones consumes two. In a one-deletion-correcting code, all these sets must be pairwise disjoint. Let \(t\) be the number of codewords with adjacent ones and \(e\) the number with nonadjacent ones. We obtain
\[
t+2e\le m.\tag{1}
\]
Two different adjacent-one words \(w_{i,i+1}\) and \(w_{i+1,i+2}\) cannot both occur: the former yields the weight-two word with ones at \((i,i+1)\) after deletion of a zero to the right, and the latter yields exactly the same word after deletion of a zero to the left. This applies for \(1\le i\le n-2\), including boundary cases. Consequently the starting positions of adjacent-one codewords are a nonconsecutive subset of \(\{1,\dots,m\}\), so
\[
t\le\left\lceil\frac m2\right\rceil.\tag{2}
\]
Combining (1) and (2), every permissible code has
\[
|\mathcal C|=t+e\le\left\lfloor\frac{m+t}{2}\right\rfloor
\le\left\lfloor\frac{m+\lceil m/2\rceil}{2}\right\rfloor
=\left\lfloor\frac{3m+1}{4}\right\rfloor
=\left\lfloor\frac{3n-2}{4}\right\rfloor.
\]

For the matching construction, take all adjacent-one words
\[
\mathcal A=\{w_{i,i+1}: 1\le i\le m,\ i\text{ odd}\},
\]
and add the nonadjacent-one words
\[
\mathcal B=\{w_{4r+2,4r+5}: r\in\mathbb Z_{\ge0},\ 4r+4\le m\}.
\]
The number of codewords is
\[
|\mathcal A\cup\mathcal B|=
\left\lceil\frac m2\right\rceil+\left\lfloor\frac m4\right\rfloor
=\left\lfloor\frac{3m+1}{4}\right\rfloor.
\]
Their weight-one descendants are disjoint: each word in \(\mathcal A\) has a distinct odd output position \(i\), whereas each word in \(\mathcal B\) has two output positions \(4r+2\) and \(4r+4\), both even and distinct across \(r\).

Their weight-two descendants are also disjoint. An adjacent-one input in \(\mathcal A\) always yields an adjacent-one output (and its possible output starting positions are \(i-1\) and \(i\), omitting any impossible boundary case). The two-element sets \(\{i-1,i\}\) for distinct odd \(i\) do not intersect. A word \(w_{4r+2,4r+5}\in\mathcal B\) yields weight-two descendants with one-position pairs among
\[
(4r+1,4r+4),\qquad(4r+2,4r+4),\qquad(4r+2,4r+5),
\]
with impossible boundary cases omitted. Every such pair has gap at least two, so these outputs are disjoint from all outputs of \(\mathcal A\). Across distinct \(r\), their first-one positions belong to the disjoint two-element sets \(\{4r+1,4r+2\}\). Thus distinct codewords in \(\mathcal B\) have disjoint weight-two outputs. Since outputs of different weights cannot coincide, all deletion balls in the construction are disjoint. This attains the upper bound for every \(n\ge2\), proving the theorem. \(\square\)

## Verification
The accompanying Python 3 standard-library program `check_weight_two_deletion.py` directly constructs every one-deletion descendant of all weight-two binary source words through length \(84\), including every boundary case. It checks the construction and the upper-bound arithmetic for every length \(2\le n\le84\). A separate exact maximum-clique computation on the compatibility graph verifies the optimum for every \(2\le n\le11\). Successful execution prints `WEIGHT_TWO_DELETION_ALL_CHECKS_PASS`. The infinite theorem is proved by the counting obstruction and explicit family above; finite exhaustive checks are supplementary.

## Relationship to prior work
Cullina, Kulkarni and Kiyavash (arXiv:1211.4056) investigated the constant-weight single-deletion graph and determined its chromatic number, including \(\chi(L_{1,n,k})=\max(k,n-k)+1\). The chromatic number does not determine the independence number of an induced graph, so it does not by itself yield the present exact formula for the largest fixed-weight-two deletion-correcting code. No (2019) treated nonasymptotic bounds on *unrestricted* binary one-deletion code size through mixed-integer optimization, rather than an all-length exact optimum constrained to weight two. The present result is an exact independence-number determination for this particular constant-weight layer, with a simple explicit optimal packing. No claim of novelty is made for the standard deletion-ball definitions or previously known graph-coloring results.

## Limitations
Only binary codewords of exactly two ones, one deleted symbol, and full ordered deletion outputs are covered. This does not determine the fixed-weight optimum for weights three or higher, deletion counts two or higher, or unrestricted optimal code sizes. Independent review and an exhaustive search of all unpublished literature have not been conducted.

## References
1. D. Cullina, A. Kulkarni and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056 (2012). DOI: 10.1109/ISIT.2012.6284242.
2. A. No, *Nonasymptotic Upper Bounds on Binary Single Deletion Codes via Mixed Integer Linear Programming*, *Entropy* **21**(12), 1202 (2019). DOI: 10.3390/e21121202. Publicly released December 6, 2019.
