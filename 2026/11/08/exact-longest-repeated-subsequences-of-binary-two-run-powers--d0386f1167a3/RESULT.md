# Exact longest repeated subsequences of binary two-run powers

## Finding
For arbitrary positive integers \(a,b,k\) and any integer \(e\ge 2\), consider the finite word \(W=(0^a1^b)^k\). Let \(\Lambda_e(W)\) be the largest length of a scattered subsequence of \(W\) that is an exact \(e\)-th power \(U^e\), where \(U\) is a nonempty word. Set \(t=\lfloor k/e\rfloor\). With value zero when no such subsequence exists,
\[
\boxed{\Lambda_e(W)=e\max\!\left\{t(a+b),\left\lfloor\frac{ka}{e}\right\rfloor,\left\lfloor\frac{kb}{e}\right\rfloor\right\}.}
\]
More precisely, when \(k\ge e\), the largest length among such powers with \(U\) containing **both** symbols is exactly \(et(a+b)\). When \(k<e\), no repeated subsequence with a two-symbol root exists. Thus the only possible improvement on the \(e\)-fold repeated-period witness is a unary root. If \(k=et+r\), \(0\le r<e\), the all-zero witness strictly beats the mixed-root optimum exactly when \(\lfloor ra/e\rfloor>tb\), with the symmetric condition \(\lfloor rb/e\rfloor>ta\) for the all-one witness.

## Assumptions and scope
A scattered subsequence of a finite word is obtained by choosing strictly increasing indices, without requiring consecutiveness. An exact \(e\)-th power means a word of the form \(U^e\) with \(U\ne\varepsilon\), *without* requiring that \(U\) be primitive; the stated exponent is the number of displayed copies, not necessarily the maximal exponent of the resulting word. All integer parameters are quantified as in the Finding; there are no asymptotic restrictions. If every nonempty repeated pattern is absent, the optimum is defined to be \(0\). This is a statement about one fixed finite input beginning with a zero-run, not about existence in a freely shifted cyclic window.

## Proof
We prove the run-capacity obstruction first. For a nonempty mixed binary word \(U\), write its *cyclic* maximal zero-run lengths as \(x_1,\ldots,x_p\), and its cyclic maximal one-run lengths as \(y_1,\ldots,y_p\). A run across the cyclic boundary joins the final and initial runs of the same symbol. As \(U\) contains both symbols, the cyclic runs of either symbol are unambiguously defined and alternate, with \(p\ge1\). Put
\[
C_0=\sum_{i=1}^{p}\left\lceil\frac{x_i}{a}\right\rceil,
\qquad C_1=\sum_{i=1}^{p}\left\lceil\frac{y_i}{b}\right\rceil.
\]
Claim: if \(U^e\) is a subsequence of \(W\), then \(k\ge eC_0\) and \(k\ge eC_1\).

Indeed, each maximal zero-block of length \(h\) in \(U^e\) must occupy at least \(\lceil h/a\rceil\) distinct zero-runs of \(W\). Two different maximal zero-blocks of \(U^e\) have a selected one between them, so they cannot use the same source zero-run. Therefore \(k\) is at least the sum of these ceiling costs. If \(U\) begins and ends in different symbols, its zero-blocks occur in \(e\) unchanged copies and their total cost is exactly \(eC_0\). If \(U\) begins and ends in zero, let \(x\) and \(y\) be its initial and terminal zero-run lengths. In \(U^e\) these boundary portions form two end runs of lengths \(x\) and \(y\), and \(e-1\) interior runs each of length \(x+y\); every other zero-run occurs \(e\) times. The boundary costs sum to
\[
\left\lceil\frac{x}{a}\right\rceil+(e-1)\left\lceil\frac{x+y}{a}\right\rceil+
\left\lceil\frac{y}{a}\right\rceil
\ \ge\ e\left\lceil\frac{x+y}{a}\right\rceil,
\]
by subadditivity of ceilings. If \(U\) begins and ends in one, there is no zero-block merger, so the unchanged-copy argument applies. In all cases \(k\ge eC_0\). Interchanging zero and one, and \(a\) and \(b\), proves \(k\ge eC_1\).

It follows that \(C_0,C_1\le\lfloor k/e\rfloor=t\). Since each cyclic run length is at most its capacity times its ceiling,
\[
|U|=\sum_i x_i+\sum_i y_i\le aC_0+bC_1\le t(a+b).
\]
Consequently every mixed-root \(e\)-power subsequence has length at most \(et(a+b)\). If \(t=0\), the inequalities \(C_0,C_1\ge1\) show that no such mixed-root subsequence exists. Otherwise, \(U=(0^a1^b)^t\) realizes equality: its \(e\) copies occupy the first \(et\le k\) full periods of \(W\).

A unary root is either \(0^m\) or \(1^m\). The source contains exactly \(ka\) zeros and \(kb\) ones, so its longest unary-root power has length
\[
e\max\!\left\{\left\lfloor\frac{ka}{e}\right\rfloor,
\left\lfloor\frac{kb}{e}\right\rfloor\right\},
\]
attained by selecting exactly that many occurrences of the selected symbol. These two root types exhaust the binary alphabet and yield the displayed formula. Finally \(\lfloor ka/e\rfloor=ta+\lfloor ra/e\rfloor\), so comparing it to \(t(a+b)\) proves the claimed exact takeover condition, and similarly for ones. This completes the proof for all parameters.

## Verification
The standalone Python 3 verifier `verify.py` computes longest exact \(e\)-power subsequences by exhaustive enumeration of root patterns and greedy subsequence membership on small instances, compares these to the formula, checks the cyclic ceiling obstruction for all enumerated mixed roots, and independently computes square-subsequence maxima by evaluating the longest common subsequence across every input partition. Execute `python3 verify.py` in a directory containing this file. The successful verification output records 213 exhaustive parameter configurations, 28,642 cyclic-cost root probes and 78 independent partition-based square cases (including seven larger cases). These are finite corroborations; the proof above establishes the universally quantified theorem.

As a phase-transition example, with \((a,b,k,e)=(10,1,3,2)\), the mixed-root maximum is \(22\), but a repeated unary root yields length \(30\); for \((a,b,k,e)=(1,1,3,2)\), the mixed-root maximum \(4\) is globally optimal. If \(k<e\) and both \(ka<e\) and \(kb<e\), no nonempty \(e\)-power subsequence exists.

## Relationship to prior work
Bannai, I, and Köppl (arXiv:2202.07189, first posted 2022-02-15) study the general longest periodic and subperiodic subsequence algorithms. The inspected full text, including §§2–5 and the factorization recurrences, treats general inputs and exponent classes rather than binary two-run powers or this run-capacity formula. Inoue, Inenaga, and Bannai (arXiv:2006.00216, first posted 2020-05-30) give general longest-square-subsequence algorithms, not the explicit all-exponent family. Inoue and coauthors (CPM 2018, DOI 10.4230/LIPIcs.CPM.2018.15, publication date 2018-05-18) study common square subsequences of two inputs; inspected abstract, setup, and algorithm material do not assert the present one-input classification. The present proof uses a cyclic ceiling-cost inequality to resolve the entire family with a closed form.

Related exact results for distinct-letter permutation powers and general window embedding are mathematically different: a permutation-power source forbids nontrivial within-run repetition, whereas the all-window embedding spectrum allows a freely chosen starting phase. Neither supplies the mixed-versus-unary all-exponent maximum for the fixed finite source merely by identifying a matching title or exponent. The general embedding machinery remains a plausible route to an alternative derivation, and that possible overlap is acknowledged rather than treated as a uniqueness guarantee.

## Limitations
The expression describes optimum **length**, not the number of optimal roots or embeddings. It makes no claim for arbitrary binary run profiles, more than two alphabet symbols, noninteger exponents, or primitive-only roots. The closed form is computable with a constant number of integer arithmetic operations; no unit-cost claim is made for arbitrarily large integer bit lengths. The surveyed and indexed literature cannot exclude all unindexed equivalent specializations; no independent audit or publication priority is asserted.

## References
- H. Bannai, T. I, D. Köppl, *Longest (Sub-)Periodic Subsequence*, arXiv:2202.07189, initial version 2022-02-15. https://arxiv.org/html/2202.07189v1
- T. Inoue, S. Inenaga, H. Bannai, *Longest Square Subsequence Problem Revisited*, arXiv:2006.00216, first posted 2020-05-30. https://arxiv.org/abs/2006.00216
- T. Inoue, S. Inenaga, H. Hyyrö, H. Bannai, M. Takeda, *Computing Longest Common Square Subsequences*, CPM 2018, DOI 10.4230/LIPIcs.CPM.2018.15, published 2018-05-18. https://doi.org/10.4230/LIPIcs.CPM.2018.15
