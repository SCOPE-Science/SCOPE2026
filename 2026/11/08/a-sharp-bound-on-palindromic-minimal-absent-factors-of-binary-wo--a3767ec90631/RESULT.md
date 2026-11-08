# A sharp bound on palindromic minimal absent factors of binary words

## Finding
For every integer \(n\geq 2\), among all length-\(n\) words \(w\in\{0,1\}^{n}\), the maximum number of **distinct palindromic minimal absent factors** is exactly \(n\). For \(n=1\), the maximum is \(2\).

More precisely, for every binary word containing both symbols, the map sending each palindromic minimal absent factor of length at least two to the ending position of the first occurrence of its length-one-shorter prefix is injective. For \(n\ge3\), the word \(w=01^{n-2}0\) meets the bound; its palindromic minimal absent factors are exactly
\[
\{00,101,1^{n-1}\}\ \cup\ \{01^k0:1\le k\le n-3\}.
\]
The displayed sets are disjoint and have \(n\) members in total. The superscripts denote repetitions of a symbol, not numerical exponentiation.

## Assumptions and scope
An occurrence is a contiguous substring of a finite **linear** word, not a scattered subsequence or a circular factor. The alphabet is the fixed binary alphabet \(\{0,1\}\), even when one letter is unused. An absent word \(p\) is *minimal absent* if every proper contiguous factor occurs. For \(|p|\ge2\), this is equivalent to requiring both \(p\) with its final symbol deleted and \(p\) with its first symbol deleted to occur. A palindrome equals its reversal. Length-one absent letters are included in the count. Positions are numbered from \(1\) to \(n\).

## Proof
**Injection.** First suppose both letters occur in \(w\); hence a minimal absent word has length at least two. Let \(P(p)\) be the prefix of a palindromic minimal absent factor \(p\) of length \(|p|-1\). Since \(P(p)\) occurs, define \(e(p)\) to be the endpoint of its first occurrence, which belongs to \(\{1,\ldots,n\}\).

Suppose distinct such palindromes \(p\) and \(q\) satisfy \(e(p)=e(q)=t\). If their lengths are equal, their prefixes occur as substrings of the same length ending at \(t\), so their prefixes coincide. A palindrome is uniquely determined by all but its final symbol, making \(p=q\), a contradiction. Thus after exchanging them assume \(r=|p|<s=|q|\). Write \(a=p_1=p_r\) and \(b=q_1=q_s\). Since \(P(p)\) and \(P(q)\) end at the same position, \(P(p)\) is a proper suffix of \(P(q)\).

If \(a=b\), the last \(r\) letters of \(q\) are \(P(p)a=p\). Reversal symmetry of \(q\) makes \(p\) also a prefix of \(q\). As \(r<s\), that prefix occurs inside \(P(q)\), a factor of \(w\), contradicting the absence of \(p\).

If \(a\ne b\), suppose \(t<n\). The symbol \(w_{t+1}\) cannot be \(a\), since it would complete the occurring \(P(p)\) to \(p\). Equally it cannot be \(b\), since it would complete \(P(q)\) to \(q\). The binary alphabet has no third symbol, a contradiction. Therefore \(t=n\).

By minimal absence of \(q\), its suffix \(S(q)=q_2\cdots q_s\) occurs in \(w\). This length-\(s-1\) factor cannot end at \(n\): the unique such substring would then equal \(P(q)\), forcing \(q_1\cdots q_{s-1}=q_2\cdots q_s\), whence \(q\) would be constant, inconsistent with \(a\ne b\) and the suffix relation. Thus an occurrence of \(S(q)\) ends strictly before \(n\). Because \(r<s\), the suffix \(P(p)\) of \(P(q)\) starts at position \(s-r+1\ge2\) of \(q\), and ends before position \(s\); hence it lies inside \(S(q)\). This supplies an occurrence of \(P(p)\) ending before \(n\), contradicting the definition \(e(p)=n\). The map \(e\) is injective, giving at most \(n\) palindromic minimal absent factors.

If \(w\) uses only one binary symbol, say \(w=0^n\), its minimal absent factors are exactly \(1\) and \(0^{n+1}\), both palindromes. Thus for \(n\ge2\) their number is \(2\le n\); for \(n=1\) it is \(2\).

**Sharpness.** For \(n\ge3\), let \(w=01^{n-2}0\). The words \(00\), \(101\), and \(1^{n-1}\) are absent, but their length-one-shorter prefixes and suffixes occur. For each integer \(1\le k\le n-3\), the palindrome \(01^k0\) is absent, while \(01^k\) and \(1^k0\) occur. All listed absent factors are distinct, giving \(3+(n-3)=n\) of them. The upper bound forces this to be the complete palindromic minimal absent set. For \(n=2\), \(w=00\) has the two palindromic minimal absent factors \(1\) and \(000\). This completes all cases.

## Verification
Two standalone Python programs are included: `verify_earliest.py` enumerates candidates from palindrome factors and checks the first-occurrence injection for every binary word of lengths \(1\) through \(16\); `verify_direct.py` independently enumerates palindromes of every feasible length, agrees with the first program for every word of lengths \(1\) through \(12\), and checks the sharpness construction through length \(29\). Both programs complete with `EARLIEST_VERIFY_OK` and `DIRECT_VERIFY_OK`, respectively. The arbitrary-length claim rests on the proof, not on finite enumeration.

## Relationship to prior work
Pinho, Ferreira, Garcia and Rodrigues (2009) introduced and structurally characterized minimal absent factors and established a general bound of order linear in input length. Barton, Heliou, Mouchard and Pissis (2014) gave a linear-time algorithm for the full minimal-absent-word set. Almirantis and colleagues (2017) gave the *same* binary family \(01^{n-2}0\) as a witness for asymptotically many minimal absent words, explicitly listing \(n-2\) of them; that published family is not claimed to be new here. The claim here is the sharp **exact** maximum for the *palindromic* subset and the endpoint injection, not invention of the family, existence of linear growth, or an algorithm for all minimal absent factors.

## Limitations
No uniqueness theorem for the maximizers is claimed. The injection depends crucially on a binary alphabet and need not hold for a ternary alphabet. The result does not address circular words, subsequence absence, or statistical/biological effectiveness of a palindrome filter. Historical priority is not independently certified; a source proving an exact stronger full-minimal-absent upper bound could potentially imply this result together with the already-published family.

## References
1. A. J. Pinho, P. J. S. G. Ferreira, S. P. Garcia, J. M. O. S. Rodrigues, “On finding minimal absent words,” *BMC Bioinformatics* 10, 137 (2009), published 2009-05-08. https://doi.org/10.1186/1471-2105-10-137
2. C. Barton, A. Heliou, L. Mouchard, S. P. Pissis, “Linear-time computation of minimal absent words using suffix array,” *BMC Bioinformatics* 15, 388 (2014); first arXiv posting 2014-06-24, https://arxiv.org/abs/1406.6341 .
3. Y. Almirantis et al., “On avoided words, absent words, and their application to biological sequence analysis,” *Algorithms for Molecular Biology* 12, 5 (2017), https://doi.org/10.1186/s13015-017-0094-z .
