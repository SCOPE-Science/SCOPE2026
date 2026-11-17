# Sharp all-length size of binary weight-two single-deletion-correcting codes

## Finding

For every integer \(n\ge2\), the maximum number of binary words of length \(n\) and Hamming weight exactly two that correct one arbitrary deletion is

\[
A^{\mathrm{del}}_2(n)=\left\lfloor\frac{3n-2}{4}\right\rfloor
=\left\lfloor\frac n2\right\rfloor+\left\lfloor\frac{n-1}{4}\right\rfloor.
\]

An explicit optimum consists of words with their two one-positions at \((2r,2r+1)\), together with words having one-positions \((4r+1,4r+4)\), whenever both positions lie in \(\{0,\ldots,n-1\}\). Positions are zero-indexed. The formula, construction, and proof hold at every length in the stated range, not only at experimentally tested lengths.

## Assumptions and scope

A binary length-\(n\) word \(x\) has a *distinct one-deletion shadow* \(D(x)\), the set of length-\(n-1\) words resulting from deleting exactly one symbol in an arbitrary position. Repeated resulting words count once. A code \(C\) corrects one deletion if \(D(x)\cap D(y)=\varnothing\) whenever \(x,y\in C\) and \(x\ne y\). Let \(\mathcal W_{n,2}\) be the set of length-\(n\) words with exactly two one-symbols and define \(A^{\mathrm{del}}_2(n)=\max\{|C|:C\subseteq\mathcal W_{n,2},C\text{ corrects one deletion}\}\).

The binary alphabet, exact weight two, single deletion (not substitution), *distinct* outputs, and all integers \(n\ge2\) are essential to this statement. This is not a statement about unrestricted binary deletion codes, other constant weights, larger alphabets, or multiple deletions.

## Proof

Write a weight-two word as \(w_{i,j}\), with one-positions \(0\le i<j<n\). Call it *adjacent* when \(j=i+1\), and *separated* otherwise. The weight-one members of its deletion shadow are obtained only by deleting a one. If \(j=i+1\), both deletions give the same length-\(n-1\) word with its sole one at position \(i\). If \(j\ge i+2\), these deletions give two different weight-one outputs, having their unique ones at positions \(i\) and \(j-1\). There are exactly \(n-1\) possible weight-one outputs of length \(n-1\).

Let \(a\) and \(b\) be the numbers of adjacent and separated words in any one-deletion-correcting code. Disjointness of full deletion shadows implies disjointness of their weight-one parts, so
\[
a+2b\le n-1.\tag{1}\]

Moreover two adjacent words \(w_{i,i+1}\) and \(w_{i+1,i+2}\) cannot both belong to the code for \(0\le i\le n-3\). Indeed, deleting a zero after the adjacent pair in the first word yields the weight-two word with one-positions \((i,i+1)\) of length \(n-1\), while deleting a zero before the pair in the second word yields exactly the same output. Thus, the adjacent words that are selected correspond to an independent set of the path with vertices \(0,1,\ldots,n-2\); in particular,
\[a\le\left\lceil\frac{n-1}{2}\right\rceil.\tag{2}\]

Equations (1) and (2) give
\[
|C|=a+b\le\left\lfloor\frac{n-1+a}{2}\right\rfloor
\le\left\lfloor\frac{n-1+\lceil(n-1)/2\rceil}{2}\right\rfloor
=\left\lfloor\frac{3n-2}{4}\right\rfloor.
\tag{3}
\]

For equality, choose the following two families of pairs of one-positions:
\[
P=\{(2r,2r+1):0\le2r+1<n\},\qquad
Q=\{(4r+1,4r+4):0\le4r+4<n\}.
\]

The family \(P\) contains \(\lfloor n/2\rfloor\) words and \(Q\) contains \(\lfloor(n-1)/4\rfloor\). To prove that all their complete deletion shadows are pairwise disjoint, distinguish the number of ones in each output.

For **weight-one outputs**, a pair in \(P\) contributes the unique one-position \(2r\), always even. A pair in \(Q\) contributes precisely the two one-positions \(4r+1\) and \(4r+3\), always odd. These positions are distinct within \(Q\) for different values of \(r\) and never coincide with a position from \(P\).

For **weight-two outputs**, deleting a zero from \(w_{2r,2r+1}\) yields one-positions \((2r-1,2r)\), when there is a zero before the pair, or \((2r,2r+1)\), when there is a zero after it. All such output pairs are adjacent and differ for distinct members of \(P\) because the source adjacent indices \(2r\) are nonconsecutive. Deleting a zero from \(w_{4r+1,4r+4}\) yields one of \((4r,4r+3)\), \((4r+1,4r+3)\), or \((4r+1,4r+4)\), subject to the existence of the corresponding zero region. Each such output has separated one-positions, so it cannot collide with a \(P\) output. For different members of \(Q\), their output-pair first positions are contained in disjoint sets \(\{4r,4r+1\}\); for a fixed member, the three displayed pairs are distinct. Hence all weight-two shadows are pairwise disjoint. No other output weights can occur after exactly one deletion from a weight-two word.

Therefore \(P\cup Q\) is a correcting code of size \(\lfloor n/2\rfloor+\lfloor(n-1)/4\rfloor\), which equals the upper bound in (3) for every integer \(n\ge2\). This completes the proof. \(\square\)

## Verification

The included `verify.py` is a standalone Python 3 standard-library program. Run `python3 verify.py` in the directory containing the extracted file. It checks the deletion shadows of every constructed word for all lengths \(2\le n\le120\), and independently constructs the complete weight-two confusability graph and calculates an exact maximum independent set by recursive branch-and-bound for \(2\le n\le12\). It prints `VERIFY_OK construction_lengths=2..120 exact_maximum_lengths=2..12` and `exact_maxima_n2_to_n12=1,1,2,3,4,4,5,6,7,7,8`.

These computational tests are finite checks, not the justification for the all-length conclusion. The upper bound (1)–(3) and the complete-shadow disjointness argument prove the result for all \(n\ge2\).

## Relationship to prior work

Sloane's study of single-deletion-correcting codes provides the deletion-shadow framework and classical Varshamov–Tenengolts benchmark. Cullina, Kulkarni, and Kiyavash study constant-weight-induced deletion graphs and prove optimal *colorings* in the single-deletion case. Their exact chromatic number does not determine the maximum independent-set size in the weight-two graph, which is the quantity here. Kulkarni and Kiyavash also develop general non-asymptotic bounds for deletion codes, but these do not supply the present exact constant-weight-two optimum. Searches of the accessible material did not reveal the all-length formula; the absence of a search hit does not establish historical novelty, and equivalent formulations could exist in unindexed literature.

## Limitations

The result concerns only binary weight-two words and one deletion, not arbitrary weight, arbitrary alphabet, insertion/deletion combinations, or more than one deletion. It classifies the **maximum size**, not all optimal codes or their symmetry classes. Priority has been checked against cited literature and accessible records only; an unindexed equivalent remains possible. The proof has undergone self-review; no independent mathematical audit has been performed.

## References

1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197, original submission 2002-07-22. https://arxiv.org/abs/math/0207197
2. D. Cullina, A. A. Kulkarni, and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056, original submission 2012-11-16. https://arxiv.org/abs/1211.4056
3. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128, original submission 2012-11-13. https://arxiv.org/abs/1211.3128
