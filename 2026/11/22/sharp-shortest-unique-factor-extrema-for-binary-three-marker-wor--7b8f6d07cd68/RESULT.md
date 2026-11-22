# Sharp shortest-unique-factor extrema for binary three-marker words

## Finding

For a finite binary word \(w\), a factor is a **contiguous** substring. An occurrence is unique if the corresponding factor occurs at exactly one starting position in \(w\); overlapping occurrences count separately. Write \(\ell(w)\) for the minimum length of a nonempty uniquely occurring factor. The whole word is always unique, so this quantity exists.

**Theorem.** Let \(n\geq5\) and let \(\mathcal B_{n,3}\) denote the binary words of length \(n\) containing exactly three ones. Set \(m=\lfloor n/4\rfloor\). Then

\[
\max_{w\in\mathcal B_{n,3}}\ell(w)=n-2m.
\]

Every maximizing word, and no other word, is of the form

\[
w=0^a1\,0^m1\,0^m1\,0^d,
\qquad a,d\in\mathbb Z_{\geq0},\quad a,d\leq m,
\quad a+d=n-3-2m.
\]

Consequently, with \(s=n-3-2m\), the number of maximizers is precisely

\[
E(n)=\min(m,s)-\max(0,s-m)+1.
\]

For \(n\geq12\), putting \(r=n-4\lfloor n/4\rfloor\in\{0,1,2,3\}\) gives \(E(n)=4-r\). For lengths \(5\leq n\leq11\), the counts, in increasing order, are \(1,2,1,2,3,2,1\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); the weight-three restriction refers to the number of ones. Words are linear, not circular, and are not terminated by an additional marker. The global unique-factor length \(\ell(w)\) differs from the shortest unique substring required to cover a prescribed position or interval. Uniqueness is by *occurrence*, not by factor type among the set of distinct factors. No assumption is made that gaps are positive: adjacent ones are permitted.

Every such word has the unique representation

\[
w=0^a1\,0^b1\,0^c1\,0^d,
\qquad a,b,c,d\geq0,
\quad a+b+c+d=n-3.
\]

## Proof

**Lemma (equal interior gaps).** If \(b=c=t\) and \(0\leq a,d\leq t\), then

\[
\ell(0^a1\,0^t1\,0^t1\,0^d)=a+d+3.
\]

*Lower bound.* Every all-zero factor occurs at least twice, since both interior zero runs have length \(t\), which is at least as large as either exterior run; if \(t=0\), no all-zero factor occurs. The one-letter factor `1` occurs three times.

Every factor containing exactly one `1` is \(0^p1\,0^q\). Its three possible central-one positions have left/right zero capacities \((a,t)\), \((t,t)\), and \((t,d)\). Any such factor occurring at the first or last `1` also occurs at the middle `1`. To occur only at the middle one, it must have \(p>a\) (excluding the first one) and \(q>d\) (excluding the last one); hence its length is at least \(a+d+3\).

Every factor containing exactly two ones has the form \(0^p1\,0^t1\,0^q\) and can align with either of the two consecutive-one pairs. To occur uniquely at the first pair, it must extend farther right than the third one's external zero run, i.e. \(q>d\), since its left zero capacity is at most \(a\leq t\). Its length is therefore at least \(t+2+d+1\geq a+d+3\). At the second pair it instead requires \(p>a\), giving length at least \(t+2+a+1\geq a+d+3\). Finally, any factor with three ones contains both interior gaps and has length at least \(2t+3\geq a+d+3\). This exhausts all possible numbers of ones in a factor.

*Upper bound.* If \(a<t\) and \(d<t\), the factor \(0^{a+1}1\,0^{d+1}\), centered at the middle `1`, is unique and has length \(a+d+3\). If \(a<t\) and \(d=t\), the unique factor is \(0^{a+1}1\,0^t1\), aligned with the second pair; if \(a=t\) and \(d<t\), use \(1\,0^t1\,0^{d+1}\), aligned with the first pair. If \(a=d=t\), the factor \(1\,0^t1\,0^t1\) is unique. In all four cases the length is \(a+d+3\). This proves the lemma, including \(t=0\).

Now write \(n=4m+r\), where \(0\leq r\leq3\). Because \(n\geq5\), we have \(m\geq1\) and \(m+r\geq2\). Put \(M=n-2m=2m+r\).

**Case 1: \(b\ne c\).** The factors \(1\,0^b1\) and \(1\,0^c1\) are both unique: a substring with precisely two ones must use one of the two neighboring-one pairs, and their separating gaps differ. Hence \(\ell(w)\leq\min(b,c)+2\). Were \(\ell(w)\geq M\), we would have \(\min(b,c)\geq M-2\), so since the two gaps differ,

\[
n-3\geq b+c\geq2M-3=4m+2r-3.
\]

Comparison with \(n-3=4m+r-3\) forces \(r=0\) and equality everywhere. Thus \(a=d=0\) and \(\{b,c\}=\{2m-2,2m-1\}\). The factor \(0^{2m-1}\) occurs just once, in the longer interior run, so \(\ell(w)\leq2m-1=M-1\), a contradiction. Therefore \(\ell(w)<M\) whenever \(b\ne c\).

**Case 2: \(b=c=t\) and \(a>t\) or \(d>t\).** In the former case \(0^{t+1}1\) occurs only at the first `1`; in the latter case \(1\,0^{t+1}\) occurs only after the last `1`. In either case \(\ell(w)\leq t+2\). Because one exterior gap is at least \(t+1\), the length equation gives \(3t+4\leq n\), whence

\[
\ell(w)\leq t+2\leq(n+2)/3<n-2m=M.
\]

The last strict inequality follows from \(n-3m=m+r>1\).

**Case 3: \(b=c=t\) and \(a,d\leq t\).** The lemma gives \(\ell(w)=a+d+3=n-2t\). Since \(a+d\leq2t\), we have \(n-3\leq4t\), and thus

\[
t\geq\lceil(n-3)/4\rceil=\lfloor n/4\rfloor=m.
\]

It follows that \(\ell(w)\leq n-2m=M\), with equality exactly when \(t=m\). Every equality case obeys the displayed restrictions on \(a,d\), and conversely the lemma shows that every such choice attains \(M\). This proves the maximum and its full equality characterization.

The integer parameter \(a\) for an equality case ranges from \(\max(0,s-m)\) to \(\min(m,s)\), inclusive, proving the formula for \(E(n)\). If \(n\geq12\), then \(m\geq3\) and \(s=2m+r-3\) lies between \(m\) and \(2m\), which yields \(E(n)=4-r\). The remaining seven lengths are obtained directly from the same integer interval formula. \(\square\)

## Verification

The companion standalone program `sus_three_verifier.py` computes exact factor multiplicities, without using the proof, for all \(7{,}315\) three-one words of lengths \(3\) through \(21\), and compares the answer with a separate bounded-gap candidate computation. The sharp upper bound and the complete equality set are exhaustively checked at lengths \(5\) through \(21\). For lengths \(22\) through \(300\), it checks all predicted maximizing gap vectors and another \(8{,}370\) seeded gap vectors against the bounded-gap computation. The captured output is `sus_three_verification_output.txt`. All checks pass. These finite computations are sanity checks, not substitutes for the proof above.

Reproduction: run `python3 sus_three_verifier.py` using Python 3 and the standard library. No network access, specialized solver, external certificate, or auxiliary input file is required.

## Relationship to prior work

Charalampopoulos, Mohamed, Pissis, Verbeek, and Zuba (first public version 6 May 2026, arXiv:2605.04826v1) define the same global shortest-unique-substring invariant and give an improved general packed-string algorithm. Their stated results concern computational complexity, not the maximum of this invariant over the fixed-weight-three class or its extremizing words. Mieno and coauthors' earlier unique-substring work treats point/interval queries, minimal unique substrings, and dynamic-window algorithms; these operations differ from the present fixed-content global extremum. Other published fixed-content studies concern shortest unique factors of two-marker sources or the *number* of minimal unique factors, neither of which implies this three-marker length extremum. The new statement is the sharp formula and equality classification, not the algorithmic ability to evaluate \(\ell(w)\) on a given input.

## Limitations

The theorem concerns exactly three ones and global occurrence uniqueness. It does not determine the complete shortest-unique-factor distribution across all three-one words or the position-constrained SUS problem. It makes no priority claim against inaccessible or unindexed results. The verification scripts provide finite checks; an independent scientific audit has not been performed.

## References

1. P. Charalampopoulos, M. Mohamed, S. P. Pissis, H. Verbeek, and W. Zuba, *Faster Algorithms for Shortest Unique or Absent Substrings*, arXiv:2605.04826v1, 6 May 2026. https://arxiv.org/html/2605.04826v1
2. T. Mieno, Y. Fujishige, Y. Nakashima, S. Inenaga, H. Bannai, and M. Takeda, *Computing Minimal Unique Substrings for a Sliding Window*, Algorithmica 84 (2022), published online 20 August 2021. https://doi.org/10.1007/s00453-021-00864-1
3. T. Mieno et al., *Space-Efficient Algorithms for Computing Minimal/Shortest Unique Substrings*, Theoretical Computer Science 845 (2020), 230–242; preprint arXiv:1905.12854. https://arxiv.org/abs/1905.12854
