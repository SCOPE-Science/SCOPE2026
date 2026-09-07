# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# No diagonally cyclic Latin squares of order 10: the transversal/mate census is empty

## Abstract
We settle the lane-10 census by proving its ground set is empty. There is no
Latin square $L$ of order 10 with $L(i+1,j+1)=L(i,j)+1\pmod{10}$.
Hence the set $F$ of normalized DCLS(10) isotopy representatives is empty,
its transversal spectrum is empty, and its orthogonal-mate question is
vacuously decided. We give a two-line sum proof plus an independent exhaustive
check of all $9!=362880$ normalized $a$-vectors (0 pass, $\approx 0.3$ s,
replayable verifier included). This corrects the working presupposition of a
nonempty family with $\tau\in\{9,10\}$. No novelty is claimed for the
nonexistence argument itself (the $n$-odd restriction is classical); the
contribution is the certified, replayable empty census for $n=10$.

## 1. Definitions
Work over $\mathbb{Z}_{10}$ for rows, columns, symbols.
$L$ is diagonally cyclic (DCLS) if
$$L(i+1\bmod 10,\;j+1\bmod 10)=L(i,j)+1\bmod 10\quad\forall i,j.$$
Put $a_k=L(0,k)$.

## 2. Theorem
**Theorem.** No DCLS(10) exists. In particular there are zero normalized
DCLS(10) $a$-vectors, zero isotopy classes, and the transversal-number /
orthogonal-mate census over $F$ is empty.

**Lemma 1 (parametrization).** Any DCLS satisfies $L(i,j)=i+a_{j-i}$
(indices mod 10). Row-Latinity holds iff $a$ is a permutation of
$\mathbb{Z}_{10}$; column-Latinity holds iff $b_k:=a_k-k$ is a permutation.
*Proof.* Fix $d=j-i$. The diagonal orbit $\{(t,t+d):t\in\mathbb{Z}_{10}\}$
is generated from $(0,d)$ by $(i,j)\mapsto(i+1,j+1)$, so
$L(t,t+d)=L(0,d)+t$ by induction. Hence $L(i,j)=a_{j-i}+i$.
Fix $i$: $j\mapsto i+a_{j-i}$ is bijective iff $a$ is. Fix $j$ and write
$d=j-i$: $L(i,j)=j+(a_d-d)$, so $i\mapsto L(i,j)$ is bijective iff
$d\mapsto a_d-d$ is. ∎

Normalization $a_0=0$ (i.e. $L(0,0)=0$) is wlog: $L\mapsto L-c$ preserves
being Latin and diagonally cyclic, so any DCLS yields a normalized one.

**Proof of Theorem (sum invariant).** Suppose $L$ is a DCLS(10) with
parameters $a,b$ as in Lemma 1, both permutations if $L$ is Latin.
Any permutation of $\mathbb{Z}_{10}$ sums to
$0+1+\cdots+9=45\equiv 5\pmod{10}$. But
$$\sum_{k\in\mathbb{Z}_{10}} b_k=\sum_k a_k-\sum_k k\equiv 5-5\equiv 0\pmod{10}\ne 5.$$
So $b$ cannot be a permutation — contradiction. Hence no Latin $L$
satisfies the diagonal-cyclicity equation. The normalized search space is
therefore empty, and so is the isotopy quotient $F$. ∎

*Remark.* This is the $n=10$ case of the classical even-order obstruction
(Hall–Paige / "DCLS exist iff $n$ is odd"). We claim no originality for the
argument; we claim only a checked, replayable instance for $n=10$.

## 3. Machine certificate
Independent of the proof, we exhaust the normalized space:
$a_0=0$, $(a_1,\dots,a_9)$ ranging over all $9!=362880$ permutations of
$\{1,\dots,9\}$, testing whether $\{a_k-k\bmod 10\}$ is all of
$\mathbb{Z}_{10}$.

- `output/artifacts/run_enumeration.py` (bitmask test): scanned 362880,
  passes 0, 0.22 s.
- `output/artifacts/dcls10_squares.csv`: header-only, 0 data rows,
  SHA256 `b1d83639e7c4fcd57fb2865cd71b255b85f80d1ab8c9ae7f0736ae96727fa61e`.
- `output/artifacts/verifier.py` (independent set-based re-scan + CSV
  reload + checksum + sum-invariant assert): `total=362880 passes=0`,
  VERIFIED in 0.31 s.

Correctness cross-checks (guard against a vacuously-rejecting bug):
- Same checker finds normalized DCLS counts 1, 3, 19, 225 for
  $n=3,5,7,9$ (e.g. $(0,2,4,1,3)$ for $n=5$ builds a verified Latin,
  diagonally cyclic square) — `sanity_odd.py`.
- A brute-force maximum-transversal enumerator gives $\tau=5$
  (15 full transversals) on that $n=5$ example — `demo_transversal.py`.
  So the transversal toolchain works where inputs exist; for $n=10$ it
  has no inputs.

Replay: `python3 output/artifacts/verifier.py` (no dependencies, seconds).

## 4. Consequences for transversals and mates
- Isotopy classes: $|F|=0$. No canonical labels, autotopism orders, or
  lex-min strings to store.
- Transversal numbers: the spectrum $\{\tau(R):R\in F\}$ is the empty set.
  In particular there is no $R$ with $\tau=10$, $9$, or $\le 8$; the
  Ryser–Brualdi–Stein bound ($\tau\ge n-1$) holds vacuously on this family.
- Orthogonal mates: the decomposition question (partition 100 cells into
  10 disjoint full transversals) has zero instances; both the mate-positive
  and mate-negative subfamilies are empty. No DLX trees to log.
- The lane's expected spectrum "$9$–$10$ with at least one deficient class"
  and the fallback "first 50–200 classes" are refuted as presuppositions,
  not as computations: the completed enumeration has 0 classes.

## 5. What is NOT claimed
- Nothing about general (non-diagonally-cyclic) Latin squares of order 10,
  their transversals, or the Parker–Bose–Shrikhande OLS(10) pair, which is
  untouched by this result.
- Nothing about Ryser–Brualdi–Stein for $n=10$ in general.
- No new classification method; tripartite-graph canonical labelling and
  DLX mate decomposition were correctly not exercised (empty input), and
  their logs are vacuous rather than missing.
- Isotopy vs. main-class distinctions are moot for the empty set.

## 6. Artifacts
- `output/artifacts/dcls10_squares.csv` — empty census (header only).
- `output/artifacts/run_enumeration.py` — primary exhaustive scan.
- `output/artifacts/verifier.py` — independent replay script.
- `output/artifacts/sanity_odd.py` — odd-order positive controls.
- `output/artifacts/demo_transversal.py` — transversal toolchain demo.
