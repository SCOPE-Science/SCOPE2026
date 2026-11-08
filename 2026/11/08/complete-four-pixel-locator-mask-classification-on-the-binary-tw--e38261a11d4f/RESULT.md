# Complete four-pixel locator-mask classification on the binary two-by-eight torus

## Finding

Let \(T=\mathbb Z/2\mathbb Z\times\mathbb Z/8\mathbb Z\), and assign a binary symbol to every one of its sixteen sites. For each four-element mask \(M\subseteq\{0,1\}\times\{0,1,2\}\), observe the ordered four-bit word obtained by translating the mask to each of the sixteen sites, with both directions read cyclically. Call the array \(M\)-universal if all sixteen possible four-bit words appear exactly once.

**Complete finite classification.** Of the fifteen literal masks, twelve occupy all three columns of the mask window, and three occupy only two columns. Each of the twelve three-column masks admits **exactly the same 64 labeled arrays**; none of the three two-column masks admits an array. Consequently each successful array locates all possible four-bit fillings for all twelve masks *simultaneously*, not merely for one prescribed mask.

The 64 successful arrays form four free orbits of size sixteen under torus translation, represented by the following pairs of row words. Bits are listed in increasing column order:

| First row | Second row |
|---|---|
| `01111010` | `11010000` |
| `11100101` | `10110000` |
| `01011010` | `11110000` |
| `10100101` | `11110000` |

Under the additional operations of global bit complementation and column reversal, these four translation orbits combine into exactly two orbits of size 32 each. Every successful array has alternating columnwise row XOR: its two rows differ in exactly the columns of one parity class.

## Assumptions and scope

The alphabet is literally \(\{0,1\}\), the torus has exactly two indexed rows and eight indexed columns, and no mask sites are repeated. The four mask sites have relative row indices in \(\{0,1\}\) and relative column indices in \(\{0,1,2\}\). A literal mask is an element of \(\binom{\{0,1\}\times\{0,1,2\}}4\), not a shape quotient. For \(M\), its coordinates are ordered lexicographically to form a four-bit word; changing this ordering only permutes the sixteen output labels and does not change universality.

Arrays are initially counted as labeled maps \(T\to\{0,1\}\). Horizontal translation is cyclic modulo eight and vertical translation is cyclic modulo two. Global complementation acts on both rows; column reversal sends column \(j\) to \(-j\pmod 8\). No row-column transposition is included.

## Proof

There are \(\binom64=15\) literal masks. If a mask uses just two distinct columns, all four sites in those two columns are included, as the torus has two rows. For this mask the all-zero four-bit word would need to occur. But swapping the translated row coordinate leaves an all-zero word unchanged, producing a second occurrence at a distinct site. Thus no such mask is universal. There are precisely three choices of two columns, giving three impossible masks.

For the remaining twelve masks, exhaust all \(2^{16}=65{,}536\) binary arrays with exact integer arithmetic. Represent an array by \(b\in\{0,\ldots,65535\}\) and define

\[
 v_b(i,j)=\left\lfloor\frac{b}{2^{8(i\bmod2)+(j\bmod8)}}\right\rfloor\bmod2.
\]

For every four-site mask \(M=\{(r_0,c_0),\ldots,(r_3,c_3)\}\) in lexicographic order and every translation \((i,j)\in T\), compute the four-bit integer

\[
 w_{b,M}(i,j)=\sum_{k=0}^{3}2^k v_b(i+r_k,j+c_k).
\]

The array is universal for \(M\) if and only if the sixteen values \(w_{b,M}(i,j)\) form exactly the set \(\{0,\ldots,15\}\). In `verify_direct.py`, the bitset `seen` is the bitwise OR of `1 << w` over all sixteen translations. Since there are exactly sixteen translations, `seen == (1 << 16)-1` is equivalent to the required bijection. The program iterates all sixteen-bit integers and all fifteen masks, establishes that the successful sets for the twelve spanning masks are identical and have cardinality 64, and establishes that all three other sets are empty. Each loop has an explicit finite range, with no probabilistic or search-cutoff assumption.

For a compact equality certificate, let \(R=\{\texttt{0x0b5e},\texttt{0x0da7},\texttt{0x0f5a},\texttt{0x0fa5}\}\). In each integer in \(R\), bits zero through seven are the first row and bits eight through fifteen the second row. Direct evaluation of all sixteen translations of every seed produces four disjoint 16-element sets; their union equals the 64 arrays obtained by the complete scan. This gives the stated complete classification and shows that all translation stabilizers are trivial.

The same checker applies complement and column reversal to the 64 arrays and obtains two orbits, each of size 32. It checks the columnwise row-XOR alternation property for each of the 64 arrays. The independently encoded `verify_independent.py` exhausts the same domain using explicit two-row tuples and four-bit tuple windows, then independently constructs the seed orbits; it agrees with the complete enumeration.

## Verification

Run, using Python 3 standard-library only:

```bash
python verify_direct.py
python verify_independent.py
```

The observed success lines are `DIRECT_OK` and `INDEPENDENT_OK`. The first checker directly examines \(65{,}536\) arrays for each of 15 masks and computes the symmetry orbits. The second checker uses independent row-word and tuple representations rather than the first checker's bitset membership test. Both scripts are embedded in the same package, with no external input or executable dependency.

## Relationship to prior work

Horan and Stevens, *Locating Patterns in the De Bruijn Torus* (2015), study the construction and decoding of arrays for nonrectangular local windows, including connected-tree conditions and quotient/de Bruijn product constructions. Their construction/existence statements motivate the four-site experiment, but are not a classification of all binary two-row, eight-column arrays and do not imply the exact 64-array census or simultaneous universality for the twelve masks, including four masks whose nearest-neighbor connection graph is disconnected.

The separate literature on one-dimensional de Bruijn sequences with sparse comb windows addresses a different cyclic indexing model: it does not impose both toroidal row translations of each four-site two-dimensional mask. The standard rectangular de Bruijn-torus existence problem also does not supply this classification.

## Limitations

The classification is finite and exact only for binary two-by-eight arrays with masks supported inside a two-by-three window. The result does not assert a formula for larger dimensions, higher alphabets, five-site masks, or arbitrary nonlocal mask arrangements. The proof's census is a complete finite enumeration, not an inferred infinite-family theorem. Historical priority outside the directly inspected literature remains open to further scrutiny.

## References

1. Victoria Horan and Brett Stevens, *Locating Patterns in the De Bruijn Torus*, arXiv:1505.04065v1 (publicly posted May 15, 2015), https://arxiv.org/abs/1505.04065 . Sections 2–3, especially Theorems 3.5 and 3.9–3.11.
2. Abbas Alhakim, Steve Butler, and Ron Graham, *De Bruijn Sequences with Varying Combs*, Integers 14A (2014), A1, https://mathweb.ucsd.edu/~ronspubs/14_03_combs.pdf . One-dimensional comb comparison only.
