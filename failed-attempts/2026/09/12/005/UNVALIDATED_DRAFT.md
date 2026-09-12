# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified dual exact census for Av(1324,1234) vs Av(1324,1243) to n=14, with Fekete growth lower bounds and insertion-state-growth obstruction

## 1. Objects and notation

Classical permutation patterns in one-line notation. Av(B) = permutations with no order-isomorphic
subsequence matching any pattern in B. Growth rate gr(C) = lim |C_n|^{1/n} (exists: Arratia's theorem
for these classes; Fekete's lemma applies via sum-closure, see section 4).

- Class A = Av(1324, 1234), counts a_n.
- Class B = Av(1324, 1243), counts b_n.

## 2. Exact census (theorem: table values)

n : a_n, b_n:
0: 1, 1. 1: 1, 1. 2: 2, 2. 3: 6, 6. 4: 22, 22. 5: 90, 90.
6: 396, 394. 7: 1837, 1806. 8: 8864, 8558. 9: 44074, 41586.
10: 224352, 206098. 11: 1163724, 1037718. 12: 6129840, 5293446.
13: 32703074, 27297738. 14: 176351644, 142078746.

Agreement a_n = b_n for n<=5; strict separation a_n > b_n for every 6<=n<=14.
Ratio a_n/b_n strictly increasing across the window:
1.0051, 1.0172, 1.0358, 1.0598, 1.0886, 1.1214, 1.1580, 1.1980, 1.2412.

## 3. Proof of correctness (independent engines + anchors)

Engine 1 (output/artifacts/enum_sep.c): min-insertion trees, one SEPARATE recursion per class.
Insert new global minimum 1 at each gap; parent avoids implies child avoids iff no forbidden-pattern
occurrence uses the new-min position (it must play value-role 1). Exact order-isomorphism test on all
index 4-tuples containing the new position. Separate trees are essential: a shared tree with per-class
pruning overcounts (documented false 93/93 at n=5 vs true 90/90).

Engine 2 (output/artifacts/enum_max.c): max-insertion trees, separate per class. Insert new global
maximum m+1 at each gap (value-role 4): 1324/1234 need a 132-/123-triple strictly left of the gap;
1243 needs indices t1<t2<gap<t3 with values v1<v2<v3. Different element, role logic, traversal.

Engine 3 (output/artifacts/gen_full.c): second max-insertion implementation (single-file dual run),
cross-agreed byte-identically with Engine 2 at n=12 and n=13 (GEN12_AGREE, GEN13_AGREE), then run to
n=14 (42s) producing the n=13/14 rows.

Further checks:
- Independent left-to-right DFS engine (output/artifacts/indep2.c) agrees to n=9: 44074/41586.
- Full Heap-algorithm brute force agrees at n=8 (8864/8558) and n=6 (396/394); n=6,7,8 match the
  admission-recorded anchors (396-vs-394, 1837-vs-1806, 8864-vs-8558).
- output/artifacts/verify14.py re-checks anchors, strict separation, widening ratios, exact-integer
  supermultiplicativity spot checks ((6,6),(6,8),(7,7),(12,2),(13,1)), and Fekete bounds (VERIFY14_OK).

## 4. Certified Fekete growth lower bounds (lemma)

Each of 1324, 1234, 1243 is sum-decomposable (1324 = 1 (+) 324 after relabelling; 1234 layered;
1243 = 1 (+) 132 after relabelling). Hence both classes are sum-closed: direct sums of avoiders avoid
all three patterns, so a_{m+n} >= a_m*a_n and b_{m+n} >= b_m*b_n (spot-verified as exact integer
inequalities in verify14.py). By Fekete's lemma, gr = sup_n c_n^{1/n}, so from the exact n=14 integers:
gr(Av(1324,1234)) >= 176351644^{1/14} = 3.881746...,
gr(Av(1324,1243)) >= 142078746^{1/14} = 3.822289....
Rigorous one-sided bounds (rounded down: 3.8817 and 3.8222).

## 5. Insertion-state-growth obstruction (lemma)

Max-insertion gap-validity profiles over the exactly enumerated avoiders:
- distinct gap masks at n=8: class A 8, class B 65 (with 832 dead ends);
- depth-2 future-equivalence type counts at n=6,7,8: A: 36,57,85; B: 108,258,608 (no stabilization);
- max active slots = n+1 at every n<=9 for both classes.
A computed obstruction datum (not a non-regularity proof): no small finite-state insertion-encoding
quotient presents itself for class B in this window, which is why the finite-DFA upper-bound route
needed for disjoint spectral enclosures is unavailable.

## 6. Relation to the target

The target claimed gr(A) < gr(B) via disjoint DFA enclosures. This finding does NOT prove the target
(finite counts cannot decide exponential rates); it proves the certified one-sided bounds above and
documents that the finite data uniformly favors the reverse direction (a_n > b_n, 6<=n<=14, widening
1.005->1.241). It is the survey's stated valuable-partial-target form (brute-force ledger to n>=12
plus rigorous growth-rate interval), reported as EMERGENT_FINDING: original, independently valuable
structural/enumerative material discovered while the blocked target was pursued, not a substitute claim.

## 7. Replay

gcc -O2 -o gen_full output/artifacts/gen_full.c && ./gen_full 14    # full table to n=14
gcc -O2 -o enum_max output/artifacts/enum_max.c && ./enum_max 13    # cross-check to n=13
gcc -O2 -o enum_sep output/artifacts/enum_sep.c && ./enum_sep 12    # cross-check to n=12
gcc -O2 -o indep2 output/artifacts/indep2.c && ./indep2 9 0 && ./indep2 9 1
python3 output/artifacts/verify14.py   # VERIFY14_OK
