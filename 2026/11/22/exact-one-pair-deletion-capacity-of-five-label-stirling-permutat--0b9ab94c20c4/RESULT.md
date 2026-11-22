# Exact one-pair-deletion capacity of five-label Stirling permutations

## Finding

Let \(\mathcal Q_5\) be the set of Stirling permutations of the multiset with two copies of each label \(1,2,3,4,5\): between the two occurrences of a label, every entry is larger than that label. For \(w\in\mathcal Q_5\), let \(\Delta(w)\subseteq\mathcal Q_4\) contain the distinct outputs obtained by deleting **both** occurrences of any one label and order-standardizing the remaining four labels. Then the largest family \(\mathcal C\subseteq\mathcal Q_5\) for which \(\Delta(u)\cap\Delta(v)=\varnothing\) whenever \(u\ne v\) is

\[
\boxed{\max |\mathcal C|=33.}
\]

In particular, among the \(945\) possible sources, 33 can be transmitted with certain recovery after one unknown *whole-label-pair* deletion; 34 cannot. This is an exact finite result. The receiver observes one standardized eight-entry Stirling permutation, not the complete deletion deck and not the deleted label.

## Assumptions and scope

A Stirling permutation of order \(r\) is a word containing each label in \(\{1,\dots,r\}\) twice, with only larger labels between matching occurrences. Define
\[
D_k(w)=(w_i-\mathbf1_{w_i>k}:w_i\ne k),\qquad
\Delta(w)=\{D_k(w):1\le k\le5\}.
\]
For every \(k\), \(D_k(w)\in\mathcal Q_4\). Repeated images are collapsed to a set. The channel always deletes the two occurrences of **the same** label, not arbitrary two coordinates. The positions and identity of the deleted label are not transmitted. A code is zero-error if all its single-output descendant sets are pairwise disjoint.

Under the standard depth-first contour-word bijection with plane recursive increasing trees, the operation corresponds to contracting an unknown nonroot labeled edge, preserving ordered-child order, and then standardizing the remaining nonroot labels. Thus the theorem also provides a finite capacity for this natural tree information-loss operation.

## Proof

The insertion rule starts with \(\mathcal Q_1=\{11\}\). Every word in \(\mathcal Q_r\) is obtained **uniquely** by inserting adjacent \(rr\) into one of the \(2r-1\) gaps of a word in \(\mathcal Q_{r-1}\), because no smaller symbol can separate the two copies of the maximum label. Consequently \(|\mathcal Q_4|=1\cdot3\cdot5\cdot7=105\) and \(|\mathcal Q_5|=945\).

Order \(\mathcal Q_4\) and \(\mathcal Q_5\) lexicographically (as integer tuples). The attached `certificate.json` gives two exact finite mathematical witnesses:

1. `lower_code_lex_indices`: 33 distinct, zero-based indices in the lexicographic \(\mathcal Q_5\) listing. For these 33 words, the 33 sets \(\Delta(w)\) are pairwise disjoint. This gives \(\max|\mathcal C|\ge33\).
2. `upper_weights_for_order4_lex_targets`: 105 nonnegative **integers** \(y_v\), one for each lexicographic \(v\in\mathcal Q_4\), with scale \(10{,}000\). The fully checked inequalities are
\[
\sum_{v\in\Delta(w)}y_v\ge10{,}000\quad\text{for each of the 945 words }w\in\mathcal Q_5,
\qquad\sum_{v\in\mathcal Q_4}y_v=339{,}636.
\]

For any zero-error code, its descendant sets are disjoint, so
\[
10{,}000|\mathcal C|\le\sum_{w\in\mathcal C}\sum_{v\in\Delta(w)}y_v
\le\sum_{v\in\mathcal Q_4}y_v=339{,}636<340{,}000.
\]
Since code size is integral, \(|\mathcal C|\le33\). Combined with the 33-word witness this proves the theorem. This argument uses exact integer arithmetic and does not depend on an optimizer's assertion of optimality.

## Verification

`verify.py` reads the complete `certificate.json` at its own directory. Run from that directory with `python3 verify.py`, using only Python's standard library. It independently forms the five-label source family (i) by inserting each new largest doubled label in all gaps and (ii) by enumerating every balanced length-ten word and testing the nesting condition. It verifies agreement of these constructions and the 105 possible outputs. It then constructs all 945 descendant sets, verifies all 33 witness decks are disjoint, verifies the nonnegative integer weights and their sum, and checks all 945 covering inequalities exactly.

Successful replay prints `VERIFY_OK`. The observed descendant-deck cardinalities across the 945 sources are \(3,46,248,404,244\) for deck sizes \(1,2,3,4,5\), respectively, providing an additional independent consistency check.

## Relationship to prior work

Stirling permutations, their insertion enumeration and the plane recursive-tree correspondence were established previously by Janson (2008) and Janson–Kuba–Panholzer (2008). Gabrys et al. (2014) treat deletion codes for **ordinary** permutations under rank-standardized one-symbol deletion. Sala–Gabrys–Dolecek (2014) treat synchronization errors in multipermutations generally, with an abstract discussing one-deletion sphere sizes and code constructions; their full text could not be accessed, so possible equivalent coverage there remains an explicit priority risk, not an asserted exclusion. Brualdi–Dahl (2024), whose full open-access text was inspected, analyze Stirling multipermutations, inversion order and deleting the **largest** matching pair, rather than exact zero-error code capacity after deletion of an **unknown** matching pair. The present channel restricts sources to nested-pair Stirling words and erases any whole matched label pair, giving the exact 33-word optimum and its finite packing certificate. None of the inspected full-text sources implies this exact optimum; general abstract-level multipermutation coverage cannot be decisively excluded.

## Limitations

This is a result only for order five and exact one-whole-pair erasure. No formula for arbitrary order, arbitrary two-position deletion, unknown number of erased labels, or noisy outputs is asserted. The upper certificate is a finite table rather than a simple closed-form family. Exhaustive program replay checks a mathematically specified finite certificate; it is not an external or independent mathematical audit. Historical novelty may be limited by unindexed work on tree contractions or repeated-label deletion codes, especially the inaccessible full text of Sala–Gabrys–Dolecek (2014).

## References

- Svante Janson, *Plane recursive trees, Stirling permutations and an urn model*, arXiv:0803.1129, publicly posted 2008-03-07. https://arxiv.org/abs/0803.1129
- Svante Janson, Markus Kuba and Alois Panholzer, *Generalized Stirling permutations, families of increasing trees and urn models*, arXiv:0805.4084, publicly posted 2008-05-27. https://arxiv.org/abs/0805.4084
- Ryan Gabrys, Eitan Yaakobi, Farzad Farnoud, Frederic Sala, Jehoshua Bruck and Lara Dolecek, *Single-Deletion-Correcting Codes over Permutations*, ISIT 2014, DOI:10.1109/ISIT.2014.6875337. https://yaakobi.net.technion.ac.il/files/2015/04/40_Single_Deletion_Permutations_ISIT14.pdf
- Frederic Sala, Ryan Gabrys and Lara Dolecek, *Deletions in Multipermutations*, ISIT 2014, DOI:10.1109/ISIT.2014.6875338. Abstract and bibliographic information accessible; full text not accessible. https://doi.org/10.1109/ISIT.2014.6875338
- Richard A. Brualdi and Geir Dahl, *Multipermutations and Stirling Multipermutations*, Graphs and Combinatorics 40, 22 (2024), open-access full text. https://doi.org/10.1007/s00373-024-02751-2
