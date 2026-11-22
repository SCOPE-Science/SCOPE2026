# A sharp five-bit threshold for ternary square-free substitution codes

## Finding
Let \(\Sigma=\{0,1,2\}\), and let \(S_n\subseteq\Sigma^n\) be the set of **all indexed square-free words**, i.e., those without a contiguous factor \(uu\) for any nonempty word \(u\). A code \(C\subseteq S_n\) corrects zero or one arbitrary substitution when different words in \(C\) have disjoint radius-one Hamming balls in the full received alphabet \(\Sigma^n\). Write \(M_n\) for its maximum cardinality. Then

\[
M_9=48,\qquad M_n\le31\quad(1\le n\le8).
\]

Consequently, **nine is the shortest length** at which a ternary square-free word code correcting a single arbitrary substitution can transmit 32 messages (five binary payload bits). In particular, a length-nine optimum has 48 words. This is a *worst-case zero-error* result; the channel may replace any symbol with either other symbol, and the corrupted output is not required to remain square-free.

## Assumptions and scope
Symbols \(0,1,2\) are distinct and labeled; word order and coordinate positions matter, and rotations are not identified. The empty word is not used as a source. A square \(uu\) has two immediately adjacent identical **nonempty blocks**, not merely two equal letters. The allowed received words are all \(3^n\) ternary words of length \(n\). The Hamming distance counts unequal coordinates.

By the triangle inequality and a length-one or length-two midpoint construction, two radius-one Hamming balls intersect exactly when their centers have distance at most two. Thus the zero-error condition is precisely minimum Hamming distance at least three. This reduction makes no assumption about the received word's square-freeness.

## Proof
**1. All shorter lengths.** Direct factor-avoidance generation gives \(|S_n|=3,6,12,18,30,42,60,78,108\) for \(1\le n\le9\). Therefore \(M_n\le30\) for \(n\le5\). For \(n=6\) and \(n=7\), the explicit perfect pairings in `CERTIFICATE.json` partition respectively all 42 and 60 square-free source words into pairs of Hamming distance one or two. A valid code contains at most one from each pair. Consequently \(M_6\le21\) and \(M_7\le30\). The checker regenerates the complete source sets and verifies every pair and its distance; this is a finite, exhaustive pairing certificate, not a heuristic matching log.

**2. A rational sphere-weight certificate at length eight.** Let \(G\) consist of all six permutations of the alphabet, optionally followed by reversal of the coordinate order. For any word \(v\), its \(G\)-orbit is \(Gv\). Assign nonnegative rational weight to each received word in the following seven orbits, and weight zero elsewhere. Each listed weight applies to every word in its orbit.

| Column | Received-word orbit representative | Orbit size | Rational weight |
|---:|---|---:|---:|
| 1 | `00120102` | 12 | \(1/2\) |
| 2 | `00120210` | 12 | \(1/4\) |
| 3 | `01010212` | 12 | \(1/2\) |
| 4 | `01020120` | 12 | \(1/4\) |
| 5 | `01020121` | 12 | \(1/4\) |
| 6 | `01200120` | 6 | \(3/4\) |
| 7 | `01201021` | 12 | \(1/2\) |

There are seven \(G\)-orbits of square-free source words at length eight. The table gives, for a representative \(x\) of each such orbit and each numbered received orbit, the integer \(|B_1(x)\cap Gv_i|\). Direct factor and one-substitution enumeration yields:

| Source orbit representative | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `01020120` | 0 | 0 | 0 | 1 | 1 | 0 | 1 |
| `01020121` | 0 | 0 | 1 | 1 | 1 | 0 | 0 |
| `01021012` | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| `01021201` | 0 | 1 | 0 | 0 | 1 | 0 | 1 |
| `01201021` | 0 | 1 | 0 | 1 | 0 | 0 | 1 |
| `01202120` | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| `01210201` | 2 | 0 | 0 | 0 | 0 | 0 | 0 |

Multiplying each row by the seven indicated weights gives exactly one. Because alphabet relabeling and reversal preserve square-freeness and Hamming distance, the same identity holds for **every** \(x\in S_8\):

\[\sum_{y\in B_1(x)}w(y)=1.\]

The orbits are disjoint and their total weight is

\[\sum_{y\in\Sigma^8}w(y)=6+3+6+3+3+\frac92+6=\frac{63}2.\]

For any correcting code the balls \(B_1(x)\) are disjoint; therefore \(|C|\le63/2\), and integrality yields \(M_8\le31<32\).

**3. A 48-word construction at length nine.** Form a code by taking the union of the complete \(G\)-orbits of the five representatives

`010201210`, `010210120`, `010212021`, `012010210`, `012021201`.

Their sizes are respectively 12, 12, 12, 6 and 6, with no duplicate members, hence the code has 48 words. Every word in the union is square-free, and all 1,128 distinct unordered pairs have Hamming distance at least three. These are exact direct comparisons replayed by the standalone checker. Thus \(M_9\ge48\).

**4. A matching rational upper certificate at length nine.** Use the same \(G\)-invariant received-word weighting with the following seven nonzero orbit types:

| Column | Received-word orbit representative | Orbit size | Rational weight |
|---:|---|---:|---:|
| 1 | `001201020` | 12 | \(1/2\) |
| 2 | `001201021` | 12 | \(1/1\) |
| 3 | `001202101` | 12 | \(1/2\) |
| 4 | `001202102` | 12 | \(1/2\) |
| 5 | `010101202` | 12 | \(1/2\) |
| 6 | `010102120` | 12 | \(1/2\) |
| 7 | `012001201` | 12 | \(1/2\) |

The eleven square-free source orbits at length nine meet these received orbits as follows:

| Source orbit representative | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `010201202` | 1 | 0 | 0 | 0 | 1 | 0 | 0 |
| `010201210` | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| `010210120` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `010212010` | 0 | 0 | 2 | 0 | 0 | 0 | 0 |
| `010212012` | 0 | 0 | 1 | 1 | 0 | 0 | 0 |
| `010212021` | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| `012010201` | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| `012010210` | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| `012021012` | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| `012021201` | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| `012102120` | 0 | 0 | 0 | 0 | 0 | 2 | 0 |

Each row has weighted sum one, hence every source radius-one ball has total weight one. The nonzero weight has total

\[6+12+6+6+6+6+6=48.\]

Disjointness of radius-one balls gives \(M_9\le48\). Combined with the construction this proves \(M_9=48\), completing the shortest-length assertion.

## Verification
`CERTIFICATE.json` gives both perfect pairings, both rational received-orbit weight systems, and the five source-orbit representatives. `verify.py` is a Python 3 standard-library checker. Run `python3 verify.py` in a directory containing both files. It regenerates every square-free ternary word through length nine by testing all \(3^n\) strings, expands the alphabet/reversal orbits, checks both pairings, verifies exact rational covering for **all** source words at lengths eight and nine, checks both exact total weights, expands the 48 codewords and checks their square-freeness and every pairwise distance. It prints `VERIFY_OK` only when all assertions pass. No optimization solver or external package is needed to verify the proof.

The finite computations establish exactly the quantified finite result: they are not being extrapolated to arbitrary lengths.

## Relationship to prior work
Square-free ternary sequences are classical, and Currie (2012) studied long square-free morphic words and permutation-block factorization, not finite Hamming-distance-three code capacity. Buschmann and Bystrykh (2013) studied barcode error correction and constrained filtering, with quaternary DNA words, different filters, and heuristic search rather than this ternary square-free exact packing. Gasnikov and Shur (DLT 2016) studied wildcard-set flexibility in infinite square-free words, a different property than the pairwise separation of finitely many source words. Przybocki (2021) classified lengths permitting *delicate* words, where **all** one-symbol substitutions destroy square-freeness; that local property does not supply maximal collections separated by Hamming distance three. Published work on ternary homopolymer-free *non-overlapping* codes and on generic substitution-detecting non-overlapping codes imposes different constraints, so neither its numeric bounds nor equality cases imply the present result.

The theorem uses the standard Hamming-ball correspondence and elementary finite rational packing certificates; it does not claim those tools as new. Available literature comparisons have not established a previous exact \(M_9=48\) for this source, but an unindexed older equivalent calculation remains possible.

## Limitations
Only ternary labeled square-free words, single arbitrary substitutions with a known word boundary, and lengths up to nine enter the shortest-length statement. No assertion is made about insertion/deletion correction, four-letter DNA alphabets, unknown boundaries, longer-length optimums, or asymptotic rates. The length-eight bound \(M_8\le31\) is not asserted to be sharp. Earlier equivalent results may exist outside the inspected sources; the literature-priority comparison is qualified.

## References
- J. D. Currie, *Infinite ternary square-free words concatenated from permutations of a single word*, arXiv:1207.3445v1, first public 2012-07-14. https://arxiv.org/abs/1207.3445
- T. Buschmann and L. V. Bystrykh, *Levenshtein error-correcting barcodes for multiplexed DNA sequencing*, BMC Bioinformatics 14:272 (2013), published 2013-09-11. https://pmc.ncbi.nlm.nih.gov/articles/PMC3853030/
- D. Gasnikov and A. M. Shur, *What is the maximum flexibility of an infinite ternary square-free word?*, DLT 2016, LNCS 9840. https://doi.org/10.1007/978-3-662-53132-7
- B. Przybocki, *Lengths of Irreducible and Delicate Words*, arXiv:2108.06646 (2021). https://arxiv.org/abs/2108.06646
