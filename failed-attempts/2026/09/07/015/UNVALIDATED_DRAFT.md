# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified partial GF(5) census for rank-4 8-element matroids: 18 types with explicit coordinatizations and excluded-minor witnesses

## 1. What is proved (and what is not)

**Proved (Theorem, machine-checked).** There exist 18 pairwise non-isomorphic
matroids of rank 4 on ground set {0,…,7}, partitioned as:

- (R) 12 GF(5)-representable, each with an explicit 4×8 matrix `[I4|A]`
  over GF(5) whose 4×4 non-zero minor pattern equals exactly the claimed
  bases (verified by exact determinant enumeration) and whose Plücker
  coordinates satisfy all (3,5) Grassmann–Plücker relations (3136/3136 each);
- (N) 6 non-GF(5)-representable, each with an explicit minor witness
  `(D,C,reference,permutation)` where the minor is isomorphic (by the given
  permutation, verified by brute force) to a reference obstruction whose
  non-GF(5)-representability is proved from first principles:
  the Fano plane F7 (backtracking UNSAT), its dual F7* (duality lemma),
  or the Vámos matroid V8 (Ingleton violation).

All 18 satisfy the basis-exchange axioms (brute-force verified), have
pairwise distinct isomorphism invariants `(number of bases, sorted degree
sequence)` hence are pairwise non-isomorphic, have valid rank-4 8-element
duals with dual-of-dual involution, and for each representable member the
number of normalized `[I|A]` realizations with fixed basis {0,1,2,3} modulo
per-column scaling is exactly the reported integer (exhaustive backtracking).

Replay: `python3 output/artifacts/replay.py` (stdlib only) replays every
check. On the test machine: **95/95 PASS in ~0.5 s**.

**Not proved.** This is *not* the complete M(4,8) census (which has
thousands of types and needs the Mayhew–Royle 7/9-element database plus the
564-member GF(5) excluded-minor list, neither available offline here).
No completeness, no enumeration-closure, and no inequivalent-representation
tally in the Hydra-5 projective sense is claimed. Uniform U(4,8) is
deliberately absent: it needs q≥7 (MDS / q+1 bound) and is non-GF(5); its
UNSAT certificate over 5^16 is not attempted. The invariant hash below is
sound but incomplete (see §6).

## 2. Prior work (originality delta)

Mayhew–Royle give the abstract catalogue to 9 elements without per-stratum
GF(5) matrices/witnesses/hashes/checker. Brettell et al. count GF(5)
excluded minors (564 on ≤9 elements) and Hydra-5/3-regular theory predicts
six GF(5) representations for 3-connected matroids with a U(2,5)-minor, but
neither publishes a per-matroid rank-4 8-element matrix-plus-witness
artifact. Our delta is constructive and partial: 18 closed types with
replayable certificates plus a verified pipeline (hash/matrix/minor/duality/
fixed-basis counts) reusable toward the 10-element program. No novelty is
claimed for Fano/Ingleton/duality facts themselves.

## 3. Definitions and conventions

Ground sets are {0,…,6} (rank-3 references) or {0,…,7} (rank-4 catalogue).
A matroid is given by its family B of r-subsets (bases). Rank:
r(A)=max_{B∈B}|A∩B|. Dual: B*={E\B}. Deletion M\e via independent sets
(maximal e-free subsets of bases; handles loops/coloops). Contraction M/e:
{B\{e}:e∈B} (non-loop) else deletion. Isomorphism: permutation with
image family equal. Representability: some r×n matrix over GF(5) whose
r×r non-singular column sets equal B. Any representation with basis
B0={0,…,r-1} can be row-reduced to [I|A] (left-multiply by the inverse of
the B0-submatrix); column scaling by nonzero preserves the matroid.

## 4. References (first-principles obstructions)

**Fano F7.** Ground {0,…,6}, rank 3. Non-bases (lines):
013,124,235,346,045,156,026 (sorted). Bases: other 28 triples.
Brute-force exchange holds (28 bases). {0,1,2} is a basis.
*Lemma (machine).* No [I3|A] over GF(5) realizes F7. Proof: exhaustive
backtracking over the 12 entries of A with early pruning on 1×1/2×2/3×3
minor constraints gives 0 solutions, both with column-scale normalization
(first nonzero per column =1, sound since scaling preserves zero-pattern)
and without (0.00 s / 0.06 s in replay). Since any representation normalizes
to [I|A] on the basis {0,1,2}, F7 is not GF(5)-representable. Human gloss:
coordinatizing forces the Fano configuration, which needs 1+1=0 (char 2);
over GF(5) the determinant system is unsatisfiable, as the machine confirms.

**Dual F7*.** B*={complements of F7 bases}, rank 4 on 7 points, 28 bases,
all degrees 16. *Lemma.* Duality preserves GF(5)-representability: if
M=[I|A] then M*=[-A^T|I] realizes the dual (standard orthogonal-complement
argument; ranks/determinants transpose). Hence F7* non-GF(5) follows from F7.

**Vámos V8.** Ground {0,…,7}, rank 4. Non-bases (5 circuit-hyperplanes):
0123,0145,2345,2367,4567. Bases: other 65 quadruples. Exchange holds.
Degrees (32×4,33×4). *Lemma (Ingleton 1971, cited, not re-proved).*
Representable matroids satisfy for all A,B,C,D:
r(A)+r(B)+r(A∪B∪C)+r(A∪B∪D)+r(C∪D)
 ≤ r(A∪B)+r(A∪C)+r(A∪D)+r(B∪C)+r(B∪D).
*Computed violation.* With A={2,3},B={4,5},C={0,1},D={6,7}:
ranks are 2,2,4,4,4 (LHS=16) vs 3,3,3,3,3 (RHS=15); 16≤15 false.
Rank values are table lookups from the 65 bases (replay recomputes).
Hence V8 is not representable over any field, in particular GF(5).
Remark: the sixth cube face 0167 is a basis (rank 4) while the other five
faces have rank 3; any vector realization would force the sixth to be a
plane — the bundle failure.

U(2,7) is noted but *not used*: it cannot be a single-element minor of any
(4,8) matroid (rank would drop by 2 while deleting one element).

## 5. Catalogue

### 5.1 Representables (12, explicit A with M=[I4|A], identity on 0–3)

| name | nb | sorted degrees | A (rows) | norm. orbits* |
|------|----|----------------|----------|---------------|
| R35 | 35 | 13,13,14,14,19,21,23,23 | [0,0,0,4],[0,4,2,1],[0,4,2,4],[2,3,4,2] | 192 |
| R39 | 39 | 14,14,17,18,20,21,26,26 | [0,3,2,1],[4,0,2,0],[0,0,4,0],[3,1,3,0] | 192 |
| R40 | 40 | 14,14,17,19,21,21,27,27 | [1,2,4,0],[3,4,3,3],[2,4,4,0],[3,1,2,0] | 384 |
| R45 | 45 | 16,16,22,22,23,23,29,29 | [0,1,4,3],[4,1,4,2],[3,4,1,1],[1,3,2,2] | 384 |
| R46 | 46 | 19,19,21,21,23,23,29,29 | [4,4,4,4],[0,1,1,0],[1,3,0,2],[4,0,0,0] | 384 |
| R49 | 49 | 21,22,22,22,23,24,31,31 | [0,2,0,0],[2,2,1,3],[4,2,1,0],[4,0,4,1] | 384 |
| R50 | 50 | 21,22,22,23,23,25,32,32 | [2,3,1,2],[0,3,4,2],[4,3,4,1],[0,0,0,1] | 128 |
| R51 | 51 | 24,24,24,26,26,26,27,27 | [1,4,0,2],[0,3,3,3],[3,1,0,3],[0,3,3,4] | 576 |
| R54 | 54 | 23,25,26,27,27,28,29,31 | [0,0,2,4],[2,3,3,2],[3,0,0,2],[4,3,0,2] | 384 |
| R58 | 58 | 26,27,27,29,30,31,31,31 | [2,0,2,4],[1,4,3,0],[1,0,3,1],[0,1,3,4] | 256 |
| R60 | 60 | 28,29,29,30,31,31,31,31 | [4,3,1,4],[4,0,3,1],[2,0,1,4],[3,4,1,3] | 256 |
| R63 | 63 | 31,31,31,31,32,32,32,32 | [2,0,2,4],[3,4,1,2],[2,4,3,4],[3,4,0,3] | 64 |

*Normalized orbits = number of A′ with [I|A′] realizing the *same labeled*
bases, modulo scaling each of the 4 A-columns by GF(5)* (first nonzero per
column fixed to 1), counted by exhaustive backtracking (row-major, minor
constraints ordered 1×1 first). This is *fixed-basis* counting, strictly
finer than Hydra-5 projective classes (which also quotient by row ops,
ground-set automorphisms, and basis changes); numbers are therefore larger
than 6 and are not claimed to test the “six” prediction directly.

Evidence per R: axioms PASS; identity {0,1,2,3} is a basis; all 70 4×4
determinants recomputed with zero-pattern exactly the bases; all 3136
(3,5) Plücker relations hold with ordered signs
Σ_t(−1)^t·σ(I,jt)·p_{I∪jt}·p_{J∖jt}=0 (σ corrects sorted-vs-appended order).

### 5.2 Nonrepresentables (6, minor witnesses)

| name | nb | degrees | witness (D=delete, C=contract) | reference | perm |
|------|----|---------|-------------------------------|-----------|------|
| N-Vamos | 65 | 32×4,33×4 | direct Ingleton (no minor needed) | V8 itself (§4) | — |
| N-F7coloop | 28 | 12×7,28 | D={7},C={} | F7 | identity |
| N-F7starloop | 28 | 0,16×7 | D={7},C={} | F7* | identity |
| N-X44 | 44 | 16,16,24×6 | D={7},C={} | F7* | (0,1,2,4,6,3,5) |
| N-X48 | 48 | 20,24×6,28 | D={7},C={} | F7* | same |
| N-X56 | 56 | 28×8 | D={7},C={} | F7* | same |

Constructions: N-F7coloop bases = {B∪{7}:B∈F7} (coloop 7); N-F7starloop
bases = F7* bases (loop 7 in none); N-X** from binary matrices
[FSTAR2|v] over GF(2) with FSTAR2=[[0,1,1,1,0,0,0],[1,0,1,0,1,0,0],
[0,0,0,1,1,1,0],[0,0,1,1,1,0,1]] and v=(1,0,0,0)/(1,1,0,0)/(1,1,1,0).
Binary matrices guarantee matroid validity; deleting 7 recovers the binary
F7* (28 bases), mapped to combinatorial F7* by the listed permutation
(brute-force verified; the permutation sends binary F7* onto F7*).
Since F7/F7* are non-GF(5) and representability is minor-closed, all six
are non-GF(5). Note N-X44 is the parallel extension (v duplicates a column);
the combinatorial parallel extension is isomorphic to it, so only one copy
is listed to keep keys distinct.

Invariant hashes (SHA256 of nb|degrees|pair-counts|dual-degrees, 16 hex):
R35 16caefeb9acd369f, R39 b272bdee1638576e, R40 8e89a792db7b5553,
R45 5cf8bfcfefe69d68, R46 448f61b144e01ed4, R49 6ba3eab5628cf234,
R50 48e73749ed62ff81, R51 4371af955a5b29bb, R54 0831a8fe94743600,
R58 76a39a58e87158d6, R60 20ab5e5a281614d6, R63 7cb2366d88ccaf17,
Vamos e77416307f1c5ac2, F7coloop 9d9eda248a366c2b,
F7starloop 90abea38e6c0c1eb, X44 ccab1ec569c5082d,
X48 5aa28ea03640ced9, X56 71f1dc616ff74db6 — all 18 (nb,degree) keys
distinct, hence pairwise non-isomorphic (sound direction).

Duals: every dual is rank-4 on 8 points with equal nb; dual-of-dual is the
primal; no further self-duality claim beyond invariant matches.

## 6. Methods, checks, and limitations (separate)

*Proof* (human): duality lemma, Ingleton application with tabulated ranks,
normalization argument for [I|A], column-scaling orbit reasoning.
*Computed evidence* (machine): axioms, determinant basis-equality, Plücker,
S7 minor isomorphisms (5040 perms each), Fano UNSAT backtracking, fixed-basis
counts, hash/duality tables — all in replay.py, 95/95 PASS.
*Conjecture (not claimed):* the 12+6 extend to a full M(4,8) census with the
564-member obstruction list and Mayhew–Royle extension closure.
*Uncertainty/limits:* (i) hash uses only nb/degrees/pair/dual-degrees —
sound for distinctness but incomplete in general; completeness of
non-isomorphism here rests on the observed key separation, not on a general
canonical labeler; (ii) representation counts are fixed-basis, not Hydra-5
projective classes; (iii) Plücker verification is a sanity consequence of
coming from a matrix, not an independent coordinatization search;
(iv) no claim covers disconnected/looped/parallel types beyond the two
listed, nor U(4,8) (MDS-excluded), nor the 3-connected core closure.

## 7. How to replay

```
python3 output/artifacts/replay.py
```
Expected: `SUMMARY 95/95 checks passed`, `CATALOGUE 18 matroids:
12 representable + 6 nonrepresentable`, per-item PASS lines plus HASH lines.
No dependencies, no randomness (seeds fixed; catalogue hard-coded).
