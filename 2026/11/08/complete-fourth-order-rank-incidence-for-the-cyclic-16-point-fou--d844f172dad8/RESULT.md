# Complete fourth-order rank incidence for the cyclic 16-point Fourier transform

## Finding

Let \(G=\mathbb Z/16\mathbb Z\), \(\zeta=\exp(2\pi i/16)\), and \(F=(\zeta^{ab})_{a,b\in G}\), without a unitary scale factor. For two four-element subsets \(A,B\subseteq G\), write \(r(A,B)=\operatorname{rank}_\mathbb C F[A,B]\). These subsets are unordered internally, but the pair \((A,B)\) is ordered.

The complete rank census is:

| \(r(A,B)\) | Ordered pairs \((A,B)\) |
|---:|---:|
| 1 | 16 |
| 2 | 9,728 |
| 3 | 293,888 |
| 4 | 3,008,768 |
| Total | 3,312,400 |

Thus 303,632 restrictions are singular. Exactly 256 row sets have all their 1820 fourth-order restrictions nonsingular (are full spark). The full row-orbit distribution is below.

## Assumptions and scope

All ranks are over \(\mathbb C\), equivalently the cyclotomic field \(\mathbb Q(\zeta)\); the finite-field calculations below are exact witnesses to these ranks, not a change of characteristic in the statement. No normalization factor is applied to \(F\). Row sets and column sets range independently over the \(\binom{16}{4}=1820\) distinct four-subsets of \(G\). The affine group consists of maps \(x\mapsto ux+b\) with odd \(u\in G^\times\) and arbitrary \(b\in G\).

## Proof

**Affine reduction.** Translating a row set by \(b\) multiplies every column by a nonzero phase. Multiplying its elements by an odd unit \(u\) corresponds to a bijective multiplication of the column index set by \(u\). Hence the number of column partners of each rank depends only on the affine orbit of the row set. Exhaustive application of the 128 affine maps to the 1820 four-subsets yields the following disjoint 25 orbits. In each row, \(s\) denotes orbit size, while \(n_j\) is the number of four-element column partners having rank \(j\) for each *fixed* row set in that orbit.

| Row-set representative | \(s\) | \(n_1\) | \(n_2\) | \(n_3\) | \(n_4\) |
|:---|---:|---:|---:|---:|---:|
| \(\{0,1,2,3\}\) | 64 | 0 | 0 | 0 | 1820 |
| \(\{0,1,2,4\}\) | 128 | 0 | 0 | 28 | 1792 |
| \(\{0,1,2,5\}\) | 128 | 0 | 0 | 20 | 1800 |
| \(\{0,1,2,6\}\) | 128 | 0 | 0 | 28 | 1792 |
| \(\{0,1,2,7\}\) | 128 | 0 | 0 | 0 | 1820 |
| \(\{0,1,2,8\}\) | 128 | 0 | 0 | 156 | 1664 |
| \(\{0,1,2,9\}\) | 32 | 0 | 0 | 236 | 1584 |
| \(\{0,1,3,4\}\) | 64 | 0 | 0 | 52 | 1768 |
| \(\{0,1,3,5\}\) | 128 | 0 | 0 | 28 | 1792 |
| \(\{0,1,3,7\}\) | 128 | 0 | 0 | 28 | 1792 |
| \(\{0,1,3,8\}\) | 64 | 0 | 0 | 140 | 1680 |
| \(\{0,1,3,9\}\) | 128 | 0 | 0 | 156 | 1664 |
| \(\{0,1,3,12\}\) | 64 | 0 | 0 | 52 | 1768 |
| \(\{0,1,3,14\}\) | 64 | 0 | 0 | 0 | 1820 |
| \(\{0,1,4,5\}\) | 64 | 0 | 4 | 192 | 1624 |
| \(\{0,1,4,8\}\) | 128 | 0 | 4 | 408 | 1408 |
| \(\{0,1,4,9\}\) | 64 | 0 | 4 | 264 | 1552 |
| \(\{0,1,7,8\}\) | 32 | 0 | 0 | 236 | 1584 |
| \(\{0,1,8,9\}\) | 16 | 0 | 140 | 896 | 784 |
| \(\{0,2,4,6\}\) | 32 | 0 | 28 | 672 | 1120 |
| \(\{0,2,4,8\}\) | 64 | 0 | 28 | 768 | 1024 |
| \(\{0,2,4,10\}\) | 16 | 0 | 28 | 832 | 960 |
| \(\{0,2,6,8\}\) | 16 | 0 | 28 | 832 | 960 |
| \(\{0,2,8,10\}\) | 8 | 0 | 156 | 1088 | 576 |
| \(\{0,4,8,12\}\) | 4 | 4 | 408 | 1152 | 256 |

Each displayed row satisfies \(n_1+n_2+n_3+n_4=1820\), and the orbit sizes sum to 1820. Summing \(s n_j\) gives the announced global multiplicities.

**Exact cyclotomic decision.** For a square Fourier restriction of order \(r\le4\), expand its determinant by the permutation formula, obtaining a polynomial \(P(T)\in\mathbb Z[T]\) consisting of at most \(r!\) signed monomials. Reduce its exponents modulo 16 and use \(\zeta^8=-1\) to obtain a polynomial \(R(T)\) of degree at most seven whose coefficients have absolute value at most \(r!\le24\). The minimal polynomial of \(\zeta\) is \(\Phi_{16}(T)=T^8+1\). Thus \(P(\zeta)=0\) if and only if all eight coefficients of \(R\) vanish as integers. Testing the \(4\)-, \(3\)-, then \(2\)-minors and finally the nonzero entry gives the rank exactly, including every low-rank case.

**A distinct modular exactness lemma.** The field \(\mathbb F_{97}\) contains exactly eight elements of multiplicative order 16, all roots of \(T^8+1\). If \(R\) vanishes at all eight, it is identically zero over \(\mathbb F_{97}\), since its degree is at most seven. Each integer coefficient lies between \(-24\) and \(24\), so it must actually be zero over \(\mathbb Z\). Conversely, integer vanishing gives vanishing at all eight roots. Applied to every square minor of size at most four, this proves that the complex rank of a Fourier restriction equals the **maximum** of its eight ranks over \(\mathbb F_{97}\) obtained by substituting the eight primitive roots. This is a fully exact finite-field method, with no tolerance or unproved lifting assumption.

**Exhaustive finite certificate.** The accompanying standalone Python program enumerates all 1820 column four-subsets against the 25 affine row representatives, for exactly 45,500 representative pairs. It computes each rank by (i) cyclotomic integer determinant coefficients and (ii) eight finite-field Gaussian eliminations, asserting agreement pair by pair. It then checks the 25 complete orbit rows, their sizes, the rank totals, and the full pair count. The affine bijections show this certifies all 3,312,400 pairs, not a sample.

**Full-spark check.** Precisely three affine row orbits have \(n_4=1820\); their sizes are \(64,128,64\), summing to 256. This also agrees with the prime-power full-spark criterion of Alexeev, Cahill and Mixon: a four-subset must meet each residue class modulo four in exactly one point, yielding \(4^4=256\) such subsets.

## Verification

Run `python3 f16_exact_check.py` using Python 3 with no third-party packages. The expected final line prefix is `EXACT_F16_FOURTH_MINOR_TWO_METHODS_PASS`. The exact checker covers every orbit representative and every four-element column set in both independent arithmetical representations. It asserts the global rank vector \( (16,9728,293888,3008768)\), all 25 row orbit distributions, the affine partition, and the total \(1820^2\). Replaying an earlier unrelated computation is not part of the certificate.

## Relationship to prior work

Tao's prime-order uncertainty theorem [1] relates the nonvanishing of *all* Fourier minors to additive uncertainty on prime cyclic groups. It does not address this composite order. Alexeev, Cahill and Mixon [2, Theorem 9] determine which row-selected harmonic frames over a prime-power cyclic group are full spark, an all-or-nothing statement; it predicts the 256 fully nonsingular row sets above, but not the ranks and multiplicities of the remaining minors. A known classification of the near-consecutive four-row pattern \(\{0,1,2,4\}\) predicts 28 singular four-column partners at order 16, matching one line of the table; it does not imply the other 24 orbit rows. Other results on Walsh transforms of order 16 use the nonisomorphic group \((\mathbb Z/2\mathbb Z)^4\) and do not determine the cyclic table.

## Limitations

This is a complete, certified **finite** census for order 16 and minors of order four, not a general formula for all cyclic powers of two, other minor sizes, or determinant magnitudes. It does not prove historical uniqueness; an unlocated table or stronger theorem about these exact minors could cover the counts. Numerical direct checks alone would not suffice, but the included arithmetic is exact and exhaustive. No independent mathematical audit is claimed.

## References

[1] T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, first submitted 29 August 2003; Lemma 1.3 and Theorem 1.1. https://arxiv.org/abs/math/0308286

[2] B. Alexeev, J. Cahill and D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first submitted 17 October 2011; Section 2, especially Theorem 9. https://arxiv.org/abs/1110.3548
