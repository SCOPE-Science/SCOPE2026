# Exact length-two tandem-duplication spectrum on the Fibonacci binary language

## Finding
Let \(\mathcal F_n\subseteq\{0,1\}^n\) be all indexed *linear* binary words containing no adjacent `11`, for any integer \(n\ge2\). For \(w\in\mathcal F_n\), let \(\mathcal D_2(w)\) consist of all **distinct** length-\(n+2\) words obtained by choosing exactly one length-two factor and replacing it by two consecutive copies. Put \(B(w)=|\mathcal D_2(w)|\), with repeated descendants from different sites counted once. Define
\[
A_n(u)=\sum_{w\in\mathcal F_n}u^{B(w)-1}.
\]
The exact all-length sphere-size distribution is
\[
\boxed{\displaystyle\sum_{n\ge2} A_n(u)t^{n-2}
=\frac{3+2ut+(u^2+2u-3)t^2}{1-t-t^2+(1-u^2)t^3}.}
\]
In particular, for every \(n\ge2\),
\[
\boxed{\max_{w\in\mathcal F_n} B(w)=1+\left\lceil\frac{2(n-2)}3\right\rceil.}
\]
The number of words attaining this maximum is exactly \(2\) if \(n\equiv0\pmod3\), exactly \(1\) if \(n\equiv1\pmod3\), and exactly \((n+7)/3\) if \(n\equiv2\pmod3\). Exactly three words have the smallest value \(B(w)=1\): the all-zero word and the two alternating words (truncated at length \(n\)). Moreover \(A_n(1)=F_{n+2}\), with \(F_0=0,F_1=1\), and the exact summed descendant count satisfies
\[
\sum_{n\ge2}A'_n(1)t^{n-2}=\frac{2t(1+t)}{(1-t-t^2)^2}.
\]
These results concern **exactly one** duplication, not the radius-at-most-one error ball (which also includes the source word).

## Assumptions and scope
The alphabet is fixed and binary. The input constraint is *linear* avoidance of consecutive ones; no wrap-around condition is imposed. A length-two tandem duplication at a zero-based position \(j\), where \(0\le j\le n-2\), transforms \(w=abc\) with \(|a|=j,|b|=2\) into \(abbc\). The output is not subject to the no-`11` constraint. Original symbols are indexed; neither reversal nor rotation equivalence is taken. We count distinct output *words*, not duplication positions or error histories.

## Proof
**1. The exact output-degree statistic.** Retain \(w_0,w_1\) and define its two-step binary derivative \(v_i=w_i\oplus w_{i+2}\) for \(0\le i\le n-3\). The initial pair and derivative determine \(w\) uniquely via \(w_{i+2}=w_i\oplus v_i\). Direct substitution shows that duplicating the factor at position \(j\) leaves the initial pair unchanged and inserts `00` into \(v\) at position \(j\). For any binary derivative, two such zero insertions agree precisely when the insertion locations lie in the same gap between successive ones, including the leading and trailing gaps. There are exactly \(1+\sum_i v_i\) such gaps, even when there are no ones. Therefore
\[
B(w)=1+\sum_{i=0}^{n-3}[w_i\ne w_{i+2}]. \tag{1}
\]
This can alternatively be proved by cancelling the common prefixes and suffixes of the two duplicated words. Equation (1) is a fixed-duplication derivative identity, not itself claimed as novel.

**2. Transfer matrix and complete generating function.** A permitted source's last two letters have state `00`, `01`, or `10`. On appending a third letter \(c\), the new indicator is \([a\ne c]\) when the old state is `ab`. With states in that order, the weighted transition matrix is
\[
M(u)=\begin{pmatrix}1&u&0\\0&0&1\\u&1&0\end{pmatrix}.
\]
Each of the three initial two-letter states has weight one. Consequently \(A_n(u)=\mathbf1^T M(u)^{n-2}\mathbf1\) for every \(n\ge2\). The formal geometric series identity gives \(\sum_{n\ge2}A_n(u)t^{n-2}=\mathbf1^T(I-tM(u))^{-1}\mathbf1\). A direct three-by-three determinant computation yields the displayed rational function. Equivalently,
\[
A_2=3,\quad A_3=3+2u,\quad A_4=3+4u+u^2,
\]
and for all \(n\ge5\),
\[
A_n=A_{n-1}+A_{n-2}+(u^2-1)A_{n-3}. \tag{2}
\]
This proves the complete spectrum for every length, without assuming experimental stabilization.

**3. Sharp maximum and number of maximizers.** Write \(m_n=\deg A_n\), and \(c_n=[u^{m_n}]A_n\). Every coefficient of \(A_n\) is a nonnegative integer count, so these are exactly the maximum exponent and its multiplicity. From the three base polynomials, \(m_2=0,m_3=1,m_4=2\), with leading coefficients \(3,2,1\). Induct in three residue classes using (2). When \(n=3k\), the term \(u^2A_{n-3}\) has degree \(2k-1\), strictly larger than all other terms; thus \(m_n=2k-1,c_n=2\). When \(n=3k+1\), it alone has degree \(2k\), giving \(m_n=2k,c_n=1\). When \(n=3k+2\), both \(A_{n-1}\) and \(u^2A_{n-3}\) have degree \(2k\) and the other terms have lower degree. Hence \(c_n=c_{n-1}+c_{n-3}=1+(k+2)=k+3=(n+7)/3\), starting with \(c_2=3\). In all cases \(m_n=\lceil 2(n-2)/3\rceil\). The subtractive term \(-A_{n-3}\) has degree at least two below the new maximum, so it cannot cancel the leading coefficient.

**4. Minimum and first moment.** At \(u=0\), the generating function simplifies to \(3/(1-t)\), giving \(A_n(0)=3\) for every \(n\ge2\). Directly from (1), a word has one distinct descendant if and only if \(w_i=w_{i+2}\) for all applicable \(i\), meaning it is two-periodic. Among no-`11` binary words, precisely `00...0`, `0101...`, and `1010...` qualify. Setting \(u=1\) in the rational series gives \((3+2t)/(1-t-t^2)\), whose coefficient of \(t^{n-2}\) is \(F_{n+2}\). Formal differentiation with respect to \(u\) at \(u=1\) gives the stated exact summed descendant-count series.

## Verification
Run `python3 verify.py` with Python 3 and no third-party modules. It independently constructs every possible duplicated output of every no-`11` source word at lengths \(2\) through \(18\), compares the resulting size to (1), and matches the complete observed histogram to the coefficient recurrence (2). This checks 17,706 source words in total. It additionally checks the polynomial totals, minimum coefficient, maximum degree and maximum multiplicity for all lengths through 60, and checks stated example coefficient arrays. The expected terminal string is `VERIFY_OK`. These finite computations support but do not replace the complete proof above. For instance,
\[
A_6(u)=3+8u+8u^2+2u^3,\qquad
A_{10}(u)=3+16u+40u^2+44u^3+32u^4+8u^5+u^6.
\]

## Relationship to prior work
Jain, Farnoud, Schwartz and Bruck [1] derive the invertible fixed-length-duplication difference transform and the zero-signature model. Their result supplies the general identity used in proof step 1, not the constrained enumerator or its sharp extremal counts. Lenz, Wachter-Zeh and Yaakobi [2] develop general tandem-duplication sphere formulas and unrestricted-channel counting bounds; their sphere includes the no-error source, while the current statistic counts *exactly one* duplication. In particular, their single-error formula implies (1) after subtracting the no-error element, but their investigated source is the full alphabet power rather than \(\mathcal F_n\), and their results do not imply the displayed restricted coefficient generating function without additional constrained enumeration. Kulkarni and Kiyavash [3] motivate constrained source coding and study deletion bounds for run-length-limited languages, not length-two tandem-duplication forward spheres.

A publicly available exact finite-optimum analysis [4] treats all binary source words under one length-two tandem duplication, and computes maximum codebook sizes, not the constrained source's forward-degree distribution. A separate exact spectrum [5] concerns *reverse-complement*, not ordinary, tandem duplication; those two transformations are different even over the binary alphabet. Related joint-duplication statistics [6] concern unrestricted independent uniform sources and pairs of duplication lengths, not the no-adjacent-one source and its sharp extremizers.

## Limitations
This result is not a capacity theorem: no maximum cardinality of a duplication-correcting code is asserted. It does not enumerate descendant sets after two successive duplications, optimal decoders, cyclic input restrictions, longer duplicated blocks, or other alphabets. The coefficient series and extremal counts are exact, but they do not establish historical uniqueness; relevant unindexed earlier work may exist. The initial difference representation and general single-duplication degree identity are prior results credited above. No independent mathematical audit is claimed.

## References
[1] S. Jain, F. Farnoud, M. Schwartz and J. Bruck, *Duplication-Correcting Codes for Data Storage in the DNA of Living Organisms*, arXiv:1606.00397v1, first public 2016-06-01, https://arxiv.org/abs/1606.00397 (particularly Sections II–III).

[2] A. Lenz, A. Wachter-Zeh and E. Yaakobi, *Bounds on Codes Correcting Tandem and Palindromic Duplications*, arXiv:1707.00052, first public 2017-06-30, https://arxiv.org/abs/1707.00052 (Sections 2.1, 3.1 and 4).

[3] A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128v1, first public 2012-11-13, https://arxiv.org/abs/1211.3128 (constrained-source motivation; different channel).

[4] *Exact finite optima for binary codes correcting one length-two tandem duplication*, published research note, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-finite-optima-for-binary-codes-correcting-one-length-two-t--8557c0dca75c.

[5] *Exact one-step descendant spectrum for length-two reverse-complement duplication*, published research note, 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-one-step-descendant-spectrum-for-length-two-reverse-comple--0aca79ccebc0.

[6] *Joint law and independence threshold for two tandem-duplication descendant counts*, published research note, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-joint-law-and-independence-threshold-for-two-tandem-duplication--d6154f9c908e (indexed summary compared; full text not inspected).
