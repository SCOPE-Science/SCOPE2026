# Exact palindromic complexity and extremizers of three-marker circular words

## Finding

Write \(w=1\,0^a\,1\,0^b\,1\,0^c\) for nonnegative integers \(a,b,c\), and regard \(w\) as a circular binary word of length \(n=a+b+c+3\). Let \(P(w)\) be the number of **distinct nonempty palindromic circular factors of lengths at most \(n\)**: for every length \(1\le \ell\le n\) and every cyclic starting position, take the corresponding contiguous factor, count it if it equals its reversal, and identify equal factor strings.

After sorting the three zero-run gaps as \(0\le a\le b\le c\), the complete formula is

\[
P(w)=
\begin{cases}
2n-c-2,&a<b<c,\\
n+\lfloor(n-1)/2\rfloor,&a=b<c\ \text{or}\ a<b=c,\\
n+\lfloor a/2\rfloor,&a=b=c.
\end{cases}
\]

Consequently, among **all** cyclic binary words of length \(n\ge14\) with exactly three occurrences of the symbol \(1\),

\[
\boxed{M_3(n)=2n-\lceil n/3\rceil-2.}
\]

All maximizers, up to rotation and reversal, are precisely the following *sorted* zero-gap triples; write \(n=3k+r\), where \(r\in\{0,1,2\}\):

\[
\begin{array}{c|l}
r& (a,b,c)\\ \hline
0&(k-2,k-1,k)\\
1&(k-3,k,k+1),\quad(k-2,k-1,k+1)\\
2&(k-2,k,k+1).
\end{array}
\]

Thus there is exactly one dihedral class of maximizing three-marker necklaces when \(n\equiv0,2\pmod3\), and two when \(n\equiv1\pmod3\). This is an optimum **within the weight-three family**, not a proof of the unrestricted circular-palindrome extremal conjecture.

## Assumptions and scope

The alphabet is the labeled set \(\{0,1\}\), with exactly three \(1\)'s and \(n-3\) zeros. Factor strings are literal; reversal is used only to test whether a factor is palindromic. Windows may cross the chosen cut but have length at most one circumference \(n\). Distinct occurrences of the same palindrome count once, and the empty word does not count. The gap tuple of a circular word is defined up to cyclic permutation; reversal also reverses its order. For three gaps these operations generate every permutation, so the sorted triple indexes rotation-and-reversal types. The full formula holds for \(n\ge3\), including zero gaps; the extremal classification is asserted only for \(n\ge14\).

## Proof

**Exhaustive decomposition by number of markers.** A window of length at most \(n\) contains at most the three \(1\)'s. Its palindrome has exactly \(0\), \(1\), \(2\), or \(3\) such markers. We count each type as a set of literal strings.

A zero-marker palindrome must be \(0^j\) with \(1\le j\le c\), contributing exactly \(c\).

A one-marker palindrome must be \(0^j1\,0^j\). The maximum allowed radius at a marker is the smaller of its two incident gaps. Among the three markers, the largest such minimum is the median gap \(b\); hence exactly \(b+1\) different one-marker palindromes occur, with \(0\le j\le b\).

A two-marker palindrome is uniquely of the form
\[
0^j1\,0^t1\,0^j,
\]
where \(t\) is one of the three cyclic gaps, and \(j\) can range from \(0\) to the smaller of the other two gaps. The factors thus obtained never contain the third marker, and their lengths do not exceed \(n\). Palindromes associated with two distinct gap values \(t\) are different strings. If the same gap occurs twice, count its possible \(j\)'s only once, taking the union. Thus the two-marker contributions are \(b+2a+3\) for \(a<b<c\), \(2a+2\) for \(a=b<c\), \(a+b+2\) for \(a<b=c\), and \(a+1\) for \(a=b=c\).

A three-marker palindrome has its central \(1\) exactly halfway between its two other \(1\)'s. Hence two neighboring zero gaps must be equal, and there are no such factors for pairwise distinct gaps. If \(a=b<c\), the three-marker factors are \(0^j1\,0^a1\,0^a1\,0^j\) for \(0\le j\le\lfloor c/2\rfloor\), giving \(\lfloor c/2\rfloor+1\). If \(a<b=c\), the analogous contribution is \(\lfloor a/2\rfloor+1\). If all gaps equal \(a\), there are \(\lfloor a/2\rfloor+1\) distinct factors. These exhaust all possible palindromes, including cases with adjacent markers.

Adding the four contributions gives \(2n-c-2\) for three distinct gaps. For \(a=b=t<c=u\) the total is \(u+3t+\lfloor u/2\rfloor+4=n+\lfloor(n-1)/2\rfloor\). For \(a=t<b=c=u\) it is \(3u+t+\lfloor t/2\rfloor+4=n+\lfloor(n-1)/2\rfloor\). For three equal gaps it is \(n+\lfloor a/2\rfloor\). This proves the complete formula without an enumeration assumption.

**Optimization and equality cases.** For three distinct sorted nonnegative gaps, \(a\le c-2\) and \(b\le c-1\), so
\[
n-3=a+b+c\le3c-3,\qquad c\ge\lceil n/3\rceil.
\]
Therefore \(P(w)\le2n-\lceil n/3\rceil-2\). Equality requires \(c=\lceil n/3\rceil\). Solving the remaining equation \(a+b=n-3-c\) subject to \(0\le a<b<c\) gives exactly the triples displayed in the Finding section, all feasible when \(n\ge14\).

For exactly two equal gaps, let \(R=n+\lfloor(n-1)/2\rfloor\) and \(U=2n-\lceil n/3\rceil-2\). Then
\[
U-R=\lfloor n/2\rfloor-\lceil n/3\rceil-1\ge1
\quad(n\ge14).
\]
For three equal gaps \(a=b=c=t\), the count \(n+\lfloor t/2\rfloor\) is strictly smaller than \(R\), since \(n=3t+3\) and \(\lfloor t/2\rfloor<\lfloor(n-1)/2\rfloor\). Thus no repeated-gap word maximizes for \(n\ge14\). The unique or double maximizing sorted triples above exhaust the equality cases. This completes the proof.

## Verification

Run `python3 verify.py` from the extracted file set. Only the Python standard library is required. The checker independently enumerates literal circular palindrome windows and compares the results with the symbolic formula for **all 7,140 ordered gap triples** of lengths \(3\) through \(36\). It verifies the proposed maximizing triples for every length \(14\) through \(36\), and separately obtains exhaustive literal-window maximizing triples at lengths \(14\) through \(24\) without using the proposed formula. Successful execution prints

`VERIFY_OK words=7140 lengths=3..36 maximizers=14..36 independent_extrema=11`

These checks test implementation and edge cases; the infinite-length statement follows from the preceding exhaustive classification and integer inequalities, not extrapolation from finite data.

## Relationship to prior work

J. Simpson, *Palindromes in circular words* (2014), proves the general strict upper bound \(P(w)<5n/3\), gives the three-marker construction with gaps \(k,k+1,k+2\) for lengths divisible by three, and explicitly poses optimality of related families as a problem. The classification above concerns **only** the three-marker subfamily; it proves exact maxima and **all** gap-pattern equality cases for every length \(n\ge14\), including the other congruence classes. Neither Simpson's general upper bound nor the exhibited lower constructions supplies the three-marker classification. The table in OEIS A247000 concerns unrestricted binary circular words and has terms only through length \(30\); it does not imply the full gap-dependent statement or infinite classification. Blondin Massé, Brlek, Garon and Labbé (2011) analyze equations on palindromes and circular words, especially periodicity and tiling, rather than the sparse-marker extremal statistic. These distinctions describe the comparisons made; lack of a matching indexed source is not a proof of universal novelty.

## Limitations

The maxima are **not asserted for all binary circular words**. The global conjecture remains open on the evidence inspected. The total palindromic count is not a length-by-length palindrome-complexity generating function. The classification is modulo rotation **and reversal**; counts of distinct *oriented* necklaces are not claimed here. Historical priority could be affected by an unindexed treatment of three-marker gap patterns.

## References

1. J. Simpson, *Palindromes in circular words*, Theoretical Computer Science 550 (2014), 66–78. DOI: https://doi.org/10.1016/j.tcs.2014.07.012. Published full text reports availability online 2014-07-22. Relevant: Lemma 6, Theorem 7, Proposition 13, open questions.
2. OEIS Foundation, A247000, *Maximal number of palindromes in a circular binary word of length n*, https://oeis.org/A247000. Consulted for existing finite unrestricted counts and examples.
3. A. Blondin Massé, S. Brlek, A. Garon, and S. Labbé, *Equations on palindromes and circular words*, Theoretical Computer Science 412 (2011), 2922–2930. Author preprint: https://archipel.uqam.ca/8427/1/Blondin-Mass%C3%A9-2011a-preprint.pdf.
