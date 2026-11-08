# Sharp 27-to-28 ternary synchronization-string threshold and its unique extremizer

## Finding

Let \(\Sigma=\{0,1,2\}\). For a word \(w\in\Sigma^n\), define its adjacent-interval LCS ratio
\[
R(w)=\max_{0\le i<j<k\le n}\frac{2\operatorname{LCS}(w[i:j],w[j:k])}{k-i},
\qquad \beta_3(n)=\min_{w\in\Sigma^n}R(w),
\]
where \(w[i:j]\) is the half-open interval and LCS is longest *scattered* common subsequence length, not longest common substring. The maximum is \(0\) when no two nonempty adjacent intervals have a nonempty common subsequence. An \(\varepsilon\)-synchronization string is one for which every pair of adjacent nonempty intervals has insertion-deletion edit distance strictly greater than \((1-\varepsilon)\) times their combined length.

**Theorem (sharp finite ternary synchronization spectrum).** For all integer lengths \(1\le n\le28\), the exact value \(\beta_3(n)\) is
\[
\begin{array}{c|c}
 n & \beta_3(n)\\\hline
 1,2,3&0\\
 4&1/2\\
 5,6&2/3\\
 7,8,9,10&4/5\\
 11,12,\ldots,26&6/7\\
 27&20/23\\
 28&8/9.
\end{array}
\]
At length \(27\), exactly one minimizer exists up to global alphabet permutation: `012010212021012102010212012`. It gives exactly six labeled minimizers. At length \(28\), there are exactly thirteen minimizers up to permutation, thus seventy-eight labeled minimizers, listed in `CENSUS.txt`.

Consequently, for each real parameter \(20/23<\varepsilon\le8/9\), the maximum possible length of a ternary strict \(\varepsilon\)-synchronization string is **exactly \(27\)**, and the only maximum-length words are the six alphabet permutations of the displayed canonical word. At \(\varepsilon=20/23\), the maximum possible length is \(26\). The asserted maximum-length conclusions apply to *all* longer words, not merely to an enumerated range.

## Assumptions and scope

Every word is over the fixed three-letter alphabet \(\Sigma\), with no restriction that all three letters occur. Lengths are positive integers. Edit distance allows only single-letter insertions and deletions; substitutions cost one deletion plus one insertion. The inequality defining synchronization strings is strict. The finite-spectrum computation is for \(1\le n\le28\); the unlimited-length cutoff is obtained from the hereditary prefix property.

An *alphabet-canonical* word is a restricted-growth spelling: its first symbol is `0`, and previously unseen symbols may first occur only in the order `1`, then `2`. Two words are equivalent when obtained by one global permutation of \(\Sigma\). An alphabet-canonical square-free word is the unique representative of its equivalence class, except that labels unused by the word can be permuted without changing it.

## Proof

**1. Reduction from edit distance to exact LCS ratios.** For any finite words \(x,y\),
\[
\operatorname{ED}(x,y)=|x|+|y|-2\operatorname{LCS}(x,y).
\]
Substituting adjacent intervals proves the exact equivalence
\[
w\text{ is a strict }\varepsilon\text{-synchronization string}
\quad\Longleftrightarrow\quad R(w)<\varepsilon.
\]
In particular, if \(w\) contains a square factor \(xx\) with \(x\ne\epsilon\), choosing the two copies gives \(R(w)=1\). Thus every word with \(R(w)<1\) is square-free.

**2. Exhaustive and symmetry-reduced search.** Every ternary word has precisely one restricted-growth form under global letter permutation. For a canonical prefix, an appended symbol must be a previously used symbol or the least unused symbol. Check each extension for a square ending at the last position by comparing its last two blocks of length \(d\) for all \(1\le d\le\lfloor n/2\rfloor\). Inductively, this enumerates *every* canonical square-free word exactly once: a new square must end at the newly appended symbol, since all shorter prefixes were square-free. Conversely any canonical square-free word is reached by this recursion. At length \(28\), the final layer has \(3370\) canonical words; length \(27\) has \(2581\).

**3. Exact evaluation of every candidate.** On appending the symbol at position \(k-1\), all previously checked adjacent-interval triples remain valid. Newly created triples must have their right endpoint at \(k\). For each \(0\le i<j<k\), calculate \(\operatorname{LCS}(w[i:j],w[j:k])\) by the standard dynamic-programming recurrence and compare the ratio \(2\operatorname{LCS}/(k-i)\) by integer cross products. The running maximum therefore equals \(R(w)\) *exactly*, with no rounding. Taking the minimum over all canonical candidates and counting attaining words gives the 28 rows and full extremizer list of `CENSUS.txt`. Every row is independently recomputed by `verify_python.py`, which evaluates all triples for each word using a bit-vector LCS recurrence rather than the C++ dynamic-programming recurrence; its table and listed extremizers agree byte-for-byte with `verify_cpp.cpp` output. The enumerated values are below one, so excluding non-square-free words in Step 2 cannot omit a minimizer.

At length \(27\), the unique canonical minimizer is
`012010212021012102010212012`, for which the maximum is \(20/23\). For example, the adjacent blocks at boundaries \((i,j,k)=(0,12,23)\) have LCS length \(10\), giving \(2(10)/23=20/23\). The exact exhaustive maximum check establishes that no other triple gives a larger ratio. At length \(28\), every canonical word has a ratio at least \(8/9\), and exactly thirteen reach equality. The first listed witness, `0102012021201210120102012021`, has an adjacent pair at \((0,4,9)\) with LCS \(4\), yielding \(8/9\).

**4. Unlimited-length cutoff.** If \(u\) is a prefix of \(v\), then \(R(v)\ge R(u)\), because every adjacent-interval triple in \(u\) also appears in \(v\). Every ternary word of length \(28\) has \(R\ge8/9\), so no longer word can satisfy the strict inequality \(R<\varepsilon\) for \(\varepsilon\le8/9\). On the other hand the length-27 witness has \(R=20/23\), and hence works for every \(\varepsilon>20/23\). Prefixes of length \(26\) attain \(6/7<20/23\), so the endpoint \(\varepsilon=20/23\) permits length \(26\) but forbids length \(27\) or greater. Global alphabet permutations leave every LCS ratio invariant and the unique canonical minimizer uses all three symbols, giving exactly six labeled words at length \(27\). This proves the theorem.

## Verification

The standalone sources `verify_cpp.cpp` (ISO C++17) and `verify_python.py` (Python 3 standard library) provide two independent, exact-arithmetic enumerations. Run

```bash
g++ -std=c++17 -O2 -Wall -Wextra verify_cpp.cpp -o verify_cpp
./verify_cpp > cxx.txt
python3 verify_python.py > py.txt
head -n -1 py.txt > py_census.txt
cmp cxx.txt py_census.txt
cmp cxx.txt CENSUS.txt
```

Both programs enumerate all restricted-growth square-free words through length \(28\); the C++ program updates the maximum incrementally using conventional LCS dynamic programming, while the Python program recomputes all triples with a bit-parallel LCS algorithm. All integer comparisons, extremizer counts and listed witnesses are exact. Their agreement was checked before recording the result. In the C++ program the final assertions additionally enforce the \(27\)- and \(28\)-length critical values.

## Relationship to prior work

Xu, Fu, Qiao and Tao (2026) prove that ternary synchronization strings exist at every length for \(\varepsilon=2001/2002\), and refine this to \(\varepsilon>226/227\). Their theorem establishes the *alphabet* threshold and infinite-length existence at larger parameters; it does not imply the exact finite-length minimax spectrum, the sharp length-27/28 obstruction at \(8/9\), or its unique canonical length-27 witness.

Cheng, Haeupler, Li, Shahrasbi and Wu (2018), Appendix A, report a computational lower bound \(B_3\ge12/13\) for the infimal parameter permitting an *infinite* ternary synchronization string. This is compatible with the present short-length cutoff but does not locate the exact finite minimum at length \(28\), enumerate its thirteen extremizers, or classify all length-27 optimal words; the article's published table contains only the infinite-parameter bound. Their computational search is a material priority risk because unpublished source data could overlap the finite spectrum.

Camungol and Rampersad (2013) examine LCS similarity for **equal-length** adjacent blocks, a weaker constraint than the unequal-interval synchronization condition here, and report experimental ternary intervals rather than the stated finite exact classification.

## Limitations

The classification is for the standard insertion-deletion LCS model, ternary alphabets and finite lengths through \(28\). The theorem does not determine \(\beta_3(n)\) at \(n>28\) or prove asymptotic optimal synchronization parameters. Its global nonexistence conclusion uses the length-28 hereditary obstruction and holds only at \(\varepsilon\le8/9\). The finite calculation is an exhaustive proof under the provided code and stated enumeration argument, but has not undergone independent mathematical audit. Historical precedence of unreleased implementations is not fully ruled out.

## References

1. H. Xu, S. Fu, Y. Qiao and D. Tao, *Synchronization Strings over the Optimal Alphabet*, first publicly available 2026-09-03, https://arxiv.org/abs/2609.04122 (Introduction, definition 1.1, Theorems 1.2 and 1.5, and computational appendix).
2. K. Cheng, B. Haeupler, X. Li, A. Shahrasbi and K. Wu, *Synchronization Strings: Efficient and Fast Deterministic Constructions over Small Alphabets*, arXiv:1803.03530, https://arxiv.org/pdf/1803.03530 (Sections 1--2 and Appendix A, Table 1).
3. C. Camungol and N. Rampersad, *Avoiding approximate repetitions with respect to the longest common subsequence distance*, arXiv:1308.1620, https://arxiv.org/abs/1308.1620 (Sections 1 and 4).
