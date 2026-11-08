# Exact circular Abelian-square type spectrum for two isolated marked letters

## Finding

Let \(p,q\geq0\) be integers, let \(w=a^pba^qb\) be read as a circular binary word, and put
\[
n=p+q+2,\qquad r=\min(p,q),\qquad M=\max(p,q),\qquad h=\left\lfloor\frac n2\right\rfloor.
\]
For each \(1\le m\le h\), let \(z_m(w)\) count the *non-equivalent Abelian-square types* of cyclic factors of length \(2m\). Two such factors are equivalent when their half-lengths and the numbers of \(b\)'s in one half agree. Then
\[
\boxed{z_m(w)=\mathbf1_{\{2m\le M\}}+\mathbf1_{\{m\ge\lceil(r+2)/2\rceil\}}.}
\]
Consequently, the total number \(N(w)=\sum_{m=1}^{h}z_m(w)\) satisfies
\[
\boxed{N(w)=n-2-r+\mathbf1_{\{n\text{ even and }r\text{ even}\}}.}
\]
When \(n\) is odd, every half-length \(1\le m\le (n-1)/2\) supports an Abelian-square type, and
\[
N(w)=\frac{n-1}{2}+\frac{|p-q|-1}{2}.
\]
Thus \(N(w)\ge(n-1)/2\), with equality if and only if \(|p-q|=1\). In particular the stronger, termwise property \(z_m(w)\ge1\) holds throughout this two-marked-letter family in odd length; hence every partial-sum inequality \(\sum_{m=1}^{k}z_m(w)\ge k\) holds for \(1\le k\le(n-1)/2\).

## Assumptions and scope

The alphabet is \(\{a,b\}\), the word contains exactly two occurrences of \(b\), and factors are read cyclically, but no factor is allowed to have length exceeding \(n\). An Abelian square is a factor \(uv\), where \(u,v\) are nonempty, have equal length and equal Parikh vectors. A *type* is identified by the pair \((m,|u|_b)\), not by the literal word or its location. Thus this is a count of non-equivalent types, not a count of distinct factors or occurrences. The allowed values \(p=q=0\) and one zero gap are included; the genuinely four-run circular words have \(p,q\ge1\).

## Proof

Fix \(m\) with \(1\le m\le h\). An Abelian square has the same number of occurrences of \(b\) in each half, and \(w\) contains exactly two \(b\)'s in total. Because \(2m\le n\), each circular factor encounters each position at most once. Therefore its half-count of \(b\) can only be \(0\) or \(1\); these give two distinct possible types.

**Zero-mark type.** A factor with no \(b\)'s is a contiguous cyclic block of \(a\)'s of length \(2m\). The two maximal \(a\)-gaps have lengths \(p\) and \(q\), so such a factor exists exactly when \(2m\le M\). This contributes the first indicator.

**One-mark-per-half type.** The two \(b\)'s have oriented cyclic separations \(p+1\) and \(q+1\); the shorter is \(s=r+1\). If an Abelian-square factor has one \(b\) in each half, the two marks occur at positions \(t\) and \(t+s'\) inside the factor, with \(0\le t<m\le t+s'\le2m-1\), for one oriented separation \(s'\in\{p+1,q+1\}\). Necessarily \(r+1\le s'\le2m-1\), or \(m\ge\lceil(r+2)/2\rceil\).

Conversely, assume \(s=r+1\le2m-1\). Start a circular factor so that the first mark is at zero-based offset \(t=\max(0,m-s)\) and the other mark, at oriented distance \(s\), lies at offset \(t+s\). If \(s\ge m\), then \(t=0\) and \(m\le t+s\le2m-1\). If \(s<m\), then \(t=m-s\) belongs to \([0,m-1]\) and \(t+s=m\). In both cases the first mark is in the first half and the second in the second half. Since \(2m\le n\), no mark is encountered twice. Hence each half contains exactly one \(b\), and the factor is an Abelian square. This proves the second indicator and the displayed formula for \(z_m\).

Put \(\ell=\lfloor M/2\rfloor\) and \(t_0=\lceil(r+2)/2\rceil\). The zero-mark type occurs exactly at \(m=1,\ldots,\ell\), and the one-mark type occurs exactly at \(m=t_0,\ldots,h\). Since \(r\le M\), \(t_0\le h\). Thus
\[
N(w)=\ell+h-t_0+1
=\left\lfloor\frac M2\right\rfloor+\left\lfloor\frac{M+r+2}2\right\rfloor-\left\lceil\frac{r+2}2\right\rceil+1.
\]
Separating the four parities of \((M,r)\) simplifies this to \(M+\mathbf1_{\{M,r\text{ both even}\}}\); since \(M=n-2-r\), this equals the claimed expression \(n-2-r+\mathbf1_{\{n\text{ even and }r\text{ even}\}}\).

If \(n\) is odd, then \(M+r\) is odd, so \(M\ge r+1\). Consequently \(\ell\ge\lfloor(r+1)/2\rfloor=t_0-1\), meaning that the two integer intervals \([1,\ell]\) and \([t_0,h]\) cover every \(m\in[1,h]\). Thus \(z_m\ge1\) termwise, proving the partial-sum inequalities. Also \(n\) odd forces the parity indicator to vanish, so \(N=M\). Substituting \(n=M+r+2\) gives \(N=(n-1)/2+(M-r-1)/2\). Equality is equivalent to \(M-r=1\), which is \(|p-q|=1\).

## Verification

The standalone Python 3 program `verify_two_marks.py` independently enumerates every cyclic length-\(2m\) factor, compares the Parikh counts of its halves, and builds the set of types without using any symbolic shortcut. For all \(3{,}600\) parameter pairs \(0\le p,q<60\), it compared the entire half-length type spectrum to the two-indicator formula, checked the closed total, and checked all odd-length partial-sum inequalities. The program returned `EXACT_TWO_MARKS_OK 3600 parameter pairs; all half-length type sets`. The symbolic proof above, rather than the finite check, establishes the unbounded quantifiers.

## Relationship to prior work

Bhattacharjee (2026, first public version October 22) settles the minimum number of *distinct* Abelian-square factors in circular binary words. Its October 27 revision introduces the count of *non-equivalent types*, states the odd-length lower bound and every-prefix partial-sum inequalities as a conjecture, verifies them by computation to length \(27\), and gives a separate exact formula for the *two-run* family \(a^p b^q\) (Section on non-equivalent squares, Proposition on two runs). The present theorem proves the conjectured inequalities termwise and gives the exact type profile for all two-\(b\)-position words \(a^pba^qb\), including four-run cases \(p,q\ge1\) not covered by that two-run proposition. Its boundary subfamilies \(p=0\) or \(q=0\) already reduce to two-run words and are not presented as a new priority claim.

The classical theorem of Fraenkel, Simpson and Paterson provides a universal extremal-length statement for a prescribed small total number of inequivalent weak circular squares; it does not supply these per-half-length spectra. Simpson (2018) surveys the original questions. Fazekas and collaborators (2026) study minima for *linear* binary words rather than the present cyclic type spectrum.

## Limitations

This theorem covers only circular binary words with exactly two \(b\)'s; it does not resolve the general odd-length conjecture for arbitrary binary words. It does not enumerate individual square occurrences or distinct literal square factors. Its claim of originality is relative to the specifically compared accessible literature and mathematical records, not an assertion that no unindexed equivalent result exists.

## References

1. Deep Bhattacharjee, *The minimum number of distinct abelian squares in a binary circular word*, Hexagon `hexagon:2610.00473v1` (October 22, 2026), revised `hexagon:2610.00473v2` (October 27, 2026), https://hexagonmath.org/2610.00473v2 ; openly accessible source: https://hexagonmath.org/api/v1/works/2610.00473v2/source?path=SimpsonCircularAbelianSquares_v2-tex/main.tex .
2. Jamie Simpson, *Solved and unsolved problems about abelian squares*, arXiv:1802.04481 (2018), https://arxiv.org/abs/1802.04481 .
3. A. S. Fraenkel, J. Simpson and M. Paterson, *On weak circular squares in binary words*, Combinatorial Pattern Matching, LNCS 1264 (1997), 76–82, https://doi.org/10.1007/3-540-63220-4_51 .
4. S. Z. Fazekas, A. Mammoliti, R. Mercaş and J. Simpson, *Binary Words Containing Few Abelian Squares*, arXiv:2604.23188 (2026), https://arxiv.org/abs/2604.23188 .
