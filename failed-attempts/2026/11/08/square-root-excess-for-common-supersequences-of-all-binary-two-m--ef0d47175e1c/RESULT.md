# Square-root excess for common supersequences of all binary two-marker words

## Finding
For an integer \(k\ge3\), let \(\mathcal F_k=\{0^a1\,0^b1\,0^c:a,b,c\in\mathbb Z_{\ge0},\ a+b+c=k-2\}\), and let \(\ell_k\) be the minimum length of a binary word containing every member of \(\mathcal F_k\) as a **scattered subsequence** (not necessarily as a factor). Then
\[
\boxed{k+2\bigl(2k(k-1)\bigr)^{1/4}-4\ \le\ \ell_k\ \le\ k+\min_{h\in\mathbb Z_{\ge1}}\left(2h+\left\lceil\frac{k-2}{h}\right\rceil-1\right).}
\]
In particular,
\[
\ell_k-k=\Theta(\sqrt{k}),\qquad
2\,2^{1/4}\le \liminf_{k\to\infty}\frac{\ell_k-k}{\sqrt{k}}
\le \limsup_{k\to\infty}\frac{\ell_k-k}{\sqrt{k}}\le 2\sqrt2.
\]
The lower estimate follows from a triangular covering inequality that applies to **each** possible supersequence. The upper estimate is realized by a specified family of periodically spaced markers. The leading constant and exact length \(\ell_k\) for general \(k\) are not determined.

## Assumptions and scope
All words are finite and over the fixed alphabet \(\{0,1\}\). A subsequence can skip letters while retaining order. Every target has exactly two occurrences of \(1\) and length exactly \(k\); a proposed supersequence can have any number of either letter. All assertions hold for every integer \(k\ge3\). Define \(t=k-2\). There are exactly \(\binom{k}{2}\) distinct targets, in bijection with the weak compositions \((a,b,c)\) of \(t\) into three parts.

## Proof
**1. Coverage by one pair of markers.** Let \(W\) be a common supersequence, containing \(r\ge2\) ones and \(Z\) zeros. Necessarily \(Z\ge t\). Put \(q=Z-t\ge0\). Choose positions of two distinct ones in increasing order. Let \(A,B,C\) be the numbers of zeros, respectively, strictly before the first chosen one, between the two chosen ones, and strictly after the second chosen one. Thus \(A+B+C=Z\). The targets embedded using *this selected pair of ones* are exactly the triples satisfying \(0\le a\le A\), \(0\le b\le B\), \(0\le c\le C\), and \(a+b+c=t\). The map \((a,b,c)\mapsto(A-a,B-b,C-c)\) injects this set into the weak compositions of \(q\) into three parts. Therefore a given pair of ones covers no more than \(\binom{q+2}{2}\) targets.

There are \(\binom r2\) pairs of ones and \(\binom k2\) required targets. Every target must be covered by at least one pair, even when multiple pairs embed the same target. The union bound gives the exact necessary inequality
\[
\boxed{\binom r2\binom{q+2}{2}\ge\binom k2,\quad\text{equivalently}\quad r(r-1)(q+1)(q+2)\ge2k(k-1).}
\]
Now \(r(r-1)\le r^2\) and \((q+1)(q+2)\le(q+2)^2\), so \(r(q+2)\ge\sqrt{2k(k-1)}\). By arithmetic--geometric means,
\[
r+q+2\ge2\sqrt{r(q+2)}\ge2(2k(k-1))^{1/4}.
\]
Since \(|W|=Z+r=k-2+q+r\), this proves the lower bound on \(\ell_k\).

**2. Explicit covering construction.** Fix any integer \(h\ge1\), let \(r=\lceil t/h\rceil\), and set \(e=t-(r-1)h\), so \(1\le e\le h\). Define
\[
W_{k,h}=(0^h1)^{r+1}0^e.
\]
Its ones occur at zero-count coordinates \(h,2h,\dots,(r+1)h\), and its total number of zeros is \(Z=(r+1)h+e=t+2h\). Therefore its length is
\[
|W_{k,h}|=t+2h+r+1=k+2h+\left\lceil\frac{k-2}{h}\right\rceil-1.
\]
For any target \(0^a1\,0^b1\,0^c\) with \(a+b+c=t\), select the \(i\)-th one and then the \(j\)-th one of \(W_{k,h}\), where
\[
i=\max\{1,\lceil a/h\rceil\},\qquad j=i+\max\{1,\lceil b/h\rceil\}.
\]
Here \(1\le i<j\le r+1\): if both \(a,b>0\), use \(\lceil a/h\rceil+\lceil b/h\rceil\le\lceil(a+b)/h\rceil+1\le r+1\); the cases with either zero give the same bound directly. There are \(ih\ge a\) zeros before the selected first one and \((j-i)h\ge b\) zeros between the pair. Moreover, \(ih\le a+h\) and \((j-i)h\le b+h\), so \(jh\le a+b+2h\). Hence there are \(Z-jh\ge t-(a+b)=c\) zeros after the selected second one. Thus every target is indeed a subsequence. Minimizing over \(h\) proves the displayed upper bound.

**3. Asymptotic consequence.** The lower estimate gives
\[
\liminf_{k\to\infty}(\ell_k-k)/\sqrt{k}\ge 2\,2^{1/4}.
\]
For \(h=\lceil\sqrt{(k-2)/2}\rceil\), the upper estimate yields \(\ell_k\le k+2\sqrt{2(k-2)}+2\), giving the upper asymptotic constant. Both constants are strictly positive and finite; hence the excess over the target length is exactly of square-root order.

## Verification
The standalone `verify.py` checks the construction by direct subsequence matching for all \(3\le k\le24\) over several spacings; it checks the exact length/zero counts and construction parameters for larger inputs. For all binary candidate words of length at most eight, it compares the three-gap pair-coverage criterion to direct subsequence recognition, and exhaustively checks the pair-counting bound. It additionally exhausts short common-supersequence minima for \(3\le k\le7\). These finite checks are confirmations, **not** the justification of the infinite claims; the preceding argument establishes those claims without computer assistance. Execute with Python 3 and no dependencies using `python3 verify.py`.

## Relationship to prior work
Clifford, Gotthilf, Lewenstein and Popa (arXiv:1004.0424, initially public 2010-04-03) investigate resource-restricted common supersequences and approximation/hardness, rather than this complete fixed-content input family. Lagoutte and Tavenas (arXiv:1309.0422, initially public 2013-09-02) highlight that shortest-common-supersequence complexity can persist even for **arbitrary chosen subsets** of equal-length binary words with exactly two nonconsecutive ones. Their related one-marker spacing lemma exhibits the square-root tradeoff for a different single-marker input family; it does not provide the present *two-marker triangular pair-packing inequality*, its stronger \(2\,2^{1/4}\) asymptotic lower constant, or the displayed all-target construction. Adamson (arXiv:2304.04583) treats words containing **all** words of a given length as subsequences, a more demanding universe with different length behavior. Ma (2025, DOI:10.1186/s12859-025-06336-5) studies balanced target strings, not the sparse two-marker input set. No universal priority assertion beyond these checked comparisons is intended.

## Limitations
The two constants in the asymptotic bounds are different; no sharp limiting constant is claimed. The optimal constructions are not classified. No claim is made for target weight other than exactly two, or for contiguous-factor coverage. Related historical work on arbitrary restricted input sets may contain unindexed statements; the literature comparison is not a proof of absolute uniqueness.

## References
- R. Clifford, Z. Gotthilf, M. Lewenstein and A. Popa, *Restricted Common Superstring and Restricted Common Supersequence*, arXiv:1004.0424 (initial version 2010-04-03), https://arxiv.org/abs/1004.0424.
- A. Lagoutte and S. Tavenas, *The complexity of Shortest Common Supersequence for inputs with no identical consecutive letters*, arXiv:1309.0422 (initial version 2013-09-02), https://arxiv.org/abs/1309.0422.
- D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583 (2023), https://arxiv.org/abs/2304.04583.
- Y. Ma, *Batch optimization for balanced binary sequences and DNA sequences*, BMC Bioinformatics 26, 300 (2025), https://doi.org/10.1186/s12859-025-06336-5.
