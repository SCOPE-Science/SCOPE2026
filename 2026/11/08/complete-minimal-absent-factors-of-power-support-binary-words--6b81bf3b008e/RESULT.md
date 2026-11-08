# Complete minimal absent factors of power-support binary words

## Finding

Fix any integer \(b\ge2\). Define the one-sided infinite binary word \(w_b\), indexed from zero, by \(w_b(t)=1\) if and only if \(t=b^j\) for an integer \(j\ge0\). A **minimal absent factor** is a nonempty finite binary word which is not a contiguous factor of \(w_b\), although every proper contiguous factor is. Equivalently, for a word of length at least two, its two immediate length-minus-one factors occur but the word itself does not.

Put \(g_j=(b-1)b^j\), let \(\ell_0=1\), and let \(\ell_j=g_{j-1}-1\) for \(j\ge1\). The **complete** minimal-absent-factor language of \(w_b\) is the disjoint union of the following four families:

\[
\begin{aligned}
\mathcal A_0&=\{1\,0^{t-1}\,1:t\ge1,\ t\notin\{g_j:j\ge0\}\},\\
\mathcal A_1&=\{0^{\ell_j+1}\,1\,0^{g_j-1}\,1:j\ge0\},\\
\mathcal A_2&=\{1\,0^{g_j-1}\,1\,0^{g_{j+1}}:j\ge0\},\\
\mathcal A_3&=\{1\,0^{g_i-1}\,1\,0^{g_0-1}\,1:i\ge0,\ g_i\le2\}.
\end{aligned}
\]

In particular, \(\mathcal A_3=\{111,1011\}\) for \(b=2\), \(\mathcal A_3=\{10101\}\) for \(b=3\), and \(\mathcal A_3\) is empty for \(b\ge4\). Every minimal absent factor therefore contains **at most three ones**.

Let \(M_b(N)\) denote the number of distinct minimal absent factors of length at most \(N\). For every integer \(N\ge1\), the exact formula is

\[
\begin{aligned}
M_b(N)={}&N-1-\sum_{j\ge0}\mathbf1_{\{g_j\le N-1\}}+\mathbf1_{\{N\ge b+2\}}\\
&+2\sum_{j\ge0}\mathbf1_{\{(b^2-1)b^j+1\le N\}}+\epsilon_b(N),
\end{aligned}
\]

where \(\epsilon_2(N)=\mathbf1_{\{N\ge3\}}+\mathbf1_{\{N\ge4\}}\), \(\epsilon_3(N)=\mathbf1_{\{N\ge5\}}\), and \(\epsilon_b(N)=0\) for \(b\ge4\). All sums are finite for each fixed \(N\). Consequently,

\[
M_b(N)=N+\log_bN+O_b(1)\qquad(N\to\infty).
\]

For every \(b\ge2\), this minimal-absent-factor language is not regular.

## Assumptions and scope

All factors are **contiguous** and all words are over the fixed alphabet \(\{0,1\}\). The support begins at position \(b^0=1\), so the zero at position zero matters in the two-one boundary family. The infinite word is one-sided; no artificial left or right boundary symbol is included. The convention \(0^0=\varepsilon\) denotes the empty word. The classification, exact counting formula, asymptotic, and nonregularity hold uniformly for every integer \(b\ge2\) and every indicated integer \(N\). Nothing is asserted for noninteger bases, other alphabets, or minimal absent **subsequences**.

## Proof

**1. Factor structure.** Consecutive ones of \(w_b\) are at \(b^j,b^{j+1}\), hence have distance \(g_j\). The \(g_j\) strictly increase. Thus \(1\,0^{t-1}\,1\) is a factor if and only if \(t=g_j\), and then occurs exactly once, starting at \(b^j\). The number of zeros immediately preceding that first one is \(\ell_j\), as defined above. After the second one, exactly \(g_{j+1}-1\) zeros precede the next one. Since both adjacent gaps grow without bound, every binary word containing at most one one is a factor.

**2. Two-one minimal absences.** An absent word containing exactly two ones has the form \(0^a1\,0^{t-1}1\,0^c\), where \(a,c\ge0\), \(t\ge1\). When \(t\) is not one of the \(g_j\), minimality forces \(a=c=0\), giving exactly \(\mathcal A_0\). When \(t=g_j\), the two-one core has one occurrence. Its left and right extensions fit precisely when \(a\le\ell_j\) and \(c\le g_{j+1}-1\). A minimal absence must exceed exactly one of these bounds by exactly one and have zero extension on the other side, yielding \(\mathcal A_1\) or \(\mathcal A_2\). Conversely, removing either endpoint letter from every displayed word gives an occurring factor, while the displayed word cannot occur.

**3. Three-one minimal absences.** Any minimal absent word containing at least three ones must start and end with one. Indeed, if it had an initial zero and its all-one-core gap list did not occur, removing that zero would leave an absent word; if its core did occur, its initial excess could not be cured by removing the last character, since at least two ones remain. The same argument applies to a final zero.

Write a putative three-one minimal absence as \(1\,0^{g_i-1}1\,0^{g_j-1}1\). The first gap must equal some \(g_i\), because the prefix ending in the second one occurs, and the second gap must equal some \(g_j\), because the suffix starting in the second one occurs. The immediate prefix of the full word additionally requires \(g_j\le g_{i+1}\), i.e. \(j\le i+1\). Its immediate suffix requires \(g_i\le\ell_j+1\). If \(j\ge1\), this becomes \(i\le j-1\), so \(j=i+1\) and the entire word occurs, a contradiction. If \(j=0\), the latter condition becomes \(g_i\le2\); the resulting word cannot occur because its gap indices are not consecutive. This is exactly \(\mathcal A_3\), and the endpoint conditions also prove minimality.

**4. No four-one minimal absences.** If a minimally absent word had at least four ones, Step 3's endpoint argument makes it start and end in one. Both its immediate prefix and suffix then contain at least three ones and occur. The first two gap distances uniquely identify an occurrence's starting marker index, while their shared gap distances force the prefix and suffix occurrences to be the two overlapping windows in the same consecutive chain of markers. Therefore the full word occurs, contradiction. This proves the exhaustive four-family classification.

**5. Exact counts.** In \(\mathcal A_0\), the length is \(t+1\), giving \(N-1\) choices minus the number of allowed gaps \(g_j\le N-1\). The unique \(j=0\) member of \(\mathcal A_1\) has length \(b+2\). Every other \(\mathcal A_1\) member, and every \(\mathcal A_2\) member, corresponds once to \(j\ge0\) and has length \(g_j+g_{j+1}+1=(b^2-1)b^j+1\). The exceptional \(\mathcal A_3\) members give exactly \(\epsilon_b(N)\). The families are disjoint by their number of ones or their endpoint symbols. Summation proves the exact formula. Both geometric-gap sums equal \(\log_b N+O_b(1)\), yielding the stated asymptotic.

**6. Nonregularity.** Intersect the minimal-absent-factor language with the regular language \(1\,0^*\,1\). The result is exactly \(\mathcal A_0\). If it were regular, the set of positive integer distances \(t\notin\{g_j\}\) would be ultimately periodic. So would its complement \(\{g_j\}\). But this latter set is infinite with unbounded successive gaps \(g_{j+1}-g_j\), and therefore is not ultimately periodic. This is a contradiction.

## Verification

The standalone Python 3 standard-library script `verify.py` reconstructs factors independently from a factor-complete finite prefix for each cutoff. It compares the entire predicted minimal-absent-word set against words whose two immediate factors occur, for \(b=2,\ldots,8\) and cutoffs \(N=8,12,18,24,32,40\). It additionally compares the exact length-count formula and explicit family generation for \(b=2,\ldots,20\) and \(N=1,\ldots,700\). The observed output was:

`VERIFY_OK complete_prefix_cases=42 factor_sets=17750 minimal_absent_words=936 formula_ranges=2..20,1..700`

For factor-completeness, choose the check's marker \(b^J\) with at least \(N\) zeros on either side. This supplies every at-most-one-one factor of length at most \(N\). Any factor with at least two ones contains a consecutive marker gap shorter than \(N\), and every such gap occurs strictly before the cutoff marker; the finite prefix includes its needed right context. These are finite checks only; the infinite quantifiers are proved by Steps 1–6, not by enumeration.

## Relationship to prior work

Akagi, Okabe, Mieno, Nakashima, and Inenaga (2022) establish a classification into five run-length types and output-sensitive algorithms for minimal absent words of arbitrary **finite** run-length-encoded strings. Ayad, Badkobeh, Fici, Héliou, and Pissis (2020) establish antidictionary computation for finite document collections. Their general algorithms and characterizations are compatible with this work, but do not themselves supply the four-family forbidden language, all-base exact cumulative count, or nonregularity for the infinite power-support sequence. The contribution here is the specialization-independent **explicit infinite classification** and its exact enumerative consequences, not the definition or general algorithm for minimal absent words.

## Limitations

The result concerns the factor language of one specific natural family, not an arbitrary sparse support or a uniform algorithmic improvement on finite-string MAW enumeration. The characterization is in the one-sided infinite limit; the minimal absent words of individual finite prefixes include additional endpoint artifacts. Existing broad MAW frameworks might yield an equivalent statement under an unstated specialization, and independent verification of the literature comparison has not been performed.

## References

- T. Akagi, K. Okabe, T. Mieno, Y. Nakashima, and S. Inenaga, *Minimal Absent Words on Run-Length Encoded Strings*, arXiv:2202.13591 (first public version, 2022-02-28), and CPM 2022, DOI: 10.4230/LIPIcs.CPM.2022.27. https://arxiv.org/abs/2202.13591
- L. A. K. Ayad, G. Badkobeh, G. Fici, A. Héliou, and S. P. Pissis, *Constructing Antidictionaries of Long Texts in Output-Sensitive Space*, Theory of Computing Systems (2020), DOI: 10.1007/s00224-020-10018-5. https://link.springer.com/article/10.1007/s00224-020-10018-5
