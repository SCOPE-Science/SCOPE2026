# Two inequivalent optimal (14,6,7) constant-weight codes of size 42

## Context

`A(n,d,w)` is the maximum size of a binary length-`n` constant-weight-`w`
code with minimum Hamming distance at least `d`.
The Brouwer table entry `A(14,6,7) = 42` records only the value plus one
explicit 42-word construction (`a14.6.7.42`).
No count of inequivalent optima, stabilizer, or distance-distribution data
is recorded there. The exact number `N*` of `S_14`-orbits of 42-optima is
not determined here.

## Definitions

- Words are binary strings of length 14 and weight 7, equivalently 7-subsets
  of `{0,...,13}`.
- Hamming distance between weight-7 words is even; the condition
  distance `>= 6` is equivalent to Johnson distance `>= 3`, i.e. a 42-clique
  in the Johnson graph `J(14,7)` (`C(14,7) = 3432` vertices).
- Equivalence is coordinate permutation (`S_14` acting on positions);
  the stabilizer is the setwise automorphism group in `S_14`.
- Distance distribution counts unordered pairs by Hamming distance;
  `C(42,2) = 861`.

## Result (certified partial census, conditional)

Conditional on the tabled value `A(14,6,7) = 42`, there are at least two
`S_14`-inequivalent optimal binary constant-weight codes with
`(n,d,w) = (14,6,7)` of size 42:

- **Code A** (`output/artifacts/brouwer42.txt`): the Brouwer-table witness.
  42 words, all weight 7, minimum Hamming distance 6,
  pairwise distance distribution `{6:580, 8:80, 10:181, 12:20}`,
  coordinate-stabilizer order **40**,
  point degrees `[20,20,21(x10),22,22]`.
- **Code B** (`output/artifacts/clique42_1_155.txt`): a second 42-clique.
  42 words, all weight 7, minimum distance 6,
  pairwise distance distribution `{6:580, 8:80, 10:180, 12:21}`,
  coordinate-stabilizer order **720**,
  point degrees `[20,21(x12),22]`.

Codes A and B are not carried to each other by any coordinate permutation.

## Proof / evidence (all replayable, stdlib only)

1. Witness files `output/artifacts/brouwer42.txt` and
   `output/artifacts/clique42_1_155.txt` each contain 42 distinct binary
   length-14 weight-7 words (SHA-256 below). Independent recount confirms
   all `861` pairwise Hamming distances are `>= 6` with the distributions
   stated above (each sums to 861).
2. `output/artifacts/stab_check.py` verifies size/weight/min-distance,
   distance distributions, and stabilizer orders via exact backtracking
   under two branching orders (agreement required) plus group-closure and
   identity checks. Output: `|Stab| = 40` (A), `|Stab| = 720` (B).
   An independent recount confirms 40 and 720.
3. `output/artifacts/iso_test.py` is an exact `S_14` isomorphism search:
   A-vs-B returns False under both variable orders; the A-vs-A control
   returns True. The distinct distance distributions already separate the
   orbits independently, since Hamming distance is `S_14`-invariant.
4. `output/artifacts/delsarte_bound.py` is an exact-rational Johnson-scheme
   Delsarte LP. Its optimum is **197, not 42**; the script asserts the
   audited weak bound `A(14,6,7) <= 197`. Optimality of size 42 is therefore
   cited from the external Brouwer table, not proved here. Both witnesses
   show 42 is attainable, so conditional on the tabled value, both are
   optimal and inequivalent.

## Limitations

- The full orbit count `N*` is not determined; only the lower count
  `K >= 2` is certified.
- The upper bound `A(14,6,7) = 42` is assumed from the Brouwer table; the
  in-artifact Delsarte LP replay gives only `<= 197`.
- Code B was found by heuristic max-clique search whose script was removed;
  its existence is certified by the verifier, not by search replay.
- Stabilizer/isomorphism checks are custom exact backtracking (two orders
  plus closure/self controls), not nauty.

## Reproducibility

```
python3 output/artifacts/delsarte_bound.py   # weak bound <= 197
python3 output/artifacts/stab_check.py        # verification + stabilizers
python3 output/artifacts/iso_test.py          # inequivalence
```

SHA-256:
- `brouwer42.txt`: `a5d8bc48b8339caeb28060c5d438a03027be58ed8fe7aaaea139d78363bbfcc1`
- `clique42_1_155.txt`: `6b6422a4a200d3906ed829f070e439861600fb21ae9121dc49ee9b81eb15bd05`
- `stab_check.py`: `e33af7b18f0b02a6b03c3ee46f309cf8b73404e595e04c0b788f01842178e735`
- `iso_test.py`: `80eeee6b2c1551791983abb2e7f0138f7e56e3b4d0cd77a9006b80bcf709b165`
- `delsarte_bound.py`: `fb032435bdd79b6a1215fc59900e5615bf9f2143c6878303dde5a0851ceaf2c8`

## References

- Brouwer et al., Bounds for binary constant weight codes (Andw table),
  `https://www.win.tue.nl/~aeb/codes/Andw.html`; construction file
  `https://www.win.tue.nl/~aeb/codes/cwc/d6/a14.6.7.42`.
- P. R. J. Ostergard, Classification of binary constant weight codes,
  IEEE Trans. Inform. Theory 56 (2010) 3779-3785,
  DOI 10.1109/tit.2010.2050922.
- E. Agrell, A. Vardy, K. Zeger, Upper bounds for constant-weight codes,
  IEEE Trans. Inform. Theory 46 (2000) 2373-2395.
- B. G. Kang, H. K. Kim, P. T. Toan, Improved linear programming bounds on
  sizes of constant-weight codes, arXiv:1108.5104.
