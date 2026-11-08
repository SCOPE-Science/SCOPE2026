# Exact closed-factor complexity of circular distinct-run periodic words

## Finding

For a word \(X\), let \(C_X(n)\) denote the number of **distinct closed factors** of length \(n\). A word of length one is closed; a longer word is closed when it has a nonempty proper border occurring exactly twice, as prefix and suffix (equivalently its longest border has exactly those two occurrences).

For the cyclic distinct-run word below, put \(p=\sum_i a_i\), and write \([P]\) for the indicator of a condition \(P\). Then, for every integer \(n\ge1\),

\[
C_X(n)=\begin{cases}
\displaystyle \sum_i[a_i\ge n]+\sum_i[2\le n-p+a_i\le a_i,\quad n-p+a_i\equiv0\pmod 2],&1\le n\le p,\\[3pt]
\displaystyle \sum_i\min(a_i,h-1)+\sum_i[a_i\ge h,\quad a_i\equiv h\pmod2],&p<n\le 2p,\quad h=n-p,\\[3pt]
p,&n>2p.
\end{cases}
\]

In particular, the full complexity sequence depends on the **multiset** of run lengths and not on their cyclic order; the middle regime includes an exceptional parity-sensitive class of closed factors.

## Assumptions and scope

Fix \(q\ge3\), pairwise distinct symbols \(c_0,\ldots,c_{q-1}\), and positive integers \(a_0,\ldots,a_{q-1}\). Define
\[
U=c_0^{a_0}c_1^{a_1}\cdots c_{q-1}^{a_{q-1}},\qquad p=|U|,\qquad X=U^\omega.
\]
Indices on run labels are cyclic modulo \(q\). Each factor begins at some *phase* \(s\in\{0,\ldots,p-1\}\). Distinct phases yield distinct factors for \(n\ge p\), because the distinct ordered cyclic transitions \(c_i c_{i+1}\) identify their positions and \(U\) is primitive. For \(n<p\), factors at different phases may coincide, and are counted only once.

## Proof

**Transition lemma.** Each ordered mixed pair \(c_i c_{i+1}\) occurs exactly once per period, and hence a factor containing this pair has occurrences only at phase shifts divisible by \(p\). In particular, two occurrences of such a factor cannot have starting positions at distance strictly between zero and \(p\).

**Regime \(1\le n\le p\).** A factor consisting of a single symbol is \(c_i^n\), which exists exactly when \(a_i\ge n\) and is closed. Consider a nonconstant closed factor \(w\), and let \(v\) be a proper border that occurs exactly twice in \(w\). Its two occurrences start at a distance strictly smaller than \(p\), so the transition lemma forces \(v\) to be constant. Thus the first and last letters of \(w\) coincide, say they equal \(c_i\). Since each \(c_i\)-run occurs only once per period, \(w\) consists of a terminal segment \(c_i^u\), then a full cyclic traverse of the other \(q-1\) runs, then an initial segment \(c_i^v\), with \(u,v\ge1\) and \(u+v\le a_i\). The longest border is \(c_i^{\min(u,v)}\). It has exactly two occurrences if and only if \(u=v\): if one of these segments is longer, the shorter border occurs at least twice in the longer segment and at least once at the other end. Hence each \(i\) contributes one mixed closed factor exactly when \(n=(p-a_i)+2u\) with \(1\le u\le\lfloor a_i/2\rfloor\). This is precisely the second indicator sum. All constructed factors are distinct because they contain a unique directed sequence of different symbols, or have different pure letter labels.

**Regime \(p<n\le 2p\).** Write \(n=p+h\), with \(1\le h\le p\). A starting phase in run \(i\) has an offset \(j\in\{0,\ldots,a_i-1\}\) from the beginning of that run. The period relation gives a border of length \(h\), whose two nominal occurrences start at phases \(s\) and \(s+p\). If \(h>a_i-j\), this length-\(h\) prefix contains the unique outgoing transition \(c_i c_{i+1}\). By the transition lemma it has exactly two occurrences in the length-\(n\) factor, making it closed. The number of such offsets is \(\min(a_i,h-1)\).

Otherwise \(h\le a_i-j\), so the period border is constant \(c_i^h\). Let \(u=a_i-j\) be the first \(c_i\)-segment length and \(v=j+h\) be the terminal \(c_i\)-segment length. Because the factor is longer than one period, it contains the complete other runs and returns to the same \(c_i\)-run. A border longer than \(h\) would have occurrences separated by \(n-\ell<p\). Such a border cannot contain a unique mixed transition by the lemma, so only constant borders can possibly occur. Their maximal length is \(\min(u,v)\), and the border has exactly two occurrences precisely when \(u=v\). The equality rearranges to \(2j=a_i-h\). It has one valid integer solution exactly when \(a_i\ge h\) and \(a_i\equiv h\pmod2\). These offsets are disjoint from the preceding case, yielding the formula.

**Regime \(n>2p\).** The border of length \(n-p>p\) of each factor contains a mixed transition. Its only occurrences start at distance \(p\), because the transition occurs exactly once in a period. Thus all \(p\) phases are closed, and the factors are distinct.

These three cases exhaust every positive length and every possible starting phase, completing the proof.

## Verification

The standalone program `closed_verify.py` defines closedness directly from all nonempty proper borders and their occurrence counts, enumerates distinct factors at all phases, and compares these counts with the displayed formulas. Exhaustive testing covered 35,920 triples of run-count, run-length profile and factor length with run counts from two through five, run lengths one through four and factor lengths through \(2p+3\). A separate seeded suite tested 2,000 further profiles with three through seven runs and run lengths as large as 15. All comparisons passed. These finite tests are consistency checks, not substitutes for the infinite proof.

Run with `python3 closed_verify.py` using the Python standard library.

## Relationship to prior work

Parshina and Puzynina [1] define closed words via complete returns and study extremal closed-rich finite and infinite words, with general observations on powers and cyclic factors. Their cyclic-square upper bound and length-based treatment of long closed factors do not supply the present complete closed-complexity formula for pairwise-distinct cyclic runs. Parshina and Postic [2] develop open/closed complexity as a periodicity criterion, addressing different general conclusions. Exact binary two-run closed/open complexity has been treated separately [3]; the present theorem assumes at least three distinct run letters and does not claim that boundary as new.

## Limitations

The classification assumes every run symbol is different from all other run symbols in a period; merely adjacent distinctness is insufficient for the transition lemma. It is a statement about the infinite periodic factor language, not the closed factors of a finite prefix. No asymptotic claim for nonperiodic words, nor any characterization of equivalent formulae beyond the inspected literature, is made. The priority comparison is necessarily limited by discoverability of prior publications.

## References

[1] O. Parshina and S. Puzynina, *Finite and infinite closed-rich words*, arXiv:2111.00863 (first public 2021-11-01), https://arxiv.org/abs/2111.00863.

[2] O. Parshina and M. Postic, *Open and closed complexity of infinite words*, arXiv:2005.06254 (2020), https://arxiv.org/abs/2005.06254.

[3] Existing exact binary two-run period closed/open complexity results; credited here as a different, already-treated alphabet boundary rather than a claim of priority.
