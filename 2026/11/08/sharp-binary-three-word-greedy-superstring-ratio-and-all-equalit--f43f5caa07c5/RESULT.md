# Sharp binary three-word greedy-superstring ratio and all equality cases

## Finding

Let \(\Sigma=\{0,1\}\), \(W=\Sigma^3\), and \(S\) be any nonempty subset of \(W\). Define \(\operatorname{OPT}(S)\) as the minimum length of a common superstring of the words in \(S\). The standard greedy algorithm repeatedly selects any ordered pair of distinct current strings having maximum suffix-prefix overlap, merges that pair, and continues to one string. Let \(G(S)\) be the greatest final length among **all legal tie-breakings**.

The sharp approximation ratio restricted to binary three-letter inputs is

\[
\boxed{\max_{\varnothing\ne S\subseteq\{0,1\}^3}
\frac{G(S)}{\operatorname{OPT}(S)}=\frac{10}{7}.}
\]

Exactly four input sets attain equality. They are the orbit, under reversal and simultaneous bit-complementation, of
\[
S_*=\{000,001,010,011,100\}.
\]
Specifically, using the lexicographic three-bit index \(0,\ldots,7\) and a mask whose bit indicates inclusion, their masks are \(31,87,234,248\). Every equality case has exactly five inputs, optimal superstring length \(7\), and worst legal greedy output length \(10\). These four sets form a single orbit under the two commuting involutions.

## Assumptions and scope

The input is a **set** of distinct three-letter binary strings, not a multiset; the empty set is excluded. Merges use ordered pairs, maximal suffix-prefix overlap (including overlap zero), and **arbitrary** resolution of equal-overlap ties. No strings are removed except the chosen two in each merge. The output is linear, not cyclic. The maximum is over all \(2^8-1=255\) possible nonempty input sets; no alphabet growth or additional input lengths are claimed.

For strings \(a,b\), write \(o(a,b)\) for the greatest integer \(j\) between zero and \(\min(|a|,|b|)\) for which the suffix of \(a\) of length \(j\) equals the prefix of \(b\) of length \(j\). Their ordered merge is \(a\odot b=a\,b[j+1\ldots |b|]\), interpreting the suffix after \(j\) in the usual zero-based implementation. The code uses unambiguous string slicing \(a+b[j:]\).

## Proof

**Lower bound and equality witness.** For \(S_*\), the length-seven word `0100011` contains all five inputs, and any linear word containing five different three-letter factors must have at least \(5+2=7\) letters. Thus \(\operatorname{OPT}(S_*)=7\). A legal greedy sequence is:

| Step | Ordered pair | Greatest current overlap | Merged word |
|---|---|---:|---|
| 1 | `001`, `010` | 2 | `0010` |
| 2 | `100`, `0010` | 2 | `10010` |
| 3 | `10010`, `011` | 1 | `1001011` |
| 4 | `000`, `1001011` | 0 | `0001001011` |

The recorded overlap equals the global maximum at each step, and the output has length \(10\). Hence \(G(S_*)/\operatorname{OPT}(S_*)\ge10/7\). Reversal and bit-complementation preserve the optimal length and the set of possible greedy output lengths (reversal reverses the order of merges), giving all four candidate equality sets.

**Exhaustive upper bound and equality classification.** The finite computation implements the following fully specified recurrences using exact integer arithmetic. If \(S=\{s_1,\ldots,s_m\}\), let \(H(T,j)\) be the maximum overlap savings of a directed Hamilton path on the words indexed by nonempty \(T\), finishing at \(j\). Set \(H(\{j\},j)=0\) and, for \(|T|>1\),
\[
H(T,j)=\max_{i\in T\setminus\{j\}}\bigl(H(T\setminus\{j\},i)+o(s_i,s_j)\bigr).
\]
Then
\[
\operatorname{OPT}(S)=3m-\max_{j\in\{1,\ldots,m\}}H(\{1,\ldots,m\},j).
\]
This formula is exact: merging a Hamilton path realizes its indicated length. Conversely, order the first appearances of the distinct length-three inputs in any common superstring; because all have equal length, consecutive starts differ by at least one, and their overlap savings from the ambient word can be no greater than the maximum suffix-prefix overlap. The corresponding Hamilton path yields a superstring no longer than the original.

For every current collection \(T\) of distinct strings let \(M(T)=\max_{a\ne b\in T}o(a,b)\). Define \(F(\{a\})=|a|\), and for \(|T|>1\),
\[
F(T)=\max_{\substack{a,b\in T,\ a\ne b\\o(a,b)=M(T)}}
F\bigl((T\setminus\{a,b\})\cup\{a\odot b\}\bigr).
\]
The recursion is exact by induction on the number of current strings: it enumerates **all** permissible ordered maximum-overlap merges and retains the longest final outcome. The standard noncontainment property of maximum-overlap greedy merging ensures distinct current strings remain distinct when starting with equal-length, distinct inputs. The direct string-state implementation does not need this lemma to enumerate the actual merges.

A bit mask from \(1\) through \(255\) enumerates every nonempty subset of \(W\) exactly once. The supplied `verify.py` computes both recurrences for every mask, checks each optimal length separately by enumerating all permutations, and checks every worst greedy length again using a separately structured endpoint-path recursion. The supplied `verify_independent.cpp` independently implements literal string-state greedy recursion and exhaustive permutations. Both programs produce precisely the \(255\) rows in `census.csv`. For every row they verify the integer inequality
\[
7G(S)\le10\operatorname{OPT}(S).
\]
Equality occurs in precisely rows \(31,87,234,248\), all with \((|S|,\operatorname{OPT}(S),G(S))=(5,7,10)\). This establishes the upper bound and complete equality classification.

## Verification

With Python 3, run `python3 verify.py`; it prints `BINARY_3MER_GREEDY_VERIFY_OK masks=255 ratio=10/7 maximizers=4` before the full census. With a C++17 compiler, run `c++ -std=c++17 -O2 verify_independent.cpp -o verify_cpp` followed by `./verify_cpp`; its error stream prints `BINARY_3MER_INDEPENDENT_CPP_OK masks=255 maximizers=4`. The two generated comma-separated censuses agree row-for-row and match `census.csv` (header excluded from the C++ output). No packages or external services are required. All state spaces are finite; no random sampling or timeout-based exclusion is used.

## Relationship to prior work

Chukhin, Kulikov, Mihajlin, and Smal (2026) prove that the worst-case length-three ratio over **arbitrary finite alphabets** is \(9/5\). This does not give the sharp restricted-binary value \(10/7\): their theorem yields only an upper bound on binary inputs and their extremal construction does not resolve the two-symbol class. Golovnev and coauthors (2019) analyze greedy and hierarchical superstring algorithms and obtain coarser bounds for length-three strings, not the binary extremal value or the four equality sets. Shibata (2026) constructs longer, even-length counterexamples to the unrestricted ratio-two conjecture (starting at length ten), which do not imply this length-three fixed-alphabet census. Accessible mathematical-record searches and direct earlier-claim comparisons did not identify a covering binary length-three classification.

## Limitations

This is an exact **finite** classification for eight available three-letter words. It does not establish a formula for larger read lengths, alphabets, or multisets, and it makes no claim about typical tie-breaking, average-case behavior, or optimal implementation performance. Independent mathematical review and definitive historical-priority confirmation have not been performed; an unindexed prior finite calculation is a residual possibility. The upper bound is a reproducible exhaustive computational proof rather than a short symbolic case-free inequality.

## References

1. N. Chukhin, A. S. Kulikov, I. Mihajlin, and A. Smal, *The Greedy Superstring Algorithm Achieves Ratio 2 for Strings of Length 6 Already*, arXiv:2608.20018, first public 2026-08-20. https://arxiv.org/abs/2608.20018
2. H. Shibata, *Disproving the Greedy Superstring Conjecture*, arXiv:2609.01365, first public 2026-09-01. https://arxiv.org/abs/2609.01365
3. A. Golovnev, A. S. Kulikov, A. Logunov, I. Mihajlin, and M. Nikolaev, *Collapsing Superstring Conjecture*, LIPIcs APPROX/RANDOM 2019, article 26. https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2019.26
