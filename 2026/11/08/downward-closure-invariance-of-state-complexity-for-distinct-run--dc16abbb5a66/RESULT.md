# Downward-closure invariance of state complexity for distinct-run conjugacy languages

## Finding
Let \(q\ge 2\), let \(c_0,\ldots,c_{q-1}\) be distinct letters, let \(a_i\ge 1\) be integers, and put \(P=c_0^{a_0}\cdots c_{q-1}^{a_{q-1}}\), \(n=\sum_i a_i\). Let \(C(P)\) be all cyclic rotations of \(P\), and let \(D(P)=\downarrow C(P)\) consist of all scattered subsequences (including the empty word) of these rotations. Over the alphabet of the \(q\) listed letters, let \(\operatorname{sc}(L)\) be the number of states of the minimal **complete** DFA of \(L\). Then

\[
\boxed{\operatorname{sc}(D(P))=\operatorname{sc}(C(P))=n^2-\sum_{i=0}^{q-1}a_i^2+3=2\sum_{0\le i<j<q}a_ia_j+3.}
\]

Thus taking every scattered subsequence of all rotations does **not** increase or decrease minimal complete DFA size in this family, despite changing the accepted language and its length spectrum. The statement includes arbitrarily many distinct letters and arbitrary positive run lengths, not just a binary two-run specialization.

## Assumptions and scope
The written period contains exactly one run of each of \(q\) *pairwise distinct* letters; each \(a_i\) is strictly positive. Rotations are linear words of exactly length \(n\). Subsequence means deletion without reordering, not contiguous factor. Language states include the rejecting dead state. The symbols are indexed cyclically modulo \(q\). No claim is made for periods in which a symbol occurs in more than one cyclic run, for empty run lengths, or for arbitrary finite languages.

For a word \(T\), write \(\downarrow T\) for all its scattered subsequences. By the Myhill–Nerode theorem, the state count equals the number of distinct right quotients \(z^{-1}L=\{y:zy\in L\}\).

## Proof
**1. Right quotients of the closure.** A nonempty accepted prefix consisting only of \(c_i^p\), \(1\le p\le a_i\), has quotient

\[
Q_{i,p}=\bigcup_{t=0}^{a_i-p}\downarrow\bigl(c_i^t\,c_{i+1}^{a_{i+1}}\cdots c_{i-1}^{a_{i-1}}\,c_i^{a_i-p-t}\bigr).
\]

To see this, place the selected \(p\) symbols within the one circular run of \(c_i\). The unused positions following the selection are bounded by the displayed rotation suffix, with \(t\) unused letters of that run before the next run and the remaining \(a_i-p-t\) just before the cut. Conversely each displayed suffix is realized: start the rotation with exactly \(p+t\) letters left in the run, select its first \(p\), and retain all subsequent positions. Therefore these are exactly the possible residual subsequences.

Now take an accepted word \(z\) with at least two different symbols. It traverses the run letters in cyclic order, visiting each run at most once, except that the first run can be revisited at the very end if the cut splits it. Let \(c_i^p\) be its first maximal constant block and \(c_j^r\) its last.

If \(i\ne j\), then

\[
z^{-1}D(P)=\downarrow T_{i,p;j,r},\qquad
T_{i,p;j,r}=c_j^{a_j-r}c_{j+1}^{a_{j+1}}\cdots c_{i-1}^{a_{i-1}}c_i^{a_i-p}.
\]

The intermediate product is empty for cyclically adjacent \(j,i\). Any embedding of \(z\) into a rotation leaves at most \(a_j-r\) letters in its last run, at most \(a_i-p\) at the final cut in its initial run, and at most the whole intervening runs. Therefore its remaining suffix embeds in \(T_{i,p;j,r}\). Equality follows by cutting just before the last \(p\) letters of the initial run and using the earliest available letters in each later visited run. The full displayed suffix then remains. This argument permits skipped runs and skipped positions.

If \(i=j\), the word must have left the initial run, completed a cyclic traversal and returned to it. The two selected endpoint blocks consume \(p+r\le a_i\), and the quotient is \(\downarrow c_i^{a_i-p-r}\). It is already one of the principal quotients in the preceding display: take first run \(i\), last run \(i-1\), initial selection length \(a_i-(a_i-p-r)\) and select the whole last run. Thus all nonconstant accepted prefixes give principal quotients indexed by ordered distinct run indices with \(1\le p\le a_i\), \(1\le r\le a_j\). Every such parameter choice occurs, using the two-block subsequence \(c_i^pc_j^r\).

**2. Counting the distinct principal quotients.** Distinct words have distinct principal downsets, since the unique maximal element of \(\downarrow T\) is \(T\). Put \(s=a_j-r\), \(t=a_i-p\), each in its indicated range from zero through one less than the run length. A principal generator is the proper cyclic arc

\[
 c_j^s\,c_{j+1}^{a_{j+1}}\cdots c_{i-1}^{a_{i-1}}\,c_i^t.
\]

For cyclically adjacent \(j,i\), the possibilities with both endpoints positive give \((a_j-1)(a_i-1)\) different two-run words. The possibilities with one or both endpoints zero contribute, across all adjacent pairs, precisely the empty word and the \(a_i-1\) positive *proper* powers of each letter. For nonadjacent ordered pairs, at least one intervening complete run occurs, and all \(a_ja_i\) choices are distinct from one another and from the adjacent-pair generators. Indeed, from the word itself a first or last run of full length is identifiable as an intervening run, whereas a nonzero endpoint is strictly shorter than its ambient run; the intervening cyclic interval then fixes both omitted boundary indices. This also covers the case when only one full intervening run remains.

Consequently the number of principal quotients is

\[
1+\sum_i(a_i-1)+\sum_j(a_j-1)(a_{j+1}-1)
 +\sum_{\substack{j,i:\ i\ne j,\ i\ne j+1}}a_ja_i
=1-n+\sum_{i\ne j}a_ia_j.
\]

**3. The other quotients.** There are exactly \(n\) constant-prefix quotients \(Q_{i,p}\). For \(p<a_i\), their \(a_i-p+1\) displayed maximal words are distinct and all have length \(n-p\), hence there are at least two incomparable maxima; they cannot equal a principal quotient. For \(p=a_i\), their sole maximal word consists of all the other runs in full. No principal generator can equal it, since in a principal generator the two endpoint runs, when present, have strictly fewer symbols than the ambient run, and the path omits at least one run-boundary segment. Constant-prefix quotients are distinct from one another: their maximal words have the Parikh vector of \(P\) with precisely \(p\) occurrences of \(c_i\) removed, which uniquely determines \((i,p)\).

The initial quotient is distinct, since its maximal words have length \(n\), while all quotients after reading any nonempty accepted prefix have shorter maximal words. There is exactly one rejecting dead quotient, and every other quotient contains the empty word. Adding yields

\[
\operatorname{sc}(D(P))=1+n+\left(1-n+\sum_{i\ne j}a_ia_j\right)+1
=3+\sum_{i\ne j}a_ia_j.
\]

**4. Comparison with the original conjugacy language.** Its accepted words all have length \(n\). At a prefix depth \(d\), \(1\le d<n\), the right quotients are determined by the sets of suffixes paired with each circular length-\(d\) prefix. Because every ordered unequal adjacent-letter pair occurs at exactly one boundary of \(P\), two distinct starting positions can have the same prefix only when that prefix lies inside a single constant run. The total reductions caused by such repeated prefixes are \(\sum_i(a_i-d)_+\), where \(x_+=\max(x,0)\). Among the remaining singleton-prefix classes, identical singleton suffixes merge exactly \(\sum_i(a_i-(n-d))_+\) further classes. Prefix and suffix repetitions cannot coexist on one length-\(n\) rotation because \(q\ge2\), and no multi-suffix quotient can equal a singleton quotient. Thus the precise layer size is

\[
 h_d=n-\sum_i(a_i-d)_+-\sum_i(a_i-(n-d))_+.
\]

Depth zero and depth \(n\) each contribute one state; a complete DFA adds one dead state. Summing the displayed formula gives

\[
\operatorname{sc}(C(P))=3+n(n-1)-\sum_i a_i(a_i-1)
=3+n^2-\sum_i a_i^2,
\]

which coincides with the closure count.

## Verification
The accompanying standalone Python 3 script `verify.py` builds cyclic rotations and their scattered-subsequence languages independently, computes exact right quotients from all accepted prefixes, and checks both state counts and each structural residual formula. It exhaustively examines all positive run-length vectors with lengths up to five for two letters, up to three for three letters, and up to two for four and five letters, as well as 180 seeded additional vectors with bounded total length. In the recorded run it returned `VERIFY_OK configurations=280 residuals=61585 accepted_words=61585`. The finite check is corroboration only; the proof above establishes all allowed \(q\) and lengths.

## Relationship to prior work
Gabric, Holub and Shallit study the **maximum** state complexity of cyclic conjugate languages at prescribed total length and alphabet size, using generalized de Bruijn words. Their extremal result does not determine this particular all-distinct-run family or how downward closure changes its state complexity. Guyot (2024, Propositions 2.5–2.6) explicitly identifies the scattered-subsequence closure of the conjugates of a word with one occurrence of each distinct letter, and proves the state count \(q^2-q+3\). Thus the all-unit specialization of the closure formula above is **already known**. The contribution here is the arbitrary positive run-vector classification and the equality with the original conjugacy-language complexity, neither of which follows from the unit case. General closure bounds likewise do not imply equality for the present parameterized family. The separate binary two-run conjugacy count alone would not establish closure invariance or the multiletter formula.

## Limitations
The theorem requires one *cyclic* run per distinct symbol. It does not say that arbitrary words, arbitrary conjugacy classes, or arbitrary finite languages preserve minimal automaton size under downward closure. For example, such preservation cannot be inferred merely from global state-complexity bounds. Independent review and a complete bibliographic exclusion of equivalent formulations have not been performed.

## References
1. D. Gabrić, Š. Holub, J. Shallit, *Maximal State Complexity and Generalized de Bruijn Words*, arXiv:1903.05442, first posted 2019-03-13, https://arxiv.org/abs/1903.05442 . Conference version *Generalized de Bruijn Words and the State Complexity of Conjugate Sets*, DCFS 2019, DOI 10.1007/978-3-030-23247-4_10.
2. J. Guyot, *On the State Complexity of Square Root and Substitution for Subword-Closed Languages*, arXiv:2407.10355v1, first posted 2024-07-14, https://arxiv.org/abs/2407.10355 .
3. J. Brzozowski, G. Jirásková, C. Zou, *Quotient Complexity of Closed Languages*, arXiv:0912.1034, https://arxiv.org/abs/0912.1034 .
