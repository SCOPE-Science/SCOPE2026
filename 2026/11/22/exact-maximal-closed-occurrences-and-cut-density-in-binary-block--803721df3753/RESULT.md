# Exact maximal closed occurrences and cut density in binary block powers

## Finding
For all integers \(a,b\ge1\) and \(k\ge3\), let \(W=(0^a1^b)^k\), \(p=a+b\), and \(n=kp\). The maximum number of maximal closed substring (MCS) occurrences crossing a single internal gap is exactly \(p-1\). Every gap between two full copies of \(0^a1^b\) attains the bound.

To determine the gap maximum, we specialize the general structure of MCSs to this family: all occurrences are the individual maximal constant runs, the bridge intervals specified below between successive equal-symbol runs, and the full interval of \(W\). Consequently their total number is
\[
K(W)=(k-1)(a+b)+3=n-p+3.
\]
Both formulas also hold for \(k=2\), where the earlier four-run endpoint classification already gives the occurrence list. The contribution here is the sharp period-dependent gap maximum for all \(k\ge3\), not a new general classification or enumeration algorithm.

## Assumptions and scope
A finite nonempty word is *closed* when it has length one, or when it possesses a nonempty proper border that occurs **exactly twice**, once as prefix and once as suffix. An occurrence \([i,j)\) in a word of length \(n\) uses zero-based, half-open coordinates. It is an MCS when its factor is closed and neither available one-position left extension \([i-1,j)\) nor right extension \([i,j+1)\) is closed. Thus maximality concerns occurrences, not distinct factor values.

For \(r=0,\ldots,2k-1\), define run starts and run lengths by
\[
 s_{2h}=hp,\quad \ell_{2h}=a,\qquad
 s_{2h+1}=hp+a,\quad \ell_{2h+1}=b
 \qquad(0\le h<k).
\]
All intervals are intersected with the fixed full word, not with an infinite-periodic extension. The complete set is the union of three disjoint families:
\[
\begin{aligned}
\mathcal R&=\{[s_r,s_r+\ell_r):0\le r<2k\},\\
\mathcal B&=\{[s_r+\ell_r-t,s_{r+2}+t):0\le r<2k-2,\quad 1\le t<\ell_r\},\\
\mathcal F&=\{[0,n)\}.
\end{aligned}
\]
An internal cut \(c\in\{1,\ldots,n-1\}\) is crossed by \([i,j)\) exactly if \(i<c<j\). Equivalently, the occurrence contains at least one letter on each side of the cut.

## Proof
**1. Unique periodic phases for mixed factors.** The primitive period \(P=0^a1^b\) contains one \(01\) transition and one \(10\) transition per cycle. Every factor containing both symbols therefore occurs at just one residue class of starting positions modulo \(p\): the location of its first symbol change determines that residue. In particular, if a mixed factor is a border of a longer word cut from \(W\), the two corresponding occurrences are shifted by a positive multiple of \(p\).

**2. Reduction of a closed mixed occurrence.** Any border witnessing closedness is either unary or mixed. If it is mixed, its two occurrences must begin exactly \(p\) positions apart: at larger separations the intermediate period-aligned copy would give a third occurrence. The whole closed factor has the form \(W[i:i+p+t]\) for a mixed border of length \(t\). Extending to the right, if possible, yields the same two period-aligned copies of the enlarged mixed border of length \(t+1\), with no third copy because a mixed border occurs in only one phase per period. The same holds for an available left extension. Hence a mixed-border closed occurrence cannot be maximal unless it is the entire \([0,n)\).

If a closed mixed factor is witnessed by a unary border \(x^t\), no complete intermediate \(x\)-run may lie between its prefix and suffix occurrences: such a run would contain another \(x^t\). The two border occurrences must therefore lie in *successive* \(x\)-runs, indexed \(r,r+2\) for some \(r\). The border occurs exactly twice only when the factor begins with precisely the last \(t\) copies of \(x\) in its first run and ends with precisely the first \(t\) copies of \(x\) in the next, yielding \([s_r+\ell_r-t,s_{r+2}+t)\) for \(1\le t\le\ell_r\). When \(t=\ell_r\), the interval is extendible: for \(x=0\), append the next \(1\) on the right, and for \(x=1\), prepend the preceding \(0\) on the left. The extension has a mixed border repeated at period \(p\) and is closed. Such adjacent letters are available because of the run index restriction.

For \(t<\ell_r\), both one-letter extensions exist and each extends an end run of \(x\) from length \(t\) to \(t+1\); the other end run still has length \(t\). Any unary border then has length \(v\le t\) and occurs at least twice in the enlarged run and at least once in the other. If a mixed border witnessed closedness of the extension, its two starts would have to differ by exactly \(p\), as shown above. Since \(s_{r+2}=s_r+p\), the extended factor has length \(p-\ell_r+2t+1\); a border with starts \(p\) apart would have length \(2t+1-\ell_r\le t\). If positive, it would lie wholly in the initial \(x\)-run, so could not be mixed. Thus neither extension is closed, and these are precisely the mixed proper MCS occurrences.

**3. Unary factors and the full word.** A unary factor extends while remaining unary and hence closed until it fills a maximal constant run. A full run is not extendible to a closed word because either available one-letter extension introduces exactly one occurrence of the opposite symbol. Finally, \(W\) is closed: its border \(P^{k-1}\) occurs exactly at positions \(0\) and \(p\), and the full interval cannot extend. Its occurrence is distinct from all run and bridge occurrences.

**4. Counts.** There are \(2k\) runs, and the bridges contribute
\[
(k-1)(a-1)+(k-1)(b-1)=(k-1)(p-2).
\]
Adding the full word yields \(K=2k+(k-1)(p-2)+1=(k-1)p+3\).

**5. Exact gap maximum.** For a fixed cut, there are at most \(a-1\) zero-bridges and at most \(b-1\) one-bridges crossing it. To see this, if the cut lies outside an \(x\)-run, only one pair of neighboring \(x\)-runs can have a bridge crossing that cut, and it has \(\ell_x-1\) possible bridge lengths. If the cut lies strictly inside an \(x\)-run at offset \(u\), bridges from its preceding pair contribute at most \(\ell_x-1-u\) and bridges from its following pair contribute at most \(u-1\), totaling \(\ell_x-2\). If the cut coincides with an \(x\)-run boundary, at most one neighboring bridge family contributes, bounded by \(\ell_x-1\). The full-word MCS crosses every internal cut. If the cut lies inside a run, the unique pure-run MCS crosses too, but its same-letter bridge contribution is smaller by one; if at a run boundary, no pure-run MCS crosses. In either case the crossing count is bounded by \(1+(a-1)+(b-1)=p-1\), with the extra pure-run contribution compensated by the smaller same-letter bridge count.

At every cut \(c=mp\), \(1\le m<k\), the full interval crosses, no pure run crosses, and for both letters all \(a-1\) and \(b-1\) bridge intervals between neighboring runs across the cut cross. Therefore the count is exactly \(1+(a-1)+(b-1)=p-1\). This proves the sharp cut claim.

## Verification
Two independently implemented, standalone Python 3 programs are included. `verify_bruteforce.py` constructs all factors, tests every possible border occurrence and one-character extension, and checks 97 parameter triples with \(1\le a,b\le5\), \(2\le k\le5\), and \(n\le40\). `verify_borders.py` independently groups occurrences by factor, tests border conditions via direct search, and checks 48 small triples; it also directly checks the predicted cut counts for 4,335 further parameter triples with \(1\le a,b\le17\), \(3\le k\le17\). Recorded outputs `bruteforce.log` and `borders.log` reproduce the results. These finite checks support, but are not substitutes for, the symbolic proof.

## Relationship to prior work
Badkobeh, De Luca, Fici and Puglisi introduced MCS and proved general global bounds and an enumeration algorithm. In the run-length-encoded treatment of Umezaki et al., Section 4, the Type 1 and 5 occurrences are maximal repetitions, and Lemma 4 gives exact intervals of valid unary-border lengths for pairs of runs. For a fixed symbol in our family, all its runs have the same length \(\ell\), so only successive such runs yield a nonempty admissible interval. The common next letter for zero-runs, or common previous letter for one-runs, rules out \(t=\ell\) by that lemma, leaving exactly our bridge intervals. The mixed-phase observation in the proof excludes proper mixed-border MCS occurrences. The occurrence list and total count are thus a direct family specialization using periodicity; we give a self-contained derivation for use in the cut analysis. The previously published four-run endpoint classification already gives the equal-block \(k=2\) list and total count \(a+b+3\).

Faro et al. consider internal queries in arbitrary words, giving a general cut-crossing bound and a dense binary construction (Theorem 12, Corollary 13 and Proposition 14). The sharp result here is instead the exact bound \(a+b-1\) for every word of this period family, with equality at all boundaries between full copies. It uses the loss of one eligible same-symbol bridge when a run itself crosses the cut. No improvement to the unrestricted worst-case bound is claimed.

## Limitations
The explicit formulas apply to equal successive two-run blocks, not arbitrary alternating runs. The cut theorem is an exact maximum *within this family*, not an upper bound for arbitrary binary words. The relevant classification and cut-bound passages of the two 2026 manuscripts are compared above; this comparison does not establish absolute priority against differently formulated or unindexed results.

## References
- G. Badkobeh, A. De Luca, G. Fici and S. J. Puglisi, *Maximal Closed Substrings*, SPIRE 2022. Author-accepted full text: https://openaccess.city.ac.uk/id/eprint/31990/1/Maximal_Closed_Substrings.pdf
- H. Umezaki, H. Shibata, Y. Nakashima and S. Inenaga, *Compact Enumeration of Maximal Closed Substrings in Run-Length Encoded Strings*, first submitted July 3, 2026, https://arxiv.org/abs/2607.02838
- S. Faro, F. P. Marino and A. Pavone, *Internal Queries for Maximal Closed Substrings*, first submitted November 8, 2026, https://arxiv.org/abs/2611.11552
- *Exact maximal-closed-substring spectrum for binary four-run words*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-exact-maximal-closed-substring-spectrum-for-binary-four-run-word--5387a5bb0a25
