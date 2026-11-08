# Exact palindromic defect and sharp defect spectrum of binary five-run words

## Finding
For all positive integers \(a,b,c,d,e\), let \(W=0^a1^b0^c1^d0^e\). Write \(\mathrm{Pal}^+(W)\) for the set of distinct nonempty palindromic contiguous factors of \(W\), and \(D(W)=|W|-|\mathrm{Pal}^+(W)|\) for its palindromic defect. Then
\[
D(W)=\begin{cases}
0,&b=d,\\
\max\{0,\min\{a,e\}-c\},&b\ne d.
\end{cases}
\]
In particular, this five-run word is rich (has defect zero) exactly when \(b=d\) or \(c\ge\min\{a,e\}\). For every integer \(n\ge5\), the *entire* set of defects attained by five-run binary words of length \(n\) is
\[
\bigl\{D(W): W=0^a1^b0^c1^d0^e,\ a,b,c,d,e\ge1,\ |W|=n\bigr\}
=\bigl\{0,1,\ldots,\lfloor(n-6)/2\rfloor\bigr\}
\]
when \(n\ge6\); for \(n=5\) the set is \(\{0\}\). Equivalently, uniformly for \(n\ge5\), the upper endpoint is \(\max\{0,\lfloor(n-6)/2\rfloor\}\). Thus a non-rich binary word with exactly five runs first occurs at length \(8\); one example is \(00101100\), of defect \(1\).

## Assumptions and scope
All factors are *contiguous* and distinct factors are counted once, irrespective of multiplicity. The empty word is palindromic but excluded from \(\mathrm{Pal}^+(W)\). Therefore \(D(W)=|W|+1-(1+|\mathrm{Pal}^+(W)|)\), the standard finite-word defect. All run lengths are positive and the alphabet consists of distinct symbols \(0\) and \(1\). Complementing letters gives the same statement for the other five-run orientation. The spectrum concerns all positive run-length compositions of a fixed total length, not arbitrary binary words.

## Proof
**Complete factor classification.** The palindrome property forces its sequence of letters and hence its run-transition pattern to be symmetric. Every palindromic factor of a five-run word has an even number of transitions, necessarily zero, two, or four. The zero-transition palindromes are precisely \(0^t\) for \(1\le t\le\max\{a,c,e\}\) and \(1^t\) for \(1\le t\le\max\{b,d\}\). With two transitions the only possibilities are
\[
0^t1^b0^t\quad(1\le t\le\min\{a,c\}),\qquad
1^t0^c1^t\quad(1\le t\le\min\{b,d\}),\qquad
0^t1^d0^t\quad(1\le t\le\min\{c,e\}).
\]
The central full run is forced: a palindrome with exactly two transitions must contain the entire single interior run, with matching lengths at the ends. The first and third families coincide exactly for those \(t\le\min\{a,c,e\}\) when \(b=d\); they are disjoint when \(b\ne d\). A palindrome with four transitions must cross all four run boundaries. Hence it must be \(0^t1^b0^c1^d0^t\), which is palindromic exactly when \(b=d\) and \(1\le t\le\min\{a,e\}\). Conversely every displayed word occurs as a factor, so this list is exhaustive.

**Counting.** Put \(X=\max\{a,e\}\) and \(Y=\min\{a,e\}\). If \(b\ne d\), no families overlap, and the preceding list gives
\[
\begin{aligned}
|\mathrm{Pal}^+(W)|
&=\max\{X,c\}+\max\{b,d\}+\min\{a,c\}+\min\{b,d\}+\min\{c,e\}\\
&=X+b+d+c+\min\{Y,c\},
\end{aligned}
\]
using \(\max\{X,c\}+\min\{X,c\}=X+c\) and \(\min\{a,c\}+\min\{e,c\}=\min\{X,c\}+\min\{Y,c\}\). As \(|W|=X+Y+b+c+d\), its defect is \(Y-\min\{Y,c\}=\max\{0,Y-c\}\).

If \(b=d\), subtract the duplicate two-transition factors and add the four-transition factors. Therefore
\[
\begin{aligned}
|\mathrm{Pal}^+(W)|
&=\max\{X,c\}+b+\min\{a,c\}+b+\min\{c,e\}
-\min\{Y,c\}+Y\\
&=\max\{X,c\}+2b+\min\{X,c\}+Y\\
&=X+c+2b+Y=|W|.
\end{aligned}
\]
This proves the defect formula, including all parameter equalities and boundaries.

**Minimality of the five-run setting.** Every binary word with at most four runs has defect zero. For four runs \(0^p1^q0^r1^s\), the distinct nonempty palindromes are unary words and two-transition words only, counted by \(\max\{p,r\}+\max\{q,s\}+\min\{p,r\}+\min\{q,s\}=p+q+r+s\). The case of one, two, or three runs follows by the same shorter transition classification (or by deleting an endpoint run from this argument). Thus the first possible positive defect at a prescribed run count indeed occurs for five runs.

**Sharp fixed-length spectrum.** If \(D(W)=k>0\), the formula implies \(b\ne d\), \(a\ge k+c\), \(e\ge k+c\), \(c\ge1\), and \(b+d\ge3\). Hence \(n=a+b+c+d+e\ge 2k+6\), or \(k\le\lfloor(n-6)/2\rfloor\). Conversely, for any integer \(k\ge1\) with \(2k+6\le n\), the positive run tuple
\[
(a,b,c,d,e)=(k+1,1,1,2,k+1+(n-2k-6))
\]
has total length \(n\) and defect \(k\). For \(k=0\) choose \((a,b,c,d,e)=(n-4,1,1,1,1)\), which has \(b=d\). These constructions give every integer in the stated interval. In particular \(n=5,6,7\) admit only defect zero, and \(n=8\) first admits defect one. This completes the proof. \(\square\)

## Verification
A standalone Python checker, `check_five_runs.py`, independently enumerates all palindromic factors by expanding around character and intercharacter centers, then compares the literal factor set to the classified families and compares computed defects to the formula. It passed all \(6^5=7776\) parameter tuples with every positive run length at most six, as well as all attainable lengthwise spectra for \(5\le n\le30\). This finite check is corroborative, not a proof for unbounded parameters; the case-free transition classification and counting prove the general claim. Execute `python3 check_five_runs.py` in the directory containing the checker.

## Relationship to prior work
The palindromic defect is a standard measure of failure of palindromic richness. Guo, Shallit, and Shur studied sufficient structural conditions and later necessary-and-sufficient run-length conditions for richness; the present richness criterion is a specialization of their general subject and is **not** presented as an independently new Boolean characterization. The new statement is an explicit *numerical* defect formula for every positive five-run composition, together with the exact set of attainable defects at each word length and complete palindrome-family accounting. Kim and Kwon (2026) study palindromic complexity of recurrent low-complexity infinite words; their results do not directly count palindromic defects of these finite run-length words. There is a historical-priority caveat: the complete text of the 2016 Guo–Shallit–Shur paper was not available for comparison, and a specialized quantitative consequence there or elsewhere has not been ruled out.

## Limitations
This result is limited to finite binary words with exactly five positive runs, and to distinct contiguous palindromic factors. It does not describe six or more runs, scattered palindromic subsequences, or arbitrary word classes. The checker covers bounded parameter ranges only. The originality comparison is qualified by the unavailable full text of the closely related 2016 run-length paper; independent mathematical audit and historical-priority confirmation have not been performed.

## References
1. D. H. Kim and S. Kwon, *On the number of palindromic factors of low complexity words*, arXiv:2609.16596, first publicly submitted 2026-09-15. https://arxiv.org/abs/2609.16596
2. C. Guo, J. Shallit, and A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112 (2015). https://arxiv.org/abs/1503.09112
3. C. Guo, J. Shallit, and A. M. Shur, *Palindromic Rich Words and Run-Length Encodings*, Information Processing Letters 116 (2016), 735–738. https://doi.org/10.1016/j.ipl.2016.07.001
