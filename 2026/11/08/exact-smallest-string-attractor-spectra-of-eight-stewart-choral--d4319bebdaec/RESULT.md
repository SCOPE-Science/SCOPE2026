# Exact smallest-string-attractor spectra of eight Stewart choral iterates

## Finding

Let \(\varphi(0)=001\) and \(\varphi(1)=011\), and let \(W_k=\varphi^k(0)\) for each integer \(k\ge1\). For a finite word \(w\), a *string attractor* is a subset \(\Gamma\) of zero-based positions such that every nonempty contiguous factor has at least one occurrence intersecting \(\Gamma\). Write \(\gamma(w)\) for the least size, and \(a(w)\) for the number of subsets of that least size. The complete exact results for the first eight iterates are:

| Iterate \(k\) | Length | \(\gamma(W_k)\) | \(a(W_k)\) | Minimal factor-coverage constraints |
|:--:|--:|--:|--:|--:|
| 1 | 3 | 2 | 2 | 2 |
| 2 | 9 | 2 | 1 | 5 |
| 3 | 27 | 3 | 55 | 10 |
| 4 | 81 | 3 | 110 | 17 |
| 5 | 243 | 3 | 160 | 25 |
| 6 | 729 | 3 | 210 | 33 |
| 7 | 2187 | 3 | 260 | 41 |
| 8 | 6561 | 3 | 310 | 49 |

For each iterate with \(3\le k\le8\), an explicit three-position attractor is
\[
\Gamma_k=\left\{3^{k-1},\frac{3^k-1}{2},\frac{5\cdot3^k-3}{6}\right\}.
\]
The data show the exact finite progression \(a(W_k)=50k-90\) for \(4\le k\le8\), but no assertion about any larger iterate is made. Independently, the infinite-family lower bound
\[
\gamma(W_k)\ge3\quad\text{for every }k\ge3
\]
is proved without extrapolation from finite data.

## Assumptions and scope

Words are binary and finite; factor occurrences are contiguous and positions zero-based. The attractor sets are unordered, with positions not repeated. Both the finite counts and the morphic lower bound concern exactly the stated morphism and the canonical seed \(0\); reversing symbols or using other Stewart directive sequences is not asserted. The finite enumeration is exhaustive for \(k\le8\), not for all depths.

## Proof

**Exact reduction to finitely many hitting constraints.** For each nonempty factor \(u\) of a word \(w\), let \(C(u)\) be the union of all position intervals on which an occurrence of \(u\) lies. A set of positions is an attractor exactly if it meets each \(C(u)\). Factors having the same set of end positions form suffix-automaton end-position classes. In a given nonroot class, the shortest word has length one more than the maximal length at its suffix-link parent. All factors in that class have the same ending positions; the coverage set of the shortest one is contained in the coverage set of every longer one. Hence one coverage mask per suffix-automaton state suffices. Further, a mask that contains another mask is redundant, leaving the minimal masks under inclusion. The supplied verifier constructs these masks from all end positions and independently from a compressed suffix tree obtained from the suffix array and longest-common-prefix values. Both methods produce exactly the same minimal mask sets for each of the eight words.

**Exhaustive cardinalities.** For each ordered pair of positions \(i<j\), define \(E(i,j)\) to be the intersection of all minimal coverage masks missing both \(i\) and \(j\), or the full position set if there are no such masks. Precisely the indices \(r>j\) inside \(E(i,j)\) complete \(\{i,j,r\}\) to a valid three-position attractor. Thus, for every case with minimum size three, the verifier calculates the exact count
\[
\sum_{0\le i<j<|W_k|}\left|E(i,j)\cap\{j+1,\ldots,|W_k|-1\}\right|.
\]
It uses integer bitsets, with no candidate omission and no random samples. In the first two cases all pairs are checked directly. For \(k=3\), all pairs fail to attract, while 55 triples succeed; hence the minimum is three. The checked triples \(\Gamma_k\) give the upper bound three through depth eight, and the projection lemma below supplies the lower bound thereafter.

**All-depth obstruction by aligned substitution.** For any binary word \(u\), each occurrence of \(\varphi(u)\) inside any substituted word \(\varphi(w)\) must start at a block boundary: the initial triple is \(001\) or \(011\), but triples at the other two phases modulo three are respectively of the form \(010\) or \(110\), or begin in \(1\). If \(\Gamma\) attracts \(\varphi(w)\), consider any occurrence class of a factor \(u\) in \(w\). Some occurrence of \(\varphi(u)\) meets \(\Gamma\); alignment implies this is the substitution of an occurrence of \(u\) in \(w\). Projecting every marked position \(p\) to \(\lfloor p/3\rfloor\) therefore yields an attractor of \(w\) of cardinality no larger than \(|\Gamma|\). Consequently \(\gamma(\varphi(w))\ge\gamma(w)\); induction from \(\gamma(W_3)=3\) proves the displayed all-depth lower bound.

## Verification

The included portable Python scripts `samcov.py`, `sufcov.py`, and `verify.py` independently form the minimal hitting masks and exactly enumerate all unordered size-two or size-three hitting sets. Execute `python verify.py` with the three files together. On successful completion it prints `STEWART_ATTRACTOR_CENSUS_VERIFY_OK 8`. The companion `census.csv` records all eight values, mask counts, and explicit witnesses. The two exact mask-generation algorithms agreed at every depth, including \(k=8\) (word length 6561). The all-depth inequality is a symbolic lemma, not the output of finite enumeration.

## Relationship to prior work

Banbara, Bannai, Guo, Köppl, Mieno, and Okamoto investigate the entire families of smallest attractors of Fibonacci, period-doubling, and Thue–Morse words, establishing that counts of optimal attractors measure an interesting refinement of repetitiveness. Their primary work does not classify the Stewart choral morphism used here. Fici and Shallit study Stewart words and their factor-combinatorial properties; the accessible abstract and relevant source descriptions do not provide this attractor spectrum. A separate minimal-unique-substring classification for the same Stewart iterates supplies only necessary factor-hitting conditions, not sufficient conditions for the counted attractors. The proof here computes all coverage constraints, including those not arising from unique factors.

## Limitations

This is a complete **finite-depth** census through \(k=8\) and an infinite lower bound; it does not establish that attractors of size three exist for all further iterates or that the observed linear count formula continues. Reproducibility is from an exact algorithm and independent data structure, not from an externally issued formal proof certificate. Earlier unindexed results or equivalent string-attractor tables could alter publication priority. Independent mathematical audit has not been performed.

## References

- M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, Y. Okamoto, *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, arXiv:2602.16152, initially public 2026-02-18, https://arxiv.org/html/2602.16152.
- G. Fici, J. Shallit, *Properties of a Class of Toeplitz Words*, arXiv:2112.12125, initially public 2021-12-22, https://arxiv.org/abs/2112.12125.
