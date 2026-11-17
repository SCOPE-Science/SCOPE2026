# Four-factor certificates and exact optimal-attractor populations for binary two-run powers

## Finding

Let \(a,b\ge 1\), \(t\ge2\), \(p=a+b\), and \(W=(0^a1^b)^t\). A string attractor \(\Gamma\) is any subset of the positions of \(W\) such that every nonempty factor of \(W\) has an occurrence crossing at least one position of \(\Gamma\). A factor \(u\) is *covered* if some occurrence of \(u\) crosses \(\Gamma\).

**Exact factor certificate.** For every subset \(\Gamma\subseteq\{1,\ldots,tp\}\), with no restriction on its cardinality,
\[
\Gamma\text{ is a string attractor of }W
\quad\Longleftrightarrow\quad
0^a,\ 1^b,\ 01,\ 10\text{ are all covered.}
\]
For \(a,b\ge2\), no one of these four tests follows from the other three. If \(\min(a,b)=1\), the \(01\) test follows from the unary tests, and the remaining three tests are irredundant.

**Complete optimal-attractor classification.** Every such \(W\) has minimum attractor size \(\gamma(W)=2\). The number \(N(a,b,t)\) of distinct two-position attractors is exactly
\[
N(a,b,t)=
\begin{cases}
2t(t-1),&a,b\ge2,\\
(t-1)(bt+1),&a=1,\\
(t-1)(at+1),&b=1.
\end{cases}
\]
The last two branches agree when \(a=b=1\), giving \(t^2-1\). Explicit positions are given in the proof. The all-cardinality certificate and the uniform count for arbitrary \(t\) are the principal content; the two-copy and alternating specializations are included for completeness, not asserted as previously unknown cases.

## Assumptions and scope

All positions are one-based and inclusive. Parameters \(a,b,t\) are integers in the stated ranges; \(p=a+b\) is the primitive run period and \(|W|=tp\). The word is linear, not circular, and factors are contiguous, not scattered. A position in a factor occurrence is covered when it belongs to that occurrence's closed interval. Nothing is assumed about the shape or size of the candidate position set \(\Gamma\).

## Proof

**Lemma 1 (long-factor coverage).** Suppose that \(u\) is a factor of \(W\) of length \(\ell\ge p\). Choose the leftmost occurrence of \(u\), whose starting position \(s\) satisfies \(1\le s\le p\): otherwise the occurrence could be shifted left by one full period. All shifts of that occurrence to the right by multiples of \(p\) that fit inside \(W\) are further occurrences. Their closed position intervals overlap or meet because \(\ell\ge p\). The first such interval starts by position \(p\), and the last must end at or after \((t-1)p+1\), since otherwise one more period-shift would fit. Their union therefore contains the entire interval
\[
[p,(t-1)p+1].
\]
Any position crossing an occurrence of \(10\) belongs to this central interval: the \(10\) transitions occur precisely at \((hp,hp+1)\), \(1\le h<t\). Thus, if \(10\) is covered, then \(u\) is covered. The use of an interval union is valid because the shifted occurrences have no gaps, not merely because the word is periodic.

**Lemma 2 (short-factor coverage).** Let \(u\) have \(1\le|u|<p\).

If \(u\) is unary, it has form \(0^r\) with \(r\le a\) or \(1^s\) with \(s\le b\). A marked position in a copy of the corresponding maximal run can be included in some shorter unary subinterval, so coverage of \(0^a\) and \(1^b\) covers all unary factors.

If \(u\) is mixed and contains \(10\), align that \(10\) with a covered interperiod transition \((hp,hp+1)\). The infinite \(p\)-periodic continuation has identical letters at identical offsets from every such transition, so the aligned substring equals \(u\). Since \(|u|<p\), it needs fewer than \(p\) positions on either side, and an internal transition of \(W\) has enough surrounding letters. Consequently this occurrence stays inside \(W\) and crosses the chosen marked position of \(10\).

If \(u\) is mixed and has no \(10\), it necessarily has form \(0^r1^s\), where \(1\le r\le a\) and \(1\le s\le b\). Align its single transition with a covered \(01\) transition \((hp+a,hp+a+1)\), \(0\le h<t\). Each such transition has \(a\) zeros immediately before and \(b\) ones immediately after, so the occurrence is valid and crosses the selected marked position.

By Lemmas 1 and 2, coverage of all four listed factors is sufficient. Their necessity is immediate from the definition of an attractor. This proves the equivalence for every position set, including the empty set and sets larger than two positions.

**Irredundance.** For all parameters, the other three factors can be covered while \(0^a\) is not: take \(\{a+1,p\}\), a subset entirely in \(1\)-runs, which covers \(1^b\), \(01\), and \(10\), but not \(0^a\). Similarly \(\{a,p+1\}\) lies entirely in \(0\)-runs and covers \(0^a\), \(01\), and \(10\), but not \(1^b\). The set \(\{1,tp\}\) covers the two maximal unary factors and \(01\), but cannot cross any interperiod \(10\). If \(a,b\ge2\), \(\{p,p+1\}\) covers the two maximal unary factors and \(10\), yet neither point lies in an occurrence of \(01\). Thus all four are irredundant when both run lengths exceed one. If \(a=1\), every occurrence of \(0\) belongs to an \(01\), and if \(b=1\), every occurrence of \(1\) belongs to an \(01\). Therefore the \(01\) condition is redundant when \(\min(a,b)=1\), while the three preceding witnesses still prove irredundance of the other tests.

**Minimum size and counts.** At least two positions are necessary since both letters occur and a single position cannot cover both one-letter factors. The descriptions below exhibit two-position attractors, so \(\gamma(W)=2\).

If \(a,b\ge2\), an occurrence of \(01\) has endpoints \((a+ip,a+ip+1)\) for \(0\le i<t\), and an occurrence of \(10\) has endpoints \((jp,jp+1)\) for \(1\le j<t\). All these endpoint pairs are disjoint, hence a two-position attractor must select one endpoint of each transition type. To cover both unary maximal runs, the two selected endpoints must have different symbols. Exactly two choices are possible: the two left endpoints, or the two right endpoints. Thus the complete position-pair family is
\[
\{a+ip,jp\}\quad\text{or}\quad\{a+ip+1,jp+1\},
\quad 0\le i<t,\quad1\le j<t.
\]
Each family contains \(t(t-1)\) different sets and the families are disjoint, proving \(2t(t-1)\).

If \(a=1\), the zero positions are \(z_h=1+hp\), \(0\le h<t\). Every \(z_h\) for \(h\ge1\) simultaneously crosses an occurrence of \(10\) and an occurrence of \(01\). Consequently pairing any such internal zero with any of the \(bt\) one positions yields an attractor: it covers all four required factors. This contributes \((t-1)bt\) pairs. The first zero \(z_0=1\) covers \(01\) but not \(10\); it can be paired with the last one of any nonfinal one-run, whose positions are \(jp\), \(1\le j<t\). These provide exactly \(t-1\) further pairs. There are no other pairs because a two-position attractor must contain one zero and one one. Hence \((t-1)(bt+1)\).

The case \(b=1\) follows by reversing the word and exchanging its two letters. This bijects its attractors with those of \((01^a)^t\), giving \((t-1)(at+1)\). The argument includes \(a=b=1\) with no double-counting.

## Verification

Run `python3 verify_attractors.py` with the standard Python 3 library. It constructs occurrence-union bitmasks for **every distinct factor**, compares the actual attractor condition against the four-factor certificate for **all** position subsets on \(37\) parameter triples with \(|W|\le15\) (\(330960\) subsets), and independently compares the stated pair counts across \(150\) parameter triples with \(1\le a,b\le5\), \(2\le t\le7\). The reported checks passed. These finite tests are diagnostic only: the proof above supplies the all-parameter quantifiers. The check script and its source must be extracted from this package before replay.

## Relationship to prior work

Banbara, Bannai, Guo, Köppl, Mieno and Okamoto (first public preprint February 18, 2026; expanded October 2026) completely classify smallest attractors for finite Fibonacci, period-doubling and, in the expanded version, Thue–Morse words. They do not classify \((0^a1^b)^t\) or give an arbitrary-cardinality certificate for this periodic family. Mantaci, Restivo, Romana, Rosone and Sciortino (2019, Proposition 4 and Example 7) give a bound for attractors of powers of general words and observe optimal size two for a two-run word, not the stated uniform all-power counts or factor certificate. Faro, Marino and Pavone (October 7, 2026) study coverage certificates for Thue–Morse words, not the present periodic family. General attractor-checking algorithms of Béal, Crochemore and Romana (2025) apply to all strings but do not state this four-test characterization.

The alternating \(a=b=1\) subcase and the two-copy \(t=2\) size-two classification overlap earlier published computations; the novelty claim is the uniform \(a,b,t\) family, exact counts beyond those specializations, and characterization for **all** marker-set sizes. This separation is important: a known special case is not presented as a new independent result.

## Limitations

The word must be a complete positive power of a two-run binary block. The result makes no claim for arbitrary primitive periods, nonintegral truncations, circular attractors, or larger alphabets. The certificate has at most four natural factor tests, and is irredundant *within that set* when both run lengths exceed one; no global minimum number of arbitrarily chosen test factors is asserted. Experimental samples are finite, and historical priority has not been independently certified.

## References

1. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, first public arXiv version 2026-02-18, https://arxiv.org/abs/2602.16152; CPM 2026, DOI https://doi.org/10.4230/LIPIcs.CPM.2026.33.
2. S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *String Attractors and Combinatorics on Words*, 2019, https://arxiv.org/abs/1907.04660, especially Proposition 4 and Example 7.
3. S. Faro, F. P. Marino, A. Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue--Morse Words*, first public 2026-10-07, https://arxiv.org/abs/2610.10950.
4. M.-P. Béal, M. Crochemore, G. Romana, *Checking and Producing Word Attractors*, first public 2025-09-10, https://arxiv.org/abs/2509.08503.
