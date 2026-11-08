# Complete longest-run-subsequence classification for weighted permutation powers

## Finding
Let \(q\ge 2\), let \(c_0,\ldots,c_{q-1}\) be pairwise distinct letters, let all \(a_i\) be positive integers, and let \(k\ge 1\) be an integer. Write
\[
U=c_0^{a_0}c_1^{a_1}\cdots c_{q-1}^{a_{q-1}},\qquad W=U^k,\qquad P=\sum_{i=0}^{q-1}a_i,
\]
\[
M=\max_{0\le i<q}a_i,\qquad H=\{i:a_i=M\},\qquad r=|H|.
\]
A *run subsequence* is a scattered subsequence in which every letter occurs in at most one maximal constant-letter run. We count distinct subsequence *strings*, not distinct choices of positions realizing a string.

**Theorem.** The maximum possible length of a run subsequence of \(W\) is
\[
\operatorname{LRS}(W)=P+(k-1)M.
\]
Moreover, **every** longest run-subsequence string, with no exceptions, is of the form
\[
T_{\mathbf t}=c_0^{a_0(1+t_0)}c_1^{a_1(1+t_1)}\cdots c_{q-1}^{a_{q-1}(1+t_{q-1})},
\]
where \(t_i\) are nonnegative integers satisfying
\[
\sum_{i=0}^{q-1}t_i=k-1,\qquad t_i=0\quad\text{whenever }a_i<M.
\]
Consequently the number of distinct longest run-subsequence strings is exactly
\[
\boxed{\binom{k+r-2}{r-1}}.
\]
In particular the longest string is unique if and only if \(k=1\) or the longest run of \(U\) has a unique symbol. These results use the same definition of longest run subsequence as Schrinner et al. (2020).

## Assumptions and scope
Letters are distinct within the one-period template, whereas their multiplicities \(a_i\) can be arbitrary strictly positive integers. All parameters \(q,k,a_i\) are unbounded subject to their stated integer ranges. The word \(W\) is a **linear finite** power, not a cyclically rotated power or an infinite word. The formula counts distinct output labels, not multiple embeddings. A longest run subsequence may combine physical runs from several copies of \(U\), with all intervening other letters deleted.

## Proof
We prove a period-span inequality and characterize equality.

Take any nonempty run subsequence \(T\) and fix any embedding into \(W\). Its sequence of maximal runs has the form
\[
T=c_{i_1}^{h_1}c_{i_2}^{h_2}\cdots c_{i_m}^{h_m},\qquad h_j\ge1,
\]
where the indices \(i_1,\ldots,i_m\) are pairwise distinct and lie in \(\{0,\ldots,q-1\}\). For the \(j\)-th selected letter let \(s_j\) and \(e_j\) be the first and last indices of copies of \(U\) containing its selected occurrences, and put \(v_j=e_j-s_j+1\). The copies are indexed by \(1,\ldots,k\). As the letter \(c_{i_j}\) occurs exactly \(a_{i_j}\) times in each copy,
\[
h_j\le a_{i_j}v_j.\tag{1}
\]

If \(i_j<i_{j+1}\), two consecutive selected letter-runs can use the same copy of \(U\), but they cannot cross in copy number: \(s_{j+1}\ge e_j\). If \(i_j>i_{j+1}\), their source order requires a new copy: \(s_{j+1}\ge e_j+1\). Let \(d\) be the number of these strict index descents. By chaining the inequalities,
\[
e_m\ge s_1+\sum_{j=1}^m(v_j-1)+d.
\]
The boundary conditions \(s_1\ge1\) and \(e_m\le k\) therefore give the *period-span inequality*
\[
\sum_{j=1}^m(v_j-1)+d\le k-1.\tag{2}
\]
Writing \(P=\sum_i a_i\), equations (1) and (2) yield
\[
|T|\le\sum_{j=1}^m a_{i_j}v_j
\le\sum_{j=1}^m a_{i_j}+M\sum_{j=1}^m(v_j-1)
\le P+M(k-1-d)\le P+M(k-1).\tag{3}
\]
For the converse, select any \(i\in H\), then choose a full occurrence of every letter in its natural template order, while choosing the \(c_i\)-runs from all \(k\) copies rather than just one. This gives length \(P+(k-1)M\). More generally, distribute the \(k-1\) extra period spans among the indices in \(H\) and take full runs in the corresponding consecutive periods. Because indices increase from \(0\) to \(q-1\), the last selected run of one letter and first selected run of the next can share a source period; this produces each displayed \(T_{\mathbf t}\).

Now suppose \(T\) attains equality in (3). All the \(a_i\) are positive, so equality of \(\sum_j a_{i_j}\le P\) forces \(m=q\) and use of every letter. Equality in the last inequality forces \(d=0\), hence the entire run order is \(c_0,\ldots,c_{q-1}\). Equality in the weighted middle inequality forces \(v_j=1\) whenever \(a_{i_j}<M\). Equality in (1) requires \(h_j=a_{i_j}v_j\), i.e. all physical runs in that period span are included. Finally, equality in (2) gives \(\sum_j(v_j-1)=k-1\). Thus \(t_i=v_i-1\) have precisely the stated properties, and there are no other optimal output strings.

The number of such vectors \(\mathbf t\) equals the number of weak compositions of \(k-1\) into \(r\) parts, namely \(\binom{k+r-2}{r-1}\). Different vectors yield different output strings, since the positive exponent of each distinct letter uniquely recovers its corresponding \(t_i\). This completes the proof, including \(k=1\). \(\square\)

## Verification
The standalone standard-library Python program `verify.py` performs two independent finite checks. First, a dynamic program over used-letter subsets and last output symbol computes the actual optimal subsequence length directly from expanded words; this was compared against the formula in 1,440 parameter configurations, with \(2\le q\le5\), \(1\le a_i\le3\), and \(1\le k\le4\). Second, an independent enumeration of all possible ordered subsets of distinct letters and positive output run lengths constructs *all* feasible optimal output strings; these were compared as sets with the classified family in 84 additional configurations, with \(2\le q\le4\), \(1\le a_i\le2\), and \(1\le k\le3\). The program also checked 3,986 constructive embeddings.

Run with `python3 verify.py`, expecting `VERIFY_OK`. These experiments test boundary cases and detect implementation errors; they are not a substitute for the preceding proof for arbitrary parameters.

## Relationship to prior work
Schrinner et al. (2020) introduced the general longest run subsequence problem in computational genomics, proved its NP-hardness, and gave exact general-purpose optimization algorithms and reduction rules. Dondi and Sikora (2020 preprint, 2021 conference) established additional parameterized and approximation-hardness results. Asahiro et al. (2023, 2025) studied approximation algorithms and the complementary deletion problem. These algorithms apply to the present inputs and could compute individual answers; the specific uniform optimization and complete distinct-optimum classification for arbitrary positive weighted permutation powers is not stated in the inspected material. General algorithms alone do not yield the closed forms without the period-span equality analysis.

The key difference from ordinary longest common subsequence and ordinary longest repeated subsequence problems is the requirement that **each letter occupy at most one run** in the selected output. The result characterizes the entire optimal language, not merely one witness or its length.

## Limitations
The result assumes that all distinct letters occur in a fixed order exactly once per period. No claim is made for templates with repeated separated appearances of a letter, for nonidentical periods, for cyclic rotations with an independently chosen starting phase, or for counting positional embeddings. The classification does not resolve the general NP-hard problem. An unindexed earlier equivalent classification remains possible; novelty assessment is based on the identified and inspected literature rather than a proof of bibliographic uniqueness.

## References
- S. Schrinner, M. Goel, M. Wulfert, P. Spohr, K. Schneeberger, G. W. Klau, *The Longest Run Subsequence Problem*, WABI 2020, DOI: 10.4230/LIPIcs.WABI.2020.6 (public 2020-08-25).
- R. Dondi, F. Sikora, *The Longest Run Subsequence Problem: Further Complexity Results*, arXiv:2011.08119, first posted 2020-11-16, CPM 2021, DOI: 10.4230/LIPIcs.CPM.2021.14.
- Y. Asahiro et al., *Approximation Algorithms for the Longest Run Subsequence Problem*, CPM 2023, DOI: 10.4230/LIPIcs.CPM.2023.2.
- Y. Asahiro et al., *Approximability of Longest Run Subsequence and Complementary Minimization Problems*, WABI 2025, DOI: 10.4230/LIPIcs.WABI.2025.3.
