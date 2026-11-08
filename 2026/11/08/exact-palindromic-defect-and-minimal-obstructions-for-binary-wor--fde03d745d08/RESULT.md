# Exact palindromic defect and minimal obstructions for binary words with at most six runs

## Finding

For a finite binary word \(w\), write \(\operatorname{Pal}^{+}(w)\) for its **set of distinct nonempty palindromic contiguous factors** and define the palindromic defect
\[
D(w)=|w|-|\operatorname{Pal}^{+}(w)|.
\]
A word is *rich* when its defect vanishes. We give a quantitative complete classification for words with at most six runs, meaning maximal nonempty constant-letter blocks. In the following, all displayed run lengths are positive integers and \([P]\) equals one if proposition \(P\) holds and zero otherwise. Set \(t_+=\max(0,t)\).

Every binary word with at most four runs is rich. Up to exchange of the two symbols, a word with five runs is \(w_5=0^a1^b0^c1^d0^e\), and with six runs is \(w_6=0^a1^b0^c1^d0^e1^f\). Their defects are exactly
\[
\begin{aligned}
D(w_5)&=[b\ne d]\bigl(\min(a,e)-c\bigr)_+,\\
D(w_6)&=[b\ne d]\bigl(\min(a,e)-c\bigr)_+
+[c\ne e]\bigl(\min(b,f)-d\bigr)_+.
\end{aligned}
\]
Thus the defect of a six-run word is the **sum** of the defects of its first and last five-run factors formed by whole runs.

Call \(w\) *minimal non-rich* if \(D(w)>0\) but all proper contiguous factors are rich. Among **all** binary words with at most six runs, the minimal non-rich words are precisely, up to exchanging the bits,
\[
0^{c+1}1^b0^c1^d0^{c+1},
\qquad b,c,d\ge1,\quad b\ne d.
\]
Every member has defect one. If \(m_n\) counts these words of length \(n\), with both possible initial bits distinguished, then
\[
\sum_{n\ge0}m_n z^n
=\frac{4z^8}{(1-z)^2(1+z)(1-z^3)}.
\]
This is a restricted bounded-run enumeration, not a generating function for *all* minimal non-rich binary words.

The bound on the number of runs is sharp. The seven-run word `010110010` has defect one and every proper factor is rich, despite both overlapping six-run prefix and suffix being rich.

## Assumptions and scope

All statements are for finite words over exactly the two symbols `0` and `1`. Run lengths are strictly positive. Bit complementation preserves distinct palindromic factor counts and defect; it is therefore sufficient to start with a zero-run. Distinct factors are counted as **different strings**, not by occurrences or start positions. A word is minimal non-rich relative to all its proper factors, not merely relative to the bounded-run subclass.

## Proof

**Step 1: classify possible palindromes.** A nonempty palindrome in a binary word of at most six runs can meet only one, three or five whole/partial runs. If it meets three runs, its two exterior runs must have the same letter and the entire middle run is contained in the palindrome. If it meets five runs, the complete second, third and fourth runs are inside it, forcing equality of the second and fourth run lengths. A six-run palindrome cannot meet all six runs because its two endpoints would have different symbols. These cases partition the *distinct palindromic strings* by their number of runs and center run.

For \(w_6\), the one-run palindromes contribute
\(\max(a,c,e)+\max(b,d,f)\).
The three-run palindromes beginning with zero contribute
\[
\min(a,c)+\min(c,e)-[b=d]\min(a,c,e),
\]
since the two families have the same middle string precisely when \(b=d\), and then overlap for exactly \(\min(a,c,e)\) exterior lengths. Likewise the three-run palindromes beginning with one contribute
\[
\min(b,d)+\min(d,f)-[c=e]\min(b,d,f).
\]
The five-run palindromes centered on the third run are \(0^i1^b0^c1^d0^i\), occurring if and only if \(b=d\), with \(1\le i\le\min(a,e)\). Those centered on the fourth run are \(1^i0^c1^d0^e1^i\), occurring if and only if \(c=e\), with \(1\le i\le\min(b,f)\). Hence the exact number of distinct nonempty palindromic factors is
\[
\begin{aligned}
|\operatorname{Pal}^{+}(w_6)|={}&\max(a,c,e)+\max(b,d,f)\\
&+\min(a,c)+\min(c,e)-[b=d]\min(a,c,e)\\
&+\min(b,d)+\min(d,f)-[c=e]\min(b,d,f)\\
&+[b=d]\min(a,e)+[c=e]\min(b,f).
\end{aligned}
\]
There are no duplicate palindromes across these categories: their run counts or their interior letter-run patterns differ. The analogous five-run count is obtained by removing the final one-run and its associated three- and five-run families. Directly counting the one- and three-run palindromes shows every word of at most four runs has as many distinct nonempty palindromes as letters.

**Step 2: simplify the defect.** For positive integers \(x,y,z\), sorting these three numbers or splitting into cases according to whether \(y\ge\min(x,z)\) gives the elementary identity
\[
x+y+z-\max(x,y,z)-\min(x,y)-\min(y,z)
=\bigl(\min(x,z)-y\bigr)_+.
\]
Substitute the palindrome count from Step 1 into \(D(w_6)=a+b+c+d+e+f-|\operatorname{Pal}^{+}(w_6)|\), apply the identity to \((a,c,e)\) and \((b,d,f)\), and use
\[
\min(a,e)-\min(a,c,e)=(\min(a,e)-c)_+,
\]
with its interchanged-symbol analogue. When \(b=d\), the candidate contribution from \((a,c,e)\) cancels exactly; when \(b\ne d\), it remains. The second contribution behaves identically according to \(c=e\). This yields precisely the two displayed defect formulas. For five runs only the first contribution is present.

**Step 3: minimal non-rich words.** Every proper factor of a rich word is rich (the factorial property; alternatively apply the longest-palindromic-suffix characterization). Thus it is sufficient to test the two immediate length-one-shorter factors of a minimal-non-rich candidate.
If a five-run word is not rich, then \(b\ne d\) and \(a,e>c\). Removing its initial letter leaves a five-run word with first run length \(a-1\), and removing its final letter leaves one with last run length \(e-1\). For *both* to become rich, the exact five-run formula forces \(a-1\le c\) and \(e-1\le c\); hence \(a=e=c+1\). The converse is immediate: such a word has defect one while both immediate proper factors have defect zero, so every proper factor is rich. A non-rich six-run word has at least one non-rich five-whole-run factor, because its defect is their sum; therefore it cannot be minimal. The words of at most four runs are rich.

**Step 4: enumerate.** For a fixed initial symbol, \(c\ge1\) contributes \(z^{3c+2}\), while the ordered pair \((b,d)\) of positive unequal integers contributes
\[
\sum_{\substack{b,d\ge1\\b\ne d}}z^{b+d}
=\frac{z^2}{(1-z)^2}-\frac{z^2}{1-z^2}
=\frac{2z^3}{(1-z)^2(1+z)}.
\]
Multiplying by two for the initial symbol choices and by \(\sum_{c\ge1}z^{3c+2}=z^5/(1-z^3)\) gives the asserted generating function.

**Step 5: sharpness at seven runs.** The seven-run word `010110010` has precisely the eight distinct nonempty palindromic factors
`0`, `1`, `00`, `11`, `010`, `101`, `0110`, `1001`.
It has nine letters and defect one. Its immediate proper prefix `01011001` and suffix `10110010` each have six runs and zero defect by the six-run formula, so it is a seven-run minimal non-rich word. Consequently, the six-run local-additivity criterion cannot be extended without extra hypotheses.

## Verification

Run `python3 check_pal_defect.py` with Python 3; the complete standalone source accompanies this result. It independently enumerates all distinct palindromic substring strings and compares their count with the formulas. Tested exhaustive run-length profiles for numbers of runs \(1,2,3,4,5,6\) were respectively \(8,64,512,2401,16807,15625\); an additional \(1,200\) larger seeded profiles passed. It checked \(180\) parameterized five-run minimal non-rich words, exhaustive binary minimal-obstruction counts through length twelve, and the explicit seven-run counterexample. The bounded-run minimal counts at lengths \(1\) to \(12\) are
\[
0,0,0,0,0,0,0,4,4,8,12,16.
\]
These finite tests corroborate the formulas but are not proofs of the unbounded integer-parameter statements; Steps 1–5 supply those proofs.

## Relationship to prior work

Pelantová and Starosta (2017) formulate characterization of minimal non-rich words as a problem, establish general compatibility conditions, and exhibit the length-eight non-rich example `11010011`. The present classification concerns only the bounded-run subclass, not the unrestricted problem; its shortest examples and richness-factorial property agree with that work. Guo, Shallit, and Shur (2015 preprint linked to a 2016 paper) prove run-length **sufficient conditions** for richness and an enumeration lower bound. Their inspected preprint, especially its richness section, does not state the exact six-run *numerical defect*, the local additivity, or the minimal-obstruction length enumerator. The journal article's abstract mentions further run-length characterization; a possible implication from an uninspected final version remains a literature risk. Currie, Mol, and Rampersad (2019) study repetition thresholds in infinite binary rich words, a different scope. No assertion of exhaustive bibliographic novelty is made.

## Limitations

The theorem is restricted to a binary alphabet and at most six alternating runs. The generating function counts minimal forbidden words *within that run-count bound* only. The seven-run example proves sharp failure of a naive extension but does not classify seven-run defects. Computational verification is finite. Literature inspection of the earlier run-length work includes an accessible 2015 preprint; the 2016 final journal version could contain additional statements not independently checked here. Self-review is not independent mathematical validation.

## References

1. E. Pelantová and Š. Starosta, *On Words with the Zero Palindromic Defect*, first arXiv version 2017-08-23, https://arxiv.org/abs/1708.06911 .
2. C. Guo, J. Shallit, and A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, first arXiv version 2015-03-31, https://arxiv.org/abs/1503.09112 ; linked final article *Palindromic Rich Words and Run-Length Encodings*, *Information Processing Letters* 116 (2016), 735–738, https://doi.org/10.1016/j.ipl.2016.07.001 .
3. J. D. Currie, L. Mol, and N. Rampersad, *The Repetition Threshold for Binary Rich Words*, first arXiv version 2019-08-08, https://arxiv.org/abs/1908.03169 .
