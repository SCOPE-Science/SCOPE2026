# Complete circular antidictionaries of distinct-letter run cycles

## Finding
Let \(q\ge3\) and let \(c_0,\ldots,c_{q-1}\) be pairwise distinct letters. For arbitrary positive integers \(a_0,\ldots,a_{q-1}\), define
\[
U=c_0^{a_0}c_1^{a_1}\cdots c_{q-1}^{a_{q-1}},\qquad X=U^\omega,\qquad p=\sum_{i=0}^{q-1}a_i.
\]
All run indices below are taken modulo \(q\). The *minimal forbidden contiguous factors* of \(X\), relative to \(\Sigma=\{c_0,\ldots,c_{q-1}\}\), are exactly the following disjoint union:
\[
\begin{aligned}
\mathcal A&=\{c_ic_j:0\le i,j<q,\ j\notin\{i,i+1\pmod q\}\},\\
\mathcal B&=\{c_i^{a_i+1}:0\le i<q\},\\
\mathcal C&=\{c_{i-1}c_i^tc_{i+1}:0\le i<q,\ 1\le t<a_i\}.
\end{aligned}
\]
In particular,
\[
\lvert\operatorname{MF}(X)\rvert=p+q(q-2)
\]
and the polynomial enumerating the minimal forbidden words by length is
\[
H_X(z)=q(q-2)z^2+\sum_{i=0}^{q-1}z^{a_i+1}+\sum_{i=0}^{q-1}\sum_{t=1}^{a_i-1}z^{t+2}.
\]
Thus the length spectrum and total number are independent of the cyclic ordering of the run lengths. For example, with run lengths \((2,1,3)\) and letters \(0,1,2\), the nine minimal forbidden words are `02`, `10`, `21`, `000`, `11`, `2222`, `201`, `120`, and `1220`.

## Assumptions and scope
A factor means a *contiguous* subword. A word \(v\in\Sigma^+\) is minimally forbidden if it does not occur in \(X\), whereas each proper contiguous factor does occur. Since the language of factors is factorial, it is equivalent to require occurrence of the proper prefix and proper suffix of \(v\). All letters of \(\Sigma\) occur. The period \(U\) is primitive because each letter occurs in a single maximal cyclic run and the \(q\ge3\) run letters are distinct. The claim concerns factors of the periodic infinite word, equivalently factors of the circular word \([U]\), and **not** the minimal absent words of the finite string \(U\) without wraparound.

## Proof
**Step 1: each displayed word is minimally absent.** A two-letter factor consisting of distinct letters is possible precisely at one of the transitions \(c_i\to c_{i+1}\), proving that the words in \(\mathcal A\) are absent and have two occurring one-letter factors. Every cyclic run of \(c_i\) has length exactly \(a_i\), so \(c_i^{a_i+1}\) is absent with occurring proper prefix and suffix, proving the assertion for \(\mathcal B\). Finally, the unique transitions \(c_{i-1}\to c_i\to c_{i+1}\) enclose a full run of length \(a_i\). Hence \(c_{i-1}c_i^tc_{i+1}\) is absent for \(1\le t<a_i\). Its length-one-shorter prefix \(c_{i-1}c_i^t\) occurs at the beginning of an \(i\)-run, and its length-one-shorter suffix \(c_i^tc_{i+1}\) occurs at the end of an \(i\)-run. This establishes minimality. The three families are disjoint: nonconstant length-two words, constant words, and words having three maximal runs, respectively.

**Step 2: avoidance forces membership in the factor language.** Suppose a nonempty word \(v\in\Sigma^+\) avoids every member of \(\mathcal A\cup\mathcal B\cup\mathcal C\). Write its maximal-run decomposition as \(d_1^{r_1}\cdots d_s^{r_s}\). Avoidance of \(\mathcal A\) forces each transition between successive, different run letters to be one of the directed cyclic transitions \(c_i\to c_{i+1}\). Avoidance of \(\mathcal B\) forces every run of symbol \(c_i\) to have length at most \(a_i\). For each internal run (with both neighboring runs present), avoidance of \(\mathcal C\) additionally forces its length to equal \(a_i\): a smaller length would exhibit the corresponding forbidden three-run factor using the immediately adjacent letters. Thus, the run labels of \(v\) follow the directed cycle, every internal run has precisely the prescribed length, and only the first and last runs may be shortened. This is exactly the structure of a contiguous segment of the periodic word \(X\): choose its initial position in the appropriate run, traverse the fully prescribed intervening runs, and stop in the final run. The same construction handles the cases of one or two maximal runs. Therefore every word avoiding the displayed list occurs in \(X\).

**Step 3: completeness and counts.** Every minimally forbidden word must contain one of the displayed words by the contrapositive of Step 2. Because the displayed words are themselves absent and minimal by Step 1, no minimally forbidden word can properly contain one of them. Hence the displayed list is the entire minimal forbidden set. There are \(q(q-2)\) forbidden distinct-letter pairs, \(q\) overlong constant-run words, and \(\sum_i(a_i-1)=p-q\) short internal-run bridge words, for a total of \(p+q(q-2)\). Counting the individual lengths proves the generating polynomial.

## Verification
The accompanying `verify_distinct_run_antidictionary.py` builds the predicted list and **independently** enumerates circular factors from three copies of the period. Every absent extension of an occurring prefix, with occurring proper suffix, is counted; the resulting set is compared exactly with the list. The checker tests all permitted length profiles with \(2\le q\le5\), each run length between one and three, and total period length at most nine, plus seeded larger profiles through period length ten. The two-letter case is tested as a boundary check, not included in the novelty claim. This computational comparison is finite and is supplementary to the general proof above.

## Relationship to prior work
Fici, Restivo and Rizzo [1] define circular minimal forbidden factors and prove general bounds and an algorithmic construction. Their Lemma 2 reduces the circular antidictionary to finite-word data and the paragraph following Lemma 3 records the \(q(q-1)\) count for a circular word where each of the \(q\) letters occurs exactly once. The formula here recovers that previously known permutation case when every \(a_i=1\), but additionally gives the exact three-family list and count for all arbitrary positive run lengths. The example \(c_0^{p-1}c_1\) and its \(p\)-element antidictionary for two letters is also explicitly reported in [1] and not claimed as new. Akagi et al. [2] provide general run-length-encoded minimal-absent-word categorization and enumeration for finite input strings, with their own terminal handling. Those general finite-string results are not the same statement as an exact symbolic antidictionary of circular distinct-letter run cycles. General-purpose algorithms can compute any fixed input, but do not by themselves state this all-parameter classification or the order-invariant spectrum.

## Limitations
The alphabet is precisely the set of run labels; adding unused letters adds length-one forbidden words. The pairwise-distinct run-letter condition matters: repeated labels can create additional return bridges and invalidate the formula. The word is periodic, not an arbitrary finite RLE string. This theorem concerns minimal forbidden **contiguous** factors, not absent scattered subsequences. Priority relative to results not indexed by the sources inspected has not been independently certified.

## References
[1] G. Fici, A. Restivo, L. Rizzo, *Minimal Forbidden Factors of Circular Words*, arXiv:1707.04450, first posted 2017-07-14, https://arxiv.org/abs/1707.04450 . In particular Section 3, Lemmas 2–3, the permutation-word example after Lemma 3, and Theorem 4.

[2] T. Akagi, K. Okabe, T. Mieno, Y. Nakashima, S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591, first posted 2022-02-28, https://arxiv.org/abs/2202.13591 . In particular Sections 1–2 and Section 5.
