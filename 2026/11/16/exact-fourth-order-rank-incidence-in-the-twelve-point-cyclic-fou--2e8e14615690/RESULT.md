# Exact fourth-order rank incidence in the twelve-point cyclic Fourier transform

## Finding

Let \(\zeta=\exp(2\pi i/12)\), let \(F=(\zeta^{ab})_{a,b\in\mathbb Z/12\mathbb Z}\), and let \(\mathcal Q\) denote the \(\binom{12}{4}=495\) four-element subsets of the twelve residues. For every ordered pair \((R,C)\in\mathcal Q^2\), put \(r(R,C)=\operatorname{rank}_{\mathbb C} F[R,C]\). The *complete fourth-order rank distribution* is

\[
\boxed{(N_1,N_2,N_3,N_4)=(0,1224,39384,204417).}
\]

In particular, exactly \(40608\) of the \(245025\) restrictions are singular, of which \(1224\) have rank two and \(39384\) rank three. There are exactly \(24\) four-row choices for which **every** four-column restriction is invertible. The \(495\) four-row sets split into precisely \(21\) affine orbits, each having the following complete partner-rank profile, where the row representative and its three counts specify the rank of every four-column choice in aggregate:

| Row representative | Orbit size | Rank 2 | Rank 3 | Rank 4 |
|---|---:|---:|---:|---:|
| \(0,1,2,3\) | 24 | 0 | 0 | 495 |
| \(0,1,2,4\) | 48 | 0 | 15 | 480 |
| \(0,1,2,5\) | 48 | 0 | 3 | 492 |
| \(0,1,2,6\) | 48 | 0 | 39 | 456 |
| \(0,1,2,7\) | 12 | 0 | 66 | 429 |
| \(0,1,3,4\) | 24 | 0 | 51 | 444 |
| \(0,1,3,5\) | 24 | 0 | 27 | 468 |
| \(0,1,3,6\) | 24 | 0 | 90 | 405 |
| \(0,1,3,7\) | 48 | 0 | 63 | 432 |
| \(0,1,3,9\) | 48 | 0 | 99 | 396 |
| \(0,1,3,10\) | 12 | 0 | 72 | 423 |
| \(0,1,4,5\) | 24 | 3 | 96 | 396 |
| \(0,1,4,7\) | 24 | 0 | 105 | 390 |
| \(0,1,4,8\) | 24 | 3 | 204 | 288 |
| \(0,1,4,9\) | 12 | 3 | 168 | 324 |
| \(0,1,5,6\) | 12 | 0 | 69 | 426 |
| \(0,1,6,7\) | 6 | 30 | 240 | 225 |
| \(0,2,4,6\) | 12 | 15 | 240 | 240 |
| \(0,2,4,8\) | 12 | 15 | 288 | 192 |
| \(0,2,6,8\) | 6 | 39 | 312 | 144 |
| \(0,3,6,9\) | 3 | 90 | 324 | 81 |


These \(21\) rows are pairwise inequivalent under affine changes of row indices, and their orbit sizes sum to \(495\). In particular, only the first orbit is full spark; its orbit size is \(24\).

## Assumptions and scope

The matrix is the unnormalized complex DFT of the **cyclic** group of order twelve, rather than the Fourier transform of a different abelian group of order twelve. Row sets and column sets are selected independently, each with exactly four distinct residues; the order within a set is irrelevant to rank. Both sets are enumerated lexicographically in the verification scripts. Ranks concern complex linear independence and not finite-field rank by definition.

## Proof

**Exact finite-field-to-complex principle.** Let \(p\) be a rational prime with \(p\equiv1\pmod{12}\) and \(p>65536\), and let \(t\in\mathbb F_p\) have multiplicative order twelve. For any \(k\times k\) submatrix of \(F\) with \(1\le k\le4\), write its determinant as \(D\in\mathbb Z[\zeta]\). The four Galois embeddings of \(\mathbb Q(\zeta)\) map \(\zeta\) to the four primitive twelfth roots; each resulting matrix still has complex entries of unit absolute value. Hadamard's bound gives \(|\sigma(D)|\le k^{k/2}\) for every embedding, so
\[
|N_{\mathbb Q(\zeta)/\mathbb Q}(D)|\le k^{2k}\le 4^8=65536.
\]
If \(D\ne0\), this norm is a nonzero integer. Its reduction modulo \(p\) is the product of the four determinant evaluations at the four primitive order-twelve roots in \(\mathbb F_p\); if evaluation at \(t\) vanished, the norm would be divisible by \(p\), impossible by the bound. Conversely, a zero complex determinant clearly reduces to zero. Hence **every** square minor of size at most four vanishes over \(\mathbb C\) exactly when its reduction at \(t\) vanishes over \(\mathbb F_p\). By the minor criterion, the full \(4\times4\) complex rank equals its reduced rank, for every restriction; no tolerance or probabilistic lifting is used.

**Finite exhaustive step.** The standalone Python verifier uses \(p=65581\), \(t=62640\), and checks primality by trial division and \(t^{12}=1\), \(t^6=-1\), \(t^4\ne1\). It enumerates all \(495^2=245025\) ordered row/column pairs, performs Gaussian elimination over \(\mathbb F_p\), and asserts the four rank totals, the total, and the full-spark count. A separate C++ verifier repeats all \(245025\) restrictions over \(p=65557\), \(t=10574\); the same exactness lemma applies. Both programs calculate the same numbers and check their numerical assertions. These are independently parametrized exact calculations, not floating-point experiments.

**Complete affine profile.** The affine group \(r\mapsto ur+b\) has \(u\in\{1,5,7,11\}\) and \(b\in\mathbb Z/12\mathbb Z\). Translating row indices multiplies Fourier columns by nonzero factors, while multiplication by a unit permutes the column indices. Thus every affine row orbit has a common partner-rank profile. The Python program constructs the complete disjoint orbit partition, verifies \(21\) orbits and total size \(495\), confirms profile agreement for every member, and prints the full table shown above. Multiplication of each profile by its orbit size yields the four global totals.

## Verification

Run `python3 verify_fourier12.py` using Python 3 standard library. The final line is `EXACT_Z12_CHECK_PASS`. Optionally compile and run `verify_fourier12.cpp` with a C++17 compiler, for example `c++ -O2 -std=c++17 verify_fourier12.cpp -o check12 && ./check12`; its final line is the same. Both programs do primality and root-order tests. The integer-bound argument above converts every finite-field pivot decision into an exact statement over \(\mathbb C\). The supplied full table and the two source programs constitute a reproducible finite certificate for this claim.

## Relationship to prior work

Alexeev, Cahill and Mixon analyze full-spark harmonic frames and show that uniform distribution of rows across divisor classes is necessary; their prime-power sufficiency theorem does not supply the rank incidence at cyclic order twelve. An existing complete order-twelve full-spark classification establishes the **already known** count of \(24\) good four-row sets, a consistency check, but does not give the three-level rank incidence for all \(245025\) row-column pairs. Other exact fourth-order rank censuses concern the cyclic orders fifteen and sixteen; neither implies the mixed-prime-power order-twelve census. Delvaux and Van Barel's construction of maximal rank-deficient submatrices from subgroup block tilings and their Hamming-number analysis provide relevant structural background, but the full text inspected does not tabulate these specific ranks or the \(21\) incidence profiles. The exact-support uncertainty function at order twelve is a minimization across supports, not an incidence distribution of all four-by-four restrictions.

## Limitations

The claim is a complete finite result specifically for four-row/four-column submatrices of the unnormalized cyclic order-twelve Fourier matrix. It does not determine singular values, condition numbers, non-square restrictions, or analogous ranks for arbitrary Fourier orders. The certificate is computational but exhaustive and exact; no unaudited infinite extrapolation is used. Priority may still be affected by unindexed equivalent tables or full-text results not available in the inspected sources. Independent mathematical validation has not been performed.

## References

1. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548 (first public 2011-10-17), especially Section 2 and Theorem 9. https://arxiv.org/abs/1110.3548
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, technical report TW477 (November 2006) and Linear Algebra Appl. 426 (2007), 349–367. DOI:10.1016/j.laa.2007.05.009.
3. *Complete full-spark classification for the order-\(12\) DFT* (2026), online finding identifier `81a97859d04e`.
4. *Complete fourth-order rank incidence for the cyclic 16-point Fourier transform* (2026), online finding identifier `d844f172dad8`.
5. *Complete rank-incidence census for four-frequency Fourier sampling on the cyclic group of order fifteen* (2026), online finding identifier `6d1752cd1bea`.
6. *Exact-support Fourier uncertainty profile on the cyclic group of order twelve* (2026), online finding identifier `0b9ac16390cf`.
