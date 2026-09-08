# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified census around R(3,4) = 9 with an R(3,5) witness

## Status: CLAIMED (partial theorem — task (a) without DRAT; see Limitations)

## 1. Objects and encoding

Let F_n^(s,t) be the CNF over C(n,2) Boolean variables x_e (True = red edge)
with edges in lexicographic order, var(e) = index(e)+1:

- for each s-set S: clause of negated edge-variables (no red K_s);
- for each t-set T: clause of positive edge-variables (no blue K_t).

DIMACS files (generator `output/artifacts/gen.py` v1.0, edge-lex order):

| file | n vars | n clauses | content |
|---|---|---|---|
| `F9_34.cnf` | 36 | 210 = C(9,3) + C(9,4) = 84 + 126 | F_9^(3,4) |
| `F8_34.cnf` | 28 | 126 = C(8,3) + C(8,4) = 56 + 70 | F_8^(3,4) |
| `F13_35.cnf` | 78 | 1573 = C(13,3) + C(13,5) = 286 + 1287 | F_13^(3,5) |

## 2. Claims

**(a) F_9^(3,4) is UNSAT.** Every red-blue coloring of K_9 contains a red
triangle or a blue K_4. Proved by exhaustive extension over the certified
complete K_8 census: for each of the 17,640 K_8 models and each of the 9
choices of deleted vertex, all 2^8 = 256 completions of the 8 star edges
contain a red K_3 or a blue K_4 — 158,760 restrictions, 40,642,560
completions, all blocked (`ext9.c` v1.0, log `ext9.log`).
Hence R(3,4) <= 9. Together with the K_8 census (which exhibits colorings),
R(3,4) = 9.

**(b) F_8^(3,4) has exactly 17,640 labeled satisfying colorings in exactly
3 isomorphism classes under S_8**, with canonical representatives (lex-min
28-bit edge-lex key), class sizes, automorphism orders, and red-degree
sequences:

| canon key | labeled models | |Aut| | red-degree seq | check |
|---|---|---|---|---|
| `0523a70` | 5040 | 8 | 22223333 | 5040 x 8 = 40320 |
| `0527568` | 10080 | 4 | 22333333 | 10080 x 4 = 40320 |
| `056ba70` | 2520 | 16 | 33333333 | 2520 x 16 = 40320 |

Class sizes sum to 5040 + 10080 + 2520 = 17,640. Completeness is established
by TWO independent C enumerators (`enum8.c`, `enum8b.c`: different edge
orders, opposite branch polarity, different violation tests) whose model
SETS agree exactly, and the one-command verifier rebuilds both from source
and re-checks set equality against the archives.

Representatives as red adjacency matrices (rows 0..7, `.`=diag, 1=red):

Class `0523a70` (|Aut|=8, degseq 22223333):

    00000111
    00001011
    00010001
    00100010
    01000100
    10001000
    11010000
    11100000

Class `0527568` (|Aut|=4, degseq 22333333):

    00001011
    00010101
    00011001
    01100010
    10100100
    01001000
    10010000
    11100000

Class `056ba70` (|Aut|=16, degseq 33333333; the 8-cycle C_8 in red):

    00000111
    00001011
    00010101
    00101010
    01010100
    10101000
    11010000
    11100000

**(c) Explicit (3,5)-free coloring of K_13** (so R(3,5) > 13). Edge-lex
red-bitstring (78 bits, 1 = red):

    000110010010110100000010001000110100110000000001010100100110001000101000111000

Red adjacency matrix (`.` diag, 1 = red, 0 = blue):

    .000110010010
    0.11010000001
    01.0001000110
    010.100110000
    1001.00000101
    11000.0100100
    001000.110001
    0001011.00010
    10010010.1000
    000000001.111
    0010110001.00
    10100001010.0
    010010100100.

Standalone checker `check13.c` (no solver calls) enumerates all C(13,3) = 286
triples and all C(13,5) = 1287 quintuples: 0 red triangles, 0 blue K_5s
(`check13.log`: WITNESS_OK). The verifier additionally confirms the witness
satisfies all 1573 clauses of `F13_35.cnf`.

## 3. Evidence and replay

One command (needs only gcc + python3 stdlib; OpenMP optional):

    python3 output/artifacts/verify.py

It rebuilds every C tool from source and re-runs the full pipeline in ~10 s
wall (dominated by the OpenMP canonical-label rerun): DIMACS header checks,
all-17,640-models-satisfy-F8, two-enumerator set agreement, from-source
re-enumeration with set comparison, 40.6M-completion extension UNSAT,
witness clause + brute-force checks, from-source `check13` rerun,
from-source `canon8` rerun with byte-identical `classes8.txt`, and a pure-
Python recheck (all 40,320 perms) of canonicity, pairwise non-isomorphism,
automorphism orders, degree sequences, and orbit-stabilizer
(class_size x |Aut| = 40,320). Result on the research machine: 23/23 PASS,
`RESULT ALL_OK`. SHA-256 checksums: `output/artifacts/SHA256SUMS`.

## 4. Methods (auditable detail)

- Enumeration: DFS over edges in fixed order with forward checking (only
  clauses whose maximum edge is the new edge can become newly violated).
  `enum8.c`: lex order, red-first, precomputed per-edge triple/quad tables
  (1,420,332 nodes, 17,640 models). `enum8b.c`: reverse order, blue-first,
  direct adjacency-matrix violation scan (604,159 nodes, 17,640 models).
- Canonical labeling: lex-minimum of the 28-bit edge-lex vector over all
  40,320 vertex permutations (OpenMP-parallel, `canon8.c`); |Aut| = number of
  fixing perms. Independently rechecked in pure Python in `verify.py`.
- UNSAT: extension argument (`ext9.c`): any K_9 coloring restricts to a K_8
  model on the census list; all 256 star completions at every deletion site
  are directly blocked. Sound because census completeness is certified by the
  two agreeing enumerators plus from-source reruns.
- K_13 witness: deterministic seeded greedy local search (`sa13.c`,
  cost = 10 x #red-K3 + #blue-K5, exhaustive best-flip + seeded kicks);
  verified solver-independently.

## 5. Limitations (honest)

1. **No DRAT proof / no drat-trim check.** The assigned audit plan required a
   DRAT UNSAT certificate for F_9^(3,4); this environment has no SAT solver
   and no package installer, so the UNSAT certificate delivered is the
   machine-checked extension argument, not DRAT. Task (a) is proved, but not
   in the required proof format.
2. **No SAT-solver cross-check.** Enumeration used bespoke backtrackers, not
   MiniSat/CaDiCaL; solver-version/seed/runtime/proof-size fields cannot be
   reported. Mitigation: two structurally independent enumerators + pure-
   Python verifier logic + from-source rebuild-everything replay.
3. **Isomorphism via brute force, not nauty/bliss.** The S_8 group (40,320
   perms) is small enough that direct lex-min search is exact and was
   cross-checked in Python; no canonical-label library was available.
4. **Values R(3,4) = 9, R(3,5) = 14 are classical** (Greenwood–Gleason 1955);
   novelty is the certificate/census packaging, not the numbers. The K_13
   witness shows R(3,5) > 13 but does not touch the R(3,5) = 14 upper bound.

## 6. Originality statement

Classical literature proves the Ramsey values existentially; the recent
verified-Ramsey work targets larger R(3,8)/R(3,9) via SAT+CAS; none publishes
a complete labeled/isomorphism census of (3,4)-free K_8 colorings with
canonical representatives and automorphism orders plus a replay-verifiable
artifact bundle of this form. The numeric census values above (17,640; 3;
5040/10080/2520; 8/4/16) are computed evidence, clearly separated from the
machine-checked proof components (extension UNSAT, brute-force witness
check, orbit-stabilizer identities).
