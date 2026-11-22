# The first super-half cut density of maximal closed substrings in binary words

## Finding

Let \(w=w_1\cdots w_n\) be a binary word. A nonempty word is **closed** if its length is one, or it admits a nonempty proper border that occurs exactly twice, at the beginning and end. An occurrence \([i,j]\) is a **maximal closed substring** (MCS) if it is closed and each available extension \([i-1,j]\) or \([i,j+1]\) is open. For a cut immediately after position \(g\), call \([i,j]\) a crossing occurrence when \(i\le g<j\). Define
\[
F_2(n)=\max_{w\in\{0,1\}^n}\max_{1\le g<n}\bigl|\{[i,j]: [i,j]\text{ is an MCS of }w,\ i\le g<j\}\bigr|.
\]

**Theorem (sharp first super-half boundary and rigidity).** The least length \(n\ge2\) for which \(F_2(n)>\lceil n/2\rceil\) is \(n=14\). In fact \(F_2(14)=8\), and exactly four pairs (binary word, one-based cut position) achieve eight crossings:

```
00101110100011  8
00111010001011  6
11000101110100  6
11010001011100  8
```

All four form a single orbit under reversal of the word (with cut position \(g\mapsto n-g\)) and bitwise complementation. The complete exact finite spectrum of maxima is
\[
(F_2(n))_{n=2}^{14}=(1,1,2,2,3,3,4,4,5,5,6,7,8).
\]
No claim is made for the sequence beyond \(n=14\), or for its asymptotic growth rate.

## Assumptions and scope

The alphabet is precisely \(\{0,1\}\); positions and cuts are one-based. Distinct MCS occurrences are counted separately even when their factor values agree. Missing extensions at the boundary are considered automatically maximal. A singleton does not cross a cut. A border may overlap itself, and the two occurrences are counted by distinct starting positions. The result is a complete, finite classification of words of lengths \(2\) through \(14\), not an infinite upper-bound theorem.

## Proof

The exact proof is an exhaustive finite disjunction, using the attached independently implemented complete checkers. Its completeness is elementary and does not rest on a sampling assumption. For each \(n=2,\ldots,14\), every length-\(n\) binary word is represented exactly once by an integer \(m\) satisfying \(0\le m<2^n\). For each such word every cut \(1\le g<n\) is tested. Every interval \([i,j]\) is tested for closedness by ranging over every proper border length \(1\le b<j-i+1\), requiring equality of the prefix and suffix, and counting all possible occurrences of that border, including overlapping occurrences. A border witnesses closedness exactly when this count is two; single letters are closed by definition.

A crossing interval is recorded exactly if it is closed, its endpoints straddle the cut, and neither of its existing one-letter extensions is closed. These are exactly the defining predicates, and no other cases exist. Thus taking the maximum over the finite loops proves the thirteen stated values of \(F_2(n)\) with no extrapolation. The same loops collect **all** length-14 pairs whose crossing count is at least eight. The output is exactly the four displayed pairs, establishing both uniqueness up to reversal/complement and exclusion of any length-14 pair with more than eight crossings. The thirteen maxima imply \(F_2(n)\le\lceil n/2\rceil\) for \(2\le n\le13\), and \(F_2(14)=8>7\), proving the least-length assertion.

For a separate, human-inspectable positive witness, the eight crossing MCS intervals of `00101110100011` at cut \(g=8\) are, in one-based inclusive coordinates,
\[
[1,11],\ [1,13],\ [2,10],\ [3,9],\ [4,14],\ [6,14],\ [7,10],\ [8,13].
\]
Their witnessing borders, in this order, are `00`, `001`, `010`, `101`, `011`, `11`, `10`, `01`. Testing the two available extensions of each gives open words. For the other three words the set of crossing intervals follows by reversal/complement symmetries. The independent checkers compute all intervals afresh rather than relying on this list.

## Verification

Two standalone programs implement different closedness tests: `verify_direct.py` compares literal strings, enumerating possible border occurrences in substrings; `verify_bits.cpp` precomputes closedness of every binary bit pattern of length at most fourteen and evaluates MCSs using bit shifts and difference arrays for crossing counts. Neither uses a look-up table of answers to generate its counts; expected outputs are only assertions at the end of the exhaustive enumeration. Both enumerate every word and every cut for lengths two through fourteen and verify the same four length-fourteen extremizers. They ran successfully in this package.

From the extracted package directory, run:

```
python3 verify_direct.py
c++ -O2 -std=c++17 verify_bits.cpp -o verify_bits
./verify_bits
```

Recorded outputs are `direct_output.txt` and `bits_output.txt`. The complete source plus exact input domain form the finite certificate. The output text alone is not a substitute for the source or for replay. No infinite statement is inferred from these finite checks.

## Relationship to prior work

Faro–Marino–Pavone [1], Section 7, prove at most \(3(n-1)\) MCSs crossing a cut and exhibit binary words with at least \(\lfloor(n-1)/2\rfloor\) crossings; they leave the optimal leading constant unknown. Their Proposition 14 construction is not an upper bound, and does not determine the first length exceeding the stronger benchmark \(\lceil n/2\rceil\) or classify its unique symmetry orbit. The result above is a finite refinement of that natural local-density question, not an improvement of the universal asymptotic lower constant. Fischer–Köppl [2] give an algorithm to enumerate MCSs of one supplied input; its generic algorithmic guarantee alone does not provide the all-binary-word extremal census stated here. The older MCS theory [3] supplies general definitions and algorithms rather than this cut-specific spectrum. Targeted published-record searches found no earlier explicit first super-half threshold or classification, but this is a best-knowledge originality assessment, not an impossibility assertion about unindexed work.

## Limitations

The threshold \(\lceil n/2\rceil\) is a motivated benchmark suggested by the known near-half-density construction, **not** a published conjectured upper bound. The theorem does not settle the asymptotic sharp constant in [1]. It is a finite exact certificate and an initial structural boundary, not a general algorithm faster than [1–3]. Independent mathematical audit has not been performed; literature coverage is limited to the sources and searches stated in the review. Program execution is reproducible with ordinary C++17 and Python 3; the proof of exhaustion relies on the explicit loops and exactness of the elementary string/bit operations.

## References

[1] Simone Faro, Francesco Pio Marino, and Arianna Pavone, *Internal Queries for Maximal Closed Substrings*, arXiv:2611.11552v1, 8 November 2026, https://arxiv.org/abs/2611.11552 (especially Section 7, Theorem 12 and Proposition 14).
[2] Johannes Fischer and Dominik Köppl, *Output-Sensitive Enumeration of Maximal Closed Substrings in Linear Space*, arXiv:2610.38114v1, 28 October 2026, https://arxiv.org/abs/2610.38114 (especially Sections 2–3).
[3] Golnaz Badkobeh, Alessandro De Luca, Gabriele Fici, and Simon J. Puglisi, *Finding maximal closed substrings*, Theoretical Computer Science 1060 (2026), article 115628, https://doi.org/10.1016/j.tcs.2025.115628 (definition and general enumeration; primary full text not verified).
