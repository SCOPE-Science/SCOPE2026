# Complete minimal-diameter profile for five-point triple sumsets

## Finding

For a five-element set \(A\subset\mathbb Z\), let \(3A=\{a+b+c:a,b,c\in A\}\), allowing repeated summands, and let \(\operatorname{diam}(A)=\max A-\min A\). For any attainable cardinality \(s\), define the exact inverse diameter profile
\[
 m(s)=\min\{\operatorname{diam}(A):A\subset\mathbb Z,\ |A|=5,\ |3A|=s\}.
\]
Then the attainable cardinalities are \(\{13\}\cup[15,35]\cap\mathbb Z\), and **the complete profile** is given in the following table. The displayed set in each row attains the stated minimum.

| \(s\) | \(m(s)\) | A minimum-diameter example \(A\) |
| ---: | ---: | :--- |
| 13 | 4 | \(\{0,1,2,3,4\}\) |
| 15 | 5 | \(\{0,1,2,3,5\}\) |
| 16 | 5 | \(\{0,1,2,4,5\}\) |
| 17 | 6 | \(\{0,1,2,3,6\}\) |
| 18 | 6 | \(\{0,1,3,4,6\}\) |
| 19 | 6 | \(\{0,1,2,5,6\}\) |
| 20 | 7 | \(\{0,1,2,5,7\}\) |
| 21 | 7 | \(\{0,1,2,6,7\}\) |
| 22 | 7 | \(\{0,1,3,6,7\}\) |
| 23 | 8 | \(\{0,1,3,6,8\}\) |
| 24 | 8 | \(\{0,1,3,7,8\}\) |
| 25 | 8 | \(\{0,1,4,7,8\}\) |
| 26 | 9 | \(\{0,1,3,8,9\}\) |
| 27 | 10 | \(\{0,1,4,9,10\}\) |
| 28 | 11 | \(\{0,1,6,9,11\}\) |
| 29 | 11 | \(\{0,1,4,9,11\}\) |
| 30 | 12 | \(\{0,1,4,10,12\}\) |
| 31 | 13 | \(\{0,1,4,11,13\}\) |
| 32 | 14 | \(\{0,1,9,11,14\}\) |
| 33 | 16 | \(\{0,1,7,12,16\}\) |
| 34 | 19 | \(\{0,1,5,16,19\}\) |
| 35 | 23 | \(\{0,1,15,18,23\}\) |

In particular, every possible five-element triple-sumset cardinality is achieved by a set in \(\{0,1,\ldots,23\}\), and the interval diameter \(23\) is optimal; the sole cardinality requiring diameter \(23\) is \(s=35\). Under Nathanson's convention that \(N(h,k)\) counts the number of integer positions in the smallest sufficient initial interval \([0,N-1]\), this proves \(N(3,5)=24\). Under the inclusive-endpoint convention \([0,N]\), the corresponding value is \(23\).

The diameter-\(23\) normalized five-element sets with \(|3A|=35\) are **exactly**
\[
\begin{aligned}
&\{0,1,15,18,23\},\quad \{0,1,15,20,23\},\\
&\{0,3,8,22,23\},\quad \{0,5,8,22,23\}.
\end{aligned}
\]
They form two reversal pairs. Here normalized means \(\min A=0\) and \(\max A=23\); their common difference gcd is automatically \(1\).

## Assumptions and scope

All sets have five **distinct integers**; sums use exactly three elements, with repetitions allowed. Diameter is ordinary integer span. Translation preserves cardinality and diameter. Dividing every difference by its positive gcd preserves sumset cardinality while weakly reducing diameter. These observations ensure that enumeration of translated nonnegative sets is complete for any proposed diameter bound. The table is an exact finite theorem, not an asymptotic claim. Published work supplies the separate infinite-range statement that \(14\) is unattainable.

## Proof

**Step 1: determine the global cardinality spectrum.** Theorem 1.7 of Rajagopal, *Possible Sizes of Sumsets*, gives \(\mathcal R(3,k)=\{3k-2\}\cup[3k,\binom{k+2}{3}]\) for every \(k>2\). Taking \(k=5\) gives precisely \(\{13\}\cup[15,35]\cap\mathbb Z\). This is a cited theorem, not an inference from the finite search.

**Step 2: exhaustive certificate for all smaller diameters.** Translate a five-element set of diameter \(D\) to \(A=\{0,a,b,c,D\}\), where \(1\le a<b<c<D\). For \(D\le23\), these are exactly
\[
\sum_{D=4}^{23}\binom{D-1}{3}=\binom{23}{4}=8855
\]
sets. For each, determine \(|3A|\) by forming all \(\binom{7}{3}=35\) unordered triples with repetition, summing their elements and counting distinct values. The standalone verifier `verify.py` exhaustively computes the **first** diameter \(D\) at which each cardinality occurs. Its computed dictionary is identical, entry by entry, to the table above. It additionally computes \(|3A|\) by a separate shift-and-union bitset recurrence and asserts the two methods agree for each of the \(8855\) sets. Thus, for every \(s\) in the table, there is no five-element integer set with \(|3A|=s\) and diameter **smaller** than \(m(s)\).

**Step 3: witnesses and global conclusion.** Each row supplies an integer set of exactly the displayed diameter and triple-sumset size, checked by both implementations. Hence all \(22\) values in the published spectrum occur at diameter at most \(23\), and their claimed minima are global. In particular, every normalized set of diameter at most \(22\) gives at most \(34\) distinct triple sums, while the last row attains \(35\) at diameter \(23\); the least universal diameter is \(23\).

**Step 4: classify the extremizers.** Among the \(8855\) sets, the verifier records every one giving \(|3A|=35\). Exactly four occur, all with diameter \(23\), precisely as displayed above. Reversal \(A\mapsto23-A\) interchanges the first with the fourth and the second with the third, leaving two classes.

The certificate is exhaustive because every five-element set of span at most \(23\) can be translated into the enumerated family. Nothing about the unbounded spectrum, including the impossibility of \(14\), is inferred from enumeration alone.

## Verification

Execute `python3 verify.py` with the Python standard library (no external dependencies). The program independently compares two exact algorithms for all \(8855\) normalized sets of span at most \(23\), validates every row's witness, checks the entire profile, and lists the four extremizers. It reports `VERIFY_OK` only after all assertions succeed. Source files in this package contain the complete certificate and no external files are required.

## Relationship to prior work

Nathanson, *Compression and complexity for sumset sizes in additive number theory* (arXiv:2505.20998, initially public 2025-05-27), defines universal finite-interval compression and explicitly poses the calculation of \(N(h,k)\). His full text establishes general upper bounds, and gives \(N(3,3)=5\) under his interval-length convention, but not this five-point profile.

Rajagopal, *Possible Sizes of Sumsets* (arXiv:2510.23022, initially public 2025-10-27), proves the global cardinality spectrum, including the exclusion of \(14\) when \(h=3,k=5\). His results concern which cardinalities exist and asymptotic size bounds rather than the complete minimum-diameter profile for this pair. His Remark 1.8 uses the alternate inclusive-endpoint convention.

Zhang, *Exact diameter compression for four-point sumset cardinalities* (arXiv:2610.02216, initially public 2026-09-09), treats **four-element** sets for all orders, and makes the inverse-diameter problem concrete. This five-element, order-three result is not a corollary of Zhang's four-point classification. The two known strands motivate a five-point exact profile rather than an arbitrary small numerical search.

## Limitations

The proof for the finite minima and four extremizers is a complete executable finite exhaustion, not a uniform symbolic formula for general \(h\) or \(k\). The admissible cardinality spectrum relies on Rajagopal's published theorem. The optimal five-element \(B_3\)-ruler endpoint or individual examples may exist in older tables; this work claims the *complete 22-entry inverse diameter profile and its extremizer identification* as a single classification, not absolute priority for every individual number. Independent mathematical audit has not been performed.

## References

1. M. B. Nathanson, *Compression and complexity for sumset sizes in additive number theory*, arXiv:2505.20998, https://arxiv.org/html/2505.20998v2 (first public 2025-05-27).
2. I. Rajagopal, *Possible Sizes of Sumsets*, arXiv:2510.23022, https://arxiv.org/html/2510.23022v3 (first public 2025-10-27), especially Theorem 1.7 and Remark 1.8.
3. E. Zhang, *Exact diameter compression for four-point sumset cardinalities*, arXiv:2610.02216, https://arxiv.t3mt.com/html/2610.02216v1 (first public 2026-09-09), especially Theorem 1.1 and Table 4.
