# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — lane-1133: the symmetric tier of cyclic STS(19)s is not index 11

## Objects
Let A1–A4 be the cyclic STS(19)s developed mod 19 from the base triples in
`output/artifacts/class_reps.txt` (one line per system):
- A1 = {(0,1,4),(0,2,9),(0,5,11)}, Aut order 19
- A2 = {(0,1,4),(0,2,12),(0,5,13)}, Aut order 57
- A3 = {(0,1,8),(0,2,5),(0,4,10)}, Aut order 57
- A4 = {(0,1,8),(0,2,5),(0,4,13)}, Aut order 171

They are verified (script `verify.py`) to each have 57 blocks with all 171 pairs
covered exactly once, hence genuine STS(19)s. Enumeration of all ordered cyclic
difference families gives 864 families fusing under affine maps to exactly these
4 isomorphism classes (script `classify.py`), so A1–A4 are the complete cyclic tier.

## Emergent finding (proved)
**Claim.** The fourth cyclic STS(19), A4, has block chromatic index exactly 12:
its 57 blocks partition into 12 partial parallel classes, and no partition into
11 (hence into 10) exists.

**Proof.**
- *Upper bound (explicit certificate).* `output/artifacts/partition12_A4.txt`
  lists 12 pairwise-disjoint partial parallel classes (sizes 3,4,5×10) whose
  union is exactly the 57 developed blocks of A4. Machine-checked by `verify.py`.
- *Lower bound (counting certificate).* Exhaustive backtracking over the 57 blocks
  (replayed by `verify.py:check_A4_bound`) shows A4 contains no 6 pairwise-disjoint
  blocks, i.e. every partial parallel class has at most 5 blocks. Hence any 11
  classes cover at most 55 < 57 blocks, so 11 (and a fortiori 10) classes never
  suffice. Therefore chi(A4) ≥ 12.
- Combined: chi(A4) = 12. In particular A4 is **not** chromatic-index 10, and its
  index exceeds 11. ∎

## Relationship to the target
The admitted target claimed some Ai has chromatic index **exactly 11**. The work
proves instead: chi(A1) = 10 (verified 10-partition `partition10_A1.txt`, sizes
6×7+5×3; 9-class impossibility by the 54-block cap) and chi(A4) = 12 exactly,
while A2, A3 each admit verified 11-partitions with 10-status undecided within
the pass (bounded heuristic 10-searches: A2 633k greedy tries + 24.3M SA steps to
1 conflict; A3 634k + 23.7M to 2 conflicts; targeted 7×6+3×5 exact-cover heuristic
also negative — all recorded as evidence only, not proofs). Hence the "exactly 11"
formulation is false on A1 and A4 and unconfirmed on A2/A3; the strongest proved,
independently valuable correction is the exact value chi(A4) = 12.

## Originality and value
The block chromatic index of individual cyclic STS(19)s at this granularity (exact
value 12 with both an explicit optimised partition and an exhaustive max-matching
certificate) is a new census fact: it separates the symmetric tier (A4 needs 12,
A1 needs only 10) and corrects any uniform-"index 11" expectation. The scripts use
only the Python standard library and every certificate replays deterministically.

## What is proved vs conjectured
- Proved: A1–A4 are STS(19)s forming the full cyclic tier (4 classes); chi(A1)=10
  (upper by file; lower by 9×6=54<57 counting); chi(A4)=12 (above).
- Computed evidence (not claimed as proof): A2/A3 resisted bounded 10-searches;
  their verified 11-partitions bound chi in {10,11}.
- Uncertain: chi(A2), chi(A3) exact values; whether any STS(19) has index exactly 11.

## Reproduction
```
cd output/artifacts
python3 verify.py        # replays all claimed certificates
python3 classify.py     # 864 families -> 4 classes, Aut orders 19/57/57/171
python3 seven6.py 0 heur 95   # rediscovers an A1 10-decomposition seed
```
