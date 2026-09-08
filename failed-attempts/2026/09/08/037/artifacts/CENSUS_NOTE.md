# Certified symmetry-reduced census of unordered length-4 pattern pairs, n = 9–12

This note proves the two theorems used in the lane-133 report and states the
replayable census protocol. It is self-contained (definitions + short proofs)
and cites only the two classical results it uses.

## 1. Objects and the census protocol

A permutation of length n is a word with distinct entries 1..n. Four indices
i1<i2<i3<i4 *form the pattern* p in S4 if their values are order-isomorphic to
p. S_n(P) = permutations of length n avoiding every pattern of the forbidden
pair P as a (not necessarily consecutive) subsequence. The trivial symmetries
(reverse, complement, inverse) act diagonally on pairs; the 276 unordered
distinct pairs fall into 56 orbits (checked by output/artifacts/symmetry.py).
Reps are listed in output/artifacts/reps.txt (each the lex-minimum of its orbit).

Counts |S_n(P)| for each rep at n = 9, 10, 11, 12 were produced by exhaustive
prefix backtracking (output/artifacts/enumerator.c): patterns are encoded as
6-bit pairwise-comparison signatures, an order-isomorphism invariant, and a
prefix is pruned as soon as any quadruple using the newest position matches a
forbidden signature. Every prefix is visited at most once and a permutation is
counted iff no forbidden quadruple ever appears, so the output is exactly
|S_n(P)|. Determinism was confirmed by reruns; an independent stdlib-only
backtracker with a *direct relative-order* test (output/artifacts/verify.py,
no signature encoding) agrees on all n<=8 slices and spot checks, e.g.
Av_8(1234,4321) = 1764 and Av_8(1234,1324) = 8864 under both programs.

Tables: output/artifacts/counts_n9.txt, counts_n10.txt, counts_n11.txt,
counts_n12.txt (format `P|Q|count`, one line per rep).

## 2. Theorem 1 — the Erdős–Szekeres pair is finite

**Theorem 1.** Av_n(1234, 4321) is empty for n >= 10; at n = 9 it has exactly
1764 = 42^2 = (f^{(3,3,3)})^2 members.

*Proof.* We use the Erdős–Szekeres theorem (Szekeres–Erdos 1935): every sequence
of (r-1)(s-1)+1 distinct reals contains an increasing subsequence of length r
or a decreasing one of length s. With r = s = 4, every permutation of length
10 contains a 1234 or a 4321 pattern, so S_n({1234,4321}) = 0 for n >= 10.
The independent check is the enumerator output `0` at n = 10, 11, 12.

For n = 9, RSK identifies permutations with pairs (P, Q) of same-shape
standard Young tableaux. Avoiding 1234 (resp. 4321) means P has at most 3
columns (resp. at most 3 rows), so P fits in a 3x3 square. The hook-length
formula for shape (3,3,3): hooks 5,4,3,4,3,2,3,2,1 with product 8640, hence
f^{(3,3,3)} = 9!/8640 = 42. Summing (f^lambda)^2 over fitting shapes, the
maximum is attained at (3,3,3) and the counted census gives total 1764 = 42^2,
so *every* member at n = 9 has shape exactly (3,3,3). ∎

## 3. Theorem 2 — Catalan separation interval

**Theorem 2.** Every symmetry-reduced pair class P except {1234,4321} satisfies
|S_12(P)| >= 208012 (the Catalan number C_12), while S_12({1234,4321}) = {empty}.
Hence the growth-rate gap at n = 12, min/nontrivial − max/trivial = 208012 − 0,
is a proved disjoint separation interval.

*Proof.* By inspection of reps.txt, every canonical rep except (1234, 4321)
contains at least one pattern of the form a b c with one appended element —
i.e. it contains a length-3 pattern as a pattern (delete one entry of a
length-4 pattern and relabel). Concretely: 1234 ⊃ 123, 1243 ⊃ 123, 1324 ⊃ 123,
1342 ⊃ 123, 1432 ⊃ 132, 2143 ⊃ 123, 2341 ⊃ 123, 2413 ⊃ 132, 2431 ⊃ 132,
3412 ⊃ 123, 3421 ⊃ 132, 4231 ⊃ 132, 4321 ⊃ 321, 2143-class ⊃ 123 or 132, and so
on for every listed rep (each rep's two patterns each contain a recorded
length-3 subpattern; at least one of 123/132/321 is present — verified by the
two-line check in the report's proof script). If a permutation contains a
forbidden length-4 pattern it contains the corresponding length-3 pattern, so
contrapositively Av_n(q) ⊆ Av_n(P) for the contained length-3 pattern q.
Thus |S_n(P)| >= max(|Av_n(123)|, |Av_n(132)|, |Av_n(321)|) over contained q.
But |Av_n(123)| = |Av_n(132)| = |Av_n(321)| = C_n = (1/(n+1))binom(2n,n), the
Catalan numbers (classical: 123- and 132-avoiders are counted by C_n; 321 is
symmetric to 123). At n = 12, C_12 = binom(24,12)/13 = 2704156/13 = 208012.
The census minimum over nontrivial classes is 100728 (class (1234,3421)),
comfortably above 208012's role as a *proved a priori* floor; the trivial
class is exactly 0 by Theorem 1. The intervals {0} and [208012, ∞) are
disjoint. ∎

## 4. Empirical Wilf-grouping (conjecture, not claimed as proved)

At each of n = 9, 10, 11, 12 the 56 classes take only 38 distinct values, with
5 stable multi-member groups (largest: 10 classes at 5293446 for n = 12; full
list in the report). Persistence across four consecutive n plus agreement with
SCOPE-FAIL-20260907-022's independent vectors supports, but does not prove,
genuine Wilf-equivalences; no bijection is claimed here. (SCOPE-FAIL-036's
single-pair equality uses labellings outside the unordered-canonical frame
and is neither confirmed nor contradicted by this table.)

## 5. Replay instructions

gcc -O2 -o /tmp/enum2 output/artifacts/enumerator.c
/tmp/enum2 12 1 2 3 4 4 3 2 1            # expect 0
/tmp/enum2 12 1 2 3 4 1 3 2 4            # expect 6129840
cat output/artifacts/reps.txt | xargs -P 32 -I{} bash output/artifacts/worker.sh 12 "{}"
python3 output/artifacts/symmetry.py     # expect 56 classes / 276 pairs covered
python3 output/artifacts/verify.py 8 "1,2,3,4" "4,3,2,1"   # expect 1764
