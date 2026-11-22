# Pair-erasure collision rigidity in Stirling-permutation words

## Finding
Let \(\mathcal Q_n\) be the Stirling permutations of order \(n\), namely indexed words using each of \(1,\ldots,n\) twice, with every symbol between the two occurrences of \(a\) greater than \(a\). Delete both copies of a chosen symbol \(i\) and reduce all larger symbols by one; denote the resulting word by \(\Delta_i(w)\). Let \(L(w)=|\{\Delta_i(w):1\le i\le n\}|\).

**Theorem.** For \(1\le i<j\le n\), equality \(\Delta_i(w)=\Delta_j(w)\) holds precisely in one of the following mutually exclusive arrangements of the labels \(i,\ldots,j\):

* **Nested:** they form a factor \(i(i+1)\cdots j\,V\,j\cdots(i+1)i\), where \(V\) is a possibly empty Stirling subword on labels greater than \(j\).
* **Increasing siblings:** they form the contiguous factor \(ii(i+1)(i+1)\cdots jj\).
* **Decreasing siblings:** they form the contiguous factor \(jj(j-1)(j-1)\cdots ii\).

The nested case permits later-label descendants inside \(V\); outside the displayed factor the word is unrestricted subject to being in \(\mathcal Q_n\). The equivalence classes of \(i\mapsto\Delta_i(w)\) are therefore intervals of consecutive integers. In particular,
\[
L(w)=n-\sum_{i=1}^{n-1}\mathbf 1\{\Delta_i(w)=\Delta_{i+1}(w)\}.
\]

Write \((2a-1)!!=1\cdot3\cdots(2a-1)\), and interpret empty products as one. For every \(1\le i<j\le n\), the exact number of Stirling words satisfying this collision is
\[
C_n(i,j)=(2i-1)!!\left[\prod_{t=j}^{n-1}(2t+1-2(j-i))+2\prod_{t=j}^{n-1}(2t-2(j-i))\right].
\]
For uniformly random \(W_n\in\mathcal Q_n\) and \(n\ge2\),
\[
\boxed{\mathbb E L(W_n)=n-\frac23-\frac{n-1}{2n-1}=n-\frac76+O(n^{-1}).}
\]
The smallest possible distinct-output count is one and occurs in exactly three sources for every \(n\ge2\): \(11\,22\cdots nn\), \(nn\cdots22\,11\), and \(12\cdots nn\cdots21\). The symbols in these displayed forms denote integer labels, not a fixed single-digit string encoding.

## Assumptions and scope
The alphabet consists of ordered labels \(1,\ldots,n\), each occurring **twice**. The channel erases the **entire pair of copies of one selected label**, not two arbitrary positions. The receiver observes only the remaining word after order-standardization; two choices of removed labels are identified when these words coincide. The result is about source-dependent deletion ambiguity, not a claim of optimal error-correcting-code capacity. All words have indexed positions. There is no quotient by cyclic rotation or relabeling of the original source.

## Proof
Every Stirling permutation of order \(s+1\) is uniquely obtained by inserting the consecutive pair \((s+1)(s+1)\) into one of the \(2s+1\) gaps of an order-\(s\) Stirling permutation. Let \(w_{\le s}\) be the subword on labels at most \(s\). The pair of occurrences of any label determines a plane rooted ordered subtree interval; these intervals are disjoint or nested.

**Two-erasure cancellation lemma.** For fixed \(i<j\), the equality \(\Delta_i(w)=\Delta_j(w)\) has exactly the three forms stated in the theorem. To see the necessity at the stage when label \(j\) is born, restrict the equal descendants to labels at most \(j-1\). This gives \(\Delta_i(w_{\le j})=w_{\le j-1}\). At \(j=i+1\), the two copies of \(i+1\), inserted into \(ii\), can give the same remaining word as erasing the new maximum only when placed before, between, or after the two copies of \(i\); these are the three stated configurations. Induct on \(j-i\). Erase the maximal pair in the displayed equality to obtain \(\Delta_i(w_{\le j-1})=w_{\le j-2}\). By induction there is a nested chain or an increasing/decreasing row of consecutive doubled siblings through \(j-1\). Compare the positions of the *new maximal adjacent pair* in the two equal descendants: for a nested chain the only compatible gap for \(jj\) is inside \((j-1)(j-1)\); for increasing siblings it is immediately after that pair; and for decreasing siblings it is immediately before that pair. In all other gaps, erasing \(i\) and erasing \(j\) locate the maximal remaining pair in different gaps of the common lower-label word. This proves the three possibilities at stage \(j\), including their sufficiency.

For insertion of a later pair \((t+1)(t+1)\), delete that maximal pair from the two proposed descendants. If equality has already failed at order \(t\), it cannot be restored. If equality holds, insertion preserves it exactly when the chosen gap maps to the same gap after erasing \(i\) and after erasing \(j\). In a nested chain of \(r=j-i+1\) labels there are precisely \(2(r-1)\) incompatible gaps: the two adjacent boundaries for each parent–single-child link. In a row of \(r\) consecutive doubled leaf siblings there are precisely \(2r-1\) incompatible gaps: the \(r\) interior gaps of the doubled pairs and the \(r-1\) gaps between them. No other insertion gap breaks the collision. Thus the three forms remain necessary and sufficient at every \(n\ge j\).

At stage \(j\), each order-\(i\) Stirling permutation has exactly **one** extension of each of the three types. There are \((2i-1)!!\) such base words. At every later stage \(t\) the nested type has \(2t+1-2(j-i)\) preserving gaps and each sibling type has \(2t-2(j-i)\) preserving gaps. Multiplication proves the displayed formula for \(C_n(i,j)\). The incompatible gaps for the extreme pair \(i,j\) contain those for every adjacent pair in their interval; hence equal extreme descendants imply equality for every intermediate erasure. This proves interval convexity and the formula for \(L\). Applying the three-form classification to \(i=1,j=n\) gives exactly the three sources having \(L=1\).

For the expectation, distinguish a **nested** adjacent-label collision from a **sibling** adjacent-label collision. At the birth of label \(i+1\), the former is created at one of \(2i+1\) gaps and the latter at two. At growth from order \(t\) to \(t+1\), each existing nested adjacent collision has exactly two destructive gaps; hence its probability of surviving from birth to order \(n\) is \((2i+1)/(2n-1)\). Each existing sibling adjacent collision has exactly three destructive gaps. If \(N_n\), \(S_n\) are the numbers of nested and sibling adjacent collisions in uniform \(\mathcal Q_n\), then linearity gives \(\mathbb E N_n=(n-1)/(2n-1)\) and \(\mathbb E S_n=\frac{2n-4}{2n-1}\mathbb E S_{n-1}+\frac2{2n-1}\), with \(\mathbb E S_2=2/3\). Thus \(\mathbb E S_n=2/3\). Substitution into \(L=n-N_n-S_n\) gives the expectation.

## Verification
Execute `python3 verify.py` in the directory containing this file and `verify.py`. The checker generates all Stirling permutations through order seven by inserting each new maximum as a consecutive pair; independently forms every standardized deletion output; compares every pair with the three-factor criterion; checks every count \(C_n(i,j)\), interval equivalence, the claimed expectation, and the three singleton-deck sources. It verified \(135135\) sources at order seven and \(2837835\) pairwise comparisons at that order, printing `VERIFY_OK`. The verification is finite corroboration of, not a substitute for, the inductive proof.

## Relationship to prior work
Gessel and Stanley introduced Stirling permutations, while Bóna's arXiv preprint of 23 August 2007 (arXiv:0708.3223) and Janson's preprint of 7 March 2008 (arXiv:0803.1129) study their insertion constructions, plateaux and increasing-tree representations. Those papers supply the classical object and insertion scheme, not the present order-standardized complete-label erasure collision law. Related research on standardized permutation deletion and distinct-subsequence balls concerns different sources or different deletion channels; no implication yielding the three-form rigidity and exact pairwise counts was found in the sources checked. Absence from searches does not prove historical uniqueness.

## Limitations
The channel removes both copies of exactly one label, not arbitrary two symbols. No statement is made about partial-label deletion, unrestricted multiset permutations, minimum-distance code capacity, or higher multiplicity Stirling words. The self-review has not been independently audited. An older unindexed equivalent result remains a priority risk.

## References
1. M. Bóna, *Real Zeros and Normal Distribution for Statistics on Stirling Permutations Defined by Gessel and Stanley*, arXiv:0708.3223, first submitted 23 August 2007. https://arxiv.org/abs/0708.3223
2. S. Janson, *Plane Recursive Trees, Stirling Permutations and an Urn Model*, arXiv:0803.1129, 7 March 2008. https://arxiv.org/abs/0803.1129
3. S. Janson, M. Kuba and A. Panholzer, *Generalized Stirling Permutations, Families of Increasing Trees and Urn Models*, arXiv:0805.4084, 27 May 2008. https://arxiv.org/abs/0805.4084
