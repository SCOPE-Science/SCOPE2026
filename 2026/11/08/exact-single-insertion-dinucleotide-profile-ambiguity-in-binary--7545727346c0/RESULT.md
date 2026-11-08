# Exact single-insertion dinucleotide-profile ambiguity in binary words

## Finding
For every nonempty **linear** binary word \(w=w_1\cdots w_n\), let \(P(w)=(c_{00},c_{01},c_{10},c_{11})\) count occurrences of the four adjacent pairs, with multiplicity. Insert **exactly one** symbol, either \(0\) or \(1\), in any of the \(n+1\) gaps including both ends. Let \(I(w)\) be the number of *distinct resulting profiles*, not the number of resulting words or insertion operations.

The exact pointwise law, for all \(n\ge1\), is
\[
I(w)=1+\mathbf1_{\{w_1=w_n\}}+\mathbf1_{\{0\text{ occurs in }w\}}+\mathbf1_{\{1\text{ occurs in }w\}}+\mathbf1_{\{00\text{ occurs in }w\}}+\mathbf1_{\{11\text{ occurs in }w\}}.
\]
Thus \(3\le I(w)\le6\); the six-profile maximum occurs exactly for words containing both \(00\) and \(11\) and having equal first and last symbols. It is first possible at \(n=5\), with exactly four words: `00110`, `01100`, `10011`, `11001`.

For \(n\ge2\), put \(C_j(n)=|\{w\in\{0,1\}^n:I(w)=j\}|\) and use Fibonacci numbers \(F_0=0,F_1=1,F_{k+2}=F_{k+1}+F_k\) and Lucas numbers \(L_0=2,L_1=1,L_{k+2}=L_{k+1}+L_k\). Writing \(\varepsilon_n=(-1)^n\), the **complete all-length distribution** is
\[
\begin{aligned}
C_3(n)&=1+\varepsilon_n,\\
C_4(n)&=2F_{n+2}-2L_{n-1}+1-3\varepsilon_n,\\
C_5(n)&=2^{n-1}+4L_{n-1}-2F_{n+2}-3+3\varepsilon_n,\\
C_6(n)&=2^{n-1}-2L_{n-1}+1-\varepsilon_n.
\end{aligned}
\]
At length \(n=1\), \((C_3,C_4,C_5,C_6)=(2,0,0,0)\). For uniformly random binary words of length \(n\), \(\Pr(I=5)\to\tfrac12\), \(\Pr(I=6)\to\tfrac12\) and \(\Pr(I\le4)\to0\), exponentially fast. In particular, insertion of a symbol never produces more than six observable adjacent-pair *profiles*, even though the unrestricted one-insertion word ball has \(n+2\) distinct words.

A channel comparison also holds for every \(n\ge2\): if deleting one symbol produces six distinct adjacent-pair profiles, then inserting one symbol produces six distinct adjacent-pair profiles. This is a direct structural implication, not an inference from the marginal distributions of the two channels.

## Assumptions and scope
All words are indexed, finite, nonempty and linear over exactly \(\{0,1\}\); no wraparound pair is counted. There are \(n+1\) insertion sites, two choices of inserted letter, and the resulting word has length \(n+1\). Distinct words that yield the same quadruple \(P\) count only once. All original and output profiles count overlapping adjacent occurrences with multiplicities. The deletion comparison concerns exactly one deletion from a word of length at least two, with the same linear profile definition.

## Proof
Let \(e_{ab}\) be the unit vector in coordinate \(ab\), with coordinates ordered \(00,01,10,11\). On inserting a symbol \(c\) between adjacent symbols \(a,b\), the profile change is
\[
\Delta(a,c,b)=e_{ac}+e_{cb}-e_{ab}.
\]
At the left and right boundaries, the changes are respectively \(e_{c w_1}\) and \(e_{w_n c}\). Evaluating the eight binary internal triples shows that *every* insertion-profile change belongs to exactly the following six distinct vectors:
\[
 e_{00},\quad e_{11},\quad e_{01},\quad e_{10},\quad
 e_{01}+e_{10}-e_{00},\quad e_{01}+e_{10}-e_{11}.
\]
The vector \(e_{00}\) occurs if and only if at least one zero is present: for a zero at a boundary insert zero adjacent to it, while an internal zero can be duplicated across an adjacent edge. The vector \(e_{11}\) occurs if and only if at least one one is present. The two three-coordinate vectors occur if and only if \(00\) and \(11\), respectively, occur in the word (insert the opposite bit between equal neighbors). The boundary vectors \(e_{01},e_{10}\) contribute one distinct type when the endpoints differ, and both distinct types when the endpoints agree. They cannot arise from an internal insertion, whose change is either one of the other four vectors. This proves the pointwise formula without any probabilistic assumption.

For \(n\ge2\), the two constant words have \(I=4\). Every nonconstant word contains both symbols, and hence
\[
I(w)=3+\mathbf1_{\{w_1=w_n\}}+\mathbf1_{\{00\subset w\}}+\mathbf1_{\{11\subset w\}}.
\]
The only words avoiding *both* \(00\) and \(11\) are the two alternating words: their endpoints agree exactly for odd lengths. This yields \(C_3(n)=1+(-1)^n\).

There are \(F_{n+2}\) words of length \(n\) avoiding \(00\). Among them, exactly \(L_{n-1}\) have equal endpoints: the allowed one-step transition matrix is
\[
M=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\qquad \#\{w:00\not\subset w,\ w_1=w_n\}=\operatorname{tr}(M^{n-1})=L_{n-1}.
\]
Bit complementation gives the same counts for avoidance of \(11\). The total number of words with equal endpoints is \(2^{n-1}\). Inclusion–exclusion on the two forbidden equal pairs shows
\[
C_6(n)=2^{n-1}-2L_{n-1}+1-(-1)^n.
\]
For \(I=4\), there are the two constants, the two alternating words when \(n\) is odd, and nonconstant words having unequal endpoints and exactly one of \(00,11\). Counting by whether \(00\) or \(11\) is avoided gives
\[
C_4(n)=2+2\mathbf1_{\{n\text{ odd}\}}+2\bigl(F_{n+2}-L_{n-1}-2\mathbf1_{\{n\text{ even}\}}\bigr)
=2F_{n+2}-2L_{n-1}+1-3(-1)^n.
\]
Because every word falls into exactly one of four classes and their total is \(2^n\), subtraction gives the displayed expression for \(C_5(n)\). For \(n=1\) the two constant words have two cross-boundary choices and one repeated-letter choice, yielding three profiles each. For \(n<5\), equal endpoints with both \(00\) and \(11\) is impossible; at \(n=5\), the four listed words are exactly the possibilities. Both the Fibonacci and Lucas sequences are \(O(\varphi^n)\) for \(\varphi=(1+\sqrt5)/2<2\), giving the limiting probabilities.

For the deletion implication, a one-deletion profile change must belong to the six-vector set
\[
\{-e_{00},-e_{11},-e_{01},-e_{10},e_{00}-e_{01}-e_{10},e_{11}-e_{01}-e_{10}\}.
\]
To see six distinct changes, \(-e_{00}\) and \(-e_{11}\) require \(00\) and \(11\) in the source. Changes \(-e_{01}\) and \(-e_{10}\) require the first or last adjacent pair to be of the corresponding type: an interior deletion cannot yield either change. Both cross-pair changes therefore force the first adjacent pair and last adjacent pair to be opposite \(01\) and \(10\), which entails equal first and last symbols. These are precisely the three conditions for an insertion ball of size six.

## Verification
`verify_direct.py` independently constructs every inserted output word and its literal pair-frequency vector for each of the \(2^n\) binary source words, for all \(1\le n\le16\). It compares each word with the pointwise formula, groups all words to check every coefficient of the four class-count expressions, and independently checks the four length-five maximizers. The run passed.

`verify_structural.py` independently computes the no-\(00\) endpoint trace by multiplying integer \(2\times2\) matrices, compares it with direct enumeration through length sixteen, and independently enumerates deletion and insertion profile balls through length twelve to test the saturation implication. The run passed. These finite enumerations corroborate the analytic all-length proof; they are not used as infinite certificates.

Representative class distributions \((C_3,C_4,C_5,C_6)\) for \(n=4,5,6,9\) are respectively \((2,6,8,0)\), \((0,16,12,4)\), \((2,18,34,10)\), and \((0,88,260,164)\).

## Relationship to prior work
Kiah, Puleo and Milenkovic's 2014 DNA-storage-channel paper, and its 2015 full sequence-profile treatment, motivate retaining adjacent-substring multiplicities rather than strings themselves, and study global profile counts and error-correcting constructions. The exact number of profiles reachable from **each fixed binary word by a single symbol insertion**, its four-class distribution, and the deletion-to-insertion saturation implication are not supplied by the inspected parts of those papers.

Jacquet, Knessl and Szpankowski count complete classes of Markov types and, in the binary special case, cyclically balanced transition-count matrices. Such global/cyclic enumeration neither counts the local insertion neighborhood of a **fixed linear word** nor implies the boundary-sensitive factors here. A published 2026 result entitled *Exact binary two-multispectrum code size and singleton classification* determines the total distinct profiles and reconstructible words at each length, but does not determine insertion-profile ball sizes. The distinction is between a global image of all source words and the local image of the one-symbol insertion channel around a fixed source.

The previously studied one-deletion dinucleotide-profile ball is the reverse edit operation and has a different all-length distribution and a later six-profile saturation threshold. The present derivation uses independent insertion-specific transformations, not an automatic substitution or reindexing of deletion counts.

## Limitations
Only binary, linear, read-length-two multiplicity profiles and exactly one inserted symbol are covered. The formulas do not determine profiles after multiple edits, nonbinary alphabets, circular words, loss of pair multiplicities, or the number of *inserted words* (as distinct from profiles). The proof does not claim any error-correcting-code size improvement. A historically unindexed equivalent calculation could exist despite the targeted comparisons; independent historical review remains open.

## References
1. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Storage Channels*, arXiv:1410.8837v1, first publicly posted 2014-10-31. https://arxiv.org/abs/1410.8837
2. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517v1, first publicly posted 2015-02-02. https://arxiv.org/abs/1502.00517
3. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, DMTCS Proceedings AM (2010), DOI:10.46298/dmtcs.2768. https://dmtcs.episciences.org/articles/2768
4. *Exact binary two-multispectrum code size and singleton classification*, published research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71
