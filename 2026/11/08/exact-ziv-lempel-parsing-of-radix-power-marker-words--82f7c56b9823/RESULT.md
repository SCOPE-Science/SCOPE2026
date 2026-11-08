# Exact Ziv–Lempel parsing of radix-power marker words

## Finding
For each integer \(b\ge2\), define the infinite binary word \(w_b\) indexed from zero by
\[
w_b(n)=\begin{cases}1,&n=b^j-1\text{ for some integer }j\ge0,\\0,&\text{otherwise}.\end{cases}
\]
For a start position \(i\), its next Ziv–Lempel (\(z\)-) phrase is the shortest nonempty factor \(w_b[i..i+L-1]\) that occurs at no earlier start \(0\le j<i\). Earlier occurrences are allowed to overlap the current phrase. The following lists are **all** phrases, as ordered pairs (zero-based start, length).

* For \(b=2\), the first two pairs are \((0,1),(1,2)\), followed for every \(s\ge1\) by
\[
\bigl(3\cdot2^{s-1},\,3\cdot2^{s-1}\bigr).
\]
* For \(b=3\), the first three pairs are \((0,1),(1,1),(2,3)\). For each \(s\ge1\), with \(B_s=5\cdot3^{s-1}\), the next consecutive pairs are
\[
\bigl(B_s,3^{s+1}-B_s\bigr),\qquad
\bigl(3^{s+1},B_{s+1}-3^{s+1}\bigr).
\]
* For every \(b\ge4\), the first three pairs are \((0,1),(1,1),(2,b-2)\). For each \(s\ge1\), with \(B_s=(2b-1)b^{s-1}\), the next consecutive pairs are
\[
\bigl(b^s,(b-1)b^{s-1}\bigr),\qquad
\bigl(B_s,(b-1)^2b^{s-1}\bigr).
\]

If \(Z_b(N)\) is the number of phrase starts strictly below \(N\), these complete descriptions imply
\[
Z_2(N)=\log_2 N+O(1),\qquad Z_b(N)=2\log_b N+O_b(1)\quad(b\ge3),\qquad N\to\infty.
\]
In particular the dyadic word has one new phrase per asymptotic radix level, while every larger base has two.

## Assumptions and scope
This is the incremental shortest-*new-contiguous-factor* convention for Ziv–Lempel parsing, also called the \(z\)-factorization, not a phrase-dictionary-only LZ78 convention and not the longest-copy LZ77 convention. Factors start at nonnegative integer indices; words are infinite and each phrase is finite. A factor is new exactly when it occurs at no position strictly before its start, even if a hypothetical earlier occurrence extends beyond that start. All claims hold for every integer \(b\ge2\) and every indicated \(s\), with no finite cutoff.

## Proof
Write \(m_t=b^t-1\) for the marker positions, so the zeros between consecutive markers \(m_{t-1}\) and \(m_t\) form a single run of length \((b-1)b^{t-1}-1\), at positions \(b^{t-1},\ldots,b^t-2\).

**1. Zero-only phrases in bases at least three.** Fix \(b\ge3\) and \(s\ge1\) and consider \(i=b^s\). The longest zero run occurring before \(i\) has length \((b-1)b^{s-1}-1\), attained immediately before marker \(b^s-1\). The factor beginning at \(i\) has at least \((b-1)b^{s-1}\) zeros, since its next marker is \(b^{s+1}-1\). Therefore the shortest factor never beginning earlier is exactly \(0^{(b-1)b^{s-1}}\). This proves the pair at \(b^s\) and its length \((b-1)b^{s-1}\).

**2. Phrases ending at the next marker in bases at least three.** Set \(B_s=(2b-1)b^{s-1}\) and \(d=(b-1)^2b^{s-1}-1\). The next marker after \(B_s\) is \(b^{s+1}-1=B_s+d\). Thus the length-\(d+1\) factor at \(B_s\) equals \(0^d1\). Every shorter nonempty prefix is zero-only and occurs earlier starting at \(B_s-1\), inside the same zero run. No earlier occurrence of \(0^d1\) is possible: its last letter would need to occupy a marker \(b^t-1\); if \(t\le s\), the preceding zero gap has length at most \((b-1)b^{s-1}-1<d\), while if \(t\ge s+1\), its required start is at least \(b^{s+1}-1-d=B_s\). The exact new phrase is consequently \(0^d1\), of length \((b-1)^2b^{s-1}\), ending at position \(b^{s+1}-1\).

**3. The dyadic exception.** Put \(B_s=3\cdot2^{s-1}\) for \(s\ge1\). The factor of length \(B_s\) at \(B_s\) is
\[
0^{2^{s-1}-1}\,1\,0^{2^s}.
\]
At the earlier position \(j=2^{s-1}\), its first \(B_s-1\) letters occur again, since the first marker of each begins at relative offset \(2^{s-1}-1\), and the second marker in the earlier occurrence is only at relative offset \(B_s-1\). The final letters differ: the earlier factor has a \(1\) there, whereas the one beginning at \(B_s\) has \(0\). So all shorter prefixes occur earlier. Conversely, a hypothetical earlier occurrence of the entire length-\(B_s\) factor would need its first \(1\) at offset \(2^{s-1}-1\). For \(s\ge2\), the only earlier nonnegative candidate start is \(2^{s-1}\) (a candidate at zero has its first \(1\) too early); that occurrence differs in its last letter. For \(s=1\), the additional candidate \(0\) spells a different factor already at its second letter. Hence the phrase length is precisely \(B_s\). Its endpoint is \(B_{s+1}-1\), so the dyadic pairs are consecutive.

**4. Initial conditions and exhaustion.** In base two, the first factors are \(1\) and \(10\), ending at start \(3=B_1\). In base three they are \(1\), \(0\), \(100\), ending at \(5=B_1\); the formula in step 2 then ends at \(9=3^2\), and steps 1 and 2 alternate thereafter. For \(b\ge4\), they are \(1\), \(0\), and \(0^{b-3}1\). The last is shortest new because its shorter zero prefixes occur from index one, whereas the earlier zero run starts there and has one additional zero before marker \(b-1\). They end at \(b\), so steps 1 and 2 alternate from \(s=1\). In each case adjacent pairs are contiguous and their endpoints tend to infinity, completing the parsing. Each radix interval contains exactly two phrases for \(b\ge3\) (apart from bounded initial exceptions), while dyadic phrase starts double. Counting starts gives the displayed logarithmic laws.

## Verification
Run `python3 check.py` with Python 3.10 or later. The standalone program constructs the marker words directly and compares each proposed phrase with every earlier start. For all integer bases \(2\le b\le12\), it tested 115 consecutive phrases whose endpoints are at most 12,000. Both the novelty of each full phrase and the occurrence of its entire shorter prefix at an earlier start were independently tested. These finite tests are checks of the formulas, not the proof of their validity for arbitrarily large powers.

## Relationship to prior work
Jahannia and Stipulanti (2024, arXiv:2403.15215, March 22 first-public date) establish exact \(z\)-factorizations for the Fibonacci, Thue–Morse, period-doubling, Rudin–Shapiro, paperfolding, and Mephisto–Waltz sequences, with the same earlier-factor convention. Their stated formulas do not concern the radix-power marker words. Constantinescu and Ilie (2007) classify growth orders of Lempel–Ziv complexity for morphic words, including logarithmic regimes, but their accessible abstract does not give these phrase positions or the sharp leading constants. The present result is an explicit all-base family calculation, not a new definition of the parsing or a claim that logarithmic compression is unknown.

## Limitations
The theorem concerns this precise indicator sequence and the \(z\)-factorization; it does not establish a result for the longest-match Crochemore or LZ77 parsings or other automatic sequences. An exact equivalent in unindexed literature cannot be ruled out. The full 2007 general-growth paper was not available for full-text comparison; its abstract provides a broader-order result only. There is no independent scientific audit.

## References
1. M. Jahannia and M. Stipulanti, *Exploring the Crochemore and Ziv-Lempel factorizations of some automatic sequences with the software Walnut*, arXiv:2403.15215 (first public March 22, 2024), https://arxiv.org/abs/2403.15215.
2. S. Constantinescu and L. Ilie, *The Lempel–Ziv Complexity of Fixed Points of Morphisms*, SIAM Journal on Discrete Mathematics **21** (2007), 466–481, https://doi.org/10.1137/050646846.
3. A. Lempel and J. Ziv, *On the complexity of finite sequences*, IEEE Transactions on Information Theory **22** (1976), 75–81.
