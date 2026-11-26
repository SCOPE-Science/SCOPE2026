# Maximal closed substrings of symmetric five-run binary words

## Finding

For every three positive integers \(a,b,c\), set
\[
W=0^a1^b0^c1^b0^a,\qquad n=2a+2b+c.
\]
A **closed** nonempty word is a one-letter word or a word with a nonempty proper border occurring exactly twice (at its two ends, possibly overlapping). A **maximal closed substring occurrence** (MCS) is a closed interval of positions that cannot be extended by one available letter on either side and remain closed. Count *occurrences*, not distinct string values. Write \(K(W)\) for the number of MCSs.

**Theorem (complete all-parameter classification).** With one-based inclusive endpoints, every MCS of \(W\) belongs to exactly one of the following four disjoint groups:

1. The five complete constant-letter runs, with endpoints
\[
(1,a),\ (a+1,a+b),\ (a+b+1,a+b+c),\ (a+b+c+1,a+2b+c),\ (a+2b+c+1,n).
\]
2. The two mirror-image groups, for each integer \(1\le t\le\min(a,c-1)\):
\[
(a-t+1,a+b+t),\qquad
(a+b+c-t+1,a+2b+c+t).
\]
3. For each integer \(1\le t\le b-1\), the central group
\[
(a+b-t+1,a+b+c+t).
\]
4. For each integer \(\min(a,c)\le t\le a\), the spanning group
\[
(a-t+1,a+2b+c+t).
\]

All ranges are inclusive and empty when the upper endpoint is smaller than the lower one. Consequently,
\[
\boxed{K(W)=a+b+4+\min(a-1,c-1)+2\mathbf1_{\{c>a\}}.}
\]
The complete length/count bivariate enumerator is the rational series
\[
\boxed{\sum_{a,b,c\ge1}z^{2a+2b+c}u^{K(W)}
=\frac{z^5u^6}{(1-z^3u^2)(1-z^2u)^2}
+\frac{z^6u^8}{(1-z)(1-z^3u^2)(1-z^2u)}.}
\]
For every fixed length \(n\ge6\), the sharp maximum within this symmetric five-run family is
\[
\boxed{\max_{2a+2b+c=n}K(W)=\left\lfloor\frac{2n}{3}\right\rfloor+4,}
\]
where positive integers \(a,b,c\) are required. For length five the unique such word has six MCSs.

## Assumptions and scope

The strings are finite and linear over the *binary* alphabet; all three run parameters are strictly positive. The five runs are genuine maximal constant-letter runs. Interchanging the two alphabet letters preserves all claims. The MCS definition is relative to the whole displayed word: if an extension would pass its boundary, that extension is unavailable and imposes no constraint. All borders are proper, and coincident/overlapping positions of border occurrences are counted under the usual string-matching convention. The theorem concerns closed **occurrences**, not the number of different closed factors, and asserts an identity for every positive parameter triple, not only asymptotically or for tested sizes.

## Proof

**1. Consecutive-longest-border criterion.** Write \(T[i..j]\) for inclusive endpoints. For distinct starting positions \(i<q\), let \(L(i,q)\) be the longest common prefix length of the suffixes \(T[i..n]\) and \(T[q..n]\). For length at least two, an interval \([i,e]\) is an MCS precisely when there is a \(q>i\) and \(h=L(i,q)>0\) such that
\[
e=q+h-1,\qquad L(i,r)<h\quad(i<r<q),
\]
and either \(i=1\) or \(T[i-1]\ne T[q-1]\). The first inequality says that the border \(T[i..i+h-1]=T[q..q+h-1]\) has no intermediate occurrence. Maximality of \(h\) makes the right one-letter extension open, and the predecessor inequality makes the left one-letter extension open. Conversely, let an MCS of length at least two have its longest border of length \(h\) and second occurrence start at \(q\). The absence of intermediate occurrences gives the inequality for \(r\). If the matching suffixes extended right, or their predecessors agreed, the factor would have a closed one-letter extension, contrary to maximality. If an extension were closed with a different border length, comparing its longest border with the original longest border forces that length to increase by exactly one, giving the same matching condition; this follows since every shorter border of a closed factor occurs inside its longest border. Thus the criterion is necessary and sufficient (also Corollary 1 of Fischer--Köppl, cited below).

For a one-letter interval, maximality means its letter differs from both available neighbors. Since all run lengths are positive, a whole run is an MCS (including a singleton run), and no proper subrun is: extending the latter within the run gives another closed unary word.

**2. Enumerating all non-unary candidates.** Any two copies of a nonempty border start in runs carrying the same letter. Thus the only possible pairs of *different* runs are \((1,3),(1,5),(2,4),(3,5)\), where runs are indexed from left to right. Pairs starting in the same run produce only the whole-run intervals: when the earlier start is not the start of that run, the predecessors agree; if it is the run start, the next matching occurrence is the next position of that same run and the rightmost matching endpoint is exactly the run end.

For pairs in runs \((1,3)\), let \(t\) be the number of zeroes remaining at the first start and \(s\) the number remaining at the second start. If \(t<s\), the common-prefix length is \(t\). The second start is the *next* occurrence of that prefix only when it is the beginning of run 3 (otherwise an earlier copy occurs in run 3); this gives exactly the first interval of group 2, with \(t\le a\) and \(t<c\). If \(t>s\), the prefix \(0^s\) occurs again inside run 1 before reaching run 3, so no interval qualifies. If \(t=s\), both copies continue through a whole \(1^b\) run and into the following zero run. Their common prefix has length \(t+b+\min(c,a)\). Their predecessor letters differ only when \(t=c\) (the run-3 start is preceded by one) or \(t=a\) (the first copy starts at the left boundary); all smaller common values have zero predecessors. This gives the single group-4 interval with \(t=\min(a,c)\). The right-mismatch condition holds: after the common zero suffix either one side has the next one-run letter or the other side has exhausted the word.

For pairs in runs \((1,5)\), the later copy can be a *next* occurrence only if its start is the beginning of the last zero run; otherwise a copy starting earlier in that last run intervenes. Let \(t\) be the zeros remaining at the first start. If \(t\le c\), a copy of \(0^t\) in the central run intervenes. If \(c<t\le a\), the two copies have maximal common prefix \(0^t\), and their predecessors differ (or the first is a boundary). This gives precisely the remaining group-4 intervals, \(c<t\le a\). In combination with the preceding case, the allowed group-4 parameters are exactly \(\min(a,c)\le t\le a\).

For pairs in runs \((3,5)\), reversal symmetry gives the second group-2 interval, with \(1\le t\le\min(a,c-1)\). This explicitly includes the endpoint \(t=a<c\) when the first copy begins inside the center zero run and the second copy reaches the final boundary.

Finally, for pairs in runs \((2,4)\), the words are \(1^b\) on both sides. If the first one-run has \(t<b\) ones remaining, only the beginning of the second one-run can give the next occurrence, and the common-prefix length is \(t\); this yields group 3. If the first copy begins at the start of its one-run, then the two starts either have equal zero predecessors (when the second copy also starts at a run boundary) or the prefix has an intervening occurrence within the first one-run (when the second copy is interior). All other starts have matching one predecessors or an intervening copy. Thus no additional pair qualifies.

These four pair analyses enumerate all possible non-unary MCSs. The endpoint formulas show that the four groups are disjoint: a run has no transitions, a group-2 or group-3 interval has exactly two transitions, and a group-4 interval has four transitions. The two-transition classes have different middle letters, and within each group different parameter values give different endpoints. The classification is proved.

**3. Exact count.** The groups contain, respectively,
\[
5,\quad 2\min(a,c-1),\quad b-1,\quad a-\min(a,c)+1
\]
intervals. Their sum equals \(a+b+5+2\min(a,c-1)-\min(a,c)\). When \(c\le a\), this simplifies to \(a+b+c+3\); when \(c>a\), it simplifies to \(2a+b+5\). The two cases are exactly the boxed indicator formula.

**4. Rational length/count series.** For \(c\le a\), write \(a=c+r\), \(r\ge0\). Then the length is \(3c+2r+2b\) and the count is \(2c+r+b+3\). Summing the three independent geometric series for \(c\ge1,r\ge0,b\ge1\) gives the first rational term. For \(c>a\), write \(c=a+1+r\), \(r\ge0\). Then the length is \(3a+1+r+2b\) and the count is \(2a+b+5\), giving the second term. Every positive triple lies in exactly one case.

**5. Sharp fixed-length extremum.** When \(c>a\), use \(n=2a+2b+c\) and \(c\ge a+1\), \(b\ge1\) to obtain
\[
3\bigl(K(W)-4\bigr)=6a+3b+3\le4a+4b+2c=2n;
\]
thus \(K(W)\le\lfloor2n/3\rfloor+4\). When \(c\le a\), the inequality \(n\ge3c+2\) implies
\[
K(W)=\frac{n+c}{2}+3\le\frac{2n-1}{3}+3
<\frac{2n}{3}+4,
\]
so the same integer upper bound holds. It is sharp for all \(n\ge6\): for lengths \(n=3a+3\), use \((a,b,c)=(a,1,a+1)\); for \(n=3a+4\), use \((a,1,a+2)\); for \(n=3a+5\), use \((a,2,a+1)\). Here \(a\ge1\), and these three families cover all integers \(n\ge6\) by residue class. The lone \(n=5\) case is \((1,1,1)\), with six MCSs.

## Verification

Two standalone scripts independently recompute the *exact endpoint sets* rather than only their counts. `check_by_closed.py` enumerates all substrings, evaluates border occurrences directly, and tests both one-letter extensions, for every \(1\le a,b,c\le6\) (216 words, 2,886 MCS occurrences). `check_by_next_occurrence.py` independently computes longest common extensions and the first-next-occurrence condition, for every \(1\le a,b,c\le18\) (5,832 words, 171,774 MCS occurrences), and checks fixed-length maxima through length 80. Both scripts use Python standard-library facilities only and compare every computed endpoint to the asserted four-group classification. Run them with `python3 check_by_closed.py` and `python3 check_by_next_occurrence.py`. The saved outputs are included. These exhaustive **bounded** checks corroborate the algebra; the all-positive-integer proof is the run-pair argument above and does not rely on extrapolation.

## Relationship to prior work

Badkobeh, De Luca, Fici and Puglisi introduced maximal closed substrings and the distinction between closed *occurrences* and factors. Umezaki, Shibata, Nakashima and Inenaga (2026) give a general compact enumeration from run-length encoding; Fischer and Köppl (October 28, 2026) give output-sensitive enumeration on arbitrary strings, including the next-occurrence/LCE criterion; Faro, Marino and Pavone (November 8, 2026) study internal queries. These algorithms compute an instance but do not provide the all-parameter endpoint formula, the explicit bivariate series or the sharp fixed-length extremum in the symmetric five-run class. Closest accessible previously published exact specializations cover **four-run MCS occurrences**, and a separate five-run result counts **distinct closed factors**, which is a different invariant. The present contribution is a narrow symbolic classification, not a new general-purpose algorithm or an improvement to unrestricted worst-case complexity.

## Limitations

The symmetry \(a=e,b=d\) is essential to the displayed formulas; no assertion is made for arbitrary five-run parameters, larger alphabets, circular words, or counts of distinct factor values. General existing algorithms already compute the underlying MCS endpoints for any fixed word, so algorithmic computability itself is not novel. Unrecognized earlier explicit special cases remain possible, and no independent mathematical validation has been performed.

## References

- H. Umezaki, H. Shibata, Y. Nakashima and S. Inenaga, *Compact Enumeration of Maximal Closed Substrings in Run-Length Encoded Strings*, arXiv:2607.02838, first public July 3, 2026. https://arxiv.org/abs/2607.02838
- J. Fischer and D. Köppl, *Output-Sensitive Enumeration of Maximal Closed Substrings in Linear Space*, arXiv:2610.38114, first public October 28, 2026. https://arxiv.org/abs/2610.38114
- S. Faro, F. P. Marino and A. Pavone, *Internal Queries for Maximal Closed Substrings*, arXiv:2611.11552, first public November 8, 2026. https://arxiv.org/abs/2611.11552
- G. Badkobeh, A. De Luca, G. Fici and S. J. Puglisi, *Maximal Closed Substrings*, arXiv:2209.00271, first public 2022. https://arxiv.org/abs/2209.00271
