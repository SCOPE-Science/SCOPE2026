# Gap-suffix compression of inverse Lyndon arrays for sparse binary words

## Finding

Let \(W\) be any nonempty binary word, with the usual order \(0<1\), written uniquely as
\[
W=0^{g_0}1\,0^{g_1}1\,0^{g_2}\cdots 1\,0^{g_r},
\]
where \(r\ge0\) is the number of ones and all the \(g_i\) are nonnegative integers. Its *inverse Lyndon array* \(\lambda_W(p)\) is the length of the longest prefix of \(W[p:]\) that is lexicographically greater than each of its own proper nonempty suffixes (zero-based positions).

**Theorem.** All \(n=|W|\) entries of \(\lambda_W\) have an exact representation by at most \(2r+1\) arithmetic-progression segments, computable from \((g_0,\ldots,g_r)\) in \(O((r+1)\log(r+2))\) time and \(O(r+1)\) working words, independent of \(n\). The representation supports an arbitrary entry query in \(O(\log(r+1))\) time. The construction is completely explicit, including the nonzero border corrections at one positions.

For \(r\ge1\), let \(p_i=g_0+(i-1)+\sum_{h=1}^{i-1}g_h\) denote the position of the \(i\)-th one. Form the length-\(r\) gap code
\[
B=(g_1,\ldots,g_{r-1},\bot),
\]
where the special terminal symbol \(\bot\) is smaller than every integer, while integers are ordered in **reverse numeric order**. Write \(B_i=B[i..r]\). Let \(j(i)\) be the least \(j>i\) such that \(B_j\) is lexicographically greater than \(B_i\), or declare it absent.

* On each zero run of length \(t\), the array entries, from left to right, are \(t,t-1,\ldots,1\).
* If \(j(i)\) is absent, \(\lambda_W(p_i)=n-p_i\).
* Otherwise, if \(h\) is the common-prefix length of \(B_i\) and \(B_{j(i)}\), then \(j(i)+h<r\), \(g_{j(i)+h}<g_{i+h}\), and
\[
\boxed{\lambda_W(p_i)=p_{j(i)}-p_i+\sum_{t=0}^{h-1}(1+g_{i+t})+1+g_{j(i)+h}.}
\]

Indices in this formula are one-based for the gap code and its one positions; the array positions \(p_i\) themselves are zero-based.

## Assumptions and scope

The input is a list of nonnegative zero-gap lengths in an exact integer word-RAM model with \(O(\log(n+1))\)-bit arithmetic words. Input length is \(r+1\), output is a run/arithmetic-progression encoding, not an explicitly expanded array. No restriction is imposed on consecutive ones (zero-length interior gaps are allowed), the leading or trailing gap, or the size of the individual gaps. When \(r=0\), the array of the all-zero word is the single arithmetic progression \(n,n-1,\ldots,1\). The empty word has no array entries and is excluded.

The time bound counts word-level comparisons and arithmetic operations, and does not claim a bound independent of integer bit length when gaps exceed machine-word capacity.

## Proof

**1. Zero positions.** From a zero position there are exactly \(t\) consecutive zeros before the next one or the end of \(W\). Each nonempty all-zero word is inverse Lyndon: all proper nonempty suffixes are strictly shorter prefixes. If a later one exists, appending it produces a word beginning in zero but with a proper suffix beginning in one, so the result is not inverse Lyndon. If no later one exists, the entire remaining zero suffix is inverse Lyndon. Hence the longest inverse Lyndon prefix at this position always has length \(t\). Every zero run is therefore one descending arithmetic-progression segment.

**2. Ordering suffixes that start at ones.** Let \(X_i=W[p_i:]\). For \(i<j\), compare \(X_i\) and \(X_j\). Each completed interior block \(1\,0^{g_k}\) has a following one; its code symbol is the integer \(g_k\). At the first unequal *interior* gap, the suffix with the smaller numerical gap next displays a one while the other still displays a zero, and is thus lexicographically larger. The terminal suffix \(1\,0^{g_r}\), on the other hand, is smaller than every suffix with a following one: either it ends first while the other remains its extension, or the other displays another one before it ends. Accordingly the terminal code must rank below every interior-gap code, regardless of \(g_r\). These comparisons prove
\[
X_i<X_j\quad\Longleftrightarrow\quad B_i<B_j
\]
for every \(i<j\), where the two comparisons use their respective stated alphabet orders. This accounts for terminal truncation, which a naïve integer-gap suffix order would mishandle. A suffix starting in zero is never greater than a suffix starting in one. It follows that the next genuinely greater suffix of \(W[p_i:]\) is exactly \(W[p_{j(i)}:]\), or no real suffix if \(j(i)\) is absent.

**3. Expansion of the longest common prefix.** If \(j=j(i)\) exists and \(h=\operatorname{lcp}(B_i,B_j)\), the first \(h\) completed blocks have identical lengths. At the first unequal code symbol, the greater later suffix cannot contain the terminal code \(\bot\), so both symbols are interior gaps and \(g_{j+h}<g_{i+h}\). The expanded suffixes then share the \(h\) completed blocks and the initial \(1\,0^{g_{j+h}}\) of the next block, with different next bits. Therefore their exact expanded-text longest common extension is
\[
\operatorname{LCE}(p_i,p_j)=\sum_{t=0}^{h-1}(1+g_{i+t})+1+g_{j+h}.
\]
Every term can be recovered in constant time from prefix sums of \(1+g_i\), once \(h\) is known.

**4. Inverse Lyndon boundary.** The nearest-greater-suffix/border identity for inverse Lyndon arrays states that for a position \(p\), if \(q>p\) is the first position whose full suffix is greater, then
\[
\lambda_W(p)=(q-p)+\operatorname{LCE}(p,q).
\]
If no such position exists, \(\lambda_W(p)=n-p\). This is the border-correction result of Negri et al. (2026), revisited in De Felice et al. (2026); its proof derives the correction from the longest proper border of the maximal inverse Lyndon prefix. In particular, an uncorrected next-greater distance need not equal the inverse Lyndon entry. Applying the identity at each one position and substituting the result of step 3 gives exactly the formula in the Finding. Together with step 1 this proves every entry, including all boundaries and degenerate gaps.

**5. Cost and representation.** Coordinate-compress the distinct interior gaps with reversed integer order and append the smallest terminal code. An integer suffix array of the \(r\)-symbol code is constructed by prefix doubling and two counting-sort passes per doubling round, in \(O((r+1)\log(r+2))\) time and \(O(r+1)\) space. Its inverse ranks yield every next-greater suffix index \(j(i)\) by a right-to-left monotone stack in \(O(r)\) time. Kasai's LCP construction and an iterative range-minimum segment tree answer each of the at most \(r\) needed suffix LCP queries in \(O(\log(r+1))\) time, with linear additional space. Prefix sums of gap-block lengths provide expanded LCEs in constant time. Output each one entry as a singleton segment, plus each nonempty zero run as a descending segment. There are at most \(r\) singleton and \(r+1\) zero-run segments. Binary search over segment starts gives the query bound. None of these operations visits the expanded zero positions.

## Verification

The standalone `check_inverse_lyndon.py` implements the stated integer suffix-array/range-minimum method, returns the compressed segments, and compares their expansion against an **independent, direct definition-based** inverse Lyndon-prefix oracle on small inputs. Run it with `python3 check_inverse_lyndon.py`. The captured output is in `check_output.txt`.

The checker passed 27,304 exhaustive nonempty gap tuples (up to six ones, initial gaps below five, later gaps below four), 1,500 deterministic-seed randomized small cases, and nonexpanding structural checks with lengths exceeding ten billion and up to 2,048 marked ones. Randomized and finite checks do not establish the general theorem; the five proof steps above do. The long cases check compressed segment coverage and bounds without constructing length-\(n\) text.

## Relationship to prior work

Negri et al., *The Inverse Lyndon Array* (arXiv:2603.17537v1), introduce the array, give the crucial NGS/LCE identity, and construct it in linear time in expanded text length. The later De Felice et al. version (arXiv:2609.23401v1) adds a direct relationship with canonical inverse Lyndon factorization; its Sections 3--4 concern expanded-input operations. The present claim is not the NGS/LCE identity itself: it establishes a new order-preserving terminal-gap encoding and a compressed full-array construction with cost depending on the number of marked ones, not the expanded text length.

Ghuman, Giaquinta and Tarhio (2019), Section 5, compute an ordinary Lyndon **factorization** from run-length encoded input, not the inverse Lyndon **array at all starting positions**. The 2025 paper *Space-Efficient Lyndon Array Construction from Compressed Texts* addresses ordinary Lyndon arrays during grammar decompression; only its public abstract was inspected, so no whole-paper noncoverage assertion is made. These distinctions matter: computing one factorization or a standard Lyndon array does not directly provide the claimed inverse-array entries and compressed LCEs at every one position.

## Limitations

The result is specific to binary inputs encoded by the number of ones and the intervening zero gaps. It does not establish an analogous number-of-runs time bound for arbitrary alphabets or for inputs with many ones inside a single long run. A fully expanded array necessarily takes \(\Omega(n)\) output time; the improvement applies to the stated compressed representation. The procedure uses the already published NGS/LCE identity, which is credited rather than claimed as new. Exhaustive searches and accessible prior literature cannot rule out unindexed or differently phrased equivalent compressed algorithms; independent audit has not been performed.

## References

1. Pietro Negri, Manuel Sica, Rocco Zaccagnino, and Rosalba Zizza, *The Inverse Lyndon Array: Definition, Properties, and Linear-Time Construction*, arXiv:2603.17537v1, first public 2026-03-18, especially §3.2. https://arxiv.org/html/2603.17537v1
2. Clelia De Felice, Pietro Negri, Manuel Sica, Rocco Zaccagnino, and Rosalba Zizza, *The Inverse Lyndon Array*, arXiv:2609.23401v1, first public 2026-09-20, especially §§3--4. https://arxiv.org/abs/2609.23401
3. Sukhpal Singh Ghuman, Emanuele Giaquinta, and Jorma Tarhio, *Lyndon Factorization Algorithms for Small Alphabets and Run-Length Encoded Strings*, Algorithms 12(6):124, 2019, especially §5. https://doi.org/10.3390/a12060124
4. *Space-Efficient Lyndon Array Construction from Compressed Texts*, Procedia Computer Science 273 (2025), pp. 413--420, abstract-level comparison only. https://doi.org/10.1016/j.procs.2025.10.326
