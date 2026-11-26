# First integer-valued fractional-packing failure for one-asymmetric-error codes on Fibonacci words

## Finding

For every integer \(1\le n\le7\), let \(\mathcal F_n\) be the binary length-\(n\) words avoiding the contiguous factor `11`. For \(w\in\mathcal F_n\), let \(D(w)\) contain \(w\) and every word obtainable from \(w\) by replacing exactly one symbol `1` by `0`. A zero-error one-asymmetric-error code is a subset \(C\subseteq\mathcal F_n\) for which the sets \(D(w)\), \(w\in C\), are pairwise disjoint. Let \(M_n\) be the largest size of such a code. Let \(P_n\) be the maximum nonnegative fractional output-shadow packing weight, defined precisely below.

The complete initial values, in increasing order of \(n=1,\ldots,7\), are

| \(n\) | \(|\mathcal F_n|\) | \(M_n\) | \(P_n\) | Number of maximum codebooks |
|---|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 | 2 |
| 2 | 3 | 1 | 1 | 3 |
| 3 | 5 | 2 | 2 | 2 |
| 4 | 8 | 3 | 3 | 1 |
| 5 | 13 | 4 | 4 | 2 |
| 6 | 21 | 6 | 6 | 1 |
| 7 | 34 | **8** | **9** | **10** |

Thus seven symbols give the first strict gap between integral code size and the natural fractional packing optimum; notably \(P_7=9\) is itself an integer, so rounding the fractional bound down still fails. All ten labeled optimum size-eight codes contain the same six-word set

```
0010001  0100101  1000100  1001001  1010010  1010101
```

Each optimum is exactly this set together with one of the following ten two-word pairs:

```
0000000 0001010    0000000 0100010
0000000 0101000    0000000 0101010
0000010 0101000    0000010 0101010
0001000 0100010    0001000 0101010
0001010 0100000    0100000 0101010
```

Exactly four of these ten codebooks are fixed by coordinate reversal and the other six form three reversal pairs, so there are seven reversal classes.

## Assumptions and scope

All words have a *fixed* binary blocklength. The source constraint forbids adjacent `1`s in the original word; one-direction errors only change a `1` to `0`, so every received word remains in \(\mathcal F_n\). Zero errors are allowed. A receiver observes one output, not an entire list of possible outputs. The code is not required to be linear, constant weight, or invariant under reversal.

Formally, if \(D(w)\) denotes the output set, then

\[
P_n=\max\left\{\sum_{w\in\mathcal F_n}x_w:\quad x_w\ge0,\quad
\sum_{w:\,v\in D(w)}x_w\le1\quad(v\in\mathcal F_n)\right\}.
\]

Its dual is

\[
\min\left\{\sum_{v\in\mathcal F_n}y_v:\quad y_v\ge0,\quad
\sum_{v\in D(w)}y_v\ge1\quad(w\in\mathcal F_n)\right\}.
\]

The fixed finite range \(1\le n\le7\) is part of the theorem. No formula beyond that range is asserted.

## Proof

**Step 1: exact compatibility criterion.** For two distinct source words \(a,b\) let \(r(a,b)\) be the number of coordinates where \(a\) has `1` and \(b\) has `0`; analogously define \(r(b,a)\). A common output \(v\in D(a)\cap D(b)\) must be a coordinatewise subset of both sources, with at most one removed `1` from each. Hence \(r(a,b)\le1\) and \(r(b,a)\le1\). Conversely, when both inequalities hold, the coordinatewise intersection word \(a\wedge b\) is in both downward error balls (because it deletes precisely \(r(a,b)\) and \(r(b,a)\) ones). Therefore

\[
D(a)\cap D(b)=\varnothing\quad\Longleftrightarrow\quad
\max\{r(a,b),r(b,a)\}\ge2.
\]

Construct the undirected compatibility graph whose vertices are \(\mathcal F_n\), joining exactly such compatible pairs. Codes are precisely cliques. Enumerating the \(2^n\) binary words and retaining those without `11` gives \(|\mathcal F_n|=F_{n+2}\), where \(F_0=0\), \(F_1=1\) and the sequence obeys the Fibonacci recurrence.

**Step 2: complete integer census.** The program `CHECK.py` constructs every individual set \(D(w)\), checks compatibility against the above independent count criterion for every pair, and applies the Bron–Kerbosch recursion with pivoting. Its recursion is exhaustive: for a current clique \(R\) and disjoint sets \(P,X\) of candidate and excluded vertices, any maximal clique extending \(R\) has at least one new vertex outside the neighbors of a chosen pivot in \(P\cup X\). Branching on each such vertex, moving it from \(P\) to \(X\) after processing, lists each maximal clique exactly once. Thus the largest listed clique is the global optimum, not a lower-bound search result. The complete maximum and equality counts for each \(1\le n\le7\) are those in the table. In particular, among the 34 seven-bit vertices there are exactly 1,398 inclusion-maximal cliques, of which precisely ten have eight vertices and none has nine.

The program `ALTERNATE.cpp` builds the seven-bit compatibility graph independently from integer bitmasks and evaluates the same exhaustive maximal-clique principle in bitset form. It confirms 1,398 maximal cliques, ten size-eight maxima, the six forced words and four reversal-fixed optima. The two separate implementations agree on the claimed finite census.

**Step 3: exact fractional optimum.** The file `CERTIFICATES.json` supplies feasible nonnegative rational weights \(x\) and \(y\) for the above primal and dual programs at every \(n=1,\ldots,7\). `CHECK.py` validates every output inequality, every input inequality, nonnegativity and equality of objectives using arbitrary-precision rational arithmetic. For \(n\le6\), primal and dual objectives equal the integer maxima in the table. At \(n=7\), the nonzero primal entries are

```
0000000:1    0001010:1/2    0010001:1
0100010:1/2 0100101:1      0101000:1/2
0101010:1/2 1000100:1      1001001:1
1010010:1   1010101:1
```

and the nonzero dual entries are

```
0000000:1    0000101:1    0001001:1
0001010:1    0010000:1    0100000:1
1000000:1    1010000:1/2  1010001:1/2
1010010:1/2  1010100:1/2
```

Both sums equal \(9\), and all 34 primal and all 34 dual constraints are explicitly checked. Weak duality makes both optimal, proving \(P_7=9\). This is independent of the clique upper bound \(M_7\le8\). The listed eight-word code supplies \(M_7\ge8\), completing the sharp assertion and the first-gap statement.

**Step 4: equality and reversal.** Intersecting the ten explicitly enumerated maximum cliques yields exactly the six printed core words, and subtracting this core yields precisely the ten printed tails. For each optimum, reverse all coordinates in every word and compare the resulting set. Exactly four optima are fixed. By Burnside's lemma for the order-two reversal action, the number of orbits is \((10+4)/2=7\).

## Verification

Run `python3 CHECK.py` in a directory containing `CERTIFICATES.json`. This uses only Python's standard library. Independently compile and run `g++ -O2 -std=c++17 ALTERNATE.cpp -o alternate && ./alternate`. Both commands reconstruct the objects rather than loading a table of results; the Python program also verifies rational certificates and the complete first-gap sequence. Successful runs terminate with `VERIFY_OK` and `ALTERNATE_OK`, respectively. No external solver, floating-point optimization, or network connection is needed for verification.

## Relationship to prior work

The single-asymmetric-error channel and checksum constructions appear in Varshamov and Tenengol'ts (1965). The binary words avoiding `11` are the vertices of Fibonacci cubes, as studied, for example, by Mollard (2012). Castro, Klavžar, Mollard and Rho (2011) computed *2-packings* of Fibonacci cubes, where pairwise graph distance must exceed two; their value for dimension seven is six, not eight. That is a strictly different constraint: 2-packing forbids some same-direction error-ball-disjoint pairs. Ashrafi and collaborators study **perfect Hamming-neighborhood codes**, not the present asymmetric packing optimum. Rameshwar and Kashyap (2023) develop constrained Hamming-distance coding bounds for bit flips/erasures, which also do not determine the downward one-error incidence system. A published index result on *single deletion* from Fibonacci-constrained binary words likewise concerns a different, shortening error channel. None of these inspected comparisons determines the current \(M_7\), \(P_7\), or the ten asymmetric-error equality cases.

## Limitations

The assertion is only for \(1\le n\le7\); there is no inferred all-length recurrence or asymptotic capacity. The general symmetric-distance 2-packing theorem cannot be used as an upper bound for this downward-error channel. The fractional dual bound of nine does *not* prove the sharp integer upper bound eight: that depends on complete graph search. Identifying ten equality cases depends on exhaustive enumeration, not on sampling or a timed optimization cutoff. The computations and independent implementations constitute a finite mathematical certificate, not an external expert audit. An earlier unindexed exact asymmetric finite case cannot be ruled out, and a small number of potentially related works were available only through abstracts or summaries.

## References

1. R. R. Varshamov and G. M. Tenengol'ts, “Code Correcting Single Asymmetric Errors,” *Avtomatika i Telemekhanika* 26 (1965), 288–292. Original text: https://m.mathnet.ru/php/getFT.phtml?jrnid=at&option_lang=eng&paperid=11293&what=fullt .
2. A. Castro, S. Klavžar, M. Mollard and Y. Rho, “On the domination number and the 2-packing number of Fibonacci cubes and Lucas cubes,” *Computers & Mathematics with Applications* 61 (2011), 2655–2660. https://doi.org/10.1016/j.camwa.2011.03.012 ; open author PDF: https://www-fourier.ujf-grenoble.fr/~mollard/accepte/FibonacciLucas5.pdf .
3. M. Mollard, “Maximal hypercubes in Fibonacci and Lucas cubes,” first arXiv version dated 2012-01-06. https://arxiv.org/abs/1201.1494 .
4. A. R. Ashrafi, J. Azarija, A. Babai, K. Fathalikhani and S. Klavžar, “The (non-)existence of perfect codes in Fibonacci cubes,” preprint (2015). https://users.fmf.uni-lj.si/klavzar/preprints/Fibonacci-PC-Sept-26-2015.pdf .
5. V. A. Rameshwar and N. Kashyap, “Estimating the Sizes of Binary Error-Correcting Constrained Codes,” arXiv:2301.05098 (2023). https://arxiv.org/abs/2301.05098 .
