# Exact inverse-diameter profile of six-point triple sumsets

## Finding
Let \(A\) range over all six-element subsets of \(\mathbb{Z}\), and let \(3A=\{a+b+c:a,b,c\in A\}\), where repetitions are allowed. For every attainable integer \(s\), define
\[
m(s)=\min_{|A|=6,\ |3A|=s}(\max A-\min A).
\]
The complete set of attainable cardinalities is \(\{16\}\cup[18,56]\) (the interval denotes its integer points). The exact inverse-diameter profile consists of the following forty values:

| Cardinality \(s\) | Minimum diameter \(m(s)\) | Cardinality \(s\) | Minimum diameter \(m(s)\) |
|---:|---:|---:|---:|
| 16 | 5 | 37 | 13 |
| 18 | 6 | 38 | 13 |
| 19 | 6 | 39 | 14 |
| 20 | 7 | 40 | 15 |
| 21 | 7 | 41 | 14 |
| 22 | 7 | 42 | 15 |
| 23 | 8 | 43 | 16 |
| 24 | 8 | 44 | 17 |
| 25 | 8 | 45 | 18 |
| 26 | 9 | 46 | 19 |
| 27 | 9 | 47 | 19 |
| 28 | 9 | 48 | 21 |
| 29 | 10 | 49 | 21 |
| 30 | 10 | 50 | 24 |
| 31 | 10 | 51 | 24 |
| 32 | 11 | 52 | 27 |
| 33 | 11 | 53 | 30 |
| 34 | 11 | 54 | 33 |
| 35 | 12 | 55 | 38 |
| 36 | 12 | 56 | 45 |

Every attainable six-point triple-sumset cardinality is realized by a set contained in \([0,45]\), and no interval of smaller diameter can realize all such cardinalities. With the inclusive-interval *length* convention \(N(3,6)\) of Nathanson's *Compression and complexity for sumset sizes in additive number theory*, in which the ambient set is \([0,N-1]\), this is the exact identity
\[
N(3,6)=46.
\]
With the *right-endpoint* convention \([0,N]\), the corresponding value is \(45\). The maximal cardinality \(|3A|=56\) has minimum diameter \(45\); its only two translation-normalized minimizers are
\[
\{0,2,11,26,42,45\},\qquad\{0,3,19,34,43,45\},
\]
which are reflections of one another. One further feature of the sharp profile is \(m(40)=15>14=m(41)\), so minimal diameter need not be monotone in sumset cardinality.

## Assumptions and scope
The ambient group is the additive group of integers, and all six set elements are distinct. Sums use exactly three elements with repetition. Translation preserves both \(|3A|\) and \(\max A-\min A\); dilation by a factor greater than one preserves cardinality but changes diameter and is not used in the minimization. The infinite-domain assertion concerning which \(s\) occur invokes Rajagopal's Theorem 1.7; the exact optimization at each admissible \(s\) is a finite exhaustive theorem.

## Proof
**1. Global cardinality spectrum.** Rajagopal proves for every integer \(k>2\) that the possible cardinalities of triple sumsets of integer sets with \(|A|=k\) are \(\{3k-2\}\cup[3k,\binom{k+2}{3}]\). For \(k=6\) this is precisely \(\{16\}\cup[18,56]\), so \(17\) is globally impossible, not merely absent from a bounded search.

**2. Exhaustive finite reduction.** Every six-point set of diameter at most \(45\) can be translated uniquely to a set \(\{0,a,b,c,d,e\}\) with \(1\le a<b<c<d<e\le45\). There are exactly \(\binom{45}{5}=1,221,759\) such sets. Conversely each five-tuple gives a valid normalized set, so the search is exhaustive for every candidate diameter below or equal to \(45\). For each set, all \(\binom{8}{3}=56\) unordered triples \(i\le j\le k\) are evaluated, and distinct values of \(a_i+a_j+a_k\) are counted. The minimum observed diameter at each size is displayed in the table. A machine-readable table with a diameter-minimizing witness for every size is in `profile.tsv`.

**3. Exactness and sharpness.** All forty globally possible sizes have explicit witnesses in `profile.tsv` and thus occur at diameter at most \(45\). Since the enumeration contains every normalized set of diameter smaller than any displayed minimum, no displayed value can be improved by a six-element integer set at any translation. The maximal sumset size \(56\) has no witness below diameter \(45\) and has precisely the two diameter-\(45\) witnesses shown above; thus the universal endpoint is exactly \(45\), and the least inclusive interval length is \(46\).

**4. Independent exhaustive implementations.** `verify.cpp` enumerates every normalized five-tuple by nested integer loops and constructs all triple sums using the \(56\) multisets of indices; their membership is stored in four 64-bit bitsets. Since the largest possible sum is \(3\cdot45=135<256\), these bitsets cover the entire domain exactly. `verify.py` independently enumerates the same tuple domain via `itertools.combinations`, encodes the original set as an unbounded integer bitset, computes \(2A\) and then \(3A\) via shifts and bitwise unions, and applies the exact `bit_count()` operation. Both independent algorithms return every tabulated minimum and exactly the same two diameter-\(45\) extremizers. The combinatorial counting and exhaustive searches, rather than sampling, constitute a finite proof of all listed minima.

## Verification
Run `python3 verify.py`; then compile `verify.cpp` with a C++17 compiler, for example `g++ -O2 -std=c++17 verify.cpp -o verify-cpp`, and execute `./verify-cpp 45`. The Python verifier independently asserts all forty minimum values, all normalized extremizers, and the exact \(\binom{45}{5}\) search count. The C++ executable prints a complete cardinality/minimum/witness listing and the same search count. Compare its forty rows with `profile.tsv`; cardinality \(17\) is intentionally absent from that table. A representative reproducible output log is `verification_output.txt`. The unbounded exclusion of \(17\) is a quoted published theorem and is not established by the finite enumeration.

## Relationship to prior work
Nathanson formulated explicit realization and compression questions for prescribed sizes of \(h\)-fold sumsets, including the least interval length \(N(h,k)\). His work gives general constructions and bounds, rather than this six-point inverse-diameter table. Rajagopal completely determines the possible triple-sumset cardinalities, but his Theorem 1.7 does not give the optimum diameter for each cardinality; his proof describes the global cardinality existence argument as nonconstructive. This result combines that independently established spectrum with a fully exhaustive and reproducible forty-case optimization. Examples of \(B_3\) sets may occur in earlier tables; the mathematical claim is the complete inverse-diameter spectrum, sharp universal interval, and exact normalized extremal list, not priority for the mere existence of one set.

## Limitations
This is an exact *finite* classification for \((h,k)=(3,6)\), not a general formula for arbitrary \(h,k\). The finite certificate relies on two fully inspectable and rerunnable exhaustive programs, not a formal proof assistant or independent audit. The existence range for unbounded integer sets is imported from Rajagopal's theorem. Earlier unindexed optimal \(B_3\) tables may contain individual extremizers and remain a historical-priority risk; there is no claim that unsuccessful searches certify uniqueness in the literature.

## References
1. Melvyn B. Nathanson, *Explicit sumset sizes in additive number theory*, arXiv:2505.05329, first public 2025-05-08; https://arxiv.org/abs/2505.05329 .
2. Melvyn B. Nathanson, *Compression and complexity for sumset sizes in additive number theory*, arXiv:2505.20998, first public 2025-05-27, especially Problems 2–3 and the definition of \(N(h,k)\); https://arxiv.org/abs/2505.20998 .
3. Isaac Rajagopal, *Possible Sizes of Sumsets*, arXiv:2510.23022, first public 2025-10-27, Theorem 1.7; https://arxiv.org/abs/2510.23022 .
